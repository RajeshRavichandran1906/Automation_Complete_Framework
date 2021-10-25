'''
Created on Feb 23, 2018

@author: Jesmin
'''
import requests
from requests.exceptions import ConnectionError
import xml.etree.ElementTree as ET
import sys, re
import wf_exception_check
import os, os.path
from configparser import ConfigParser
import time
import requests


sleepTime=300
http= "http://"
required_file=sys.argv[1]


class WF_Install_Checker_Class(object):
    
    def __init__(self):
        self.__current_file_path=os.path.abspath(os.path.dirname(__file__))
    
    def __parseinitfile(self,required_file, key):
        init_file = required_file
        config_pair = {}
        try:
            fileObj = open(init_file, "r")
            line = fileObj.readline()
            while line:
                lineObjbj = re.match(r'(\S*)\s(.*)', line)
                keyName = lineObjbj.group(1)
                config_pair[keyName] = lineObjbj.group(2)
                line = fileObj.readline()
            fileObj.close()
        except IOError:
            exit()
        if key in config_pair:
            return (config_pair[key])
        else:
            return ('Key not found')
    
    def __get_dir_name(self,parentpath,required_file): 
        for dirName, subdirList, fileList in os.walk(parentpath):
            if required_file in fileList:
                fileDir=os.path.abspath(dirName)
                filePath=os.path.join(fileDir,required_file)
                return(filePath) 
         
    def __read_wf_install_properties(self,config_file_path):      
        if os.path.exists(config_file_path):
            server = self.__parseinitfile(config_file_path,'nodeid')
            port = self.__parseinitfile(config_file_path,'httpport')
            context = self.__parseinitfile(config_file_path,'wfcontext')
            #userId = self.__parseinitfile(config_file_path,'mrid')
            #userPass = self.__parseinitfile(config_file_path,'mrpass')
            #Overwriting the assigned credentials until
            userId = "admin"
            userPass = "admin"
            wfUrl=http+server+":"+port+context
            return(wfUrl, userId, userPass)
        else:
            userMessage=("Properties file is not found in this path = "+config_file_path) 
            e=FileNotFoundError(userMessage)
            raise(e) 
   
    def start_wf_login_test(self,required_file):
        
        wfExceptObject=wf_exception_check.WF_Exception_Check()
        mypath=os.path.dirname(__file__)
        parentpath=os.path.abspath(os.path.join(mypath, os.pardir))
        config_file_path=self.__get_dir_name(parentpath, required_file)
        print("config_file_path = %s"%config_file_path) 
        wfUrl, userId, userPass= self.__read_wf_install_properties(config_file_path)
        env_status = requests.get(wfUrl).status_code
        if env_status != 200:
            print('The WebFocus client is inaccessible.')
            sys.exit(1)
        print("wfUrl = %s, userId = %s, userPass = %s" %(wfUrl, userId, userPass))
         
        try:
            sign_on_status = wfExceptObject.wfSignOn(wfUrl,userId,userPass)
            reporting_server_status = wfExceptObject.check_reporting_server(wfUrl)
            wfExceptObject.wfSignOut(wfUrl)
            if sign_on_status == '10000':
                if reporting_server_status == '10000':
                    print('The WebFocus environment has no issues.')
                else:
                    print('Please check the reporting server.')
                    sys.exit(1)
            else:
                #This will not give a valid result right now because the user is hardcoded to admin.
                print('Please check your WebFocus credentials.')
                sys.exit(1)
        except:
            print('Please check settings.')
            sys.exit(1)
    
WF_Install_Checker_Class().start_wf_login_test(required_file)
    
                                                                                                                                                                                        
        
        
    
   

                
    