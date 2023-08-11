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
