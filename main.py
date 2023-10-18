from url import *
from db import DB
import requests
import json
from concurrent.futures import ThreadPoolExecutor

fl = float
c = 10

def float(n):
    if n == '' or n is None:
        return 0.0
    else:
        return fl(n.replace('\n', '').replace(' ', '').replace(',', '.'))

def main(f):
    sql = DB(db_config)
    p = 0
    while True:
        url = f'https://www.tablicakalorijnosti.ru/foodstuff/filter-list?format=json&page={p}&limit=800&query=&type=0&brand=&min={f}&max={f + c}&sliderType=0'
        response = requests.get(url)
        # Проверка статуса
        if response.status_code == 200:
            data = response.json()  # Перенос ответа в переменную
            if not data['data']:
                break
            for el in data['data']:
                result = (el['title'], float(el['energy']), float(el['protein']), float(el['fat']), float(el['carbohydrate']), float(el['fiber']), float(el['salt']), float(el['water']), 'https://www.tablicakalorijnosti.ru/produkty/'+el['url'])
                print(result)
                try:
                    sql.do("""INSERT INTO product (user_id, name, kcal, protein, fat, carbohydrate, fiber, salt, water, url) VALUES (1689863728,?,?,?,?,?,?,?,?,?)""", result)
                except Exception as e:
                    print(e)
        else:
            print("Что-то пошло не так:", response.status_code)
            break
        p += 1

if __name__ == "__main__":
    f = list(range(0, 10, c))
    with ThreadPoolExecutor() as executor:
        executor.map(main, f)
    # for fs in f:
    #     main(fs)
