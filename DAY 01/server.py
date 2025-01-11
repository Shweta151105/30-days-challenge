from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Configuration
PORT = 8080
Handler = SimpleHTTPRequestHandler

# Start the server
with TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()