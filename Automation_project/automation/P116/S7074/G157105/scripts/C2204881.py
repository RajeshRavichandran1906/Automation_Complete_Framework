'''
Created on JUL 13, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204881
TestCase Name = Verify user can edit column on Y-Axis
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,active_chart_rollup
from common.lib import utillity

class C2204881_TestClass(BaseTestCase):

    def test_C2204881(self):
        
        Test_Case_ID="C2204881"
        """
            TESTCASE VARIABLES
        """   
        driver = self.driver #Driver reference object created
        
        utillobj = utillity.UtillityMethods(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        """
            Step 01:Execute attached fex "C2204881.fex" in IA.
        """
        utillobj.active_run_fex_api_login("C2204881.fex", "S7074", 'mrid', 'mrpass')
        parent_css="div [id='MAINTABLE_wmenu0']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 60)
        
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 01.1: Verify Y-Axis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 01.2 Verify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 01.3:Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 20, 'Step 01.4: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g2!mbar!", "cerulean_blue", "Step 01.5: Verify  bar color")
        expected_tooltip_list=['Dollar Sales, Coffee/Latte: 10,943,622']
        miscelaneous_obj.verify_active_chart_tooltip('MAINTABLE_wbody0', "riser!s1!g2!mbar!", expected_tooltip_list, "Step 01.6: verify tooltip values")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 01.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 01.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        """
            Step 02:Click Add (Y) option from the dropdown menu. Verify that chart shows Unit Sales and Dollar Sales checked
        """
        rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0', 1, 'Add (Y)',elem_index=0, custom_css='cpop', checked_list_item=['Unit Sales', 'Dollar Sales'], msg="Step 02:Verify checked_list_item")
        time.sleep(3)
        """
            Step 03:Click Add (Y) > Unit Sales. Verify that chart now shows 'Dollar Sales By Category, Product'
        """
        rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0', 1, 'Add (Y)->Unit Sales',elem_index=0,custom_css='cpop')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 03.1 Verify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 03.2:Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 10, 'Step 03.3: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g2!mbar!", "cerulean_blue", "Step 03.4: Verify  bar color")
        expected_tooltip_list=['Dollar Sales, Coffee/Latte: 10,943,622']
        miscelaneous_obj.verify_active_chart_tooltip('MAINTABLE_wbody0', "riser!s0!g2!mbar!", expected_tooltip_list, "Step 03.5: verify tooltip values")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales BY Category, Product', 'Step 03.6: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 03.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        """
            Step 04:Now go back to dropdown menu and click Add (Y) > Unit Sales
        """
        rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0', 1, 'Add (Y)->Unit Sales',elem_index=0,custom_css='cpop')
        time.sleep(3)
        """
            Step 05:Verify chart with this title 'Dollar Sales, Unit Sales BY Category, Product' is displayed. Where 2 measures are displayed together on Y axis.

        """
        resobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 05.1 Verify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 05.2:Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 20, 'Step 05.3: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g2!mbar!", "cerulean_blue", "Step 05.4: Verify  bar color")
        expected_tooltip_list=['Dollar Sales, Coffee/Latte: 10,943,622']
        miscelaneous_obj.verify_active_chart_tooltip('MAINTABLE_wbody0', "riser!s0!g2!mbar!", expected_tooltip_list, "Step 05.5: verify tooltip values")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales, Unit Sales BY Category, Product', 'Step 05.6: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 05.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        legend=["Dollar Sales", "Unit Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.10: Verify Y-Axis Title")
        time.sleep(3)
        ele=driver.find_element_by_css_selector("#orgdivouter0")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step5', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()  