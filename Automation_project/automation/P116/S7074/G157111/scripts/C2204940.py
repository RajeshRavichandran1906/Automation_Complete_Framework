'''
Created on Jul 24, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204940
TestCase Name = Verify data tip displays value when mouse hovers over
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2204940_TestClass(BaseTestCase):

    def test_C2204940(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)

        """
        1. Execute the attached repro - 46045-AHTML.fex
        Expect to see the following Active Bar Chart.
        """
        utillobj.active_run_fex_api_login("46045-AHTML.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(5)
        css="#MAINTABLE_wbody0 .chartPanel"
        elem1=(By.CSS_SELECTOR, css)
        result_obj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 5)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 5)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        result_obj.wait_for_property(parent_css, 6)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1)
        xaxis_value="COUNTRY"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 01:a(i) Verify X-Axis Title")
        yaxis_value="SALES"
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 01:a(ii) Verify Y-Axis Title")
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 1.1: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 5, 'Step 1.2: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "cerulean_blue_1", "Step 01.3: Verify bar color")
        
        """
        2. Hover over the top bar for England.
        Expect to see the following Tooltip information.
        """
        time.sleep(5)
        expected_tooltip_list=['SALES, ENGLAND: 12,000']
        miscelaneousobj.verify_active_chart_tooltip("MAINTABLE_wbody0", "riser!s0!g0!mbar!", expected_tooltip_list, 'Step 02: verify the bar tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'SALES by COUNTRY', 'Step 02: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 02: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.take_screenshot(ele,'C2204940_Actual_step02', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(3)
        
        
if __name__ == '__main__':
    unittest.main()        