'''
Created on Sep 19, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2067503
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea
from common.lib import utillity
from selenium.webdriver.common.by import By
import unittest,time

class C2067503_TestClass(BaseTestCase):

    def test_C2067503(self):
        
        """
            Step 01: Execute the attached repro - ACT-583.fex.
        """
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.active_run_fex_api_login("ACT-583.fex", "S7215", 'mrid', 'mrpass')
        val = '#MAINTABLE_wbody0_ft div'
        heading = self.driver.find_element(By.CSS_SELECTOR, val).text
        utillobj.asequal(heading,'RETAIL_COST by CAR','Step 01: Expect to see the Active Bar Chart')
        
        """
        Step 02: Hover over the bar for Alfa Romeo.
        """
        miscelanousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g0!mbar', ['RETAIL_COST, ALFA ROMEO: 19,565'], 'Step 02: Expect to see the hover-over information')
        
        """
        Step 03: Hover over the bar for Jaguar.
        """
        miscelanousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g4!mbar', ['RETAIL_COST, JAGUAR: 22,369'], 'Step 03: Expect to see the hover-over information')
        
        """
        Step 04: Left click the bar for Jaguar.
        """
        
        time.sleep(5)
        resultobj.create_lasso('MAINTABLE_wbody0', 'rect', 'riser!s0!g4!mbar')
        time.sleep(3)
        resultobj.select_or_verify_lasso_filter(verify=['1 point','Filter Chart','Exclude from Chart'],msg='Step 04: Expect to see the left-click options appear')
        """
        Step 05: Select Exclude from Chart.
        """
        resultobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        values1 = ['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']

        x_labels=self.driver.find_elements_by_css_selector("#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']")
        label = []
        for i in range(len(x_labels)):
            label.append(x_labels[i].text)
        utillobj.asequal(values1,label,'Step 05: Expect to see the proper bar for Jaguar removed.')
            
        """
        Step 06: Click the Filter icon at the top.
        """
    
        self.driver.find_element(By.CSS_SELECTOR,'[title="Remove Filter"]').click()
        time.sleep(7)
        values2 = ['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        x_labels1=self.driver.find_elements_by_css_selector("#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']")
        label_new = []
        for i in range(len(x_labels1)):
            label_new.append(x_labels1[i].text)
        utillobj.asequal(label_new,values2,'Step 06: Expect to see the Excluded bar for Jaguar return')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()