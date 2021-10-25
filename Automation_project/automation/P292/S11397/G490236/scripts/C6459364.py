'''
Created on Sep 10, 2019

@author: Niranjan

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6459364
Test Case Title =  Use existing bin for histogram
'''
import unittest,pyautogui,time
from common.wftools.chart import Chart
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.pages.visualization_metadata import Visualization_Metadata 

class C6459364_TestClass(BaseTestCase):

    def test_C6459364(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        utils = UtillityMethods(self.driver)
        metaobj = Visualization_Metadata(self.driver)
        coreutils = CoreUtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        querytree_css = "#queryTreeWindow"
        chart_css = "#pfjTableChart_1"
        ok_button_css = "#qbSelectChartTypeDlgOkBtn"
        
        Step1 = """
            STEP 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG435181%2F&master=baseapp%2Fwf_retail&tool=chart
        """
        chart.invoke_chart_tool_using_api("baseapp/wf_retail", mrid = "mrid", mrpass = "mrpass", folder_path = "P292_S11397%2FG435181")
        chart.wait_for_visible_text(chart_css, "Group 0")
        utils.capture_screenshot("01.01", Step1)
        
        Step2 = """
            STEP 02 : Right click Revenue > Click "Create Bins"
        """
        metaobj.datatree_field_click("Revenue", 1, 1, 'Create Bins...')
        chart.wait_for_number_of_element("div[id^='QbDialog'] div[class*='active window']", 1, chart.chart_short_timesleep)
        utils.capture_screenshot("02.00", Step2)
        
        Step3 = """
            STEP 03 : Change bin width to 100, change format to integer 9 with comma (I9C) > Click OK button.
        """
        metaobj.create_bin('REVENUE_US_BIN_1', btn_click='OK', bin_width='100', bin_format_edit= 'I9C')
        chart.wait_for_visible_text("[id^='QbMetaDataTree']", "REVENUE_US_BIN_1", chart.chart_medium_timesleep)
        utils.capture_screenshot("03.00", Step3)
        
        Step4 = """
            STEP 04 : Select Format tab > Select Other > Bar > Select "Vertical Histogram" chart > Click OK button.
        """
        chart.select_ia_ribbon_item("Format", "other")
        chart.wait_for_visible_text(ok_button_css, "OK")
        chart.select_other_chart_type("bar", "vertical_histogram", 1, verify_selection=False)
        utils.synchronize_until_element_disappear(ok_button_css, chart.home_page_medium_timesleep)
        utils.capture_screenshot("04.00", Step4)
        
        Step5 = """
            STEP 05 : Double click Revenue.
            Second BIN field is created under data pane.
        """
        chart.double_click_on_datetree_item('Revenue', 1)
        chart.wait_for_visible_text(querytree_css, "REVENUE_US_BIN_2", chart.chart_medium_timesleep)
#         chart.verify_field_listed_under_datatree('Sales', 'REVENUE_US_BIN_2', 17, msg='Step 05.00')
        metaobj.verify_all_data_panel_fields(["REVENUE_US_BIN_2"], 'Step 05.00: Verify data panel fields', comparison_type='asin')
        utils.capture_screenshot("05.00", Step5, True)
        
        Step6 = """
            STEP 06 : Drag REVENUE_US_BIN_1 from data pane over the REVENUE_US_BIN_2 in the query
            REVENUE_US_BIN_2 is replaced with REVENUE_US_BIN_1 and canvas updated.
        """
        REVENUE_US_BIN_elem = utils.validate_and_get_webdriver_objects('table[class="bi-tree-view-table"] img[src*="bins"]', 'REVENUE_US_BIN')
        REVENUE_US_BIN_1_coordinate = coreutils.get_web_element_coordinate(REVENUE_US_BIN_elem[0])
        coreutils.left_click(REVENUE_US_BIN_elem[0])
        pyautogui.mouseDown(REVENUE_US_BIN_1_coordinate['x'], REVENUE_US_BIN_1_coordinate['y'], duration=2)
        REVENUE_US_BIN_2_coordinate=coreutils.get_web_element_coordinate(REVENUE_US_BIN_elem[2])
        pyautogui.moveTo(REVENUE_US_BIN_2_coordinate['x'], REVENUE_US_BIN_2_coordinate['y'], duration =2)
        time.sleep(2)
        pyautogui.mouseUp(REVENUE_US_BIN_2_coordinate['x'], REVENUE_US_BIN_2_coordinate['y'])
        chart.wait_for_visible_text(querytree_css, "REVENUE_US_BIN_1", chart.chart_medium_timesleep)
        chart.verify_field_listed_under_querytree('Measure', 'REVENUE_US_BIN_1', position=2, msg='Step 06.00')
        chart.verify_x_axis_label_in_preview(['0', '100', '200', '300', '400', '500', '600', '700', '800', '900', '1,000', '1,100', '1,200', '1,300', '1,400', '1,500', '1,600', '1,700', '1,800', '1,900', '2,000', '2,100', '2,200', '2,300', '2,400', '2,500', '2,600', '2,700', '2,800', '2,900', '3,000', '3,100', '3,200', '3,300', '3,400', '3,500', '3,700', '3,800', '3,900', '4,000', '4,100', '4,200', '4,400', '4,600', '4,700', '4,800', '5,000', '5,100', '5,200', '5,300', '5,400', '5,500', '5,700', '5,900', '6,000', '6,100', '6,200', '6,300', '6,700', '6,900', '7,100', '7,300', '7,600', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],  msg = "Step 06.01 : Verify canvas updated")
        chart.verify_y_axis_label_in_preview(['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K'], msg = "Step 06.02 : Verify canvas updated")
        chart.verify_x_axis_title_in_preview(["REVENUE_US_BIN_1"],  msg = "Step 06.03 : Verify canvas updated")
        chart.verify_y_axis_title_in_preview(['CNT Revenue'],  msg = "Step 06.04 : Verify canvas updated")
        chart.verify_number_of_risers("#pfjTableChart_1 rect", 1, 85, msg = "Step 06.05 : Verify canvas updated")
        chart.verify_chart_color("pfjTableChart_1", "riser!s0!g1!mbar!", "lochmara", msg = "Step 06.06 : Verify canvas updated")
        utils.capture_screenshot("06.00", Step6, True)
        
        """
            STEP 07 : Logout using API
            http://machine:port/alias/service/wf_security_logout.js
        """
 
if __name__ == '__main__':
    unittest.main()