'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270473'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.pages import as_panels
from common.lib import as_utility

class C2270473_TestClass(AS_BaseTestCase):
    def test_C2270473(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_panels_obj= as_panels.AS_Panels(driver)
        as_utilobj=as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button() 
        time.sleep(1)
             
        '''Environments Detail_Menu_Tooltips'''
        
        as_panels_obj.Verify_Tooltip_Using_Name('View Options','Step 01: Verified Environments Detail Tooltip is View Options',move_x=2,move_y=2)
        time.sleep(1)
         
        as_panels_obj.Verify_Tooltip_Using_Name('All Files',"Step 02: Verified Environments Detail Tooltip is All Files - Show all content files",move_x=2,move_y=2)
        time.sleep(1)
         
        as_panels_obj.Verify_Tooltip_Using_Name('Procedure Files',"Step 03: Verified Environments Detail Tooltip is Procedure Files - Show only Procedure files",move_x=2,move_y=2)
        time.sleep(1)
         
        as_panels_obj.Verify_Tooltip_Using_Name('Master Files',"Step 04: Verified Environments Detail Tooltip is Master Files - Show only Master files",move_x=2,move_y=2)
        time.sleep(1)
         
        as_panels_obj.Verify_Tooltip_Using_Name('HTML Files',"Step 05: Verified Environments Detail Tooltip is HTML Files - Show only HTML files",move_x=2,move_y=2)
        time.sleep(1)
         
        as_panels_obj.Verify_Tooltip_Using_Name('Maintain Files',"Step 06: Verified Environments Detail Tooltip is Maintain Files - Show only Maintain files",move_x=2,move_y=2)
        time.sleep(1)
         
        as_panels_obj.Verify_Tooltip_Using_Name('Image Files',"Step 07: Verified Environments Detail Tooltip is Image Files - Show only Image files",move_x=2,move_y=2)
        time.sleep(1)
         
        as_panels_obj.Verify_Tooltip_Using_Name('ReportCaster Files',"Step 08: Verified Environments Detail Tooltip is ReportCaster Files - Show only ReportCaster files",move_x=2,move_y=2)
        time.sleep(1)
         
        as_panels_obj.Verify_Tooltip_Using_Name('Library Files',"Step 09: Verified Environments Detail Tooltip is Library Files - Show only Library files",move_x=2,move_y=2)
        time.sleep(1)
         
        as_panels_obj.Verify_Tooltip_Using_Name('Other Files',"Step 10: Verified Environments Detail Tooltip is Other files - Show only Other files",move_x=2,move_y=2)
        time.sleep(1)
       
        as_panels_obj.Verifypanel_Tooltip('-1','-22','Window Position',"Step 11: Verified Environments Detail Tooltip is Window Position",move_x=2,move_y=2)
        time.sleep(1)
        
        as_panels_obj.Verifypanel_Tooltip('17','0','Auto Hide',"Step 12: Verified Environments Detail Tooltip is Auto Hide",move_x=2,move_y=2)
        time.sleep(1)
        
        as_panels_obj.Verifypanel_Tooltip('17','0','Close',"Step 13: Verified Environments Detail Tooltip is Close",move_x=2,move_y=2)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()