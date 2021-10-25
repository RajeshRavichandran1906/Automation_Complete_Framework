'''
Created on Aug 26, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050560
Description : 

DATE field tests.
These tests use Filter, then:

Greater than
Greater than or equal to
Less than
Less than or equal to
Between
Not Between
Contains
Contains(match case)
Omits
Omits(case match)

'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import unittest, time


class C2050562_TestClass(BaseTestCase):

    def test_C2050562(self):
        
        """
            TESTCASE VARIABLES
        """
        
        """
            Step 01:   Execute the attached AR-RP-141DT

        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-141DT.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
       
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01:  Expect to see the following Active Report. - page summary verification")
                 
        
        """Step 02 :      
         
        For the following DATETIME fields, select Filter, then Greater than and use these values:
         
        HYYMDSA - 2011/03/30 10:23:24PM
        HYY Datetime - 2002
        HHISA Datetime - 12:13:14PM
        HYYMDIA Datetime - 01/01/2013 00:00
        HYYMDm Datetime - 2013/04/04 00:00:00.000000
        HYYMDn Datetime - 2013/01/01 00:00:00.000000000
        HYYMDH Datetime - 2013/04/04 00
        HDMtY Datetime - 14 Jul 13
 
        """
  
        #Expect 985 rows - all Greater than 2011/03/30 10:23:24PM
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Greater than")
        
        
        filterselectionobj.create_filter(1, 'Greater than',value1='2011/03/30 10:23:24PM')
        
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '985of1000records,Page1of18', "Step 02: Expect 985 rows - all Greater than 2011/03/30 10:23:24PM")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 10 rows - all Greater than 2002
         
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Greater than")
         
        filterselectionobj.create_filter(1, 'Greater than',value1='2002')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 02: Expect 10 rows - all Greater than 2002")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 10 rows - all Greater than 12:13:14PM
         
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Greater than")
          
        filterselectionobj.create_filter(1, 'Greater than',value1='12:13:14PM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 02:Expect 10 rows - all Greater than 12:13:14PM")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
         
        #Expect 20 rows - all Greater than 01/01/2013 00:00
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Greater than")
         
        filterselectionobj.create_filter(1, 'Greater than',value1='01/01/2013 00:00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '20of1000records,Page1of1', "Step 02: Expect 20 rows - all Greater than 01/01/2013 00:00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 15 rows - all Greater than 2013/04/04 00:00:00.000000
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Greater than")
         
        filterselectionobj.create_filter(1, 'Greater than',value1='2013/04/04 00:00:00.000000')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 02: Expect 15 rows - all Greater than 2013/04/04 00:00:00.000000")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 20 rows - all Greater than 2013/01/01 00:00:00.000000000
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Greater than")
         
        filterselectionobj.create_filter(1, 'Greater than',value1='2013/01/01 00:00:00.000000000')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '20of1000records,Page1of1', "Step 02:Expect 20 rows - all Greater than 2013/01/01 00:00:00.000000000")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
 
        #Expect 15 rows - all Greater than 2013/04/04 00
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Greater than")
         
        filterselectionobj.create_filter(1, 'Greater than',value1='2013/04/04 00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 02: Expect 15 rows - all Greater than 2013/04/04 00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 10 rows - all Greater than 14 Jul 13
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Greater than")
         
        filterselectionobj.create_filter(1, 'Greater than',value1='14 Jul 13')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 02:Expect 10 rows - all Greater than 14 Jul 13")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        
        """Step 03: FFor the following DATETIME fields, select Filter, then Greater than or equal to and use these values:
 
        HYYMDSA - 2011/03/30 10:23:24PM
         
        HYY Datetime - 2002
        HHISA Datetime - 12:13:14PM
        HYYMDIA Datetime - 01/01/2013 00:00
        HYYMDm Datetime - 2013/04/04 00:00:00.000000  
        HYYMDn Datetime - 2013/01/01 00:00:00.000000000
        HYYMDH Datetime - 2013/04/04 00
        HDMtY Datetime - 14 Jul 13
 
        """
 
         
        # Expect 990 rows - all Greater than or equal to 2011/03/30 10:23:24PM
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141DT.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='2011/03/30 10:23:24PM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '990of1000records,Page1of18', "Step 03: Expect 990 rows - all Greater than or equal to 2011/03/30 10:23:24PM")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 1000 rows - all Greater than or equal to 2002
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='2002')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03: Expect 10000 rows - all Greater than or equal to 2002")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        # Expect 15 rows - all Greater than or equal to 12:13:14PM
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='12:13:14PM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 03:  Expect 15 rows - all Greater than or equal to 12:13:14PM")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        # Expect 1000 rows - all Greater than or equal to 01/01/2013 00:00
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='01/01/2013 00:00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03:  Expect 1000 rows - all Greater than or equal to 01/01/2013 00:00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 20 rows - all Greater than or equal to 2013/04/04 00:00:00.000000
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='2013/04/04 00:00:00.000000')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '20of1000records,Page1of1', "Step 03: Expect 20 rows - all Greater than or equal to 2013/04/04 00:00:00.000000")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #  Expect 10 rows - all Greater than or equal to 2013/10/04 00:00:00.000000000
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='2013/10/04 00:00:00.000000000')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 03:   Expect 10 rows - all Greater than or equal to 2013/10/04 00:00:00.000000000")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
       
        # Expect 15 rows - all Greater than or equal to 2013/07/14 00
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='2013/07/14 00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 03:Expect 15 rows - all Greater than or equal to 2013/07/14 00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 20 rows - all Greater than or equal to 04 Apr 13
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='04 Apr 13')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '20of1000records,Page1of1', "Step 03: Expect 20 rows - all Greater than or equal to 04 Apr 13")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
         
 
        """Step 04: For the following DATETIME fields, select Filter, then Less than and use these values:
 
        HYYMDSA - 2011/03/30 10:23:24PM
        HYY Datetime - 2013
        HHISA Datetime - 12:13:14PM
        HYYMDIA Datetime - 04/04/2013 00:00
        HYYMDm Datetime - 2013/04/04 00:00:00.000000
        .
        HYYMDn Datetime - 2013/10/04 00:00:00.000000000
        .
        HYYMDH Datetime - 2013/04/04 00
        HDMtY Datetime - 14 Jul 13
 
        """
         
        #Expect 10 rows - all Less than 2011/03/30 10:23:24PM
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141DT.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='2011/03/30 10:23:24PM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 04: Expect 10 rows - all Less than 2011/03/30 10:23:24PM")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        time.sleep(3)
         
         
        #Expect 990 rows - all Less than 2013
         
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter", "Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='2013')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '990of1000records,Page1of18', "Step 04: Expect 990 rows - all Less than 2013")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 985 rows - all Less than 12:13:14PM
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='12:13:14PM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '985of1000records,Page1of18', "Step 04: Expect 985 rows - all Less than 12:13:14PM")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 980 rows - all Less than 04/04/2013 00:00
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='04/04/2013 00:00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '980of1000records,Page1of18', "Step 04: Expect 980 rows - all Less than 04/04/2013 00:00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 0 rows - none are Less than than 2013/01/01 00:00:00.000000
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='2013/01/01 00:00:00.000000')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 04: Expect 0 rows - none are Less than than 2013/01/01 00:00:00.000000")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 990 rows - all Less than 2013/10/04 00:00:00.000000000
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='2013/10/04 00:00:00.000000000')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '990of1000records,Page1of18', "Step 04: Expect 990 rows - all Less than 2013/10/04 00:00:00.000000000")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 980 rows - all Less than 2013/04/04 00
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='2013/04/04 00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '980of1000records,Page1of18', "Step 04: Expect 980 rows - all Less than 2013/10/04 00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 985 rows - all Less than 14 Jul 13
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='14 Jul 13')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '985of1000records,Page1of18', "Step 04: Expect 985 rows - all Less than 14 Jul 13")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
         
        """Step 05:  For the following DATETIME fields, select Filter, then Less than or equal to and use these values:
 
        HYYMDSA - 2011/03/30 10:23:24PM
         
        HYY Datetime - 2013
        HHISA Datetime - 12:13:14PM
         
        HYYMDIA Datetime - 04/04/2013 00:00
         
        HYYMDm Datetime - 2013/04/04 00:00:00.000000
        .
        HYYMDn Datetime - 2013/10/04 00:00:00.000000000
        .
        HYYMDH Datetime - 2013/10/04 00
        HDMtY Datetime - 01 Jan 13
 
 
        """
   
         
        # Expect 15 rows - all Less than or equal to 2011/03/30 10:23:24PM
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141DT.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60) 
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='2011/03/30 10:23:24PM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 05: Expect 15 rows - all Less than or equal to 2011/03/30 10:23:24PM")
        time.sleep(5)                         
        filterselectionobj.close_filter_dialog()
        # Expect 1000 rows - all Less than or equal to 2013
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" ,"Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='2013')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 05: Expect 1000 rows - all Less than or equal to 2013")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
             
        #Expect 990 rows - all Less than or equal to 12:13:14PM
        time.sleep(3)
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='12:13:14PM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '990of1000records,Page1of18', "Step 05: Expect 990 rows - all Less than or equal to 12:13:14PM")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 985 rows - all Less than or equal to 04/04/2013 00:00
        time.sleep(3)
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='04/04/2013 00:00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '985of1000records,Page1of18', "Step 05: Expect 985 rows - all Less than or equal to 04/04/2013 00:00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 980 rows - all Less than or equal to 2013/01/01 00:00:00.000000
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='2013/01/01 00:00:00.000000')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '980of1000records,Page1of18', "Step 05: Expect 980 rows - all Less than or equal to 2013/01/01 00:00:00.000000")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 1000 rows - all Less than or equal to 2013/10/04 00:00:00.000000000
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='2013/10/04 00:00:00.000000000')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 05: Expect 1000 rows - all Less than or equal to 2013/10/04 00:00:00.000000000")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
    
        #Expect 990 rows - all Less than or equal to 2013/01/01 00
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='2013/01/01 00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '980of1000records,Page1of18', "Step 05: Expect 980 rows - all Less than or equal to 2013/10/04 00 As per Dan Mail")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        # Expect 980 rows - all Less than or equal to 01 Jan 13
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='04 Apr 13')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '985of1000records,Page1of18', "Step 05: Expect 985 rows - all Less than or equal to 01 Jan 13 As per Dan Mail")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
         
 
        """Step 06: For the following DATETIME fields, select Filter, then Between and use the pairs of values:
 
        HYYMDSA - 2011/03/30 10:23:24PM & 2013/10/04 1:02:03AM
         
        HYY Datetime - 2002 & 2013
        HHISA Datetime - 12:13:14PM & 10:23:24PM
         
        HYYMDIA Datetime - 04/04/2013 00:00 & 10/04/2013 00:00
         
        HYYMDm Datetime - 2013/07/14 00:00:00.000000 & 2013/10/04 00:00:00.000000
        .
        HYYMDn Datetime - 2013/01/01 00:00:00.000000000 & 2013/04/04 00:00:00.000000000
        .
        HYYMDH Datetime - 2013/07/14 00 & 2013/10/04 00
         
        HDMtY Datetime - 04 Apr 13 & 14 Jul 13
 
 
        """
 
         
        #Expect 990 rows - all Between 2011/03/30 10:23:24PM & 2013/10/04 1:02:03AM
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141DT.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60) 
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='2011/03/30 10:23:24PM', value2='2013/10/04 1:02:03AM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '990of1000records,Page1of18', "Step 06: Expect 990 rows - all Between 2011/03/30 10:23:24PM & 2013/10/04 1:02:03AM")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
       
        #Expect 1000 rows - all Between 2002 & 2013
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" ,"Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='2002', value2='2013')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 06: Expect 1000 rows - all Between 2002 & 2013")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
         
        #Expect 10 rows - all Between 12:13:14PM & 10:23:24PM
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='12:13:14PM', value2='10:23:24PM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 06: Expect 10 rows - all Between 12:13:14PM & 10:23:24PM")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 20 rows - all Between 04/04/2013 00:00 & 10/04/2013 00:00
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='04/04/2013 00:00',value2='10/04/2013 00:00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '20of1000records,Page1of1', "Step 06: Expect 20 rows - all Between 04/04/2013 00:00 & 10/04/2013 00:00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 15 rows - all Between 2013/07/14 00:00:00.000000 & 2013/10/04 00:00:00.000000
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='2013/07/14 00:00:00.000000', value2='2013/10/04 00:00:00.000000')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 06: Expect 15 rows - all Between 2013/07/14 00:00:00.000000 & 2013/10/04 00:00:00.000000")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 985 rows - all Between 2013/01/01 00:00:00.000000000 & 2013/04/04 00:00:00.000000000
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='2013/01/01 00:00:00.000000000', value2='2013/04/04 00:00:00.000000000')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '985of1000records,Page1of18', "Step 06: Expect 985 rows - all Between 2013/01/01 00:00:00.000000000 & 2013/04/04 00:00:00.000000000")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
   
         
        # Expect 15 rows - all Between 2013/07/14 00 & 2013/10/04 00
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='2013/07/14 00', value2='2013/10/04 00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 06: Expect 15 rows - all Between 2013/07/14 00 & 2013/10/04 00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 10 rows - all Between 04 Apr 13 & 14 Jul 13
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='04 Apr 13', value2='14 Jul 13')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 06: Expect 10 rows - all Between 04 Apr 13 & 14 Jul 13")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        """Step 07:For the following DATETIME fields, select Filter, then Not Between and use the pairs of values:
 
        HYYMDSA - 2011/03/30 10:23:24PM & 2013/10/04 1:02:03AM
        HYY Datetime - 2002 & 2013
         
        HHISA Datetime - 12:13:14PM & 10:23:24PM
        HYYMDIA Datetime - 04/04/2013 00:00 & 10/04/2013 00:00
        HYYMDm Datetime - 2013/07/14 00:00:00.000000 & 2013/10/04 00:00:00.000000
        HYYMDn Datetime - 2013/01/01 00:00:00.000000000 & 2013/04/04 00:00:00.000000000
        HYYMDH Datetime - 2013/01/04 00 & 2013/04/04 00
         
        HDMtY Datetime - 04 Apr 13 & 14 Jul 13
 
        """
        
         
        #Expect 10 rows - all Not Between 2011/03/30 10:23:24PM & 2013/10/04 1:02:03AM
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141DT.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
         
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='2011/03/30 10:23:24PM', value2='2013/10/04 1:02:03AM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 07: Expect 10 rows - all Not Between 2011/03/30 10:23:24PM & 2013/10/04 1:02:03AM")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
      
        #Expect 0 rows - none are Not Between Between 2002 & 2013
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" , "Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='2002', value2='2013')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 07: Expect 0 rows - none are Not Between Between 2002 & 2013")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 990 rows - all Between 12:13:14PM & 10:23:24PM
        
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='12:13:14PM', value2='10:23:24PM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '990of1000records,Page1of18', "Step 07:Expect 990 rows - all Between 12:13:14PM & 10:23:24PM")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        # Expect 980 rows - all Between 04/04/2013 00:00 & 10/04/2013 00:00
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='04/04/2013 00:00',value2='10/04/2013 00:00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '980of1000records,Page1of18', "Step 07:  Expect 980 rows - all Between 04/04/2013 00:00 & 10/04/2013 00:00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 985 rows - all Between 2013/07/14 00:00:00.000000 & 2013/10/04 00:00:00.000000
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='2013/07/14 00:00:00.000000', value2='2013/10/04 00:00:00.000000')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '985of1000records,Page1of18', "Step 07:Expect 985 rows - all Between 2013/07/14 00:00:00.000000 & 2013/10/04 00:00:00.000000")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        # Expect 15 rows - all Between 2013/01/01 00:00:00.000000000 & 2013/04/04 00:00:00.000000000
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='2013/01/01 00:00:00.000000000', value2='2013/04/04 00:00:00.000000000')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 07: Expect 15 rows - all Between 2013/01/01 00:00:00.000000000 & 2013/04/04 00:00:00.000000000")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
 
        #Expect 985 rows - all Between 2013/07/14 00 & 2013/10/04 00
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='2013/07/14 00', value2='2013/10/04 00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)  
         
        miscelanousobj.verify_page_summary(0, '985of1000records,Page1of18', "Step 07: Expect 867 rows - values 140.00CR & 125.00CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 990 rows - all Between 04 Apr 13 & 14 Jul 13
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141DT.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Not Between")
        
        filterselectionobj.create_filter(1, 'Not Between',value1='04 Apr 13', value2='14 Jul 13')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '990of1000records,Page1of18', "Step 07: Expect 460 rows - not between Wednesday & Friday")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        """Step 08: For the following DATE fields, select Filter, then Contains, then enter the strings below.
        Case does not need to match.
        Only fields containing multiple alphanumeric characters are included.
        
        HYYMDSA - pm
        HHISA Datetime - AM
        HDMtY Datetime - apr
        """
        
        #Expect 15 rows - all containing the string 'PM'
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Contains")
        
        filterselectionobj.create_filter(1, 'Contains',value1='PM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 08: Expect 15 rows - all containing the string 'PM'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 985 rows - all containing the string 'AM'
        
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter" , "Contains")
        
        filterselectionobj.create_filter(1, 'Contains',value1='AM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '985of1000records,Page1of18', "Step 08: Expect 985 rows - all containing the string 'AM'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 5 rows - all containing the string 'Apr'
        
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Contains")
        
        filterselectionobj.create_filter(1, 'Contains',value1='Apr')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '5of1000records,Page1of1', "Step 08: Expect 5 rows - all containing the string 'Apr'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
 
        
        """Step 09: For the following DATE fields, select Filter, then Contains, then enter the strings below.
        Exact case match is required for filtering
        Only fields containing multiple alphanumeric characters are included.
        
        HYYMDSA - pm
        HYYMDSA - PM
        HHISA Datetime - am
        HHISA Datetime - AM
        HDMtY Datetime - apr
        HDMtY Datetime - Apr
        """   
        #Expect 0 rows - none containing the string 'pm'
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141DT.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Contains (match case)")
        
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='pm')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09: Expect 0 rows - none containing the string 'pm'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 15 rows - all containing the string 'PM'
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter" , "Contains (match case)")
        
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='PM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 09: Expect 15 rows - all containing the string 'PM'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 0 rows - none containing the string 'am'
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Contains (match case)")
        
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='am')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09: Expect 0 rows - none containing the string 'am'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 985 rows - all containing the string 'AM'
        
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Contains (match case)")
        
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='AM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '985of1000records,Page1of18', "Step 09: Expect 985 rows - all containing the string 'AM'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 0 rows - none containing the string 'apr'
        
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Contains (match case)")
        
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='apr')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09:Expect 0 rows - none containing the string 'apr'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 5 rows - all containing the string 'Apr'
        
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Contains (match case)")
        
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='Apr')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '5of1000records,Page1of1', "Step 09: Expect 5 rows - none containing the string 'Apr'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()

        
        """Step 10: 

        For the following DATE fields, select Filter, then Omits, then enter the strings below.
        Case does not need to match.
        Only fields containing multiple alphanumeric characters are included.
        
        HYYMDSA - pm
        HHISA Datetime - AM
        HDMtY Datetime - apr

        """
       

        #Expect 985 rows - all omitting the string 'PM'
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141DT.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Omits")        
        filterselectionobj.create_filter(1, 'Omits',value1='pm')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '985of1000records,Page1of18', "Step 10: Expect 985 rows - all omitting the string 'PM'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 15 rows - all omitting the string 'AM'
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter" , "Omits")
        
        filterselectionobj.create_filter(1, 'Omits',value1='AM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 10: Expect 15 rows - all omitting the string 'AM'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 995 rows - all omitting the string 'Apr'
        
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Omits")
        
        filterselectionobj.create_filter(1, 'Omits',value1='Apr')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '995of1000records,Page1of18', "Step 10: Expect 995 rows - all omitting the string 'Apr'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        """Step 11: For the following DATE fields, select Filter, then Omits (match case), then enter the strings below.
        Exact case match is required for filtering
        Only fields containing multiple alphanumeric characters are included.
        
        HYYMDSA - pm  
        HYYMDSA - PM
        HHISA Datetime - am
        HHISA Datetime - AM
        HDMtY Datetime - apr
        HDMtY Datetime - Apr

        """  
        # Expect 1000 rows - all omitting the string 'pm'
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Omits (match case)")
        
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='pm')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11: Expect 1000 rows - all omitting the string 'pm'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 985 rows - all omitting the string 'PM'
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter" , "Omits (match case)")
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='PM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '985of1000records,Page1of18', "Step 11: Expect 985 rows - all omitting the string 'PM'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 1000 rows - all omitting the string 'am'
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Omits (match case)")
        
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='am')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11: Expect 1000 rows - all omitting the string 'am''")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 15 rows - all omitting the string 'AM'
        
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Omits (match case)")
        
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='AM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 11:Expect 15 rows - all omitting the string 'AM'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 1000 rows - all omitting the string 'apr'
        
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Omits (match case)")
        
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='apr')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11: Expect 1000 rows - all omitting the string 'apr'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        #Expect 995 rows - all omitting the string 'Apr'
        
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Omits (match case)")
        
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='Apr')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '995of1000records,Page1of18', "Step 11: Expect 995 rows - all omitting the string 'Apr'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()

        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        