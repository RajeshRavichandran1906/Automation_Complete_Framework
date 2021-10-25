'''
Created on July 03, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204921
TestCase Name =Verify that Chart displayed with Linear Trendline.

'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon
from common.lib import utillity


class C2204921_TestClass(BaseTestCase):

    def test_C2204921(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID="C2204921"
        driver = self.driver
        
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Open IA and create a new chart using the GGSALES file.
        Select Active Report as the output format.
        Add Product to the Horizontal axis.
        Add Unit Sales to the Vertical axis.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1 svg g.risers >g>rect[class^='riser']", 25, 65)
        
        ribbonobj.change_output_format_type('active_report')
        time.sleep(4)
        metadataobj.datatree_field_click('Product', 1, 1, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(parent_css,"Product", 15)
        
        metadataobj.datatree_field_click('Unit Sales', 1, 1,'Add To Query','Vertical Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(parent_css,"Unit Sales", 15)
        
        result_obj.verify_xaxis_title("TableChart_1",'Product', "Step 01.1:a Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 01.1:b Verify Y-Axis Title")
        expected_xval_list=['Capuccino','Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 01.2 :')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 01.3 : Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 01.3: Verify bar color")
         
        """
        Step 02: Right click on any bar and select "Add Trendline".
        Expect to see the following Trendline menu  
        """
#         obj_locator1=driver.find_element_by_css_selector("#TableChart_1 [class*='riser!s0!g1!mbar!']")
#         utillobj.default_click(obj_locator1, click_option=1)
        
        obj_locator=driver.find_element_by_css_selector("#TableChart_1 [class*='riser!s0!g0!mbar!']")
                 
        utillobj.click_on_screen(obj_locator, 'middle', click_type=0)
        time.sleep(2)
        utillobj.click_on_screen(obj_locator, 'middle', click_type=1)
        time.sleep(2)
        popup_list1=['Filter Values...', 'Sort', 'Visibility', 'Change Title...', 'Series Type', 'Series Color...', 'More Style Options...', 'Data Labels', 'Color Mode', 'Add Trendline', 'Edit Format', 'Drill Down', 'More', 'Delete']
        utillobj.select_or_verify_bipop_menu('Add Trendline',verify=True,expected_popup_list=popup_list1,msg='Step 02.1 : ')
        time.sleep(2)
        
        """
        Step 03: Select Linear as the Trend Line option.
        Click the Run button.      
        """
        popup_list2=['None', 'Linear', 'Quadratic', 'Polynomial', 'Hyperbolic', 'Logarithmic', 'Modified Hyperbolic', 'Rational', 'Exponential', 'Modified Exponential', 'Log Quadratic', 'Geometric']
        utillobj.select_or_verify_bipop_menu('Linear',verify=True,expected_popup_list=popup_list2,msg='Step 03.1 : ')
        parent_css="#TableChart_1 path[class='series!s0!g0!mtrendline!']"
        result_obj.wait_for_property(parent_css, 1)
        result_obj.verify_xaxis_title("TableChart_1",'Product', "Step 03.3:a Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 03.4:b Verify Y-Axis Title")
        expected_xval_list=['Capuccino','Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 03.5 :')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 03.6 : Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 03.7: Verify bar color") 
        utillobj.verify_chart_color("TableChart_1",None, "bar_blue1", "Step 03.8: Verify Trend Linear Line color",custom_css="path[class='series!s0!g0!mtrendline!']",attribute_type='stroke') 
        total_liner_lines=len(self.driver.find_elements_by_css_selector("#TableChart_1 path[class*='series!']"))
        utillobj.asequal(1,total_liner_lines,'Step 03.9 : Verify no of Trend Linear Lines')
        """
        Click the Run button.      
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 40)
        
        utillobj.switch_to_frame(pause=2)
        
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 10)
        
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Product", "Step 03:9a Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","Unit Sales", "Step 03:9b Verify Y-Axis Title")
        expected_xval_list=['Biscotti','Capuccino','Coffee Grinder','Coffee Pot','Croissant','Espresso','Latte','Mug','Scone','Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03.10: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 03.11: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", 'bar_blue', 'Step 003.12: Verify bar Color')
        utillobj.verify_chart_color("MAINTABLE_wbody0",None, "bar_blue", "Step 03.13: Verify Trend Linear Line color",custom_css="path[class='series!s0!g0!mtrendline!']",attribute_type='stroke')
        total_liner_lines=len(self.driver.find_elements_by_css_selector("#MAINTABLE_wbody0 path[class*='series!']"))
        utillobj.asequal(1,total_liner_lines,'Step 03.13a : Verify no of Trend Linear Lines')
        expected_tooltip_list=['Product:Croissant', 'Unit Sales:630054', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g4!mbar!', expected_tooltip_list, 'Step 03.14: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Product', 'Step 03.15: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.16: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.17: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.18: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        
        """
        Save Report      
        """
        parent_css="#applicationButton img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2204921_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()