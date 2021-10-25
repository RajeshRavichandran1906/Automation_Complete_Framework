'''
Created on Jun 12, 2019

@author: Varun/Prasanth
Testcase Name : Auto Drill with proper Output format for chart
Testcase ID :http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/7279867

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart

class C7279867_TestClass(BaseTestCase):
    
    def test_C7279867(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        
        """
        STEP 1: Reopen the saved fex using API link:
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/IA-Chart.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(None, fex_name="IA-Chart")
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
            STEP 2 : Click "Format" tab.
        """
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        
        """
            STEP 2.01 Expected : Check "Auto Drill" button is active.
        """
        chart_obj.verify_ribbon_item_is_enabled("format_auto_drill", "2.01")
        
        """
            STEP 3 : Click the Output format button in the Status bar and Click "Active Report" option.
        """
        chart_obj.select_output_format_from_status_bar("Active Report")
        chart_obj.wait_for_visible_text("#sbpOutputFormatPanel", "Active Report")
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        
        """
            STEP 3.01 Expected : Check "Auto Drill" button is active.
        """
        chart_obj.verify_ribbon_item_is_enabled("format_auto_drill", "3.01")
        
        """
            STEP 4 : Click the Output format button in the Status bar and Click "HTML" option.
        """
        chart_obj.select_output_format_from_status_bar("HTML")
        chart_obj.wait_for_visible_text("#sbpOutputFormatPanel", "HTML")
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        
        """
            STEP 4.01 Expected : Check "Auto Drill" button is inactive.
        """
        chart_obj.verify_ribbon_item_is_disabled("format_auto_drill", "4.01")
        
        """
            STEP 5 : Click the Output format button in the Status bar and Click "PDF" option.
        """
        chart_obj.select_output_format_from_status_bar("PDF")
        chart_obj.wait_for_visible_text("#sbpOutputFormatPanel", "PDF")
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        
        """
            STEP 5.01 Expected : Check "Auto Drill" button is inactive.
        """
        chart_obj.verify_ribbon_item_is_disabled("format_auto_drill", "5.01")
        
        """
            STEP 6 : Click the Output format button in the Status bar and Click " Excel (xlsx)" option.
        """
        chart_obj.select_output_format_from_status_bar("Excel (xlsx)")
        chart_obj.wait_for_visible_text("#sbpOutputFormatPanel", "Excel (xlsx)")
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        
        """
            STEP 6.01 Expected : Check "Auto Drill" button is inactive.
        """
        chart_obj.verify_ribbon_item_is_disabled("format_auto_drill", "6.01")
        
        """
            STEP 7 : Click the Output format button in the Status bar and Click "Powerpoint (pptx)" option.
        """
        chart_obj.select_output_format_from_status_bar("PowerPoint (pptx)")
        chart_obj.wait_for_visible_text("#sbpOutputFormatPanel", "PowerPoint (pptx)")
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        
        """
            STEP 7.01 Expected : Check "Auto Drill" button is inactive.
        """
        chart_obj.verify_ribbon_item_is_disabled("format_auto_drill", "7.01")
        
        """
            STEP 8 : Click the Output format button in the Status bar and Click "HTML5" option.
        """
        chart_obj.select_output_format_from_status_bar("HTML5")
        chart_obj.wait_for_visible_text("#sbpOutputFormatPanel", "HTML5")
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        
        """
            STEP 8.01 Expected : Check "Auto Drill" button is active.
        """
        chart_obj.verify_ribbon_item_is_enabled("format_auto_drill", "8.01")
        
        """
            STEP 9 : Click "IA" menu and Select "Close" option.
            STEP 10 : Click "No" button.
        """
        chart_obj.close_ia_without_save()              
         
        """
            STEP 11 : Logout using API: 
                http://machinename:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
         
if __name__ == '__main__':
    unittest.main()