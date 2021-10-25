'''
Created on Dec 4, 2018
@author: qaauto
'''
from common.lib.global_variables import Global_variables
import unittest
import re
import os
import sys
import pyautogui
from common.lib.exceptions import Exceptions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from common.locators.loginpage_locators import LoginPageLocators
import time
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException,StaleElementReferenceException
from PIL import Image, ImageGrab
import warnings
from openpyxl import Workbook
from openpyxl import load_workbook
import subprocess
from selenium.webdriver.common import alert
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from common.lib import utillity
import keyboard
import os
import subprocess
import uiautomation as automation
from common.pages import as_ribbon
from selenium.webdriver.support.ui import Select
from common.lib.webdriverfactory.WebDriverFactory import WebDriverFactory
from common.lib.core_utility import CoreUtillityMethods as coreutillobject
from selenium.webdriver.support.color import Color
import pywinauto

class AS_Core_Utility_Methods(object):
    '''
    This class has methods specific for Appstudio
    '''
    LOCAL_SLEEP_TIME=10
    SHORTWAIT = Global_variables.shortwait * AS_Core_Utility_Methods.LOCAL_SLEEP_TIME
    MEDIUMWAIT = Global_variables.mediumwait * AS_Core_Utility_Methods.LOCAL_SLEEP_TIME
    LONGWAIT = Global_variables.longwait * AS_Core_Utility_Methods.LOCAL_SLEEP_TIME
    
    def __init__(self, driver):
        self.as_driver = driver
        self.exceptions = Exceptions(self)
    
    def validate_exceptions(self, obj):
        try:
            obj.is_displayed()
        except:
            print(sys.exc_info()[1].__class__.__name__)
    
    def create_failure_log(self, msg):
        try:
            Global_variables.verification_failure_msg_list.append(msg)
        except:
            print("Unable to append in failure capture message '{0}' to verification_failure_msg_list",format(msg))
    
    def as_List_equal(self,*params):
        try:
            testobj = unittest.TestCase()
            testobj.assertListEqual(params[0], params[1], params[2])
            print(params[2] + " - PASSED.")
        except AssertionError as e:
            m = re.match(r'.*(Step.*)...', str(e.args))
            msg = m.group(1)+" - FAILED."+'List Equal comparison : value1=['+str(params[0])+'], value2=['+str(params[1])+']'
            print(msg)
            Global_variables.asert_failure_count += 1
            AS_Core_Utility_Methods.create_failure_log(self, msg)
    
    def asequal(self, *params):
        try:
            testobj = unittest.TestCase()
            testobj.assertEqual(params[0], params[1], params[2])
            print(params[2] + " - PASSED.")
        except AssertionError as e:
            m = re.match(r'.*([S|s]tep.*)...', str(e.args))
            msg = m.group(1)+" - FAILED."+'Equal comparison : value1=['+str(params[0])+'], value2=['+str(params[1])+']'
            print(msg)
            Global_variables.asert_failure_count += 1
            AS_Core_Utility_Methods.create_failure_log(self, msg)
            
    def as_not_equal(self, *params):
        try:
            testobj = unittest.TestCase()
            testobj.assertNotEqual(params[0], params[1], params[2])
            print(params[2] + " - PASSED.")
        except AssertionError as e:
            m = re.match(r'.*(Step.*)...', str(e.args))
            msg = m.group(1)+" - FAILED."+'Not Equal comparison : value1=['+str(params[0])+'], value2=['+str(params[1])+']'
            print(msg)
            Global_variables.asert_failure_count += 1
            AS_Core_Utility_Methods.create_failure_log(self, msg)
    
    def asin(self, *params):
        try:
            #testobj = unittest.TestCase()
            assert params[0] in params[1], params[2]
            print(params[2] + " - PASSED.")
        except AssertionError as e:
            m = re.match(r'.*(Step.*)...', str(e.args))
            msg = m.group(1)+" - FAILED."+'ASIN comparison : value1=['+str(params[0])+'], value2=['+str(params[1])+']'
            print(msg)
            Global_variables.asert_failure_count += 1
            AS_Core_Utility_Methods.create_failure_log(self, msg)
            
    def as_notin(self, *params):
        try:
            #testobj = unittest.TestCase()
            assert params[0] not in params[1], params[2]
            print(params[2] + " - PASSED.")
        except AssertionError as e:
            m = re.match(r'.*(Step.*)...', str(e.args))
            msg = m.group(1)+" - FAILED."+'Equal comparison : value1=['+str(params[0])+'], value2=['+str(params[1])+']'
            print(msg)
            Global_variables.asert_failure_count += 1
            AS_Core_Utility_Methods.create_failure_log(self, msg)
    
    def as_GE(self, *params):
        try:
            testobj = unittest.TestCase()
            testobj.assertGreaterEqual(params[0], params[1], params[2])
            print(params[2] + " - PASSED.")
        except AssertionError as e:
            m = re.match(r'.*(Step.*)...', str(e.args))
            msg = m.group(1)+" - FAILED."+'As GEqual to comparison : value1=['+str(params[0])+'], value2=['+str(params[1])+']'
            print(msg)
            Global_variables.asert_failure_count += 1
            AS_Core_Utility_Methods.create_failure_log(self, msg)

    def as_LE(self, *params):
        try:
            testobj = unittest.TestCase()
            testobj.assertLessEqual(params[0], params[1], params[2])
            print(params[2] + " - PASSED.")
        except AssertionError as e:
            m = re.match(r'.*(Step.*)...', str(e.args))
            msg = m.group(1)+" - FAILED."+'As LEqual to comparison : value1=['+str(params[0])+'], value2=['+str(params[1])+']'
            print(msg)
            Global_variables.asert_failure_count += 1
            AS_Core_Utility_Methods.create_failure_log(self, msg)
    
    def take_monitor_screenshot(self, file_name, image_type='actual', left=0, top=0, right=0, bottom=0):#Need to delete
        """
        :param file_name: file for saving
        :param image_type: where you want to save your image in directory
        :param left: how much you want to reduce the size from left in output of your image
        :param top: how much you want to reduce the size from top in output of your image
        :param right: how much you want to reduce the size from right in output of your image
        :param bottom: how much you want to reduce the size from bottom in output of your image
        :usage take_monitor_screenshot('full_monitor_screenshot', image_type='actual', left=10, top=25, right=10, bottom=25)
        """        
        if image_type=='actual' :
            location='actual_images'
        elif image_type=='fail' :
            location='failure_captures'
        else:
            location='images'
        file_path=os.getcwd() + "\\" + location + "\\" + file_name + ".png"
        im=ImageGrab.grab()
        im.save(file_path)
        resolution=pyautogui.size()
        left_rs = left
        top_rs = top
        right_rs=resolution[0]-right
        bottom_rs=resolution[1]-bottom
        bbox = (left_rs, top_rs, right_rs, bottom_rs)
        base_image = Image.open(file_path)
        cropped_image = base_image.crop(bbox)
        cropped_image.save(file_path)
    
    
    
    
    def select_tree_view_pane_item_fast_no_check(self,tree_path):                
        """
        Usage: select_item_from_tree_view("driver.find_element_by_name("Static"), "jawin7->Domains->P20")
        params:parent_obj="driver.find_element_by_name("Static" ) ;  "jawin7->Domains->P20"
        """        
        pyautogui.hotkey("home")
        time.sleep(2)                   
        path_list=tree_path.split("->")  
        for arg in path_list:
            ac = ActionChains(self.as_driver)
            ac.double_click(self.as_driver.find_element_by_name(arg)).perform()
            time.sleep(2)
            del ac
            time.sleep(1)
    
    def select_tree_view_pane_item(self,tree_path,**kwargs):
        
        """
        Usage: select_tree_view_pane_item(jawin7->Domains->P20", Parent_Object = driver.find_element_by_name("Static"))
        params:parent_obj="driver.find_element_by_name("Static" );"jawin7->Domains->P20"
        """ 
        try:
            pyautogui.FAILSAFE=False
            if "Parent_Object" in kwargs:
                self.as_driver.find_element(*kwargs["Parent_Object"]).click()
            else:
                tree_view = automation.TreeControl(ClassName="SysTreeView32")
                tree_view.Click(ratioX=10,ratioY=140)
                automation.SendKey(automation.Keys.VK_HOME,waitTime=3) 
            path_list=tree_path.split("->")
            for i in path_list:
                time.sleep(5)
                automation.TreeItemControl(Name=i).ScrollIntoView()
                automation.TreeItemControl(Name=i).Expand(waitTime=3)
                if (automation.TreeItemControl(Name=i).CurrentExpandCollapseState()==3):
                    automation.TreeItemControl(Name=i).DoubleClick(waitTime=3)
        except:
                print("Tree element does not exist")
                
    def ui_double_click_tree_view_item(self, tree_path,**kwargs):
        
        '''==========================================================================
        Description : To expand any folder or to double click any file.
        using click in right click menu for ENV Tree: as_utilo_obj.select_tree_view_item_using_ui(self,tree_path,**kwargs):
        @author: Robert
        ========================================================================='''
        
        try:
            pyautogui.FAILSAFE=False
            driver = self.driver
            if "Parent_Object" in kwargs:
                self.as_driver.find_element(*kwargs["Parent_Object"]).click()
            else:
                self.as_driver.find_element_by_class_name("SysTreeView32").click()
            pyautogui.hotkey("home")
            path_list=tree_path.split("->")
            for i in path_list:
                automation.TreeItemControl(Name=i).ScrollIntoView()
                automation.TreeItemControl(Name=i).DoubleClick()
        except:
                print("No Element Found")
        
        