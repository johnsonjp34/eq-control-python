import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import steppercontrol

# Simple http server to receive commands and then call the Stepper Controller to move motor forward or backwards a given number of steps.
# Request looks like this:
# curl -X POST http://localhost:8085 -H "Content-Type: application/json" -d '{"direction":"backward", "distance":5, "motor":"alt", "correctionNumber":1}'
# Stepper motors are dumb, Polar software will need to continue sending commands until it is lined up correctly

listOfCorrection = []


class MotorWebControl(BaseHTTPRequestHandler):
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
        calibration(result['distance'], result['motor'], result['correctionNumber'], result['direction'])


server = HTTPServer(("localhost", 8085), MotorWebControl)

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass


def calibration(distance, motor, correctionNumber, direction):
    listOfCorrection.append(distance)

    if correctionNumber == 1:
        if direction == "forward":
            steppercontrol.stepforward(distance, motor)
        else:
            steppercontrol.stepbackward(distance, motor)

    if correctionNumber > 1:
        # correction number begins with 1. this is the error calculated after each set of pictures
        # correction Factor. This is to see how much the stepper motor is moving the mount
        # Compare the difference between the last entry and the remaining error and divide by the previous motor steps
        correctionFactor = (listOfCorrection[correctionNumber - 2] - listOfCorrection[correctionNumber - 1]) / \
                           listOfCorrection[correctionNumber - 2]
    if direction == "forward":
        steppercontrol.stepforward(distance * correctionFactor, motor)
    else:
        steppercontrol.stepbackward(distance * correctionFactor, motor)
