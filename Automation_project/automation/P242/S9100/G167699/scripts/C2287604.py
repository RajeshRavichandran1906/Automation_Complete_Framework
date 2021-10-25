'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287604'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import uiautomation as automation

class C2287604_TestClass(AS_BaseTestCase):
    def test_C2287604(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Test Case Property Variables'''
        
        webfocus_env_path="webfocus_environment"
        base_folder_path="Domains->S9100"
        base_folder="S9100"
        
        '''Test Case Verifications'''
        
        verify_comments="step2_C2287604.png"
        verify_comments_posted="step3_C2287604.png"
        verify_msg_1="Step 01: Verify new blog is created with the default name"
        verify_msg_2="Step 02: Verify comments added successfully"
        verify_msg_3="Step 03: Verify comments are posted in blog"
        verify_msg_4="Step 04: Verify Blog has been added under domains"
        
        '''Test Script'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, right-click AS Framework and select New | Blog
                    Click OK to accept the default provided file name'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                             
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
          
        as_utilobj.select_tree_view_pane_item(base_folder_path)
        time.sleep(3)
         
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_blog)
        time.sleep(5)
         
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(25)
         
        as_utilobj.verify_active_tool("App Studio - Comments - Blog1.blog",verify_msg_1)
        time.sleep(2)
         
        '''Step 02: Click "Add comment" in the blog tool
                    Type the following:
                    comment=first comment 
                    tag=first tag'''
         
        as_utilobj.click_element_using_ui(text_click="Add comment...")
        time.sleep(5)
         
        text_to_type=['comment=first comment','tag=first tag']
        for text in text_to_type:
            automation.SendKeys(text,waitTime=8)
            automation.SendKey(automation.Keys.VK_ENTER,waitTime=1)
         
        as_utilobj.verify_picture_using_sikuli(verify_comments,verify_msg_2) 
        time.sleep(3)
         
        '''Step 03: Click Post'''
         
        as_utilobj.select_home_button(move_x=1200,move_y=640)
        time.sleep(2)
            
        as_utilobj.verify_picture_using_sikuli(verify_comments_posted,verify_msg_3)
        time.sleep(5)
             
        '''Step 04: Click X on the Comments - Blog1.blog tab
                    Right click on Blog1 and select Delete
                    Click Yes in App Studio delete prompt message'''
         
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_item="Blog1",click=component_locators.properties_button)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_4,tree_item="Blog1",available=True)
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_item="Blog1",click="Delete")
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()  