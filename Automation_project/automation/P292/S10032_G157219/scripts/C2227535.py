'''
Created on 02-Feb-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227535
TestCase Name = Verify Document with adding/switching to another master file
'''
import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase

class C2227535_TestClass(BaseTestCase):

    def test_C2227535(self):
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """ 1. Launch IA Document mode: http://machine:port/ibi_apps/ia?tool=Document&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032 """
        utillobj.infoassist_api_login('document','ibisamp/car','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document') 
        
        """ 2. Verify "Data" pane contains fields from CAR.MAS. """
        metaobj.verify_data_pane_field('Dimensions', 'COUNTRY', 1, "Step 02a")
        metaobj.verify_data_pane_field('Measures/Properties', 'DEALER_COST', 2, "Step 02b")
                
        """ 3. Select "Data" > "Add". """
        ribbonobj.select_ribbon_item("Data", "Add")
        
        """ 4. Select EMPDATA.MAS. """
        file_name_input_css="#IbfsOpenFileDialog7_cbFileName input" 
        self.driver.find_element_by_css_selector(file_name_input_css).click()
        time.sleep(2)   
        utillobj.select_masterfile_in_open_dialog('ibisamp', 'employee') 
        #utillobj.ibfs_save_as("employee")
        time.sleep(1)
        
        """ 5. Verify "Data" pane has been updated with fields from EMPDATA.MAS. """
        metaobj.verify_data_pane_field('Dimensions', 'LAST_NAME', 2, "Step 05a")
        metaobj.verify_data_pane_field('Measures/Properties', 'CURR_SAL', 1, "Step 05b")
        
        """ 6. Click "Switch" (dropdown). """
        """ 7. Verify 2 options are displayed. """
        """ 8. Select "ibisamp/car" option. """
        ribbonobj.select_ribbon_item("Data", "Switch")
        utillobj.select_or_verify_bipop_menu("ibisamp/car", verify='true', expected_popup_list=['ibisamp/car', 'ibisamp/employee'], msg='Step 06a: Verify 2 menu options listed')
        time.sleep(10)
        
        """ 9. Verify "Data" pane has been updated with fields from CAR.MAS. """
        metaobj.verify_data_pane_field('Dimensions', 'CAR', 2, "Step 09a")
        metaobj.verify_data_pane_field('Measures/Properties', 'SALES', 4, "Step 09b")
        
        """ 10. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp """
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()