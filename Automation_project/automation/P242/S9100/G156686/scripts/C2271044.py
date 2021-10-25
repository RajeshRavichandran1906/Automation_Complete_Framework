'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2271044'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_ribbon

class C2271044_TestClass(AS_BaseTestCase):
    def test_C2271044(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        as_ribbon_obj= as_ribbon.AS_Ribbon(driver)
        
        as_utilobj.select_home_button()
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains->S9100->Report1"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)

        '''Verify Quick Access Toolbar Tooltips'''        
                
        as_ribbon_obj.Verify_Single_Tooltip('Home','Application Menu',"Step 01: Verify Tooltip is Application Menu - Application Menu",move_x=5,move_y=5)
        time.sleep(1)
        as_ribbon_obj.Verify_Singlediff_Tooltip('Home','Open...','Open (Ctrl+O)',"Step 02: Verify Tooltip is Open (Ctrl+O) - Open an existing document",move_x=5,move_y=5)
        time.sleep(1)
        as_ribbon_obj.Verify_Singlediff_Tooltip('Home','Save','Save (Ctrl+S)',"Step 03: Verify Tooltip is Save (Ctrl+S) - Save the active document",move_x=5,move_y=5)
        time.sleep(1)
        as_ribbon_obj.Verify_Single_Tooltip('Home','Save All',"Step 04: Verify Tooltip is Save All - Save all active documents",move_x=5,move_y=5)
        time.sleep(1)
        as_ribbon_obj.Verify_Single_Tooltip('Home','Quick Print',"Step 05: Verify Tooltip is Save All - Print the active documents using current options",move_x=5,move_y=5)
        time.sleep(1)
        as_ribbon_obj.Verify_Singlediff_Tooltip('Home','Undo','Undo (Ctrl+Z)',"Step 06: Verify Tooltip is Undo (Ctrl+Z) - Undo the last action",move_x=5,move_y=5)
        time.sleep(1)
        as_ribbon_obj.Verify_Singlediff_Tooltip('Home','Redo','Redo (Ctrl+Y)',"Step 07: Verify Tooltip is Redo (Ctrl+Y) - Redo the previously undone action",move_x=5,move_y=5)
        time.sleep(1)
        as_ribbon_obj.Verify_Singlediff_Tooltip('Home','Cut','Cut (Ctrl+X)',"Step 08: Verify Tooltip is Cut (Ctrl+X) - Cut the selection and put it on the Clipboard",move_x=5,move_y=5)
        time.sleep(1)
        as_ribbon_obj.Verify_Singlediff_Tooltip('Home','Copy','Copy (Ctrl+C)',"Step 09: Verify Tooltip is Copy (Ctrl+C) - Copy the selection and put it on the Clipboard",move_x=5,move_y=5)
        time.sleep(1)
        as_ribbon_obj.Verify_Singlediff_Tooltip('Home','Paste','Paste (Ctrl+V)',"Step 10: Verify Tooltip is Paste (Ctrl+V) - Insert Clipboard Contents",move_x=5,move_y=5)
        time.sleep(1)
        as_ribbon_obj.Verify_Singlediff_Tooltip('Home','Run','Run (F5)',"Step 11: Verify Tooltip is Run (F5) - Executes open component",move_x=5,move_y=5)
        time.sleep(1)
                 
        '''Run Icon Drop Down'''

        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Run','Message Viewer OFF','Step 12: Verify Run Tooltip is Message Viewer OFF - Do not Display any messages',25,6, 10,45)
        time.sleep(1)
        
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Run','Message Viewer ON','Step 13: Verify Run Tooltip is Message Viewer ON - Display messages in seprate frame below the report output',25,6, 10,65)
        time.sleep(1)
        
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Run','Display command lines','Step 14: Verify Run Tooltip is Display command lines - Displays messages and lines in a separate frame below the report output that are expanded and stacked for execution',25,6, 10,85)
        time.sleep(1)
        
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Run','Display Dialogue Manager commands','Step 15: Verify Run Tooltip is Display Dialogue Manager commands - Displays messages and lines in a separate frame below the report output that are expanded and stacked for execution while also displaying all Dialogue Manager commands',25,6, 10,105)
        time.sleep(1)
        
        as_ribbon_obj.Verify_Single_Tooltip('Home','Customize Quick Access Toolbar',"Step 16: Verify Tooltip is Customize Quick Access Toolbar",move_x=5,move_y=5)
        time.sleep(2)

        as_utilobj.close_canvas_item()
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()