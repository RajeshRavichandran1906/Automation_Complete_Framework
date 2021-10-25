'''
Created on Aug 10, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050553
Description : Verify the chart filter funtionality 
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea,active_chart_rollup

class C2050553_TestClass(BaseTestCase):

    def test_C2050553(self):
        
        """
            CLASS OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
    
        """
            Step 01: Execute the attached 89821.fex
        """
        utillobj.active_run_fex_api_login("89821.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(8)
        
        """Step 02 : Select Capuccino, Espresso and Latte bars from Coffee section in the chart via lasso.
        Verify these menu items appear on the chart:
        3 points
        Filter Chart
        Exclude from Chart
        """
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 02.01: Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 02.02: erify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 02.03: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 10, 'Step 02.04: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "cerulean_blue", "Step 02.05: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 02.06: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 02.07: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
       
        source_element = utillobj.validate_and_get_webdriver_object('#MAINTABLE_wbody0 rect[class*="riser!s0!g0!mbar!"]', 'source_element')
        target_element = utillobj.validate_and_get_webdriver_object('#MAINTABLE_wbody0 rect[class*="riser!s0!g2!mbar!"]', 'target_element')
        resobj.create_laso(source_element, target_element, source_element_location='middle',  target_element_location='bottom_middle', source_xoffset=0, source_yoffset=0, target_xoffset=0, target_yoffset=0)
        menu_list = ['3 points', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_lasso_tooltip(menu_list, 'Step 02.10: Verify these menu items appear on the chart')
        
        """Step 03: Click Filter Chart menu option. """
        resobj.select_lasso_tooltip_item('Filter Chart')
        time.sleep(8)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 03.01: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 03.02: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.03: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 03.05: Filter Button Visible')
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 03.06: Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 03.07: Verify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 03.08: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 3, 'Step 03.09: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "cerulean_blue", "Step 03.10: Verify  bar color")

        """Step 04: Mouse over on Espresso bar and verify context menu appears. It displays:"""
        
        expected_tooltip_list=['Unit Sales, Coffee/Espresso: 308,986']
        miscelaneous_obj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g1!mbar!', expected_tooltip_list, "Step 04: verify tooltip values")
        
        """Step 05: Left click on the Espresso bar. 
        Click on Remove filter icon available on active tool bar"""
        
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 8)
        time.sleep(3)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 05.01: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 05.02: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.03: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 05.05: Filter Button Removed')
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 05.06: Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 05.07: Verify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 05.08: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 10, 'Step 05.09: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "cerulean_blue", "Step 05.10: Verify  bar color")
        
if __name__ == '__main__':
    unittest.main()        