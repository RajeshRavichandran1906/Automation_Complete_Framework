'''
Created on JUL 19, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2234976
TestCase Name = Verify chart filter functionality in Vertical Cluster Bars in others tab (under Format menu).
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,active_chart_rollup,ia_ribbon
from common.lib import utillity
# from selenium.webdriver.common.by import By

class C2234976_TestClass(BaseTestCase):

    def test_C2234976(self):
        
        Test_Case_ID="C2234976"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """
            Step 01: Create a new Chart ion IA using the GGSALES file.
                        Select Active Report as Output file format.
                        Select Format > Other
                        From Select Vertical Cluster Bars
        """    
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        element_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        
        ribbonobj.change_output_format_type('active_report', location='Home')
        element_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        
        ribbonobj.select_ribbon_item('Format', 'Other')
        element_css='#TableChart_1'
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        ia_ribbonobj.select_other_chart_type('bar', 'vertical_clustered_bars', 1, ok_btn_click=True)

        """
            Step 02 : Add fields: Category under Horizontal Axis
                        Unit Sales and Dollar Sales under Vertical Axis
                        Click Ok and run.
        """
        metadataobj.datatree_field_click('Category', 1, 0, 'Add To Query', 'Horizontal Axis')
        element_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'Category', 20)
        
        metadataobj.datatree_field_click('Unit Sales', 1, 0, 'Add To Query', 'Vertical Axis')
        element_css="#TableChart_1 .chartPanel g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 20)
        
        metadataobj.datatree_field_click('Dollar Sales', 1, 0, 'Add To Query', 'Vertical Axis')
        element_css="#TableChart_1 .legend g text[class*='legend-labels!s1']"
        utillobj.synchronize_with_visble_text(element_css, 'DollarSales', 20)
        
        resobj.verify_xaxis_title("TableChart_1", "Category", "Step 02.1 : Verify -xAxis Title")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M','6M', '7M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 02.2: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 02.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 02.4: Verify  bar color")
        resobj.verify_riser_legends('TableChart_1', ['Unit Sales', 'Dollar Sales'], "Step 02.5:")
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        utillobj.switch_to_frame(pause=2)
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category", "Step 2a.1: Verify -xAxis Title")
        expected_xval_list=['Coffee','Food', 'Gifts']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 2a.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step 2a.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 2a.4: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category', 'Step 2a.5: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 2a.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 2a.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 2a.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resobj.verify_riser_legends('MAINTABLE_wbody0', ['Unit Sales', 'Dollar Sales'], "Step 2a.9:")
#         expected_tooltip_list=['Category:Coffee', 'Unit Sales:1376266', 'Filter Chart', 'Exclude from Chart']
#         resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar", expected_tooltip_list, "Step 2a.10: Verify bar value")
        
        """
            Step 03 : Select Coffee and Food bars for chart filter via lasso feature.
        """
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 g rect[class*='riser!s0!g0!mbar']")
        utillobj.click_on_screen(elem1, 'middle', click_type=0)
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 g rect[class*='riser!s0!g0!mbar']")
        source_elem=utillobj.get_object_screen_coordinate(elem1, 'top_middle', move=True)   
        elem2=driver.find_element_by_css_selector("#MAINTABLE_wbody0 g rect[class*='riser!s1!g1!mbar']")
        target_elem=utillobj.get_object_screen_coordinate(elem2, 'top_middle', move=True)  
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x'],sy_offset=source_elem['y'],tx_offset=target_elem['x'],ty_offset=target_elem['y'])
        
        """
            Step 04 : Verify chart context menu appears on the screen with these options:
                        4 Points
                        Filter Chart
                        Exclude from Chart
        """
        resobj.select_or_verify_lasso_filter(verify=['4 points','Filter Chart','Exclude from Chart'],msg='Step 4.1 : Expect to see the left-click options appear')
        
        """
            Step 05 : Click Filter chart and verify Coffee and Food bars (for US and DS) are displayed.
                        Make sure remove filter icon is displayed in active tool bar.
        """
        resobj.select_or_verify_lasso_filter(select='Filter Chart')
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category", "Step 5.1: Verify -xAxis Title")
        expected_xval_list=['Coffee','Food']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 5.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 4, 'Step 5.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 5.4: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category', 'Step 5.5: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 5.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 5.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 5.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resobj.verify_riser_legends('MAINTABLE_wbody0', ['Unit Sales', 'Dollar Sales'], "Step 5.9:")
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 5.10: Filter Button Visible')
        
        """
        Step 06 : Hover over green bar of Coffee (DS) and verify context menu shows these details:
                    Category: Coffee
                    Dollar Sales: 17,231,455
                    Filter Chart
                    Exclude from Chart
                    Remove Filter
        """
        expected_tooltip_list=['Category:Coffee', 'Dollar Sales:17231455', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g0!mbar", expected_tooltip_list, "Step 6.1 : Verify bar value")
        
        """
            Step 07 : Click Exclude from chart on Coffee bar (DS)
        """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0","riser!s1!g0!mbar", 'Exclude from Chart')
        
        """
            Step 08 : Verify only Food bars for DS and US are displayed.
        """
        title_sync_css = "#MAINTABLE_wbody0 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_number_of_element(title_sync_css,1,45)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category", "Step 8.1: Verify -xAxis Title")
        expected_xval_list=['Food']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 8.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 2, 'Step 8.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 8.4: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category', 'Step 8.5: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 8.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 8.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 8.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resobj.verify_riser_legends('MAINTABLE_wbody0', ['Unit Sales', 'Dollar Sales'], "Step 8.9:")
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 8.10: Filter Button Visible')
        
        """
            Step 09 : Hover over blue bar of Food (US) and verify context menu shows these details:
                        Category: Food
                        Unit Sales: 1,384,845
                        Remove Filter
        """
        expected_tooltip_list=['Category:Food', 'Unit Sales:1384845', 'Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar", expected_tooltip_list, "Step 9.1 : Verify bar value")
        
        """
            Step 10 : Click Remove filter from the menu
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        
        """
            Step 11 : Verify Coffee, Food  and Gifts are displayed.
        """
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category", "Step 11.1: Verify -xAxis Title")
        expected_xval_list=['Coffee','Food', 'Gifts']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 11.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step 11.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 11.4: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category', 'Step 11.5: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resobj.verify_riser_legends('MAINTABLE_wbody0', ['Unit Sales', 'Dollar Sales'], "Step 11.9:")
        expected_tooltip_list=['Category:Coffee', 'Unit Sales:1376266', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar", expected_tooltip_list, "Step 11.10: Verify bar value")
        
        """
        Step 12 : Select Coffee and Food bars for chart filter via lasso feature and click filter.
        """
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 g rect[class*='riser!s0!g0!mbar']")
        utillobj.click_on_screen(elem1, 'middle', click_type=0)
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 g rect[class*='riser!s0!g0!mbar']")
        source_elem=utillobj.get_object_screen_coordinate(elem1, 'top_middle', move=True)   
        elem2=driver.find_element_by_css_selector("#MAINTABLE_wbody0 g rect[class*='riser!s1!g1!mbar']")
        target_elem=utillobj.get_object_screen_coordinate(elem2, 'top_middle', move=True)  
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x'],sy_offset=source_elem['y'],tx_offset=target_elem['x'],ty_offset=target_elem['y'])
        resobj.select_or_verify_lasso_filter(select='Filter Chart')
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category", "Step 12.1: Verify -xAxis Title")
        expected_xval_list=['Coffee','Food']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 12.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 4, 'Step 12.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 12.4: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category', 'Step 12.5: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 12.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 12.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 12.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resobj.verify_riser_legends('MAINTABLE_wbody0', ['Unit Sales', 'Dollar Sales'], "Step 12.9:")
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 12.10: Filter Button Visible')
        expected_tooltip_list=['Category:Coffee', 'Dollar Sales:17231455', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g0!mbar", expected_tooltip_list, "Step 12.11: Verify bar value")
        
        """
            Step 13 : Remove Filter icon from the active menu and verify chart is in original state.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category", "Step 13.1: Verify -xAxis Title")
        expected_xval_list=['Coffee','Food', 'Gifts']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 13.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step 13.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 13.4: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category', 'Step 13.5: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 13.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 13.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 13.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resobj.verify_riser_legends('MAINTABLE_wbody0', ['Unit Sales', 'Dollar Sales'], "Step 13.9:")
        expected_tooltip_list=['Category:Coffee', 'Unit Sales:1376266', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar", expected_tooltip_list, "Step 13.10: Verify bar value")
        utillobj.switch_to_default_content(pause=3)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step17', image_type='actual',x=1, y=1, w=-1, h=-1)
        

if __name__ == '__main__':
    unittest.main()      