'''
Created on Jan 04, 2018

@author: Praveen Ramkumar/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227749
TestCase Name = Report-Other: Verify the Filtering functionality of a coordinated report in AHTML.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from common.wftools import active_report

class C2511619_TestClass(BaseTestCase):

    def test_C2511619(self):
        
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name="AHTML_Coordinated.fex"
        Test_Case_ID = "C2511619"

        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G157266 
            Execute the following URL:http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_Coordinated.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 #TCOL_0_C_1 span", synchronize_visible_element_text="COUNTRY")
        
        """
            Step 03 : Verify the report is generated.
            Verify the default output of England is show on the coordinated report.  
        """
        
        miscelanousobj.verify_page_summary('0','4of13records,Page1of1', 'Step 03.1: Verify the page summary')
#         utillobj.create_data_set('ITableData0','I0r','C2227749_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx', 'Step 03.2:Verify the report is generated.')
        time.sleep(4)
        
        """
            Step 04:Click dropdown for country and change it from ENGLAND to JAPAN   
            Verify values for JAPAN are displayed on change.        
        """        
        dropdown_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0[class*='arDashboardBar']")
        utillobj.click_on_screen(dropdown_css, 'middle')
        utillobj.click_on_screen(dropdown_css, 'middle', click_type=0)
        time.sleep(2)
        production_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0[class*='arDashboardBar'] option[value='JAPAN']")
        production_css.click()
        time.sleep(2)
        miscelanousobj.verify_page_summary('0','2of13records,Page1of1', 'Step 04.1: Verify the page summary')
#         utillobj.create_data_set('ITableData0','I0r','C2227749_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds02.xlsx', 'Step 04.2:Verify the report is generated.')
        time.sleep(4)
        
        """
            Step 05:Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
if __name__ == '__main__':
    unittest.main()