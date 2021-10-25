'''
Created on July 03, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204921
TestCase Name =Verify that Changed titles on axis labels are reflected in output

'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon
from common.lib import utillity


class C2204915_TestClass(BaseTestCase):

    def test_C2204915(self):
       
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID="C2204915"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        def change_axis_title(field_name,title):
            metadataobj.querytree_field_click(field_name,1,1,"Change Title...")
            parent_css="div[id^='BiDialog'] div[id^='BiOptionPane'] input"
            result_obj.wait_for_property(parent_css,1)
            change_title=self.driver.find_element_by_css_selector(parent_css)
            change_title.clear()
            change_title.send_keys(title)
            buttons=self.driver.find_elements_by_css_selector("div[id^='BiDialog'] div[id^='BiOptionPane'] [id^='BiButton']")
            buttons[0].click()
            time.sleep(2)
            
        """
        Step 01 : Open IA and create a new chart using the GGSALES file.
        Select Active Report as the output format.
        Add Category to the Horizontal axis.
        Add Unit Sales to the Vertical axis.
        Expect to see the following Bar Chart Preview pane.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(5)
        metadataobj.datatree_field_click('Category', 1, 1, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="Category")
        metadataobj.datatree_field_click('Unit Sales', 1, 1,'Add To Query','Vertical Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="Unit Sales")
        result_obj.verify_xaxis_title("TableChart_1",'Category', "Step 01.1 : Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 01.2 : Verify Y-Axis Title")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 01.3 :')
        result_obj.verify_number_of_riser('TableChart_1', 1, 1, 'Step 01.4 : Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 01.5 : Verify bar color")
         
        """
        Step 02: Click the Run button.
        Expect to see the following Preview Bar chart, Verify that the Horizontal axis reads - 'Category'.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(8)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css,3)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Category", "Step 02.1 : Verify that the Horizontal axis reads - 'Category'")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","Unit Sales", "Step 02.2 :  Verify that the Horizontal axis reads - 'Unit Sales'")
        expected_xval_list=['Coffee','Food','Gifts']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 02.3 : ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 3, 'Step 02.4 : Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!", 'bar_blue', 'Step 02.5 : Verify bar Color')
        expected_tooltip_list=['Category:Food', 'Unit Sales:1384845', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g1!mbar!', expected_tooltip_list, 'Step 02.6 : verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category', 'Step 02.7 : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.8 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        
        """
        Step 03 : Right click on Unit Sales in Query window and select 'Change Title'.
        Change the Title to - 'Summed Units of Sale'
        Expect to see the following Preview pane with the changed title for Unit Sales.
        """
        change_axis_title('Unit Sales','Summed Units of Sale')
        parent_css="#TableChart_1 text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Summed Units of Sale')
        result_obj.verify_xaxis_title("TableChart_1",'Category', "Step 03.1 : Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Summed Units of Sale', "Step 03.2 : Verify Expect to see the following Preview pane with the changed title for Unit Sales")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 03.3 :')
        result_obj.verify_number_of_riser('TableChart_1', 1, 1, 'Step 03.4 : Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 03.5 : Verify bar color")
        
        """
        Step 04 : Click OK to the Title change entry. Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(8)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css,3)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Category", "Step 04.1 : Verify that the Horizontal axis reads - 'Category'")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","Summed Units of Sale", "Step 04.2 :  Verify Expect to see the following Bar chart with changed title for Unit Sales")
        expected_xval_list=['Coffee','Food','Gifts']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 04.3 : ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 3, 'Step 04.4 : Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!", 'bar_blue', 'Step 04.5 : Verify bar Color')
        expected_tooltip_list=['Category:Food', 'Summed Units of Sale:1384845', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g1!mbar!', expected_tooltip_list, 'Step 04.6 : verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Summed Units of Sale by Category', 'Step 04.7 : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.8 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        
        """
        Step 05 : Right click on Category in Query window and select 'Change Title'.
        Change the title to 'Name of Product Category'.
        Expect to see the following Preview pane with the changed title for Category.
        """
        
        change_axis_title('Category','Name of Product Category')
        parent_css="#TableChart_1 text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Name of Product Category')
        result_obj.verify_xaxis_title("TableChart_1",'Name of Product Category', "Step 05.1 :  Verify Expect to see the following Preview pane with the changed title for Category")
        result_obj.verify_yaxis_title("TableChart_1", 'Summed Units of Sale', "Step 05.2 : Verify Y-Axis Title")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 05.3 :')
        result_obj.verify_number_of_riser('TableChart_1', 1, 1, 'Step 05.4 : Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 05.5 : Verify bar color")
        
        """
        Step 06 : Click OK to the Title change entry. Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(8)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css,3)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Name of Product Category", "Step 06.1 : Verify that the Horizontal axis reads - 'Category'")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","Summed Units of Sale", "Step 06.2 :  Verify Expect to see the following Bar chart with changed title for Unit Sales")
        expected_xval_list=['Coffee','Food','Gifts']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 06.3 : ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 3, 'Step 06.4 : Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!", 'bar_blue', 'Step 06.5 : Verify bar Color')
        expected_tooltip_list=['Name of Product Category:Food', 'Summed Units of Sale:1384845', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g1!mbar!', expected_tooltip_list, 'Step 06.6 : verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Summed Units of Sale by Name of Product Category', 'Step 06.7 : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.8 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        
        """
        Save Report      
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2204915_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
        result_obj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(8)
        
if __name__ == '__main__':
    unittest.main()