import requests
from bs4 import BeautifulSoup
from db import DB

sql = DB('db.db')

l = sql.read('SELECT id, url FROM second_name')
for id, url in l:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    soup = soup.find('table', class_='uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed').find('tbody')
    for i in soup.find_all('tr'):
        j = i.find_all('td')
        result = [j[0].get_text()[:-2]]+[float(x.get_text().split(' ')[0].replace(',', '.')) for x in j[1:]]+[f"https://health-diet.ru{j[0].find('a').get('href')}", id]
        print(result)
        sql.add_data(result)
