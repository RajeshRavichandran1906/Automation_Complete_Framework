'''
Created on June 21, 2019

@author: Aftab

Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2510335
TestCase Name : Last item of Matrix Marker Chart
'''

import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C2510335_TestClass(BaseTestCase):

    def test_C2510335(self):
        """
            CLASS OBJECTS 
        """
        chart_obj= chart.Chart(self.driver)
        
        """
            TESTCASE ID Variable 
        """
        format_css = "#FormatTab"
        querypane_css = "#queryBoxColumn"
        
        """
        1 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=ibisamp/car
        """
        chart_obj.invoke_chart_tool_using_api("ibisamp/car")
        
        """
        2 : Add "COUNTRY" to Horizontal Axis bucket and "DEALER_COST" to Vertical
        """
        chart_obj.drag_field_from_data_tree_to_query_pane("COUNTRY",1,"Horizontal Axis")
        chart_obj.wait_for_visible_text(querypane_css,"COUNTRY")
        chart_obj.drag_field_from_data_tree_to_query_pane("DEALER_COST",1,"Vertical Axis")
        chart_obj.wait_for_visible_text(querypane_css,"DEALER_COST")
        
        """
        3 : Select Format > Run with > Insight
        """
        chart_obj.select_ia_ribbon_item("Format", "run_with")
        chart_obj.wait_for_visible_text(format_css, "Run with")
        chart_obj.select_ia_ribbon_item("Format", "insight")        
         
        """
        4 : Click Run
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()  
         
        """
        5 : Click Chart picker drop down > Select Matrix Marker chart
        """
        chart_obj.change_chart_type_from_chart_picker_option_in_insight('Matrix')
                 
        """
        6 : Verify following Matrix marker chart with all items displayed
        6.01: Bottom item for "West Germany" is fully displayed.
        """
        chart_obj.verify_number_of_risers('#runbox_id circle', 1, 5, msg='Step 6 & 6.01 Matrix marker chart')
               
        """
        7 : Click Save in the toolbar > Save as "C2510335" > Click Save
        """
        chart_obj.switch_to_default_content()
        chart_obj.select_item_in_top_toolbar('save')
        chart_obj.save_file_in_save_dialog('C2510335')
        
        """
        8 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
         
        """
        9 : Run the fex from BIP using API
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP309_S10666%2FG169735&BIP_item=C2510335.fex
        """
        chart_obj.run_fex_using_api_url('P309_S10666/G169735', 'C2510335', mrid="mrid", mrpass="mrpass", run_chart_css="body[class*='ibx-root'] rect[pointer-events='all']")        
         
        """
        10 : Click Chart picker drop down > Select Matrix Marker chart
        """
        chart_obj.change_chart_type_from_chart_picker_option_in_insight('Matrix') 
         
        """
        11 : Verify following Matrix marker chart with all items displayed
        """
        chart_obj.verify_number_of_risers('#runbox_id circle', 1, 5, msg='Step 11 Matrix marker chart')
        
        """
        12 : Logout using API
             http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()