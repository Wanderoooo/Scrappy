import requests
from bs4 import BeautifulSoup
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')

URL = "https://ca.indeed.com/jobs?q=front+end+developer%2C+web+developer&l=British+Columbia&vjk=286f6af6626c8ab9"
driver = webdriver.Chrome()
driver.get(URL)