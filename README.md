# percona-slides-downloader
Download Percona Live's all slides: just input Percona Live index page, and this program will download all slides!
It requires Python 3.6+ 

# Install
```
python3 -m pip install requests docopt beautifulsoup4
git clone https://github.com/leafonsword/percona-slides-downloader.git
cd percona-slides-downloader/
```
# Usage:
    ./percona-slides-downloader.py -u <url> [-t <threads>]

# Options:
    -u <url>, the web page
    -t <threads>, optional, default to 100

# Examples:
```
./percona-slides-downloader.py -u 'http://www.percona.com/live/17/resources/slides'
```
above command will download percona live 2017's all slides into dir ./percona_live_17_slides/

