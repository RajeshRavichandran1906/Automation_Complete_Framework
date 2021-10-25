'''
Created on Aug 18, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050430
'''
import unittest
import re
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_chart_rollup
from common.lib import utillity

class C2050430_TestClass(BaseTestCase):

    def test_C2050430(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        chartrollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        """
        1. Execute the attached repro - 163586.fex
        
        Expect to see the following Active Report.
        """
        utillobj.active_run_fex_api_login("163586.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', 'Step 01.1: Execute the attached repro - 163586.fex and Verify the Report Heading')
        column_list=['COUNTRY', 'RETAIL_COST', 'DEALER_COST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 163586.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050430_Ds01.xlsx', 'Step 01.3: Verify Report data for all required columns.')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2050430_Ds01.xlsx')
        
        
        """
        2. Click on dropdown for Retail_Cost and select chart>PIE>Country.
        
        Expect to see the following PIE chart.
        """
        miscelanousobj.select_menu_items('ITableData0', "1", "Chart","Pie","COUNTRY")
        # Expect to see the following PIE chart.
        utillobj.take_screenshot(driver.find_element_by_css_selector("#wall1"),'C2050430_Actual_Pic01', image_type='actual')
        
        # verify legends
        expected_lgnds_list=['ENGLAND 26.2%', 'FRANCE 3.2%', 'ITALY 29.5%', 'JAPAN 3.7%', 'W GERMANY', '37.4%', 'RETAIL_COST by COUNTRY']
        raiser_css = "#Pie1>div>div[style*='align'][style*='left']"
        lgnds = driver.find_elements_by_css_selector(raiser_css)
        actual_lgnds_list=[]
        
        for i in range(len(lgnds)):
            actual_lgnds_list.append((lgnds[i].text).strip())
        utillity.UtillityMethods.asequal(self,actual_lgnds_list, expected_lgnds_list,'Step 02.a: Expect to see a legend entry for the PIE chart')
        
        
        expected_pie_list = ['ENGLAND = 45319 (26.2%)', 'FRANCE = 5610 (3.2%)', 'ITALY = 51065 (29.5%)', 'JAPAN = 6478 (3.7%)', 'W GERMANY = 64732 (37.4%)']
        actual_pie_list = []
        input_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        #input_list=['W GERMANY', 'JAPAN', 'ITALY', 'ENGLAND', 'FRANCE']
        for i in range(len(input_list)):
            pie_slice="#Pie1>div>div[title^='" + input_list[i] + " =']"
            pie_val=driver.find_element_by_css_selector(pie_slice).get_attribute("title")
            actual_pie_list.append(pie_val.strip())
        utillity.UtillityMethods.asequal(self,actual_pie_list, expected_pie_list,'Step 02.b: Expect to see a five slice PIE chart with each Country represented')   
        
        """
        3. Now click on any pie slice, notice no error is thrown
        
        Expect to see the following information displayed for the PIE slice
        """
        expected_val=['ENGLAND = 45319 (26.2%)']
        actual_val=[]
        raiser_css="#Pie1>div>div[title^='ENGLAND =']"
        tooltips=driver.find_elements_by_css_selector(raiser_css)
        tooltips[round(len(tooltips)/2)].click()
        actual_val.append(tooltips[round(len(tooltips)/2)].get_attribute("title"))
        utillity.UtillityMethods.asequal(self,actual_val, expected_val,'Step 03.a: Expect to see a tooltip value for a slice in PIE chart')

        """
        4. From the tool bar, click on Line Chart
        
        Expect to see the following Line Chart.
        """
        chartrollupobj.click_chart_menu_bar_items('wall1', 3)
        # Expect to see the following LINE chart.
        utillobj.take_screenshot(driver.find_element_by_css_selector("#wall1"),'C2050430_Actual_Pic02', image_type='actual')
        
        expected_line_list=['ENGLAND:45319', 'FRANCE:5610', 'ITALY:51065', 'JAPAN:6478', 'W GERMANY:64732']
        line_val_list=[]
        
        for i in range (0,5):
            line_css="#Pie1>div>div:nth-child(" + str(i*2+3) + ")"
            line_val_css="#Pie1>div>div[style*='background']:nth-child(" + str(28+i) + ")"
            line_level=driver.find_element_by_css_selector(line_css).get_attribute("title")
            val=re.match(r'RETAIL_COST = (.*)', driver.find_element_by_css_selector(line_val_css).get_attribute("title"))
            line_rect=driver.find_element_by_css_selector(line_val_css).value_of_css_property("clip")
            clipx =bool(re.match(r'.*\s8px.*', line_rect))
            utillity.UtillityMethods.asequal(self,True, clipx,'Step 04.a: Expect to see a Line chart-riser '+str(i)+'')
            line_val=val.group(1)
            line_val_list.append(line_level + ":" + line_val)
            
         
        utillity.UtillityMethods.asequal(self,line_val_list, expected_line_list,'Step 04.a: Expect to see a Line chart')
        
        """
        5. From the tool bar, click on BAR Chart
        
        Expect to see the following BAR Chart.
        """
        chartrollupobj.click_chart_menu_bar_items('wall1', 1)
        # Expect to see the following BAR chart.
        utillobj.take_screenshot(driver.find_element_by_css_selector("#wall1"),'C2050430_Actual_Pic03', image_type='actual')
        
        expected_bar_list=['ENGLAND:45319', 'FRANCE:5610', 'ITALY:51065', 'JAPAN:6478', 'W GERMANY:64732']
        bar_val_list=[]
        for i in range (0,5):
            bar_level_css="#Pie1>div>div:nth-child(" + str(i*2+3) + ")"
            bar_val_css="#Pie1>div>div[style*='background']:nth-child(" + str(28+i) + ")"
            bar_level=driver.find_element_by_css_selector(bar_level_css).get_attribute("title")
            val=re.match(r'RETAIL_COST = (.*)', driver.find_element_by_css_selector(bar_val_css).get_attribute("title"))
            bar_val=val.group(1)
            bar_val_list.append(bar_level + ":" + bar_val)
        utillity.UtillityMethods.asequal(self,bar_val_list, expected_bar_list,'Step 05.a: Expect to see a BAR chart')       
        
        
if __name__ == '__main__':
    unittest.main()

