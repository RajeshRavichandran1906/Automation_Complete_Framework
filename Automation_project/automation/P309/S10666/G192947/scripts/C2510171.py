'''
Created on Jun 19, 2019

@author: Magesh/Pearlson Joyal

Test Case : http://172.19.2.180/testrail/index.php?/cases/view/2510171
TestCase Name : Removed Show Fex from More Options menu
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage

class C2510171_TestClass(BaseTestCase):

    def test_C2510171(self):
        
        """
        TESTCASE Object's
        """
        chart_obj= chart.Chart(self.driver)
        context_obj=wf_mainpage.Wf_Mainpage(self.driver)
        
        """
            TESTCASE ID Variable 
        """
        format_css = "#FormatTab"
        
        """
        STEP 1 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                 http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=ibisamp/car
        """
        chart_obj.invoke_chart_tool_using_api("ibisamp/car")
                
        """
        STEP 2 : Select Format > Run with > Insight
        """
        chart_obj.select_ia_ribbon_item("Format", "run_with")
        chart_obj.wait_for_visible_text(format_css, "Run with")
        chart_obj.select_ia_ribbon_item("Format", "insight")  
         
        """
        STEP 3 : Click Run
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.wait_for_number_of_element("[id^='ReportIframe']",1)
        chart_obj.switch_to_frame()        
         
        """
        STEP 4 : Click "Chart Options (3 vertical dots)" menu
        """
        chart_obj.select_header_option_item_in_insight("more_options")
         
        """
        STEP 5 : Verify following menu displayed and "Show Fex" not displayed
        """
        context_obj.verify_context_menu_item(expected_context_menu_item_list=['Export Data','Export Image','Series Layout','Y-Axis Log Scale','Show Data Label'], msg='Step 5')
        
        """
        STEP 6 : Click IA > Close > click No.
        """
        chart_obj.switch_to_default_content()
        chart_obj.close_ia_without_save()
           
        """
        STEP 7 : Logout using API
                 http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
   
if __name__ == '__main__':
    unittest.main()