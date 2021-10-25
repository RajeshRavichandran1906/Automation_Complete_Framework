'''
Created on Oct 6, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203747
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_metadata,ia_ribbon
from common.lib import utillity

class C2203747_TestClass(BaseTestCase):

    def test_C2203747(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        Test_Case_ID = 'C2203747'
        
        """
        Step 01: Create a report with IA, use car file
        """
        utillobj.infoassist_api_login('report', 'ibisamp/car', 'P116/S7072', 'mrid', 'mrpass')
        element_css="div[id='HomeTab'] div[id='HomeFormatType']"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=30)
        
        """
        Step 02:Add fields car, model, dc, sales
        """
        metadataobj.datatree_field_click('CAR', 2, 1)
        element_css="#TableChart_1 div[class='bi-component meta_api_unselected']"
        utillobj.synchronize_with_number_of_element(element_css, 2, 30)
        
        metadataobj.datatree_field_click('MODEL', 2, 1)
        element_css="#resultArea div[class^='bi-component meta_api_unse']"
        utillobj.synchronize_with_number_of_element(element_css, expected_number=4, expire_time=30)
        
        metadataobj.datatree_field_click('DEALER_COST', 2, 1)
        element_css="#resultArea div[class^='bi-component meta_api_unse']"
        utillobj.synchronize_with_number_of_element(element_css, expected_number=6, expire_time=30)
        
        metadataobj.datatree_field_click('SALES', 2, 1)
        element_css="#resultArea div[class^='bi-component meta_api_unse']"
        utillobj.synchronize_with_number_of_element(element_css, expected_number=8, expire_time=30)
        
        """
        Step 03: Select Format tab, select Active Report format
        """
        element_css="div[id='HomeTab'] div[id='HomeFormatType']"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=30)
        ribbonobj.change_output_format_type('active_report', location='Home')
        
        """
        Step 04: Select 'Active Report Options' from Format->Features menu.
        """
        ribbonobj.select_ribbon_item('Format', 'Active_Report_Options')
        
        """
        STep 05: UnderMenu Options tab in the Active Report dialog, select user type Basic.
        """ 
        ia_ribbonobj.active_report_options('Menu Options',menu_options=True, menu_value='Basic')
         
        """
        Step 06: Now select Advanced tab, enter Password:New1 and date:250220, say ok to dialog and execute the report.
        """
        ia_ribbonobj.active_report_options('Advanced', advanced_expiration=True, advanced_expirationDateTxtFld='250220', advanced_password='New1', btnOk=True)
         
        """
        Step 07: Enter Password and Select Ok from the Dialog box and verify report is displayed.
        """
        ribbonobj.select_tool_menu_item('menu_run')
         
        utillobj.switch_to_frame(pause=5) 
         
        self.driver.find_element_by_css_selector('[name="promptform"] input').send_keys('New1')
        self.driver.find_element_by_css_selector('[class="arPromptButton"]').click()

        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx','Step 07: Verify report')
          
        utillobj.switch_to_default_content(pause=2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == "__main__":
    unittest.main()        