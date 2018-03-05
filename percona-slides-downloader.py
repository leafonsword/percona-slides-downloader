#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Download Percona Live's all slides: just input Percona Live index page, and this program will download all slides
Requires Python 3.6+ 
Downloaded slides will be saved on current dir's subdir like this: percona_live_XX_slides

Install:
    python3 -m pip install percona-slides-downloader

Usage:
    ./percona-slides-downloader.py -u <url> [-t <threads>]

Options:
    -u <url>, the web page
    -t <threads>, optional, default to 100

Examples:
    ./percona-slides-downloader.py -u 'http://www.percona.com/live/17/resources/slides'
'''


import os
import logging
from concurrent import futures
from bs4 import BeautifulSoup
import requests
from docopt import docopt


__author__ = '刀尖红叶'
__version__='0.1'

# config loggging
logging.captureWarnings(True)
log_file=os.path.realpath(__file__).rstrip('.py') + '.debug.log'
logging.basicConfig(filename=log_file,level=logging.DEBUG,format='%(levelname)s: %(asctime)s, %(filename)s, line:%(lineno)d: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
columns, rows = os.get_terminal_size()
extra_length = columns - 47
logging.debug('-' * extra_length)      

# get args
args = docopt(__doc__, version=__version__)
url_index = args['-u']
#logging.debug(f'args:{args})')

# def var
workers = 100 if not args['-t'] else args['-t']
url_prefix = 'http://www.percona.com'
href_c = set()
year = '20' + url_index.split('/')[4]
dirname = f'percona_live_{year}_slides'
os.system('mkdir -p ./{dirname}/')


def get_session_url(url):
    global href_c
    html = requests.get(url, timeout=10).text
    soup = BeautifulSoup(html, "lxml")
    list_a = soup.find_all('a')
    for link in list_a:
        if link.get('href',None):
            if '/live/' in link['href'] and '/sessions/' in link['href']:
                href_c.add(url_prefix+link['href'])

        if link.get('title',None):
            if link['title'] == 'Go to next page':
                get_session_url(url_prefix+link['href'])

def get_slide(url):
    html = requests.get(url, timeout=10).text
    soup = BeautifulSoup(html, "lxml")
    url_pdf = soup.object['data']
    file_name = url_pdf.split('/')[-1]
    with open(f'./slides/{file_name}', 'wb') as f:
        f.write(requests.get(url_pdf, timeout=10).content)

# main entrance
if __name__ == '__main__':
    get_session_url(url_index)
    #logging.debug(f'href_c: {href_c}, len: {len(href_c)}')
    
    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for future in executor.map(get_slide, href_c):
            pass
    
#    logging.debug(f'href_c:{href_c}')
