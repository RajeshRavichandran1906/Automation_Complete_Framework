'''
Created on MAY 16, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2205165
TestCase Name = Verify a chart shows correct filtered output once filter applied from context menu - Pie Chart
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2205165_TestClass(BaseTestCase):

    def test_C2205165(self):
        
        Test_Case_ID="C2205165"
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(driver)
        resobj=visualization_resultarea.Visualization_Resultarea(driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(driver)
        """
            Step 01: Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES
        """    
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        time.sleep(4)  
        """
            Step 02: On the Format tab, in the Output Types group, click active report/Active Flash/Active PDF
            From the Format Tab select the PIE chart option.
        """   
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        ribbonobj.select_ribbon_item('Format', 'Pie')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resobj._validate_page(elem1)
        """
            Step 03: Select data from the left pane (Dimensions and Measures)
            Category - Columns
            Product - Color
            Unit Sales - Measures
        """  
        metadataobj.datatree_field_click('Category', 1, 0, 'Add To Query', 'Columns')
        parent_css="#TableChart_1 g.chartPanel g text[class='colHeader-label!']"
        resobj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Product', 2, 0)
        parent_css="#TableChart_1 g.legend g text[class='legend-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 2, 0)
        parent_css="#TableChart_1 g.chartPanel g.scrollCharts g text[class='pieLabel!g0!mpieLabel!']"
        resobj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        time.sleep(3)
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', ['Unit Sales'], "Step 03:")
        expected_label_list=['Product', 'Capuccino', 'Espresso']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 03.a: Verify pie lablesList ')
        time.sleep(2)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!r0!c0!", "bar_blue1", "Step 03.b: Verify first bar color")
        resobj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Category', ['Coffee'], "Step 03.c: Verify row header and value")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, "Step 03.d: Verify number of pie segment", custom_css=".chartPanel .scrollCharts path[class*='riser!']")
        """
            Step 04:Run the report    

        """     
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales', 'Unit Sales', 'Unit Sales'], "Step 04.a:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 04.b: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c1!", "bar_blue", "Step 04.c Verify first bar color")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 04.d: Verify row header")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 04.e(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.e(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.e(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.e(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 04.f: Verify number of pie", custom_css=".chartPanel .scrollCharts path[class*='riser!']")     
        """
            Step 05:Hover over on Capuccino pie slice. Verify context menu displays:
            Category: Coffee
            Product: Capuccino
            Unit Sales: 189,217
            Filter Chart
            Exclude from Chart
        """ 
        expected_tooltip_list=['Category:Coffee', 'Product:Capuccino', 'Unit Sales:189217  (13.75%)', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g0!mwedge!r0!c0!", expected_tooltip_list, "Step 05: Verify bar value")
        parent_element_obj=self.driver.find_element_by_id('MAINTABLE_wbody0')
        utillobj.click_on_screen(parent_element_obj, 'top_middle')
        time.sleep(5)
        
        """
            Step 06: Click Filter Chart option.
            Verify based on 'Capuccino' product selection, one pie is displayed as filtered value.
            Filet icon is also displayed in the active tool bar.
        """ 
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0", "riser!s1!g0!mwedge!r0!c0!", 'Filter Chart')
        time.sleep(3)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales'], "Step 06.a:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product', 'Capuccino']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 06:b: Verify pie lablesList ')
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee'], "Step 06.c: Verify row header")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c0!", "bar_blue", "Step 06.d: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 06.e(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.e(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.e(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.e(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 06.e(v): Filter Button Visible')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 1, "Step 06.f: Verify number of pie",custom_css=".chartPanel .scrollCharts path[class*='riser!']")
        """
            Step 07 :Click on Capucciono pie. Verify context menu displays:
            Category: Coffee
            Product: Capuccino
            Unit Sales: 189,217
            Remove Filter
        """
        expected_tooltip_list=['Category:Coffee', 'Product:Capuccino', 'Unit Sales:189217  (100.00%)', 'Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c0!", expected_tooltip_list,"Step 07: Verify Chart tooltip ")
        time.sleep(5)
        """
            Step 08: Click Remove Filter option.
            Verify original chart appears in the output. 
            Make sure filter icon is not present.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        time.sleep(3)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 08.a(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.a(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.a(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.a(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 08.a(v): Filter Button Removed')
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales', 'Unit Sales', 'Unit Sales'], "Step 08.b",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product','Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 08.c: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c1!", "bar_blue", "Step 08.d: Verify first bar color")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 08.e: Verify row header")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 08.f: Verify number of pie",custom_css=".chartPanel .scrollCharts path[class*='riser!']")
        """ Step 09: Hover over on Biscotti bar. Verify context menu displays
            Category: Food
            Product: Biscotti
            Unit Sales: 421,377
            Filter Chart
            Exclude from Chart
        """
        expected_tooltip_list=['Category:Food', 'Product:Biscotti', 'Unit Sales:421377  (30.43%)', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c1!", expected_tooltip_list, "Step 09: Verify bar value")
        parent_element_obj=self.driver.find_element_by_id('MAINTABLE_wbody0')
        utillobj.click_on_screen(parent_element_obj, 'top_middle')
        time.sleep(5)
        
        """ Step 10:
            Click Exclude from Chart option.
            Verify the Biscotti slice has been removed from the FOOD category and the filter icon appears on the Active tool bar.
        """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c1!", 'Exclude from Chart')
        time.sleep(3)
        expected_label_list=['Product', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 10.a: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c0!", "bar_blue", "Step 10.b: Verify first bar color")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 10.c: Verify row header")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 10.d(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.d(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.d(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.d(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 10.d(v): Filter Button Visible')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 9, "Step 10.e: Verify number of pie",custom_css=".chartPanel .scrollCharts path[class*='riser!']")  
        """ Step 11:Click remove filter icon from the active tool bar.
            Verify original chart appears with FOOD category and 'Remove filter' is not present.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        time.sleep(3)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 11.a(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.a(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.a(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.a(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 11.a(v): Filter Button Removed')
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales', 'Unit Sales', 'Unit Sales'], "Step 11.b:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 11.c Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c1!", "bar_blue", "Step 11.d Verify first bar color")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 11.e Verify row header")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 11.f: Verify number of pie",custom_css=".chartPanel .scrollCharts path[class*='riser!']")
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