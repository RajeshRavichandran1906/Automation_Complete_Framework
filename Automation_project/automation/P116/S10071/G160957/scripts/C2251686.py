'''
Created on Feb 5, 2018

@author: BM13368
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2251686
TestCase Name : AHTML: Combo Box incorrectly positioned to Filter Report - 161399
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2251686_TestClass(BaseTestCase):

    def test_C2251686(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID1="161399_Old.fex"
        Test_Case_ID2="161399_New.fex"
        Test_Case_ID="C2251686"
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01:Execute the attached Document repro - 161399_Old.
        This fex purposely uses a bad value for ARFILTER_VALUE to demonstrate the old, incorrect ComboBox behavior.
        """
        utillobj.active_run_fex_api_login(Test_Case_ID1, 'S10071_3', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_2", "YR_MO", 65)
         
        """
        Expect to see the following Document, with the Combo Box positioned incorrectly at the first value, which reads 'ALL'. This was the old behavior.
        """
        miscelanousobj.verify_page_summary('0','5595of5595records,Page1of280','Step 01.1 : Verify page summary')
        expected_value_list=['[All]', 'DEC, 2000', 'JAN, 2001', 'FEB, 2001', 'MAR, 2001', 'APR, 2001']
        utillobj.verify_dropdown_value("#combobox_dsCOMBOBOX1",value_list=expected_value_list, msg="Step 01:02:Verify the dropdown values", expected_default_selected_value='[All]', default_selection_msg="Step 01:03:Verify the default value has selected as All")
        textbox_label_elem=self.driver.find_element_by_css_selector("#LOBJtext11_TEXT")
        label_val=textbox_label_elem.text.strip()
        expected_label_value = "Select a Date:"
        utillobj.asequal(expected_label_value, label_val, "Step 01:04:verify the textbox value")
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID +'_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID +'_Ds01.xlsx', "Step 01:04: Verify entire Data set in Run Report on Page 1")
        utillobj.infoassist_api_logout()
        utillobj.synchronize_with_number_of_element("#SignonbtnLogin", 1, 65)
        
        """
        Step 02:Execute the attached Document repro - 161399_New.
        Expect to see the following Document, with the Combo Box positioned at JAN, 2002, now correctly using the start value specified in the keyword ARFILTER_VALUE, for the ComboBox definition.
        """
        utillobj.active_run_fex_api_login(Test_Case_ID2, 'S10071_3', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_2", "YR_MO", 65)
        """
        Verify that the dates on the report are for Jan, 2002 dates only, that is beginning with '2002/01'.
        """
        miscelanousobj.verify_page_summary('0','72of5595records,Page1of4','Step 02.1 : Verify page summary')
        textbox_label_elem=self.driver.find_element_by_css_selector("#LOBJtext11_TEXT")
        label_val=textbox_label_elem.text.strip()
        expected_label_value = "Select a Date:"
        utillobj.asequal(expected_label_value, label_val, "Step 02:04:verify the textbox value")
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID +'_Ds02.xlsx', "Step 02:05: Verify entire Data set in Run Report on Page 1")
        
        """
        Step 03:Click on the arrow in the Combo Box to verify that the displayed date is in the middle of the list and between the values DEC, 2001 and FEB, 2002.
        Expect to see the following expanded ComboBox list.
        """
        expected_value_list=['[All]', 'DEC, 2000', 'JAN, 2001', 'FEB, 2001', 'MAR, 2001', 'APR, 2001', 'MAY, 2001', 'JUN, 2001']
        utillobj.verify_dropdown_value("#combobox_dsCOMBOBOX1",value_list=expected_value_list, msg="Step 02:02:Verify the dropdown values", expected_default_selected_value='JAN, 2002', default_selection_msg="Step 02:03:Verify the default value has selected as All")
        

if __name__ == "__main__":
    unittest.main()