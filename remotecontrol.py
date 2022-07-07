from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import steppercontrol

class TestPage(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<body><p>This is an example web server.</p></body>", "utf-8"))
server = HTTPServer(("localhost", 8080),TestPage)
steppercontrol.stepforward()

try:
    server.serve_forever()
except KeyboardInterrupt:pass