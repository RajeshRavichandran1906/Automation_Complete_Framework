'''
Created on Aug 1, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050535
Test case Name = Verify Pivot Table status for problem - Filter/Equals options are not accessible.
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_chart_rollup, visualization_resultarea
from common.lib import utillity
import unittest,time
from pywinauto.uia_element_info import elements_from_uia_array

class C2050535_TestClass(BaseTestCase):

    def test_C2050535(self):
    
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)  
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step 01: Execute AR-RP-196.fex for the report that drives the Chart/Column and Scatter graphs.
        """
        utillobj.active_run_fex_api_login("AR-RP-196.fex", "S7068", 'mrid', 'mrpass')
        active_misobj.verify_page_summary(0, '10of10records,Page1of1', "Step 01.01: Execute AR-RP-196.fex verify Page Summary 2000of2000")
        
        column=['Category', 'Product ID', 'Product', 'Unit Sales', 'Dollar Sales']
        active_misobj.verify_column_heading('ITableData0',column, "Step 01.02: Expect to see a 10 row report, sorted by Category, Product ID and Product.")
        
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-196.xlsx', "Step 01.03: Expect to see a 10 row report, sorted by Category, Product ID and Product. data set")
        
        #utillobj.create_data_set('ITableData0','I0r','AR-RP-196.xlsx')
        
        """
        Step 02:Run an Active report, click drop down arrow next to Unit Sales column and select Rollup > Product     
        """
        active_misobj.select_menu_items('ITableData0', 3, 'Rollup','Product')
        
        time.sleep(5)
        
        utillobj.verify_popup_data_set('wall1','ITableData1','C2050535_Ds01.xlsx', "Step 02.01: Expect to see a 10 row report, sorted by Product. data set")
        
        #utillobj.create_popup_data_set('wall1','ITableData1','C2050535_Ds01.xlsx')
        
      
        
        """Step 03: In the Roll up table, click the Pie button."""
        
        #Expect to see the Rollup report converted to a PIE chart.
        
        rollupobj.click_chart_menu_bar_items('wall1', 2)
        time.sleep(5)
        
        #Tooltip & Color
        #['Biscotti', 'Unit Sales: 421K', '11.4% of 3.7M']
#         active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['Biscotti', 'Unit Sales: 421K', '11.4% of 3.7M'],"Step 03.01: Verify Chart piebevel tooltip for Unit Sales")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 03.01: Verify the bar riser First Pie Chart Color ")
        time.sleep(5)
        
        #Pie Label
        resobj.verify_riser_pie_labels_and_legends('wall1', ['Unit Sales'],"Step 03.02: Verify Chart pie Label & Legend")
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos'], "Step 03.03: Verify Chart piebevel Legends")
        #Title
        active_misobj.verify_popup_title('wall1', 'Unit Sales by Product', 'Step 03.04: Verify the dialog title')
        #Menu
        rollupobj.verify_arChartMenu('wall1',"Step 03.05: Verify the chart Menu")
        time.sleep(6)
    
        """Step 04: In the Pie chart, no percentage of total shows up.
        Expect to see Percentages on each slice of the PIE."""
        
        elements = self.driver.find_elements_by_css_selector("#wall1 .chartPanel  text[class*='data']")
        actual_percentages_list = [element.text for element in elements]
        expected_percentages_list = ['11%', '5%', '5%', '5%', '17%', '8%', '24%', '10%', '9%', '5%']
        utillobj.asequal(actual_percentages_list, expected_percentages_list, 'Step 4.01: Percentages on each slice of the PIE')

if __name__ == '__main__':
    unittest.main()     