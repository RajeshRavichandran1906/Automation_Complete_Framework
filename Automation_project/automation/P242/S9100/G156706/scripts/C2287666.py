'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287666'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators

class C2287666_TestClass(AS_BaseTestCase):
    def test_C2287666(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        click_ibisamp_folder="ibisamp"
        car_master_file="car.mas"
        created_report_file="Report2.fex"
        wait_time=[1,2,3,4,5,6,7,8,9,10,11] 
        select_initial_repository="Domains->S9100"
        
        '''Testcase verification'''
        
        verify_report_wizard="Report Wizard"
        verify_select_procedure_location="Report Wizard - Select Procedure Location"
        verify_select_data_source="Select Data Source"
        verify_report_component_canvas="App Studio - Report2*"
        verify_error_message="The 'IBFS:/unxrh7/WFC/Repository/S9100/Report2.fex' file no longer exists"
        verify_msg_1="Step 01: Verify Report Wizard opening dialog appears"
        verify_msg_2="Step 02: Verify Report Wizard - Select Procedure Location opens with AS Framework folder hi-lighted"
        verify_msg_3="Step 03: Verify Select Data Source dialolg opens. AS Framework folder hi-lighted"
        verify_msg_4="Step 04: Verify Top level tab 'Report2*' opens. Report component canvas opens"
        verify_msg_5="Step 06: Verify Report Wizard opening dialog appears again"
        verify_msg_6="Step 07: Verify Error message [location]/Report4.fex file no longer exists"
        verify_msg_7="Step 08: Verify Top level tab 'Report2*' opens. Report component canvas opens"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, select AS Framework
                    Click Report on ribbon bar (Content section)'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[2])
                  
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[2])
                  
        as_utilobj.select_tree_view_pane_item(select_initial_repository) 
        time.sleep(wait_time[4])
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.report_button)
        time.sleep(wait_time[0])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_report_wizard,verify_msg_1)
        time.sleep(wait_time[1])
        
        '''Step 02: Click Create Report button'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=component_locators.create_new_report)
        time.sleep(wait_time[0])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_select_procedure_location,verify_msg_2)
        time.sleep(wait_time[1])
        
        '''Step 03: Click Next'''
        
        as_utilobj.select_any_dialog(component_locators.next_button)
        time.sleep(wait_time[1])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_select_data_source,verify_msg_3)
        time.sleep(wait_time[1])
        
        '''Step 04: Click ibisamp 
                    Click car.mas
                    Click Finish'''
        
        as_utilobj.select_file_in_dialogs(component_locators.finish_button,tree_path=click_ibisamp_folder,select_file=car_master_file)
        time.sleep(wait_time[0])
        
        as_utilobj.verify_active_tool(verify_report_component_canvas,verify_msg_4)
        time.sleep(wait_time[0])
        
        '''Step 05: Click Report4* X to close it.'''
        
        as_utilobj.close_canvas_item() 
        time.sleep(wait_time[6])
        
        '''Step 06: Click Report on ribbon bar (Content section)'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.report_button)
        time.sleep(wait_time[0])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_report_wizard,verify_msg_5)
        time.sleep(wait_time[1])
        
        '''Step 07: Under Recent Reports section, double-click Report4.fex 
                    Click OK on error message
                    Click Create Report
                    Click Next'''
        
        as_utilobj.click_element_using_ui(list_item_double_click=created_report_file)
        time.sleep(wait_time[0])
        
        as_utilobj.Verify_Element(verify_error_message,verify_msg_6,available=True)
        time.sleep(wait_time[0])
        
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(wait_time[2])
        
        as_utilobj.click_element_using_ui(button_item=True,name=component_locators.create_new_report)
        time.sleep(wait_time[0])
        
        as_utilobj.select_any_dialog(component_locators.next_button)
        time.sleep(wait_time[1])
        
        '''Step 08: Click ibisamp 
                    Click car.mas
                    Click Finish'''
        
        as_utilobj.select_file_in_dialogs(component_locators.finish_button,tree_path=click_ibisamp_folder,select_file=car_master_file)
        time.sleep(wait_time[0])
        
        as_utilobj.verify_active_tool(verify_report_component_canvas,verify_msg_7)
        time.sleep(wait_time[0])
        
        '''Step 09: Click X on Report4* tab'''
        
        as_utilobj.close_canvas_item() 
        time.sleep(wait_time[3])
        
if __name__=='__main__' :
    unittest.main() 