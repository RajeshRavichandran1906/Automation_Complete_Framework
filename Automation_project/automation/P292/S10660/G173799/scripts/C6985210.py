"""-------------------------------------------------------------------------------------------
Created on August 05, 2019
@author: Niranjan

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/6985210
Test Case Title =  Verify restore Compute field in Chart mode
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from common.lib.utillity import UtillityMethods
from common.pages.ia_miscelaneous import IA_Miscelaneous
import time

class C6985210_TestClass(BaseTestCase):

    def test_C6985210(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        utils = UtillityMethods(self.driver)
        ia_mis = IA_Miscelaneous(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        qwerty_tree_css = "#queryTreeWindow"
        chart_css = "#pfjTableChart_1"
        cancel_css = "#fldCreatorCancelBtn"
        
        """
            STEP 1 : Launch IA Chart mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10660
        """
        chart.invoke_chart_tool_using_api("baseapp/wf_retail_lite", folder_path="P292/S10032_infoassist_2")
        chart.wait_for_visible_text(chart_css, "Group 0")
        
        """
            STEP 2 : Double click "Revenue","Product,Category".
        """
        chart.double_click_on_datetree_item("Revenue", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Revenue")
        
        chart.double_click_on_datetree_item("Product,Category", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Product,Category")
        
        """
            STEP 3 : Select "Data" > "Summary (Compute)".
        """
        chart.select_ia_ribbon_item("Data", "summary_compute")
        chart.wait_for_visible_text(cancel_css, "Cancel")
        
        """
            STEP 4 : Enter "Field" = "NewRevenue".
        """
        chart.define_compute_dialog().enter_values_in_field_textbox("NewRevenue")
        
        """
            STEP 5 : Double click "Revenue".
        """
        chart.define_compute_dialog().double_click_on_data_field("Revenue", 1)
        time.sleep(3)
        
        """
            STEP 6 : Enter "+ 9999999" into the textbox.
        """
        chart.define_compute_dialog().enter_values_in_text_area("+ 9999999", clear=False)
        
        """
            STEP 7 : Click "OK".
        """
        chart.define_compute_dialog().click_ok_button()
        utils.synchronize_until_element_disappear("#fldCreatorCancelBtn", chart.home_page_medium_timesleep)
        
        """
            STEP 8 : Verify the following chart is displayed.
        """
        chart.verify_x_axis_title_in_preview(['Product Category'],  msg="Step 8.1")
        chart.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="Step 8.2")
        chart.verify_y_axis_label_in_preview(['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M'], msg="Step 8.3")
        chart.verify_legends_in_preview(['Revenue', 'NewRevenue'], msg="Step 8.4")
        chart.verify_number_of_risers("#pfjTableChart_1 rect", 1, 14, msg="Step 8.5")
        chart.verify_chart_color("pfjTableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 8.6 : Verify the following chart is displayed")
        chart.verify_chart_color("pfjTableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 8.7 : Verify the following chart is displayed")
        
        """
            STEP 9 : Click "Run".
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text("#jschart_HOLD_0", "Accessories")
        
        """
            STEP 10 : Verify the following chart is displayed.
        """
        self.driver.set_page_load_timeout(30)
        chart.verify_x_axis_title_in_run_window(['Product Category'],  msg="Step 10.1")
        chart.verify_x_axis_label_in_run_window(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="Step 10.2")
        chart.verify_y_axis_label_in_run_window(['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M'], msg="Step 10.3")
        chart.verify_legends_in_run_window(['Revenue', 'NewRevenue'], msg="Step 10.4")
        chart.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 14, msg="Step 10.5")
        chart.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 10.6 : Verify the following chart is displayed")
        chart.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar!", "pale_green", "Step 10.7 : Verify the following chart is displayed")
        chart.switch_to_default_content()
        
        """
            STEP 11 : Highlight "NewRevenue" > Right mouse click > "Edit Compute".
        """
        chart.right_click_on_field_under_query_tree("NewRevenue", 1, "Edit Compute")
        chart.wait_for_visible_text(cancel_css, "Cancel")
        
        """
            STEP 12 : Enter 'Field' = 'NewRevenue_1'.
        """
        chart.define_compute_dialog().enter_values_in_field_textbox("NewRevenue_1")
            
        """
            STEP 13 : Click "OK".
        """ 
        chart.define_compute_dialog().click_ok_button()
        utils.synchronize_until_element_disappear("#fldCreatorCancelBtn", chart.home_page_medium_timesleep)
        
        """
            STEP 14 : Verify the following chart is displayed.
        """
        chart.verify_x_axis_title_in_preview(['Product Category'],  msg="Step 14.1")
        chart.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="Step 14.2")
        chart.verify_y_axis_label_in_preview(['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M'], msg="Step 14.3")
        chart.verify_legends_in_preview(['Revenue', 'NewRevenue_1'], msg="Step 14.4")
        chart.verify_number_of_risers("#pfjTableChart_1 rect", 1, 14, msg="Step 14.5")
        chart.verify_chart_color("pfjTableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 14.6 : Verify the following chart is displayed")
        chart.verify_chart_color("pfjTableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 14.7 : Verify the following chart is displayed")
        
        """
            STEP 15 : Click "IA" > "Save".
        """
        chart.select_ia_application_menu("save")
        chart.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")
        
        """
            STEP 16 : Enter Title = "C6985210".
            STEP 17 : Click "Save".
        """
        chart.save_file_in_save_dialog("C6985210")
        utils.synchronize_until_element_disappear("#IbfsOpenFileDialog7_btnCancel", chart.home_page_short_timesleep)
        time.sleep(5)
        
        """
            STEP 18 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
        chart.logout_chart_using_api()
        
        """
            STEP 19 : Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC6985210.fex&tool=Chart
        """
        ia_mis.invoke_ia_tool_in_edit_mode_using_api("C6985210", tool="chart", mrid='mrid', mrpass='mrpass', folder_path="P292/S10032_infoassist_2")
        chart.wait_for_visible_text("#pfjTableChart_1", "Accessories")
        
        """
            STEP 20 : Verify Chart on "Live Preview".
        """
        chart.verify_x_axis_title_in_preview(['Product Category'],  msg="Step 20.1")
        chart.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="Step 20.2")
        chart.verify_y_axis_label_in_preview(['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M'], msg="Step 20.3")
        chart.verify_legends_in_preview(['Revenue', 'NewRevenue_1'], msg="Step 20.4")
        chart.verify_number_of_risers("#pfjTableChart_1 rect", 1, 14, msg="Step 20.5")
        chart.verify_chart_color("pfjTableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 20.6 : Verify the following chart is displayed")
        chart.verify_chart_color("pfjTableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 20.7 : Verify the following chart is displayed")
        
        """
            STEP 21 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart.api_logout()
        
if __name__ == '__main__':
    unittest.main()