print("hello")
#first im iportion my main libraries request to get the data using my http header and beutifull soup for parsimg the data
import requests
import lxml
from bs4 import BeautifulSoup
#now i need to extract the page for that i need a url and a header because by default python scripts will be blocked ny the browser
def extract(page):
            
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
        url = f'https://careers.google.com/jobs/results/?distance=50&page={page}&q='
        r = requests.get(url, headers = headers)
        status = r.status_code
        print(status)
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup

def transform(soup):
    divs =soup.find_all('h2') 
    return divs



c = extract(0)
print(transform(c))






           
     for tag2 in content.find_all('a', {'href': re.compile("statements")}) and content.find_all('a', {'href': re.compile("2022-08-02")}) :
        print(tag2)   
     for tag3 in content.find_all('a', {'href': re.compile("statements")}) and content.find_all('a', {'href': re.compile("2022-08-03")}) :
        print(tag3) 
     for tag4 in content.find_all('a', {'href': re.compile("statements")}) and content.find_all('a', {'href': re.compile("2022-08-04")}) :
        print(tag4)
     for tag5 in content.find_all('a', {'href': re.compile("statements")}) and content.find_all('a', {'href': re.compile("2022-08-05")}) :
        url=tag5(0)
        print(url)
      