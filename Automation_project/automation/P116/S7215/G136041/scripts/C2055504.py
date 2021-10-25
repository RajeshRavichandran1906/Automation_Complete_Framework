'''
Created on Sep 13, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055504
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest
import re
from selenium.webdriver.common.by import By

class C2055504_TestClass(BaseTestCase):

    def test_C2055504(self):
        """Test case variables"""
        country = "//span[contains(text(),'COUNTRY')]"
        england = "//span[contains(text(),'ENGLAND')]"
        france = "//span[contains(text(),'FRANCE')]"
        italy = "//span[contains(text(),'ITALY')]"
        japan = "//span[contains(text(),'JAPAN')]"
        germany = "//span[contains(text(),'W GERMANY')]"
        
        """
            Step 01: Execute 148241.fex form repro
        """
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login("148241.fex", "S7215", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Execute the 148241.fex")
        column_list = ['COUNTRY', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY', 'MODEL', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST']
        column_heading_css = "#ITableData0 td b"
        columns=self.driver.find_elements_by_css_selector(column_heading_css)
        actual_list = []
        for i in range(len(columns)):
            actual_list.append(re.sub(r'\n', ' ', columns[i].text.strip()))
        utillobj.asequal(column_list,actual_list,'Step 01.2: Verify column headings')
        
        """
        Step 02: Verify that heading width is displayed properly.
        """
        column1 = self.driver.find_element(By.XPATH,country).location['x']
        print(column1)
        column2 = self.driver.find_element(By.XPATH,england).location['x']
        print(column2)
        column3 = self.driver.find_element(By.XPATH,france).location['x']
        print(column3)
        column4 = self.driver.find_element(By.XPATH,italy).location['x']
        print(column4)
        column5 = self.driver.find_element(By.XPATH,japan).location['x']
        print(column5)
        column6 = self.driver.find_element(By.XPATH,germany).location['x']
        print(column6)
        
        '''Verification check point'''
        if column1 and column2 == 159 or 154:
            print("Step 02.1: Verify that 'COUNTRY' & 'ENGLAND' heading width is displayed properly - Passed")
        else:
            self.fail("Step 02.1: Verify that 'COUNTRY' & 'ENGLAND' heading width is displayed properly - Failed")
            
        if column3 in range(590, 620):
            print("Step 02.2: Verify that 'FRANCE' heading width is displayed properly - Passed")
        else:
            self.fail("Step 02.2: Verify that 'FRANCE' heading width is displayed properly - Failed")
            
        if column4 in range(990, 1050):
            print("Step 02.3: Verify that 'ITALY' heading width is displayed properly - Passed")
        else:
            self.fail("Step 02.3: Verify that 'ITALY' heading width is displayed properly - Failed")
            
        if column5 in range(1425, 1550):
            print("Step 02.4: Verify that 'JAPAN' heading width is displayed properly - Passed")
        else:
            self.fail("Step 02.4: Verify that 'JAPAN' heading width is displayed properly - Failed")
            
        if column6 in range(1850, 1940):
            print("Step 02.5: Verify that 'W GERMANY' heading width is displayed properly - Passed")
        else:
            self.fail("Step 02.5: Verify that 'W GERMANY' heading width is displayed properly - Failed")
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()        