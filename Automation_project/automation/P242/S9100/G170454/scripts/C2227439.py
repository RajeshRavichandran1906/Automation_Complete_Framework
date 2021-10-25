'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227439'''

from common.lib.as_basetestcase import AS_BaseTestCase
from common.pages import as_panels,as_ribbon
import time,unittest
from common.lib import as_utility

class C2227439_TestClass(AS_BaseTestCase):
    def test_C2227439(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_panels_obj= as_panels.AS_Panels(driver)
        as_utilobj=as_utility.AS_Utillity_Methods(driver)
        as_ribbon_obj=as_ribbon.AS_Ribbon(driver)
        
        as_utilobj.select_home_button()
        
        as_ribbon_obj.verify_click_checkbox("Checked",click="Environments Tree")
        time.sleep(1)
                         
        '''Environments Tree_Menu_Tooltips'''
                 
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                      
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
             
        as_panels_obj.Verify_Tooltip_Using_Name('View Options',"Step 01: Verified Environments Tree Tooltip is View Options",move_x=2,move_y=2)
        time.sleep(2)
               
        as_panels_obj.Verify_Tooltip_Using_Name('All Files',"Step 02: Verified Environments Tree Tooltip is All Files - Show all content files",move_x=2,move_y=2)
        time.sleep(2)
           
        as_panels_obj.Verify_Tooltip_Using_Name('Procedure Files',"Step 03: Verified Environments Tree Tooltip is Procedure Files - Show only Procedure files",move_x=2,move_y=2)
        time.sleep(2)
                
        as_panels_obj.Verify_Tooltip_Using_Name('Master Files',"Step 04: Verified Environments Tree Tooltip is Master Files - Show only Master files",move_x=2,move_y=2)
        time.sleep(1)
                
        as_panels_obj.Verify_Tooltip_Using_Name('HTML Files',"Step 05: Verified Environments Tree Tooltip is HTML Files - Show only HTML files",move_x=2,move_y=2)
        time.sleep(1)
                
        as_panels_obj.Verify_Tooltip_Using_Name('Maintain Files',"Step 06: Verified Environments Tree Tooltip is Maintain Files - Show only Maintain files",move_x=2,move_y=2)
        time.sleep(2)
                
        as_panels_obj.Verify_Tooltip_Using_Name('Image Files',"Step 07: Verified Environments Tree Tooltip is Image Files - Show only Image files",move_x=2,move_y=2)
        time.sleep(2)
                
        as_panels_obj.Verify_Tooltip_Using_Name('ReportCaster Files',"Step 08: Verified Environments Tree Tooltip is ReportCaster Files - Show only ReportCaster files",move_x=2,move_y=2)
        time.sleep(2)
                
        as_panels_obj.Verify_Tooltip_Using_Name('Library Files',"Step 09: Verified Environments Tree Tooltip is Library Files - Show only Library files",move_x=2,move_y=2)
        time.sleep(2)
             
        as_panels_obj.Verify_Tooltip_Using_Name('Other Files',"Step 10: Verified Environments Tree Tooltip is Other files - Show only Other files",move_x=2,move_y=2)
        time.sleep(2)
            
        as_panels_obj.Verifypanel_Tooltip('-22','-22','Window Position',"Step 11: Verified Environments Tree Tooltip is Window Position",move_x=4,move_y=4)
        time.sleep(2)
            
        as_panels_obj.Verifypanel_Tooltip('17','0','Auto Hide',"Step 12: Verified Environments Tree Tooltip is Auto Hide",move_x=4,move_y=4)
        time.sleep(1)
            
        as_panels_obj.Verifypanel_Tooltip('17','0','Close',"Step 13: Verified Environments Tree Tooltip is Close",move_x=4,move_y=4)
        time.sleep(2)
        
                 
if __name__=='__main__' :
    unittest.main()  