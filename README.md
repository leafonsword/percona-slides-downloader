# percona-slides-downloader
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)  
Download Percona Live's all slides: just input Percona Live index page, and this program will download all slides into a dir!

# Requirements:
Python 3.6+

# Install
```
python3 -m pip install requests docopt beautifulsoup4 lxml
git clone https://github.com/leafonsword/percona-slides-downloader.git
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

```
11:42 $ ls -l ./percona_live_2017_slides/
total 41176
-rw-r--r--  1 gf  wheel        0  3 14 11:40 12_Step_tuning_program_Janis_Griffin.pdf
-rw-r--r--  1 gf  wheel        0  3 14 11:41 170425-TUE-%20ScaleDB%20Tech%20Preso_0.pdf
-rw-r--r--  1 gf  wheel   407750  3 14 11:41 2017-04-25_plsc_two_bugs_almost_brought_down_b_com_v1.0.pdf
-rw-r--r--  1 gf  wheel   407750  3 14 11:40 2017-04-25_plsc_two_bugs_almost_brought_down_b_com_v1.0_0.pdf
-rw-r--r--  1 gf  wheel  1048454  3 14 11:41 2017-04-26_plsc_mysql-mariadb_parallel_replication-inventory_use-case_and_limitations_v1.0.pdf
-rw-r--r--  1 gf  wheel   568652  3 14 11:41 2017-04-27_plsc_deal_with_lag_v0.3.pdf
-rw-r--r--  1 gf  wheel        0  3 14 11:40 2017-04-27_plsc_mysql_parallel_replication-logical_clock_details_v1.0.pdf
-rw-r--r--  1 gf  wheel        0  3 14 11:40 2017.%204.%2026%20-%20Percona%20Live%202017%20-%20MyFlashSQL%20%28Sang-Won%20Lee%29.pdf
-rw-r--r--  1 gf  wheel        0  3 14 11:40 A%20brief%20introduction%20of%20TiDB%20%28Percona%20Live%29.pdf
-rw-r--r--  1 gf  wheel        0  3 14 11:40 Aurora%20deep%20dive%20-%20Percona%20Live%202017.pdf
-rw-r--r--  1 gf  wheel   135885  3 14 11:40 Automating_MySQL_in_AWS_Cloud.pdf
...
```
