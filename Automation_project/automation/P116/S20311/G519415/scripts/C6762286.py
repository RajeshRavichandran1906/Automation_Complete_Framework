'''
Created on Jan 8, 2019

@author: Vpriya

Testsuite =  http://172.19.2.180/testrail/index.php?/suites/view/20311&group_by=cases:section_id&group_id=519415&group_order=asc
Testcase id=http://172.19.2.180/testrail/index.php?/cases/view/6762286
TestCase Name = AHTML:negative color is not applied in visualized column(127568)
'''
import unittest, time
from common.lib import utillity
from common.wftools import report
from common.wftools import active_report
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.color import Color
from selenium.common.exceptions import NoSuchElementException

class C6762286_TestClass(BaseTestCase):

    def test_C6762286(self):
        
        """
            TESTCASE VARIABLES
        """
        fex_name='127568'
        Testcase_ID="C6762286"
        folder_name='P116_S20311/G519415'
        
        """
            TESTCASE Objects
        """
        report_obj=report.Report(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        active_report_obj=active_report.Active_Report(self.driver)
        
        """
        Step 01:Execute the attached repro - 127568.fex.
        """
        report_obj.run_fex_using_api_url(folder_name, fex_name, 'mrid', 'mrpass',run_table_css='#ITableData0',wait_time=60)
       
        """
        Step 02:Click on test column and locate the Visualize option.
        """
        active_report_obj.select_menu_items("ITableData0", 1,'Visualize')
        time.sleep(2)
        #active_report_obj.create_active_report_dataset(Testcase_ID+"DS_01.xlsx")
        active_report_obj.verify_active_report_dataset(Testcase_ID+"DS_01.xlsx",table_css="#ITableData0",msg="Step 02.01: Verify data of the table")
        
        """
        Step 03:click the Visualize option.
        Expect to see visualization for negative numbers to be in Red and the bars pointing to the left. The positive bars point to the right.
        """
        
        rows1=self.driver.find_elements_by_css_selector('#ITableData0 >tbody >tr > td:nth-child(3) > table > tbody > tr > td:nth-child(1)')
        left_allign_count=0
        for left_alligned_item in rows1:     
            try:
                obj=left_alligned_item.find_element_by_css_selector('table >tbody > tr >td')
                left_allign_count = left_allign_count + 1    
            except NoSuchElementException:        
                continue
        
        actual_color = Color.from_string(utill_obj.get_element_css_propery(obj, 'background-color')).rgba
        expected_color = utill_obj.color_picker('dark_red3', 'rgba')
        utill_obj.asequal(actual_color, expected_color, 'Step 03.01: Verify the negative coloured riser')
        utill_obj.asequal(left_allign_count,5,"Step 03.02: Verify visualization alignment")
        rows2=self.driver.find_elements_by_css_selector('#ITableData0 >tbody >tr > td:nth-child(3) > table > tbody > tr > td:nth-child(3)')
        right_allign_count=0
        for right_alligned_item in rows2:
            try:       
                obj=right_alligned_item.find_element_by_css_selector('table >tbody > tr >td')
                right_allign_count = right_allign_count + 1
            except NoSuchElementException:        
                continue
        
        utill_obj.asequal(right_allign_count,13,"Step 03.03: Verify visualization right alignment")
        actual_color = Color.from_string(utill_obj.get_element_css_propery(obj, 'background-color')).rgba
        expected_color = utill_obj.color_picker('muscyane_blue', 'rgba')
        utill_obj.asequal(actual_color, expected_color, 'Step 03.04: Verify the negative coloured riser')

if __name__ == '__main__':
    unittest.main()