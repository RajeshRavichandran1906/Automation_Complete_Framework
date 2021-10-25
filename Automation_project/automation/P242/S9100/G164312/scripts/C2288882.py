'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288882'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2288882_TestClass(AS_BaseTestCase):
    def test_C2288882(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        
        '''Step 01: WebFOCUS Administration drop down menu, click on BI Portal
                    Expand Domains->CC App Studio
                    Right click on AS Framework->New-Blog
                    Type ASNewBlog and click OK'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                           
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
             
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(6)
           
        as_utilobj.select_component_by_right_click(right_click_folder='S9100',click="New",click_sub_menu='Blog')
        time.sleep(2)
           
        as_utilobj.select_any_dialog("OK",rename_file="AsNewBlog")
        time.sleep(5)
           
        '''Step 02: Close Comments - ASNewblog.blog window
                    Close WebFOCUS Home tab
                    In Environments Tree, set filter to Other Files
                    Select Refresh from the View Options'''
           
        as_utilobj.close_canvas_item()
        time.sleep(2)
          
        as_utilobj.select_component_by_right_click(right_click_folder='S9100',click="Refresh Descendants")
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_item='AsNewBlog',click="Properties")
        time.sleep(2)
         
        as_utilobj.Verify_Element("AsNewBlog","Step 02: Verified that the required ASNewBlog been created",available=True)
        time.sleep(2)
          
        '''Step 03: Right click on ASNewBlog and select Open
                    Close Comments - ASNewblog.blog tab'''
          
        as_utilobj.select_component_by_right_click(right_click_item="AsNewBlog",click="Open")
        time.sleep(7)
          
        as_utilobj.verify_active_tool("App Studio - Comments - AsNewBlog.blog","Step 03: Verified ASNewBlog file been invoked")
        time.sleep(1)
      
        as_utilobj.close_canvas_item()
        time.sleep(4)
          
        '''Step 04: In Environments Tree, double click on ASNewBlog
                    Close Comments - ASNewblog.blog tab'''
        
        tree_path="AsNewBlog"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(6)
        
        as_utilobj.verify_active_tool("App Studio - Comments - AsNewBlog.blog","Step 03: Verified ASNewBlog file been invoked")
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        '''Step 05: Verify the blog created on BI Portal is showing in your folder with AppStudio unique icon.'''
        
        as_utilobj.select_component_by_right_click(right_click_folder='AsNewBlog',click="Properties")
        time.sleep(2)
        
        as_utilobj.verify_picture_using_sikuli("step5_C2288882.png","Step 05: Verified that the required ASNewBlog icon been displayed")
        time.sleep(2)
        
        '''Delete the created blog'''
        
        as_utilobj.select_component_by_right_click(right_click_item='AsNewBlog',click='Delete')
        time.sleep(2)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  