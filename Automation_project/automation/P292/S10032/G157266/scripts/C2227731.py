'''
Created on Dec 13, 2017

@author: Pavithra/updated by :Bhagavathi 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157266
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227731
TestCase Name : Report:Verify that user is able to run a simple AHTML report
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous
from common.lib import utillity
from common.wftools import active_report

class C2227731_TestClass(BaseTestCase):

    def test_C2227731(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227731'
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelanousobj =active_miscelaneous.Active_Miscelaneous(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        obrowser=utillobj.parseinitfile('browser')
        
        fex_name ="AHTML_OFF_001a.fex"
        report_dataset_name="AHTML_OFF_001a"
        
        """        
            Step 01:Sign in to WebFOCUS as a Basic user
                    http://machine:port/{alias} Sign on screen will display
            Step 02:Expand folder P292_S10032_G157266
                    Execute the following URL:
                    http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001a.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        """
            Step 03:Verify the AHTML formatted report is generated.
        """
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.1: Verify column heading')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 03.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")

        """
            Step 04:Click dropdown next to Category column heading.
                Verify all the report menu options are present on a report.
        """
        if obrowser == "IE":
            expected_menu_list=['Sort Ascending', 'Sort Descending', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Send as E-mail', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        else :    
            expected_menu_list=['Sort Ascending', 'Sort Descending', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Save Changes','Export', 'Print', 'Window', 'Restore Original']
        miscelanousobj.verify_menu_items("ITableData0",0, None,expected_menu_list, 'Step 04:  Verify all the report menu options are present on a report')

        """
            Step 05:From the dropdown list of controls for Category, select Calculate, then Count to test the basic functionality of Active options.
                    Expect to see a Count of all records.
        """
        miscelanousobj.select_menu_items("ITableData0", 0, "Calculate","Count")       
        parent_css="#ITableData0  span[class='arGridAgg']"
        result_obj.wait_for_property(parent_css, 1)
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 05.1: Verify column heading')
        miscelanousobj.verify_calculated_value(2, 1, "Total Cnt 107", True, "Step 05.2: Expect to see Total Cnt 107")
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 05.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01.xlsx", "Step 05.3: verify Count of all records ", desired_no_of_rows=20)
        
        """
            Step 06:Dismiss the window and logout.
                http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """   
        time.sleep(5)   
                
if __name__ == '__main__':
    unittest.main()
        