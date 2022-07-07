from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import steppercontrol

#curl -X POST http://localhost:8085 -H "Content-Type: application/json" -d '{"direction":"backwards", "distance":5}'


class TestPage(BaseHTTPRequestHandler):

    def do_Post(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body)
        steppercontrol.stepforward()

server = HTTPServer(("localhost", 8085),TestPage)


try:
    server.serve_forever()
except KeyboardInterrupt:pass