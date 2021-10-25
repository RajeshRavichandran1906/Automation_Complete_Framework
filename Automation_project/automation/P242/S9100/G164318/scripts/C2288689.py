'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288689'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators,as_uiautomation_mainpage_locators
from common.pages import as_panels

class C2288689_TestClass(AS_BaseTestCase):
    def test_C2288689(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        as_panels_obj=as_panels.AS_Panels(driver)
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_ibisamp="Web Applications->ibisamp"
        select_wfmstart_html="wfmstart.html"
        baseapp="baseapp"
        
        '''Testcase verification'''
        
        verify_msg_1="Step 01: Verify copied wfmstart.html file been pasted into the baseapp folder"
        verify_msg_2="Step 02: Verify copied wfmstart.html file been deleted"   
                
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, set Filter to HTML Files 
                    Web Applications, double click on ibisamp 
                    Right click on wfmstart.html and select copy
                    Right click on baseapp and select Paste'''
        
        as_panels_obj.environment_panel_file_filter(filter=locators.html_files)
        time.sleep(1)
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.select_tree_view_pane_item(expand_ibisamp) 
        time.sleep(3)
#                        
        as_utilobj.select_component_by_right_click(right_click_item=select_wfmstart_html,click=component_locators.copy)
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_item=baseapp,click=component_locators.paste)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_1,tree_item=select_wfmstart_html,available=True)
        time.sleep(2)
        
        '''Step 02: Web Applications, baseapp
                    Right click on wfmstart.html and select Delete
                    Click Yes in App Studio delete prompt message'''
        
        as_utilobj.select_component_by_right_click(right_click_item=select_wfmstart_html,click=component_locators.delete)
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_2,tree_item=select_wfmstart_html,unavailable=True)
        time.sleep(2)
        
        as_panels_obj.environment_panel_file_filter(filter=locators.all_files_filter)
        time.sleep(1)
         
if __name__=='__main__' :
    unittest.main()