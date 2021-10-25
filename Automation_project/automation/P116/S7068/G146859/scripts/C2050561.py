'''
Created on Aug 25, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050561
TestCase Name = AHTML: Verify Filter operators against various DATETIME fields(Part 1).
'''
import unittest,time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from common.lib import take_screenshot
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators


class C2050561_TestClass(BaseTestCase):

    def test_C2050561(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050561'
        """
        Step 01: Execute the attached AR-RP-141DT.
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-141DT.fex','S7068','mrid','mrpass')      
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 01.1: Verify Page summary 1000of1000records')
        column=['Order Number INTEGER','HYYMDSA','HYY Datetime','HHISA Datetime','HYYMDIA Datetime','HYYMDm Datetime','HYYMDn Datetime','HYYMDH Datetime','HDMtY Datetime']
        active_misobj.verify_column_heading('ITableData0',column, "Step 01.2: Expect to see column headings for AR-RP-141DT")
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-141DT_page1.xlsx',"Step 01.3: Verify Data set of AR-RP-141DT page1")
        time.sleep(5) 
        """
        Step 02: For the following DATE fields, select Filter, then Equals and use these values:
        """
        """HYYMDSA - 2011/03/30 10:23:24PM"""
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2011/03/30 10:23:24PM')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 5 rows - all Equal to 2011/03/30 10:23:24PM"""
        active_misobj.verify_page_summary('0','5of1000records,Page1of1', 'Step 02.3: Verify Page summary 5of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.4: Verify Page summary 1000of1000records after close dialog')
            
        """HYY Datetime - 2013"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2013')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 10 rows - all Equal to 2013"""
        active_misobj.verify_page_summary('0','10of1000records,Page1of1', 'Step 02.5: Verify Page summary 10of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.6: Verify Page summary 1000of1000records after close dialog')
            
        """HHISA Datetime - 12:13:14PM"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='12:13:14PM')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 5 rows - all Equal to 12:13:14PM """
        active_misobj.verify_page_summary('0','5of1000records,Page1of1', 'Step 02.7: Verify Page summary 5of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.8: Verify Page summary 1000of1000records after close dialog')
             
        """HYYMDIA Datetime - 10/04/2013 00:00"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='10/04/2013 00:00')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 10 rows - all Equal to 10/04/2013 00:00"""
        active_misobj.verify_page_summary('0','10of1000records,Page1of1', 'Step 02.9: Verify Page summary 10of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.10: Verify Page summary 1000of1000records after close dialog')
            
        """HYYMDm Datetime - 2013/01/01 00:00:00.000000"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2013/01/01 00:00:00.000000')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 980 rows - all Equal to 2013/01/01 00:00:00.000000 """
        active_misobj.verify_page_summary('0','980of1000records,Page1of18', 'Step 02.11: Verify Page summary 980of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.12: Verify Page summary 1000of1000records after close dialog')
           
        """HYYMDn Datetime - 2013/04/04 00:00:00.000000000"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2013/04/04 00:00:00.000000000')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 5 rows - all Equal to 2013/04/04 00:00:00.000000000"""
        active_misobj.verify_page_summary('0','5of1000records,Page1of1', 'Step 02.11: Verify Page summary 5of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.12: Verify Page summary 1000of1000records after close dialog')
            
        """HYYMDH Datetime - 2013/10/04 00"""
        active_misobj.select_menu_items('ITableData0', 7, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2013/10/04 00')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 10 rows - all Equal to 2013/10/04 00"""
        active_misobj.verify_page_summary('0','10of1000records,Page1of1', 'Step 02.13: Verify Page summary 180of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.14: Verify Page summary 1000of1000records after close dialog')
            
        """HDMtY Datetime - 04 Apr 13"""
        active_misobj.select_menu_items('ITableData0', 8, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='04 Apr 13')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 5 rows - all Equal to 04 Apr 13"""
        active_misobj.verify_page_summary('0','5of1000records,Page1of1', 'Step 02.15: Verify Page summary 5of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.16: Verify Page summary 1000of1000records after close dialog')
        driver.refresh()
        time.sleep(1)
         
        """
        Step 03: For the following DATE fields, select Filter, then Equals and use these multiple values:
        """
        """HYYMDSA - 2007/08/08 12:13:14PM & 2011/03/30 10:23:24PM"""
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2007/08/08 12:13:14PM',value2='2011/03/30 10:23:24PM')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 10 rows - all Equal to 2007/08/08 12:13:14PM or 2011/03/30 10:23:24PM"""
        active_misobj.verify_page_summary('0','10of1000records,Page1of1', 'Step 03.1: Verify Page summary 10of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.2: Verify Page summary 1000of1000records after close dialog')
            
        """HYY Datetime - 2002 & 2013"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2002',value2='2013')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 1000 rows - all Equal to 2002 or 2013"""
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.3: Verify Page summary 1000of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.4: Verify Page summary 1000of1000records after close dialog')
            
        """HHISA Datetime - 12:13:14PM & 11:59:59PM & 10:23:24PM"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='12:13:14PM',value2='11:59:59PM',value3='10:23:24PM')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 15 rows - all Equal to 12:13:14PM or 11:59:59PM or 10:23:24PM"""
        active_misobj.verify_page_summary('0','15of1000records,Page1of1', 'Step 03.5: Verify Page summary 15of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.6: Verify Page summary 1000of1000records after close dialog')
             
        """HYYMDIA Datetime - 04/04/2013 00:00 & 07/14/2013 00:00"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='04/04/2013 00:00',value2='07/14/2013 00:00')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 10 rows - all Equal to 04/04/2013 00:00 or 07/14/2013 00:00"""
        active_misobj.verify_page_summary('0','10of1000records,Page1of1', 'Step 03.7: Verify Page summary 10of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.8: Verify Page summary 1000of1000records after close dialog')
            
        """HYYMDm Datetime - 2013/04/04 00:00:00.000000 & 2013/07/14 00:00:00.000000"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2013/04/04 00:00:00.000000',value2='2013/07/14 00:00:00.000000')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 10 rows - all Equal to 2013/04/04 00:00:00.000000 or 2013/07/14 00:00:00.000000"""
        active_misobj.verify_page_summary('0','10of1000records,Page1of1', 'Step 03.9: Verify Page summary 10of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.10: Verify Page summary 1000of1000records after close dialog')
            
        """HYYMDn Datetime - 2013/07/14 00:00:00.000000000 & 2013/10/04 00:00:00.000000000"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2013/07/14 00:00:00.000000000',value2='2013/10/04 00:00:00.000000000')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 15 rows - all Equal to 2013/07/14 00:00:00.000000000 or 2013/10/04 00:00:00.000000000"""
        active_misobj.verify_page_summary('0','15of1000records,Page1of1', 'Step 03.11: Verify Page summary 15of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.12: Verify Page summary 1000of1000records after close dialog')
            
        """HYYMDH Datetime - 2013/01/01 00 & 2013/10/04 00"""
        time.sleep(5)
        active_misobj.select_menu_items('ITableData0', 7, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2013/01/01 00',value2='2013/10/04 00')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 990 rows - all Equal to 2013/01/01 00 or 2013/10/04 00"""
        active_misobj.verify_page_summary('0','990of1000records,Page1of18', 'Step 03.13: Verify Page summary 990of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.14: Verify Page summary 1000of1000records after close dialog')
            
        """HDMtY Datetime - 04 Apr 13 & 14 Jul 13 & 04 Oct 13"""
        active_misobj.select_menu_items('ITableData0', 8, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='04 Apr 13',value2='14 Jul 13',value3='04 Oct 13')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 20 rows - all Equal to 04 Apr 13 or 14 Jul 13 or 04 Oct 13"""
        active_misobj.verify_page_summary('0','20of1000records,Page1of1', 'Step 03.15: Verify Page summary 20of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.16: Verify Page summary 1000of1000records after close dialog')
        driver.refresh()
        time.sleep(1)
            
        """
        Step 04:For the following DATE fields, select Filter, then Equals and use these values:
        Click the Highlight button instead of the Filter button.
        """
        """HYYMDSA - 2011/03/30 10:23:24PM"""
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2011/03/30 10:23:24PM')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value 2011/03/30 10:23:24PM to be Highlighted."""
        active_misobj.move_active_popup("1", "1000", "200")
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds01_Page1.xlsx',"Step 04.1: Verify highlighted dataset 2011/03/30 10:23:24PM")
        time.sleep(10)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.2: Verify Page summary 1000of1000records after close dialog')
            
        """HYY Datetime - 2013"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2013')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value 2011/03/30 10:23:24PM to be Highlighted."""
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds02_Page1.xlsx',"Step 04.3: Verify highlighted dataset 2013")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.4: Verify Page summary 1000of1000records after close dialog')
            
        """HHISA Datetime - 12:13:14PM"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='12:13:14PM')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value 12:13:14PM to be Highlighted."""
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds03_Page1.xlsx',"Step 04.5: Verify highlighted dataset 12:13:14PM")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.6: Verify Page summary 1000of1000records after close dialog')
             
        """HYYMDIA Datetime - 10/04/2013 00:00"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='10/04/2013 00:00')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value 10/04/2013 00:00 to be Highlighted."""
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds04_Page1.xlsx',"Step 04.7: Verify highlighted dataset 0/04/2013 00:00")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.8: Verify Page summary 1000of1000records after close dialog')
            
        """HYYMDm Datetime - 2013/01/01 00:00:00.000000"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2013/01/01 00:00:00.000000')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value 2013/01/01 00:00:00.000000 to be Highlighted."""
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds05_Page1.xlsx',"Step 04.9: Verify highlighted dataset 2013/01/01 00:00:00.000000")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.10: Verify Page summary 1000of1000records after close dialog')
            
        """HYYMDn Datetime - 2013/04/04 00:00:00.000000000"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2013/04/04 00:00:00.000000000')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value 2013/04/04 00:00:00.000000000 to be Highlighted."""
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds06_Page1.xlsx',"Step 04.11: Verify highlighted dataset 2013/04/04 00:00:00.000000000")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.12: Verify Page summary 1000of1000records after close dialog')
            
        """HYYMDH Datetime - 2013/10/04 00"""
        active_misobj.select_menu_items('ITableData0', 7, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='2013/10/04 00')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value 2013/10/04 00 to be Highlighted."""
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds07_Page1.xlsx',"Step 04.13: Verify highlighted dataset 2013/10/04 00")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.14: Verify Page summary 1000of1000records after close dialog')
            
        """HDMtY Datetime - 04 Apr 13"""
        active_misobj.select_menu_items('ITableData0', 8, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='04 Apr 13')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value 04 Apr 13 to be Highlighted."""
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds08_Page1.xlsx',"Step 04.15: Verify highlighted dataset 04 Apr 13")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.16: Verify Page summary 1000of1000records after close dialog')
        driver.refresh()
        time.sleep(1)
            
        """
        Step 05: For the following DATE fields, select Filter, then Not equal and use these values
        """
        """HYYMDSA - 2011/03/30 10:23:24PM"""
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2011/03/30 10:23:24PM')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 995 rows - all Not equal to 2011/03/30 10:23:24PM"""
        active_misobj.verify_page_summary('0','995of1000records,Page1of18', 'Step 05.1: Verify Page summary 995of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.2: Verify Page summary 1000of1000records after close dialog')
             
        """HYY Datetime - 2002"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2002')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 10 rows - all Not equal to 2002"""
        active_misobj.verify_page_summary('0','10of1000records,Page1of1', 'Step 05.3: Verify Page summary 10of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.4: Verify Page summary 1000of1000records after close dialog')
             
        """HHISA Datetime - 12:13:14PM"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='12:13:14PM')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 995 rows - all Not equal to 12:13:14PM """
        active_misobj.verify_page_summary('0','995of1000records,Page1of18', 'Step 05.5: Verify Page summary 820of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.6: Verify Page summary 1000of1000records after close dialog')
              
        """HYYMDIA Datetime - 10/04/2013 00:00"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='10/04/2013 00:00')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 990 rows - all Not equal to 10/04/2013 00:00"""
        active_misobj.verify_page_summary('0','990of1000records,Page1of18', 'Step 05.7: Verify Page summary 990of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.8: Verify Page summary 1000of1000records after close dialog')
             
        """HYYMDm Datetime - 2013/01/01 00:00:00.000000"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2013/01/01 00:00:00.000000')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 20 rows - all Not equal to 2013/01/01 00:00:00.000000 """
        active_misobj.verify_page_summary('0','20of1000records,Page1of1', 'Step 05.9: Verify Page summary 20of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.10: Verify Page summary 1000of1000records after close dialog')
             
        """HYYMDn Datetime - 2013/04/04 00:00:00.000000000"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2013/04/04 00:00:00.000000000')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 995 rows - all Not equal to 2013/04/04 00:00:00.000000000"""
        active_misobj.verify_page_summary('0','995of1000records,Page1of18', 'Step 05.11: Verify Page summary 995of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.12: Verify Page summary 1000of1000records after close dialog')
             
        """HYYMDH Datetime - 2013/10/04 00"""
        active_misobj.select_menu_items('ITableData0', 7, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2013/10/04 00')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 990 rows - all Not equal to 2013/10/04 00"""
        active_misobj.verify_page_summary('0','990of1000records,Page1of18', 'Step 05.13: Verify Page summary 990of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.14: Verify Page summary 1000of1000records after close dialog')
             
        """HDMtY Datetime - 01 Jan 13"""
        active_misobj.select_menu_items('ITableData0', 8, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='01 Jan 13')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 20 rows - all Not equal to 01 Jan 13"""
        active_misobj.verify_page_summary('0','20of1000records,Page1of1', 'Step 05.15: Verify Page summary 20of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.16: Verify Page summary 1000of1000records after close dialog')
        driver.refresh()
        time.sleep(1)
         
        """
        Step 06: For the following DATE fields, select Filter, then Not equals and use these multiple values:
        """
        """HYYMDSA - 2007/08/08 12:13:14PM & 2011/03/30 10:23:24PM"""
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2007/08/08 12:13:14PM',value2='2011/03/30 10:23:24PM')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 990 rows - all Not equal to 2007/08/08 12:13:14PM or 2011/03/30 10:23:24PM"""
        active_misobj.verify_page_summary('0','990of1000records,Page1of18', 'Step 06.1: Verify Page summary 990of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.2: Verify Page summary 1000of1000records after close dialog')
             
        """HYY Datetime - 2002 & 2013"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2002',value2='2013')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 0 rows - none are Not equal to 2002 or 2013"""
        active_misobj.verify_page_summary('0','0of1000records,Page1of1', 'Step 06.3: Verify Page summary 0of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.4: Verify Page summary 1000of1000records after close dialog')
             
        """HHISA Datetime - 12:13:14PM & 11:59:59PM & 10:23:24PM"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='12:13:14PM',value2='11:59:59PM',value3='10:23:24PM')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 985 rows - all Not equal to 12:13:14PM or 11:59:59PM or 10:23:24PM"""
        active_misobj.verify_page_summary('0','985of1000records,Page1of18', 'Step 06.5: Verify Page summary 985of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.6: Verify Page summary 1000of1000records after close dialog')
              
        """HYYMDIA Datetime - 04/04/2013 00:00 & 01/01/2013 00:00"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='04/04/2013 00:00',value2='01/01/2013 00:00')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 15 rows - all Not equal to 04/04/2013 00:00 or 01/01/2013 00:00 """
        active_misobj.verify_page_summary('0','15of1000records,Page1of1', 'Step 06.7: Verify Page summary 15of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.8: Verify Page summary 1000of1000records after close dialog')
             
        """HYYMDm Datetime - 2013/04/04 00:00:00.000000 & 2013/07/14 00:00:00.000000"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2013/04/04 00:00:00.000000',value2='2013/07/14 00:00:00.000000')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 990 rows - all Not equal to 2013/04/04 00:00:00.000000 or 2013/07/14 00:00:00.000000"""
        active_misobj.verify_page_summary('0','990of1000records,Page1of18', 'Step 06.9: Verify Page summary 990of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.10: Verify Page summary 1000of1000records after close dialog')
             
        """HYYMDn Datetime - 2013/07/14 00:00:00.000000000 & 2013/10/04 00:00:00.000000000"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2013/07/14 00:00:00.000000000',value2='2013/10/04 00:00:00.000000000')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 985 rows - all Not equal to 2013/07/14 00:00:00.000000000 or 2013/10/04 00:00:00.000000000"""
        active_misobj.verify_page_summary('0','985of1000records,Page1of18', 'Step 06.11: Verify Page summary 985of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.12: Verify Page summary 1000of1000records after close dialog')
             
        """HYYMDH Datetime - 2013/01/01 00 & 2013/10/04 00"""
        active_misobj.select_menu_items('ITableData0', 7, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2013/01/01 00',value2='2013/10/04 00')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 10 rows - all Not equal to 2013/01/01 00 or 2013/10/04 00"""
        active_misobj.verify_page_summary('0','10of1000records,Page1of1', 'Step 06.13: Verify Page summary 10of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.14: Verify Page summary 1000of1000records after close dialog')
             
        """HDMtY Datetime - 01 Jan 13 & 14 Jul 13 & 04 Oct 13"""
        active_misobj.select_menu_items('ITableData0', 8, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='01 Jan 13',value2='14 Jul 13',value3='04 Oct 13')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 5 rows - all Not equal to 01 Jan 13 or 14 Jul 13 or 04 Oct 13"""
        active_misobj.verify_page_summary('0','5of1000records,Page1of1', 'Step 06.15: Verify Page summary 5of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.16: Verify Page summary 1000of1000records after close dialog')
        driver.refresh()
        time.sleep(1)   
         

        """
        Step 07: For the following DATE fields, select Filter, then Not equal and use these values:
        Click the Highlight button instead of the Filter button.
        """
        """HYYMDSA - 2011/03/30 10:23:24PM"""
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2011/03/30 10:23:24PM')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect all rows except 2011/03/30 10:23:24PM to be Highlighted."""
#         active_misobj.move_active_popup("1", "600", "200")
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds09_Page1.xlsx',"Step 07.1: Verify highlighted dataset not equal 2011/03/30 10:23:24PM")
        time.sleep(8)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.2: Verify Page summary 1000of1000records after close dialog')
        driver.refresh()
        time.sleep(1) 
            
        """HYY Datetime - 2013"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2013')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect all rows except 2013 to be Highlighted."""
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds10_Page1.xlsx',"Step 07.3: Verify highlighted dataset not equal 2013")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        """HHISA Datetime - 12:13:14PM"""
        time.sleep(5)
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='12:13:14PM')
        active_filter.filter_button_click('Highlight')
        time.sleep(8)
        """Expect all rows except 12:13:14PM to be Highlighted."""
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds011_Page1.xlsx',"Step 07.5: Verify highlighted dataset not equal 12:13:14PM")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.6: Verify Page summary 1000of1000records after close dialog')
           
        """HYYMDIA Datetime - 10/04/2013 00:00"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='10/04/2013 00:00')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect all rows except 10/04/2013 00:00 to be Highlighted."""
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds12_Page1.xlsx',"Step 07.7: Verify highlighted dataset not equal 10/04/2013 00:00")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.8: Verify Page summary 1000of1000records after close dialog')
        driver.refresh()
        time.sleep(1)
           
        """HYYMDm Datetime - 2013/01/01 00:00:00.000000"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2013/01/01 00:00:00.000000')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect all rows except 2013/01/01 00:00:00.000000 to be Highlighted."""
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds13_Page1.xlsx',"Step 07.9: Verify highlighted dataset not equal 2013/01/01 00:00:00.000000")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.10: Verify Page summary 1000of1000records after close dialog')
           
        """HYYMDn Datetime - 2013/04/04 00:00:00.000000000"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2013/04/04 00:00:00.000000000')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect all rows except 2013/04/04 00:00:00.000000000 to be Highlighted."""
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds14_Page1.xlsx',"Step 07.11: Verify highlighted dataset not equal 2013/04/04 00:00:00.000000000")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.12: Verify Page summary 1000of1000records after close dialog')
           
        """HYYMDH Datetime - 2013/10/04 00"""
        active_misobj.select_menu_items('ITableData0', 7, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='2013/10/04 00')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect all rows except 2013/10/04 00 to be Highlighted."""
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds15_Page1.xlsx',"Step 07.13: Verify highlighted dataset not equal 2013/10/04 00")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.14: Verify Page summary 1000of1000records after close dialog')
           
        """HDMtY Datetime - 04 Apr 13"""
        active_misobj.select_menu_items('ITableData0', 8, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='04 Apr 13')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect all rows except 04 Apr 13 to be Highlighted."""
        utillobj.verify_data_set('ITableData0','rgb','C2050561_Ds16_Page1.xlsx',"Step 07.15: Verify highlighted dataset not equal 04 Apr 13")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.16: Verify Page summary 1000of1000records after close dialog')
           
if __name__ == '__main__':
    unittest.main()
        
        
        