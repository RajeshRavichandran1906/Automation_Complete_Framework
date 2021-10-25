'''
Created on Jul 10, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204985
TestCase Name = AHTML/FLEX/APDF:NOPRINT: Sorting of BAR chart is not working-150397
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea,ia_resultarea
from common.lib import utillity
from selenium.webdriver.support.color import Color

class C2204985_TestClass(BaseTestCase):

    def test_C2204985(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        1. Execute the attached repro - 150397.fex.
        """
        utillobj.active_run_fex_api_login("150397.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(4)
        parent_css="#MAINTABLE_wbody0 div[style*='pointer'][onclick^='ibiChart']"
        result_obj.wait_for_property(parent_css, 4)
        time.sleep(1)
        expected_xval_list=['W GERMANY','JAPAN','ITALY','ENGLAND','FRANCE']
        expected_yval_list=['0', '20 K', '40 K', '60 K', '80 K', '100 K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 01.1: Verify XY labels',x_custom_css ="div[title][style*='nowrap']",y_custom_css="div[style*='text-align'][style*='right']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 01.2: Verify number of risers', custom_css ="div[style*='pointer'][onclick^='ibiChart']")
        raiser_css = driver.find_elements_by_css_selector("#MAINTABLE_wbody0 div[style*='pointer'][onclick^='ibiChart']")
        riser_color = Color.from_string((raiser_css[0]).value_of_css_property("background-color")).rgba
        expected_color=utillobj.color_picker("Lochmara", 'rgba')
        utillobj.asequal(riser_color, expected_color, 'Step 01.3: Verify Bar color')
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            chart_title=driver.find_element_by_css_selector("#MAINTABLE_wbody0 div[style*='background-color: transparent']").text.strip()
        else:
            chart_title=driver.find_element_by_css_selector("#MAINTABLE_wbody0 div[style*='background-color:transparent']").text.strip()
        print(chart_title)
        expected_title = 'SALES by COUNTRY'
        utillobj.asequal(chart_title,expected_title,'Step 01.4: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01.5: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.take_screenshot(ele,'C2204985_Actual_step01', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(3)
        

if __name__ == '__main__':
    unittest.main()