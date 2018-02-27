# percona-slides-downloader
Download Percona Live's all slides: just input Percona Live index page, and this program will download all slides!
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
    -t <threads>, optional, default to 2X cpu cores

# Examples:
    ./percona-slides-downloader.py -u 'http://www.percona.com/live/17/resources/slides'
