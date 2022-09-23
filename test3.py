#here was just feeling depressed tried different stuffs out wasn't really working
#got this code from a youtube video

from asyncio import sleep
from requests_html import HTMLSession
session = HTMLSession
url = 'https://github.com/marcelrodriguesymphony?tab=repositories'
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'}
r = session.get(url, headers=headers)
r.html.render(sleep=1, keep_page = True, scrolldown=1)
data = r.html.find('a')

for item in data :
    item = {
        'title':'item.absolute_links'
    }
    print(data)