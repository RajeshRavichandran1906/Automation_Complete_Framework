'''
Created on Feb 9, 2018

@author: ja13707

'''

import difflib
import time
import unittest
from bs4 import BeautifulSoup, SoupStrainer
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from common.lib.utillity import UtillityMethods as utilObject
from selenium.webdriver.common.by import By
from common.lib.core_utility import CoreUtillityMethods as core_utilobj
from selenium.webdriver.support import expected_conditions as EC

class Html_Dom_Utility():     
        
    def __init__(self,driver): 
        self.driver=driver    
    
    def wf_login(self, wf_url,loginid):   
        self.driver.get(wf_url)
        time.sleep(2)
        self.driver.find_element_by_id("SignonUserName").send_keys(loginid)
        time.sleep(2)
        #self.driver.find_element_by_id("SignonPassName").send_keys(loginpwd)
        self.driver.find_element_by_id("SignonbtnLogin").click()
        time.sleep(2)
                            
    def get_html_dom(self,test_url):
        driver=self.driver
        driver.get(test_url)
        time.sleep(20)
        html_source=driver.page_source        
        soup = BeautifulSoup(html_source, 'html.parser')        
        return(soup.prettify())
    
    def save_html_dom(self,html_page,filename): 
        #page=self.get_html_dom(test_url)
        with open(filename,'w')as file: 
            file.write(html_page)
    
    def read_html_dom(self,filename):
        with open(filename,'r') as file:
            dom=file.read()
            return(dom)
    
    def make_soup(self, file_name):
        soup = BeautifulSoup(file_name, 'html.parser')
        return(soup)
    
    def get_tag_list(self,filename,tag,key,value):
        soup=self.make_soup(filename)               
        tagList=soup.find_all(tag, {key:value}) 
        return(tagList)   
        
                               
    def get_soup_strainer(self, tag_name,html_source):
        #html_source=self.driver.page_source
        only_specific_tag = SoupStrainer(tag_name)
        soup= BeautifulSoup(html_source, "html.parser", parse_only=only_specific_tag)
        return(soup)
        
    def get_html_tag(self,filename,tag_name,tag_key):
        soup = BeautifulSoup(filename, 'html.parser')
        tagList=soup.find_all(tag_name)
        get_tag=None
        for items in tagList:
            tagDict = items.attrs
            if tag_key in tagDict:
                get_tag=tagDict.get(tag_key)
        print(items.get(tagDict)) 
        return(items.get(tagDict)) 
    
    
    def get_html_key_value(self,html_source,tag_name,key,value,**kwargs): 
        #TODO: incomplete 
        #html_source=self.driver.page_source   
        soup=self.get_soup_strainer(tag_name,html_source)
        
        get_tagDict=None       
        for child in soup.children:
            tagDict=child.attrs
            if key in tagDict:  
                value= tagDict[key][0] 
                if value.startswith(value):
                    if key in kwargs:
                        get_tagDict=tagDict.get(kwargs["key"])
                    else:
                        get_tagDict=tagDict.get(key)
                    
        print(get_tagDict)                      
        return(get_tagDict) 
    
                
    def get_html_text_attributes(self,filename,tag_attribute,search_label): 
        """
        :param value: String, BeautifulSoup, Tag, or list of the above
        :param str parser: Parser to use; defaults to BeautifulSoup default
        :return: Tag or list of Tags    
        """
        only_specific_tag = SoupStrainer('text')
        soup= BeautifulSoup(filename, "html.parser", parse_only=only_specific_tag)
        get_text=[]
        for child in soup.children:
            if child[tag_attribute][0].startswith(search_label):
                x=child.text.replace("\n","")                
                get_text.append(x.replace(" ",""))
        return(get_text)
        
    def get_key_value(self,fileName,tag,searchString):
            soup = BeautifulSoup(fileName, 'html.parser')
            tagList=soup.find_all(tag)
            get_tagDict=[]
            for items in tagList:
                tagDict = items.attrs
                if "class" in tagDict:   
                    value= tagDict["class"][0] 
                    if value.startswith(searchString):
                        get_tagDict=tagDict.get("fill")
            
            return(get_tagDict)
  
    def strip_text(self,tagList,search,**kwargs):
        '''kwargs=startswith or endswith'''        
        get_text=[]
        for i in tagList:
            x=i.text.strip(' \n')
            if 'startswith' in kwargs:
                if x.startswith(search):
                    get_text.append(x)
            elif 'endswith' in kwargs:
                if x.endswith(search):
                    get_text.append(x)                        
        return(get_text)
        
    def create_comparison_file(self, path_file1_name,path_file2_name,path_write_location):
        dom1_lines=open(path_file1_name).readlines()
        dom2_lines=open(path_file2_name).readlines()
        
        #diff=difflib.HtmlDiff().make_table(dom1_lines,dom2_lines,base_chart_file_name,new_chart_file_name,True)
        diff=difflib.HtmlDiff().make_file(dom1_lines,dom2_lines,path_file1_name,path_file2_name)
        with open(path_write_location+"diff.html",'w') as file:
            file.write(diff)
        
    
 
        
        
        
        
        
        
    
            

        
        
    
        
