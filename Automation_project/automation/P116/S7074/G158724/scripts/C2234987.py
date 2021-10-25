'''
Created on Nov 27, 2017

@author: Pavithra 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234987
TestCase Name = Scatter diagram from Compound Report - Cache=OFF, Cachemode=n/a, Preview=OFF & IF test
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,ia_run,visualization_run,ia_resultarea
from common.lib import utillity

class C2234987_TestClass(BaseTestCase):

    def test_C2234987(self):
        
        TestCase_ID='C2234987'
        utillobj = utillity.UtillityMethods(self.driver)
        Visual_run=visualization_run.Visualization_Run(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """        
            Step 01:Execute the attached repro - IA-2969I.
                    
                    Expect to see the following scatter diagram.
        """
        utillobj.active_run_fex_api_login('IA-2969I.fex', 'S7074', 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody1_f text[class^='xaxisNumeric-title']"
        resobj.wait_for_property(parent_css, 1, string_value='NetSales', with_regular_exprestion=True, expire_time=20)
        time.sleep(2)
        resobj.verify_xaxis_title('MAINTABLE_wbody1_f','Net Sales','Step 01.1 : Verify X-Axis title')
        resobj.verify_yaxis_title('MAINTABLE_wbody1_f','LAST_CONTACT','Step 01.2 : Verify Y-Axis title')
        expected_xaxis_labels=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        expected_yaxis_labels=['0', '10', '20', '30', '40', '50', '60', '70']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f',expected_xaxis_labels, expected_yaxis_labels,'Step 01.3 :')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody1_f', 196, 'Step 03.e: Expect to see the Series Selection set to Scatter.', custom_css="g [class*= 'marker'] circle")
        screenshot_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_fmg")
        utillobj.take_screenshot(screenshot_element,TestCase_ID+'_Actual_step 01','actual')

        """
            Step 02:Hover the point just above and to the left of the 80k value on the X-=Axis.
                    
                Expect to see the following display of the four fields for this point:

                Net Sales: 65,760.0
                LAST_CONTACT: 3
                Company Name: T.Rowe Price Group, Inc.
                Transactions: 2
        """
        expected_tooltip=['Net Sales:65,760.0', 'LAST_CONTACT:3', 'Company Name:T. Rowe Price Group, Inc.', 'Transactions:2', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g0!mmarker!', expected_tooltip, 'Step 02.1 : Verify circle tooltip')
        time.sleep(6)

        """
            Step 03:Convert the scatter diagram into a report by clicking on the arrow in the bottom right corner, then selecting the first icon for report.
                    Expect to see the following first page of the report.All Company Names should begin with 'T'.
        """
        Visual_run.select_run_menu_option('MAINTABLE_menuContainer1','show_report')
        parent_css="table[class='arPivot'] table tr:nth-child(1)>td:nth-child(1)>span"
        resobj.wait_for_property(parent_css, 1, string_value='CompanyName', with_regular_exprestion=True, expire_time=20)


        """
            Step 04:Scroll all the way to the bottom of the report.
                    
                    Expect to see the following page, containing the last set of Company Names beginning with 'T'.
        """
        before_scroll=self.driver.find_element_by_css_selector("table[class='arPivot'] table>tbody>tr:nth-child(197) td").location['y']
#         iarun.create_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table",TestCase_ID+'_DataSet_Ds01.xlsx')
        iarun.verify_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table",TestCase_ID+'_DataSet_Ds01.xlsx','Step 04.1 : Verify Expect to see the following first page of the report.')
        time.sleep(2)
        utillobj.mouse_scroll('down', 60)
        time.sleep(4)
        after_scroll=self.driver.find_element_by_css_selector("table[class='arPivot'] table>tbody>tr:nth-child(197) td").location['y']
        utillobj.as_LE(after_scroll,before_scroll,'Step 04.2 : Verify page scrolled to bottom')
        iarun.verify_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table",TestCase_ID+'_DataSet_Ds01.xlsx','Step 04.3 : Verify Expect to see last set of Company Names beginning with T') 
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


