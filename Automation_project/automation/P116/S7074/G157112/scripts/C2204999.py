'''
Created on Jul 27, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204999
TestCase Name = MED >> Project 132231 AHTML: Embedded heading crashes the server
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea
from common.lib import utillity

class C2204999_TestClass(BaseTestCase):

    def test_C2204999(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        1. Run the attached repro - 132331.fex from adhoc page.
        Check that the chart report heading does not crash the server and no error messages appear.
        """
        utillobj.active_run_fex_api_login("132231.fex", "S7074", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='legend-labels!s0!']", 'SEATS', 60)
        xaxis_value="COUNTRY"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 01:a(i) Verify X-Axis Title")
        yaxis_value="SEATS"
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 01:a(ii) Verify Y-Axis Title")
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '5', '10', '15', '20', '25', '30', '35', '40']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 1.1: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 5, 'Step 1.2: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "cerulean_blue_1", "Step 01.3: Verify bar color")
        time.sleep(5)
        expected_tooltip_list=['SEATS, ENGLAND: 13']
        miscelaneousobj.verify_active_chart_tooltip("MAINTABLE_wbody0", "riser!s0!g0!mbar!", expected_tooltip_list, 'Step 01.4: verify the bar tooltip values')
        expected_title="This is HEADING"
        cr_title=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0_f text[class^='title']").text.strip()
        utillobj.asequal(cr_title,expected_title,'Step 01.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.take_screenshot(ele,'C2204999_Actual_step01', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()