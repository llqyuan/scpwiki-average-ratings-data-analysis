# SCP wiki data analysis project

Compares how well-received each author of interest is to the average author on the site. Average ratings were obtained by web scraping. When possible, ratings for specific authors were obtained manually from their dedicated author pages. Data was analyzed using R.

## Technologies

General:
* Python 3.7.3

pip3 libraries:
* beautifulsoup4 4.9.3
* requests      2.25.1

## Running the script

`python3 general_data.py`. Data will be saved to "data.txt". This data can be read and analyzed in R.
