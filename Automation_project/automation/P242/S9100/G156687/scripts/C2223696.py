'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2223696'''

from common.lib.as_basetestcase import AS_BaseTestCase
from common.pages import as_ribbon
import time,unittest
from common.lib import as_utility

class C2223696_TestClass(AS_BaseTestCase):
    def test_C2223696(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_ribbon_obj= as_ribbon.AS_Ribbon(driver)
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
         
        as_utilobj.select_home_button()
        time.sleep(1)
            
        '''Verify DATA SubMenus tooltips'''
          
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Data','Synonym via Metadata Canvas',"Step 01: Verified Tooltip is Synonym via Metadata Canvas - create or open existing data source definitions",15,60,5,20)
        time.sleep(1)
           
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Data','Import Synonym',"Step 02: Verified Tooltip is Import Synonym - Import a data source definitions",15,60,5,40)
        time.sleep(1)
           
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Data','Manage Adapters',"Step 03: Verified Tooltip is Manage Adapters - Add new or manage existing adapter connections",15,60,5,70)
        time.sleep(1)
           
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Data','DBA Password',"Step 04: Verified Tooltip is DBA Password - Specify the DBA and user password for the data sources",15,60,5,85)
        time.sleep(1)
           
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Data','Rebuild FOCUS Data Source',"Step 05: Verified Tooltip is Rebuild FOCUS Data Source - Restructure a data source, rebuild indexes, or check the integrity of data sources",15,60,5,105)
        time.sleep(1)
         
        '''Verify DATA SubMenus'''
         
        as_ribbon_obj.Click_Ribbon_Dropdown('Home','Data','1','Data Source Definition Wizard','Cancel','Step 06: Verify the dialog - Data Source Definition Wizard is displayed',50,15)
        time.sleep(1)
         
        as_ribbon_obj.Click_Ribbon_Dropdown('Home','Data','1','Select Server Node','Cancel','Step 07: Verify the dialog - Select Server Node is displays',50,35)
        time.sleep(1)
         
        as_ribbon_obj.Click_Ribbon_Dropdown('Home','Data','1','Select Server Node','Cancel','Step 08:  Verify the dialog - Select Server Node is displayed',50,50)
        time.sleep(1)
         
        as_ribbon_obj.Click_Ribbon_Dropdown('Home','Data','1','Password Dialog','Cancel','Step 09: Verify the dialog - Password Dialog is displayed',50,75)
        time.sleep(1)
        
        as_ribbon_obj.Click_Ribbon_Dropdown('Home','Data','1','Rebuild','Cancel','Step 10: Verify the dialog - Rebuild is displayed',50,90)
        time.sleep(1) 
        
if __name__=='__main__' :
    unittest.main()