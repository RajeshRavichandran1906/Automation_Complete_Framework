"""-------------------------------------------------------------------------------------------
Created on June 25, 2019
@author: Magesh/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22589378
Test Case Title =  When running a Ring Pie a new Chart Picker type "Extension" is seen
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from common.pages.insight_header import Insight_Header
from common.lib.utillity import UtillityMethods

class C2509763_TestClass(BaseTestCase):

    def test_C2509763(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        insight_header = Insight_Header(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        qwerty_tree_css = "#queryTreeWindow"
        chart_css = "#pfjTableChart_1"
        
        """
            STEP 1 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=baseapp/wf_retail_lite
        """
        chart.invoke_chart_tool_using_api("baseapp/wf_retail_lite")
        chart.wait_for_visible_text(chart_css, "Group 0")
        
        """
            STEP 2 : Click Format tab > Other > Pie > Ring Pie > OK
        """
        chart.select_ia_ribbon_item("Format", "other")
        chart.wait_for_visible_text("#qbSelectChartTypeDlgOkBtn", "OK")
        
        chart.select_other_chart_type("pie", "ring_pie", 4, verify_selection=False)
        chart.wait_for_visible_text(chart_css, "Group 0")
 
        """
            STEP 3 : Double click on "Product, Category" and "Revenue" to add fields.
        """
        chart.double_click_on_datetree_item("Product,Category", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Product,Category")
        
        chart.double_click_on_datetree_item("Revenue", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Revenue")
        
        """
            STEP 4 : Select Format > Run with > Insight
        """
        chart.select_ia_ribbon_item("Format", "run_with")
        chart.select_ia_ribbon_item("Format", "insight")
        
        """
            STEP 5 : Click run
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text("#runbox_id", "Revenue")
        
        """
            STEP 6 : Verify Chart Picker icon shows Ring pie icon in the insight chart
        """
        utils.verify_picture_using_sikuli("C2509763_step6.png", "STEP 6 : Verify Chart Picker icon shows Ring pie icon in the insight chart")

        """
            STEP 7 : Click Change chart drop down(Chart picker)
        """
        insight_header.select_header_option_item("change_chart")        
        
        """
            STEP 8 : Verify Ring pie icon highlighted
        """    
        utils.verify_picture_using_sikuli("C2509763_step8.png","STEP 8 : Verify Ring pie icon highlighted")
        
        """
            STEP 9 : Click Save in the toolbar > Save as "C2509763" > Click Save
        """
        chart.switch_to_default_content()
        chart.save_as_from_application_menu_item("C2509763", target_table_path="P309_S10666->G169735")
 
        """
            STEP 10 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()

        """
            STEP 11 : Run the fex using API
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP309_S10666%2FG169735&BIP_item=C2509763.fex
        """
        chart.run_fex_using_api_url("P309_S10666/G169735", fex_name="C2509763", mrid="mrid", mrpass="mrpass", run_chart_css="#runbox_id")
        chart.wait_for_visible_text("#runbox_id", "Revenue")
         
        """
            STEP 12 : Verify Chart Picker icon shows Ring pie icon in the insight chart
        """
        utils.verify_picture_using_sikuli("C2509763_step12.png", "STEP 12 : Verify Chart Picker icon shows Ring pie icon in the insight chart")

        """
            STEP 13 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()     