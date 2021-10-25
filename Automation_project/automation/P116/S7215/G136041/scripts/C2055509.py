'''
Created on Sep 13, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055509
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest, time, re
from selenium.webdriver.common.by import By


class C2055509_TestClass(BaseTestCase):

    def test_C2055509(self):
        
        """
            Step 01: Execute 143947.fex form repro
        """
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login("143947.fex", "S7215", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Execute the 143947.fex")
        column_list=['COUNTRY', 'CAR', 'MODEL', 'BODYTYPE', 'SEATS', 'DEALER_COST', 'RETAIL_COST', 'SALES', 'LENGTH', 'WIDTH', 'HEIGHT', 'WEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'RPM', 'MPG', 'ACCEL', 'DEALER_COST', 'RETAIL_COST', 'SALES', 'LENGTH', 'WIDTH', 'HEIGHT', 'WEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'RPM', 'MPG', 'ACCEL']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
        utillobj.verify_data_set('ITableData0', 'I0r', '143947.xlsx','Step 01.3: Verify data set')
        
        miscelanousobj.verify_horizontal_page_scroll('IWindowBody0', 'yes', 'Step 01.4: Notice the scroll bar, as the report extends off-page to the right')
        
        """
        Step 02: Select the column CAR and click on Freeze Column
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Freeze Column')
        time.sleep(5)
        miscelanousobj.verify_freeze_column('yes', 'IScrollWindowBody0', 'Step 02.1: verify freeze column scroll bar')
        column_list1=['MODEL', 'BODYTYPE', 'SEATS', 'DEALER_COST', 'RETAIL_COST', 'SALES', 'LENGTH', 'WIDTH', 'HEIGHT', 'WEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'RPM', 'MPG', 'ACCEL', 'DEALER_COST', 'RETAIL_COST', 'SALES', 'LENGTH', 'WIDTH', 'HEIGHT', 'WEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'RPM', 'MPG', 'ACCEL']
        miscelanousobj.verify_column_heading('IScrollWindowBody0 ', column_list1, 'Step 02.2: notice that the scroll bar begins under the MODEL column')
        
        """
        Step 03: Scroll the report all the way to the right.
        """
        val = '[id="I0r0.0C30"]'
        
        miscelanousobj.verify_freeze_column('yes', 'IFixWindowBody0', 'Step 03.1: Expect to see COUNTRY and CAR not move')
        val_1 = self.driver.find_element_by_css_selector(val).location['x']
        utillobj.as_not_equal('2195',val_1,'Step 03.2: Expect to see the MODEL field and all others move to the left')
        
        """
        Step 04: Click on the 'SEATS' column, the pop up menu is displaying under the seats column
        """     
        seat_col = "#MAINTABLE_wbody0 table tbody #TCOL_0_C_4 > tt"
        driver.find_element_by_css_selector(seat_col).click()
        pop_up = '[id="popid0_4"]'
        pop_up_menu = '[id^="set0_4_0_"]'
        self.driver.find_element(By.CSS_SELECTOR,pop_up).click()
        menu=self.driver.find_elements(By.CSS_SELECTOR,pop_up_menu)
        actual_list=[]
        menu_list = ['Sort Ascending', 'Sort Descending', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', 'Hide Column', 'Freeze Column', 'Unfreeze All', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Export', 'Print', 'Window', 'Restore Original']
        menu_list_ie = ['Sort Ascending', 'Sort Descending', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', 'Hide Column', 'Freeze Column', 'Unfreeze All', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Send as E-mail', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        for i in range(len(menu)):
            actual_list.append(re.sub(r'\n', ' ', menu[i].text.strip()))
        
        value = [x for x in actual_list if x]
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            utillobj.asequal(menu_list_ie,value,'Step 04: Expect to see the pop up menu appear below SEATS')
        else:
            utillobj.asequal(menu_list,value,'Step 04: Expect to see the pop up menu appear below SEATS')
        
if __name__ == '__main__':
    unittest.main()     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        