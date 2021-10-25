'''
Created on Jul 28, 2017
@author: Nasir
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, active_chart_rollup
from common.lib import utillity


class C2205002_TestClass(BaseTestCase):

    def test_C2205002(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2205002'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        """
        Step 01: Run the attached 152241.fex from adhoc page.
        """
        utillobj.active_run_fex_api_login("C2205002.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(7)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, 190)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","COUNTRY", "Step 01a: Verify X-Axis Title")
        expected_xval_list=['ENGLAND','FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 01b: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 5, 'Step 01c: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g3!mbar!", 'cerulean_blue_1', 'Step 01d: Verify bar Color')
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0',"riser!s0!g2!mbar!", ['SALES, ITALY: 30,200'],"Step 01e: Verify Chart tooltip")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'SALES BY COUNTRY', 'Step 01f: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01g: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01h: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01i: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        
        """
        Step 02: From Chart tool bar click first icon and select Add (Y) Dealer Cost field.
        """
        rollobj.select_chartmenubar_option('MAINTABLE_0', 0, 'Add (Y)', 0, custom_css='cpop', verify=True, expected_list=['COUNTRY', 'SALES', 'DEALER_COST'], msg='step 02a: ')
        rollobj.click_pivot_menu_bar_items('MAINTABLE_0', 7)
        """
        Step 03: Click on Dealer_Cost. 
        """
        rollobj.select_chartmenubar_option('MAINTABLE_0', 0, 'Add (Y)->DEALER_COST', 0, custom_css='cpop')
        time.sleep(7)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, 290)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","COUNTRY", "Step 03a: Verify X-Axis Title")
        result_obj.verify_riser_legends("MAINTABLE_wbody0",['SALES', 'DEALER_COST'], "Step 03b: Verify Y-Axis Legends Title")
        expected_xval_list=['ENGLAND','FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03c: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 2, 5, 'Step 03d: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", 'cerulean_blue_1', 'Step 03e(i): Verify First Series bar Color')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g4!mbar!", 'black', 'Step 03e(ii): Verify Second Series bar Color')
#         miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0',"riser!s0!g2!mbar!", ['SALES, ITALY: 30,200'],"Step 03f(i): Verify first series Chart tooltip")
#         miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0',"riser!s1!g3!mbar!", ['DEALER_COST, JAPAN: 5,512'],"Step 03f(ii): Verify second series Chart tooltip")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'SALES, DEALER_COST BY COUNTRY', 'Step 03g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 03h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#orgdiv0")   
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)
        
        
if __name__ == '__main__':
    unittest.main()