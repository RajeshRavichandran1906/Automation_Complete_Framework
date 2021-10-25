'''@author: Adithyaa AK

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2223819'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_ribbon

class C2223819_TestClass(AS_BaseTestCase):
    def test_C2223819(self):
    
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_ribbon_obj=as_ribbon.AS_Ribbon(driver)
          
        as_utilobj.select_home_button()
        
        """Step 1. Press Alt key, press H (for Home), press RE for report wizard"""
        
        as_ribbon_obj.sendkeys_ribbon_shortcut('Report Wizard',"Step 01: Verify the dialog - 'Report Wizard' is displayed",key1='H',key2='re',key3='alt')
        time.sleep(3)
         
        """Step 2. Click Cancel to close dialog"""
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(2)
        
        """Step 3. Press Alt key, press H (for Home), press CH For chart wizard"""
        
        as_ribbon_obj.sendkeys_ribbon_shortcut('Chart Wizard',"Step 02: Verify the dialog - 'Chart Wizard' is displayed",key1='H',key2='ch',key3='alt')
        time.sleep(3)
         
        """Step 4. Click Cancel to close dialog"""
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(2)
        
        """Step 5. Press Alt key, press H (for Home), press HD For html\document"""
        
        as_ribbon_obj.sendkeys_ribbon_shortcut('HTML / Document Wizard',"Step 03: Verify the dialog - 'HTML / Document Wizard' is displayed",key1='H',key2='hd',key3='alt')
        time.sleep(3)
         
        """Step 6. Click Cancel to close dialog"""
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()