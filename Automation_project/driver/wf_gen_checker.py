'''
Created on Jun 19, 2018

@author: ja13707
'''

import time, sys, os, re
from selenium import webdriver
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
from configparser import ConfigParser


JSP="/diagnostics/about.jsp"
http= "http://"
required_file=sys.argv[1]
#browserForDictKey = sys.argv[2]
browserForDictKey="CR"
BROWSER_CONFIG_FILE_PATH="common\\lib\\configfiles"
BROWSER_CONFIG_FILE="config.ini"


class Get_WF_GEN_Class():  
    userId          ="admin"
    userPass        ="admin" 

    'locators'
    SignonUserName  ="input[id='SignonUserName']"
    SignonPassName  ="input[id='SignonPassName']"
    SignonbtnLogin  ="input[ id='SignonbtnLogin']"
    brDict          ={"cr": "chrome"
                      ,"ff": "firefox"
                      ,"ie": "ie"
                      ,"eg": "edge"
                      }

        
    def __get_dir_name(self,parentpath,required_file): 
        for dirName, subdirList, fileList in os.walk(parentpath):
            if required_file in fileList:
                fileDir=os.path.abspath(dirName)
                filePath=os.path.join(fileDir,required_file)                
                return(filePath)
                break    

        
                
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
    
    def __read_browser_ini_file(self,config_file_path):          
        
        if os.path.exists(config_file_path):   
            parser= ConfigParser()
            parser.read(config_file_path)
            rootDir= parser.get("DEFAULT","executables_path")
            #driverExe=parser.get(self.brDict['browserForDictKey.lower()'],"executable") 
            driverExe=parser.get(self.brDict['cr'],"executable")           
            executablePath= os.path.join(rootDir,driverExe)
            return(executablePath)
        else:
            userMessage=("Properties file is not found in this path ="+config_file_path) 
            e=ConnectionError(userMessage)
            raise(e)
                 
    def __read_wf_insatll_properties(self,config_file_path): 
        
        if os.path.exists(config_file_path):
            server = self.__parseinitfile(config_file_path,'nodeid')
            port = self.__parseinitfile(config_file_path,'httpport')
            context = self.__parseinitfile(config_file_path,'wfcontext')          
            wfUrl=http+server+":"+port+context
            return(wfUrl)
            
        else:
            userMessage=("Properties file is not found in this path = "+config_file_path) 
            e=FileNotFoundError(userMessage)
            raise(e)  
    
    def get_wf_gen_Info(self):  
        os.path.abspath(os.chdir(os.pardir)) 
        dirList=os.listdir('.')
        for i in dirList:
            if i.startswith("S"):                
                path1= os.path.join(i,BROWSER_CONFIG_FILE_PATH)
                config_file_path=os.path.join(path1,BROWSER_CONFIG_FILE)                                  
                break  
      
        executablePath=self.__read_browser_ini_file(config_file_path)        
        if browserForDictKey.lower() == 'cr':
            driver= webdriver.Chrome(executablePath) 
            self.driver=driver               
        else:
            print("browser doesn't match")
             
   
        seleniumPath=os.path.abspath(os.getcwd())
        config_file_path= self.__get_dir_name(seleniumPath, required_file)         
        wfUrl= self.__read_wf_insatll_properties(config_file_path)
        driver.implicitly_wait(3)
        driver.get(wfUrl)
        driver.find_element_by_css_selector(self.SignonUserName).click()
        driver.find_element_by_css_selector(self.SignonUserName).send_keys(self.userId)
        driver.find_element_by_css_selector(self.SignonPassName).click()
        driver.find_element_by_css_selector(self.SignonPassName).send_keys(self.userPass)
        driver.find_element_by_css_selector(self.SignonbtnLogin).click()


        url= wfUrl+JSP
        driver.get(url)
        time.sleep(5)
        pagesource=driver.page_source
        soup=BeautifulSoup(pagesource, 'html.parser')
        soup.prettify()
        
        innerText=soup.find_all("tr")
        genInfo=[]
        for i in innerText:
            genInfo.append(i.text)
        
        print("********************************************************************\nThe following items are WebFOCUS Build information: ")
        print("wfUrl:"+ wfUrl)
        for i in genInfo[0:3]:    
            print(i)
                       
        print("\n")   

        
        'close browser'
        self.driver.quit()
    
        
wfGenObj=Get_WF_GEN_Class()
wfGenObj.get_wf_gen_Info()


