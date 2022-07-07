import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import steppercontrol


# Simple http server to receive commands and then call the Stepper Controller to move motor forward or backwards a given number of steps.
# Request looks like this:
# curl -X POST http://localhost:8085 -H "Content-Type: application/json" -d '{"direction":"backward", "distance":5, "motor":"alt"}'
# Stepper motors are dumb, Polar software will need to continue sending commands until it is lined up correctly

class TestPage(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            bytes("<body><p>This is just a test page to see if the server is working.</p></body>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        result = json.loads(body)
        print(result)
        if result['direction'] == "forward":
            print("move forward")
            steppercontrol.stepforward(result['distance'],result['motor'])
        if result['direction'] == "backward":
            print("move backward")
            steppercontrol.stepbackward(result['distance'], result['motor'])


server = HTTPServer(("localhost", 8085), TestPage)

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
