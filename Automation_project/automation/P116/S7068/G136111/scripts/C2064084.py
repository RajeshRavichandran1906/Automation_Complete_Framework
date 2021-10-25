'''
Created on Aug 21, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2064084    
Description : This Case tests the ability to remove a single Bar from a chart, for which there are two sorts.
Excluding/Filtering on one bar of a group of bars should not eliminate all bars from the major sort.
'''

import unittest, time
from common.lib import utillity,core_utility
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea,active_chart_rollup

class C2064084_TestClass(BaseTestCase):

    def test_C2064084(self):
        
        """
            CLASS OBJECTS
        """
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
            Step 01:Execute the attached repro - bar_chart_8105m.fex
        """
        utillobj.active_run_fex_api_login("bar_chart_8105m.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(10)
        
        #Expect to see the following Active Bar Chart, with 10 bars for Category/Product.
        
        resultobj.verify_number_of_riser('MAINTABLE_0', 1,10, 'Step 01.01: Expect to see the following Active Bar Chart, with 10 bars ')
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 01.02: Verify -yAxis Title")
        resultobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 01.03: Verify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 01.04:")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "cerulean_blue", "Step 01.05: Verify  bar color")
        miscelanousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 01.06: Verify Chart Title')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 01.07: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
            Step 02 : Left-click the second Bar, representing Coffee/Espresso, then select Exclude from Chart.
        """
        second_bar = driver.find_element_by_css_selector("#MAINTABLE_0 rect[class*='riser!s0!g1!mbar']")
        core_utils.left_click(second_bar)
        resultobj.select_lasso_tooltip_item('Exclude from Chart')
        
        #Expect to see only the single bar for Coffee/Espresso removed.
        
        expected_xval_list1=['Coffee/Capuccino', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_0', expected_xval_list1, expected_yval_list, 'Step 02.01: Expect to see only the single bar for Coffee/Espresso removed.')
        time.sleep(10)
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 02.02: Verify -yAxis Title")
        resultobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 02.03: Verify -xAxis Title")
        resultobj.verify_number_of_riser('MAINTABLE_0', 1,9, 'Step 02.04: Expect to see the following Active Bar Chart, with 9 bars')
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "cerulean_blue", "Step 02.05: Verify  bar color")
        miscelanousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 02.06: Verify Chart Title')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 02.07: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 02.10: Filter Button Visible')
       
        
        """
            Step 03: Click the Filter control at the top to remove the Filter. 
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 8)
        time.sleep(3)
        
        #Expect to see all 10 bars again displayed.
        
        resultobj.verify_number_of_riser('MAINTABLE_0', 1, 10, 'Step 03.01: Expect to see the following Active Bar Chart, with 10 bars  .')
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 03.02: Verify -yAxis Title")
        resultobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 03.03: Verify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 03.04:")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "cerulean_blue", "Step 03.05: Verify  bar color")
        miscelanousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 03.06: Verify Chart Title')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 03.07: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 03.10: Filter Button Removed')
           
        """
            Step 04: Draw a box with the left-click that touches Coffee/Latte and Food/Biscotti, the third and fourth bars.
            Select Exclude from Chart.
        """
        source_element = utillobj.validate_and_get_webdriver_object('#MAINTABLE_wbody0 rect[class*="riser!s0!g2!mbar!"]', 'source_element')
        target_element = utillobj.validate_and_get_webdriver_object('#MAINTABLE_wbody0 rect[class*="riser!s0!g3!mbar!"]', 'target_element')
        resultobj.create_laso(source_element, target_element, source_element_location='middle',  target_element_location='middle', source_xoffset=0, source_yoffset=0, target_xoffset=0, target_yoffset=0)
        resultobj.select_lasso_tooltip_item('Exclude from Chart')
        time.sleep(6)
        
        #Expect to see only the bars for Coffee/Latte and Food/Biscotti removed.
        
        expected_xval_list2=['Coffee/Capuccino', 'Coffee/Espresso', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_0', expected_xval_list2, expected_yval_list, 'Step 04.01: Expect to see only the bars for Coffee/Latte and Food/Biscotti removed.')
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 04.02: Verify -yAxis Title")
        resultobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 04.03: Verify -xAxis Title")
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "cerulean_blue", "Step 04.04: Verify  bar color")
        miscelanousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 04.05: Verify Chart Title')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 04.06: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 04.09: Filter Button Visible')
        resultobj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 8, 'Step 04.10: Verify the total number of risers displayed on preview')
       
        """
            Step 05: Reset the Bar Chart again by clicking the Filter icon at the top.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 8)
        time.sleep(3)
        
        #Expect to see all 10 bars again displayed.
        
        miscelanousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 05.01: Verify Chart Title')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 05.02: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.03: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 05.05: Filter Button Removed')
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 05.06: Verify -yAxis Title")
        resultobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 05.07: Verify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 05.08:")
        resultobj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 10, 'Step 05.09: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "cerulean_blue", "Step 05.10: Verify  bar color")

if __name__ == '__main__':
    unittest.main()        