'''
Created on Aug 23, 2016

@author: Gobizen

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053780
TestCase Name = Verify Group By option adds column on x-axis
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.pages import active_miscelaneous, visualization_resultarea
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators

class C2053780_TestClass(BaseTestCase):

    def test_C2053780(self):
        
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
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01: Verify Page summary')
        
        """Step 02:Select State > Chart > Pie > Category"""
        
        active_misobj.select_menu_items('ITableData0', 3, 'Chart','Pie','Category')
        time.sleep(5)
        
        #Verify that 'State By Product' pop up window for the chart is displayed.
        
        active_misobj.verify_popup_title('wall1', 'State by Category', 'Step 02: Verify that State By Product pop up window for the chart is displayed')
        
  
        """Step 03: Click New icon (dropdown) > Group By (X) > Product"""
        
#         rollupobj.create_new_item(0, 'Group By (X)->Product')
        act_obj.create_new_item('wall1', 'Group By (X)->Product')
        time.sleep(5)
#       Verify horizontal sort field 'Product' column has been added to the chart.
#       Chart title changes to 'State by Category, Product'. See attached screenshot.

        expected= 'State by Category, Product'
        title = driver.find_element_by_css_selector(ActiveMiscelaneousLocators.chart_tool_title_inner.format('1')).text
        s =   title.strip()  
        s1 = s==expected
        utillobj.asequal(True, s1,'Step 03: Chart title changes to State by Category, Product')
        
        
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos'], "Step 03.1: Verify Chart piebevel Legends for Top 5")
        
        #Color
#         active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['Coffee/Capuccino','State: 8','7.5% of 107'],"Step 04.3: Verify Chart piebevel tooltip for Unit Sales")
        time.sleep(5)
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 04.4: Verify Chart piebevel Color ")


if __name__ == '__main__':
    unittest.main()