'''
Created on Jan 30, 2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203731
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import ia_run
from common.lib import utillity

class C2203731_TestClass(BaseTestCase):

    def test_C2203731(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        """
        Step 01.Run HTMLCSS=ON.fex in IA.
        Verify report shows Country field as link with inserted URLs.
        """
        utillobj.active_run_fex_api_login("HTMLCSS-ON.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        ia_runobj.verify_table_data_set('table[border]', 'HTMLCSS-ON_Ds01.xlsx','Step 01.3: Expect to see the  Active Report')
        
        """
        Step02: Click any Country from the report
        """
        ia_runobj.select_and_verify_drilldown_report_field("table[border]", 3, 1, underline=True, msg='Step 02.1: Verify ENGLAND value is underlined')
        ia_runobj.select_and_verify_drilldown_report_field("table[border]", 3, 1, underline=True, msg='Step 02.1: Verify ENGLAND value is underlined')
        time.sleep(2)
        expected_tooltip_list=['Drilldown 1 - Yahoo', 'Drilldown 2 - CNN','Drilldown 3 - IBI']
        ia_runobj.verify_autolink_tooltip_values("table[border]",3,1, expected_tooltip_list, "Step 02.2: verify the default Autolink tooltip values list")
        
        """
        Step03: Click DrillDown 1 under ENGLAND.
        """
        ia_runobj.select_autolink_tooltip_menu("table[border]",3,1,'Drilldown 1 - Yahoo', "Step 03a: Select the menu Drilldown 1 - Yahoo")
        owebpage=driver.title
        utillobj.asin('Yahoo', owebpage, "Step03b: Verify Yahoo page is displayed")
        time.sleep(5)
        self.driver.back()
        time.sleep(3)
         
        """
        Step04: Click DrillDown 2 under ENGLAND.
        """
        ia_runobj.select_autolink_tooltip_menu("table[border]",3,1,'Drilldown 2 - CNN', "Step04a.: Select the menu Drilldown 2 - CNN")
        time.sleep(5)
        owebpage=driver.current_url
        utillobj.asin('cnn.com', owebpage, "Step04b: Verify CNN page is displayed")
        time.sleep(5)
        self.driver.back()
        time.sleep(3)
        
        """
        Step05: Click DrillDown 3 under ENGLAND.
        """
        ia_runobj.select_autolink_tooltip_menu("table[border]",3,1,'Drilldown 3 - IBI', "Step05a: Select the menu Drilldown 2 - CNN")
        time.sleep(5)
        owebpage=driver.current_url
        utillobj.asin('informationbuilders.com', owebpage, "Step05b: Verify IBI page is displayed")
        time.sleep(5)
        self.driver.back()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()