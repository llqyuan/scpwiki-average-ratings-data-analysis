# SCP wiki data analysis project

Compare how well-received each author of interest is to the average author on the site. Average ratings were obtained by web scraping. When possible, ratings for specific authors were obtained manually from their dedicated author pages. Data was analyzed using R.

## Technologies

General:
* Python 3.7.3

pip3 libraries:
* beautifulsoup4 4.9.3
* certifi       2020.12.5
* chardet       4.0.0    
* idna          2.10     
* pip           18.1     
* pkg-resources 0.0.0    
* requests      2.25.1   
* setuptools    40.8.0   
* urllib3       1.26.3

## Running the script

`python3 general_data.py`. Data will be saved to "data.txt". This data can be read and analyzed in R.
