'''
Created on Sep 26, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203696 
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection, visualization_resultarea
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity
import unittest,os
import time
from selenium.webdriver.common import keys
from selenium.webdriver import ActionChains



class C2203696_TestClass(BaseTestCase):

    def test_C2203696(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2203696'
        """
        Step 01: Execute the attached fex. 102803.fex.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.active_run_fex_api_login("102803.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary('0','60of60records,Page1of1', 'Step 01.1: Verify Page summary 60of60')
        column=['MOVIECODE','TITLE']
        miscelanousobj.verify_column_heading('ITableData0', column, "Step 01.2: Verify Column heading of 102803.fex")
        utillobj.verify_data_set('ITableData0','I0r','102803.xlsx',"Step 01.3: Verify 102803.fex dataset")      
         
        """
        Step 02: When the report is displayed / Select the drop down arrow next to Moviecode.
        Select Filter / Equals
        """
        time.sleep(5)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Filter','Equals')
         
        """
        Step 03: In the Filter selection click on the drop down arrow to display values.
        Verify values are displayed as normal text without hyperlinks.
        """
        driver.find_element_by_css_selector(".arFilterItem #ftp1_1_0 img").click()
        utillobj.verify_popup_data_set('wall2','FiltSel2','C2203696_Ds01.xlsx', "Step 03.1: Verify Pop up data doesn't have hyper link")
        try:
            driver.find_element_by_css_selector("#wall2 #FiltSel2 span").get_attribute('href')
        except:
            utillobj.asequal(False,False,"Step 03.2: Verify value doesn't have  href(hyperlink)")
        
        """
        Step 04:Go back and run the request again but uncomment the following line:
        -*WHERE RECORDLIMIT EQ 20 
        """
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("102803a.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary('0','20of20records,Page1of1', 'Step 04.1: Verify Page summary 20of20')
        column=['MOVIECODE','TITLE']
        miscelanousobj.verify_column_heading('ITableData0', column, "Step 04.2: Verify Column heading of 102803a.fex")
        utillobj.verify_data_set('ITableData0','I0r','102803a.xlsx',"Step 04.3: Verify 102803a.fex dataset")
        
        """
        Step 05: When the report is displayed / Select the drop down arrow next to Moviecode.
        Select Filter / Equals
        """
        time.sleep(5)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Filter','Equals')
        
        """
        Step 06: In the Filter selection click on the drop down arrow to display values.
        Verify values are displayed as normal text without hyperlinks.
        """
        driver.find_element_by_css_selector(".arFilterItem #ftp1_1_0 img").click()
        menu_list=['001MCA', '005WAR', '020TUR', '024WAR', '031KKV', '035CBS', '040ORI', '043DIS', '053WAR', '076WAR', '081MCA', '082MCA', '090CBS', '093WOR', '095CBS', '103LOR', '104MED', '128VES', '139RCA', '145MGM']
        filterselectionobj.verify_filter_values_menu_list(1, menu_list, 'Step 06.1: Verify all values are present')
        try:
            a=driver.find_element_by_css_selector("set0_ftp1_1_0_x__0_0i_t").get_attribute('href')
        except:
            utillobj.asequal(False,False,"Step 06.2: Verify value doesn't have  href(hyperlink)")
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        