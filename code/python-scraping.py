# ```python
import requests

url = "https://www.example.com"
response = requests.get(url)
html_content = response.content
# ```


# ```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_content, "html.parser")
title = soup.title.string
print(title)
# ```

