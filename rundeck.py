from flask import Flask
import requests
import json

app = Flask(__name__)

version = '32'
headers = {'Accept':'application/json','X-Rundeck-Auth-Token':'fGL1HIlvTcHqNsv6g3jeCDcqGnkMkeUT'}
API_ENDPOINT = "http://172.16.117.134:4440/api/{}/".format(version)

@app.route('/')
def RunDasa():
    return 'Rundasa, Run!'

@app.route('/jobs/<projeto>')
def listjobs(projeto):
    url = "project/{}/jobs".format(projeto)
    r = requests.get(API_ENDPOINT + url, headers=headers)
    jlo = (json.loads(r.content))
    teste = (json.dumps(jlo,indent=4))
    return (teste)

@app.route('/runjob/<id>')
def runjob(id):
    data = {"argString":"","loglevel":"DEBUG","asUser":"admin","filter":"","runAtTime":"2019-08-14T16:30:00-0300","options":{"argument":""}}
    url = 'job/{}/executions'.format(id)
    r = requests.post(API_ENDPOINT + url, headers=headers,data=data)
    jlo = (json.loads(r.content))
    teste = (json.dumps(jlo,indent=4))
    return (teste)

if __name__ == "__main__":
    app.run()
