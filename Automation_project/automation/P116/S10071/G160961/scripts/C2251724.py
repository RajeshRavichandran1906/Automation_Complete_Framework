'''
Created on Feb 12, 2018

@author: BM13368
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2251724
TestCase Name : Add Multiple conditions using a Global filter in a Document for reports with (GRMERGE=ADVANCED).
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, ia_run, active_filter_selection
from common.lib import utillity

class C2251724_TestClass(BaseTestCase):

    def test_C2251724(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251724'
        active_fex_name ='Multi-page-Global-filter.fex'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        """
            Step 01:Execute the attached repro -
            Multi-page-Global-filter.fex
            Expect to see the Multi-page Document appear.
        """
        utillobj.active_run_fex_api_login(active_fex_name, "S10071_4", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 70)
        
        """ Page1 Verifcation """
#         ia_runobj.create_table_data_set('#ITableData0', Test_Case_ID+'_DS01.xlsx')
        ia_runobj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DS01.xlsx', 'Step 01.1 : Verify Activr Report displays')
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.2 : Verify report page summary')
        
        """ Page 2 Verification """
        
        select_css=self.driver.find_element_by_css_selector("#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']")
        utillobj.default_click(select_css)
        utillobj.synchronize_with_visble_text("#ITableData1 #TCOL_1_C_0 span", 'Category', 30)
        
#         ia_runobj.create_table_data_set('#ITableData1', Test_Case_ID+'_DS02.xlsx')
        ia_runobj.verify_table_data_set('#ITableData1', Test_Case_ID+'_DS02.xlsx', 'Step 01.1 : Verify Activr Report displays')
        miscelanousobj.verify_page_summary(1, '10of10records,Page1of1', 'Step 01.2 : Verify report page summary')
        
        """
            Step 02:Click the Global Filter icon to apply a filter to the Document.
            Move the filter panel below the report so it does not cover the Text Box or Report.
            Expect to see the following Global Filter menu appear.
        """
        filter_elem=self.driver.find_element_by_css_selector("table[id='iLayTB$'] .arDashboardBarGlobalButton")
        utillobj.default_click(filter_elem)
#         utillobj.click_on_screen(filter_elem, "middle", click_type=0)
        utillobj.synchronize_with_number_of_element("#wall1 .arFilterButton", 5, 30)
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 08.1: Verify Filter that the selection menu appears:")
        miscelanousobj.move_active_popup('1', '600', '200')
        time.sleep(5)
        
        """ 
            Step 03:Click the Add Condition button, select Category as the filter field.
            From the dropdown box select Categories - Food and Gifts.
            Expect to see the following panel for filtering on Category.
        """
        select_css=self.driver.find_element_by_css_selector("#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']")
        utillobj.default_click(select_css)
        filterselectionobj.add_global_condition_field('Category', parent_menu_css='0_globalop_x__0')
        filterselectionobj.create_filter(1,'Equals', value1='Food', value2='Gifts')
        time.sleep(3)
       
        """ 
            Step 04:Click the Filter button.
            Expect to see the following Filtered report, contain only Food & Gifts for Category.
        """
        filterselectionobj.filter_button_click('Filter')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 30)
        
        """ Verify Page1 report """
#         ia_runobj.create_table_data_set('#ITableData0', Test_Case_ID+'_DS03.xlsx')
        ia_runobj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DS03.xlsx', 'Step 04.1 : Verify Active Report page1 report data')
        miscelanousobj.verify_page_summary(0, '7of10records,Page1of1', 'Step 04:02 : Verify report page summary')
        
        """ Verify page2 Report """
        
        elem=self.driver.find_element_by_css_selector("#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']")
        utillobj.default_click(elem)
        utillobj.synchronize_with_visble_text("#ITableData1 #TCOL_1_C_0 span", 'Category', 30)
#         ia_runobj.create_table_data_set('#ITableData1', Test_Case_ID+'_DS04.xlsx')
        ia_runobj.verify_table_data_set('#ITableData1', Test_Case_ID+'_DS04.xlsx', 'Step 04.03 : Verify Active Report page2 report data')
        miscelanousobj.verify_page_summary(1, '7of10records,Page1of1', 'Step 04:04 : Verify report page summary')
        
        """
            Step 05:Set the operator to AND, then select Add Condition and select Product as the Filter field.
            Check the operator as Equal condition
            From the drop-down for Product, select Mug and Thermos for exclusion.
            Expect to see the following compound Filter panel.
        """
        
        select_css=self.driver.find_element_by_css_selector("#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']")
        utillobj.default_click(select_css)
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 30)
        
        filterselectionobj.add_global_condition_field('Product', parent_menu_css='0_globalop_0')
        filterselectionobj.create_filter(2,'Equals',value1='Mug', value2='Thermos')
        time.sleep(3)
        
        """ 
            Step 06:Click the Filter button to apply the multiple condition filter.
            Expect to see the following Filtered reports, contain only Food & Gifts for Category and with Products Mug & Thermos removed.
        """
        filterselectionobj.filter_button_click('Filter')
        
        """ Verify Page1 """
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 30)
#         ia_runobj.create_table_data_set('#ITableData0', Test_Case_ID+'_DS05.xlsx')
        ia_runobj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DS05.xlsx', 'Step 06:1 : Verify Active Report displays')
        miscelanousobj.verify_page_summary(0, '2of10records,Page1of1', 'Step 06:02 : Verify report page summary')
        
        """ Verify Page2 """
        
        select_css=self.driver.find_element_by_css_selector("#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']")
        utillobj.default_click(select_css)
        utillobj.synchronize_with_visble_text("#ITableData1 #TCOL_1_C_0 span", 'Category', 30)
        
#         ia_runobj.create_table_data_set('#ITableData1', Test_Case_ID+'_DS06.xlsx')
        ia_runobj.verify_table_data_set('#ITableData1', Test_Case_ID+'_DS06.xlsx', 'Step 06:1 : Verify Active Report displays')
        miscelanousobj.verify_page_summary(1, '2of10records,Page1of1', 'Step 06:02 : Verify report page summary')
        
        elem=self.driver.find_element_by_css_selector("#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']")
        utillobj.default_click(elem)
        
        """
            Step 07:Remove the Product filter by clicking the X next to the fieldname.
            Change the Operator to OR, then click the Add Condition and select Product again.
            Make sure to use Equals condition.
            Then select Mug and Thermos again.
            Expect to see the following filter panel.
        """
        filterselectionobj.delete_filter(2)
        time.sleep(3)
        filterselectionobj.add_global_condition_field('Product', parent_menu_css='0_globalop_0')
        filterselectionobj.create_filter(2,'Equals',value1='Mug', value2='Thermos')
        time.sleep(2)
        
        """ 
            Step 08:Click the Filter button to apply the OR condition.
        """
        filterselectionobj.filter_button_click('Operator: OR')
        filterselectionobj.filter_button_click('Filter')
        
        
        """ Verify Page1 """
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 30)
#         ia_runobj.create_table_data_set('#ITableData0', Test_Case_ID+'_DS07.xlsx')
        ia_runobj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DS07.xlsx', 'Step 07:01: Verify Active Report displays')
        miscelanousobj.verify_page_summary(0, '7of10records,Page1of1', 'Step 07:02 : Verify report page summary')
        
        """ Verify Page2 """
        
        elem=self.driver.find_element_by_css_selector("#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']")
        utillobj.default_click(elem)
        
        utillobj.synchronize_with_visble_text("#ITableData1 #TCOL_1_C_0 span", 'Category', 30)
#         ia_runobj.create_table_data_set('#ITableData1', Test_Case_ID+'_DS08.xlsx')
        ia_runobj.verify_table_data_set('#ITableData1', Test_Case_ID+'_DS08.xlsx', 'Step 07:03: Verify Active Report displays')
        miscelanousobj.verify_page_summary(1, '7of10records,Page1of1', 'Step 07:04: Verify report page summary')
        
        elem=self.driver.find_element_by_css_selector("#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']")
        utillobj.default_click(elem)
        
        """ Step 09:Click on Clear All button and click on the Global Filter x button to close the Filter panel."""
        filterselectionobj.filter_button_click('Clear All')
        
        """ Verify Page1 """
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 30)
        ia_runobj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DS01.xlsx', 'Step 09:01: Verify Active Report displays')
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 09:02 : Verify report page summary')
        
        """ Verify Page2 """
        
        elem=self.driver.find_element_by_css_selector("#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']")
        utillobj.default_click(elem)
        utillobj.synchronize_with_visble_text("#ITableData1 #TCOL_1_C_0 span", 'Category', 30)
        ia_runobj.verify_table_data_set('#ITableData1', Test_Case_ID+'_DS02.xlsx', 'Step 09:03: Verify Active Report displays')
        miscelanousobj.verify_page_summary(1, '10of10records,Page1of1', 'Step 09:04: Verify report page summary')

if __name__ == "__main__":
    unittest.main()