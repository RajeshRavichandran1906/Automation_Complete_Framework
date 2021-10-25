'''
Created on July , 2019

@author: Prasanth
Testcase Name : Tooltip on pie not displaying the proper field
Testcase ID :http://172.19.2.180/testrail/index.php?/cases/view/2276131

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart

class C2276131_TestClass(BaseTestCase):
    
    def test_C2276131(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        
        """
            CLASS VARIABLES
        """
        expected_tooltip_list_1=['COUNTRY:  W GERMANY', 'RETAIL_COST:  64,732  (37.37%)']
        expected_tooltip_list_2=['COUNTRY:  W GERMANY', 'SALES:  88190  (42.31%)']
        
        """
        STEP 1:Launch the IA API with Chart (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP251_S9164%2FG159426&tool=chart&master=ibisamp/car
        """
        chart_obj.invoke_chart_tool_using_api("ibisamp/car")
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
        STEP 2 : Select "Format" > "Chart Types" > "Pie".
        """
        chart_obj.select_ia_ribbon_item('Format', "pie")
        chart_obj.wait_for_number_of_element("text[class*='pieLabel']", 5)
        
        """
        STEP 3 : Double click "COUNTRY","SALES","RETAIL_COST".
        """
        chart_obj.double_click_on_datetree_item("COUNTRY", 1)
        chart_obj.wait_for_visible_text("#singleReportPanel", "COUNTRY")
        chart_obj.double_click_on_datetree_item("SALES", 1)
        chart_obj.wait_for_visible_text("#singleReportPanel", "SALES")
        chart_obj.double_click_on_datetree_item("RETAIL_COST", 1)
        chart_obj.wait_for_visible_text("#singleReportPanel", "RETAIL_COST")
        
        """
        STEP 4: Click Run 
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text("#jschart_HOLD_0","COUNTRY")
        
        """
        STEP 5:Hover over any slice on "RETAIL_COST" pie
        STEP 6:Verify the following chart tool tip info displayed
        """
        chart_obj.verify_active_chart_tooltip("jschart_HOLD_0", "riser!s4!g1!mwedge!", expected_tooltip_list_1, msg="Step 06.01 : Verify the following chart tool tip info displayed")
        
        """
        STEP 7:Hover over any slice on "Sales" pie
        STEP 8:Verify the following chart tool tip info displayed
        """
        chart_obj.verify_active_chart_tooltip("jschart_HOLD_0", "riser!s4!g0!mwedge!", expected_tooltip_list_2, msg="Step 08.01 : Verify the following chart tool tip info displayed")
        
        """
        STEP 9 : Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
if __name__ == '__main__':
    unittest.main()
        
        