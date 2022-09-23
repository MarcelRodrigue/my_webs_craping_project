#depenencies

from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
import re


from selenium.webdriver import ChromeOptions
#target url
url = 'https://journal.un.org/en/new-york/meeting/officials/97250ac0-e677-4b83-80b5-08da00cb1115/2022-08-01/statements'
#dynamic sites
options = ChromeOptions()
options.headless = True
driver = webdriver.Chrome(executable_path="C:\Program Files\Authomation\web drivers\chromedriver")
driver.get(url)
def getData() :
 test = BeautifulSoup(driver.page_source, 'lxml')
 test1=test.find_all('a') 
 print('getting all the data')
 print(test1)
 print('all links have been printed')

getData() 