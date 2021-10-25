'''
Created on JUN 08, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2234950
TestCase Name = Verify all Bar options via Advanced chart tool.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,active_chart_rollup
from common.lib import utillity

class C2234950_TestClass(BaseTestCase):

    def test_C2234950(self):
        
        Test_Case_ID="C2234950"
        """
            TESTCASE VARIABLES
        """
        driver = self.driver#Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
               
        """
            Step 01:Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES.
            Select Format Active Report and run the chart.
            Add fields as follows: Category under Columns, Product under Horizontal axis, Unit Sales, Dollar Sales under Vertical axis.
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)  
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        metadataobj.datatree_field_click('Category', 1, 0, 'Add To Query', 'Columns')
        parent_css="#TableChart_1 g.chartPanel g text[class='colHeader-label!']"
        resobj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Product', 1, 0, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='colHeader-label!']"
        resobj.wait_for_property(parent_css, 1, string_value='Category : Product', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 1, 0, 'Add To Query', 'Vertical Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        resobj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Dollar Sales', 1, 0, 'Add To Query', 'Vertical Axis')
        parent_css="#TableChart_1 g.legend g text[class='legend-labels!s1!']"
        resobj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        time.sleep(2)   
        resobj.verify_xaxis_title("TableChart_1", "Category : Product", "Step 01.1: Verify -xAxis Title",custom_css="text[class='colHeader-label!']")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M','3M', '3.5M', '4M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 01.2: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step 01.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 01.4: Verify  bar color")
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.5:")
        resobj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Category', ['Coffee'], "Step 01.6: Verify row header and value")
        """
            Step 02:Click Run.
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 02.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 02.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 02.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 02.4: Verify  bar color")
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.5:")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee', 'Food', 'Gifts'], "Step 02.6: Verify row header and value")
        time.sleep(2)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 02.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g6!mbar!r0!c0!", expected_tooltip_list, "Step 02.11: Verify bar value")
          
        """
            Step 03:Select Advance Chart icon from the tool bar.
            Click the Column option.Click Ok.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'column')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 03.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 03.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 03.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 03.4: Verify  bar color")
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 03.5:")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee', 'Food', 'Gifts'], "Step 03.6: Verify row header and value")
        time.sleep(2)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 03.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g6!mbar!r0!c0!", expected_tooltip_list, "Step 03.11: Verify bar value")
        """
            Step 04:Again select Advance Chart icon from the tool bar.
            Select the Stacked Column option.Click Ok.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'stackedcolumn')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 04.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '3M', '6M', '9M', '12M','15M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 04.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 04.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 04.4: Verify  bar color")
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.5:")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee', 'Food', 'Gifts'], "Step 04.6: Verify row header and value")
        time.sleep(2)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 04.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g6!mbar!r0!c0!", expected_tooltip_list, "Step 04.11: Verify bar value")
        """
            Step 05:Again select Advance Chart icon from the tool bar.
            Select the Percent Column option.Click Ok.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'percentcolumn')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 05.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 05.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 05.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 05.4: Verify  bar color")
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.5:")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee', 'Food', 'Gifts'], "Step 05.6: Verify row header and value")
        time.sleep(2)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 05.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g6!mbar!r0!c0!", expected_tooltip_list, "Step 05.11: Verify bar value")
        """
            Step 06:Again select Advance Chart icon from the tool bar.
            Select the Column Depth option.Click Ok.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'columndepth')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 06.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 06.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 06.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 06.4: Verify  bar color")
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 06.5: ")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee', 'Food', 'Gifts'], "Step 06.6: Verify row header and value")
        time.sleep(2)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 06.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g6!mbar!r0!c0!", expected_tooltip_list, "Step 06.11: Verify bar value")
        """
        Step 07:Again select Advance Chart icon from the tool bar.
        Select the Stacked Depth option.Click Ok.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'stackeddepth')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 07.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '3M', '6M', '9M', '12M','15M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 07.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 07.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 07.4: Verify  bar color")
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 07.5: ")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee', 'Food', 'Gifts'], "Step 07.6: Verify row header and value")
        time.sleep(2)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 07.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g6!mbar!r0!c0!", expected_tooltip_list, "Step 07.11: Verify bar value")
        """
        Step 08:Again select Advance Chart icon from the tool bar.
        Select the Percent Depth option.Click Ok.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'percentdepth')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 08.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 08.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 08.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 08.4: Verify  bar color")
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 08.5:")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee', 'Food', 'Gifts'], "Step 08.6: Verify row header and value")
        time.sleep(2)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 08.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g6!mbar!r0!c0!", expected_tooltip_list, "Step 08.11: Verify bar value")
        """
        Step 09:Close Run window 
        From query pane change category from Columns to Rows and click run.
        Now click Chart Rollup tool from Active Chart toolbar.
        Select Horizontal Bar chart and click Ok.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        elem1=driver.find_element_by_css_selector("#queryTreeWindow table tr:nth-child(5) td")
        utillobj.click_on_screen(elem1, 'middle', click_type=0)
        time.sleep(6)   
        srcobj=driver.find_element_by_css_selector("#queryTreeWindow table tr:nth-child(5) td img.icon")
        trgobj=driver.find_element_by_css_selector("#queryTreeWindow table tr:nth-child(3) td img.icon")
        utillobj.drag_drop_using_uisoup(srcobj, trgobj)
        time.sleep(3)
#         browser=utillobj.parseinitfile('browser')
#         if browser == 'Firefox':
        elem1=driver.find_element_by_css_selector("#queryTreeWindow table tr:nth-child(3) td img.icon")
        utillobj.click_on_screen(elem1, 'middle', click_type=0)
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'bar')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 09.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 09.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 09.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 09.4: Verify  bar color")
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 09.5:")
        time.sleep(3)
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'Rows', "CategoryProduct", ['Coffee', 'Food', 'Gifts'], "Step 09.6: Verify row header and value")
        time.sleep(2)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 09.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g6!mbar!r0!c0!", expected_tooltip_list, "Step 09.11: Verify bar value")
#          
        """
            Step 10:Again select Advance Chart icon from the tool bar. Select the second Horizontal option, Stacked Bar.Click Ok.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'stackedbar')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 10.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '3M', '6M', '9M', '12M','15M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 10.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 10.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 10.4: Verify  bar color")
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 10.5:")
        time.sleep(3)
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'Rows', "CategoryProduct", ['Coffee', 'Food', 'Gifts'], "Step 10.6: Verify row header and value")
        time.sleep(2)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 10.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g6!mbar!r0!c0!", expected_tooltip_list, "Step 10.11: Verify bar value")
         
        """
            Step 11:Again select Advance Chart icon from the tool bar. Select the third Horizontal option, Percent Bar.Click Ok
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'percentbar')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 11.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 11.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 11.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 11.4: Verify  bar color")
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 11.5:")
        time.sleep(3)
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'Rows', "CategoryProduct", ['Coffee', 'Food', 'Gifts'], "Step 11.6: Verify row header and value")
        time.sleep(2)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 11.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g6!mbar!r0!c0!", expected_tooltip_list, "Step 11.11: Verify bar value")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
     
if __name__ == '__main__':
    unittest.main()
      
        