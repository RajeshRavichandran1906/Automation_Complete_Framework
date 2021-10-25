'''
Created on Sep 1, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053843
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,active_pivot_comment
from common.lib import utillity

class C2053843_TestClass(BaseTestCase):

    def test_C2053843(self):
        """
            TESTCASE VARIABLES
        """
        
        """
        Step 01: Generate the initial report by executing fex.
        """
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        pivobj=active_pivot_comment.Active_Pivot_Comment(self.driver)
        
        utillobj.active_run_fex_api_login('AR_RP_CALCULATE.fex','S7078','mrid','mrpass')    
        misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 01.1: Verify Page summary 1000of1000')
        
        """
        Step 02: Create a new Pivot Table by selecting P9.2M Unit Price and from the drop down list, 
        select Pivot(Cross Tab), move to Group BY(SUM) and select ALPHA Store Code, move to Across and 
        select Date YYMD for the Across.
        Expect to see this Pivot Table. Notice that the lock icon is open.
        """
        time.sleep(5)
        misobj.select_menu_items('ITableData0', 6, 'Pivot (Cross Tab)','ALPHA Store Code','Date YYMD')
        unlock = "//div[@id='LINKIMG1_-1']//img[contains(@src,'AAAAAElFTkSuQmCC')]"
        lock = "//div[@id='LINKIMG1_-1']//img[contains(@src,'AAAAABJRU5ErkJggg')]"
        utillobj.asequal(len(self.driver.find_elements_by_xpath(unlock)),1,"Step 02.1: Verify freeze icon is unlocked")
        utillobj.verify_pivot_data_set('piv1', 'C2053843_Ds01.xlsx', "Step 02.2: Verify Pivot dataset")
         
        """
        Step 03: Click the lock icon in the tool bar of the Pivot Table.
        Expect to see the lock icon close. Very subtle change to icon.
        """
        pivobj.click_pivot_menu_bar_items('wall1', 1)
        utillobj.asequal(len(self.driver.find_elements_by_xpath(lock)),1,"Step 03.1: Verify freeze icon is locked")
        
        """
        Step 04: Go back to the Report and click the drop down arrow for the ALPHA Store Code field. Select Filter, 
        then Not equal.
        Expect to see the Filter selection box appear for ALPHA Store Code.
        """
        misobj.move_active_popup(1,600,200)
        misobj.select_menu_items('ITableData0', 1, 'Filter', 'Not equal')
        misobj.move_active_popup(2,10,-650)
        
        """
        Step 05: Click the drop down arrow and select R1019 for the value from the list of values.
        Expect to see R1019 appear in the Filter box.
        """        
        active_filter.create_filter(1, 'Not equal',popup_id='wall2',value1='R1019')
        active_filter.verify_filter_selection_dialog(True,'Step 05.1: Verify filter row.',['ALPHA Store Code','Not equal','R1019'],popup_id="wall2")
        
        """
        Step 06: Click the Filter button.
        Expect to see the report no longer contains ALPHA Store Code of R1019.
        """
        active_filter.filter_button_click('Filter',popup_id="wall2")
#         utillobj.create_data_set('ITableData0','I0r','C2053843_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2053843_Ds02.xlsx','Step 06.1: Verify dataset ALPHA Store Code Not Equal R1019')
        
        """
        Step 07: Switch back to the Pivot Table.
        Expect to see that the Pivot Table still contains ALPHA Store Code of R1019.
        """
        utillobj.verify_pivot_data_set('piv1', 'C2053843_Ds01.xlsx', "Step 07.1: Verify Pivot dataset still contains ALPHA Store Code of R1019")
        
        """
        Step 08: In the Pivot Table, click the lock icon again.
        Expect to see that the lock is again open and that 
        ALPHA Store Code value R1019 is automatically removed from the Pivot Table.
        """
        misobj.move_active_popup(2,10,600)
        unlock = "//div[@id='LINKIMG1_-1']//img[contains(@src,'AAAAAElFTkSuQmCC')]"
        lock = "//div[@id='LINKIMG1_-1']//img[contains(@src,'AAAAABJRU5ErkJggg')]"
        pivobj.click_pivot_menu_bar_items('wall1', 1)
        utillobj.asequal(len(self.driver.find_elements_by_xpath(unlock)),1,"Step 08.1: Verify freeze icon is unlocked")
        utillobj.verify_pivot_data_set('piv1', 'C2053843_Ds03.xlsx', "Step 08.2: Verify Pivot dataset ALPHA Store Code value R1019 is automatically removed")
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
