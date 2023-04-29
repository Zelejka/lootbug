import sqlite3

img = 'img'

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute('SELECT COUNT(*) FROM stocks;')
count = cursor.fetchall()
count = str(count)
res_cou = count.replace(",", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "")
res_cou = (int(res_cou))
for j in range(res_cou):
    cursor.execute(f'select name from stocks where id = {j+1};')
    name = cursor.fetchone()
    name = str(name)
    name = name.replace(",", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "")
    cursor.execute(f'select comment from stocks where id = {j+1}')
    comment = cursor.fetchone()
    comment = str(comment)
    comment = comment.replace(",", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "")
    cursor.execute(f'select price from stocks where id = {j+1}')
    price = cursor.fetchone()
    price = str(price)
    price = price.replace(",", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "")
    print(f'''
        <div class="projeckt{j+1}">
            <img src="img/{img}" alt="">
            <p><b>{name}</b></p>
            <p>{comment}</p>
            <p>{price}</p>
        </div>
    ''')
connection.close()
