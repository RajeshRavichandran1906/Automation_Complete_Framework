'''
Created on Dec 14, 2017

@author: Magesh/ Updated by : Bhagavathi

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227786
TestCase Name = Report-Filter: Verify user can use Filter menu options under each column (Greater Than or Equal to, Less Than & Less Than or Equal To).
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from common.wftools import active_report

class C2227786_TestClass(BaseTestCase):

    def test_C2227786(self):
        
        active_reportobj=active_report.Active_Report(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        fex_name ="AHTML_OFF_001a.fex"
        report_dataset_name="AHTML_OFF_001a"
        Test_Case_ID = "C2227786"
        
        """
        Step 01: Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
        Step 02: Expand folder P292_S10032_G157266
        Execute the following URL:
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        """
        Step 03: Verify the report is generated.
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', 'Step 03.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")
        
        """
        Step 04: Select Unit Sales > Filter 
        Verify Filter menu shows all the filter options mentioned in the Test Description.
        """ 
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 4, 'Filter', option, 'Step 04: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        
        """
        Step 05: Select Unit Sales > Filter > Greater Than or Equal to Then click the dropdown for Unit Sales Filter values and select 27100.
        Click the Filter button.
        Verify Filter selection pop up is opened.
        Verify the Unit Sales value Filter selection menu appears.
        Verify report returns 55 of 107 records that have Unit Sales value greater than "27100".
        """
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter", "Greater than or equal to")
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 05.1: Verify Filter that the selection menu appears:',['Unit Sales', 'Greater than or equal to'])
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 05.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1, 'Greater than or equal to','large', value1='27100')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        """ 
        Verify report returns 55 of 107 records that have Unit Sales value greater than "27100". 
        """
        miscelanousobj.verify_page_summary('0','55of107records,Page1of1', 'Step 05.3: Verify the page summary')
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID+'_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds02.xlsx', 'Step 05.4: Verify that report returns 55 of 107 records, all Less Than 15905.')
        time.sleep(4)
        
        """ 
        Step 06: Close Filter selection pop up
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
        
        """ 
        Verify report is restored in original format.
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', 'Step 06.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", 'Step 06.2: Verify report is restored in original format.')
        time.sleep(4)
        
        """
        Step 07: Select Unit Sales > Filter > Less than. Then click the dropdown for Unit Sales Filter values and select 15905.
        Click the Filter button.
        Verify Filter selection pop up is opened.
        Verify the Unit Sales value Filter selection menu appears.
        """
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter", "Less than")
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 07.1: Verify Filter selection pop up is opened',['Unit Sales', 'Less than'])
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 07.2:Verify Filter selection pop up is opened")
        filterselectionobj.create_filter(1, 'Less than','large', value1='15905')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        """ 
        Verify that report returns 17 of 107 records, all Less Than 15905. 
        """
        miscelanousobj.verify_page_summary('0','17of107records,Page1of1', 'Step 07.3: Verify the page summary')
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID+'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds03.xlsx', 'Step 07.4: Verify that report returns 17 of 107 records, all Less Than 15905.')
        
        """ 
        Step 08: Close Filter selection pop up
        """
        miscelanousobj.close_popup_dialog('1')
        
        """ 
        Verify report is restored in original format.
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', 'Step 08.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 08.2: verify report data")
        
        """
        Step 09: Select Dollar Sales > Filter > Less than or Equal to. Then click the dropdown for Unit Sales Filter values and select 187901.
        Click the Filter button.
        Verify Filter selection pop up is opened.
        Verify the Dollar Sales value Filter selection menu appears.
        """
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter", "Less than or equal to")
        utillobj.synchronize_with_number_of_element("#wall1 #wtop1 .arWindowBarTitle", 1, 30)
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 09.1: Verify Filter selection pop up is opened',['Dollar Sales', 'Less than or equal to'])
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 09.2:Verify Filter selection pop up is opened")
        filterselectionobj.create_filter(1, 'Less than or equal to','large', value1='187901')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        """ 
        Verify report returns 10 of 107 records that have Dollar Sales values Less Than or Equal To 187901.
        """
        miscelanousobj.verify_page_summary('0','10of107records,Page1of1', 'Step 09.3: Verify the page summary')
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds04.xlsx', 'Step 09.4: Verify report returns 10 of 107 records that have Dollar Sales values Less Than or Equal To 187901.')
        
        """ 
        Step 10: Dismiss the window and logout. http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()