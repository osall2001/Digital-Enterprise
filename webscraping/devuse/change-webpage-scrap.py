#!/bin/bash
#
#
################################ Read Me ##########################################
#
#Better web scraping in Python with
#Selenium (pip install Selenium)
#Beautiful Soup (pip install BeautifulSoup4) - -bs4
#pandas
#
# https://medium.freecodecamp.org/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251
# https://www.pythonforbeginners.com/python-on-the-web/beautifulsoup-4-python/
#
#/Documents/Digital-Enterprize/webscraping$ python webtext-scrapingrev1.py
#
#Beautiful Soup is a Python library for pulling data out of HTML and XML files.
#
#################################################################################

print ("""



        /((((((\\\\ \n
=======((((((((((\\\\\ \n
     ((           \\\\\\\ \n
     ( (*    _/      \\\\\\\ \n
       \    /  \      \\\\\\________________ \n
        |  |   |       </                  ((\\\\ \n
        o_|   /        /                      \ \\\\    \\\\\\\ \n
             |  ._    (                        \ \\\\\\\\\\\\\\\\ \n
             | /                       /       /    \\\\\\\     \\ \n
     .______/\/     /                 /       /         \\\ \n
    / __.____/    _/         ________(       /\ \n
   / / / ________/`---------'         \     /  \_ \n
  / /  \ \                             \   \ \_  \ \n
 ( <    \ \                             >  /    \ \ \n
  \/     \\_                           / /       > ) \n
          \_|                         / /       / / \n
                                    _//       _// \n
                                   /_|       /_| \n


██╗    ██╗███████╗██████╗     ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗
██║    ██║██╔════╝██╔══██╗    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝    ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝

 Knowledge Digestion Summarizer - Scraping List for Publishing and Graphics Creation

""")

#################################################################################

print ('######################## Import Module Library ########################')

# soup create - from unstructure to structured
import os, sys, re
from bs4 import BeautifulSoup
import urllib3
import requests

# data structured
import pandas as pd
from tabulate import tabulate   # Pretty-print tabular data in Python,tabulate output in the terminal.
import datetime
import csv

print ('######################## Reading File or URL ##################################')

# url = 'https://www.forbes.com/sites/briannawiest/2018/02/26/13-difficult-things-highly-successful-people-learn-to-do-young/#785b15df300f'
# url = 'http://time.com/5408514/breast-cancer-prevention/'
# url = 'http://fortune.com/2018/10/01/ai-data-security-mpw/'
# url = 'http://fortune.com/2017/10/23/influential-websites/'
# url = "https://hackspirit.com/28-simple-mindful-practices-rewire-brain-focused-present/"
# url = 'https://www.recruiter.com/i/how-to-harness-data-science-to-boost-your-hr-and-benefits-strategy/?sf199835796=1'
# url = 'http://therealtimereport.com/2018/08/10/5-industries-research-new-investment-opportunities/'
url = 'https://www.forbes.com/sites/kevinkruse/2016/01/20/15-surprising-things-productive-people-do-differently'
#file_to_soup = url

print ('######################### Creating Soup 1 #############################')

## Using HTTP Client
http = urllib3.PoolManager()    #HTTP Client
response = http.request('GET', url)
http_to_soup = response.data.decode('utf-8')


### Input to BS4 either file or http URL
soup = BeautifulSoup(http_to_soup, 'html.parser')
#print (soup)
print (soup.prettify())
#print (soup.text)


print ('################## Search Soup for Your Interest ######################')

############# Syntax dictionary

### Find with matching regex
# s_regex = soup.find_all(re.compile("^b"))

### Find with tags
# s_tags = soup.find_all('strong')

### Find with class
# s_class = soup.find_all(class_='username u-dir u-textTruncate')
# print (s_class)


print ('############################# SYNTAX USAGE - ##########################')

print ('############ Make Changes Here to Match WebScraping Interest #############')


### Find with tags
s_tags = soup.find('title')
# print (s_tags)
print (s_tags.get_text())

#### printing page source out
print (f'source : {url}')

# s_tags_list = soup.find_all('h2')
s_tags_list = soup.find_all('strong')
# print (s_tags)

i = 1
for item in s_tags_list:
    print (str(i) + '} ' + item.get_text()) #print list items in standard output
    i = i + 1



print ('################## Writing out data to files ###################')

# Write to .CSV , .JSON .dat and Web UI (html and js) read out
# nowdata or archivedata

read_out = '/home/tutamon/Documents/Digital-Enterprize/webscraping/devuse/outfiles/webscraped-nowdata.dat'
url_out = open(read_out, 'a')

title = str(s_tags.get_text())
url_out.write('\n' + '\n' + title + '\n')
url_out.write(f'source : {url}')
content = s_tags_list
i = 1
for item in content:
    str_item = str(str(i) + '} ' + item.get_text() + '\n')
    url_out.write(str_item)
    i = i + 1


print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

 # for k , v in dict_trends.items():
 #     print (dict_trends[k]['date'] , dict_trends[k]['trend'], dict_trends[k]['stats'])
 #     fdrow = dict_trends[k]['date'] + ',' + dict_trends[k]['trend'] + ',' + dict_trends[k]['stats'] + '\n'
 #     fdout.write(fdrow)

print ('####################### Good Bye #######################################')
