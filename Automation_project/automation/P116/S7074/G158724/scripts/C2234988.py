'''
Created on JUN 23, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2234988
TestCase Name = Verify all PIE Chart options via Advanced chart tool bar - single Measure, single Dimension for Color only.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2234988_TestClass(BaseTestCase):

    def test_C2234988(self):
        
        Test_Case_ID="C2234988"
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        rollupobj =active_chart_rollup.Active_Chart_Rollup(driver)
        """
            Step 01: Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES.
            Select Active from the Home tab.
            From the Format tab select PIE.
            Add fields as follows:
            Product under Color
            Unit Sales, Dollar Sales under Measure
        """    
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(4)  
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1)
        ribbonobj.select_ribbon_item('Format', 'pie')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resobj._validate_page(elem1)  
        metadataobj.datatree_field_click('Product', 2, 0)
        parent_css="#TableChart_1 g.legend g text[class='legend-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Dollar Sales',2, 0)
        parent_css="#TableChart_1 g.chartPanel g text[class='pieLabel!g0!mpieLabel!']"
        resobj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        time.sleep(2)
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', ['Dollar Sales'], "Step 01.1:",custom_css="text[class*='pieLabel']",same_group=True) 
        expected_label_list=['Product', 'Capuccino', 'Espresso']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 01.2: Verify pie lablesList ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!", "bar_blue1", "Step 03.b: Verify first bar color")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, "Step 03.d: Verify number of pie segment", custom_css=".chartPanel g path[class*='riser!']")
        """
            Step 02: Click run. Hover over a PIE slice.
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Dollar Sales'], "Step 02.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 02.2: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", "bar_blue", "Step 02.3: Verify first bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales BY Product', 'Step 02.4: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.5: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 02.8: Verify number of pie", custom_css=".chartPanel g path[class*='riser!']")  
        time.sleep(2)  
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'start')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='riser!s0!g0!mwedge!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(3)
        expected_tooltip_list=['Product:Biscotti', 'Dollar Sales:5263317  (11.40%)', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", expected_tooltip_list, "Step 02.9: Verify bar value", default_move=True)
        """
            Step 03:From the second icon on the chart, Advanced Chart, select 
            PIE with Depth.
            Click OK.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'piewithdepth')
        time.sleep(3)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Dollar Sales'], "Step 03.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 03.2: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", "bar_blue", "Step 03.3: Verify first bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales BY Product', 'Step 03.4:Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.5: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 52, "Step 03.8: Verify number of pie", custom_css=".chartPanel g path[class*='riser!']")
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'start')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='riser!s0!g0!mwedge!']")
        utillobj.click_on_screen(parent_obj,'top_middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(3)
        expected_tooltip_list=['Product:Biscotti', 'Dollar Sales:5263317  (11.40%)', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", expected_tooltip_list, "Step 03.9: Verify bar value", default_move=True)
        """
            Step 04:Click the third icon, Original Chart.
            Click the Advanced Chart tab again and select
            Donut (Cylinder).
            Click OK.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'dountcylinder')
        time.sleep(3)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Dollar Sales'], "Step 04.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 04.2: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", "bar_blue", "Step 04.3: Verify first bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales BY Product', 'Step 04.4:Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.5: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 20, "Step 04.8: Verify number of pie", custom_css=".chartPanel g path[class*='riser!']")
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['46.2M'], "Step 04.9:",custom_css="text[class^='totalLabel!g']",same_group=True) 
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'start')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='riser!s0!g0!mwedge!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(3)
        expected_tooltip_list=['Product:Biscotti', 'Dollar Sales:5263317  (11.40%)', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", expected_tooltip_list, "Step 04.10: Verify bar value", default_move=True)
         
        """
            Step 05:Click the third icon, Original Chart.
            Click the Advanced Chart tab again and select
            Donut with Depth.
            Click OK.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'dountwithDepth')
        time.sleep(3)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Dollar Sales'], "Step 05.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 05.2: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", "bar_blue", "Step 05.3: Verify first bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales BY Product', 'Step 05.4:Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.5: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 64, "Step 05.8: Verify number of pie", custom_css=".chartPanel g path[class*='riser!']")
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['46.2M'], "Step 05.9:",custom_css="text[class^='totalLabel!g']",same_group=True) 
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'start')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='riser!s0!g0!mwedge!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(3)
        expected_tooltip_list=['Product:Biscotti', 'Dollar Sales:5263317  (11.40%)', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", expected_tooltip_list, "Step 05.10: Verify bar value", default_move=True)
         
        """
            Step 06:Click the third icon, Original Chart.
            Click the Advanced Chart tab again and select
            Donut (Bevel)
            Click OK.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'donutbevel')
        time.sleep(3)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Dollar Sales'], "Step 06.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 06.2: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", "bar_blue", "Step 06.3: Verify first bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales BY Product', 'Step 06.4:Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.5: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 06.8: Verify number of pie", custom_css=".chartPanel g path[class*='riser!']")
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['46.2M'], "Step 06.9:",custom_css="text[class^='totalLabel!g']",same_group=True) 
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'start')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='riser!s0!g0!mwedge!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(3)
        expected_tooltip_list=['Product:Biscotti', 'Dollar Sales:5263317  (11.40%)', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", expected_tooltip_list, "Step 06.10: Verify bar value", default_move=True)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step6', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()          