'''
Created on JUN 19, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2234947
TestCase Name = Verify Scatter Chart in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea
from common.lib import utillity
from selenium.webdriver.common.by import By
from uisoup import uisoup

class C2234947_TestClass(BaseTestCase):

    def test_C2234947(self):
        
        Test_Case_ID="C2234947"
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
        
        """
            Step 01:Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES.
            From Home tab Select Active Report as Output file format.
            From Select a chart pop up choose 'Scatter' and click Ok.
        """  
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(4)  
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1)
        ribbonobj.select_ribbon_item('Format', 'Scatter')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resobj._validate_page(elem1)
        """
            Steps 02:Select Unit Sales for the Vertical axis. Select Category for the Horizontal axis. Select product for the Detail. Click Run.
        """
        metadataobj.datatree_field_click('Unit Sales', 1, 0, 'Add To Query', 'Vertical Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        resobj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Category', 1, 0, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Product', 1, 0, 'Add To Query', 'Detail')
        parent_css="#queryTreeWindow  table tr:nth-child(13) td"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 02.1: Verify -yAxis Title")
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category", "Step 02.2: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Coffee','Food', 'Gifts']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 02.3: Verify XY labels")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g4!mmarker!', 'bar_blue', 'Step 02.4: Verify Color',attribute_type='stroke')
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 02.5: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 02.9: Verify number of Scatter", custom_css="g [class*= 'marker'] circle")
        
        """
            Step 03:Hover over the point in the lower left, just above Coffee.
        """ 
        expected_tooltip_list=['Category:Coffee',  'Unit Sales:189217', 'Product:Capuccino', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mmarker!", expected_tooltip_list, "Step 03: Verify bar value")
        time.sleep(3)
        """
            Step 04:Switch Category and Product fields. Click Run.
        """
        utillobj.switch_to_default_content(pause=3)
        elem1=driver.find_element_by_css_selector("#queryTreeWindow table tr:nth-child(13) td")
        utillobj.click_on_screen(elem1, 'middle', click_type=0)
        time.sleep(6)   
        srcobj=driver.find_element_by_css_selector("#queryTreeWindow table tr:nth-child(13) td img.icon")
        trgobj=driver.find_element_by_css_selector("#queryTreeWindow table tr:nth-child(8) td img.icon")
        utillobj.drag_drop_using_uisoup(srcobj, trgobj)
        time.sleep(3)
#         browser=utillobj.parseinitfile('browser')
#         if browser == 'Firefox':
        elem1=driver.find_element_by_css_selector("#queryTreeWindow table tr:nth-child(8) td img.icon")
        utillobj.click_on_screen(elem1, 'middle', click_type=0)
#         target_obj=utillobj.get_object_screen_coordinate(trgobj, 'middle')
#         target_obj_x=target_obj['x']
#         target_obj_y=target_obj['y']
#         mouse_obj=uisoup.mouse
#         mouse_obj.click(target_obj_x,target_obj_y)
        time.sleep(10)
        metadataobj.datatree_field_click('Category', 1, 0, 'Add To Query', 'Detail')
        parent_css="#queryTreeWindow  table tr:nth-child(13)"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 04.1: Verify -yAxis Title")
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 04.2: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 04.3: Verify XY labels")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g4!mmarker!', 'bar_blue', 'Step 04.4: Verify Color',attribute_type='stroke')
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Product, Category', 'Step 04.5: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 04.9: Verify number of Scatter", custom_css="g [class*= 'marker'] circle")
         
        """
            Step 05:Hover over the point above Capuccino.
        """ 
        expected_tooltip_list=['Product:Capuccino', 'Unit Sales:189217', 'Category:Coffee', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g1!mmarker!", expected_tooltip_list, "Step 05: Verify bar value")
        time.sleep(6)
        utillobj.switch_to_default_content(pause=5)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step5', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()          
    