'''
Created on Sept'06

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053789
TestCase Name =Edit columns under Series tab and check results
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators

class C2157260_TestClass(BaseTestCase):

    def test_C2157260(self):
        
       
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
            Step 01: Execute the attached repro - act-534.fex
        """
        utillobj.active_run_fex_api_login('act-534.fex','S7074','mrid','mrpass')   
        riser_css = "#MAINTABLE_wbody0 circle[class*='riser']"   
        utillobj.synchronize_with_number_of_element(riser_css, 10, 30)      

        #Diagram with Unit Sales along the X-axis and Dollar Sales along the Y-axis.
        #The Dimension BY field is Product.
        
        x_axis = driver.find_element(*ActiveMiscelaneousLocators.xaxis_title).text
        y_axis = driver.find_element(*ActiveMiscelaneousLocators.yaxis_title).text 
        
        utillobj.asequal('Unit Sales', x_axis, 'Step 01.01: Unit Sales along the X-axis')
        utillobj.asequal('Dollar Sales', y_axis, 'Step 01.02: Dollar Sales displayed along the Y axis')
        
        
        #X annd Y axis Scales Values 
        
        expected_xval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_0', expected_xval_list, expected_yval_list, 'Step 01.03: X annd Y axis Scales Values')
          
        
        """Step 02:Hover over the data point in the extreme upper right."""
        #Expect to see the Scatter Diagram with Hover over values.
        #The Product displayed should be Latte.
        
        expected=['Unit Sales:  878063','Dollar Sales:  10943622','Product:  Latte','Filter Chart','Exclude from Chart']
        
        active_misobj.verify_active_chart_tooltip('MAINTABLE_0', 'riser!s0!g6',expected,"Step 02.01: Verify correct/selected chart tooltip value is displayed ")
        utillobj.verify_chart_color('MAINTABLE_0', None ,'bar_blue1',"Step 02.02: Verify Chart piebevel Color ", attribute_type='stroke', custom_css="g[class='markers']>g")
        
        time.sleep(8)

        """Step 03: For the data point in the upper right, hover over and click Exclude from Chart."""
        #Expect to see the Scatter Diagram with Hover over values.
        #Notice that the scales for both the X-axis and Y-axis have changed, after Latte was removed.
        resobj.select_default_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g6!mmarker', 'Exclude from Chart')
         
        time.sleep(6)
        """Step 04:Hover over the data point in the extreme upper right."""
        #Expect to see the Scatter Diagram with Hover over values.
        #Also expect to see that the upper right data point is now displayed as Croissant.
        
        
        expected_xval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03.01: X annd Y axis Scales Values has changed or NOT')
        
        expected1=['Unit Sales:  630054', 'Dollar Sales:  7749902', 'Product:  Croissant', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        
        active_misobj.verify_active_chart_tooltip('MAINTABLE_0', 'riser!s0!g4',expected1,"Step 03.02: Verify correct/selected chart tooltip value is displayed ")
        utillobj.verify_chart_color('MAINTABLE_0', None ,'bar_blue1',"Step 03.03: Verify Chart piebevel Color",attribute_type='stroke', custom_css="g[class='markers']>g")
        

if __name__ == '__main__':
    unittest.main()