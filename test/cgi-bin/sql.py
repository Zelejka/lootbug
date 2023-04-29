import sqlite3

# Создаем соединение с базой данных
conn = sqlite3.connect('db_test.db')

# Получаем курсор для выполнения запросов
c = conn.cursor()

# Создаем таблицу
c.execute('''CREATE TABLE stocks
             (id SERIAL PRIMARY KEY,
              name text,
               comment text,
               img text,
                price int)''')

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()