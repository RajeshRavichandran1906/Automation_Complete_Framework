'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288418'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import keyboard as keys

class C2288418_TestClass(AS_BaseTestCase):
    def test_C2288418(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on AS Framework and select New-> Blog
                    Type NewBlog for File name
                    Click OK'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Blog")
        time.sleep(6)
        
        as_utilobj.select_any_dialog("OK",rename_file="NewBlog")
        time.sleep(6)
        
        as_utilobj.verify_active_tool("App Studio - Comments - NewBlog.blog","Step 01: Verified that NewBlog been created")
        time.sleep(1)
        
        '''Step 02: Close Comments - NewBlog.blog by clicking on X'''
        
        as_utilobj.close_canvas_item()
        time.sleep(4)
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(tree_item_select="NewBlog")
        time.sleep(1)
         
        as_utilobj.Verify_Element("NewBlog","Step 02: Verified NewBlog is closed and shown in the tree",available=True)
        time.sleep(2)
        
        '''Step 03: Right click on NewBlog and select Open
                    Click Add comment 
                    Type This is a New comment
                    Click on Post'''
        
        as_utilobj.select_component_by_right_click(right_click_item="NewBlog",click="Open")
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(text_click="Add comment...")
        time.sleep(2)

        keys.write("This is a New comment")
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(text_click="Post")
        time.sleep(2)
        
        as_utilobj.verify_text_appstudio_canvas("Step 03: Verified that comment been posted to the NewBlog",item_list=['Administrator','This is a New comment'])
        time.sleep(1)
        
        '''Step 04: Close Comments - NewBlog.blog by clicking on X'''
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        '''Created new blog file deleted for reason of next run'''
        
        as_utilobj.select_component_by_right_click(right_click_item="NewBlog",click="Delete")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        print("Note: Created new blog file deleted for reason of next run")
           
if __name__=='__main__' :
    unittest.main()      