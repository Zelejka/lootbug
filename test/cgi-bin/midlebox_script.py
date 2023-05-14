import sqlite3
import json
import urllib.parse
import os


# Получение параметров из HTTP-запроса
query_string = os.environ.get("QUERY_STRING", "")
query_dict = urllib.parse.parse_qs(query_string)
_id = query_dict.get("id", [""])[0]


html = ''

# Установка заголовка Content-type для вывода HTML
print('Content-type: text/html\n')

# Создание подключения к базе данных SQLite и курсора
# для выполнения SQL-запросов
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stocks'")
result = cursor.fetchone()

if not result:
    cursor.execute('''CREATE TABLE stocks
             (id SERIAL PRIMARY KEY,
              name text,
               comment text,
               img text,
                price int)''')

# Получение количества записей в таблице stocks
cursor.execute('SELECT COUNT(*) FROM stocks;')
count = cursor.fetchone()[0]

# Итерация по записям в таблице и формирование HTML-кода
for j in range(count):
    # Получение данных для текущей записи
    cursor.execute('SELECT img, name, comment, price FROM stocks WHERE id = ?', (j+1,))
    img, name, comment, price = cursor.fetchone()

    # Преобразование данных в строки и замена кавычек для корректной вставки в HTML
    img = str(img).replace("'", "")
    name = str(name).replace("'", "")
    comment = str(comment).replace("'", "")
    price = str(price).replace("'", "")

    # Формирование HTML-кода для текущей записи
    html += (f'''
        <div class="projeckt">
            <img src="img/{img}.png" alt="" class="img">
            <div class="textonprojeckt">
                <p class='name'><b>{name}</b></p>
                <p class='comment'>{comment}</p>
                <p class='price'>{price}</p>
                <p>sas id-{_id}</p>
            </div>
        </div>
    ''')

y = json.dumps(html)
print(y)

# Закрытие соединения с базой данных
connection.close()
