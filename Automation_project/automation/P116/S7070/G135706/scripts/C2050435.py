'''
Created on Aug 18, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050435
'''
import unittest
import re
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_chart_rollup
from common.lib import utillity
from selenium.common.exceptions import NoSuchElementException
import time
class C2050435_TestClass(BaseTestCase):

    def test_C2050435(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        chartrollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        """
        1. Execute attached repro 150608.
    
        Expect to see a four slice PIE chart with each Country represented except for France, which has zero value.
        Expect to see a legend entry for France underneath the PIE chart, showing 0% of total.
        Also expect the order of the slices to be W GERMANY, JAPAN, ITALY and ENGLAND, starting at 12:00 and proceeding clock-wise, reflecting the by HIGHEST SALES.
        """
        utillobj.active_run_fex_api_login("150608.fex", "S7070", 'mrid', 'mrpass')
        time.sleep(8)
        # taking screenshot for the image
        utillobj.take_screenshot(driver.find_element_by_css_selector("#MAINTABLE_wmenu0"),'C2050435_Actual_Pic01', image_type='actual')
        utillobj.take_screenshot(driver.find_element_by_css_selector("#MAINTABLE_wbody0"),'C2050435_Actual_Pic02', image_type='actual')
        
        expected_lgnds_list=['W GERMANY 42.3%', 'JAPAN 37.4%', 'ITALY 14.5%', 'ENGLAND 5.8%', 'FRANCE 0%', 'SALES by COUNTRY']
        raiser_css = "#MAINTABLE_0 div[style*='left'][style*='text-align']"
        lgnds = driver.find_elements_by_css_selector(raiser_css)
        actual_lgnds_list=[]
         
        actual_lgnds_list.extend([t.text.strip() for t in lgnds])
          
        utillity.UtillityMethods.asequal(self,actual_lgnds_list, expected_lgnds_list,'Step 01.a: Expect to see a legend entry for France underneath the PIE chart, showing 0% of total')
        
        driver.implicitly_wait(1)
        expected_pie_list = ['W GERMANY = 88190 (42.3%)', 'JAPAN = 78030 (37.4%)', 'ITALY = 30200 (14.5%)', 'ENGLAND = 12000 (5.8%)', 'Null']
        actual_pie_list = []
        input_list=['W GERMANY', 'JAPAN', 'ITALY', 'ENGLAND', 'FRANCE']
        for i in range(len(input_list)):
            try:
                pie_slice="#MAINTABLE_0 div[title^='" + input_list[i] + " =']"
                pie_val=driver.find_element_by_css_selector(pie_slice).get_attribute("title")
                actual_pie_list.append(pie_val.strip())
            except NoSuchElementException:
                actual_pie_list.append('Null')
        utillity.UtillityMethods.asequal(self,actual_pie_list, expected_pie_list,'Step 01.b: Expect to see a four slice PIE chart with each Country represented except for France, which has zero value')   
        driver.implicitly_wait(45)    
        
        """
        2. To prove that France will participate in other graphs, click the Bar Chart icon at the top of the PIE Chart.

        Expect to see a 5 Bar graph with France showing zero value.
        """
        chartrollupobj.click_chart_menu_bar_items('MAINTABLE_0', 1)
        
        # taking screenshot for the image
        utillobj.take_screenshot(driver.find_element_by_css_selector("#MAINTABLE_wmenu0"),'C2050435_Actual_Pic01', image_type='actual')
        utillobj.take_screenshot(driver.find_element_by_css_selector("#MAINTABLE_wbody0"),'C2050435_Actual_Pic04', image_type='actual')

        driver.implicitly_wait(1)
        # verify 4 bars displayed on bar
        actual_bar_val_list=[]
        expected_bar_val_list=['W GERMANY:88190', 'JAPAN:78030', 'ITALY:30200', 'ENGLAND:12000', 'FRANCE:Null']
        for i in range (0,5):
            bar_level_css="#Piet0 > div > div:nth-child(" + str(i*2+3) + ")"
            bar_val_css="#Piet0 > div > div[style*='background']:nth-child(" + str(31+i) + ")"
            bar_level=driver.find_element_by_css_selector(bar_level_css).get_attribute("title")
            try:
                val=re.match(r'SALES = (.*)', driver.find_element_by_css_selector(bar_val_css).get_attribute("title"))
                bar_val=val.group(1)
            except NoSuchElementException:
                bar_val='Null'
            actual_bar_val_list.append(bar_level + ":" + bar_val)
        utillity.UtillityMethods.asequal(self,actual_bar_val_list, expected_bar_val_list,'Step 02.a: Expect to see a 5 Bar graph with France showing zero value.')

        
if __name__ == '__main__':
    unittest.main()

