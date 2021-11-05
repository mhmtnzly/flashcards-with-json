import time
import os
import json
from datetime import datetime, timedelta
class user:
    def __init__(self,username,time=0,progress=1):
        self.login(username,time,progress)

    def login(self,name,time,progress):
        self.start_time()
        os.chdir('users')
        names_of_file=[name_.split(".")[0]  for name_ in os.listdir('.') if os.path.isfile(name_)]
        if name in names_of_file:
            with open('{}.json'.format(name),'r') as file:
                data = file.read()
                user_current=json.loads(data)
                os.chdir("..")
                self.username=user_current['username']
                self.time=user_current['time']
                self.progress=user_current['progress']
        else:
            os.chdir("..")
            self.username=name
            self.progress=progress
            self.time=time
    def save_progress(self):
        with open('users/{}.json'.format(self.username),'w') as file:
            json.dump({'username':self.username,'time':self.time,'progress':self.progress}, file)
    def next_levels(self):
        self.progress+=1
    def start_time(self):
        self.time_start=time.perf_counter()
    def stop_time(self):
        self.counter_second = time.perf_counter()-self.time_start
        self.total_time=round(self.counter_second)
        self.time+=self.total_time
    def progress(self):
        return self.progress
    def log_out(self):
        self.stop_time()
        self.save_progress()
    def time_(self):
        sec=timedelta(seconds=self.time)
        d=datetime(1,1,1)+sec
        return "%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second)