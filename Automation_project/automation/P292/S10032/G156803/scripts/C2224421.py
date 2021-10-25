'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2224421'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys
from common.locators import as_uiautomation_mainpage_locators
import uiautomation as automation

class C2224421_TestClass(AS_BaseTestCase):
    def test_C2224421(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Testcase property variables'''
        
        webfocus_env_path="webfocus_environment"
        key_pattern=['down']
        tree_path_1="Domains->P292_S10032_G156803->FrameWork"
        tree_path_2="FrameWork"
        tree_path_3="Data Servers->EDASERVE->Applications->ibisamp"
        id_combo_box="1515"
        wait_time=[1,2,3,4]
        hot_key_1='esc'
        
        '''Testcase verification'''
        
        verify_dialog="Open File"
        verify_image=["step1_C2224421.png","step2_C2224421.png","step3_C2224421.png","step4_C2224421.png","step5_C2224421.png","step6_C2224421.png"]
        verify_msg_1="Step 1: Verify elements located in dropdown of 'View Options'"
        verify_msg_2="Step 2.1: Verify that open file dialog invokes"
        verify_msg_3="Step 2.2: Verify current location is highlighted in the left pane. Under the file type drop down menu, Procedure Files is selected by default and required files types avaliable in drop down"
        verify_msg_4="Step 3&4: Verify current location is highlighted in the left pane of Open File Dialog. Verify Only javascript files is displayed in file list"
        verify_msg_5="Step 5&6: Verify current location is highlighted in the left pane of Open File Dialog. Verify Only text files is displayed in file list"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree panel, click the View Options icon'''
           
        as_utilobj.click_element_using_ui(menu_item=True,name=locators.view_option_menu_item)
        time.sleep(wait_time[3])
        
        as_utilobj.verify_picture_using_sikuli(verify_image[0],verify_msg_1)
        time.sleep(2)
           
        keys.hotkey(hot_key_1)
        time.sleep(wait_time[0])
          
        '''Step 02: In Environments Tree, expand Configured Environments-> Domains -> Select P292_S10032_G156803
                    Click the AS logo and select Open'''
          
#         as_utilobj.logout_conf_env(webfocus_environment=True)
#         time.sleep(wait_time[2])
                                      
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[2])
          
        as_utilobj.select_tree_view_pane_item(tree_path_1) 
        time.sleep(wait_time[2])
         
        as_utilobj.select_application_menu_options(send_keys=key_pattern)
        time.sleep(wait_time[0])
         
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_2)
        time.sleep(wait_time[0])
        
        as_utilobj.click_element_using_ui(combo_box=id_combo_box)
        time.sleep(wait_time[3])
          
        as_utilobj.verify_picture_using_sikuli(verify_image[1],verify_msg_3)
        time.sleep(wait_time[0])
         
        keys.hotkey(hot_key_1)
        time.sleep(wait_time[0])
         
        '''Step 03: Close the Open File dialog window
                    Expand P292_S10032_G156803 Domains
                    Select Framework
                    Click the AS logo and select Open.'''
          
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(wait_time[0])
        
        as_utilobj.select_tree_view_pane_item(tree_path_2) 
        time.sleep(wait_time[3])
        
        as_utilobj.verify_picture_using_sikuli(verify_image[2],verify_msg_3)
        time.sleep(wait_time[0])
          
        as_utilobj.select_application_menu_options(send_keys=key_pattern)
           
        '''Step 04: In the Open File dialog, click on the drop down next to Procedure Files and select JavaScript Files(*.js)
                    Click Cancel'''
           
        as_utilobj.click_element_using_ui(combo_box=id_combo_box)
        time.sleep(wait_time[0])
           
        as_utilobj.click_element_using_ui(list_item=locators.javascript)
        time.sleep(wait_time[3])
         
        as_utilobj.verify_picture_using_sikuli(verify_image[3],verify_msg_4)
        time.sleep(wait_time[0])
         
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(wait_time[0])
         
        '''Step 05: Navigate to Data Servers->EDASERVE->Applications
                    Select ibisamp
                    Click the AS logo and select Open.'''
        
        as_utilobj.select_tree_view_pane_item(tree_path_3)
        time.sleep(wait_time[3])
        as_utilobj.verify_picture_using_sikuli(verify_image[4],verify_msg_4)
        time.sleep(wait_time[0])
        
        as_utilobj.select_application_menu_options(send_keys=key_pattern)
        time.sleep(wait_time[0])
        
        '''Step 06: In the Open File dialog, click on the drop down next to Procedure Files and select Text Documents (*.txt)
                    Click Cancel
                    Collapse Data Servers'''
        
        as_utilobj.click_element_using_ui(combo_box=id_combo_box)
        time.sleep(wait_time[0])
          
        as_utilobj.click_element_using_ui(list_item=locators.text_document)
        time.sleep(wait_time[3])
        
        as_utilobj.verify_picture_using_sikuli(verify_image[5],verify_msg_5)
        time.sleep(wait_time[0])
        
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(wait_time[0])

if __name__=='__main__' :
    unittest.main()   