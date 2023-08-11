db.py:
```py
import sqlite3

class DB:
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()

    def do(self, sql, values=()) -> None:
        self.cursor.execute(sql, values)
        self.connect.commit()

    def read(self, sql, values=()) -> tuple:
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()

    def add_second_name(self, values: list | tuple | set) -> None:
        self.do('INSERT INTO second_name (name, url, first_name_id) VALUES (?, ?, ?)', tuple(values))

    def add_data(self, values: list | tuple | set) -> None:
        self.do(f'INSERT INTO data (product, kcal, protein, fat, carbonates, url, second_name_id) VALUES (?, ?, ?, ?, ?, ?, ?)', tuple(values))

```
main.py:
```py
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

```
test1.py:
```py
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <div class="example">Элемент 1</div>
        <div class="example">Элемент 2</div>
        <div class="example">Элемент 3</div>
        <div class="example">Элемент 4</div>
        <div class="example">Элемент 5</div>
        <div class="example">Элемент 6</div>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Находим все элементы с классом "example"
elements = soup.find_all(class_="example")

# Получаем первый элемент
first_element = elements[0]
print(first_element.text)  # Вывод: Элемент 1

# Получаем шестой элемент
sixth_element = elements[5]
print(sixth_element.text)  # Вывод: Элемент 6

```
test2.py:
```py

```
