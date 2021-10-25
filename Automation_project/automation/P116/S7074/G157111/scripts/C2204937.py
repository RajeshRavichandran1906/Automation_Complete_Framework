'''
Created on Jul 04, 2017
@author: Nasir
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, active_chart_rollup
from common.lib import utillity


class C2204937_TestClass(BaseTestCase):

    def test_C2204937(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2204937'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """    1. Execute T1121448.fex    """
        utillobj.active_run_fex_api_login("T1121448.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(7)
        miscelaneousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01a: Execute the 46036.fex and Verify the Report Heading')
        column_list=['Category','Product', 'Unit Sales']
        miscelaneousobj.verify_column_heading('ITableData0', column_list, 'Step 01b: Execute the 46036.fex and Verify the column heading')
        value = driver.find_element_by_css_selector("[id^='THEAD_0_'] span").text.strip()
        utillobj.asequal('GGSALES Original Heading', value, 'Step 01c: Verify that the procedure contains a custom heading, GGSALES Original Heading')
        time.sleep(2)
        
        """    2. Using the Active control for Unit Sales, create a Rollup report by Category.    """
        miscelaneousobj.select_menu_items('ITableData0', 2, 'Rollup','Category')
        time.sleep(8)
        column=['Category','Unit Sales']
        miscelaneousobj.verify_column_heading('ITableData1', column, "Step 02a: Verify Column heading after rollup")
        miscelaneousobj.verify_page_summary('1','3of3records,Page1of1', 'Step 02b: Verify Page summary 245of245')
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID + '_Ds01.xlsx',"Step 02c:Verify dataset for ROLLUP on Revenue")
        value = driver.find_element_by_css_selector("[id^='THEAD_1_'] span").text.strip()
        utillobj.asequal('GGSALES Original Heading', value, 'Step 02d: Verify that the RollUp contains a custom heading, GGSALES Original Heading')
        time.sleep(2)
        
        """    3. From the Rollup report, click the third icon and generate a PIE chart.    """
        rollobj.click_chart_menu_bar_items('wall1',2)
        """ Verify values are arranged in ascending order."""
        time.sleep(5)
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, Test_Case_ID + '_Actual_Step03', image_type='actual')
        miscelaneousobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge!", ['Coffee','Unit Sales: 1.4M','37.3% of 3.7M'],"Step 03a: Verify Chart piebevel tooltip for Unit Sales")
        utillobj.verify_chart_color('wall1',"riser!s0!g0!mwedge!",'cerulean_blue',"Step 03b:Verify Fill Color")
        result_obj.verify_riser_legends('wall1', ['Coffee','Food','Gifts'], "Step 03c: Verify Chart piebevel Legends")
        miscelaneousobj.verify_popup_title('wall1', 'Unit Sales by Category', 'Step 03d: Verify the dialog title')
        rollobj.verify_arChartMenu('wall1',"Step 03e: Verify the chart Menu")
        value = driver.find_element_by_css_selector("#wall1 [id^='THEAD_0_'] span").text.strip()
        utillobj.asequal('GGSALES Original Heading', value, 'Step 03e: Expect to still see the Original Heading appear over the PIE chart.')
        time.sleep(2)
        
        """    4. Close the PIE chart and return to the Active Report. Using the Active control for Unit Sales, create a PIVOT report with Product for by and Category for ACROSS.    """
        miscelaneousobj.close_popup_dialog('1')
        time.sleep(2)
        miscelaneousobj.select_menu_items('ITableData0', 2, 'Pivot (Cross Tab)','Product','Category')         
        """Verify Pivot table 'State By Product ID, Category' is generated based on the columns selection."""    
        utillobj.verify_pivot_data_set('piv1', Test_Case_ID + '_Ds02.xlsx','Step 04: Verify Pivot dataset')
        value = driver.find_element_by_css_selector("#piv1 [id^='THEAD_0_'] span").text.strip()
        utillobj.asequal('GGSALES Original Heading', value, 'Step 04a: Expect to still see the Original Heading appear over the PIE chart.')
        time.sleep(2)
         
        """    5. Edit the Fex and comment the first ARDEFAULTHEAD command, then uncomment the second ARDEFAULTHEAD command with value 'GENERATED'. Save and execute the Fex.    """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        utillobj.active_run_fex_api_login("T1121448g.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(7)
        miscelaneousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 05a: Execute the 46036.fex and Verify the Report Heading')
        column_list=['Category','Product', 'Unit Sales']
        miscelaneousobj.verify_column_heading('ITableData0', column_list, 'Step 05b: Execute the 46036.fex and Verify the column heading')
        value = driver.find_element_by_css_selector("[id^='THEAD_0_'] span").text.strip()
        utillobj.asequal('GGSALES Original Heading', value, 'Step 05c: Expect to see the same original Report with the Heading "GGSALES Original Heading".')
        time.sleep(2)
        
        """    6. Using the Active control for Unit Sales, create a Rollup report by Category.    """
        miscelaneousobj.select_menu_items('ITableData0', 2, 'Rollup','Category')
        time.sleep(8)
        column=['Category','Unit Sales']
        miscelaneousobj.verify_column_heading('ITableData1', column, "Step 06a: Verify Column heading after rollup")
        miscelaneousobj.verify_page_summary('1','3of3records,Page1of1', 'Step 06b: Verify Page summary 245of245')
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID + '_Ds01.xlsx',"Step 06c:Verify dataset for ROLLUP on Revenue")
        value = driver.find_element_by_css_selector("[id^='THEAD_1_'] tt>div").text.strip()
        utillobj.asequal('Unit Sales by Category', value, 'Step 06d: Expect to see the Active generated Heading "Unit Sales by Category"')
        time.sleep(2)
        
        """    7. From the Rollup report, click the third icon and generate a PIE chart.    """
        rollobj.click_chart_menu_bar_items('wall1',2)
        """ Verify values are arranged in ascending order."""
        time.sleep(5)
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, Test_Case_ID + '_Actual_Step07', image_type='actual')
        miscelaneousobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge!", ['Coffee','Unit Sales: 1.4M','37.3% of 3.7M'],"Step 07a: Verify Chart piebevel tooltip for Unit Sales")
        utillobj.verify_chart_color('wall1',"riser!s0!g0!mwedge!",'cerulean_blue',"Step 07b:Verify Fill Color")
        result_obj.verify_riser_legends('wall1', ['Coffee','Food','Gifts'], "Step 07c: Verify Chart piebevel Legends")
        miscelaneousobj.verify_popup_title('wall1', 'Unit Sales by Category', 'Step 07d: Verify the dialog title')
        rollobj.verify_arChartMenu('wall1',"Step 07e: Verify the chart Menu")
        value = driver.find_element_by_css_selector("#wall1 #wbody1_ft table tr>td>div").text.strip()
        utillobj.asequal('Unit Sales by Category', value, 'Step 07e: Expect to still see the Active generated Heading appear over the PIE chart.')
        time.sleep(2)
        
        """    8. Close the PIE chart and return to the Active Report. Using the Active control for Unit Sales, create a PIVOT report with Product for by and Category for ACROSS.    """ 
        miscelaneousobj.close_popup_dialog('1')
        time.sleep(2)
        miscelaneousobj.select_menu_items('ITableData0', 2, 'Pivot (Cross Tab)','Product','Category')         
        """Verify Pivot table 'State By Product ID, Category' is generated based on the columns selection."""  
        utillobj.verify_pivot_data_set('piv1', Test_Case_ID + '_Ds02.xlsx','Step 08: Verify Pivot dataset')
        value = driver.find_element_by_css_selector("#piv1 > tbody > tr:nth-child(1) > td > table > tbody > tr > td > div").text.strip()
        utillobj.asequal('Unit Sales by Category, Product', value, 'Step 08a: Expect to see the Active generated Heading again over the Pivot Report.')
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()
    
    
    