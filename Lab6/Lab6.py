from http.server import HTTPServer, CGIHTTPRequestHandler
httpd = HTTPServer(('', 8000), CGIHTTPRequestHandler)
print('Server started on http://localhost:8000')
httpd.serve_forever()

