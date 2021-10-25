'''
Created on Sep 27, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203695 
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection, visualization_resultarea
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity
import unittest,os
import time
from selenium.webdriver.common import keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class C2203695_TestClass(BaseTestCase):

    def test_C2203695(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2203695'
        """
        Step 01: Execute the attached fex, 121266.fex.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.active_run_fex_api_login("121266.fex", "S7068", 'mrid', 'mrpass')
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        miscelanousobj.verify_page_summary('0','134of134records,Page1of3', 'Step 01.1: Verify Page summary 134of134')
        column=['Country', 'Region', 'State', 'Product Type', 'Line Total', 'Quantity', 'Cost of Goods Sold', 'Profit', 'Returns', 'Return Ratio']
        miscelanousobj.verify_column_heading('ITableData0', column, "Step 01.2: Verify Column heading of 121266.fex")
        utillobj.verify_data_set('ITableData0','I0r','121266.xlsx',"Step 01.3: Verify 121266.fex dataset")      
         
        """
        Step 02: Click the arrow in the heading of column STATE, select Filter option, from submenu select Equals(EQ).
        """
        time.sleep(5)
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
         
        """
        Step 03: Click down arrow to select the values.
        """
        filterselectionobj.create_filter(1, 'Equals','large', value1='Indiana',value2='Illinois')
        time.sleep(5)
        """
        Step 04:Single Click two values: Indiana and Illinois.
        Verify whether both values are selected with tick sign in multi-column select box. 
        """
        driver.find_element_by_css_selector(".arFilterItem #ftp1_1_0 img").click()
        browser=utillobj.parseinitfile('browser')
        if browser=='IE':
            utillobj.verify_popup_data_set('wall2','FiltSel2','C2203695_Ds01_ie.xlsx',"Step 04: Verify Indiana and Illinois values are selected")
        else:
            utillobj.verify_popup_data_set('wall2','FiltSel2','C2203695_Ds01.xlsx',"Step 04: Verify Indiana and Illinois values are selected")
        driver.find_element_by_css_selector("div[onclick='closewin(2)'] img").click()
        """
        Step 05: Again Click on two values: Indiana and Illinois
        Verify values are deselected and tick sign is disappeared from the multi-column select box.
        """        
        filterselectionobj.create_filter(1, 'Equals','large', value1='Indiana',value2='Illinois')
        driver.find_element_by_css_selector(".arFilterItem #ftp1_1_0 img").click()
        utillobj.verify_popup_data_set('wall2','FiltSel2','C2203695_Ds02.xlsx',"Step 05: Verify Indiana and Illinois values are deselected")
        
        
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        