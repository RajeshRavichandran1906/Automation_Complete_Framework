'''
Created on Jun 12, 2019

@author: Varun/Prasanth
Testcase Name : Auto Drill with proper Output format for report
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9336419

'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.pages import visualization_ribbon
from common.lib.global_variables import Global_variables

class C9336419_TestClass(BaseTestCase):
    
    def test_C9336419(self):
        
        """
            CLASS OBJECTS 
        """
        report_obj = report.Report(self.driver)
        visualization_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        STEP 1: Reopen the saved fex using API link:
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S29835/G784981/IA-Shell.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(fex_name="IA-Shell")
        report_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
            STEP 2 : Click "Format" tab.
        """
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text("#tableFeatures", "Features")
        
        """
            STEP 2.01 Expected : Check "Auto Drill" button is active.
        """
        report_obj.verify_ribbon_item_is_enabled("format_auto_drill", "2.01")
        
        """
            STEP 3 : Click the Output format button in the Status bar and Click "HTML Analytic Document" option.
        """
        visualization_obj.change_output_format_type("active_report", "status_bar")
        
        """
            STEP 3.01 Expected : Check "Auto Drill" button is active.
        """
        if Global_variables.browser_name =='firefox':
            time.sleep(10)
        report_obj.verify_ribbon_item_is_enabled("format_auto_drill", "3.01")
        
        """
            STEP 4 : Click the Output format button in the Status bar and Click "PDF" option.
        """
        visualization_obj.change_output_format_type("pdf", "status_bar")
        
        """
            STEP 4.01 Expected : Check "Auto Drill" button is inactive.
        """
        if Global_variables.browser_name =='firefox':
            time.sleep(10)
        report_obj.verify_ribbon_item_is_disabled("format_auto_drill", "4.01")
        
        """
            STEP 5 : Click the Output format button in the Status bar and Click " Excel (xlsx)" option.
        """
        visualization_obj.change_output_format_type("excel", "status_bar")
        
        """
            STEP 5.01 Expected : Check "Auto Drill" button is inactive.
        """
        if Global_variables.browser_name =='firefox':
            time.sleep(10)
        report_obj.verify_ribbon_item_is_disabled("format_auto_drill", "5.01")
        
        """
            STEP 6 : Click the Output format button in the Status bar and Click "Powerpoint (pptx)" option.
        """
        visualization_obj.change_output_format_type("powerpoint", "status_bar")
        
        """
            STEP 6.01 Expected : Check "Auto Drill" button is inactive.
        """
        if Global_variables.browser_name =='firefox':
            time.sleep(10)
        report_obj.verify_ribbon_item_is_disabled("format_auto_drill", "6.01")
        
        """
            STEP 7 : Click the Output format button in the Status bar and Click "HTML" option.
        """
        visualization_obj.change_output_format_type("html", "status_bar")
        
        """
            STEP 7.01 Expected : Check "Auto Drill" button is active.
        """
        if Global_variables.browser_name =='firefox':
            time.sleep(10)
        report_obj.verify_ribbon_item_is_enabled("format_auto_drill", "7.01")
        
        """
            STEP 8 : Click "IA" menu and Select "Close" option.
            STEP 9 : Click "No" button.
        """
        report_obj.close_ia_without_save()              
         
        """
            STEP 10 : Logout using API: 
                http://machinename:port/alias/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
         
if __name__ == '__main__':
    unittest.main()