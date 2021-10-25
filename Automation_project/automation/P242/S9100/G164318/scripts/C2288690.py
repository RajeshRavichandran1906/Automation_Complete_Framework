'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288690'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators,as_uiautomation_mainpage_locators
import uiautomation as automation

class C2288690_TestClass(AS_BaseTestCase):
    def test_C2288690(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        write_c2288690="c2288690{Enter}"
        c2288690="c2288690"
        
        '''Testcase verification''' 
        
        verify_html_page="App Studio - Edit HtmlPage1.htm"
        verify_java_script_file="App Studio - JavaScriptFile1.js"
        verify_cascading_style_sheet="App Studio - CascadingStyleSheet1.css"
        verify_msg_1="Step 01: Verify new html file been invoked"
        verify_msg_2="Step 02: Verify new javascript file been invoked"
        verify_msg_3="Step 03: 05: Verify new cascading stylesheet been invoked"
                
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, set Filter to Other Files
                    Right click Web Applications and select New Folder
                    Hit Enter
                    Right click on newapp and select New HTML Page
                    Close Edit HtmlPage1.htm tab'''
           
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                       
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                
        as_utilobj.select_component_by_right_click(right_click_folder=locators.web_application,click=component_locators.new_folder_under_webapp)
        time.sleep(3)
         
        automation.SendKeys(write_c2288690,waitTime=2)
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_folder=c2288690,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_html_page)
        time.sleep(3)
        
        as_utilobj.verify_active_tool(verify_html_page,verify_msg_1)
        time.sleep(2)

        as_utilobj.close_canvas_item()
        time.sleep(3)
         
        '''Step 02: Right click on newapp and select New->JavaScript File
                    Close JavaScript1.js tab'''
         
        as_utilobj.select_component_by_right_click(right_click_folder=c2288690,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_javascript_file)
        time.sleep(1)
         
        as_utilobj.verify_active_tool(verify_java_script_file,verify_msg_2)
        time.sleep(2)

        as_utilobj.close_canvas_item()
        time.sleep(3)

        '''Step 03: Right click on newapp and select New-> Cascading Style Sheet
                    Close CascadingStyleSheet1.css tab'''
         
        as_utilobj.select_component_by_right_click(right_click_folder=c2288690,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_cascading_style_sheet)
        time.sleep(1)
        
        as_utilobj.verify_active_tool(verify_cascading_style_sheet,verify_msg_3)
        time.sleep(2)

        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder=c2288690,click=component_locators.delete)
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()