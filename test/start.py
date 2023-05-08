from http.server import HTTPServer, CGIHTTPRequestHandler
server_adress = ("", 8000)
httpd = HTTPServer(server_adress, CGIHTTPRequestHandler)
print(True)
httpd.serve_forever()