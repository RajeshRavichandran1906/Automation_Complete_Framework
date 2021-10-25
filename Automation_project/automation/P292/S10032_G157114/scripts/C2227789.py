'''
Created on Dec 18, 2017

@author: Magesh/ Updated by : Bhagavathi

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227789
TestCase Name = Report-Filter: Compound Filter Conditions: Single, then two field Filters, using AND & OR connections.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from common.wftools import active_report

class C2227789_TestClass(BaseTestCase):

    def test_C2227789(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_OFF_001a.fex"
        report_dataset_name="AHTML_OFF_001a"
        
        """
        Step 01: Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
        Step 02: Expand folder P292_S10032_G157266
        Execute the following URL:http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        """
        Step 03: Verify the report is generated.
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', 'Step 03.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.2: verify report data")
        
        """
        Step 04: Select State > Filter > Equals
        Click the dropdown for State values and select "IL".
        """ 
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 3, 'Filter', option, 'Step 04: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter", "Equals")
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 04.1: Verify Filter that the selection menu appears:',['State', 'Equals'])
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 04.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1, 'Equals', value1='IL')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
         
        """ 
        Expect to see the report containing 9 records, first Filtered for State = "IL" 
        """
        miscelanousobj.verify_page_summary('0','9of107records,Page1of1', 'Step 04.3: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2227789_Ds02.xlsx', 'Step 04.4: Verify that report containing 9 records, first Filtered for State = "IL"')
#         utillobj.create_data_set('ITableData0','I0r','C2227789_Ds02.xlsx')
        time.sleep(5)
         
         
        """
        Step 05: In the Filter Box, click Add Condition, then select Product.
        Expect to see a second Filter appear for Product.
        Verify that the Operator is the default value of "AND".
        """ 
        filterselectionobj.add_condition_field('Product')
        time.sleep(4)
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 05.1: Verify Filter that the selection menu appears:',['Product', 'Equals'],row_num=3)
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 05.2: Verify Filter that the selection menu appears:")
        
        """
        Step 06: Select 'Not Equal' for Product column and from the value list, select "Espresso".
        Click the Filter button.
        """ 
        filterselectionobj.create_filter(2, 'Not equal', value1='Espresso')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
         
        """ 
        Expect to see the report now with 8 records, as Espresso has been removed from the list of Products for State = "IL".
        """
        miscelanousobj.verify_page_summary('0','8of107records,Page1of1', 'Step 06.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2227789_Ds03.xlsx', 'Step 06.2: Verify that report now with 8 records, as Espresso has been removed from the list of Products for State = "IL".')
#         utillobj.create_data_set('ITableData0','I0r','C2227789_Ds03.xlsx')
        time.sleep(4)
         
        """
        Step 07: Close the current Filter screen.
        Select Category > Filter > Equals
        Click the dropdown for Category values and select "Coffee".
        """ 
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", "0", "Filter", "Equals")
        filterselectionobj.create_filter(1, 'Equals', value1='Coffee')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        """ 
        Expect to see 30 records, all with Category Equal to "Coffee".
        """
        miscelanousobj.verify_page_summary('0','30of107records,Page1of1', 'Step 07.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2227789_Ds04.xlsx', 'Step 07.2: Verify that report 30 records, all with Category Equal to "Coffee"')
#         utillobj.create_data_set('ITableData0','I0r','C2227789_Ds04.xlsx')
        time.sleep(4)
        
        
        """
        Step 08: Click the Add Condition in the Filter menu.
        Select Product and change the Operator to "OR". 
        Expect to see the following compound Filter menu.
        Verify that the Operator is set to "OR" for Product.
        """ 
        filterselectionobj.add_condition_field('Product')
        time.sleep(4)
        filterselectionobj.filter_button_click('Operator: AND')
        time.sleep(4)
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 08.1: Verify Filter that the selection menu appears:',['Product', 'Equals'],row_num=3)
        filterselectionobj.verify_filter_buttons(['Operator: OR', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 08.2: Verify Filter that the selection menu appears:")
        
        """
        Step 09: From the dropdown for Product, select "Scone". Click Filter.
        """ 
        filterselectionobj.create_filter(2, 'Equals', value1='Scone')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        """ 
        Expect to see 41 records, all with Category Equal to "Coffee" or with Product value of "Scone".
        """
        miscelanousobj.verify_page_summary('0','41of107records,Page1of1', 'Step 09.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2227789_Ds05.xlsx', 'Step 09.2: Verify that 41 records, all with Category Equal to "Coffee" or with Product value of "Scone"')
#         utillobj.create_data_set('ITableData0','I0r','C2227789_Ds05.xlsx')
        time.sleep(4)
        
        """ 
        Step 10: Dismiss the window and logout. http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()