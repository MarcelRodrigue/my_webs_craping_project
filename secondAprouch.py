import requests
import lxml
from bs4 import BeautifulSoup
#target url
url = 'https://journal.un.org/en/new-york/meeting/officials/97250ac0-e677-4b83-80b5-08da00cb1115/2022-08-01/statements'
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'}
#getting the data
def extract():
 r = requests.get(url, headers = headers)
 print(r.status_code)
 soup = BeautifulSoup(r.content, 'html.parser')
 return soup

def transform(soup):
    divs =soup.find_all('a') 
    return divs


c = extract()
print(transform(c))