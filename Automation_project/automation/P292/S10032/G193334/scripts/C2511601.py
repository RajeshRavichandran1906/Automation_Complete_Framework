'''
Created on December 29, 2017

@author: Prabhakaran/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227769
TestCase Name = Report Export - HTML: Verify user can export report in HTML format
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, ia_run
from common.lib import utillity
from common.wftools import active_report

class C2511601_TestClass(BaseTestCase):

    def test_C2511601(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2511601'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 : Expand folder P292_S10032_G157266 Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        """
            Step 03 : Verify the report is generated
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.2: verify report data")
        
        """
            Step 04 : Click dropdown next to Category column and select Export > HTML > All Records
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export' ,'HTML', 'All records')
        time.sleep(3)
        utillobj.switch_to_window(1)
        utillobj.synchronize_with_visble_text("html>body>table>tbody>tr:nth-child(1)", "PAGE 1", 35)
        
        """
            Step 04.1 : Verify data for the reports are displayed in new browser and user can save as export.htm
        """
        actual_page1_title=self.driver.find_element_by_css_selector("html>body>table>tbody>tr>td>table>tbody>tr>td:nth-of-type(1)").text.strip()
        utillobj.asequal(actual_page1_title, 'PAGE 1', 'Step 04.1 : Verify Page 1 title')
#         iarun.create_table_data_set("html>body>table", Test_Case_ID+'_DataSet_01.xlsx')
        iarun.verify_table_data_set("html>body>table", Test_Case_ID+'_DataSet_01.xlsx', 'Step 04.2 : Verify page 1 data for the reports are displayed in new browser and user can save as export.htm')
        self.driver.close()
        utillobj.switch_to_window(0)
        
        """
            Step 5 : Dismiss the window and logout http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
    
if __name__=='__main__' :
    unittest.main()