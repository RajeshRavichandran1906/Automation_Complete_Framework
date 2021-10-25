'''
Created on Sep 19, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2062874

Test case Name = This repro will require several targeted cell click operations to verify the location of the cell options window.

'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity,core_utility
from selenium.webdriver.common.by import By
from common.lib.global_variables import Global_variables
import unittest,time

class C2062874_TestClass(BaseTestCase):

    def test_C2062874(self):
               
        def cell_location(table_id, rownum, colnum):
            """
            Usage: Return upper value 
            Note : Local Function Specially designed for this test case and all locators stable locators chosen for this case.
            """
            field_css="#" + table_id + " tr[id*='r" + str(rownum) + ".'] td[id$='C" + str(colnum) + "']"
            upper=self.driver.find_element_by_css_selector(field_css).location['y']
            return upper
        
        def menu_location(rownum, elmnum):
            upper_menu = self.driver.find_elements(By.CSS_SELECTOR, '.arMenu[id*="dt0_I0r'+str(rownum)+'."]')
            upper_menus=upper_menu[elmnum].location['y']
            return upper_menus
                
        driver = self.driver 
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        browser=Global_variables.browser_name
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
                
        """
        Step 01: Execute the attached repro - act-503.fex.
        """
        utillobj.active_run_fex_api_login('act-503.fex','S7215','mrid','mrpass')  
             
        active_misobj.verify_page_summary('0','4317of4317records,Page1of76', 'Step 01.01: Verify Page summary')
        title= ['Sequence#', 'Category', 'Product ID', 'Product', 'Region', 'State', 'City', 'Store ID', 'Date', 'Unit Sales', 'Dollar Sales', 'Budget Units', 'Budget Dollars']
        active_misobj.verify_column_heading('ITableData0', title, "Step 01.02: Verify Column heading of act-503.fex")
        utillobj.verify_data_set('ITableData0','I0r','act-503_page1.xlsx',"Step 01.03: Verify entire Data set in Page 1")
        
        
        """Step 02:Left click the first cell in the upper left corner, containing Sequence# 1."""
        
        cell1 = int(cell_location("ITableData0",2, 1))
        
        expected_value=['Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        active_misobj.verify_field_menu_items("ITableData0", 2, 1, expected_value, "Step 02.02: Expect to see the cell options menu ")
        
        #Expect to see the cell options menu open right underneath the cell.
        loci = int(menu_location(2, 0))
        
        if loci in range(cell1, cell1+40):
            loc = True
        else: 
            loc = False
        utillobj.asequal(True, loc, 'Step 02.02: Expect to see the cell options menu open right underneath the cell.')        
        
        """Step 03: Left click the first cell in the upper right corner, containing Budget Dollars 14304."""
        #Expect to see the cell options menu open right underneath the cell.
        
        expected_value=['Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        
        active_misobj.verify_field_menu_items("ITableData0", 2, 12, expected_value, "Step 03.01: Expect to see the cell options menu ")
        
        utillobj.asequal(True, loci==int(menu_location(2, 1)), 'Step 03.02: Expect to see the cell options menu open right underneath the cell.')
            
        """Step 04: Using the vertical scroll bar move all the way to the bottom of Page 1."""
        
        #Expect to see the Active Report, showing rows 27 thru 57.
        #Also note that the vertical scroll bar is positioned all the way to the bottom.
        
        """Step 05: Left click the last cell in the lower left corner, containing Sequence# 57."""
        
        #Expect to see only the top of the cell options menu appear.
        #Also notice that the vertical scroll bar has moved slightly upward.
        cell2 = int(cell_location("ITableData0",56, 1))
        expected_value=['Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        
        if browser=='firefox' :
            scroll_field=driver.find_element_by_css_selector("#ITableData0 tr[id*='r56.'] td[id$='C1']")
            driver.execute_script("return arguments[0].scrollIntoView();", scroll_field)
            core_utils.left_click(web_element = scroll_field, element_location='top_left', yoffset=-480)
            time.sleep(2)      
            driver.execute_script("return window.scrollTo(0, document.body.scrollHeight)")
            menu=self.driver.find_element_by_css_selector("div[id^='dt0_I0r'][style*='block']")
            x = menu.find_elements_by_css_selector("span[id^='set0_I0r']")
            actual_value=[el.text.strip() for el in x if el.text.strip() != '']
            utillobj.asequal(expected_value, actual_value, "Step 05.01: Expect to see the cell options menu ")
        else:
            active_misobj.verify_field_menu_items("ITableData0", 56, 1, expected_value, "Step 05.01: Expect to see the cell options menu ")
        loci2= int(menu_location(56, 0))
        
        """Step 06: Again, using the vertical scroll bar advance to the bottom of Page 1."""
        
        #Expect to see more room at the bottom of Page 1, to show the cell options.
        #Also expect to see the full cell options menu appear.
        #this verification done in step 05
        
        if loci2 in range(cell2, cell2+25):
            loc2 = True
        else: 
            loc2 = False
        utillobj.asequal(True, loc2, 'Step 06.01: Expect to see more room at the bottom of Page 1, to show the cell options.')  
               
if __name__ == '__main__':
    unittest.main()