'''
Created on August 02, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/204914
TestCase Name =Verify that bars for fields may be hidden in output chart, then re-displayed.
'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon
from common.lib import utillity


class C2204914_TestClass(BaseTestCase):

    def test_C2204914(self):
       
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID="C2204914"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01 : Open IA and create a new Chart using the GGSALES file.
        Select Active Report as the output format.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(5)
        
        """
        Add fields Unit Sales and Dollar Sales to the Vertical axis.
        Add fields Category and Product to the Horizontal axis.
        """
        metadataobj.datatree_field_click('Unit Sales', 1, 1,'Add To Query','Vertical Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="Unit Sales")
            
        metadataobj.datatree_field_click('Dollar Sales', 1, 1,'Add To Query','Vertical Axis')
        parent_css="#TableChart_1 .legend g text[class*='legend-labels']"
        result_obj.wait_for_property(parent_css, 2)
        
        metadataobj.datatree_field_click('Category', 1, 1, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="Category")
        
        metadataobj.datatree_field_click('Product', 1, 1, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="Category : Product")
        
        """
        Step 01.1 : Expect to see the following Chart Preview pane.
        """
        result_obj.verify_xaxis_title("TableChart_1",'Category : Product', "Step 01.1 : Verify X-Axis Title")
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 01.2 :')
        result_obj.verify_riser_legends('TableChart_1',['Unit Sales','Dollar Sales'],'Step 01.3 : ')
        result_obj.verify_number_of_riser('TableChart_1', 1, 4, 'Step 01.5 : Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 01.4 : Verify bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "bar_green", "Step 01.5 : Verify bar color")
        
        """
        Step 02 : Click the Run button.
        Expect to see the following default Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css,20)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Category : Product", "Step 02.1 : Verify X-Axis Title")
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso','Coffee : Latte','Food : Biscotti','Food : Croissant','Food : Scone','Gifts : Coffee Gri...','Gifts : Coffee Pot','Gifts : Mug','Gifts : Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M','10M','12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 02.3 : ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 02.4 : Verify number of risers')
        result_obj.verify_riser_legends('MAINTABLE_wbody0',['Unit Sales','Dollar Sales'],'Step 02.4 : ')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", 'bar_blue1', 'Step 02.5 : Verify bar Color')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", 'pale_green', 'Step 02.6 : Verify bar Color')
        expected_tooltip_list1=['Category:Coffee', 'Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        expected_tooltip_list2=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list1, 'Step 02.6 : verify the default tooltip values')
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g2!mbar!', expected_tooltip_list2, 'Step 02.7 : verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product', 'Step 02.7 : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.8 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        
        """
        Step 03 : Right click on Unit Sales Bar in design area, and select Visibility > Hide.
        """
        result_obj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        time.sleep(2)
        obj_locator=driver.find_element_by_css_selector("#TableChart_1 [class*='riser!s0!g0!mbar!']")
        utillobj.click_on_screen(obj_locator, 'middle', click_type=0)
        utillobj.click_on_screen(obj_locator, 'middle', click_type=1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Visibility')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Hide')
        parent_css="#TableChart_1 [class*='riser!s']"
        result_obj.wait_for_property(parent_css,2)
         
        """
        Step 03.1 : Expect to see the following Preview pane with the bar for Unit Sales removed.
        """
        result_obj.verify_xaxis_title("TableChart_1",'Category : Product', "Step 03.1 : Verify X-Axis Title")
        result_obj.verify_yaxis_title('TableChart_1', 'Dollar Sales','Step 03.2 : Verify Y-Axis Title')
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 03.3 :')
        legends=len(driver.find_elements_by_css_selector("#TableChart_1 .legend text"))
        utillobj.asequal(0,legends,'Step 03.4 : Verify legends removed')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 03.5 : Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 03.5 : Verify bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue1", "Step 03.6 : Verify bar color")
         
        """
        Step 04 : Click the Run button.
        Expect to see the following Active Bar chart with only Dollar Sales bars and Category/Product across the chart.
        Also verify that the Unit Sales field in the query panel has been grayed out(Hidden).
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css,10)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Category : Product", "Step 04.1 : Verify X-Axis Title")
        result_obj.verify_yaxis_title('MAINTABLE_wbody0', 'Dollar Sales','Step 04.2 : Verify Y-Axis Title')
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso','Coffee : Latte','Food : Biscotti','Food : Croissant','Food : Scone','Gifts : Coffee Gri...','Gifts : Coffee Pot','Gifts : Mug','Gifts : Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M','10M','12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 04.3 : ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 02.4 : Verify number of risers')
        legends=len(driver.find_elements_by_css_selector("#MAINTABLE_wbody0 .legend text"))
        utillobj.asequal(0,legends,'Step 03.4 : Verify legends removed')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", 'bar_blue1', 'Step 02.5 : Verify bar Color')
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list, 'Step 02.6 : verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales by Category, Product', 'Step 02.7 : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.8 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        
        """
        Step 04.1 : verify that the Unit Sales field in the query panel has been grayed out(Hidden).
        """
        hidden_feild=driver.find_element_by_css_selector("#queryTreeColumn .bi-tree-view-body-content table[class='bi-tree-view-table']>tbody>tr[style*='gray']").text.strip()
        utillobj.asequal('Unit Sales',hidden_feild,'Step 04.1.1 : Verify that the Unit Sales field in the query panel has been grayed out(Hidden).')

        """
        Step 05 : To make the Unit Sales Bars re-appear, right click on the Unit Sales field in the Query panel, then select Visibility and select Show.
        """
        result_obj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        time.sleep(2)
        metadataobj.querytree_field_click('Unit Sales',1,1)
        time.sleep(4)
        utillobj.select_or_verify_bipop_menu('Visibility')
        utillobj.select_or_verify_bipop_menu('Show')
        parent_css="#TableChart_1 [class*='riser!s']"
        result_obj.wait_for_property(parent_css,4)
        
        """
        Step 05.1 : Expect to see the Dollar Sales Bar re-appear in the Preview pane.
        """
        result_obj.verify_xaxis_title("TableChart_1",'Category : Product', "Step 05.1 : Verify X-Axis Title")
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 05.2 :')
        result_obj.verify_riser_legends('TableChart_1',['Unit Sales','Dollar Sales'],'Step 05.3 : ')
        result_obj.verify_number_of_riser('TableChart_1', 1, 4, 'Step 01.5 : Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 05.4 : Verify bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "bar_green", "Step 05.5 : Verify bar color")
        hidden_feild=len(driver.find_elements_by_css_selector("#queryTreeColumn .bi-tree-view-body-content table[class='bi-tree-view-table']>tbody>tr[style*='gray']"))
        utillobj.asequal(0,hidden_feild,'Step 05.6 : Verify that the Unit Sales field in the query panel has been removed grayed out(Hidden).')
        
        """
        Step 06 : Click the Run button.
        Expect to see the Unit Sales Bar re-appear.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css,20)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Category : Product", "Step 06.1 : Verify X-Axis Title")
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso','Coffee : Latte','Food : Biscotti','Food : Croissant','Food : Scone','Gifts : Coffee Gri...','Gifts : Coffee Pot','Gifts : Mug','Gifts : Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M','10M','12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 06.2 : ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 06.3 : Verify number of risers')
        result_obj.verify_riser_legends('MAINTABLE_wbody0',['Unit Sales','Dollar Sales'],'Step 06.4 : ')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", 'bar_blue1', 'Step 06.5 : Verify bar Color')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", 'pale_green', 'Step 06.6 : Verify bar Color')
        expected_tooltip_list1=['Category:Coffee', 'Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        expected_tooltip_list2=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list1, 'Step 06.7 : verify the default tooltip values')
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g2!mbar!', expected_tooltip_list2, 'Step 06.8 : verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product', 'Step 06.9 : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.10 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.11 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.12 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        
        """
        Step 07 : Right click on Unit Sales Bar in design area, and select Visibility > Hide. 
        Click the Run button to re-hide Unit Sales.
        """
        result_obj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        time.sleep(2)
        obj_locator=driver.find_element_by_css_selector("#TableChart_1 [class*='riser!s0!g0!mbar!']")
        utillobj.click_on_screen(obj_locator, 'middle', click_type=0)
        utillobj.click_on_screen(obj_locator, 'middle', click_type=1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Visibility')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Hide')
        parent_css="#TableChart_1 [class*='riser!s']"
        result_obj.wait_for_property(parent_css,2)
        
        """
        Verify design area
        """
        result_obj.verify_xaxis_title("TableChart_1",'Category : Product', "Step 07.1 : Verify X-Axis Title")
        result_obj.verify_yaxis_title('TableChart_1', 'Dollar Sales','Step 07.2 : Verify Y-Axis Title')
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 07.3 :')
        legends=len(driver.find_elements_by_css_selector("#TableChart_1 .legend text"))
        utillobj.asequal(0,legends,'Step 07.4 : Verify legends removed')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 07.5 : Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 07.5 : Verify bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue1", "Step 07.6 : Verify bar color")
        hidden_feild=driver.find_element_by_css_selector("#queryTreeColumn .bi-tree-view-body-content table[class='bi-tree-view-table']>tbody>tr[style*='gray']").text.strip()
        utillobj.asequal('Unit Sales',hidden_feild,'Step 07.6.1 : Verify that the Unit Sales field in the query panel has been grayed out(Hidden).')
        
        """
        Click the Run button to re-hide Unit Sales.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css,10)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Category : Product", "Step 07.7 : Verify X-Axis Title")
        result_obj.verify_yaxis_title('MAINTABLE_wbody0', 'Dollar Sales','Step 07.8 : Verify Y-Axis Title')
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso','Coffee : Latte','Food : Biscotti','Food : Croissant','Food : Scone','Gifts : Coffee Gri...','Gifts : Coffee Pot','Gifts : Mug','Gifts : Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M','10M','12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 07.9 : ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 07.10 : Verify number of risers')
        legends=len(driver.find_elements_by_css_selector("#MAINTABLE_wbody0 .legend text"))
        utillobj.asequal(0,legends,'Step 03.4 : Verify legends removed')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", 'bar_blue1', 'Step 07.11 : Verify bar Color')
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list, 'Step 07.11 : verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales by Category, Product', 'Step 07.12 : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.13 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.12 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.13 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        
        """
        Step 08 : Right click on remaining Dollar Sales Bar in design area, and select Visibility > Show.
        """
        result_obj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        time.sleep(2)
        obj_locator=driver.find_element_by_css_selector("#TableChart_1 [class*='riser!s0!g0!mbar!']")
        utillobj.click_on_screen(obj_locator, 'middle', click_type=0)
        utillobj.click_on_screen(obj_locator, 'middle', click_type=1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Visibility')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Show')
        parent_css="#TableChart_1 [class*='riser!s']"
        result_obj.wait_for_property(parent_css,4)
        
        """
        Expect to see the Preview pane back with bars for Unit Sales and Dollar Sales.
        """
        result_obj.verify_xaxis_title("TableChart_1",'Category : Product', "Step 08.1 : Verify X-Axis Title")
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 08.2 :')
        result_obj.verify_riser_legends('TableChart_1',['Unit Sales','Dollar Sales'],'Step 08.3 : ')
        result_obj.verify_number_of_riser('TableChart_1', 1, 4, 'Step 08.5 : Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 08.4 : Verify bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "bar_green", "Step 08.5 : Verify bar color")
        hidden_feild=len(driver.find_elements_by_css_selector("#queryTreeColumn .bi-tree-view-body-content table[class='bi-tree-view-table']>tbody>tr[style*='gray']"))
        utillobj.asequal(0,hidden_feild,'Step 08.6 : Verify that the Unit Sales field in the query panel has been removed grayed out(Hidden).')
        
        """
        Step 09 : Click the Run button.
        Expect to see the following Active Bar chart with Unit Sales and Dollar Sales bars and Category/Product across the chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css,20)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Category : Product", "Step 09.1 : Verify X-Axis Title")
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso','Coffee : Latte','Food : Biscotti','Food : Croissant','Food : Scone','Gifts : Coffee Gri...','Gifts : Coffee Pot','Gifts : Mug','Gifts : Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M','10M','12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 09.2 : ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 09.3 : Verify number of risers')
        result_obj.verify_riser_legends('MAINTABLE_wbody0',['Unit Sales','Dollar Sales'],'Step 09.4 : ')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", 'bar_blue1', 'Step 09.5 : Verify bar Color')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", 'pale_green', 'Step 09.6 : Verify bar Color')
        expected_tooltip_list1=['Category:Coffee', 'Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        expected_tooltip_list2=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list1, 'Step 09.7 : verify the default tooltip values')
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g2!mbar!', expected_tooltip_list2, 'Step 09.8 : verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product', 'Step 09.9 : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.10 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.11 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.12 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
          
        """
        Save Report      
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2204917_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
        result_obj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(8)
        
if __name__ == '__main__':
    unittest.main()  