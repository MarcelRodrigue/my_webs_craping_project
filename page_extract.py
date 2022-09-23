#depenencies

import requests
from bs4 import BeautifulSoup
import re

from secondAprouch import extract

#target url
url = 'https://www.un.org/en/conferences/npt2020/information-for-participants'
#custum header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
my_target_url= []
   #make get request
response = requests.get(url, headers = headers)
def xtract():

    #extract the content
    content= BeautifulSoup(response.text, 'html.parser')
    for tag in content.find_all('a', {'href': re.compile("statements")}) and content.find_all('a', {'href': re.compile("2022-08-01")}) :
        print(tag)
    for tag1 in content.find_all('a', {'href': re.compile("statements")}) and content.find_all('a', {'href': re.compile("2022-08-02")}) :
        print(tag1)    
    for tag2 in content.find_all('a', {'href': re.compile("statements")}) and content.find_all('a', {'href': re.compile("2022-08-03")}) :
        print(tag2)
    for tag3 in content.find_all('a', {'href': re.compile("statements")}) and content.find_all('a', {'href': re.compile("2022-08-04")}) :
        print(tag3)        
    for tag4 in content.find_all('a', {'href': re.compile("statements")}) and content.find_all('a', {'href': re.compile("2022-08-04")}) :
        print(tag4)    



xtract()        