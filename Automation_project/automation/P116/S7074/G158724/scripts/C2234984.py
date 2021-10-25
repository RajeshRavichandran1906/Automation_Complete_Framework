'''
Created on Nov 24, 2017

@author: Pavithra 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234984
TestCase Name = Scatter diagram from Compound Report - Cache=ON, Cachemode=not set, Preview=OFF, IF test
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,ia_run,visualization_run,ia_resultarea
from common.lib import utillity

class C2234984_TestClass(BaseTestCase):

    def test_C2234984(self):
        
        TestCase_ID='C2234984'
        utillobj = utillity.UtillityMethods(self.driver)
        Visual_run=visualization_run.Visualization_Run(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
  
        """ 
            Step 01:Execute the attached repro - IA-2969F.
                    
                    Expect to see the following scatter diagram, containing only points for Companies that pass any IF/WHERE test(s) in the repro.
        """
        utillobj.active_run_fex_api_login('IA-2969F.fex', 'S7074', 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody1_f text[class^='xaxisNumeric-title']"
        resobj.wait_for_property(parent_css, 1, string_value='NetSales', with_regular_exprestion=True, expire_time=20)
        time.sleep(2)
        resobj.verify_xaxis_title('MAINTABLE_wbody1_f','Net Sales','Step 01.01 : Verify X-Axis title')
        resobj.verify_yaxis_title('MAINTABLE_wbody1_f','LAST_CONTACT','Step 01.02 : Verify Y-Axis title')
        expected_xaxis_labels=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        expected_yaxis_labels=['0', '10', '20', '30', '40', '50', '60', '70']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f',expected_xaxis_labels, expected_yaxis_labels,'Step 01.03 :')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody1_f', 68, 'Step 01.04 : Expect to see the Series Selection set to Scatter.', custom_css="g [class*= 'marker'] circle")
        screenshot_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_fmg")
        utillobj.take_screenshot(screenshot_element,TestCase_ID+'_Actual_step 01','actual')

        """
            Step 02:Hover over several points to verify that the Company Names begin with 'G'.
                    Lastly hover over the bottom left point.

                Expect to see the four fields for the point:
                Net Sales: 4,500.00
                LAST_CONTACT: 2
                Company Name: Gander Mountain Company
                Transactions: 1
        """
        expected_tooltip = ['Net Sales:4,500.0', 'LAST_CONTACT:2', 'Company Name:Gander Mountain Company', 'Transactions:1', 'Filter Chart', 'Exclude from Chart']
#         expected_tooltip=['Net Sales:4500.0', 'LAST_CONTACT:2', 'Company Name:Gander Mountain Company', 'Transactions:1', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g9!mmarker!', expected_tooltip, 'Step 02.01 : Verify circle tooltip')
        time.sleep(6)

        """
            Step 03:Convert the scatter diagram into a report by clicking on the arrow in the bottom right corner, then selecting the first icon for report.
                    Expect to see the following first page of the report.
                    All Company Names should begin with 'G'.
        """
        Visual_run.select_run_menu_option('MAINTABLE_menuContainer1','show_report')
        parent_css="table[class='arPivot'] table tr:nth-child(1)>td:nth-child(1)>span"
        resobj.wait_for_property(parent_css, 1, string_value='CompanyName', with_regular_exprestion=True, expire_time=20)

        """
            Step 04:Scroll all the way to the bottom of the report.
                    Expect to see the following page, containing the last set of Company Names beginning with 'G'.
        """
        before_scroll=self.driver.find_element_by_css_selector("table[class='arPivot'] table>tbody>tr:nth-child(69) td").location['y']
        iarun.verify_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table",TestCase_ID+'_DataSet_Ds01.xlsx','Step 04.01 : Verify Expect to see the following first page of the report.')
        time.sleep(2)
        utillobj.mouse_scroll('down', 4)
        time.sleep(4)
        after_scroll=self.driver.find_element_by_css_selector("table[class='arPivot'] table>tbody>tr:nth-child(69) td").location['y']
        utillobj.as_LE(after_scroll,before_scroll,'Step 04.02 : Verify page scrolled to bottom')
        iarun.verify_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table",TestCase_ID+'_DataSet_Ds01.xlsx','Step 04.03 : Verify Expect to see last set of Company Names beginning with G') 
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()