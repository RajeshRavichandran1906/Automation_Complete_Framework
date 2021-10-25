'''
Developed By   : KK14897
Developed Date : 21-09-2018

Test Suite = http://172.19.2.180/testrail/index.php?/runs/view/77665&group_by=cases:section_id&group_order=asc&group_id=156524
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2274415
TestCase Name = Auto Drill (or OLAP auto drill) and Accessibility enabled returns 'XML did not run' error
'''
import unittest
from common.wftools import report
from common.lib.basetestcase import BaseTestCase

class C2274415_TestClass(BaseTestCase):
    
    def test_C2274415(self):
        
        report_obj=report.Report(self.driver)
        """    
            Step 01 : Launch IA, Report using Api link
            http://machine:port/alias/ia?tool=Report&master=ibisamp/carolap&item=IBFS%3A%2FWFC%2FRepository%2FP276_S9970/G156524    
        """
        report_obj.invoke_ia_tool_using_api_login("report", "ibisamp/carolap", 'mrid')
        
        """    
            Step 02 : Double click on "SALES", "COUNTRY"
        """
        report_obj.double_click_on_datetree_item("SALES", 1)
        report_obj.wait_for_visible_text('#queryTreeColumn', 'SALES', report_obj.report_long_timesleep)
        report_obj.double_click_on_datetree_item("COUNTRY->COUNTRY->COUNTRY", 3)
        report_obj.wait_for_visible_text('#queryTreeColumn', 'COUNTRY', report_obj.report_long_timesleep)
        
        """    
            Step 03 : Select Format Tab -> click "Auto Drill"
        """
        report_obj.select_ia_ribbon_item("Format", "auto_drill")
        
        """    
            Step 04 : Verify the "Accessibility" is gray out (from features group)
        """
        report_obj.wait_for_number_of_element("#FormatAccessibility [disabled='true']", 1)
        report_obj.verify_ribbon_item_is_disabled('format_accessibility', '04.01')
        
        """    
            Step 05 : Click "Auto drill" again to disable to autodrill 
        """
        report_obj.select_ia_ribbon_item("Format", "auto_drill")
        
        """    
            Step  6 : Click "Accessibility" (from features group)
        """
        report_obj.select_ia_ribbon_item("Format", "accessibility")
        
        """    
            Step 07 : Verify the "Auto drill" is gray out    
        """
        report_obj.wait_for_number_of_element("#FormatAutoDrill [disabled='true']", 1)
        report_obj.verify_ribbon_item_is_disabled('format_auto_drill', '07.01')
        
        """   
            Step 08 : Logout:
            http://machine:port/alias/service/wf_security_logout.jsp   
        """
        
if __name__ == '__main__':
    unittest.main()