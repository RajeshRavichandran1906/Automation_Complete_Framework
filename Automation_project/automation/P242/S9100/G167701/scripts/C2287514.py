'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287514'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import keyboard as keys

class C2287514_TestClass(AS_BaseTestCase):
    def test_C2287514(self): 
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, right click on Domains->New Folder
                    Click on New Folder1 and type (without the quotes): 'ThisIsAnExampleOfALongFolderName' 
                    Hit Enter'''
             
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                       
        as_utilobj.select_tree_view_pane_item("Domains") 
        time.sleep(2)
             
        as_utilobj.select_component_by_right_click(right_click_folder="Domains",click="New Folder")
        time.sleep(3)
             
        keys.write(("ThisIsAnExampleOfALongFolderName"))
        keys.press("enter")
        time.sleep(1)
              
        as_utilobj.Verify_Element("ThisIsAnExampleOfALongFolderName","Step 01: Verified that folder name been changed to ThisIsAnExampleOfALongFolderName",available=True)
              
        '''Step 02: Right click on ThisIsAnExampleOfALongFolderName->New Folder
                    Click on New Folder1 and type (without the quotes): 'ThisIsAnExampleOfALongSubfolderName'
                    Hit Enter'''
             
        as_utilobj.select_component_by_right_click(right_click_folder="ThisIsAnExampleOfALongFolderName",click="New",click_sub_menu="Folder")
        time.sleep(2)
              
        keys.write(("ThisIsAnExampleOfALongSubFolderName"))
        time.sleep(2)
        keys.press("enter")
        time.sleep(1)
             
        as_utilobj.Verify_Element("ThisIsAnExampleOfALongSubFolderName","Step 02: Verified that Sub folder name been changed to ThisIsAnExampleOfALongSubFolderName",available=True)
        time.sleep(2)
             
        '''Step 03: Right click on ThisIsAnExampleOfALongFolderName->New Report
                    EDASERVE Applications->ibisamp
                    Click empdata.mas and click Finish
                    Double click on DIV, DEPT and SALARY'''
             
        as_utilobj.select_component_by_right_click(right_click_folder="ThisIsAnExampleOfALongFolderName",click="New",click_sub_menu="Report")
        time.sleep(2)
     
        as_utilobj.select_file_in_dialogs("Finish",tree_path="ibisamp",select_file="empdata.mas")
        time.sleep(7)
             
        as_utilobj.click_element_using_ui(tree_item="DIV") 
             
        as_utilobj.click_element_using_ui(tree_item="DEPT") 
             
        as_utilobj.click_element_using_ui(tree_item="SALARY")
        time.sleep(2) 
             
        '''Step 04: Click on AS menu->Save As... 
                    For File name type: thisisalongfilenamesoicantesthowmanycharactersicanwrite
                    Click OK'''
           
        as_utilobj.select_component_by_right_click(right_click_folder="ThisIsAnExampleOfALongFolderName",click="Refresh Descendants")
        time.sleep(12)
            
        as_utilobj.select_application_menu_options(send_keys=['down','down','down'])
        time.sleep(2)
           
        keys.write("thisisalongfilenamesoicantesthowmanycharactersicanwrite")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(tree_item_select="thisisalongfilenamesoicantesthowmanycharactersicanwrite")
        time.sleep(1)
        
        as_utilobj.Verify_Element("thisisalongfilenamesoicantesthowmanycharactersicanwrite","Step 03: Verified that report been saved as thisisalongfilenamesoicantesthowmanycharactersicanwrite",available=True)
        time.sleep(4)
           
        '''Step 05: Click on AS menu->Save As... 
                    Click OK 
                    Click Yes in App Studio prompt window to overwrite'''
         
        as_utilobj.select_component_by_right_click(right_click_folder="ThisIsAnExampleOfALongFolderName",click="Refresh Descendants")
        time.sleep(10)
          
        as_utilobj.select_application_menu_options(send_keys=['down','down','down'])
        time.sleep(2)
        
        as_utilobj.select_any_dialog("OK")
        time.sleep(2)
         
        as_utilobj.select_any_dialog("Yes")
        time.sleep(2)
         
        '''Step 06: Close thisisalongfilenamesoicantesthowmanycharactersicanwrite by clicking on X'''
         
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        '''Deleted created Files'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="ThisIsAnExampleOfALongFolderName",click="Delete")
        time.sleep(2)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(2)
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)

if __name__=='__main__' :
    unittest.main()  