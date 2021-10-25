import unittest, time
from selenium import webdriver
from common.lib import utillity,as_utility
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
from selenium.common.exceptions import NoSuchElementException
from common.lib.as_utility import AS_Utillity_Methods
from common.lib.utillity import UtillityMethods
import pyautogui
import uiautomation as automation
from urllib.error import URLError

class AS_BaseTestCase(unittest.TestCase):

    def setUp(self):
        UtillityMethods.asert_failure_count=0
        AS_Utillity_Methods.asert_failure_count=0
        
        try:
            window_exist=automation.WindowControl(Name='App Studio').Exists()
            time.sleep(5)
            if window_exist==True:
                    automation.WindowControl(Name='App Studio').Maximize()
                    automation.WindowControl(Name='App Studio').SetFocus()
        
        except LookupError or TimeoutError:
            print("App Studio not invoked")
         
        try:   
            self.driver = webdriver.Remote(command_executor='http://localhost:9999',
                                  desired_capabilities={'debugConnectToRunningApp': 'true'})#'false', "app": r"C:/ibi/AppStudio82/bin/Focshell.exe"})
        except URLError:
            print("Winium.driver.exe is not running")
        
        '''Close Error Prompt'''
           
        try:
            automation.WindowControl(ClassName="#32770").Exists()
            automation.WindowControl(ClassName="#32770").ButtonControl(Name="OK").Click()
            time.sleep(2)
                 
        except:
            pass 
                            
        ''' close recovery HTML dialog '''
        try:
            document_recovery=automation.WindowControl(Name="Document Recovery").Exists()
            if document_recovery==True:
                automation.WindowControl(Name="Document Recovery").ButtonControl(Name="Cancel").Click()
                automation.WindowControl(Name="Document Recovery").ButtonControl(Name="No").Click()
                time.sleep(2)
        except LookupError:
            pass   
                
        """ Close startup help window"""             
        try:
            welcome_screen=automation.WindowControl(ClassName="#32770").Exists()
            if welcome_screen==True:
                automation.WindowControl(ClassName="#32770").Close()   
        except:
            pass
                
        try:
            help_wizard=automation.PaneControl(AutomationId="2054").Exists()
            if help_wizard==True:
                automation.TabItemControl(Name="Home").Click()
                automation.CheckBoxControl(Name="Help Wizard").Click()
        except:
            pass   
        
    def tearDown(self):  
         
        '''close HTML canvas area'''

        appstudio_exists=automation.WindowControl(RegexName="App*").Exists()
                                           
        if appstudio_exists!=True:
            print("App studio got closed")
        else:
            pass
        
        suite_list=["S9100_ToolTips"]
        appstudio_window="App Studio"
        dialog_class_name="#32770"
        click_no="No"
          
        suite=as_utility.AS_Utillity_Methods.parseinitfile(self,"suite_id")
        if suite not in [suite_list]:
              
            window_exist=automation.WindowControl(Name=appstudio_window).Exists()
            if window_exist!=True:
                  
                try:
                    dialog_window_exist=automation.WindowControl(ClassName=dialog_class_name).Exists() 
                    if dialog_window_exist==True: 
                        automation.WindowControl(ClassName=dialog_class_name).Close(waitTime=2)
                    window_exist=automation.WindowControl(Name=appstudio_window).Exists()
                    if window_exist==True:
                        automation.ButtonControl(Name=click_no).Click(waitTime=1)
                    
                  
                except:
                    print ("Eror: Unable to close the App Studio alert dialog window")
                  
                    '''close any unsaved files when test fails'''
  
                try: 
                    canvas_item_exists=automation.PaneControl(RegexName="HtmlPage.*").Exists()
                    while canvas_item_exists==True:
                        as_utility.AS_Utillity_Methods.close_canvas_item(self)
                        time.sleep(5)
                        canvas_item_exists=automation.PaneControl(RegexName="HtmlPage.*").Exists()
                        save_warning_prompt=automation.WindowControl(ClassName=dialog_class_name).Exists() 
                        if save_warning_prompt==True:
                            automation.ButtonControl(Name=click_no).Click(waitTime=1)
                except:
                    print ("Error: Unable to close the open documents in canvas")
            
            else:
                if automation.ButtonControl(Name=click_no).Exists():
                    automation.ButtonControl(Name=click_no).Click(waitTime=1)
                
        else:
            pass 

        filename = os.getcwd() + "\\failure_captures\\"+ self._testMethodName + ".png"
        for method, error in self._outcome.errors:
            if error:
                try:
                    self.driver.save_screenshot(filename)
                except:
                    print("Exception in save_screenshot")
                    filename_obj=self._testMethodName
                    utillity.UtillityMethods.take_monitor_screenshot(self, filename_obj, image_type='fail')

        if UtillityMethods.asert_failure_count>0:
            self.fail('Verification check point failed')
            
        if AS_Utillity_Methods.asert_failure_count>0:
            self.fail('Verification check point failed')

