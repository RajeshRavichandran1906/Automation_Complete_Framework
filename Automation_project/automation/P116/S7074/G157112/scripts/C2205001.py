'''
Created on Jul 28, 2017
@author: Nasir
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, active_chart_rollup
from common.lib import utillity


class C2205001_TestClass(BaseTestCase):

    def test_C2205001(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2205001'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        """
        Step 01: Run the attached 150599.fex from adhoc page
        """
        utillobj.active_run_fex_api_login("C2205001.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(7)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 5)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","COUNTRY", "Step 01a: Verify X-Axis Title")
        expected_xval_list=['JAPAN','W GERMANY','ITALY','ENGLAND','FRANCE']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 01b: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 5, 'Step 01c: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!", 'cerulean_blue_1', 'Step 01d: Verify bar Color')
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0',"riser!s0!g2!mbar!", ['SALES, ITALY: 30,200'],"Step 01e: Verify Chart tooltip")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'SALES by COUNTRY', 'Step 01f: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01g: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01h: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01i: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        
        """
        Step 02: Select pie chart from chart window toolbar.
        Step 03: Hover the mousecursor over the pie chart on each slices it has to display the correct tooltip data.
        """
        rollobj.click_pivot_menu_bar_items("MAINTABLE_0", 2)
        time.sleep(7)
        element = self.driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.take_screenshot(element,Test_Case_ID + '_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0',"riser!s0!g0!mwedge!", ['JAPAN','SALES: 78,030','37.4% of 208K'],"Step 03a(i): Verify first pie slice tooltip")
        utillobj.verify_chart_color('MAINTABLE_wbody0',"riser!s0!g0!mwedge!",'cerulean_blue_1',"Step 03a(ii):Verify first pie slice fill Color")
        time.sleep(5)
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0',"riser!s1!g0!mwedge!", ['W GERMANY','SALES: 88,190','42.3% of 208K'],"Step 03b(i): Verify second pie slice tooltip")
        utillobj.verify_chart_color('MAINTABLE_wbody0',"riser!s1!g0!mwedge!",'dark_turquoise',"Step 03b(ii):Verify second pie slice fill Color")
        time.sleep(5)
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0',"riser!s2!g0!mwedge!", ['ITALY','SALES: 30,200','14.5% of 208K'],"Step 03c(i): Verify third pie slice tooltip")
        utillobj.verify_chart_color('MAINTABLE_wbody0',"riser!s2!g0!mwedge!",'sun_yellow',"Step 03c(ii):Verify third pie slice fill Color")
        time.sleep(5)
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0',"riser!s3!g0!mwedge!", ['ENGLAND','SALES: 12,000','5.8% of 208K'],"Step 03d(i): Verify fourth pie slice tooltip")
        utillobj.verify_chart_color('MAINTABLE_wbody0',"riser!s3!g0!mwedge!",'milky_carrot',"Step 03d(ii):Verify fourth pie slice fill Color")
        time.sleep(5)
        result_obj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['SALES'],"Step 03e: Verify PIE Chart Label")
        result_obj.verify_riser_legends('MAINTABLE_wbody0', ['JAPAN', 'W GERMANY', 'ITALY', 'ENGLAND', 'FRANCE'], "Step 03f: Verify PIE Chart Legends")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'SALES by COUNTRY', 'Step 03g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 03h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()
    
    
    