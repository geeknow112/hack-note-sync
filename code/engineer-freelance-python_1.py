import requests
from bs4 import BeautifulSoup

url = 'https://example.com/python'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
jobs = soup.find_all('div', class_='job')

for job in jobs:
	title = job.find('h2').text
	company = job.find('p', class_='company').text
	location = job.find('p', class_='location').text
	print(title, company, location)
