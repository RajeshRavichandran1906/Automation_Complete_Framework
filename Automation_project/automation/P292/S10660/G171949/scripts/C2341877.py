'''
Created on Sep 3, 2019

@author: Niranjan
Test rail link : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2341877
Testcase title : Content Menu:Double click on items to run.
'''
import unittest
from common.wftools.wf_mainpage import Wf_Mainpage, Run
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login
from common.wftools.report import Report
from common.lib.core_utility import CoreUtillityMethods

class C2341877_TestClass(BaseTestCase):
   
    def test_C2341877(self):
       
        """ CLASS  OBJECTS """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        report_obj = Report(self.driver)
        homepagerun = Run(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
       
        step1 = """
            STEP 01 : Launch WF Home Page as Administrator.
            New home page is displayed as default.
        """
        loginpage.invoke_home_page('mradmid', 'mradmpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.main-panel .toolbar', 'Domains', homepage.home_page_long_timesleep)
        utils.capture_screenshot('01.01', step1)
        
        step2 = """
            STEP 02 : Under Domain tree >> Navigate to Retail_Samples domain >> 'Reports' folder.
        """
        homepage.expand_repository_folder('Domains->Retail Samples->Reports')
        utils.synchronize_with_visble_text('.sd-content-title-label-files', 'Items', homepage.home_page_short_timesleep)
        utils.capture_screenshot('02.01', step2)
        
        step3 = """
            STEP 03 : Double click on report "Margin by Product Category"
            Verify the report run in the same window.
        """
        homepage.double_click_on_content_area_items('Margin by Product Category')
        homepagerun.switch_to_frame()
        core_utils.switch_to_frame('iframe')
        utils.synchronize_with_visble_text('table[summary="Summary"]', 'Product', homepage.home_page_long_timesleep)
#         report_obj.create_html_report_dataset('C2341877_Ds01.xlsx')
        report_obj.verify_html_report_dataset("C2341877_Ds01.xlsx", "Step 03.00: Verify report")
        homepagerun.switch_to_default_content()
        utils.capture_screenshot('03.01', step3, expected_image_verify=True)
        homepagerun.close()
        
        """
            STEP 04 : In the banner link, click on the top right username > Sign Out.
        """
        utils.synchronize_with_visble_text('.sd-content-title-label-files', 'Items', homepage.home_page_short_timesleep)
        homepage.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()