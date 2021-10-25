'''
Created on Aug 8, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050541
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



class C2050541_TestClass(BaseTestCase):

    def test_C2050541(self):
        """
            Step 01: Execute repro 163008.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("163008.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01: Execute 163008.fex")
        utillobj.verify_data_set('ITableData0', 'I0r', '163008.xlsx',"Step 01: Verify table")
        columns1=['COUNTRY','AMPER_CAR','AMPER_MODEL','AMPER_BODY','SEATS','RETAIL_COST','DEALER_COST']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01: Verify all columns listed on the report')
         
        """
        STep 02: Select the drop-down arrow for AMPER_CAR, select Filter/Equals, then select value - &JAGUAR from the drop-down value box. 
        Click the Filter button.
        """
         
        miscelanousobj.select_menu_items('ITableData0', '1', 'Filter','Equals')
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Equals','small', value1='&JAGUAR')
         
        filter_values = ['AMPER_CAR','Equals','&JAGUAR']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02: Verify filter dialogue',filter_values)
        filterselectionobj.filter_button_click('Filter')
          
        miscelanousobj.move_active_popup('1', '600', '200')
        try:
            value="//div[contains(text(),'ENGLAND')]"
            verify_table=self.driver.find_element(By.XPATH,value).is_displayed()
            utillity.UtillityMethods.asequal(self,True,verify_table,"Step 02: Issue fixed")
        except NoSuchElementException:
            print("Step 02: Issue still not fixed, verify ACT-868")
            self.fail()
        filterselectionobj.close_filter_dialog()
         
        """
        Step 03: Select the drop-down arrow for AMPER_CAR, select Filter/Equals, then select value - JEN & SEN(embedded blank) from the value box. 
        Click the Filter button.
        """
         
        miscelanousobj.select_menu_items('ITableData0', '1', 'Filter','Equals')
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Equals','small', value1='JEN & SEN')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '1of18records,Page1of1', "Step 03: Verify page summary")
        utillobj.verify_data_set('ITableData0','I0r', 'C2050541_Ds01.xlsx','Step 03: Expect to see the filtered 1 line report')
        filterselectionobj.close_filter_dialog()
        """
        Step 04: Select the drop-down arrow for AMPER_MODEL, select Filter/Equals, then select values that contain only the ampersand character, 
        from the value box. values - &&&, & &, & and &&. Click the Filter button.
        """        
        miscelanousobj.select_menu_items('ITableData0', '2', 'Filter','Equals')
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Equals','small', value1='&',value2='& &',value3='&&',value4='&&&')
        filterselectionobj.filter_button_click('Filter')
        try:
            value="//div[contains(text(),'ENGLAND')]"
            verify_table=self.driver.find_element(By.XPATH,value).is_displayed()
            utillity.UtillityMethods.asequal(self,True,verify_table,"Step 04: Issue fixed")
        except NoSuchElementException:
            print("Step 04: Issue still not fixed, verify ACT-868")
            self.fail()
        filterselectionobj.close_filter_dialog()
        
        """
        STep 05: Select the drop-down arrow for AMPER_BODY, select Filter/Equals, 
        then select values that contain one or more trailing ampersand from the value box.
        Values - 'HARDTOP&', 'COUPE&&&', 'ROADSTER&&'.Click the Filter button.
        """
        
        miscelanousobj.select_menu_items('ITableData0', '3', 'Filter','Equals')
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Equals','small', value1='COUPE&&&',value2='HARDTOP&',value3='ROADSTER&&')
        filterselectionobj.filter_button_click('Filter')
        try:
            value="//div[contains(text(),'ENGLAND')]"
            verify_table=self.driver.find_element(By.XPATH,value).is_displayed()
            utillity.UtillityMethods.asequal(self,True,verify_table,"Step 05: Issue fixed")
        except NoSuchElementException:
            print("Step 05: Issue still not fixed, verify ACT-868")
            self.fail()
        filterselectionobj.close_filter_dialog()
        
        """
        STep 06: These tests use Filter/Contains to retrieve data.
        Select the drop-down arrow for AMPER_CAR, select Filter/Contains, then enter the string '&&P'.
        This uses a search string that starts with an ampersand and finds data at the beginning of the field.
        Click the Filter button.    
        """
        
        miscelanousobj.select_menu_items('ITableData0', '1', 'Filter','Contains')
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Contains','small', value1='&&P')
        filterselectionobj.filter_button_click('Filter')
        try:
            value="//div[contains(text(),'FRANCE')]"
            verify_table=self.driver.find_element(By.XPATH,value).is_displayed()
            utillity.UtillityMethods.asequal(self,True,verify_table,"Step 06: Issue fixed")
        except NoSuchElementException:
            print("Step 06: Issue still not fixed, verify ACT-868")
            self.fail()
        
        filterselectionobj.close_filter_dialog()
        """
        Select the drop-down arrow for AMPER_CAR, select Filter/Contains, then enter the string '&ROMEO'.
        This uses a search string that starts with an ampersand and finds data embedded in the field.
        Click the Filter button.
        """
        miscelanousobj.select_menu_items('ITableData0', '1', 'Filter','Contains')
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Contains','small', value1='&ROMEO')
        filterselectionobj.filter_button_click('Filter')
        try:
            value="//div[contains(text(),'ITALY')]"
            verify_table=self.driver.find_element(By.XPATH,value).is_displayed()
            utillity.UtillityMethods.asequal(self,True,verify_table,"Step 06: Issue fixed")
        except NoSuchElementException:
            print("Step 06: Issue still not fixed, verify ACT-868")
            self.fail()
        filterselectionobj.close_filter_dialog()
        
        """
        Step 07: Select the drop-down arrow for AMPER_CAR, select Filter/Contains, then enter the string 'DAT&&'.
        This uses a search string that ends with an ampersand.
        Click the Filter button.
        """
        
        miscelanousobj.select_menu_items('ITableData0', '1', 'Filter','Contains')
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Contains','small', value1='DAT&&')
        filterselectionobj.filter_button_click('Filter')
        try:
            value="//div[contains(text(),'JAPAN')]"
            verify_table=self.driver.find_element(By.XPATH,value).is_displayed()
            utillity.UtillityMethods.asequal(self,True,verify_table,"Step 07: Issue fixed")
        except NoSuchElementException:
            print("Step 07: Issue still not fixed, verify ACT-868")
            self.fail()
        filterselectionobj.close_filter_dialog()
            
        """
        Step 08: Select the drop-down arrow for AMPER_MODEL, select Filter/Contains, then enter the string '&.2'.
        Click the Filter button.
        """
        miscelanousobj.select_menu_items('ITableData0', '2', 'Filter','Contains')
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Contains','small', value1='&.2')
        filterselectionobj.filter_button_click('Filter')
        try:
            value="//div[contains(text(),'W GERMANY')]"
            verify_table=self.driver.find_element(By.XPATH,value).is_displayed()
            utillity.UtillityMethods.asequal(self,True,verify_table,"Step 08: Issue fixed")
        except NoSuchElementException:
            print("Step 08: Issue still not fixed, verify ACT-868")
            self.fail()
        filterselectionobj.close_filter_dialog()
        
        """
        STep 09: Select the drop-down arrow for AMPER_MODEL, select Filter/Contains, then enter the generic value '&'.
        Click the Filter button.
        """
        
        miscelanousobj.select_menu_items('ITableData0', '2', 'Filter','Contains')
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Contains','small', value1='&')
        filterselectionobj.filter_button_click('Filter')
        try:
            value="//div[contains(text(),'W GERMANY')]"
            verify_table=self.driver.find_element(By.XPATH,value).is_displayed()
            utillity.UtillityMethods.asequal(self,True,verify_table,"Step 09: Issue fixed")
        except NoSuchElementException:
            print("Step 09: Issue still not fixed, verify ACT-868")
            self.fail()
        filterselectionobj.close_filter_dialog()
        
        """
        Step 10: Select the drop-down arrow for AMPER_BODY, select Filter/Contains, then enter the value '&&&'.
        Click the Filter button.
        """
        miscelanousobj.select_menu_items('ITableData0', '3', 'Filter','Contains')
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Contains','small', value1='&&&')
        filterselectionobj.filter_button_click('Filter')
        try:
            value="//div[contains(text(),'W GERMANY')]"
            verify_table=self.driver.find_element(By.XPATH,value).is_displayed()
            utillity.UtillityMethods.asequal(self,True,verify_table,"Step 10: Issue fixed")
        except NoSuchElementException:
            print("Step 10: Issue still not fixed, verify ACT-868")
            self.fail()
        filterselectionobj.close_filter_dialog()
            
        """
        STep 11: Filter/Indirect retrieval of data with ampersand(s).
        This includes Less than or equal to, Greater than, Between & Contains but do not explicitly reference the ampersands themselves.
        Select the drop-down arrow for AMPER_CAR, select Filter/Less than or equal to, then select 'BMW' from the drop-down list.
        Click the Filter button.
        """
        miscelanousobj.select_menu_items('ITableData0', '1', 'Filter','Less than or equal to')
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Less than or equal to','small', value1='BMW')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '13of18records,Page1of1', "Step 11: Verify page summary")
        utillobj.verify_data_set('ITableData0','I0r', 'C2050541_Ds02.xlsx','Step 11: Expect the Filtered report to contain 13 rows')
        filterselectionobj.close_filter_dialog()
            
        """
        Step 12: Select the drop-down arrow for AMPER_MODEL, select Filter/Greater than, then select '2002 2 DOOR AUTO' from the drop-down list. 
        Click the Filter button.
        """
        miscelanousobj.select_menu_items('ITableData0', '2', 'Filter','Greater than')
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Greater than','small', value1='2002 2 DOOR AUTO')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '9of18records,Page1of1', "Step 12: Verify page summary")
        utillobj.verify_data_set('ITableData0','I0r', 'C2050541_Ds03.xlsx','Step 12: Expect the Filtered report to contain 9 rows')
        filterselectionobj.close_filter_dialog() 
            
        """
        STep 13: Select the drop-down arrow for AMPER_BODY, select Filter/Between, then select '&&&&&&&&' for the first value 
        and 'CONVERTIBLE' for the second value, each from their respective drop-down boxes.Click the Filter button.
        """
        miscelanousobj.select_menu_items('ITableData0', '3', 'Filter','Between')
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Between','small', value1='&&&&&&&&&&',value2='CONVERTIBLE')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '4of18records,Page1of1', "Step 13: Verify page summary")
        utillobj.verify_data_set('ITableData0','I0r', 'C2050541_Ds04.xlsx','Step 13: Verify table')
        filterselectionobj.close_filter_dialog() 
            
        """
        Step 14: Select the drop-down arrow for AMPER_CAR, select Filter/Contains, then enter the single letter 'U' for the search argument.
        Click the Filter button.
        """
        miscelanousobj.select_menu_items('ITableData0', '1', 'Filter','Contains')
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Contains','small', value1='U')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '6of18records,Page1of1', "Step 14: Verify page summary")
        utillobj.verify_data_set('ITableData0','I0r', 'C2050541_Ds05.xlsx','Step 14: Expect the Filtered report to contain 6 rows')
        filterselectionobj.close_filter_dialog() 
        
if __name__ == '__main__':
    unittest.main() 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
         
         
        
        
        
        
        
        