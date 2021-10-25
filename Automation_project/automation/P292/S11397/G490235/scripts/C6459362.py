"""---------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 09-September-2019
---------------------------------------------------------------------------------------"""
from common.wftools.chart import Chart
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods

class C6459362_TestClass(BaseTestCase):

    def test_C6459362(self):
    
        """
            CLASS OBJECTS
        """
        chart = Chart(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """
            VARIABLES
        """
        case_id = "C6459362"
        preview_chart_id = "pfjTableChart_1"
        preview_chart_css = "#"  +preview_chart_id
        run_chart_id = "jschart_HOLD_0"
        run_chart_css = "#" + run_chart_id
        
        STEP_01 = """
            STEP 01 : Launch the IA API with chart - http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG435181%2F&master=baseapp%2Fwf_retail&tool=chart
        """
        chart.invoke_chart_tool_using_api('baseapp/wf_retail')
        chart.wait_for_visible_text(preview_chart_css, "Group", chart.chart_long_timesleep)
        utils.capture_screenshot("01", STEP_01)
        
        STEP_02 = """
            STEP 02 : Expand Customer > Customer > Full,Name > Attributes > Right click Age > Create Bins > leave defaults > Click OK button
        """
        chart.collapse_data_field_section('Filters and Variables')
        chart.collapse_data_field_section('Measure Groups')
        ok_btn_css = "#qbBinsOkBtn"
        chart.right_click_on_datetree_item("Age", 1, "Create Bins...")
        chart.wait_for_visible_text(ok_btn_css, "OK", chart.chart_short_timesleep)
        ok_btn = self.driver.find_element_by_css_selector(ok_btn_css)
        core_utils.left_click(ok_btn)
        utils.synchronize_until_element_disappear(ok_btn_css, chart.chart_short_timesleep)
        utils.capture_screenshot("02", STEP_02)
        
        STEP_03 = """
            STEP 03 : Drag and drop "AGE_BIN_1" to Horizontal Axis
        """
        field_path = "Dimensions->Customer->Customer->Full,Name->Attributes->AGE_BIN_1"
        chart.drag_field_from_data_tree_to_query_pane(field_path, 1, 'Horizontal Axis')
        chart.wait_for_visible_text(preview_chart_css, "AGE_BIN_1", chart.chart_short_timesleep)
        utils.capture_screenshot("03", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Fields added to query pane and canvas updated.
        """
        x_axis_label = ['0', '10', '20', '30', '40', '50', '60', '70', '80']
        chart.verify_field_availability_in_querytree('Horizontal Axis', 'AGE_BIN_1', 'Marker', msg="Step 03.01")
        chart.verify_number_of_risers(preview_chart_css + " rect", 1, 9, msg="Step 03.02")
        chart.verify_x_axis_label_in_preview(x_axis_label, msg="Step 03.03")
        chart.verify_x_axis_title_in_preview(['AGE_BIN_1'], msg="Step 03.04")
        utils.capture_screenshot("03.01", STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Select Format tab > Select "Pie chart" under Chart types group
        """
        pie_riser_css = preview_chart_css + " path"
        chart.select_ia_ribbon_item("Format", "pie")
        utils.synchronize_until_element_is_visible(pie_riser_css, chart.chart_medium_timesleep)
        utils.capture_screenshot("04", STEP_04 )
        
        STEP_04_01 = """
            STEP 04.01 : Bar chart is converted it in to Pie chart
        """
        legends = ['AGE_BIN_1', '0', '10', '20', '30', '40', '50', '60', '70', '80']
        chart.verify_number_of_risers(pie_riser_css, 1, 9, msg="Step 04.01")
        chart.verify_legends_in_preview(legends, msg="Step 04.02")
        chart.verify_chart_color(preview_chart_id, "riser!s0!g0!mwedge!", "bar_blue", "Step 04.03 : Verify chart color")
        utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Double click "Revenue"
        """
        chart.double_click_on_datetree_item("Revenue", 1)
        chart.wait_for_visible_text(preview_chart_css, "Revenue", chart.chart_short_timesleep)
        utils.capture_screenshot("05", STEP_05)
        
        STEP_06 = """
            STEP 06 : Right click "Revenue" in query > More > "Aggregation Functions" > Select "Count".
        """
        chart.right_click_on_field_under_query_tree("Revenue", 1, "More->Aggregation Functions->Count")
        chart.wait_for_visible_text(preview_chart_css, "CNT Revenue", chart.chart_short_timesleep)
        utils.capture_screenshot("06", STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : "CNT" prefix is added to measure field and canvas updated
        """
        legends = ['AGE_BIN_1', '10', '20', '30', '40', '50', '60', '70']
        chart.verify_number_of_risers(pie_riser_css, 1, 7, msg="Step 06.01")
        chart.verify_legends_in_preview(legends, msg="Step 06.02")
        chart.verify_chart_color(preview_chart_id, "riser!s0!g0!mwedge!", "bar_blue", "Step 06.03 : Verify chart color")
        chart.verify_riser_pie_labels_and_legends(preview_chart_id, ['CNT Revenue'], "Step 06.04 : Verify pi label")
        utils.capture_screenshot("06.01", STEP_06_01, True)
        
        STEP_07 = """
            STEP 07 : Right click Bin in Color bucket > Delete
        """
        chart.collapse_data_field_section('Filters and Variables')
        chart.collapse_data_field_section('Measure Groups')
        chart.right_click_on_field_under_query_tree("AGE_BIN_1", 1, "Delete")
        utils.capture_screenshot("07", STEP_07)
        
        STEP_08 = """
            STEP 08 : Double click "AGE_BIN_1" in data pane
        """
        chart.double_click_on_datetree_item(field_path, 1)
        chart.wait_for_visible_text(preview_chart_css, "AGE_BIN_1", chart.chart_short_timesleep)
        utils.capture_screenshot("08", STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : Field added to Horizontal bucket and canvas updated
        """
        legends = ['AGE_BIN_1', '10', '20', '30', '40', '50', '60', '70']
        chart.verify_number_of_risers(pie_riser_css, 1, 7, msg="Step 08.01")
        chart.verify_legends_in_preview(legends, msg="Step 08.02")
        chart.verify_chart_color(preview_chart_id, "riser!s0!g0!mwedge!", "bar_blue", "Step 08.03 : Verify chart color")
        chart.verify_riser_pie_labels_and_legends(preview_chart_id, ['CNT Revenue'], "Step 08.04 : Verify pi label")
        utils.capture_screenshot("08.01", STEP_08_01, True)
        
        STEP_09 = """
            STEP 09 : Click Run button
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text(run_chart_css, "CNT Revenue", chart.chart_short_timesleep)
        utils.capture_screenshot("09", STEP_09)
        
        STEP_09_01 = """
            STEP 09.01 : Chart displayed in run time without error
        """
        legends = ['AGE_BIN_1', '10', '20', '30', '40', '50', '60', '70']
        chart.verify_number_of_risers(run_chart_css + " path", 1, 7, msg="Step 09.01")
        chart.verify_legends_in_run_window(legends, msg="Step 09.02")
        chart.verify_chart_color(run_chart_id, "riser!s0!g0!mwedge!", "bar_blue", "Step 09.03 : Verify chart color")
        chart.verify_riser_pie_labels_and_legends(run_chart_id, ['CNT Revenue'], "Step 09.04 : Verify pi label")
        utils.capture_screenshot("09.01", STEP_09_01, True)
        chart.switch_to_default_content()
        
        STEP_10 = """
            STEP 10 : Click Save icon in the toolbar > Enter title as "C6459362" > Click Save button.
        """
        chart.select_ia_toolbar_item("toolbar_save")
        chart.save_file_in_save_dialog(case_id)
        utils.capture_screenshot("10", STEP_10)
        
        STEP_11 = """
            STEP 11 : Logout using API
        """
        chart.api_logout()
        utils.capture_screenshot("11", STEP_11)
        
        STEP_12 = """
            STEP 12 : Run C6459362.fex from bip
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S11397%2FG435181&BIP_item=C6459362.fex
        """
        chart.run_fex_using_api_url("P292_S11397/G490235", case_id, 'mrid', 'mrpass')
        chart.wait_for_visible_text(run_chart_css, "CNT Revenue", chart.chart_short_timesleep)
        utils.capture_screenshot("12", STEP_12)
        
        STEP_12_01 = """
            STEP 12.01 : Chart displayed in run time
        """
        legends = ['AGE_BIN_1', '10', '20', '30', '40', '50', '60', '70']
        chart.verify_number_of_risers(run_chart_css + " path", 1, 7, msg="Step 12.01")
        chart.verify_legends_in_run_window(legends, msg="Step 12.02")
        chart.verify_chart_color(run_chart_id, "riser!s0!g0!mwedge!", "bar_blue", "Step 12.03 : Verify chart color")
        chart.verify_riser_pie_labels_and_legends(run_chart_id, ['CNT Revenue'], "Step 12.04 : Verify pi label")
        utils.capture_screenshot("12.01", STEP_12_01, True)
        
        STEP_13 = """
            STEP 13 : Logout using API
        """
        chart.api_logout()
        utils.capture_screenshot("13", STEP_13)
        
        STEP_14 = """
            STEP 14 : Restore the C6459362.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG435181%2FC6459362.fex
        """
        chart.edit_fex_using_api_url(None, fex_name=case_id)
        chart.wait_for_visible_text(preview_chart_css, "CNT Revenue", chart.chart_short_timesleep)
        utils.capture_screenshot("14", STEP_14)
        
        STEP_14_01 = """
            STEP 14.01 : Field added to Horizontal bucket and canvas updated
        """
        legends = ['AGE_BIN_1', '10', '20', '30', '40', '50', '60', '70']
        chart.verify_number_of_risers(pie_riser_css, 1, 7, msg="Step 14.01")
        chart.verify_legends_in_preview(legends, msg="Step 14.02")
        chart.verify_chart_color(preview_chart_id, "riser!s0!g0!mwedge!", "bar_blue", "Step 14.03 : Verify chart color")
        chart.verify_riser_pie_labels_and_legends(preview_chart_id, ['CNT Revenue'], "Step 14.04 : Verify pi label")
        utils.capture_screenshot("14.01", STEP_14_01, True)
        
        STEP_15 = """
            STEP 15 : Logout using API
        """
        chart.api_logout()
        utils.capture_screenshot("15", STEP_15)
        