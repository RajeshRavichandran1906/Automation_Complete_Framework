'''
Created on Jan 19, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251740
Test_Case Name : AHTML:CMPD:FilterCntr do not display Integer data values (115793)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import ia_run, active_miscelaneous
from common.lib import utillity

class C2251740_TestClass(BaseTestCase):

    def test_C2251740(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2251740'
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
            Step 01 : Execute the attached repro - 115793.fex
        """
        utillobj.active_run_fex_api_login('115793.fex', 'S10071_5', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0>tt", 'ProductType', 60)
        
        """
            Step 01.1 : Expect to see the following AHTML Document with two ComboBoxes and one drop down list.
        """
        #iarun.create_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_01.xlsx')
        iarun.verify_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_01.xlsx', 'Step 01.1 : Verify Report data')
        active.verify_page_summary(0, '100of100records,Page1of2', 'Step 01.2 : Verify page summary')
        utillobj.verify_dropdown_value("#combobox_dCOMBOBOX1 select", ['[All]', 'Audio', 'Camcorders', 'Cameras', 'Office', 'Video'], 'Step 01.3 : Verify default value of first dropdown', '[All]' ,'Step 01.4 : Verify all value of first dropdown')
        expected_dropdown2_list=['[All]', '101', '138', '185', '215', '251', '280', '289', '302', '305', '320', '400', '459', '490', '557', '573', '590', '707', '872', '899', '961', '986', '990', '1020', '1068', '1073', '1200', '1244', '1414', '1499', '1527', '1758', '1972', '2300', '2444', '3068', '3494', '3527', '4000', '4050', '5507', '5961', '6758', '7000', '7050', '9480', '9707']
        utillobj.verify_dropdown_value("#combobox_dCOMBOBOX2 select", expected_dropdown2_list, 'Step 01.5 : Verify default value of second dropdown', '[All]', 'Step 01.6 : Verify all value of second dropdown')
        expected_listbox_values=['[All]', '1', '13', '39', '52', '55', '58', '59', '62', '79', '83', '92', '99', '133', '172', '212', '258', '279', '305', '319', '358', '399', '425']
        iarun.verify_active_dashboard_prompts('listbox', '#list_dLISTBOX1', expected_listbox_values, 'Step 01.7 : Verify all values of listbox')
        
        """
            Step 02 : From the upper left ComboBox, select Office.
        """
        utillobj.select_dropdown('#combobox_dCOMBOBOX1 select', 'visible_text', 'Office')
        time.sleep(2)
        
        """
            Step 02.1 : Expect to see only rows for Product Type = Office.
        """
        #iarun.create_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_02.xlsx')
        iarun.verify_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_02.xlsx', 'Step 02.1 : Verify Expect to see only rows for Product Type = Office.')
        active.verify_page_summary(0, '8of100records,Page1of1', 'Step 02.2 : Verify page summary')
        
        """
            Step 03 : From the lower left ComboBox, select value 400.
        """
        utillobj.select_dropdown('#combobox_dCOMBOBOX2 select', 'visible_text', '400')
        time.sleep(2)
        
        """
            Step 03.1 : Expect to see only rows for  Quantity In Stock I11 = 400.
        """
        #iarun.create_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_03.xlsx')
        iarun.verify_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_03.xlsx', 'Step 03.1 : Verify Expect to see only rows for  Quantity In Stock I11 = 400.')
        active.verify_page_summary(0, '2of100records,Page1of1', 'Step 03.2 : Verify page summary')
        
        """
            Step 04 : From the List Box, select value 79.
        """
        iarun.select_active_dashboard_prompts('listbox', '#list_dLISTBOX1', selection_list=['79'])
        time.sleep(2)
        
        """
            Step 04.1 : Expect to see only rows for Quantity I8C = 79.
        """
        #iarun.create_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_04.xlsx')
        iarun.verify_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_04.xlsx', 'Step 04.1 :  Expect to see only rows for Quantity I8C = 79.')
        active.verify_page_summary(0, '5of100records,Page1of1', 'Step 04.2 : Verify page summary')
        
        """
            Step 05 : From the List Box, select value [All].
        """
        utillobj.select_dropdown('#combobox_dCOMBOBOX1 select', 'visible_text', '[All]')
        time.sleep(2)
        
        """
            Step 05.1 : Expect to see the original Document with all records.
        """
        iarun.verify_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_01.xlsx', 'Step 05.1 : Verify Expect to see the original Document with all records')
        active.verify_page_summary(0, '100of100records,Page1of2', 'Step 05.2 : Verify page summary')
        
if __name__ == '__main__':
    unittest.main()