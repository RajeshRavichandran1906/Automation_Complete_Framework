"""-------------------------------------------------------------------------------------------
Created on June 12, 2019
@author: Aftab/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22585973
Test Case Title =  Auto Drill with proper Output format for chart 
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart,report
import time
from common.lib.global_variables import Global_variables

class C9336420_TestClass(BaseTestCase):

    def test_C9336420(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        report_obj = report.Report(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        chart_css = "#pfjTableChart_1"
        format_css = "#FormatTab"
        hometab_css = "#HomeTab"
        
        """
            STEP 1 : Reopen the saved fex using API link:
        """
        chart_obj.edit_fex_using_api_url("P292_S29835%2FG784981", fex_name="IA-Chart")
        chart_obj.wait_for_visible_text(chart_css, "Revenue")
        
        """
            STEP 2 : Click "Format" tab.
        """
        chart_obj.switch_ia_ribbon_tab('Format')
        chart_obj.wait_for_visible_text(format_css, "Features")

        """
            STEP 02.01 : Check "Auto Drill" button is active.
        """
        chart_obj.verify_ribbon_item_is_enabled("format_auto_drill", "02.01")

        """
            STEP 3 : Click the Output format button in the Status bar and Click "HTML Analytic Document" option.
        """
        chart_obj.switch_ia_ribbon_tab('Home')
        chart_obj.wait_for_visible_text(hometab_css, "Filter")
        
        chart_obj.select_output_format_from_ribbon("HTML Analytic Document")
        chart_obj.wait_for_visible_text(chart_css, "Revenue")
        if Global_variables.browser_name =='firefox':
            time.sleep(10)
        
        chart_obj.switch_ia_ribbon_tab('Format')
        chart_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 03.01 : Check "Auto Drill" button is active.
        """
        chart_obj.verify_ribbon_item_is_enabled("format_auto_drill", "03.01")

        """
            STEP 4 :Click the Output format button in the Status bar and Click "HTML" option.
        """
        chart_obj.switch_ia_ribbon_tab('Home')
        chart_obj.wait_for_visible_text(hometab_css, "Filter")
        
        chart_obj.select_output_format_from_ribbon("HTML")
        chart_obj.wait_for_visible_text("#HomeFormatType", "HTML")
        if Global_variables.browser_name =='firefox':
            time.sleep(10)
        
        chart_obj.switch_ia_ribbon_tab('Format')
        chart_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 04.01 : Check "Auto Drill" button is inactive.
        """
        chart_obj.verify_ribbon_item_is_disabled("format_auto_drill", "04.01")
        
        """
            STEP 5 : Click the Output format button in the Status bar and Click "PDF" option.
        """
        chart_obj.switch_ia_ribbon_tab('Home')
        chart_obj.wait_for_visible_text(hometab_css, "Filter")
        
        chart_obj.select_output_format_from_ribbon("PDF")
        chart_obj.wait_for_visible_text("#HomeFormatType", "PDF")
        if Global_variables.browser_name =='firefox':
            time.sleep(10)

        chart_obj.switch_ia_ribbon_tab('Format')
        chart_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 05.01 : Check "Auto Drill" button is inactive.
        """
        chart_obj.verify_ribbon_item_is_disabled("format_auto_drill", "05.01")

        """
            STEP 6 : Click the Output format button in the Status bar and Click " Excel (xlsx)" option.
        """
        chart_obj.switch_ia_ribbon_tab('Home')
        chart_obj.wait_for_visible_text(hometab_css, "Filter")
        
        chart_obj.select_output_format_from_ribbon("Excel (xlsx)->Excel (xlsx)")
        chart_obj.wait_for_visible_text("#HomeFormatType", "Excel")
        if Global_variables.browser_name =='firefox':
            time.sleep(10)
        
        chart_obj.switch_ia_ribbon_tab('Format')
        chart_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 06.01 : Check "Auto Drill" button is inactive.
        """
        chart_obj.verify_ribbon_item_is_disabled("format_auto_drill", "05.01")

        """
            STEP 7 : Click the Output format button in the Status bar and Click "Powerpoint (pptx)" option.
        """
        chart_obj.switch_ia_ribbon_tab('Home')
        chart_obj.wait_for_visible_text(hometab_css, "Filter")
        
        chart_obj.select_output_format_from_ribbon("PowerPoint (pptx)->PowerPoint (pptx)")
        chart_obj.wait_for_visible_text("#HomeFormatType", "PowerPoint")
        if Global_variables.browser_name =='firefox':
            time.sleep(10)
        
        chart_obj.switch_ia_ribbon_tab('Format')
        chart_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 07.01 : Check "Auto Drill" button is inactive.
        """
        chart_obj.verify_ribbon_item_is_disabled("format_auto_drill", "05.01")

        """
            STEP 8 : Click the Output format button in the Status bar and Click "HTML5" option.
        """
        chart_obj.switch_ia_ribbon_tab('Home')
        chart_obj.wait_for_visible_text(hometab_css, "Filter")
        
        chart_obj.select_output_format_from_ribbon("HTML5")
        chart_obj.wait_for_visible_text("#HomeFormatType", "HTML5")
        if Global_variables.browser_name =='firefox':
            time.sleep(10)
        
        chart_obj.switch_ia_ribbon_tab('Format')
        chart_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 08.01 : Check "Auto Drill" button is active.
        """
        chart_obj.verify_ribbon_item_is_enabled("format_auto_drill", "03.01")

        """
            STEP 9 : Click "IA" menu and Select "Close" option.
            STEP 10 :Click "No" button.
        """
        report_obj.close_ia_without_save()  
        
        """
            STEP 11 : Logout using API:
        """
        report_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()