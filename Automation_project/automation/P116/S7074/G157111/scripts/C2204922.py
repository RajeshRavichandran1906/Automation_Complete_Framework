'''
Created on Jul 4, 2017

@author: Magesh
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon, ia_resultarea
from common.lib import utillity


class C2204922_TestClass(BaseTestCase):

    def test_C2204922(self):
        """
        TESTCASE VARIABLES
        """
        
        driver = self.driver
        
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        iaresult_obj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step 01: Right click on folder created in IA and
        select New > Chart using the file wf_retail_lite.
        Select Active Reports for the output type.
        Then add Revenue to the Vertical axis and
        Product,Category to the Horizontal axis.
        """
        utillobj.infoassist_api_login('Chart','new_retail/wf_retail_lite','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 65)
        
        ribbonobj.change_output_format_type('active_report')
        time.sleep(4)
        
        metadataobj.datatree_field_click("Revenue",2,1)
        utillobj.synchronize_with_visble_text("#TableChart_1 svg g text[class*='yaxis-title']", "Revenue", 12)
        
        metadataobj.datatree_field_click("Product,Category", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 svg g text[class*='xaxisOrdinal-title']", "ProductCategory", 12)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 01:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 01:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 01: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 7, 'Step 01: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 01: Verify bar color")
        
        """
        Step 02: Right-click on any Bar and select Trendline, then the first option - Linear.
        """
        raiser_css="#TableChart_1 [class*='riser!s0!g1!mbar!']"
        obj_locator1=driver.find_element_by_css_selector(raiser_css)
        utillobj.default_click(obj_locator1, click_option=1)
        time.sleep(1)
        
        raiser_css="#TableChart_1 [class*='riser!s0!g4!mbar!']"
        obj_locator2=driver.find_element_by_css_selector(raiser_css)
        utillobj.default_click(obj_locator2, click_option=1,coordinate_type='top_middle')
        time.sleep(1)
        
        utillobj.select_or_verify_bipop_menu('Add Trendline')
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu('Linear',verify='true',expected_ticked_list=['None'],expected_popup_list=['None', 'Linear', 'Quadratic', 'Polynomial', 'Hyperbolic', 'Logarithmic', 'Modified Hyperbolic', 'Rational', 'Exponential', 'Modified Exponential', 'Log Quadratic', 'Geometric'],msg='Step 02.0: Verify Trendline menu')
        utillobj.synchronize_with_number_of_element("#pfjTableChart_1 path[class*='series!s0!g0!mtrendline!']", 1, 15)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 02:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 02:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 7, 'Step 2: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 02: Verify bar color")
        
        iaresult_obj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 02(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("TableChart_1", "series!s0!g0!mtrendline!", "bar_blue1", "Step 02(ii): Verify first trendline color", attribute_type='stroke')
        
        """Click the Run button."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f svg g text[class*='xaxisOrdinal-title']", "ProductCategory", 20)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 02:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 02:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 02: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 7, 'Step 2: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 02: Verify bar color")
        time.sleep(5)
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Revenue BY Product Category', 'Step 02: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 1, 'Step 02(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "series!s0!g0!mtrendline!", "bar_blue", "Step 02(ii): Verify first trendline color", attribute_type='stroke')
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        result_obj.select_panel_caption_btn(0, select_type='close', custom_css="div[id^='QbReportWindow']")
        time.sleep(10)
        
        """
        Step 03: Switch back to the Preview pane.
        Right-click on any Bar and select Trendline, then the second option - Quadratic.
        """
        raiser_css1="#TableChart_1 [class='riser!s0!g1!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css1)
        utillobj.default_click(obj_locator)
        time.sleep(2)
        
        raiser_css="#TableChart_1 [class='riser!s0!g4!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css)
        utillobj.default_click(obj_locator, click_option=1,coordinate_type='top_middle')
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Add Trendline')
        utillobj.select_or_verify_bipop_menu('Quadratic',verify='true',expected_ticked_list=['Linear'],expected_popup_list=['None', 'Linear', 'Quadratic', 'Polynomial', 'Hyperbolic', 'Logarithmic', 'Modified Hyperbolic', 'Rational', 'Exponential', 'Modified Exponential', 'Log Quadratic', 'Geometric'],msg='Step 03.0: Verify Trendline menu')
        utillobj.synchronize_with_number_of_element("#pfjTableChart_1 path[class*='series!s0!g0!mtrendline!']", 1, 8)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 03:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 03:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 3: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 7, 'Step 3: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 03: Verify bar color")
        
        iaresult_obj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 03(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("TableChart_1", "series!s0!g0!mtrendline!", "bar_blue1", "Step 03(ii): Verify first trendline color", attribute_type='stroke')
        
        """Click the Run button."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f svg g text[class*='xaxisOrdinal-title']", "ProductCategory", 20)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 03:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 03:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 7, 'Step 03: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 03: Verify bar color")
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Revenue BY Product Category', 'Step 03: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 1, 'Step 03(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "series!s0!g0!mtrendline!", "bar_blue", "Step 03(ii): Verify first trendline color", attribute_type='stroke')
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        result_obj.select_panel_caption_btn(0, select_type='close', custom_css="div[id^='QbReportWindow']")
        time.sleep(5)
        
        """
        Step 04: Switch back to the Preview pane.
        Right-click on any Bar and select Trendline, then the third option - Polynomial.
        """
        raiser_css="#TableChart_1 [class*='riser!s0!g0!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css)
        utillobj.default_click(obj_locator)
        time.sleep(1)
        
        raiser_css1="#TableChart_1 [class='riser!s0!g4!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css1)
        utillobj.default_click(obj_locator, click_option=1,coordinate_type='top_middle')
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu('Add Trendline')
#         utillobj.select_or_verify_bipop_menu('Polynomial')
        utillobj.select_or_verify_bipop_menu('Polynomial',verify='true',expected_ticked_list=['Quadratic'],expected_popup_list=['None', 'Linear', 'Quadratic', 'Polynomial', 'Hyperbolic', 'Logarithmic', 'Modified Hyperbolic', 'Rational', 'Exponential', 'Modified Exponential', 'Log Quadratic', 'Geometric'],msg='Step 04.0: Verify Trendline menu')
        utillobj.synchronize_with_number_of_element("#pfjTableChart_1 path[class*='series!s0!g0!mtrendline!']", 1, 8)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 04:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 04:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 04: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 7, 'Step 04: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 04: Verify bar color")
        
        iaresult_obj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 04(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("TableChart_1", "series!s0!g0!mtrendline!", "bar_blue1", "Step 04(ii): Verify first trendline color", attribute_type='stroke')
        
        """Click the Run button."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f svg g text[class*='xaxisOrdinal-title']", "ProductCategory", 20)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 04:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 04:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 04: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 7, 'Step 04: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 04: Verify bar color")
       
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Revenue BY Product Category', 'Step 04: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 1, 'Step 04(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "series!s0!g0!mtrendline!", "bar_blue", "Step 04(ii): Verify first trendline color", attribute_type='stroke')
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        result_obj.select_panel_caption_btn(0, select_type='close', custom_css="div[id^='QbReportWindow']")
        time.sleep(5)
        
        """
        Step 05: Switch back to the Preview pane.
        Right-click on any Bar and select Trendline, then the fourth option - Hyperbolic.
        """
        
        raiser_css="#TableChart_1 [class*='riser!s0!g0!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css)
        utillobj.default_click(obj_locator)
        time.sleep(1)
        raiser_css1="#TableChart_1 [class='riser!s0!g4!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css1)
        utillobj.default_click(obj_locator, click_option=1,coordinate_type='top_middle')
        time.sleep(1)
        
        utillobj.select_or_verify_bipop_menu('Add Trendline')
#         utillobj.select_or_verify_bipop_menu('Hyperbolic')
        utillobj.select_or_verify_bipop_menu('Hyperbolic',verify='true',expected_ticked_list=['Polynomial'],expected_popup_list=['None', 'Linear', 'Quadratic', 'Polynomial', 'Hyperbolic', 'Logarithmic', 'Modified Hyperbolic', 'Rational', 'Exponential', 'Modified Exponential', 'Log Quadratic', 'Geometric'],msg='Step 05.0: Verify Trendline menu')
        parent_css= "#TableChart_1 svg>g path[class^='series']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 05:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 05:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 05: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 7, 'Step 05: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 05: Verify bar color")
        
        iaresult_obj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 05(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("TableChart_1", "series!s0!g0!mtrendline!", "bar_blue1", "Step 05(ii): Verify first trendline color", attribute_type='stroke')
        
        """Click the Run button."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f svg g text[class*='xaxisOrdinal-title']", "ProductCategory", 20)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 05:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 05:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 5: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 7, 'Step 5: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 05: Verify bar color")
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Revenue BY Product Category', 'Step 05: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 1, 'Step 05(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "series!s0!g0!mtrendline!", "bar_blue", "Step 05(ii): Verify first trendline color", attribute_type='stroke')
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        result_obj.select_panel_caption_btn(0, select_type='close', custom_css="div[id^='QbReportWindow']")
        time.sleep(5)
        
        """
        Step 06: Switch back to the Preview pane.
        Right-click on any Bar and select Trendline, then the fifth option - Logarithmic.
        """
        raiser_css="#TableChart_1 [class*='riser!s0!g0!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css)
        utillobj.default_click(obj_locator)
        time.sleep(1)
        
        raiser_css1="#TableChart_1 [class='riser!s0!g4!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css1)
        utillobj.default_click(obj_locator, click_option=1,coordinate_type='top_middle')
        time.sleep(1)
        
        utillobj.select_or_verify_bipop_menu('Add Trendline')
#         utillobj.select_or_verify_bipop_menu('Modified Hyperbolic')
        utillobj.select_or_verify_bipop_menu('Logarithmic',verify='true',expected_ticked_list=['Hyperbolic'],expected_popup_list=['None', 'Linear', 'Quadratic', 'Polynomial', 'Hyperbolic', 'Logarithmic', 'Modified Hyperbolic', 'Rational', 'Exponential', 'Modified Exponential', 'Log Quadratic', 'Geometric'],msg='Step 07.0: Verify Trendline menu')
        time.sleep(4)
        
        """Click the Run button."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f svg g text[class='xaxisOrdinal-title']", "ProductCategory", 20)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 06:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 06:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 06: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 7, 'Step 06: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 06: Verify bar color")
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Revenue BY Product Category', 'Step 06: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        parent_css= "#MAINTABLE_wbody0 svg>g path[class^='series']"
        result_obj.wait_for_property(parent_css, 1)
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 1, 'Step 02(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "series!s0!g0!mtrendline!", "bar_blue", "Step 06(ii): Verify first trendline color", attribute_type='stroke')
        
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        result_obj.select_panel_caption_btn(0, select_type='close', custom_css="div[id^='QbReportWindow']")
        time.sleep(5)
        
        """
        Step 07: Switch back to the Preview pane.
        Right-click on any Bar and select Trendline, then the sixth option - Modified Hyperbolic.
        """
        raiser_css="#TableChart_1 [class*='riser!s0!g0!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css)
        utillobj.default_click(obj_locator)
        time.sleep(1)
        raiser_css1="#TableChart_1 [class='riser!s0!g4!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css1)
        utillobj.default_click(obj_locator, click_option=1,coordinate_type='top_middle')
        time.sleep(1)
        
        utillobj.select_or_verify_bipop_menu('Add Trendline')
#         utillobj.select_or_verify_bipop_menu('Modified Hyperbolic')
        utillobj.select_or_verify_bipop_menu('Modified Hyperbolic',verify='true',expected_ticked_list=['Logarithmic'],expected_popup_list=['None', 'Linear', 'Quadratic', 'Polynomial', 'Hyperbolic', 'Logarithmic', 'Modified Hyperbolic', 'Rational', 'Exponential', 'Modified Exponential', 'Log Quadratic', 'Geometric'],msg='Step 07.0: Verify Trendline menu')
        time.sleep(4)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 07:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 07:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 7: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 7, 'Step 7: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 07: Verify bar color")
        
        iaresult_obj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 07(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("TableChart_1", "series!s0!g0!mtrendline!", "bar_blue1", "Step 07(ii): Verify first trendline color", attribute_type='stroke')
        
        """Click the Run button."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f svg g text[class*='xaxisOrdinal-title']", "ProductCategory", 20)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 07:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 07:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 07: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 7, 'Step 7: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 07: Verify bar color")
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Revenue BY Product Category', 'Step 07: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 1, 'Step 07(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "series!s0!g0!mtrendline!", "bar_blue", "Step 07(ii): Verify first trendline color", attribute_type='stroke')
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        result_obj.select_panel_caption_btn(0, select_type='close', custom_css="div[id^='QbReportWindow']")
        time.sleep(5)
        
        """
        Step 08: Switch back to the Preview pane.
        Right-click on any Bar and select Trendline, then the seventh option - Rational.
        """
        
        raiser_css="#TableChart_1 [class*='riser!s0!g0!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css)
        utillobj.default_click(obj_locator)
        time.sleep(1)
        
        raiser_css1="#TableChart_1 [class='riser!s0!g4!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css1)
        utillobj.default_click(obj_locator, click_option=1,coordinate_type='top_middle')
        time.sleep(1)
        
        utillobj.select_or_verify_bipop_menu('Add Trendline')
#         utillobj.select_or_verify_bipop_menu('Rational')
        utillobj.select_or_verify_bipop_menu('Rational',verify='true',expected_ticked_list=['Modified Hyperbolic'],expected_popup_list=['None', 'Linear', 'Quadratic', 'Polynomial', 'Hyperbolic', 'Logarithmic', 'Modified Hyperbolic', 'Rational', 'Exponential', 'Modified Exponential', 'Log Quadratic', 'Geometric'],msg='Step 08.0: Verify Trendline menu')
        time.sleep(4)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 08:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 08:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 8: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 7, 'Step 8: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 08: Verify bar color")
        
        iaresult_obj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 8(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("TableChart_1", "series!s0!g0!mtrendline!", "bar_blue1", "Step 8(ii): Verify first trendline color", attribute_type='stroke')
        
        """Click the Run button."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f svg g text[class*='xaxisOrdinal-title']", "ProductCategory", 20)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 08:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 08:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 8: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 7, 'Step 8: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 08: Verify bar color")
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Revenue BY Product Category', 'Step 08: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        parent_css= "#MAINTABLE_wbody0 svg>g path[class^='series']"
        result_obj.wait_for_property(parent_css, 1)
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 1, 'Step 08(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "series!s0!g0!mtrendline!", "bar_blue", "Step 08(ii): Verify first trendline color", attribute_type='stroke')
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        result_obj.select_panel_caption_btn(0, select_type='close', custom_css="div[id^='QbReportWindow']")
        time.sleep(5)
        
        """
        Step 09: Switch back to the Preview pane.
        Right-click on any Bar and select Trendline, then the eighth option - Exponential.
        """
        raiser_css="#TableChart_1 [class*='riser!s0!g0!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css)
        utillobj.default_click(obj_locator)
        time.sleep(1)
        
        raiser_css1="#TableChart_1 [class='riser!s0!g4!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css1)
        utillobj.default_click(obj_locator, click_option=1,coordinate_type='top_middle')
        time.sleep(1)
        
        utillobj.select_or_verify_bipop_menu('Add Trendline')
#         utillobj.select_or_verify_bipop_menu('Exponential')
        utillobj.select_or_verify_bipop_menu('Exponential',verify='true',expected_ticked_list=['Rational'],expected_popup_list=['None', 'Linear', 'Quadratic', 'Polynomial', 'Hyperbolic', 'Logarithmic', 'Modified Hyperbolic', 'Rational', 'Exponential', 'Modified Exponential', 'Log Quadratic', 'Geometric'],msg='Step 09.0: Verify Trendline menu')
        time.sleep(4)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 09:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 09:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 09: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 7, 'Step 09: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 09: Verify bar color")
        
        iaresult_obj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 09(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("TableChart_1", "series!s0!g0!mtrendline!", "bar_blue1", "Step 09(ii): Verify first trendline color", attribute_type='stroke')
        
        """Click the Run button."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f svg g text[class*='xaxisOrdinal-title']", "ProductCategory", 20)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 09:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 09:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 09: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 7, 'Step 09: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 09: Verify bar color")
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Revenue BY Product Category', 'Step 09: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        parent_css= "#MAINTABLE_wbody0 svg>g path[class^='series']"
        result_obj.wait_for_property(parent_css, 1)
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 1, 'Step 09(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "series!s0!g0!mtrendline!", "bar_blue", "Step 09(ii): Verify first trendline color", attribute_type='stroke')
        
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        result_obj.select_panel_caption_btn(0, select_type='close', custom_css="div[id^='QbReportWindow']")
        time.sleep(5)
        
        """
        Step 10: Switch back to the Preview pane.
        Right-click on any Bar and select Trendline, then the ninth option - Modified Exponential.
        """
        raiser_css="#TableChart_1 [class*='riser!s0!g0!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css)
        utillobj.default_click(obj_locator)
        time.sleep(1)
        
        raiser_css1="#TableChart_1 [class='riser!s0!g4!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css1)
        utillobj.default_click(obj_locator, click_option=1,coordinate_type='top_middle')
        time.sleep(1)
        
        utillobj.select_or_verify_bipop_menu('Add Trendline')
#         utillobj.select_or_verify_bipop_menu('Modified Exponential')
        utillobj.select_or_verify_bipop_menu('Modified Exponential',verify='true',expected_ticked_list=['Exponential'],expected_popup_list=['None', 'Linear', 'Quadratic', 'Polynomial', 'Hyperbolic', 'Logarithmic', 'Modified Hyperbolic', 'Rational', 'Exponential', 'Modified Exponential', 'Log Quadratic', 'Geometric'],msg='Step 010.0: Verify Trendline menu')
        time.sleep(4)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 10:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 10:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 10: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 7, 'Step 10: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 10: Verify bar color")
       
        iaresult_obj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 10(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("TableChart_1", "series!s0!g0!mtrendline!", "bar_blue1", "Step 10(ii): Verify first trendline color", attribute_type='stroke')
        
        """Click the Run button."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f svg g text[class*='xaxisOrdinal-title']", "ProductCategory", 20)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 10:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 10:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 10: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 7, 'Step 10: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 10: Verify bar color")
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Revenue BY Product Category', 'Step 10: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
       
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 1, 'Step 10(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "series!s0!g0!mtrendline!", "bar_blue", "Step 10(ii): Verify first trendline color", attribute_type='stroke')
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        result_obj.select_panel_caption_btn(0, select_type='close', custom_css="div[id^='QbReportWindow']")
        time.sleep(5)
        
        """
        Step 11: Switch back to the Preview pane.
        Right-click on any Bar and select Trendline, then the tenth option - Log Quadratic.
        """
        
        raiser_css="#TableChart_1 [class*='riser!s0!g0!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css)
        utillobj.default_click(obj_locator)
        time.sleep(1)
        
        raiser_css1="#TableChart_1 [class='riser!s0!g4!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css1)
        utillobj.default_click(obj_locator, click_option=1,coordinate_type='top_middle')
        time.sleep(1)
        
        utillobj.select_or_verify_bipop_menu('Add Trendline')
#         utillobj.select_or_verify_bipop_menu('Log Quadratic')
        utillobj.select_or_verify_bipop_menu('Log Quadratic',verify='true',expected_ticked_list=['Modified Exponential'],expected_popup_list=['None', 'Linear', 'Quadratic', 'Polynomial', 'Hyperbolic', 'Logarithmic', 'Modified Hyperbolic', 'Rational', 'Exponential', 'Modified Exponential', 'Log Quadratic', 'Geometric'],msg='Step 011.0: Verify Trendline menu')
        time.sleep(4)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 11:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 11:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 11: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 7, 'Step 11: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 11: Verify bar color")
        
        iaresult_obj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 11(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("TableChart_1", "series!s0!g0!mtrendline!", "bar_blue1", "Step 11(ii): Verify first trendline color", attribute_type='stroke')
        
        """Click the Run button."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f svg g text[class*='xaxisOrdinal-title']", "ProductCategory", 20)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 11:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 11:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 11: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 7, 'Step 11: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 11: Verify bar color")
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Revenue BY Product Category', 'Step 11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 1, 'Step 11(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "series!s0!g0!mtrendline!", "bar_blue", "Step 11(ii): Verify first trendline color", attribute_type='stroke')
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        result_obj.select_panel_caption_btn(0, select_type='close', custom_css="div[id^='QbReportWindow']")
        time.sleep(5)
        
        """
        Step 12: Switch back to the Preview pane.
        Right-click on any Bar and select Trendline, then the eleventh option - Geometric.
        """
        
        raiser_css="#TableChart_1 [class*='riser!s0!g0!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css)
        utillobj.default_click(obj_locator)
        time.sleep(1)
        
        raiser_css1="#TableChart_1 [class='riser!s0!g4!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css1)
        utillobj.default_click(obj_locator, click_option=1,coordinate_type='top_middle')
        time.sleep(1)
       
        utillobj.select_or_verify_bipop_menu('Add Trendline')
#         utillobj.select_or_verify_bipop_menu('Geometric')
        utillobj.select_or_verify_bipop_menu('Geometric',verify='true',expected_ticked_list=['Log Quadratic'],expected_popup_list=['None', 'Linear', 'Quadratic', 'Polynomial', 'Hyperbolic', 'Logarithmic', 'Modified Hyperbolic', 'Rational', 'Exponential', 'Modified Exponential', 'Log Quadratic', 'Geometric'],msg='Step 012.0: Verify Trendline menu')
        time.sleep(4)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 12:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 12:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 12: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 7, 'Step 12: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 12: Verify bar color")
        
        iaresult_obj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 12(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("TableChart_1", "series!s0!g0!mtrendline!", "bar_blue1", "Step 12(ii): Verify first trendline color", attribute_type='stroke')
        
        """Click the Run button."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f svg g text[class*='xaxisOrdinal-title']", "ProductCategory", 20)
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 12:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 12:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 12: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 7, 'Step 12: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 12: Verify bar color")
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Revenue BY Product Category', 'Step 12: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        parent_css= "#MAINTABLE_wbody0 svg>g path[class^='series']"
        result_obj.wait_for_property(parent_css, 1)
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 1, 'Step 12(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "series!s0!g0!mtrendline!", "bar_blue", "Step 12(ii): Verify first trendline color", attribute_type='stroke')
        
        utillobj.switch_to_default_content(pause=1)
        
        parent_css="#applicationButton img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2204922_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
if __name__ == '__main__':
    unittest.main()