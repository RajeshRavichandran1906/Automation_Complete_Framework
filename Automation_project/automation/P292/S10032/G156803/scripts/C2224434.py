'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2224434'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import keyboard as keys
from common.locators import as_uiautomation_mainpage_locators

class C2224434_TestClass(AS_BaseTestCase):
    def test_C2224434(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Testcase property variables'''
        
        webfocus_env_path="webfocus_environment"
        folder_path="Data Servers->EDASERVE->Applications"
        web_app_path="Web Applications"
        Folders=["Applications","newapp","nnewapp","Web Applications"]
        click_items=["New Application Directory","Rename","Delete","New Folder"]
        wait_time=[1,2,3,4,5,6] 
        press_enter="enter"
        rename_folder="nnewapp"
        
        '''Testcase verification'''

        verify_new_folder=["newapp","nnewapp"]
        verify_dialog="App Studio"
        verify_msg_1="Step 01: Verify new application is created with default name 'newapp' in edit mode."
        verify_msg_2="Step 02: Verify new app name changes as per edit."
        verify_msg_3="Step 03: Verify Both applications, the one created in Data Server and the one created in Web Applications, are showing in both locations."
        verify_msg_4="Step 04: Verify new applications are removed from the Web Application tree"
        verify_msg_5="Step 05: Verify new applications are removed from the Data tree"
        
        '''Testscript'''
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, expand Data Servers->EDASERVE->Applications
                    Right click Applications and select New Application Directory'''
        
#         as_utilobj.logout_conf_env(webfocus_environment=True)
#         time.sleep(wait_time[2])
#                                       
#         tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(wait_time[2])
#           
#         tree_path=folder_path
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(wait_time[2])
#         
#         as_utilobj.select_component_by_right_click(right_click_folder=Folders[0],click=click_items[0])
#         time.sleep(wait_time[2])
#         
#         keys.press(press_enter)
#         time.sleep(wait_time[1])
#         
#         as_utilobj.Verify_Element(verify_new_folder[0],verify_msg_1,available=True)
#         time.sleep(wait_time[1])
#         
#         '''Step 02: Rename the new application
#                     Type nnewapp
#                     Hit Enter
#                     Collapse Data Servers'''
#         
#         as_utilobj.select_component_by_right_click(right_click_folder=Folders[1],click=click_items[1])
#         time.sleep(wait_time[2])
#         
#         keys.write(rename_folder)
#         time.sleep(wait_time[0])
#         
#         keys.press(press_enter)
#         time.sleep(wait_time[2])
#         
#         as_utilobj.Verify_Element(verify_new_folder[1],verify_msg_2,available=True)
#         time.sleep(wait_time[1])
        
        '''Step 03: Right click on Web Applications->New Folder'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[2])
                                      
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[2])
        
        as_utilobj.select_tree_view_pane_item(web_app_path) 
        time.sleep(wait_time[2])
        
        as_utilobj.select_component_by_right_click(right_click_folder=web_app_path,click=click_items[3])
        time.sleep(wait_time[2])
        
        keys.press(press_enter)
        time.sleep(wait_time[1])
        
        as_utilobj.Verify_Element(verify_new_folder[0],verify_msg_3,available=True)
        time.sleep(wait_time[1])
        
        '''Step 04: Right click on newapp and select Delete
                    Click Yes in App Studio message prompt
                    Right click on nnewapp and select Delete
                    Click Yes in App Studio message prompt'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=Folders[1],click=click_items[2])
        time.sleep(wait_time[2])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_4)
        time.sleep(wait_time[0])
        
        as_utilobj.select_any_dialog(locators.yes_button)
        time.sleep(wait_time[1])
        
        '''Step 05: Collapse Web Applications 
                    In Environments Tree-View Options->Refresh View
                    Expand EDASERVE->Applications
                    Collapse Data Servers'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[2])
                                      
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[2])
          
        as_utilobj.select_tree_view_pane_item(folder_path) 
        time.sleep(wait_time[2])
        
        as_utilobj.Verify_Current_Dialog_Closes(verify_new_folder[1],verify_msg_5)
        time.sleep(wait_time[0])
        
if __name__=='__main__' :
    unittest.main()  