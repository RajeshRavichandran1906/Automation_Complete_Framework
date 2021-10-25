'''
Created on June16, 2016
@author: Kiruthika

Setup file to create the below master files

Tutorials -> WF_RETAIL Demo(wf_retail, wf_retail_lite)
          -> Legacy tables(car, ggorder)
Upload    -> Customer_data xlsx
          -> Century_master xlsx
Placing the mutual funds mas and foc file

'''
import unittest
import time,os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.base import BasePage
from common.lib import utillity

class startup_function_TestClass(BasePage):
    
    def RS_file_upload(self,upload_dir,upload_type,upload_file,sample_data):
        """
        :Usage: RS_file_upload(self,'baseapp','Data','centurymaster.xlsx','United States')
        Reporting server version : Release 88
        """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(0) #Intializing common implicit wait for throughout the test        
        utillobj = utillity.UtillityMethods(self.driver)
        """ Reporting Server Console"""
        baseapp ="//div[@class='bi-tree-view-body-content']//span[contains(text(),'"+upload_dir+"')]"
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, baseapp)))
        action = ActionChains(self.driver)
        action.context_click(self.driver.find_element_by_xpath(baseapp)).perform()
        new="//*[contains(@id,'BiPopup')]//tr[*]/td[contains(text(),'New')]"
        time.sleep(5)
        elements = self.driver.find_elements_by_xpath(new)
        elements[len(elements)-1].click()
        
        """ Upload Data """
        
        upload_data="//*[contains(@id,'BiPopup')]//td[contains(text(),'Upload "+upload_type+"')]"
        time.sleep(5)
        elements = self.driver.find_elements_by_xpath(upload_data)
        elements[len(elements)-1].click() 
        
        """ Function call to AutoIt_file_upload"""
        self.AutoIt_file_upload('FileUpload',upload_file)
        time.sleep(15)         
        Load_Data="//div[contains(@id,'BiFlowPanel')]//div[contains(text(),'Load')]/img[contains(@src,'runadvanced')]"
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, Load_Data)))
        self.driver.find_element_by_xpath(Load_Data).click()
        Target = "//div[contains(@id,'BCFilePicker')]//input"
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, Target)))
        self.driver.find_element_by_xpath(Target).clear()
        self.driver.find_element_by_xpath(Target).send_keys(upload_dir)
        Proceed="//div[contains(@id,'BiGridPanel')]/div[contains(text(),'Proceed to Load')]"
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, Proceed)))
        self.driver.find_element_by_xpath(Proceed).click()
        time.sleep(30)
        Loaded_Data="//div[contains(@id,'BiFlowPanel')]//div[contains(text(),'Show')]"
        WebDriverWait(self.driver, 80).until(EC.visibility_of_element_located((By.XPATH, Loaded_Data)))
        
        """ Sample Data """
        sample="//div[contains(@id,'BiFlowPanel')]//div[contains(text(),'Sample')]"
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, sample)))
        self.driver.find_element_by_xpath(sample).click()
        Data = "//*[@class='grid-header' and contains(text(),'Country')]"
        time.sleep(10)
        close ="//*[contains(@class,'bi-button window-close-button')]"
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, close)))
        self.driver.find_element_by_xpath(close).click()
        time.sleep(10)
        
    def AutoIt_file_upload(self,exe_file,upload_file):
        utillobj = utillity.UtillityMethods(self.driver)
        browser = utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            os.system(os.getcwd() + "\data\\"+exe_file+"_FF.exe \data\\"+upload_file) #"D:\AutoIt\FileUpload.exe"
        elif browser == 'Chrome':
            os.system(os.getcwd() + "\data\\"+exe_file+"_Chrome.exe \data\\"+upload_file) #"D:\AutoIt\FileUpload.exe"
        elif browser == 'IE':
            os.system(os.getcwd() + "\data\\"+exe_file+"_IE.exe \data\\"+upload_file) #"D:\AutoIt\FileUpload.exe"
        time.sleep(15)
        
    def RS_create_tutorials(self,dir,tutorial):
        """
        :Usage: RS_create_tutorials(self,'baseapp','WebFOCUS - Retail Demo')
        """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(0) #Intializing common implicit wait for throughout the test        
        utillobj = utillity.UtillityMethods(self.driver)
        """ Reporting Server Console"""
        baseapp ="//div[@class='bi-tree-view-body-content']//span[contains(text(),'"+dir+"')]"
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, baseapp)))
        action = ActionChains(self.driver)
        action.context_click(self.driver.find_element_by_xpath(baseapp)).perform()
        new="//*[contains(@id,'BiPopup')]//tr[*]/td[contains(text(),'New')]"
        time.sleep(5)
        elements = self.driver.find_elements_by_xpath(new)
        elements[len(elements)-1].click()
        
        """ Tutorials """
        
        tut="//*[contains(@id,'BiPopup')]//td[contains(text(),'Tutorials')]"
        time.sleep(5)
        elements = self.driver.find_elements_by_xpath(tut)
        elements[len(elements)-1].click()
        
        select = "//*[contains(@id,'BiGridPanel')]//div[contains(text(),'"+tutorial+"')]"
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, select)))
        self.driver.find_element_by_xpath(select).click()
        
        create = "//*[contains(@id,'BiGridPanel')]//div[@class='bi-button-label wc-button' and contains(text(),'Create')]"
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, create)))
        self.driver.find_element_by_xpath(create).click()
        
        OK="//*[contains(@id,'BiButton')]//div[contains(@id,'BiLabel') and contains(text(),'OK')]"
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, OK)))
        self.driver.find_element_by_xpath(OK).click()
        
        Server="//*[contains(text(),'Executing server request')]"
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, Server)))
        time.sleep(260)
        
        

