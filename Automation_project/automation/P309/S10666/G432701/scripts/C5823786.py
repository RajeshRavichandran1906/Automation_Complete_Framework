'''
Created on Jun 24, 2019

@author: Aftab

Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5823786
TestCase Name : UNDO is not working after selecting insight or AutoDrill
'''

import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.lib import utillity

class C5823786_TestClass(BaseTestCase):

    def test_C5823786(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj= chart.Chart(self.driver)
        cor_utl = core_utility.CoreUtillityMethods(self.driver)
        utli_obj = utillity.UtillityMethods(self.driver)
        
        """
            TESTCASE ID Variable 
        """
        format_css = "#FormatTab"
        querypane_css = "#queryBoxColumn"
        
        """
        1 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=baseapp/wf_retail_lite
        """
        chart_obj.invoke_chart_tool_using_api("baseapp/wf_retail_lite")

        """
        2 : Double click on fields "Product,Category" and "Cost of Goods"
        """
        chart_obj.double_click_on_datetree_item('Product,Category', 1)
        chart_obj.wait_for_visible_text(querypane_css,"Product,Category")
        chart_obj.double_click_on_datetree_item('Cost of Goods', 1)
        chart_obj.wait_for_visible_text(querypane_css,"Cost of Goods")
 
        """
        3 : Select Format tab > Run With > Insight
        """
        chart_obj.select_ia_ribbon_item("Format", "run_with")
        chart_obj.wait_for_visible_text(format_css, "Run with")
        chart_obj.select_ia_ribbon_item("Format", "insight") 
        
        """
        4 : Click "Undo" button in the toolbar
        """
        chart_obj.select_item_in_top_toolbar('undo')
        #chart_obj.wait_for_number_of_element(".chartPanel rect[class^='riser!']",1)
       
        """       
        4.01 : Verify Insight is de-selected
        """
        chart_obj.select_ia_ribbon_item("Format", "run_with")
        chart_obj.wait_for_visible_text(format_css, "Run with")
        chart_obj.verify_ribbon_item_not_selected('format_insight','4.01')
        
        """
        5 : Click Save in the toolbar > Save as "C5823786" > Click Save
        """
        chart_obj.select_item_in_top_toolbar('save')
        chart_obj.save_file_in_save_dialog('C5823786')
         
        """
        6 : Logout:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()  
         
        """
        7 : Right click on saved InsightChart > Edit using API link,
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/P309_S10666/G169735/C5823786.fex
        """
        chart_obj.edit_fex_using_api_url(folder_name='P309_S10666/G169735',fex_name='C5823786')
         
        """
        8 : Select Format tab > Run With > AutoDrill
        """
        chart_obj.select_ia_ribbon_item("Format", "run_with")
        chart_obj.wait_for_visible_text(format_css, "Run with")
        chart_obj.select_ia_ribbon_item("Format", "auto_drill")
        
        """
        9 : Click "Undo" button in the toolbar
        """
        chart_obj.select_item_in_top_toolbar('undo')
        #chart_obj.wait_for_number_of_element(".chartPanel rect[class^='riser!']",1)
        
        """
        9.01 Verify AutoDrill is de-selected
        """
        chart_obj.select_ia_ribbon_item("Format", "run_with")
        chart_obj.wait_for_visible_text(format_css, "Run with")
        chartriser = utli_obj.validate_and_get_webdriver_object('#pfjTableChart_1', 'chart_riser')
        cor_utl.python_move_to_element(chartriser)
        chart_obj.verify_ribbon_item_not_selected('format_auto_drill','9.01')

        """
        10 : Logout:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()