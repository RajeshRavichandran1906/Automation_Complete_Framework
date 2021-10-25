'''
@author: Adithyaa AK

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287642'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287642_TestClass(AS_BaseTestCase):
    def test_C2287642(self):
        
        '''Creating Object Instance'''
        
        driver = self.driver 
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
    
        '''Step01&02: In a configured WebFOCUS Environment, expand Data Servers>EDASERVE>Applications>ibisamp 
                    Right click on carinst.fex and select Open in Text Editor
                    Right click on cargraph.fex and select Open in Text Editor
                    In Edit carinst.fex, click next to END and hit enter 
                    In Edit carhraph.fex, click next to END and hit enter'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
        
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)

        tree_path="Domains"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
                         
        tree_path="Data Servers->EDASERVE->Applications->ibisamp"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_item="carinst.fex",click="Open in Text Editor")
        time.sleep(2) 
         
        as_utilobj.select_component_by_right_click(right_click_item="cargraph.fex",click="Open in Text Editor")
        time.sleep(2) 
        
        '''Step 03: In Domains, right click on Public and select ReportCaster Explorer
                    Click on Edit carinst.fex tab
                    Click AS menu->Save All
                    Click Yes on "All documents have been saved. Close all Documents?" prompt'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="ReportCaster Explorer")
        time.sleep(4) 
        
        as_utilobj.select_application_menu_options(send_keys=['down','down','down','down'])
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        as_utilobj.verify_active_tool("App Studio","Step 03: Verify Both editor tabs and ReportCaster Explorer are closed")
        time.sleep(1)
         
if __name__=='__main__' :
    unittest.main()