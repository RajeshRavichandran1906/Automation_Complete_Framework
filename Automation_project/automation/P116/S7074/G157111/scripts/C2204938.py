'''
Created on Jul 11, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204938
TestCase Name = HTML:AFLEX Compound report with 1 report doesnt work(Project 99382)

'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity
from selenium.webdriver.support.ui import Select

class C2204938_TestClass(BaseTestCase):

    def test_C2204938(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2204938'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01 : Execute the attached repro - T1121449.fex
        """
        utillobj.active_run_fex_api_login("T1121449.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#ITableData0 .arGridColumnHeading [id^='TCOL']"
        result_obj.wait_for_property(parent_css,5)
        
        """
        Expect to see the report contain all three Categories of data and the drop down box show 'Coffee'.
        """
        miscelaneousobj.verify_page_summary(0,'39of39records,Page1of1','Step 01.1 : Verify page summary')
        miscelaneousobj.verify_column_heading('ITableData0',['Category', 'Product ID', 'Region', 'Product', 'Unit Sales'],'Step 01.2 : Verify table column headings')
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+'_Data_Set_01.xlsx','Step 01.3 : Verify Expect to see the report contain all three Categories of data') 
        drop_down=Select(self.driver.find_element_by_css_selector("form[id='comboboxCOMBOBOX_1'] select[id='combobox_dsCOMBOBOX_1']"))
        drop_down_values=[option.text.strip() for option in drop_down.options]
        dropdown_default_value=drop_down.first_selected_option.text.strip()   
        utillobj.asequal('Coffee',dropdown_default_value,"Step 01.4 : Verify the drop down box show 'Coffee'")
        utillobj.asequal(drop_down_values,['Coffee','Food','Gifts'],'Step 01.5 : Verify drop down values')
        utillobj.infoassist_api_logout()
        
        """
        Step 02 : Edit the Fex and uncomment the first ARFILTER_ACTIVE statement with value 'ONLOAD'.Execute the Fex.
        """
        utillobj.active_run_fex_api_login("T1121449_ONLOAD.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#ITableData0 .arGridColumnHeading [id^='TCOL']"
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0", 'Category', 30)
        
        """
        Expect to see the report contain only the data for Category Coffee and the drop down box showing 'Coffee'.
        """
        miscelaneousobj.verify_page_summary(0,'11of39records,Page1of1','Step 02.1 : Verify page summary')
        miscelaneousobj.verify_column_heading('ITableData0',['Category', 'Product ID', 'Region', 'Product', 'Unit Sales'],'Step 02.2 : Verify table column headings')
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+'_Data_Set_02.xlsx','Step 02.3 : Verify Expect to see the report contain only the data for Category Coffee') 
        drop_down=Select(self.driver.find_element_by_css_selector("form[id='comboboxCOMBOBOX_1'] select[id='combobox_dsCOMBOBOX_1']"))
        drop_down_values=[option.text.strip() for option in drop_down.options]
        dropdown_default_value=drop_down.first_selected_option.text.strip()   
        utillobj.asequal('Coffee',dropdown_default_value,"Step 02.4 : Verify the drop down box show 'Coffee'")
        utillobj.asequal(drop_down_values,['Coffee','Food','Gifts'],'Step 02.5 : Verify drop down values')
        utillobj.infoassist_api_logout()
        
        """
        Step 03 : Edit the Fex again and comment the first ARFILTER_ACTIVE command with value 'ONLOAD' and uncomment the second ARFILTER_ACTIVE command with value 'Gifts'.Execute the Fex.
        """
        utillobj.active_run_fex_api_login("T1121449_GIFTS.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#ITableData0 .arGridColumnHeading [id^='TCOL']"
        result_obj.wait_for_property(parent_css,5)
        
        """
        Expect to see the report contain
        """
        miscelaneousobj.verify_page_summary(0,'16of39records,Page1of1','Step 03.1 : Verify page summary')
        miscelaneousobj.verify_column_heading('ITableData0',['Category', 'Product ID', 'Region', 'Product', 'Unit Sales'],'Step 03.2 : Verify table column headings')
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+'_Data_Set_03.xlsx','Step 03.3 : Verify Expect to see the report contain') 
        drop_down=Select(self.driver.find_element_by_css_selector("form[id='comboboxCOMBOBOX_1'] select[id='combobox_dsCOMBOBOX_1']"))
        drop_down_values=[option.text.strip() for option in drop_down.options]
        dropdown_default_value=drop_down.first_selected_option.text.strip()   
        utillobj.asequal('Gifts',dropdown_default_value,"Step 03.4 : Verify the drop down box show 'Coffee'")
        utillobj.asequal(drop_down_values,['Coffee','Food','Gifts'],'Step 03.5 : Verify drop down values')
        
if __name__=='__main__' :
    unittest.main()