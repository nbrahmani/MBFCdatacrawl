import csv
import requests
from bs4 import BeautifulSoup

main_url = 'https://mediabiasfactcheck.com/filtered-search/?pg='
pages = 49
biases = []

for i in range(pages+1):
    print(i)
    url = f'{main_url}{i}'
    html = requests.get(url)
    html = html.text
    data = BeautifulSoup(html, 'lxml')
    data = data.html
    tables = data.find_all('table')
    rows = tables[1].find_all('tr')

    # Store header
    temp = []
    for x in rows[0].find_all('th'):
        temp.append(x.text.strip())

    biases.append(temp)

    for row in rows[1:]:
        temp = []
        for td in row.find_all('td'):
            temp.append(td.text.strip())
        biases.append(temp)

with open('data.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(biases)
