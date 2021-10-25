'''
Created on November 24, 2017

@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234986
TestCase Name = RScatter diagram from Compound Report - Cache=OFF, Cachemode=n/a, Preview=OFF
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,ia_run,visualization_run
from common.lib import utillity

class C2234986_TestClass(BaseTestCase):

    def test_C2234986(self):
        
        TestCase_ID='C2234986'
        utillobj = utillity.UtillityMethods(self.driver)
        visurun=visualization_run.Visualization_Run(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iarun=ia_run.IA_Run(self.driver)
          
        """ 
        Step 01 : Execute the attached repro - IA-2969H.

        """
        utillobj.active_run_fex_api_login('IA-2969H.fex', 'S7074', 'mrid', 'mrpass')
        result_obj.wait_for_property("#MAINTABLE_wbody1_f text[class^='xaxisNumeric-title']",1,30,string_value='Net Sales')
        time.sleep(2)
        
        """
        Step 01.1 : Expect to see the following Scatter diagram, containing all points.
        """
        result_obj.verify_xaxis_title('MAINTABLE_wbody1_f','Net Sales','Step 01.1 : Verify X-Axis title')
        result_obj.verify_yaxis_title('MAINTABLE_wbody1_f','LAST_CONTACT','Step 01.2 : Verify Y-Axis title')
        expected_xaxis_labels=['0','40K','80K','120K','160K','200K','240K','280K']
        expected_yaxis_labels=['0','10','20','30','40','50','60','70','80']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f',expected_xaxis_labels, expected_yaxis_labels,'Step 01.3 :')
        result_obj.verify_number_of_circle('MAINTABLE_wbody1_f',1,1993,'Step 01.4 : Verify number of circles')
        utillobj.verify_chart_color("MAINTABLE_wbody1_f", "riser!s0!g1511!mmarker!", "royal_blue", "Step 01.05: Verify  riser color",attribute_type='stroke')
        screenshot_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_fmg")
        utillobj.take_screenshot(screenshot_element,TestCase_ID+'_Actual_step 01','actual')
        
        """
        Step 02 :HHover over the point just above the 160k value on the X=axis, to verify the four fields participating.
        Expect to see the four fields for the point:
        Net Sales: 166,000.00
        LAST_CONTACT: 6
        Company Name: Colorado Springs Utilities
        Transactions: 3
        """
        
        expected_tooltip_list=['Net Sales:166,000.0', 'LAST_CONTACT:6', 'Company Name:Colorado Springs Utilities', 'Transactions:3', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values("MAINTABLE_wbody1_f", "riser!s0!g442!mmarker!", expected_tooltip_list, "Step 02.1: Verify bar value")
         
        """
        Step 03 :Convert the scatter diagram into a report by clicking on the arrow in the bottom right corner, then selecting the first icon for report.

        """
        visurun.select_run_menu_option('MAINTABLE_menuContainer1','show_report')
        result_obj.wait_for_property("#MAINTABLE_wbody2 table[class='arPivot'] table tr:nth-child(1)>td:nth-child(1)>span",1,20,strig_value='Company Name')
        
        """
        Step 03.1 : Expect to see the following first page of the report.
        """
        before_scroll=self.driver.find_element_by_css_selector("#MAINTABLE_wbody2 table[class='arPivot'] table>tbody>tr:nth-child(1993)").location['y']
#         iarun.create_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table", TestCase_ID+'_DataSet_01.xlsx',desired_no_of_rows=100)
        iarun.verify_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table",TestCase_ID+'_DataSet_01.xlsx','Step 03.1 : Verify Expect to see the following first page of the report.',desired_no_of_rows=100)
        
        """
        Step 04 : Scroll all the way to the bottom of the report.
        """
        utillobj.mouse_scroll('down',490)
        time.sleep(4)
        
        """
        Step 04.1 : Expect to see Company names with first letters of Y and Z, followed by lower case names.
        """
        after_scroll=self.driver.find_element_by_css_selector("#MAINTABLE_wbody2 table[class='arPivot'] table>tbody>tr:nth-child(1993)").location['y']
        utillobj.as_LE(after_scroll,before_scroll,'Step 04.1 : Verify page scrolled to bottom')
#         iarun.create_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table", TestCase_ID+'_DataSet_02.xlsx',starting_rownum=1943)
        iarun.verify_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table",TestCase_ID+'_DataSet_02.xlsx','Step 04.2 : Verify Expect to see Company names with first letters of Y and Z, followed by lower case names.',starting_rownum=1943)
        
if __name__=='__main__' :
    unittest.main()
