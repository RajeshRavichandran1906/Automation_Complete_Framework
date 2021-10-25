'''
Created on Feb 23, 2018

@author: ja13707
'''
import requests
from requests.exceptions import ConnectionError
import xml.etree.ElementTree as ET

class WF_Exception_Check(object):
    def __init__(self):
        self.wsPath="/rs/ibfs"
        self.csrf_token_value = ""
        self.session = requests.session()
    
    def wfSignOn(self,wfUrl, userId, userPass=""):
        url=wfUrl+self.wsPath
        params= {'IBIRS_action':'signOn','IBIRS_userName':userId,'IBIRS_password':userPass}  
        r = self.session.get(url = url, params = params) 
        xmlFile=str(r.text)
        root = ET.fromstring(xmlFile)
        key=root.attrib    
        
        self.csrf_token_value = root[1][1].attrib['value']
        return key['returncode']  
           
    def wfSignOut(self,wfUrl):
        url=wfUrl+self.wsPath
        params={'IBIRS_action':'signOff'}
        r = self.session.get(url = url, params = params)
        xmlFile=str(r.text)
        root = ET.fromstring(xmlFile)
        key=root.attrib

        return key['returncode']
       
    def check_reporting_server(self, wf_url):
        url = wf_url + self.wsPath + '/EDA/EDASERVE'
        params = {'IBIRS_action':'get', 'IBIWF_SES_AUTH_TOKEN':self.csrf_token_value}
        r = self.session.post(url = url, params = params)
        xmlFile = str(r.text)
        root = ET.fromstring(xmlFile)
        key=root.attrib
        
        return key['returncode']
      
   
    

    

                
    