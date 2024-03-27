import http.server
import sqlite3


class CGIHTTPRequestHandler(http.server.CGIHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()


server_address = ('', 8000)
httpd = http.server.HTTPServer(server_address, CGIHTTPRequestHandler)


conn = sqlite3.connect('lab6.db')
cursor = conn.cursor()

print('Server started on http://localhost:8000')
httpd.serve_forever()