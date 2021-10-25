'''
Created on Jul 14, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7067&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2071421
'''
import unittest, time
from selenium import webdriver
from common.pages import active_miscelaneous
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.keys import Keys


class C2071421_TestClass(BaseTestCase):

    def test_C2071421(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2071421'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 01: Sign to Webfocus using the below link.
        http://machine:port/ibi_apps
        Step 01 : Sign on screen will display. Login with valid credentials 
        Step 02 : Execute the attached Fex - act-562 using the below API URL 
        """
        utillobj.active_run_fex_api_login('act-562.fex', 'S7067', 'mrid', 'mrpass')
        utillobj.verify_data_set('ITableData0','I0r','C2055535_Ds01.xlsx',"Step 02: Expect to see the following multi-page Compound Report.Page 1 screen:.")
        time.sleep(5)
        miscelanousobj.verify_page_scroll('0', "no", "Step 02: Expect to see no scroll bars on Page 1.")
        """
        Step 03 : Click Page 2 in the Layout area at the top.
        """
        miscelanousobj.navigate_coordinate_report_page("2")
        time.sleep(4)
        miscelanousobj.verify_page_summary(1,'107of107records,Page1of2', "Step 03: Page 2 screen:Expect to see the first page of a two page report.")
        miscelanousobj.verify_page_scroll('1', "yes", "Step 03: Also expect to see both upward and downward arrows on the scroll bar.")
        time.sleep(4)
        """
        Step 04 : On the pagination bar at the top, click either arrow to go to page 2.
        """               
        miscelanousobj.navigate_page("next_page")
        miscelanousobj.verify_page_summary(1,'107of107records,Page2of2', "Step 04: Expect to see the second and last page of a two page report.")
        browser = utillity.UtillityMethods.parseinitfile(self, 'browser')
        if browser == 'IE':
            doc=driver.find_element_by_css_selector("#ITableData1 td:nth-child(1) td:nth-child(1)")
            doc_height1=doc.location['y']
            self.driver.find_element_by_css_selector("#ITableData1").send_keys(Keys.PAGE_DOWN)          
            doc1=driver.find_element_by_css_selector("#ITableData1 td:nth-child(1) td:nth-child(1)")
            doc_height2=doc1.location['y']
            print(doc_height1)
            print(doc_height2)
            utillity.UtillityMethods.as_GE(self,doc_height1,doc_height2,"Step 04:Also expect to see both upward and downward arrows on the scroll bar")
        else:
            miscelanousobj.verify_page_scroll('1', "yes", "Step 04: Also expect to see both upward and downward arrows on the scroll bar. .")

if __name__ == '__main__':
        unittest.main()        