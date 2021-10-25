'''
Created on Sep 28, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2067501
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest,time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class C2067501_TestClass(BaseTestCase):

    def test_C2067501(self):
        
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Execute the attached repro - act-499.fex.
        """
        utillobj.active_run_fex_api_login("act-499.fex", "S7215", 'mrid', 'mrpass')
        element = (By.CSS_SELECTOR, "span[title='Goto Page']")
        utillobj._validate_page(element)
        time.sleep(5)
        driver.set_window_size('900', '700')
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Execute the act-499.fex")
        column_list=['SEATS', 'DEALER_COST', 'RETAIL_COST', 'SALES', 'LENGTH', 'WIDTH', 'HEIGHT', 'WEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'RPM', 'MPG', 'ACCEL']
        miscelanousobj.verify_column_heading("IScrollWindowBody0", column_list, 'Step 01.2: Verify all columns listed on the report act-499.fex')
        miscelanousobj.verify_freeze_column('yes', 'IScrollWindowBody0', 'Step 01.4: Expect to see the following Active report, with a visible Freeze column after BODYTYPE')
        
        """
        Step 02: Click the drop down for the first column, COUNTRY.
        """
        
        val1 = self.driver.find_element_by_css_selector('[id="TCOL_0_C_0"]').location['x'] #before image
        self.driver.find_element_by_css_selector('[id="TCOL_0_C_0"]').click()
        val3 = self.driver.find_element_by_css_selector('[id="popid0_0"]').location['x'] #dropdown
        self.driver.find_element_by_css_selector('[id="popid0_0"]').click()
        val2 = self.driver.find_element_by_css_selector('[id="dt0_0_0"]').location['x'] #menu
        val = val2 - val1
        val_1 = val2 - val3
        
        result = True if val >= 60 and val <=70 else False
        utillobj.asequal(result,True,'Step 02.1: Expect to see the Context Menu of drop down options to appear just slightly to the right of the COUNTRY column')
        result_1 = True if val_1>=1 and val_1<=5 else False
        utillobj.asequal(result_1,True,'Step 02.2: Expect to see upper left corner of the Context Menu should just touch the drop down arrow for COUNTRY')
        
        
        """
        Step 03: Click the drop down for the fourth column, BODYTYPE.
        """
        
        bodytype = self.driver.find_element_by_css_selector('[id="TCOL_0_C_3"]').location['x']
        self.driver.find_element_by_css_selector('[id="TCOL_0_C_3"]').click()
        bodytype_arrow = self.driver.find_element_by_css_selector('[id="popid0_3"]').location['x']
        self.driver.find_element_by_css_selector('[id="popid0_3"]').click()
        bodytype_popup = self.driver.find_element_by_css_selector('[id="dt0_3_0"]').location['x']
        bodytype_val = bodytype_popup - bodytype
        bodytype_val_1 = bodytype_popup - bodytype_arrow
         
        result = True if bodytype_val>=54 or bodytype_val>=43 else False
        utillobj.asequal(result,True,'Step 03.1: Expect to see the Context Menu of drop down options to appear just slightly to the right of the BODYTYPE column.')
         
        result1 = True if val_1>=1 and val_1<=5 else False
        utillobj.asequal(result1,True,'Step 03.2: Expect to see the upper left corner of the Context Menu should just touch the drop down arrow for BODYTYPE')
        
        
        """
        Step 04: lick the drop down for the fifth column for SEATS, the first column after the Freeze line.
        """
        seat = self.driver.find_element_by_css_selector('[id="TCOL_0_C_4"]').location['x']
        self.driver.find_element_by_css_selector('[id="TCOL_0_C_4"]').click()
        seat_arrow = self.driver.find_element_by_css_selector('[id="popid0_4"]').location['x']
        self.driver.find_element_by_css_selector('[id="popid0_4"]').click( )
        arrow_popup = self.driver.find_element_by_css_selector('[id="dt0_4_0"]').location['x']
          
        drop_down = seat - arrow_popup
        result = True if drop_down>=40 or drop_down<=45 else False
        utillobj.asequal(result,True,'Step 04.1: Expect to see the Context Menu of drop down options to appear just slightly to the right of the SEATS column')
          
        arrow = seat_arrow - arrow_popup
        result1 = True if arrow<=5 else False
        utillobj.asequal(result1,True,'Step 04.2: Expect to see upper left corner of the Context Menu should just touch the drop down arrow for SEATS')
        
        
        """
        STep 05: Click the drop down for the last fully visible column on the right, for BHP.
        """
        self.driver.find_element_by_css_selector('[id="TCOL_0_C_17"]').click()
        self.driver.find_element_by_css_selector('[id="TCOL_0_C_14"]').click()
        bhp = self.driver.find_element_by_css_selector('[id="TCOL_0_C_14"]').location['x']
        bhp_arrow = self.driver.find_element_by_css_selector('[id="popid0_14"]').location['x']
        time.sleep(3)
        self.driver.find_element_by_css_selector('[id="popid0_14"]').click()
        time.sleep(3)
        bhp_popup = self.driver.find_element_by_css_selector('[id="dt0_14_0"]').location['x']
         
        bhp_1 = bhp - bhp_popup
        bhp_2 = bhp_arrow - bhp_popup
         
        result = True if bhp_1>=25 or bhp_1<=30 else False
        utillobj.asequal(result,True,'Step 05.1: Expect to see the Context Menu of drop down options to appear just slightly to the right of the BHP column')
         
        result_1 = True if bhp_2<=5 else False
        utillobj.asequal(result_1,True,'Step 05.2: Expect to see the upper right corner of the Context Menu should just touch the drop down arrow for BHP')
        
        
        """
        Step 06: Use the scroll bar and move the report all the way to the right.
        """
        
        col = self.driver.find_element_by_css_selector('[id="TCOL_0_C_17"]')
        col.click()
        
        utillobj.asequal(col.text,'ACCEL','Step 06.1: Expect to see the columns after BODYTYPE shifted, so that ACCEL is now the last column visible on the right side of the report')
        columns = ['COUNTRY','CAR','MODEL','BODYTYPE']
        miscelanousobj.verify_column_heading('IFixWindowBody0', columns,'Step 06.2: expect to see COUNTRY, CAR, MODEL and BODYTYPE remain in their original positions, to the left of the Freeze line')
        
        """
        Step 07: Click the drop down for the last fully visible column on the right, for ACCEL.
        """
        col.click()
        accel = col.location['x']
        accel_arrow = self.driver.find_element_by_css_selector('[id="popid0_17"]').location['x']
        time.sleep(3)
        col.click()
        self.driver.find_element_by_css_selector('[id="popid0_17"]').click()
        accel_popup = self.driver.find_element_by_css_selector('[id="dt0_17_0"]').location['x']
        
        bhp_1 = accel - accel_popup
        bhp_2 = accel_arrow - accel_popup
        
        result = True if bhp_1>=25 or bhp_1<=30 else False
        utillobj.asequal(result,True,'Step 07.1: Expect to see the Context Menu of drop down options to appear just slightly to the right of the ACCEL column.')
         
        result_1 = True if bhp_2>=85 else False
        utillobj.asequal(result_1,True,'Step 07.2: For this field, the upper right corner of the Context Menu should just touch the drop down arrow for ACCEL.')
        
        

if __name__ == "__main__":
    unittest.main()