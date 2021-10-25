'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6461026'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators

class C6461026_TestClass(AS_BaseTestCase):
    def test_C6461026(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        webfocus_env_path="webfocus_environment"
        folder_path="Domains->P292_S10032_G156803"
        Folders=["FrameWork","Comment","ibisamp"]
        files=["car.mas","Procedure1"]
        click_items=["COUNTRY","CAR","SALES"]
        procedure_view_panel=[-52,170]
        press_keys=["down","down","down","down","down","down","down"]
        wait_time=[1,2,3,4,5,6,7,8,9] 
        
        '''Testcase verification'''

        verify_image="step3_C6461026.png"
        verify_msg_1="Step 01: Verify procedure canvas opens"
        verify_msg_2="Step 03: Verify WebFOCUS Report tab"
        verify_msg_4="Note: Created Procedure file been deleted for reason of next run"
        verify_tool="App Studio - Procedure1"
        
        '''Testscript'''
    
        as_utilobj.select_home_button()
        time.sleep(wait_time[0])
        
        '''Step 01: In Environments Tree, Domains, expand P292_S10032_G156803
                    Right click on Framework folder and select New-> Procedure 
                    Click Procedure View panel'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[2])
                                      
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[2])
          
        tree_path=folder_path
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[2])
        
        as_utilobj.select_component_by_right_click(right_click_folder=Folders[0],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_procedure)
        time.sleep(wait_time[3])
         
        as_utilobj.verify_active_tool(verify_tool,verify_msg_1)
        time.sleep(wait_time[1])

        as_utilobj.select_home_button(move_x=procedure_view_panel[0],move_y=procedure_view_panel[1])
        time.sleep(wait_time[0])
        
        '''Step 02: Right click on Comment and select New->Report
                    Click ibisamp->car.mas
                    Click Finish'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=Folders[1],click=component_locators.comments_new,click_sub_menu=component_locators.new_report)
        time.sleep(wait_time[3])
        
        as_utilobj.select_file_in_dialogs(locators.ok_button,tree_path=Folders[2],select_file=files[0])
        time.sleep(wait_time[2])
        
        '''Step 03: Double click on COUNTRY, CAR and SALES
                    Click on Run icon from QAT
                    Close WebFOCUS Report tab output'''
        
        as_utilobj.click_element_using_ui(tree_item=click_items[0])
        time.sleep(wait_time[0])
        
        as_utilobj.click_element_using_ui(tree_item=click_items[1])
        time.sleep(wait_time[0])
         
        as_utilobj.click_element_using_ui(tree_item=click_items[2])
        time.sleep(wait_time[0])
        
        as_utilobj.click_element_using_ui(split_button=locators.run_button)
        time.sleep(wait_time[8])
        
        as_utilobj.verify_picture_using_sikuli(verify_image,verify_msg_2)
        time.sleep(wait_time[2])
     
        as_utilobj.Verify_Browser_Content(locators.ie_browser_classname,msg=None,browser_close=True)
        time.sleep(wait_time[3])
         
        '''Step 04: Close Procedure1 tab
                    Click Yes to App Studio saving prompt
                    Click OK'''
         
        as_utilobj.select_application_menu_options(send_keys=press_keys)
        time.sleep(wait_time[0])
         
        as_utilobj.select_any_dialog(locators.yes_button)
        time.sleep(wait_time[0])
         
        as_utilobj.select_any_dialog(locators.ok_button)
        time.sleep(wait_time[0])
         
        '''Step 05: Created File been deleted for reason of next run'''
         
        as_utilobj.select_component_by_right_click(right_click_item=files[1],click=component_locators.delete)
        time.sleep(wait_time[3])
         
        as_utilobj.select_any_dialog(locators.yes_button)
        time.sleep(wait_time[0])
         
        print(verify_msg_4)
         
if __name__=='__main__' :
    unittest.main()     