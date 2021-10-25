'''
Created on Dec 28, 2017

@author: Robert/Updated by : Bhagavathi

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227771
TestCase Name = Report Export - EXCEL Verify user can export report in excel format
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from common.wftools import active_report

class C2511603_TestClass(BaseTestCase):

    def test_C2511603(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
        
        ''' Testcase Variables'''
        
        Test_Case_ID = 'C2511603'
        
        '''    Step 1. Sign in to WebFOCUS as a Basic user, http://machine:port/{alias    '''
        '''    Step 2. Expand folder P292_S10032_G157266, Execute the following URL:    '''
        
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        '''  Step 3. Verify the report is generated.  '''
        
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")
                
        '''    '4. Using the Category field, add a Filter for Equals, selecting Food as the Filter value.    '''
        '''    '4.1. Verify that the original 107 line report now shows only 33 records, all with Category value of 'Food'.    '''
        
        miscelanousobj.select_menu_items("ITableData0", 0, "Filter", "Equals")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 4.1: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Equals',value1='Food')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        miscelanousobj.verify_page_summary('0','33of107records,Page1of1', 'Step 04.2: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx', 'Step 04.3: Verify that report returns 33 of 107 records')
        time.sleep(4)
        miscelanousobj.move_active_popup('1', 550, 40, custom_css="#wall1 .arWindowBar")
        
        '''    '5. Click dropdown next to Category column and select Export > Excel > Filtered only..    '''
        '''    '5.1. Verify that the Filtered report has been saved to default Excel file named - book1. Also verify that all 33 Filter records have been saved and an additional Heading record added. Scroll down inside the Excel spreadsheet to see the last record, numbered row 34.    '''
        miscelanousobj.select_menu_items("ITableData0", 0, "Export", "Excel", "Filtered only")
        time.sleep(15)
        utillobj.save_file_from_browser('C2511603_actual_1')
        utillobj.verify_xml_xls('C2511603_actual_1.xlsx', 'C2511603_base_1.xlsx', 'Step 5.1 Verify file contents')
        
if __name__ == '__main__':
    unittest.main()