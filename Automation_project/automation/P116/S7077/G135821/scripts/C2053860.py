'''
Created on Oct 4, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053860
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest,time,os

class C2053860_TestClass(BaseTestCase):

    def test_C2053860(self):
        
        driver = self.driver #Driver reference object created'
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        Test_Case_ID = 'C2053860'
        """
        Step 01: Execute the AR-RP-001.fex.
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7077", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01.1: Verify Page Summary")
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.1: Verify all columns listed on the report AR-RP-001.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'AR-RP-001.xlsx','Step 01.2: Verify data set')

        """
        Step 02: Click dropdown next to any column and select Send as E-mail option.
        """
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            miscelanousobj.select_menu_items('ITableData0', 1, 'Send as E-mail')
            time.sleep(10)
            """
            autoit script to click on OK ActiveX Popup
            """
            time.sleep(10)
            utillobj.autoit_activex()
            
            """
            Step 03: Click Save Report.
            """
            miscelanousobj.send_as_email(Test_Case_ID+".htm",False,False,False)
            time.sleep(15)
            
            """
            Step 04: Click and open email attachment 'ActiveReport.htm'.
            """
            utillobj.open_outlook_attachment()   
            time.sleep(15)
            dir=os.getcwd() + "\data\\" + Test_Case_ID+".htm"
            driver.get(dir)
            time.sleep(4)
            
            utillobj.verify_data_set('ITableData0', 'I0r', 'AR-RP-001.xlsx','Step 04: Verify active report is correctly displayed')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()