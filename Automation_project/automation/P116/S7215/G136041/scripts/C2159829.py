'''
Created on Sep 20, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2159829
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea
from common.lib import utillity

class C2159829_TestClass(BaseTestCase):

    def test_C2159829(self):
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resobj= visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step 01. Execute the attached repro - act-195.fex
        Expect to see the following Active Bar Chart.
        The second Bar in each Country/Car pair represents a redefined Dealer_Cost field using format P6.2.
        P6.2 has a maximum display of 999.99.
        """
        utillobj.active_run_fex_api_login("act-195.fex", "S7215", 'mrid', 'mrpass')
        #screenshot
        time.sleep(15)
        element = self.driver.find_element_by_css_selector("#MAINTABLE_wbody0_fmg")
        utillobj.take_screenshot(element, 'C2159829_Actual_Step01', image_type='actual_images')
        #Tooltip & Color
        time.sleep(10)
        active_misobj.verify_active_chart_tooltip('MAINTABLE_0',"riser!s0!g0!mbar!",['RETAIL_COST, ENGLAND/JAGUAR: 22,369'],"Step 01.1a: Verify Chart tooltip RETAIL_COST")
        utillobj.verify_chart_color('MAINTABLE_0',"riser!s0!g0!mbar!",'cerulean_blue',"Step 01.1a: Verify Chart color RETAIL_COST")
        time.sleep(5)
        #Label
        x=['ENGLAND/JAGUAR', 'ENGLAND/JENSEN', 'ENGLAND/TRIUMPH']
        y=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_0', x, y, "Step 01.c Verify Chart XY labels")
        #Chart Title
        active_misobj.verify_chart_title('MAINTABLE_wbody0_ft', 'RETAIL_COST, P6.2 Dcost by COUNTRY, CAR', 'Step 01.d: Verify Chart Title')
        #Legends
        resobj.verify_riser_legends('MAINTABLE_0', ['RETAIL_COST','P6.2 Dcost'],"Step 01.e: Verify Chart Legend")
        #X axis Title    
        resobj.verify_xaxis_title('MAINTABLE_wbody0_f', 'COUNTRY : CAR', 'Step 01.f: Verify xaxis Title')        
        #archartToolbar
        active_misobj.verify_arChartToolbar('MAINTABLE_0',['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 01.g: Verify Chart toolbar")
        """
        Step 02: Hover over the second bar for England/Jaguar.
        Expect to see the following hover-over values for England/Jaguar, with no overflow characters(*), even 
        though the value displayed exceeds 999.99.

        P6.2 Dcost, ENGLAND/JAGUAR: 18,621.00.
        """
        active_misobj.verify_active_chart_tooltip('MAINTABLE_0',"riser!s1!g0!mbar!",['P6.2 Dcost, ENGLAND/JAGUAR: 18,621.00'],"Step 02.1a: Verify Chart tooltip P6.2 Dcost")
        utillobj.verify_chart_color('MAINTABLE_0',"riser!s1!g0!mbar!",'gold_tips',"Step 02.1a: Verify Chart color P6.2 Dcost")
        time.sleep(5)
        
        
        
           
if __name__ == '__main__':
    unittest.main()            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            