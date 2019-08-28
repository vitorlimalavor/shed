import requests
import json
import datetime

version = '32'
headers = {'Accept':'application/json','X-Rundeck-Auth-Token':'fGL1HIlvTcHqNsv6g3jeCDcqGnkMkeUT'}
API_ENDPOINT = "http://172.16.117.130:4440/api/{}/".format(version)

class ListJobs():
      def __init__(self,project):
        j_certo = {}
        url = "project/{}/jobs".format(project)
        r=requests.get(API_ENDPOINT+url,headers=headers).json()
        jdump = json.dumps(r,indent=4)
        jlo=(json.loads(jdump))
        teste=(json.dumps({'HREF': jlo[0]['href']}))
        print(teste)

class RunJob():
    def __init__(self,idjob):
        url = 'job/{}/executions'.format(idjob)
        r=requests.post(API_ENDPOINT+url,headers=headers)
        j_conv = r.json()
        (json.loads(json.dumps(j_conv,indent=4)))



#ListJobs('echo')
#RunJob('fa378b8e-bf0d-4f4d-9aa6-d88510cee642')
#print (date.isoformat())