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

class C2227771_TestClass(BaseTestCase):

    def test_C2227771(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_OFF_001a.fex"
        report_dataset_name="AHTML_OFF_001a"
        
        ''' Testcase Variables'''
        
        Test_Case_ID = 'C2227771'
        
        step1 = '''    Step 1. Sign in to WebFOCUS as a Basic user, http://machine:port/{alias    
            Step 2. Expand folder P292_S10032_G157266
               Execute the following URL:
               http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTMLOFF&BIP_item=AHTML_OFF_001a.fex
               active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")    '''
        
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        utillobj.capture_screenshot('02.00', step1)
        
        step3 = '''  Step 3. Verify the report is generated.  '''
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")
        utillobj.capture_screenshot('03.00', step3, expected_image_verify=True)
                
        step4 = '''    '4. Using the Category field, add a Filter for Equals, selecting Food as the Filter value.    
             Verify that the original 107 line report now shows only 33 records, all with Category value of 'Food'.    '''
        
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
        utillobj.capture_screenshot('04.00', step4, expected_image_verify=True)
        
        step5 = '''    '5. Click dropdown next to Category column and select Export > XML (Excel) > Filtered only.    
                 Verify that the Filtered report has been saved to default Excel file named - book1. Also verify that all 33 Filter records have been saved and an additional Heading record added. Scroll down inside the Excel spreadsheet to see the last record, numbered row 34.    '''
        miscelanousobj.select_menu_items("ITableData0", 0, "Export", "XML (Excel)", "Filtered only")
        time.sleep(15)
        utillobj.save_file_from_browser('C2227771_actual_1')
        utillobj.verify_xml_xls('C2227771_actual_1.xls', 'C2227771_base_1.xls', 'Step 05.00. Verify file contents')
        utillobj.capture_screenshot('05.00', step5, expected_image_verify=True)
        utillobj.switch_to_main_window()
        
        step6 = '''Step  6:Dismiss the window and logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp'''
        utillobj.capture_screenshot('06.00', step6)
        
if __name__ == '__main__':
    unittest.main()