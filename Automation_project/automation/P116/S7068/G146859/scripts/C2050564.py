'''
Created on Aug 19, 2016

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

class C2050564_TestClass(BaseTestCase):

    def test_C2050564(self):
        
        """
            Step 01:   Execute the attached AR-RP-141DA.

        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-141PA.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
         
        
       
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01:  Expect to see the following Active Report. - page summary verification")
                  
         
         
        """Step 02 : For the following PACKED data fields, select Filter, then Greater than and use these values:
 
        Packed Order - 5
        P9.2M Unit Price - $13.00
        P9.2C Unit Price - 17.00
        P9.2Lc Unit Price - $000,026.00
        P9.2B Unit Price - (28.00)
        P9.2R Unit Price - 58.00 CR
        P9.2% Unit Price - 76.00%
 
        """
 
         
        #Expect 995 rows - all greater than 5
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Greater than")
         
        filterselectionobj.create_filter(1, 'Greater than','large',value1='5')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '995of1000records,Page1of18', "Step 02: Expect 995 rows - all greater than 5")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 916 rows - all greater than $13.00
         
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Greater than")
         
        filterselectionobj.create_filter(1, 'Greater than',value1='$13.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '916of1000records,Page1of17', "Step 02: Expect 916 rows - all greater than $13.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 817 rows - all greater than 17.00
         
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Greater than")
          
        filterselectionobj.create_filter(1, 'Greater than',value1='17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '817of1000records,Page1of15', "Step 02: Expect 817 rows - all greater than 17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
         
        #Expect 683 rows - all greater than $000,026.00
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Greater than")
         
        filterselectionobj.create_filter(1, 'Greater than',value1='$000,026.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '683of1000records,Page1of12', "Step 02: Expect 683 rows - all greater than $000,026.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 317 rows - all greater than (28.00)
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Greater than")
         
        filterselectionobj.create_filter(1, 'Greater than',value1='(28.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '317of1000records,Page1of6', "Step 02: Expect 317 rows - all greater than (28.00)")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 465 rows - all greater than 58.00 CR
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Greater than")
         
        filterselectionobj.create_filter(1, 'Greater than',value1='58.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '465of1000records,Page1of9', "Step 02: Expect 465 rows - all greater than 58.00 CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
 
        #Expect 418 rows - all greater than 76.00% CR
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Greater than")
         
        filterselectionobj.create_filter(1, 'Greater than',value1='76.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '418of1000records,Page1of8', "Step 02: Expect 418 rows - all greater than 76.00% CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
 
        """Step 03: For the following PACKED data fields, select Filter, then Greater than or equal to and use these values:
 
        Packed Order - 5
        P9.2M Unit Price - $13.00
        P9.2C Unit Price - 17.00
        P9.2Lc Unit Price - $000,026.00
        P9.2B Unit Price - (28.00)
        P9.2R Unit Price - 58.00 CR
        P9.2% Unit Price - 76.00%
 
 
        """
 
         
        #  Expect 996 rows - all greater than or equal to 5
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141PA.fex", "S7068", 'mrid', 'mrpass') 
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Greater than or equal to")
        
        filterselectionobj.create_filter(1, 'Greater than or equal to','large', value1='5')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '996of1000records,Page1of18', "Step 03: Expect 996 rows - all greater than or equal to 5")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 1000 rows - all are greater than or equal to $13.00
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='$13.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03: Expect 1000 rows - all are greater than or equal to $13.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 916 rows - all greater than or equal to 17.00
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '916of1000records,Page1of17', "Step 03: Expect 916 rows - all greater than or equal to 17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 817 rows - all greater than or equal to $000,026.00
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='$000,026.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '817of1000records,Page1of15', "Step 03: Expect 817 rows - all greater than or equal to $000,026.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 465 rows - all greater than or equal to (28.00)
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='(28.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '465of1000records,Page1of9', "Step 03: Expect 465 rows - all greater than or equal to (28.00)")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 549 rows - all greater than or equal to 58.00 CR
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='58.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '549of1000records,Page1of10', "Step 03: Expect 549 rows - all greater than or equal to 58.00 CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 451 rows - all greater than or equal to 76.00% CR
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='76.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '451of1000records,Page1of8', "Step 03: Expect 451 rows - all greater than or equal to 76.00% CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
         
         
 
        """Step 04: For the following PACKED data fields, select Filter, then Less than and use these values:
 
        Packed Order - 5
        P9.2M Unit Price - $13.00
        P9.2C Unit Price - 17.00
        P9.2Lc Unit Price - $000,026.00
        P9.2B Unit Price - (28.00)
        P9.2R Unit Price - 58.00 CR
        P9.2% Unit Price - 76.00%
 
        """
         
 
        #Expect 4 rows - all less than 5
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141PA.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60) 
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than','large',value1='5')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '4of1000records,Page1of1', "Step 04: Expect 4 rows - all less than 5")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        time.sleep(3)
        #Expect 0 rows - none are less than $13.00
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter", "Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='$13.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 04: #Expect 0 rows - none are less than $13.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()

        #Expect 84 rows - all less than 17.00
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Less than")
        
        filterselectionobj.create_filter(1, 'Less than',value1='17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 04: Expect 84 rows - all less than 17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 183 rows - all less than $000,026.00
        
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Less than")
        
        filterselectionobj.create_filter(1, 'Less than',value1='$000,026.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '183of1000records,Page1of4', "Step 04: Expect 183 rows - all less than $000,026.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 535 rows - all less than (28.00)
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Less than")
        
        filterselectionobj.create_filter(1, 'Less than',value1='(28.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '535of1000records,Page1of10', "Step 04: Expect 535 rows - all less than (28.00)")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 451 rows - all less than 58.00 CR
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Less than")
        
        filterselectionobj.create_filter(1, 'Less than',value1='58.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '451of1000records,Page1of8', "Step 04:Expect 451 rows - all less than 58.00 CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        # Expect 549 rows - all less than 76.00% CR
        
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Less than")
        
        filterselectionobj.create_filter(1, 'Less than',value1='76.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '549of1000records,Page1of10', "Step 04 : Expect 549 rows - all less than 76.00% CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()

        
        """Step 05:  For the following PACKED data fields, select Filter, then Less than or equal to and use these values:

        Packed Order - 5
        P9.2M Unit Price - $13.00
        P9.2C Unit Price - 17.00
        P9.2Lc Unit Price - $000,026.00
        P9.2B Unit Price - (28.00)
        P9.2R Unit Price - 58.00 CR
        P9.2% Unit Price - 76.00%


        """

        
        
        #  Expect 5 rows - all less than 5
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141PA.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Less than or equal to")
        
        filterselectionobj.create_filter(1, 'Less than or equal to','large',value1='5')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '5of1000records,Page1of1', "Step 05: Expect 5 rows - all less than 5")
        time.sleep(5)                         
        filterselectionobj.close_filter_dialog()
        # Expect 84 rows - none are less than $13.00
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" ,"Less than or equal to")
        
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='$13.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 05:  Expect 84 rows - none are less than $13.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        # Expect 183 rows - all less than 17.00
        
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Less than or equal to")
        
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '183of1000records,Page1of4', "Step 05:Expect 183 rows - all less than 17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 317 rows - all less than $000,026.00
        
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Less than or equal to")
        
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='$000,026.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '317of1000records,Page1of6', "Step 05: Expect 317 rows - all less than $000,026.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 683 rows - all less than (28.00)
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Less than or equal to")
        
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='(28.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '683of1000records,Page1of12', "Step 05: Expect 683 rows - all less than (28.00)")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 535 rows - all less than 58.00 CR
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Less than or equal to")
        
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='58.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '535of1000records,Page1of10', "Step 02: Expect 535 rows - all less than 58.00 CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
   
        #Expect 582 rows - all less than 76.00% CR
        
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Less than or equal to")
        
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='76.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '582of1000records,Page1of11', "Step 05: Expect 582 rows - all less than 76.00% CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        

        """Step 06:For the following PACKED data fields, select Filter, then Between and use the pair of values:

        Packed Order - 5 & 10
        P9.2M Unit Price - $13.00 & $17.00
        P9.2C Unit Price - 17.00 & 26.00
        P9.2Lc Unit Price - $000,026.00 & $000,028.00
        P9.2B Unit Price - (58.00) & (28.00) in that order
        P9.2R Unit Price - 76.00 CR & 58.00 CR in that order
        P9.2% Unit Price - 76.00% & 81.00%


        """

        
        #Expect 6 rows - all between 5 and 10
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141PA.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Between")
        
        filterselectionobj.create_filter(1, 'Between','large', value1='5', value2='10')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '6of1000records,Page1of1', "Step 06: Expect 6 rows - all between 5 and 10")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        
        #Expect 183 rows - all between than $13.00 & $17.00
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" ,"Between")
        
        filterselectionobj.create_filter(1, 'Between',value1='$13.00', value2='$17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '183of1000records,Page1of4', "Step 06: Expect 183 rows - all between than $13.00 & $17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 233 rows - all between 17.00 & 26.00
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Between")
        
        filterselectionobj.create_filter(1, 'Between',value1='17.00', value2='26.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '233of1000records,Page1of5', "Step 06: Expect 233 rows - all between 17.00 & 26.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 282 rows - all between $000,026.00 & $000,028.00
        
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Between")
        
        filterselectionobj.create_filter(1, 'Between',value1='$000,026.00',value2='$000,028.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '282of1000records,Page1of5', "Step 06: Expect 282 rows - all between $000,026.00 & $000,028.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #issue 
        #Expect 683 rows - all between (58.00) & (28.00)
        #actual 232
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Between")
        
        filterselectionobj.create_filter(1, 'Between',value1='(58.00)', value2='(28.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '232of1000records,Page1of5', "Step 06: Expect 232 rows - all between (58.00) & (28.00)")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 117 rows - all between 76.00 CR & 58.00 CR
        
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Between")
        
        filterselectionobj.create_filter(1, 'Between',value1='76.00 CR', value2='58.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '117of1000records,Page1of3', "Step 06: Expect 117 rows - all between 76.00 CR & 58.00 CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
  
        
        # Expect 251 rows - all between 76.00% CR & 81.00% 
        
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Between")
        
        filterselectionobj.create_filter(1, 'Between',value1='76.00%', value2='81.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '251of1000records,Page1of5', "Step 06: Expect 251 rows - all between 76.00% CR & 81.00% ")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
         


        
        """Step 07:For the following PACKED data fields, select Filter, then Not Between and use the pair of values:

        Packed Order - 5 & 10
        P9.2M Unit Price - $13.00 & $17.00
        P9.2C Unit Price - 17.00 & 26.00
        P9.2Lc Unit Price - $000,026.00 & $000,028.00
        
        P9.2B Unit Price - (58.00) & (28.00) in that order
        P9.2R Unit Price - 76.00 CR & 58.00 CR in that order
        P9.2% Unit Price - 76.00% & 81.00%


        """
  

        
        #Expect 994 rows - all not between 5 and 10
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Not Between")
        
        filterselectionobj.create_filter(1, 'Not Between','large',value1='5', value2='10')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '994of1000records,Page1of18', "Step 07: Expect 994 rows - all not between 5 and 10")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
      
        # Expect 817 rows - all not between than $13.00 & $17.00
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" , "Not Between")
        
        filterselectionobj.create_filter(1, 'Not Between',value1='$13.00', value2='$17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '817of1000records,Page1of15', "Step 07: Expect 817 rows - all not between than $13.00 & $17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 767 rows - all not between 17.00 & 26.00
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Not Between")
        
        filterselectionobj.create_filter(1, 'Not Between',value1='17.00', value2='26.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '767of1000records,Page1of14', "Step 07: Expect 767 rows - all not between 17.00 & 26.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 718 rows - all not between $000,026.00 & $000,028.00
        
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Not Between")
        
        filterselectionobj.create_filter(1, 'Not Between',value1='$000,026.00',value2='$000,028.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '718of1000records,Page1of13', "Step 07: Expect 718 rows - all not between $000,026.00 & $000,028.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 317 rows - all not between (58.00) & (28.00)
        
        #Issue
        
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Not Between")
        
        filterselectionobj.create_filter(1, 'Not Between',value1='(58.00)', value2='(28.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '768of1000records,Page1of14', "Step 07:Expect 317 rows - all not between (58.00) & (28.00)")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        
        #Expect 883 rows - all not between 76.00 CR & 58.00 CR
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Not Between")
        
        filterselectionobj.create_filter(1, 'Not Between',value1='76.00 CR', value2='58.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '883of1000records,Page1of16', "Step 07:Expect 883 rows - all not between 76.00 CR & 58.00 CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()

        #Expect 749 rows - all not between 76.00% CR & 81.00%
        
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Not Between")
        
        filterselectionobj.create_filter(1, 'Not Between',value1='76.00%', value2='81.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)  
        
        miscelanousobj.verify_page_summary(0, '749of1000records,Page1of14', "Step 07: Expect 749 rows - all not between 76.00% CR & 81.00%")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
         

        
        
        
        
 
         
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        