'''
Created on Aug 23, 2016

@author: Gobizen

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053781
TestCase Name = Verify Add option adds column to y-axis
'''
import unittest, time 
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.pages import active_miscelaneous, visualization_resultarea
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators

class C2053781_TestClass(BaseTestCase):

    def test_C2053781(self):
        
        """
            Class Objects
        """
        driver = self.driver #Driver reference object created
        act_obj = Active_Chart(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
            Step 01: Execute the AR-RP-001.fex
        """        
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7074','mrid','mrpass')      
        time.sleep(8)      
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01.01: Verify Page summary')
        
        """Step 02:Select State > Chart > Pie > Category"""
        
        active_misobj.select_menu_items('ITableData0', 3, 'Chart','Pie','Category')
        time.sleep(5)
        
        #Verify that 'State By Product' pop up window for the chart is displayed.
        
        active_misobj.verify_popup_title('wall1', 'State by Category', 'Step 02.01: Verify that State By Product pop up window for the chart is displayed')
      
        """Step 03: Click New icon (dropdown) > Add (Y) > Product ID"""
        
#         rollupobj.create_new_item(0, 'Add (Y)->Product ID')
        act_obj.create_new_item('wall1', 'Add (Y)->Product ID')
        time.sleep(5)
        #Verify vertical sort field 'Product ID' has been added to the chart.
        #Chart title changes to 'Product ID by Category'. See attached screenshot.
        
        expected= 'Product ID by Category'
        title = driver.find_element_by_css_selector(ActiveMiscelaneousLocators.chart_tool_title_inner.format('1')).text
        s =   title.strip()  
        s1 = s==expected
        utillobj.asequal(True,s1,'Step 03.01:Chart title changes to Product ID by Category') 
        
        #Pie Legend
        resobj.verify_riser_legends('wall1',  ['Coffee', 'Food', 'Gifts'], "Step 03.02: Verify Chart piebevel Legends for Top 5")
        
        #Tooltip & Color
        active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['Coffee','Product ID: 30','28.0% of 107'], "Step 03.03: Verify Chart piebevel tooltip for Unit Sales")
        time.sleep(5)
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 03.04: Verify Chart piebevel Color ")

if __name__ == '__main__':
    unittest.main()