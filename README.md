# SCP wiki data analysis project

Compares the ratings of entries belonging to different authors on the site. Average ratings were obtained by web scraping. Data was analyzed using R; the report can be found in rdata/report-ratings-of-authors.pdf.

## Technologies

General:
* Python 3.7.3

pip3 libraries:
* beautifulsoup4 4.9.3
* requests      2.25.1

## Running the script

`python3 general_data.py`. Data will be saved to "data.txt". This data can be read and analyzed in R.
