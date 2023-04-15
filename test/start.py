# Импорт библиотек для запуска WEB-сервера
from http.server import HTTPServer, CGIHTTPRequestHandler

# Адрес сервера и номер порта, который он будет "слушать"
server_address = ('', 100)

# Создаем сам WEB-сервер
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

# Старт WEB-сервера
print('start')
httpd.serve_forever()
print('stop')