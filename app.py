from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import logging
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import os
#logFormatStr = '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'

logFormatStr = '[%(asctime)s] p%(process) s:%(lineno)d} %(levelname)s - %(message)s'

logging.basicConfig(format=logFormatStr)
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

app = Flask(__name__)
#jobstores = {
#  'default': MongoDBJobStore(database='apscheduler', collection='jobs', host='localhost', port=27017)
#}

sched = BackgroundScheduler()
sched.start()

def job_listener(event):
    if event.exception:
        print('Houve Algum problema no job')
    else:
        print('Job Executado com sucesso!')

sched.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

def Run():
    return print('teste')

@app.route('/register/')
def reg_job():
    return('registro')

@app.route('/schedule/Run/<data>')
def sche(data):
    #sched.add_job(Run,'date',run_date='2019-08-20 17:23:00')
    sched.add_job(Run,'date',run_date=data)
    return ('Job Schedulado')

app.run(host='0.0.0.0', port='50000')
