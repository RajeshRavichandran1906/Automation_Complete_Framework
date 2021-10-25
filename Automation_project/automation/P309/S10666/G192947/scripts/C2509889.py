"""-------------------------------------------------------------------------------------------
Created on June 21, 2019
@author: Niranjan/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2509889
Test Case Title =  Field amper parameters values retained on Reset
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from common.wftools.report import Report
from common.wftools.designer_chart import Designer_Insight

class C2509889_TestClass(BaseTestCase):

    def test_C2509889(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        report = Report(self.driver)
        insight = Designer_Insight(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        qwerty_tree_css = "#queryTreeWindow"
        chart_css = "#pfjTableChart_1"
        save_css = "#IbfsOpenFileDialog7_btnOK"
        insight_chart_css = "#runbox_id"
    
        """
            STEP 1 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=baseapp/wf_retail_lite
        """
        chart.invoke_chart_tool_using_api("baseapp/wf_retail_lite")
        chart.wait_for_visible_text(chart_css, "Group 0")
        
        """
            STEP 2 : Right click on Horizontal > select 'New Parameter'
        """
        chart.right_click_on_field_under_query_tree("Horizontal Axis", 1, "New Parameter")
        chart.wait_for_visible_text(qwerty_tree_css, "Parameter1")  
           
        """
            STEP 3 : Drag "Product, Category" and "Product, Subcategory" under Parameter1
        """
        chart.drag_field_from_data_tree_to_query_pane("Product,Category", 1, "Parameter1", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Product,Category")
        
        chart.drag_field_from_data_tree_to_query_pane("Product,Subcategory", 1, "Product,Category", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Product,Subcategory")
        
        """
            STEP 4 : Right click on Vertical > select New Parameter
        """
        chart.right_click_on_field_under_query_tree("Vertical Axis", 1, "New Parameter")
        chart.wait_for_visible_text(qwerty_tree_css, "Parameter2")
        
        """
            STEP 5 : Drag "Revenue" and "Quantity, Sold" under Parameter2
        """
        chart.drag_field_from_data_tree_to_query_pane("Revenue", 1, "Parameter2", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Revenue")
        
        chart.drag_field_from_data_tree_to_query_pane("Quantity,Sold", 1, "Revenue", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Quantity,Sold")
        
        """
            STEP 6 : Verify following query and preview has been displayed
        """
        chart.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="Step 6.01")
        chart.verify_y_axis_label_in_preview(['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M'], msg="Step 6.02")
        chart.verify_x_axis_title_in_preview(['Product Category'], msg="Step 6.03")
        chart.verify_y_axis_title_in_preview(['Revenue'], msg="Step 6.04")
        chart.verify_number_of_risers("#pfjTableChart_1 rect", 1, 7, msg="Step 6.05")
        
        """
            STEP 7 : Select Format > Run with > Insight
        """
        chart.select_ia_ribbon_item("Format", "run_with")
        chart.select_ia_ribbon_item("Format", "insight")
        
        """
            STEP 8 : Click Save in the toolbar > Save as "C2509889" > Click Save
        """
        chart.select_item_in_top_toolbar("save")
        chart.wait_for_visible_text(save_css, "Save")
        
        chart.save_file_in_save_dialog("C2509889")
        
        """
            STEP 9 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.logout_chart_using_api()
        
        """
            STEP 10 : Run the fex from the BIP using API
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP309_S10666%2FG169735&BIP_item=C2509889.fex
        """
        chart.run_fex_using_api_url("P309_S10666/G169735", fex_name="C2509889", mrid="mrid", mrpass="mrpass", run_chart_css="div#promptPanel")
        
        """
            STEP 10.01 : Expected to see auto prompt
        """
        chart.wait_for_visible_text("div#promptPanel", "Filter Values")
        report.verify_selected_field_dropdown_value_in_autoprompt("Parameter2", "Revenue", msg="STEP 10.01 : Expected to see auto prompt")
        report.verify_selected_field_dropdown_value_in_autoprompt("Parameter1", "Product Category", msg="STEP 10.02 : Expected to see auto prompt")

        """
            STEP 11 :  Accept the default selections from the Auto Prompt screen by selecting the Auto Prompt Run icon
        """
        report.run_auto_prompt_report()
        
        """
            STEP 11.01 : Expected to see "Revenue By Product, Category" values chart displayed
        """
        chart.switch_to_frame("iframe.autop-wf-output")
        chart.wait_for_visible_text("#runbox_id", "Revenue")
        chart.verify_x_axis_label_in_run_window(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="Step 11.01", parent_css=insight_chart_css)
        chart.verify_y_axis_label_in_run_window(['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M'], msg = "Step 11.02", parent_css=insight_chart_css)
        chart.verify_x_axis_title_in_run_window(['Product Category'], msg="Step 11.03", parent_css=insight_chart_css)
        chart.verify_y_axis_title_in_run_window(['Revenue'], msg="Step 11.04", parent_css=insight_chart_css)
        chart.verify_number_of_risers("#runbox_id rect", 1, 7, msg="Step 11.05",)
        
        """
            STEP 12 : From the Insight Options shelf > select "Reset" button
        """
        insight.select_insight_optionsbox_in_preview("Reset")
        chart.wait_for_visible_text("#runbox_id", "Revenue")
        
        """
            STEP 13 : Verify amper values are retained
            STEP 13.01 : "Revenue By Product, Category" values chart displayed
        """
        chart.verify_x_axis_label_in_run_window(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="Step 13.01", parent_css=insight_chart_css)
        chart.verify_y_axis_label_in_run_window(['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M'], msg = "Step 13.02", parent_css=insight_chart_css)
        chart.verify_x_axis_title_in_run_window(['Product Category'], msg="Step 13.03", parent_css=insight_chart_css)
        chart.verify_y_axis_title_in_run_window(['Revenue'], msg="Step 13.04", parent_css=insight_chart_css)
        chart.verify_number_of_risers("#runbox_id rect", 1, 7, msg="Step 13.05",)
        
        """
            STEP 14 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()

if __name__ == '__main__':
    unittest.main()            