import win32serviceutil
import os
import time
import socket
import jenkinsapi
from jenkinsapi.utils.crumb_requester import CrumbRequester
from jenkinsapi.jenkins import Jenkins

machine_name = socket.gethostname()
if "tcrunner" in machine_name: 
    services = ['Sentinel LDK License Manager', 'TestComplete 14 Service', 'jenkinsslave-D__Jenkins']
else:
    services = ['jenkinsslave-D__Jenkins']
limit = 50
user = 'guest'
pw = 'guest'
url = 'http://jenkins:8080'

def start_jenkins_service():
    #Check status
    #If it's active, don't start it
    #Otherwise run a loop for x amount of time to restart it
    tc_flag = True
    for svc in services:
        if svc == 'jenkinsslave-D__Jenkins' and tc_flag == False:
            try:
                print("Attempting to disable Jenkins service since TC service did not come up...")
                win32serviceutil.StopService(svc)
            except:
                print("Jenkins service already down.")
                return
        count = 0
        time.sleep(10)
        status = win32serviceutil.QueryServiceStatus(svc)
        while status[1] != 4 and count < limit: 
            win32serviceutil.StartService(svc)
            time.sleep(10)
            status = win32serviceutil.QueryServiceStatus(svc)
            count+=1
            print("restarting " + svc + " attempt " + str(count))
            print(str(status[1]))
            if status[1] != 4:
                crumb=CrumbRequester(username=user, password=pw, baseurl=url)
                jenkins = Jenkins(url, username=user, password=pw, requester=crumb)
                jenkins.build_job('Runner Agent Offline Alert', params={'node_name':machine_name})
        if svc in ['TestComplete 14 Service', 'Sentinel LDK License Manager'] and status[1] != 4:
            tc_flag = False
        
        
        
start_jenkins_service()
