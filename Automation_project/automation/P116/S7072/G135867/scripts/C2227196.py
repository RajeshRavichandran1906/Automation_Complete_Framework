'''
Created on April 24, 2017

@author: khan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227196
Description = AHTML: Context Menu: Cascading Multidrill Integration (ACT-348)-Manual
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, ia_run, visualization_resultarea
from common.lib import utillity
import unittest, time



class C2227196_TestClass(BaseTestCase):

    def test_C2227196(self):
        
        driver = self.driver #Driver reference object created'
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscellaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        iarunobj = ia_run.IA_Run(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        browser=utillobj.parseinitfile('browser')
        
        """ Step 1: Execute the attached repro - ACT_161Updated.fex.
                    There should be a column (DEALER_COST, title not displayed) containing hyperlinks.
        """
        utillobj.active_run_fex_api_login("ACT_161Updated.fex", "S7072", 'mrid', 'mrpass')
        utillobj.wait_for_page_loads(10)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(1)
        miscellaneousobj.verify_page_summary(0, '5of5records,Page1of1', 'Step 01.01: Verify the Report Heading')
#         iarunobj.create_table_data_set('table#ITableData0', 'C2227196_Ds01.xlsx')
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        result_obj.wait_for_property(parent_css, 1, string_value='37,853', with_regular_exprestion=True)
        iarunobj.verify_table_data_set('table#ITableData0', 'C2227196_Ds01.xlsx', 'Step 01.02: Verify data set')
        time.sleep(2)


        """ Step 2: Select the first hyperlink (37,853) by hovering the mouse pointer over it or selecting it with the tab key.
                    The URL of the hyperlink should appear at the bottom of the browser, as
                    http://www.informationbuilders.com?SEARCH=ENGLAND?
                    (Explorer).
        """
        #expected_href='http://www.informationbuilders.com/&SEARCH=ENGLAND&'
        
        if browser == 'IE':
            iarunobj.verify_autolink('table#ITableData0', '37,853', 2, 1, 5, "Step 02.", color_name='navy_blue')
        else:
            iarunobj.verify_autolink('table#ITableData0', '37,853', 2, 1, 5, "Step 02.", color_name='hyperlink_blue')
        time.sleep(2)
        
        
        """ Step 3: (Optional) Activate the hyperlink with the left mouse button or the Enter key. This may not be suitable in automation because the URL target will change as time goes on.
                    The Information Builders main home page should appear.
        """
        
        iarunobj.select_and_verify_drilldown_report_field('table#ITableData0', 2, 1)
        utillobj.wait_for_page_loads(10)
        time.sleep(10)
        utillobj.switch_to_window(0,window_title='Business')
        
        expected='Data and Analytics Company | ibi'
        actual=driver.title
        utillobj.asequal(expected, actual,"Step  03.01: verify title Information Builders")
        
        
        """ Step 4: Close the Information Builders home page.
        """
        time.sleep(5)
        
        
        
if __name__ == '__main__':
    unittest.main()  