'''
Created on Aug 19, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050533
Description : Graph axis label overlaid after Chart type change.
Original test AR-RP-195.
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.pages.active_chart_rollup import Active_Chart_Rollup
from common.lib import utillity
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
import re
 

class C2050533_TestClass(BaseTestCase):

    def test_C2050533(self):
        """
            Step 01: Execute AR-RP-195 for the report that drives the Chart/Column and Scatter graphs.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        active_rollup = Active_Chart_Rollup(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-195.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(8)
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Expect to see a 1000 row report with Order Number INTEGER as the first and sort column.")
        
        
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-195_Page1.xlsx',"Step 01: Verify table loaded data correctly table")
        
        
        """Step 02 : For field Order Number INTEGER, select Chart/Bar or Column and select Date YYMD as the Group By field. """
        
        miscelanousobj.select_menu_items("ITableData0", "0", "Chart","Column", "Date YYMD")
        time.sleep(8)
        #Expect to see a proper Bar Chart with 6 bars and correct axis label information underneath.
        
        element = driver.find_element(*ActiveMiscelaneousLocators.active_chart_container)
        
        utillobj.take_screenshot(element,'C2050533_Actual_Step02', image_type='actual')
        
        
        actual_bar_val_list=[]
        expected_bar_val_list=['1996/01/01:16290', '1996/02/01:48690', '1996/03/01:81090', '1996/04/01:113490', '1996/05/01:145890', '1996/06/01:95050']
        for i in range (0,6):
            bar_level_css="#Pie1 > div > div:nth-child(" + str(i*2+3) + ")"
            bar_val_css="#Pie1 > div > div[style*='background']:nth-child(" + str(30+i) + ")"
            bar_level=driver.find_element_by_css_selector(bar_level_css).get_attribute("title")
            try:
                val=re.match(r'Order Number INTEGER = (.*)', driver.find_element_by_css_selector(bar_val_css).get_attribute("title"))
                bar_val=val.group(1)
            except NoSuchElementException:
                bar_val='Null'
            actual_bar_val_list.append(bar_level + ":" + bar_val)
        utillity.UtillityMethods.asequal(self,actual_bar_val_list, expected_bar_val_list,'Step 02.a:Expect to see a proper Bar Chart with 6 bars and correct axis label information underneath.')
        
        
        
        
        """Step 03: In the Bar Chart, select Scatter, the fifth icon in the toolbar. """
        
        active_rollup.click_chart_menu_bar_items('wall1', 4)
        
        #Expect to see a correct Scatter Diagram with six points. 
        time.sleep(5)
        element=driver.find_element_by_css_selector("#wall1 div[class='chartContainer']")
        #element = driver.find_element(*ActiveMiscelaneousLocators.active_chart_container)
        utillobj.take_screenshot(element,'C2050533_Actual_Step03', image_type='actual')
        
        #miscelanousobj.select_menu_items('ITableData0', "0", "Global Filter")
        time.sleep(4)

        """ Step 04: Exit the Scatter Diagram."""
       
        #Expect to see the original report from step 1. 
        
        time.sleep(6)
        
        filterselectionobj.close_filter_dialog('wall1')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of1', "Step 04: Expect to see a 1000 row report with Order Number INTEGER as the first and sort column.")
        
        
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-195_Page1.xlsx',"Step 04: Verify table loaded data correctly table")
         
        
        
        
        """Step 05:For field Order Number INTEGER, select Chart/Bar and select ALPHA Store Code as the Group By field. """
         
        
        #Expect to see a proper Bar Chart with 12 Bars and correct axis labels below.
        miscelanousobj.select_menu_items("ITableData0", "0", "Chart","Column", "ALPHA Store Code")
        time.sleep(8)

        actual_bar_val_list1=[]
        expected_bar_val_list=['R1019:41220', 'R1020:42570', 'R1040:42975', 'R1041:45255', 'R1044:46605', 'R1088:47955', 'R1100:45295', 'R1109:35475', 'R1200:36600', 'R1244:37725', 'R1248:38850', 'R1250:39975']
        for i in range (0,12):
            bar_level_css="#Pie1 > div > div:nth-child(" + str(i*2+3) + ")"
            bar_val_css="#Pie1 > div > div[style*='background']:nth-child(" + str(45+i) + ")"
            bar_level=driver.find_element_by_css_selector(bar_level_css).get_attribute("title")
            try:
                val=re.match(r'Order Number INTEGER = (.*)', driver.find_element_by_css_selector(bar_val_css).get_attribute("title"))
                bar_val=val.group(1)
            except NoSuchElementException:
                bar_val='Null'
            actual_bar_val_list1.append(bar_level + ":" + bar_val)
        
        utillity.UtillityMethods.asequal(self,actual_bar_val_list1, expected_bar_val_list,'Step 05.a:Expect to see a proper Bar Chart with 12 Bars and correct axis labels below.')
        
        element = driver.find_element(*ActiveMiscelaneousLocators.active_chart_container)
        
        utillobj.take_screenshot(element,'C2050533_Actual_Step05', image_type='actual') 
        
      

        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        