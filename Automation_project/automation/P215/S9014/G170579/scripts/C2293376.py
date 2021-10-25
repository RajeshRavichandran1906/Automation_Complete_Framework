'''
Created on Nov 2, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2293376
Testcase Name : Verify to Run 'Store Sales Report'

'''
import unittest
from common.wftools import report
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity

class C2293376_TestClass(BaseTestCase):

    def test_C2293376(self):
        
        driver = self.driver
        
        TEST_CASE_ID="C2293376"
        
        report_obj=report.Report(driver)
        utillobj=utillity.UtillityMethods(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        LONG_WAIT=180
        
        USERNAME= 'mrdevuser'
        PASSWORD= 'mrdevpass'
        FEX_NAME='Store_Sales_Report'
        FOLDER_NAME='Retail_Samples/InfoApps/Maps'
         
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        
        RUN_BUTTON_CSS=".autop-pane div[class^='autop-navbar'] a[title^='Run']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
            Step 1: Sign to WebFocus using "rsdev" user
            http://machine:port/ibi_apps
            Run the report using the below API link
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/InfoApps/Maps&BIP_item=store_sales_report.fex
        """
        report_obj.run_fex_using_api_url(FOLDER_NAME, fex_name=FEX_NAME, mrid=USERNAME, mrpass=PASSWORD, run_table_css=RUN_BUTTON_CSS)
        
        """
            Verify the Auto Prompt window is displayed
        """
        css="#promptPanel .autop-title"
        utillobj.verify_object_visible(css, True, "Step 1: Verify Autoprompt is displayed.")
        
        """
            Step 3: Click Run in autoprompt window
        """
        
        report_obj.run_auto_prompt_report()
        iframe_css="[name='wfOutput']"
        report_obj.wait_for_number_of_element(iframe_css, 1, LONG_WAIT)
        report_obj.switch_to_frame(frame_css=iframe_css)
        
        """
            Verify the following output
        """
        TABLE_CSS="table"
        report_obj.wait_for_visible_text('table', 'Arlington', time_out=report_obj.home_page_long_timesleep)
        #report_obj.create_table_data_set(TABLE_CSS, TEST_CASE_ID+"_Ds01.xlsx")
        report_obj.verify_table_data_set(TABLE_CSS,TEST_CASE_ID+"_Ds01.xlsx", "Step 3: Verify report data.")
        
        """
            Step 4: Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """



if __name__ == "__main__":
    unittest.main()