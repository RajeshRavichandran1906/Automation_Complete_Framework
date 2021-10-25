'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287603'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287603_TestClass(AS_BaseTestCase):
    def test_C2287603(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Domains, right click on ContextMenu>New>Procedure
                    Procedure View panel, right-click top level folder in Procedure View panel and select New... | Other
                    Click X on the Other component tab'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                              
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                     
        tree_path="Domains"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Procedure")
        time.sleep(2)
 
        as_utilobj.select_home_button(move_x=-52,move_y=170)
        time.sleep(1)
         
        as_utilobj.select_component_by_right_click(right_click_folder="Comment",click="New ...",click_sub_menu="Other")
        time.sleep(2)
         
        as_utilobj.select_home_button(move_x=482,move_y=137)
        time.sleep(1)
         
        as_utilobj.select_home_button(move_x=-52,move_y=170)
        time.sleep(1)
         
        as_utilobj.click_element_using_ui(tree_item="Comment")
         
        as_utilobj.Verify_Element("Other","Step 01: Verified that 'other' component has not added to the procedure tree",avaliable=True)
        time.sleep(2)
         
        '''Step 02: Right-click top level folder in Procedure View panel and select New... | Dialog Mngr>Dialogue Mngr
                    Click X on the Dialog Mngr... component tab'''
         
        as_utilobj.select_home_button(move_x=-52,move_y=170)
        time.sleep(1)
         
        as_utilobj.select_component_by_right_click(right_click_folder="Comment",send_keys=['down','right'],click="Dialogue Mngr",click_sub_menu="Dialogue Mngr")
        time.sleep(2)
         
        as_utilobj.select_home_button(move_x=515,move_y=137)
        time.sleep(1)

        as_utilobj.select_home_button(move_x=-52,move_y=170)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(tree_item="Comment")
        
        
        as_utilobj.Verify_Element("Dialogue Mngr","Step 02: Verified that dialogue manager component has not added to the procedure tree",unavailable=True)
        time.sleep(2)
        
        '''Step 03: Close Procedure1'''
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()