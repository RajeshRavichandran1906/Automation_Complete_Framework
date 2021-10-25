'''
Created on Jun 28, 2019

@author: Varun/Prasanth
Testcase Name : Treemap tooltip is not showing Grouping information
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2276143

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart

class C2276143_TestClass(BaseTestCase):
    
    def test_C2276143(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
    
        """
        STEP 1:Launch the API to create new Chart.
        http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP251_S9164%2FG159435&tool=chart&master=baseapp/wf_retail_lite
        """
        chart_obj.invoke_chart_tool_using_api("baseapp/wf_retail_lite")
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
        STEP 2 : Select "Format" > "Chart Types" > "Other" > "HTML5" > "Treemap".
        STEP 3 : Click "OK".
        """
        chart_obj.select_ia_ribbon_item('Format', "other")
        chart_obj.select_other_chart_type("html5", "tree_map", 1,verify_selection=False)
        
        """
        STEP 4 : Double click on field "Product,Category"
        """
        chart_obj.double_click_on_datetree_item("Product,Category", 1)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Media Player")
        
        """
        STEP 5 : Drag "Brand" to Categories - Grouping (below "Product,Category").
        """
        chart_obj.drag_field_from_data_tree_to_query_pane("Brand", 1, "Product,Category")
        chart_obj.wait_for_visible_text("#singleReportPanel", "Samsung")
        
        """
        STEP 6 : Drag "Gross Profit" to Metric - Size.
        """
        chart_obj.drag_field_from_data_tree_to_query_pane("Gross Profit", 1, "Size")
        chart_obj.wait_for_visible_text("#queryTreeWindow", "Gross Profit")
        
        """
        STEP 7 : Select Data tab > Define.
        """
        chart_obj.select_ia_ribbon_item("Data", "detail_define")
        chart_obj.wait_for_number_of_element("div[id*='QbDialog']", 1)
        chart_obj.define_compute_dialog().enter_values_in_field_textbox("Margin")
        
        
        """
        STEP 8 : Field name = Margin ; calculation = "Gross Profit / Cost of Goods".
        """
        chart_obj.define_compute_dialog().double_click_on_data_field("Gross Profit")
        chart_obj.define_compute_dialog().click_key_buttons("div")
        chart_obj.define_compute_dialog().double_click_on_data_field("Cost of Goods")
        chart_obj.define_compute_dialog().click_ok_button()
        
        """
        STEP 9 : Drag "Margin" to Mertic - Color.
        """
        chart_obj.wait_for_visible_text("#iaMetaDataBrowser", "Margin")
        chart_obj.drag_field_from_data_tree_to_query_pane("Measure Groups->Sales->Margin", 1, "Color")
        
        """
        STEP 10 : Highlight "Margin" > Right mouse click > "More" > "Aggregation Functions" > "Average".
        """
        chart_obj.right_click_on_field_under_query_tree("Margin", 1, "More->Aggregation Functions->Average")
        chart_obj.wait_for_visible_text("#singleReportPanel", "AVE Margin")
        
        """
        STEP 11: Click Run 
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text("#jschart_HOLD_0","AVE Margin")
        
        """
        STEP 12: Hover over any data point and verify the tooltip 
        """
        chart_obj.verify_chart_color("jschart_HOLD_0", "riser!sStereo Systems-_-LG!g0!mnode", "soft_orange1", msg="Step 12.01 : Verify Treemap colors")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 53, msg="Step 12.02 : Verify Treemap")
        expected_tooltip_list=['Product Category:Media Player', 'Brand:Panasonic', 'Gross Profit:$10,334,362.67', 'AVE Margin:0.29']
        chart_obj.verify_tooltip_in_run_window("riser!sMedia Player-_-Panasonic!g0!mnode", expected_tooltip_list, msg="Step 12.03 : Verify_tooltip_in_run_window ")
        
        """
        STEP 13 : Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
if __name__ == '__main__':
    unittest.main()
        
        