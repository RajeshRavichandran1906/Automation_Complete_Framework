'''
Created on MAY 23, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2205170
TestCase Name = Verify a chart shows correct filtered output once filter via lasso applied - Pie Chart
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2205170_TestClass(BaseTestCase):

    def test_C2205170(self):
        
        Test_Case_ID="C2205170"
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
#         utillobj.infoassist_api_edit('test','idis','S7074',mrid='mrid',mrpass='mrpass')  
#         time.sleep(40)
        """
            Step 01: Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES
        """    
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        time.sleep(6)  
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
        metadataobj.datatree_field_click('Product', 1, 0, 'Add To Query', 'Color')
        parent_css="#TableChart_1 g.legend g text[class='legend-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 1, 0, 'Add To Query', 'Measure')
        parent_css="#TableChart_1 g.chartPanel g.scrollCharts g text[class='pieLabel!g0!mpieLabel!']"
        resobj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        time.sleep(4)
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', ['Unit Sales'], "Step 03.a:")
        expected_label_list=['Product', 'Capuccino', 'Espresso']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 03.b: Verify pie lablesList ')
        time.sleep(2)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!r0!c0!", "bar_blue1", "Step 03.c: Verify first bar color")
        resobj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Category', ['Coffee'], "Step 03.d: Verify row header and value")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, "Step 03.e: Verify number of pie segment", custom_css=".chartPanel .scrollCharts path[class*='riser!']")
        """
            Step 04:Run the report    
  
        """     
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales', 'Unit Sales', 'Unit Sales'], "Step 04.a:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 04.b: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c1!", "bar_blue", "Step 04.c Verify first bar color")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 04.d: Verify row header")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 04.e(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.e(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.e(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.e(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 04.f: Verify number of pie", custom_css=".chartPanel .scrollCharts path[class*='riser!']")     
        """
            Step 05:Left-click and drag a box around the Mug and Thermos pie slices, in the Gifts Category.
            Step 06:Click Filter Chart option.
        """ 
        time.sleep(5)
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 .chartPanel .scrollCharts g path[class='riser!s7!g0!mwedge!r0!c2!']")
        utillobj.click_on_screen(elem1, 'middle', click_type=0)
        time.sleep(6)   
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 .chartPanel .scrollCharts g path[class='riser!s7!g0!mwedge!r0!c2!']")
        source_elem=utillobj.get_object_screen_coordinate(elem1, 'middle', move=True)   
        elem2=driver.find_element_by_css_selector("#MAINTABLE_wbody0 .chartPanel .scrollCharts g path[class='riser!s9!g0!mwedge!r0!c2!']")
        target_elem=utillobj.get_object_screen_coordinate(elem2, 'middle', move=True)  
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x'],sy_offset=source_elem['y'],tx_offset=target_elem['x'],ty_offset=target_elem['y'])
        time.sleep(3)
        resobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(2)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales'], "Step 06.a:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product', 'Mug', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 06:b: Verify pie lablesList ')
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Gifts'], "Step 06.c: Verify row header")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c0!", "bar_blue", "Step 06.d: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 06.e(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.e(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.e(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.e(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 06.e(v): Filter Button Visible')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, "Step 06.f: Verify number of pie",custom_css=".chartPanel .scrollCharts path[class*='riser!']")
     
        """
            Step 07:Hover over the Mug pie slice.
        """ 
        time.sleep(3)
        expected_tooltip_list=['Category:Gifts', 'Product:Mug', 'Unit Sales:360570  (65.48%)', 'Filter Chart', 'Exclude from Chart','Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c0!", expected_tooltip_list, "Step 07: Verify bar value")
        time.sleep(5)
         
        """
            Step 08:Click Remove Filter option.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        time.sleep(3)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 08.a(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.a(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.a(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.e(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 08.a(v) Filter Button Removed')
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales', 'Unit Sales', 'Unit Sales'], "Step 08.b",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product','Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 08.c: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c1!", "bar_blue", "Step 08.d: Verify first bar color")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 08.e: Verify row header")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 08.f: Verify number of pie",custom_css=".chartPanel .scrollCharts path[class*='riser!']")
        
        """
            Step 09:Left-click and drag a box around the Mug and Coffee Pot pie slices in the Coffee PIE chart.
            Step 10:Click Exclude from Chart option.
        """
        time.sleep(5)
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 .chartPanel .scrollCharts g path[class='riser!s7!g0!mwedge!r0!c2!']")
        utillobj.click_on_screen(elem1, 'middle', click_type=0)
        time.sleep(6)   
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 .chartPanel .scrollCharts g path[class='riser!s7!g0!mwedge!r0!c2!']")
        source_elem=utillobj.get_object_screen_coordinate(elem1, 'middle', move=True)   
        elem2=driver.find_element_by_css_selector("#MAINTABLE_wbody0 .chartPanel .scrollCharts g path[class='riser!s3!g0!mwedge!r0!c2!']")
        target_elem=utillobj.get_object_screen_coordinate(elem2, 'middle', move=True)  
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x'],sy_offset=source_elem['y'],tx_offset=target_elem['x'],ty_offset=target_elem['y'])
        time.sleep(3)
        resobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        time.sleep(5)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Croissant', 'Espresso', 'Latte', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 10.a: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c1!", "bar_blue", "Step 10.b: Verify first bar color")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 10.c: Verify row header")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 10.d(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.d(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.d(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.e(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 10.d(v): Filter Button Visible')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 8, "Step 10.e: Verify number of pie",custom_css=".chartPanel .scrollCharts path[class*='riser!']")
             
        """
            Step 11: Click remove filter icon from the active tool bar.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        time.sleep(3)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 11.a(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.a(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.a(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.e(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 11.a(v): Filter Button Removed')
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales', 'Unit Sales', 'Unit Sales'], "Step 11.b",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product','Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 11.c: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c1!", "bar_blue", "Step 11.d: Verify first bar color")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 11.e: Verify row header")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 11.f: Verify number of pie",custom_css=".chartPanel .scrollCharts path[class*='riser!']")
        
        """
            Step 12:Left-click and drag a box around the Croissant slice in FOOD and the Mug slice in GIFTS.
            This will span two categories.
            Step 13:Click Exclude from the Chart option.
        """
        time.sleep(5)
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 .chartPanel .scrollCharts g path[class='riser!s4!g0!mwedge!r0!c1!']")
        utillobj.click_on_screen(elem1, 'middle', click_type=0)
        time.sleep(6)   
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 .chartPanel .scrollCharts g path[class='riser!s4!g0!mwedge!r0!c1!']")
        source_elem=utillobj.get_object_screen_coordinate(elem1, 'middle', move=True)   
        elem2=driver.find_element_by_css_selector("#MAINTABLE_wbody0 .chartPanel .scrollCharts g path[class='riser!s7!g0!mwedge!r0!c2!']")
        target_elem=utillobj.get_object_screen_coordinate(elem2, 'middle', move=True)  
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x'],sy_offset=source_elem['y'],tx_offset=target_elem['x'],ty_offset=target_elem['y'])
        time.sleep(3)
        resobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        time.sleep(5)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Espresso', 'Latte', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 13.a: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r0!c1!", "bar_blue", "Step 13.b: Verify first bar color")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 13.c: Verify row header")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 13.d(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 13.d(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 13.d(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 13.e(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 13.d(v): Filter Button Visible')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 8, "Step 13.e: Verify number of pie",custom_css=".chartPanel .scrollCharts path[class*='riser!']")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
