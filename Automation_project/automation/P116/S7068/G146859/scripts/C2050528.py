'''
Created on Aug 3, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050528
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_filter_selection
from common.lib import utillity
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class C2050528_TestClass(BaseTestCase):

    def test_C2050528(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050528'
        unlock = "//div[@id='LINKIMG1_-1']/div/img[contains(@src,'PPXq6HHAIyeUcCNovBsAAAAAElFTkSuQmCC')]"
        lock="//div[@id='LINKIMG1_-1']/div/img[contains(@src,'vu7K7AAAAABJRU5ErkJggg')]"
        
        """
            Step 01: Execute the AR-RP-193.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj=active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-193.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Execute the AR-RP-193.fex")
        columns1=['Order Number INTEGER','ALPHA Store Code','Date YYMD','Date MDYY','Date DMYY','D10.2 Unit Price','P9.2M Unit Price', 'DATETIME HYYMDSA']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01: Verify all columns listed on the report')

        """
        Step 02: Create a new Pivot Table by selecting P9.2M Unit Price and from the drop down list, select Pivot(Cross Tab),
        move to Group BY(SUM) and select ALPHA Store Code, move to Across and select Date YYMD for the Across.
        """
        miscelanousobj.select_menu_items('ITableData0', "6", "Pivot (Cross Tab)","ALPHA Store Code","Date YYMD")
        utillobj.verify_pivot_data_set("piv1", "C2050528_Ds01.xlsx","Step 02: Expect to see the following Pivot Table.")
        
        try:    
            unlock_icon = self.driver.find_element(By.XPATH, unlock).is_displayed()
            utillobj.asequal(True,unlock_icon,"Step 02: Notice that the lock icon is open")
        except NoSuchElementException:
            print("Step 02: Notice that the lock icon is open - Failed")
            
        """
        Step 03: Click the lock icon in the tool bar of the Pivot Table.
        """
        
        self.driver.find_element(By.XPATH, unlock).click()
        
        try:    
            lock_icon = self.driver.find_element(By.XPATH, lock).is_displayed()
            utillobj.asequal(True,lock_icon,"Step 03: Expect to see the lock icon close")
        except NoSuchElementException:
            print("Step 03: Expect to see the lock icon close - Failed")
        
        """
        Step 04: Go back to the Original Report and click the drop down arrow for the ALPHA Store Code field. Select Filter, then Not equal.
        """
        miscelanousobj.move_active_popup("1", "450", "200")
        miscelanousobj.select_menu_items('ITableData0', "1", "Filter","Not equal")
        time.sleep(2)
        filterselectionobj.verify_filter_selection_dialog(True, "Step 04: Expect to see the Filter selection box",['ALPHA Store Code','Not equal'],popup_id="wall2")
        """
        Step 05: Click the drop down arrow and select R1019 for the value from the list of values.
        """
        
        filterselectionobj.create_filter(1, 'Not equal',popup_id='wall2',value1="R1019")
        filterselectionobj.verify_filter_selection_dialog(True, "Step 05: Expect to see R1019 appear in the Filter box",['ALPHA Store Code','Not equal','R1019'],popup_id="wall2")
        """
        Step 06: Click the Filter button.
        """
        
        filterselectionobj.filter_button_click('Filter',popup_id="wall2")
        utillobj.verify_data_set("ITableData0", "I0r", "C2050528_Ds02.xlsx","Step 06: Expect to see the report no longer contains ALPHA Store Code of R1019")
        """
        Step 07: Switch back to the Pivot Table.    
        Expect to see that the Pivot Table still contains ALPHA Store Code of R1019.
        """
        utillobj.verify_pivot_data_set("piv1", "C2050528_Ds03.xlsx","Step 07: Expect to see that the Pivot Table still contains ALPHA Store Code of R1019")
        
        """
        STep 08: In the Pivot Table, click the lock icon again.
        """
        miscelanousobj.move_active_popup("2", "100", "300")
        self.driver.find_element(By.XPATH, lock).click()
        """
        Expect to see that the lock is again open and that ALPHA Store Code value R1019 is automatically removed from the Pivot Table.
        """
        try:    
            unlock_icon = self.driver.find_element(By.XPATH, unlock).is_displayed()
            utillobj.asequal(True,unlock_icon,"Step 08: Expect to see that the lock is again open")
        except NoSuchElementException:
            print("Step 08:Expect to see that the lock is again open - Failed")
            
        utillobj.verify_pivot_data_set("piv1", "C2050528_Ds04.xlsx","Step 08: Expect to see ALPHA Store Code value R1019 is automatically removed from the Pivot Table")
        
if __name__ == '__main__':
    unittest.main()   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         