'''
Created on Jul 11, 2017
@author: Nasir @Fixed By : Bhagavathi
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, active_chart_rollup
from common.lib import utillity


class C2204974_TestClass(BaseTestCase):

    def test_C2204974(self):
        """
        TESTCASE VARIABLES
        """
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """
        Step 01: Execute attached fex "Chart_AHTML.fex" in IA.
        """
        utillobj.active_run_fex_api_login("Chart_AHTML.fex","S7074", 'mrid', 'mrpass')
        time.sleep(7)
        parent_css="div [id='MAINTABLE_wmenu0']"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(1)
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 02.1 Verify -yAxis Title")
        result_obj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 02.2 Verify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 02.3:Verify XY labels")
        result_obj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 10, 'Step 02.4: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "cerulean_blue", "Step 02.5: Verify  bar color")
        expected_tooltip_list=['Unit Sales, Coffee/Latte: 878,063']
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list, 'Step 01.d: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0', 'Unit Sales by Category, Product', 'Step 01.e: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
                                
        """
        Step 02: Click aggregation icon under Active tool bar.
        
        """
        expected_menu_list=['Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct']
        actual_menu_list=[]
        rollobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 7)
        time.sleep(2)
        sum_css="[id^='dt0_SUM'][id$='_x__0'][style*='block'] span[id ^='set']"
        x=self.driver.find_elements_by_css_selector(sum_css)
        for i in range(len(x)):
            actual_menu_list.append(x[i].text.strip())
        utillobj.asequal(expected_menu_list, actual_menu_list, "Step 02: Verify that calculation list shows 6 options for Numeric field ")
        
        
if __name__ == '__main__':
    unittest.main()
    
    
    