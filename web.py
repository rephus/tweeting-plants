#http://flask.pocoo.org/
from flask import Flask, jsonify, render_template, request
import json
import time
from db.action import Action
from db.sensor import Sensor

app = Flask(__name__)

action = Action()
sensor = Sensor()

@app.route("/")
def hello():
    return render_template('stats.html')

@app.route("/action/all")
def action_all():
    start = time.time()
    actions = action.all()
    print "Parsing {} actions".format(len(actions))
    json = []
    for a in actions:
      j = {
        "id": a[0],
        "timestamp": a[1],
        "action": a[2],
        "category": a[3],
        "content": a[4]
      }
      json.append(j)
      
    return jsonify({
      "count":len(json), 
      "results":json,
      "time": int(time.time()- start)
    })
  
@app.route("/sensor/all")
def sensor_all():
    start = time.time()
    sensors = sensor.all()

    maxi = int(request.args.get('max'))
    print "Parsing {} actions, max {}".format(len(sensors),maxi)
    json = []
    for a in sensors:
      j = {
        "id": a[0],
        "timestamp": a[1],
        "datetime": a[2],
        "temperature": min(a[3],maxi),
        "humidity":min(a[4],maxi),
        "light": min(a[5],maxi)
      }
      json.append(j)
      
    return jsonify({
      "max": maxi,
      "count":len(json), 
      "results":json,
      "time": int(time.time()- start)
    })
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)