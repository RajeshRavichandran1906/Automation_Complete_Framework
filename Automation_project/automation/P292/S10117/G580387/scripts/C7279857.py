"""-------------------------------------------------------------------------------------------
Created on June 12, 2019
@author: Aftab/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22268769
Test Case Title =  Auto Drill with proper Output format for report
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report

class C7279857_TestClass(BaseTestCase):

    def test_C7279857(self):
        
        """
            CLASS OBJECTS 
        """
        report_obj = report.Report(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        qwery_css = "#queryBoxColumn"
        format_css = "#FormatTab"
        hometab_css = "#HomeTab"
        
        """
            STEP 1 : Reopen the saved fex using API link:
        """
        report_obj.edit_fex_using_api_url("IA-Shell")
        report_obj.wait_for_visible_text(qwery_css, "Revenue", 90)
        
        """
            STEP 2 : Click "Format" tab.
        """
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 02.01 : Check "Auto Drill" button is active.
        """
        report_obj.verify_ribbon_item_is_enabled("format_auto_drill", "02.01")


        """
            STEP 3 : Click the Output format button in the Status bar and Click "Active Report" option
        """
        report_obj.switch_ia_ribbon_tab('Home')
        report_obj.wait_for_visible_text(hometab_css, "Filter")
        
        report_obj.select_output_format_from_ribbon("Active Report")
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 03.01 : Check "Auto Drill" button is active.
        """
        report_obj.verify_ribbon_item_is_enabled("format_auto_drill", "03.01")

        """
            STEP 4 : Click the Output format button in the Status bar and Click "PDF" option.
        """
        report_obj.switch_ia_ribbon_tab('Home')
        report_obj.wait_for_visible_text(hometab_css, "Filter")
        
        report_obj.select_output_format_from_ribbon("PDF")
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 04.01 : Check "Auto Drill" button is inactive.
        """
        report_obj.verify_ribbon_item_is_disabled("format_auto_drill", "04.01")

        """
            STEP 5 : Click the Output format button in the Status bar and Click " Excel (xlsx)" option.
        """
        report_obj.switch_ia_ribbon_tab('Home')
        report_obj.wait_for_visible_text(hometab_css, "Filter")
        
        report_obj.select_output_format_from_ribbon("Excel (xlsx)->Excel (xlsx)")
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 05.01 : Check "Auto Drill" button is inactive.
        """
        report_obj.verify_ribbon_item_is_disabled("format_auto_drill", "05.01")

        """
            STEP 6 : Click the Output format button in the Status bar and Click "Powerpoint (pptx)" option.
        """
        report_obj.switch_ia_ribbon_tab('Home')
        report_obj.wait_for_visible_text(hometab_css, "Filter")
        
        report_obj.select_output_format_from_ribbon("PowerPoint (pptx)->PowerPoint (pptx)")
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 06.01 : Check "Auto Drill" button is inactive.
        """
        report_obj.verify_ribbon_item_is_disabled("format_auto_drill", "05.01")

        """
            STEP 7 : Click the Output format button in the Status bar and Click "HTML" option.
        """
        report_obj.switch_ia_ribbon_tab('Home')
        report_obj.wait_for_visible_text(hometab_css, "Filter")
        
        report_obj.select_output_format_from_ribbon("HTML")
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 07.01 : Check "Auto Drill" button is active.
        """
        report_obj.verify_ribbon_item_is_enabled("format_auto_drill", "07.01")

        """
            STEP 8 : Click "IA" menu and Select "Close" option.
            STEP 9 : Click "No" button.
        """
        report_obj.close_ia_without_save()  

        """
            STEP 10 : Logout using API:
        """
        report_obj.api_logout()

if __name__ == '__main__':
    unittest.main()