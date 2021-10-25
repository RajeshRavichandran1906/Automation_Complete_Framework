'''
Created on November 24, 2017

@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234985
TestCase Name =Scatter diagram from Compound Report - Cache=OFF, Cachemode=n/a, Preview=ON
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,ia_run, active_miscelaneous,visualization_run
from common.lib import utillity

class C2234985_TestClass(BaseTestCase):

    def test_C2234985(self):
        
        TestCase_ID='C2234985'
        utillobj = utillity.UtillityMethods(self.driver)
        visurun=visualization_run.Visualization_Run(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        iarun=ia_run.IA_Run(self.driver)
          
        """ 
        Step 01 : Execute the attached repro - IA-2969G.
        """
        utillobj.active_run_fex_api_login('IA-2969G.fex', 'S7074', 'mrid', 'mrpass')
        result_obj.wait_for_property("#MAINTABLE_wbody1_f text[class^='xaxisNumeric-title']",1,30,string_value='Net Sales')
        time.sleep(2)
        
        """
        Step 01.1 :    Expect to see the following scatter diagram, with only Preview points.
                This is equivalent to the Preview pane in InfoAssist.
        """
        result_obj.verify_xaxis_title('MAINTABLE_wbody1_f','Net Sales','Step 01.1 : Verify X-Axis title')
        result_obj.verify_yaxis_title('MAINTABLE_wbody1_f','LAST_CONTACT','Step 01.2 : Verify Y-Axis title')
        expected_xaxis_labels=['0','2','4','6','8','10','12']
        expected_yaxis_labels=['0','2','4','6','8','10','12']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f',expected_xaxis_labels, expected_yaxis_labels,'Step 01.3 :')
        result_obj.verify_number_of_circle('MAINTABLE_wbody1_f',1,11,'Step 01.4 : Verify number of circles')
        expected_tooltip=['Net Sales:  6.0', 'LAST_CONTACT:  6', 'Company Name:  Fxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'Transactions:  6', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody1_f','riser!s0!g5!mmarker!',expected_tooltip,'Step 01.5 : Verify circle tooltip')
        screenshot_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_fmg")
        utillobj.take_screenshot(screenshot_element,TestCase_ID+'_Actual_step 01','actual')
        
        """
        Step 02 :Convert the scatter diagram into a report by clicking on the arrow in the bottom right corner, then selecting the first icon for report.
        """
        visurun.select_run_menu_option('MAINTABLE_menuContainer1','show_report')
        result_obj.wait_for_property("#MAINTABLE_wbody2 table[class='arPivot'] table tr:nth-child(1)>td:nth-child(1)>span",1,20,strig_value='Company Name')
        
        """
        Step 02.1 : Expect to see the preview points displayed as generic values in the report.
        """
        #iarun.create_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table", TestCase_ID+'_DataSet_01.xlsx')
        iarun.verify_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table",TestCase_ID+'_DataSet_01.xlsx','Step 02.1 : Verify Expect to see the preview points displayed as generic values in the report.')
        
if __name__=='__main__' :
    unittest.main()