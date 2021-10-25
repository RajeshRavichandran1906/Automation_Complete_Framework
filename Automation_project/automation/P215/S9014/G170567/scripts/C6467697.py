'''
Created on Jul 13, 2018

@author: BM13368
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/6467697&group_by=cases:section_id&group_id=170567&group_order=asc
TestCase_Name : Precondition to check the App path mapping for Retail Samples
'''
import unittest
from common.wftools import report
from common.lib.basetestcase import BaseTestCase


class C6467697_TestClass(BaseTestCase):

    def test_C6467697(self):
        
        report_obj=report.Report(self.driver)
        fex_name="smoke_retail_samples_test"
        folder_name="Retail_Samples"
                
        """
            Step 01 : Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 02 : Run the Report using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples&BIP_item=smoke_retail_samples_test.fex
        """
        report_obj.run_fex_using_api_url(folder_name, fex_name=fex_name, mrid='mrid', mrpass='mrpass', run_table_css="html body")
        
        """
            Step 03 : Verify the App path is pointed to /bipgqashare/qaauto_lnx_apps/smoke_retailsamples_alphaformat/wf_retail_lite.mas
        """
        report_obj.wait_for_number_of_element('body', 1, 120)
        report_obj.verify_message_in_html_body(msg="Step :03:01:Verify body of the message shows smoke_retailsamples")
        
        """
            Step 04 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()