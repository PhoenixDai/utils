"""
parse a shared onetab shared page to onetab importable url list
"""

import requests
from bs4 import BeautifulSoup


page = requests.get('https://www.one-tab.com/page/abc123')
soup = BeautifulSoup(page.text, 'html.parser')

html = list(soup.children)[2]
body = list(html.children)[3]

a_list = soup.find_all('a')

for a in a_list[2:]:
    print( a.get('href'), '|', a.contents[0])
