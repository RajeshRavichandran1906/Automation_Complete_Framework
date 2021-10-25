'''
Created on Sep 29, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2110928
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest,time,re

class C2110928_TestClass(BaseTestCase):

    def test_C2110928(self):
        
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Execute the attached repro - act94_default.fex.
        """
        utillobj.active_run_fex_api_login("act94_default.fex", "S7215", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', "Step 01.1: Verify Page Summary")
        column_list=['Category','Product','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.1: Verify all columns listed on the report ACT-485t.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act94_default.xlsx','Step 01.2: Verify data set')
        
        val ='[id="checkboxPROMPT_1"]'
        val_list=[el.strip() for el in self.driver.find_element_by_css_selector(val).text.split("\n") if bool(re.match('\S', el))]
        utillobj.asequal(val_list,['[All]', 'Coffee', 'Food', 'Gifts'],'Step 01.3: Notice the presence of the ALL value in the Check Box')
        
        """
        STep 02:  Check the Coffee value
        """
        self.driver.find_element_by_css_selector('[id="checkboxPROMPT_1_1"]').click()
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '3of10records,Page1of1', "Step 02.1: Verify Page Summary")
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2110928_Ds01.xlsx','Step 02.2: Expect to see the following Dashboard, with only Coffee data')
        
        """
        Step 03: Click the Coffee value again, to turn it off.
        """
        self.driver.find_element_by_css_selector('[id="checkboxPROMPT_1_1"]').click()
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', "Step 03.1: Verify Page Summary")
        utillobj.verify_data_set('ITableData0', 'I0r', 'act94_default.xlsx','Step 03.2: Expect to see the following Dashboard, with all data again and the Check Box set to "ALL"')
        
        """
        Step 04: Close the act94_default window. Execute the attached repro - act94_off.fex Maximize the output window.
        """
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("act94_off.fex", "S7215", 'mrid', 'mrpass')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act94_default.xlsx','Step 04.1: Verify data set')
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', "Step 04.2: Verify Page Summary")
        val = '[id="checkboxPROMPT_1"]'
        val_list=[el.strip() for el in self.driver.find_element_by_css_selector(val).text.split("\n") if bool(re.match('\S', el))]
        utillobj.asequal(val_list,['Coffee', 'Food', 'Gifts'],'Step 04.3: Notice that there is no ALL value in the Check Box')
                
        """
        Step 05: Check the Food value.
        """
        self.driver.find_element_by_css_selector('[id="checkboxPROMPT_1_1"]').click()
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '3of10records,Page1of1', "Step 05.1: Verify Page Summary")
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2110928_Ds02.xlsx','Step 05.2: Expect to see with only Food Data')
        
        """
        Step 06: Click the Food value again, to turn it off.
        """
        self.driver.find_element_by_css_selector('[id="checkboxPROMPT_1_1"]').click()
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'act94_default.xlsx','Step 06.1: Expect to see the following Dashboard, with all data again.')
        
        """
        Step 07: Close the act94_off window. Execute the attached repro - act94_on.fex Maximize the output window.
        """
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("act94_on.fex", "S7215", 'mrid', 'mrpass')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act94_default.xlsx','Step 07.1: Verify data set')
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', "Step 07.2: Verify Page Summary")
        
        val ='[id="checkboxPROMPT_1"]'
        val_list=[el.strip() for el in self.driver.find_element_by_css_selector(val).text.split("\n") if bool(re.match('\S', el))]
        utillobj.asequal(val_list,['[All]','Coffee', 'Food', 'Gifts'],'Step 07.3: Notice the presence of the ALL value in the Check Box')
        
        """
        Step 08: Check the Gifts value.
        """
        self.driver.find_element_by_css_selector('[id="checkboxPROMPT_1_3"]').click()
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '4of10records,Page1of1', "Step 08.1: Verify Page Summary")
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2110928_Ds03.xlsx','Step 08.2: Expect to see with only Gifts Data')
        
        
        """
        Step 09: Click the Gifts value again, to turn it off.
        """
        self.driver.find_element_by_css_selector('[id="checkboxPROMPT_1_3"]').click()
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'act94_default.xlsx','Step 09.1: Expect to see the following Dashboard, with all data again and the Check Box set to "ALL"')
        
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
