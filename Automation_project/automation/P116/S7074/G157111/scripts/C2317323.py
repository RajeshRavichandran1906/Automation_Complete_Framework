'''
Created on August 03, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2317323
TestCase Name =Verify that Bar Chart may be displayed by Series or by Group.

'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon
from common.lib import utillity


class C2317323_TestClass(BaseTestCase):

    def test_C2317323(self):
       
        
        """
        TESTCASE VARIABLES
        """
        TestCase_ID="C2317323"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01 : Open IA and create a new chart using the GGSALES file.
        Select Active Report as the output type.
        Add Unit Sales & Dollar Sales to the Vertical axis.
        Add Category & Product ID to the Horizontal axis.
        """
        
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(5)
        
        metadataobj.datatree_field_click('Unit Sales', 1, 1,'Add To Query','Vertical Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="Unit Sales")
        
        metadataobj.datatree_field_click('Dollar Sales', 1, 1,'Add To Query','Vertical Axis')
        parent_css="#TableChart_1 .legend text"
        result_obj.wait_for_property(parent_css, 2)
        time.sleep(2)
        
        metadataobj.datatree_field_click('Category', 1, 1, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="Category")
        
        metadataobj.datatree_field_click('Product ID', 1, 1, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="Category : Product ID")
        
        """
        01.1 : Expect to see the following Active Bar Preview pane.
        """
        result_obj.verify_xaxis_title("TableChart_1",'Category : Product ID', "Step 01.1 : Verify X-Axis Title")
        expected_xval_list=['Coffee : C141','Coffee : C144']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 01.2 :')
        result_obj.verify_number_of_riser('TableChart_1', 1, 4, 'Step 01.3 : Verify number of risers')
        result_obj.verify_riser_legends('TableChart_1',['Unit Sales','Dollar Sales'], 'Step 01.4: Verify chart legends lablesList')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 01.5 : Verify bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "bar_green", "Step 01.6 : Verify bar color")
        
        """
        Step 02 : Right click on any bar in the query panel and select Color Mode.
        Expect to see the Color Mode - by Series. 
        Jira Ticket - ACT-1275 ( By Series option not selected by default)
        """
        obj_locator=driver.find_element_by_css_selector("#TableChart_1 [class*='riser!s1!g0!mbar!']")
        utillobj.click_on_screen(obj_locator, 'middle', click_type=0)
        time.sleep(3)
        utillobj.click_on_screen(obj_locator, 'middle', click_type=1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Color Mode')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu(verify=True,expected_popup_list=['By Series','By Group'],msg='Step 02.1 : Expect to see the Color Mode - by Series')
        
        """
        Step 03 : Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(8)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css,20)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product ID', 'Step 03.1 : Verify Chart Title')
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Category : Product ID", "Step 03.2 : Verify X-Axis Title")
        result_obj.verify_riser_legends('MAINTABLE_wbody0',['Unit Sales','Dollar Sales'], 'Step 03.3: Verify chart legends lablesList')
        expected_xval_list=['Coffee : C141','Coffee : C142','Coffee : C144','Food : F101','Food : F102','Food : F103','Gifts : G100','Gifts : G104','Gifts : G110','Gifts : G121']
        expected_yval_list=['0', '2M', '4M', '6M', '8M','10M','12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03.4 : ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 03.5 : Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!", 'bar_blue1', 'Step 03.6 : Verify bar Color')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g1!mbar!", 'pale_green', 'Step 03.7 : Verify bar Color')
        expected_tooltip_list1=['Category:Coffee', 'Product ID:C142', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        expected_tooltip_list2=['Category:Coffee', 'Product ID:C142', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g1!mbar!', expected_tooltip_list1, 'Step 02.6 : verify the default tooltip values')
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g1!mbar!', expected_tooltip_list2,'Step 02.6 : verify the default tooltip values')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.8 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,TestCase_ID+'_Actual_Step_03', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 04 : Right click on any bar in the query panel and select Color Mode.Change the Color Mode to - by Group.
        """
        result_obj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        time.sleep(2)
        obj_locator=driver.find_element_by_css_selector("#TableChart_1 [class*='riser!s1!g0!mbar!']")
        utillobj.click_on_screen(obj_locator, 'middle', click_type=0)
        utillobj.click_on_screen(obj_locator, 'middle', click_type=1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Color Mode')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('By Group')
        
        """
        Step 04.1 : Expect to see the following Preview pane displaying the Color Mode - by Group.Each set of bars for Category/Product ID should be the same color.
        """
        result_obj.verify_xaxis_title("TableChart_1",'Category : Product ID', "Step 04.1 : Verify X-Axis Title")
        expected_xval_list=['Coffee : C141','Coffee : C144']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M','4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 04.2 :')
        result_obj.verify_number_of_riser('TableChart_1', 1, 4, 'Step 01.3 : Verify number of risers')
        result_obj.verify_riser_legends('TableChart_1',['Unit Sales','Dollar Sales'], 'Step 04.4: Verify chart legends lablesList')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 04.5 : Verify bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "bar_blue1", "Step 04.6 : Verify bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_green", "Step 04.7: Verify bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g1!mbar!", "bar_green", "Step 04.8 : Verify bar color")
        
        """
        Step 05 : Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(8)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css,20)
        
        """
        Step 05.1 : Expect to see the following Bar Chart, now displaying different colors for each set of bars.
        """
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product ID', 'Step 05.1 : Verify Chart Title')
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Category : Product ID", "Step 05.2 : Verify X-Axis Title")
        result_obj.verify_riser_legends('MAINTABLE_wbody0',['Unit Sales','Dollar Sales'], 'Step 03.3: Verify chart legends lablesList')
        expected_xval_list=['Coffee : C141','Coffee : C142','Coffee : C144','Food : F101','Food : F102','Food : F103','Gifts : G100','Gifts : G104','Gifts : G110','Gifts : G121']
        expected_yval_list=['0', '2M', '4M', '6M', '8M','10M','12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.3 : ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 05.4 : Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", 'bar_blue', 'Step 05.5 : Verify bar Color')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", 'bar_blue', 'Step 05.6 : Verify bar Color')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!", 'pale_green', 'Step 05.7 : Verify bar Color')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g1!mbar!", 'pale_green', 'Step 05.8 : Verify bar Color')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g3!mbar!", 'pale_yellow', 'Step 05.9 : Verify bar Color')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g3!mbar!", 'pale_yellow', 'Step 05.10 : Verify bar Color')
        expected_tooltip_list=['Category:Coffee', 'Product ID:C142', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g1!mbar!', expected_tooltip_list, 'Step 05.11 : verify the default tooltip values')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.12 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.13 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.14 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,TestCase_ID+'_Actual_Step_05', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Save Report      
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        result_obj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(TestCase_ID)
        time.sleep(2)
        
    if __name__=='__main__' :
        unittest.main()