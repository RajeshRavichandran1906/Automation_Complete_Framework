'''
Created on Jun 12, 2019

@author: Sudhan/Pearlson Joyal

Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/7279826
TestCase Name : Auto Drill is not accessible with a MFD that does not have a dimensional hierarchy
'''
import unittest
from common.wftools import report
from common.lib.basetestcase import BaseTestCase

class C7279826_TestClass(BaseTestCase):

    def test_C7279826(self):
        """
            CLASS OBJECTS 
        """
        report_obj = report.Report(self.driver)
        
        """
            TESTCASE ID Variable 
        """
        tablechart_css = "#TableChart_1"
        format_css = "#FormatTab"
        hometab_css = "#HomeTab"

        """       
            STEP 1 : Launch the API to create new Report with CAR.
            http://machine:port/{alias}/ia?is508=false&tool=report&master=ibisamp/car&item=IBFS:/WFC/Repository/P292_S10117/G580387
        """
        report_obj.invoke_ia_tool_using_new_api_login(master='ibisamp/car')
        report_obj.wait_for_visible_text(tablechart_css, "Drag and drop", 90)    
         
        """
            STEP 2 : Click on Format tab.
        """
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 2.01 : Verify Autodrill button is inactive as below.
        """
        report_obj.verify_ribbon_item_is_disabled("format_auto_drill", "2.01")
        
        """
            STEP 3 : Click "Home" tab.
            STEP 4 : Click on Format drop down (HTML) and select Active Report format
        """
        report_obj.switch_ia_ribbon_tab('Home')
        report_obj.wait_for_visible_text(hometab_css, "Filter")
        report_obj.change_output_format_type("active_report")
        
        """
            STEP 5 : Click "Format" tab.
        """        
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 5.01 :Verify Autodrill button is inactive as below.
        """
        report_obj.verify_ribbon_item_is_disabled("format_auto_drill", "5.01")      
         
        """
            STEP 6 : Logout using API: 
                http://machinename:port/alias/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
         
if __name__ == '__main__':
    unittest.main()