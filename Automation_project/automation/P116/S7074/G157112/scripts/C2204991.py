'''
Created on Jul 11, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204991
TestCase Name = AHTML: Cache:In Chart click on Bar Fld-> incorrect results(Project 90388)
'''
import unittest
import time, re
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea,ia_resultarea
from common.lib import utillity
from selenium.webdriver.support.color import Color

class C2204991_TestClass(BaseTestCase):

    def test_C2204991(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)

        """
        1. Execute cache on.fex from repro
        """
        utillobj.active_run_fex_api_login("cacheon.fex", "S7074", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '864of864records,Page1of16', 'Step 01.1: Execute the cacheon.fex')
        column_list=['City', 'Date', 'Budget Dollars', 'Budget Units', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'cacheon.xlsx','Step 01.3: Expect to see the  Active Report')
#         utillobj.create_data_set('ITableData0', 'I0r', 'cacheon.xlsx')
        
        """
        Step 02: Select Chart Bar option -DOLLAR SALES by CITY -get correct bar output
        """
        values=['Group By (X)', 'City', 'Date', 'Budget Dollars', 'Budget Units', 'Dollar Sales']
        miscelanousobj.verify_menu_items('ITableData0', 5, 'Chart->Column', values, 'Step 02: Verify Group By (Columns) list are displayed', all_items='yes')
        miscelanousobj.select_menu_items("ITableData0", "5", "Chart", "Column", "City")
        time.sleep(5)
        parent_css="#wall1 div[style*='rect'][onclick^='ibiChart']"
        result_obj.wait_for_property(parent_css, 12)
        time.sleep(1)
        expected_xval_list=['Atlanta','Boston','Chicago','Houston','Los Angeles','Memphis','New Haven','New York','Orlando','San Francisco','Seattle','St. Louis']
        expected_yval_list=['3400 K', '3600 K', '3800 K', '4000 K', '4200 K', '4400 K']
        result_obj.verify_riser_chart_XY_labels('wall1', expected_xval_list, expected_yval_list, 'Step 02.1: Verify XY labels',x_custom_css ="div[title][style*='nowrap']",y_custom_css="div[style*='text-align'][style*='right']")
        ia_resultobj.verify_number_of_chart_segment('wall1', 12, 'Step 02.2: Verify number of risers', custom_css ="div[style*='rect'][onclick^='ibiChart']")
        raiser_css = driver.find_elements_by_css_selector("#wall1 div[style*='rect'][onclick^='ibiChart']")
        riser_color = Color.from_string((raiser_css[0]).value_of_css_property("background-color")).rgba
        expected_color=utillobj.color_picker("Lochmara", 'rgba')
        utillobj.asequal(riser_color, expected_color, 'Step 02.3: Verify Bar color')
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            chart_title=driver.find_element_by_css_selector("#wall1 div[style*='background-color: transparent']").text.strip()
        else:
            chart_title=driver.find_element_by_css_selector("#wall1 div[style*='background-color:transparent']").text.strip()
        print(chart_title)
        expected_title = 'Dollar Sales by City'
        utillobj.asequal(chart_title,expected_title,'Step 02.4: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 02.5: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 02.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 02.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(5)
        
        """
        Step 03: click any Bar Field -get the menu,select for example City=Atlanta
        """
        time.sleep(5)
        raiser_css="#wall1 div[style*='rect'][onclick^='ibiChart']"
        obj_locator=driver.find_elements_by_css_selector(raiser_css)
        utillobj.click_on_screen(obj_locator[0], 'middle')
        time.sleep(3)
        utillobj.click_on_screen(obj_locator[0], 'middle', click_type=0)
        time.sleep(2)
        expected_tooltip_list=['Dollar Sales = 4100107', 'City=Atlanta']
        self.select_or_verify_bipop_menu(expected_tooltip_list, msg='Step 03:')
        time.sleep(15)
        ele=driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(ele,'C2204991_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
    def select_or_verify_bipop_menu(self, expected_popup_list, **kwargs):
        utillobj = utillity.UtillityMethods(self.driver)
        temp_css=kwargs['custom_css'] if 'custom_css' in kwargs else "table tr[id]"
        bipopup_css="div[id^='dt0_null_x__0'][class*='arMenu']"
        bipopups=self.driver.find_elements_by_css_selector(bipopup_css)
        menu_items=bipopups[len(bipopups)-1].find_elements_by_css_selector(temp_css)
        time.sleep(2)
        actual_popup_list=[el.text.strip() for el in menu_items  if bool(re.match('\S+', el.text.strip()))]
        print(actual_popup_list)
        utillobj.as_List_equal(expected_popup_list, actual_popup_list, kwargs['msg'] + " Verify bar tooltip.")    


if __name__ == '__main__':
    unittest.main()