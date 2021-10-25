'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287588'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2287588_TestClass(AS_BaseTestCase):
    def test_C2287588(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        folders=["Domains","S9100"]
        sleep=[1,2,3,4,5,6,7,8,9] 
        
        '''Testcase verification'''
        
        verify_image="step1_C2287588.png"
        verify_html_tool="App Studio - HtmlPage1 (English)"
        verify_document_tool="App Studio - Document1"
        verify_msg_1="Step 01: Verify there is no display of the path that is clicked on in the tree"
        verify_msg_2="Step 02: Verify HTML page invoked"
        verify_msg_3="Step 03: Verify Document page invoked"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on AS Framework and select New | HTML/Document'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
                   
        as_utilobj.select_tree_view_pane_item(folders[0]) 
        time.sleep(sleep[4])
         
        as_utilobj.select_component_by_right_click(right_click_folder=folders[1],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_html_document)
        time.sleep(sleep[1])
         
        as_utilobj.verify_picture_using_sikuli(verify_image,verify_msg_1)
        time.sleep(sleep[2])
         
        '''Step 02: Click Next
                    Click Finish
                    Close HtmlPage1 tab'''
         
        as_utilobj.select_any_dialog(component_locators.next_button)
        time.sleep(sleep[0])
         
        as_utilobj.select_any_dialog(component_locators.finish_button)
        time.sleep(sleep[6])
         
        as_utilobj.verify_active_tool(verify_html_tool,verify_msg_2)
        time.sleep(sleep[1])
         
        as_utilobj.close_canvas_item()
        time.sleep(sleep[6])
         
        '''Step 03: Right click on AS Framework and select New | HTML/Document 
                    Select Document (PDF, Excel...) radio button
                    Click Next
                    Click Finish
                    Close Document2 tab'''
         
        as_utilobj.select_component_by_right_click(right_click_folder=folders[1],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_html_document)
        time.sleep(sleep[1])
         
        as_utilobj.click_element_using_ui(radio_button=component_locators.document_file_type)
        time.sleep(sleep[1])
         
        as_utilobj.select_any_dialog(component_locators.next_button)
        time.sleep(sleep[0])
         
        as_utilobj.select_any_dialog(component_locators.finish_button)
        time.sleep(sleep[5])
         
        as_utilobj.verify_active_tool(verify_document_tool,verify_msg_3)
        time.sleep(sleep[0])   
         
        as_utilobj.close_canvas_item()
        time.sleep(sleep[1]) 
        
if __name__=='__main__' :
    unittest.main() 