'''
Created on Jan 29, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10851
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2358904
TestCase Name = Removing a Global Filter from a Document.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous
from common.lib import utillity

class C2358904_TestClass(BaseTestCase):

    def test_C2358904(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID='C2358904'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)

        """
        Step 01 : Execute the attached repro - GLOBALFILTER_CHART_ON for AHTML.
        """
        utillobj.active_run_fex_api_login('GLOBALFILTER_CHART_ON.fex', 'S10851_2', 'mrid', 'mrpass')
        vis_resultobj.wait_for_property("#MAINTABLE_wbody0_ft tbody", 1, string_value='UnitSalesbyState', with_regular_exprestion=True)
        time.sleep(3)
        
        """
        Expect to see an AHTML Document with Global Filtering enabled. The bar at the top shows the Filter symbol.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 25)
        
        global_filter_css = "#IBILAYOUTDIV0TABS td[id='iLayM4$'] [class='arDashboardBarGlobalButton']"
        utillobj.verify_object_visible(global_filter_css, True, 'Step 01: Expect to see an AHTML Document with Global Filtering enabled.')
        
        exp_page_text = 'Global Filter for Document containing Reports'
        elem_css = driver.find_element_by_css_selector("[id^=LOBJText] span")
        act_page_text = elem_css.text.strip()
        print(act_page_text)
        utillobj.asequal(act_page_text, exp_page_text,  "Step 01.a: Verify Global Filter for Document containing Reports")
        
        xaxis_value="State"
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 1:a(i) Verify X-Axis Title")
        yaxis_value="Unit Sales"
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 1:a(ii) Verify y-Axis Title")
        expected_xval_list=['CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 1:a(iii):Verify XY labels")
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 11, 'Step 1.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "cerulean_blue", "Step 1.c: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0","Unit Sales by State", "Step 1.e : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart','Original Chart'],"Step 1.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 1.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 1.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Unit Sales, CA:610,570']
        vis_resultobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 1.i: verify the default tooltip values')
        time.sleep(8)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step01', image_type='actual',x=1, y=1, w=-1, h=-1)
        utillobj.wf_logout()
        time.sleep(2)
        
        """
        Step 02 : Execute the attached repro - GLOBALFILTER_CHART_OFF for AHTML.
        """
        utillobj.active_run_fex_api_login('GLOBALFILTER_CHART_OFF.fex', 'S10851_2', 'mrid', 'mrpass')
        vis_resultobj.wait_for_property("#MAINTABLE_wbody0_ft tbody", 1, string_value='UnitSalesbyState', with_regular_exprestion=True)
        time.sleep(3)
        
        """
        Expect to see an AHTML Document with Global Filtering disabled. The bar at the top does not show the Filter symbol.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 25)
        
        global_filter_css = "#IBILAYOUTDIV0TABS td[id='iLayM4$'] [class='arDashboardBarGlobalButton']"
        utillobj.verify_object_visible(global_filter_css, False, 'Step 02: Expect to see an AHTML Document with Global Filtering disabled.')
        
        exp_page_text = 'Global Filter for Document containing Reports'
        elem_css = driver.find_element_by_css_selector("[id^=LOBJText] span")
        act_page_text = elem_css.text.strip()
        print(act_page_text)
        utillobj.asequal(act_page_text, exp_page_text,  "Step 02.a: Verify Global Filter for Document containing Reports")
        
        xaxis_value="State"
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 2:a(i) Verify X-Axis Title")
        yaxis_value="Unit Sales"
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 2:a(ii) Verify y-Axis Title")
        expected_xval_list=['CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 2:a(iii):Verify XY labels")
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 11, 'Step 2.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "cerulean_blue", "Step 2.c: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0","Unit Sales by State", "Step 2.e : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart','Original Chart'],"Step 2.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 2.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 2.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Unit Sales, CA:610,570']
        vis_resultobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 2.i: verify the default tooltip values')
        time.sleep(8)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step02', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()