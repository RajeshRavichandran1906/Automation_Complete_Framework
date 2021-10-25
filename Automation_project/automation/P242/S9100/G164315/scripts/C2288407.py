'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288407'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import keyboard as keys_1
import pyautogui as keys
import uiautomation as automation

class C2288407_TestClass(AS_BaseTestCase):
    def test_C2288407(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
         
        '''Step 01: Right click on InfoMini'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                            
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
               
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
             
        as_utilobj.select_component_by_right_click(right_click_item='Infomini',send_keys=['down'])
        time.sleep(1)
             
        item_list=['Run','Print','Security','New','Duplicate','Copy','Rename','Delete','Properties']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 01: "+ items + " element avaliable in right clicking infomini",available=True)
            
        keys.hotkey('escape')
        time.sleep(1)
                
        '''Step 02: Double click on InfoMini procedure
                    Click on Format->PDF
                    Click Run'''
                
        tree_path="Infomini"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(45)
            
        as_utilobj.web_element_click("Infomini - WebFOCUS InfoAssist+ - Internet Explorer",text_click="Format")
        time.sleep(3)
    
        as_utilobj.web_element_click("Infomini - WebFOCUS InfoAssist+ - Internet Explorer",text_click="PDF")
        time.sleep(2)   
    
        as_utilobj.Verify_Element("PDF","Step 02: Verified Infomini reports selected for PDF format",available=True)
        time.sleep(2)
            
        '''Step 03: Click Save icon
                    Type InfoMiniPDF for Title
                    Click Save
                    Close InfoMiniPDF - WebFOCUS InfoAssist+ tab'''
            
        as_utilobj.web_element_click("Infomini - WebFOCUS InfoAssist+ - Internet Explorer",group_click="saveButton")
        time.sleep(4)
          
        as_utilobj.click_element_using_ui(button_item=True,name='Clear value')
            
        keys_1.write("InfominiPDF")
        time.sleep(2)
           
        automation.GroupControl(Name="Save").Click()
        time.sleep(6)
          
        as_utilobj.web_element_click("InfominiPDF - WebFOCUS InfoAssist+ - Internet Explorer",text_click="Run")
        time.sleep(8)  
           
        as_utilobj.Verify_Browser_Content("IEFrame","Step 03: Verified Infomini report saved successfully in PDF format",item="InfominiPDF[0]",browser_close=True)
        time.sleep(3)
           
        '''Step 04: Under Environments Tree, View Options-> Refresh View
                    Right click on InfoMiniPDF'''
          
        as_utilobj.select_component_by_right_click(right_click_folder='S9100',click='Refresh Descendants')
        time.sleep(5)
         
        as_utilobj.select_component_by_right_click(right_click_item='InfominiPDF',send_keys=['down'])
        time.sleep(3)
         
        item_list=['Run','Print','Hide','Security','New','Duplicate','Copy','Rename','Delete','Properties']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 04: "+ items + " element avaliable in right clicking infominiPDF",available=True)
        time.sleep(2)
             
        keys.hotkey('escape')
        time.sleep(1)
             
        '''Step 05: Double click on InfoMiniPDF 
                    Close InfoMiniPDF - WebFOCUS InfoAssist+ tab'''
        
        tree_path="InfominiPDF"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(45)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 05: Verified Infomini report reopened successfully in PDF format",item="InfominiPDF[0]",browser_close=True)
        time.sleep(3)
        
        '''Delete the created infomini PDF for reason of next run'''
        
        as_utilobj.select_component_by_right_click(right_click_item='InfominiPDF',click='Delete')
        time.sleep(2)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        print("Note:Created Infomini PDF file deleted for reason of next run")
        
if __name__=='__main__' :
    unittest.main()    