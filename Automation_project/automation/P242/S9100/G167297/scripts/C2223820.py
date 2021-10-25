'''
@author: Adithyaa

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2223820
'''
from common.lib.as_basetestcase import AS_BaseTestCase
import unittest, time
from common.lib import as_utility

class C2223820_TestClass(AS_BaseTestCase):
    def test_C2223820(self):
    
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 01. Select first option under Data, Synonym via Metadata Canvas'''
        
        as_utilobj.click_element_using_ui(split_button="Data",send_keys=['down','enter'],x=0.25,y=0.85)
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Data Source Definition Wizard","Step 01: Verify Data Source Definition Wizard opens")
        
        '''Step 2. Click Cancel to close dialog'''
        
        as_utilobj.select_any_dialog("Cancel")
        
        as_utilobj.Verify_Current_Dialog_Closes("Data Source Definition Wizard","Step 02: Verify Data Source Definition window closes")
        time.sleep(1)

        '''Step 3. Click down arrow for Data in the Home Ribbon and select the second option, Synonym'''
        
        as_utilobj.click_element_using_ui(split_button="Data",send_keys=['down','down','enter'],x=0.25,y=0.85)
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Select Server Node","Step 03: Verify Select Server Node dialog opens. If a Data Servers location is hi-lited in the environment tree, the same location will be hi-lited in the Select Server Node tree.")
        
        '''Step 4. Click Cancel on dialog'''
        
        as_utilobj.select_any_dialog("Cancel")
        
        as_utilobj.Verify_Current_Dialog_Closes("Select Server Node","Step 04: Verify Select Server Node Dialog closes")
        time.sleep(1)
        
        '''Step 5. Click down arrow for Data in the Home Ribbon and select the third option, Manage Adapters'''
        
        as_utilobj.click_element_using_ui(split_button="Data",send_keys=['down','down','down','enter'],x=0.25,y=0.85)
        time.sleep(1)
    
        as_utilobj.Verify_Current_Dialog_Opens("Select Server Node","Step 05: Verify Select Server Node dialog opens for manage adapters option")
        
        '''Step 6. Click Cancel to close dialog'''
        
        as_utilobj.select_any_dialog("Cancel")
        
        as_utilobj.Verify_Current_Dialog_Closes("Select Server Node","Step 06: Verify Select Server Node Dialog closes")
        time.sleep(1)
        
        '''Step 7. Click down arrow for Data in the Home Ribbon and select fourth option, Data Source Password'''
        
        as_utilobj.click_element_using_ui(split_button="Data",send_keys=['down','down','down','down','enter'],x=0.25,y=0.85)
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Password Dialog","Step 07: Verify 'Password Dialog' is displayed")

        '''Step 8. Click Cancel to close it'''
        
        as_utilobj.select_any_dialog("Cancel")
        
        as_utilobj.Verify_Current_Dialog_Closes("Password Dialog","Step 08: Verify Verify 'Password Dialog' closes")
        time.sleep(1)
        
        '''Step 9. Click down arrow for Data in the Home Ribbon and select the last option, Rebuild Data Source.'''
        
        as_utilobj.click_element_using_ui(split_button="Data",send_keys=['down','down','down','down','down','enter'],x=0.25,y=0.85)
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Rebuild","Step 09: Verify the dialog - 'Rebuild' is displayed")
        
        '''Step 10. Click Cancel to close dialog'''
        
        as_utilobj.select_any_dialog("Cancel")
        
        as_utilobj.Verify_Current_Dialog_Closes("Rebuild","Step 10: Verify 'Rebuild' closes")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  