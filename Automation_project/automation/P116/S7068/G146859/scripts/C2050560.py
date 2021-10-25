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
import unittest
import time
 

class C2050560_TestClass(BaseTestCase):

    def test_C2050560(self):
        """
            Step 01:   Execute the attached AR-RP-141DA.

        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-141DA.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(10)
       
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01:  Expect to see the following Active Report. - page summary verification")
                  
         
        """Step 02 : For the following DATE fields, select Filter, then Greater than and use these values:
  
        YYMD Order Date - 19960201
        MTRDYY Order Date - MARCH 1, 1996
        YYJUL Order Date - 1996/001
        JULIAN Order Date - 96/092
        QYY Order Date - Q1 1996
        wrMtrYY Order Date - Monday, Apr 1 1996
        Mtr Order Date - May
        Wtr Order Date - Wednesday
        """
   
  
          
          
        #Expect 640 rows - later than 19960201
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Greater than")
          
        filterselectionobj.create_filter(1, 'Greater than',value1='19960201')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '640of1000records,Page1of12', "Step 02: Expect 640 rows - later than 19960201")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        #Expect 460 rows - later than MARCH 1, 1996
          
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Greater than")
          
        filterselectionobj.create_filter(1, 'Greater than',value1='MARCH 1, 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '460of1000records,Page1of9', "Step 02: Expect 460 rows - later than MARCH 1, 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        #Expect 820 rows - later than 1996/001
          
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Greater than")
           
        filterselectionobj.create_filter(1, 'Greater than',value1='1996/001')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
           
        miscelanousobj.verify_page_summary(0, '820of1000records,Page1of15', "Step 02: Expect 820 rows - later than 1996/001")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
          
        #Expect 280 rows - later than 96/092
          
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Greater than")
          
        filterselectionobj.create_filter(1, 'Greater than',value1='96/092')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '280of1000records,Page1of5', "Step 02: Expect 280 rows - later than 96/092")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        #Expect 460 rows - later than Q1 1996
          
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Greater than")
          
        filterselectionobj.create_filter(1, 'Greater than',value1='Q1 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '460of1000records,Page1of9', "Step 02: Expect 460 rows - later than Q1 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        #Expect 280 rows - later than Monday, Apr 1 1996
          
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Greater than")
          
        filterselectionobj.create_filter(1, 'Greater than',value1='Monday, April 1 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '280of1000records,Page1of5', "Step 02: Expect 280 rows - later than Monday, Apr 1 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
  
        #Expect 100 rows - later than May
          
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Greater than")
          
        filterselectionobj.create_filter(1, 'Greater than',value1='May')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '100of1000records,Page1of2', "Step 02: Expect 100 rows - later than May")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        #Expect 460 rows - later than Wednesday
          
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Greater than")
          
        filterselectionobj.create_filter(1, 'Greater than',value1='Wednesday')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '460of1000records,Page1of9', "Step 02:Expect 460 rows - later than Wednesday")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
  
        """Step 03: For the following DATE fields, select Filter, then Greater than or equal to and use these values:
  
        YYMD Order Date - 19960201
        MTRDYY Order Date - MARCH 1, 1996
        YYJUL Order Date - 1996/001
        JULIAN Order Date - 96/092
        QYY Order Date - Q1 1996
        wrMtrYY Order Date - Monday, Apr 1 1996
        Mtr Order Date - May
        Wtr Order Date - Wednesday
  
        """
  
  
          
        # Expect 820 rows - equal to 19960201 or later
          
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Greater than or equal to")
          
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='19960201')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '820of1000records,Page1of15', "Step 03: Expect 916 rows - value 17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 640 rows - equal to MARCH 1, 1996 or later
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='MARCH 1, 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '640of1000records,Page1of12', "Step 03: Expect 640 rows - equal to MARCH 1, 1996 or later")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 1000 rows - equal to 1996/001 or later
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='1996/001')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 02: Expect 1000 rows - equal to 1996/001 or later")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 460 rows - equal to 96/092 or later
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='96/092')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '460of1000records,Page1of9', "Step 03: Expect 460 rows - equal to 96/092 or later")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 1000 rows - equal to Q1 1996 or later
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='Q1 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03: Expect 1000 rows - equal to Q1 1996 or later")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 460 rows - equal to Monday, Apr 1 1996 or later
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='Monday, April 1 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '460of1000records,Page1of9', "Step 03: Expect 460 rows - equal to Monday, Apr 1 1996 or later")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        # Expect 280 rows - equal to May or later
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='May')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '280of1000records,Page1of5', "Step 03: Expect 280 rows - equal to May or later")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 640 rows - equal to Wednesday or later
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Greater than or equal to")
         
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='Wednesday')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '640of1000records,Page1of12', "Step 03: Expect 640 rows - equal to Wednesday or later")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
         
 
        """Step 04: For the following DATE fields, select Filter, then Less than and use these values:
        YYMD Order Date - 19960201
        MTRDYY Order Date - MARCH 1, 1996
        YYJUL Order Date - 1996/001
        JULIAN Order Date - 96/122
        QYY Order Date - Q2 1996
        wrMtrYY Order Date - Thursday, February 1 1996
        Mtr Order Date - March
        Wtr Order Date - Saturday
        """
         
        #Expect 180 rows - before 19960201
         
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='19960201')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 04: Expect 84 rows - value 17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        time.sleep(3)
        #Expect 360 rows - before MARCH 1, 1996
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter", "Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='MARCH 1, 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '360of1000records,Page1of7', "Step 04: Expect 360 rows - before MARCH 1, 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 0 rows - before 1996/001
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='1996/001')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 04: Expect 0 rows -before 1996/001")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 720 rows - before 96/122
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='96/122')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '720of1000records,Page1of13', "Step 04: Expect 720 rows - before 96/122")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 540 rows - before Q2 1996
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='Q2 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '540of1000records,Page1of10', "Step 04: Expect 540 rows - before Q2 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 180 rows - before Thursday, February 1 1996
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='Thursday, February 1 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 04: Expect 180 rows - before Thursday, February 1 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 360 rows - before March
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='March')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '360of1000records,Page1of7', "Step 04: Expect 360 rows - before March")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 900 rows - before Saturday
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Less than")
         
        filterselectionobj.create_filter(1, 'Less than',value1='Saturday')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '900of1000records,Page1of16', "Step 04: EExpect 900 rows - before Saturday")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
         
        """Step 05:  For the following DATE fields, select Filter, then Less than or equal to and use these values:
 
        YYMD Order Date - 19960201
        MTRDYY Order Date - MARCH 1, 1996
        YYJUL Order Date - 1996/001
        JULIAN Order Date - 96/122
        QYY Order Date - Q2 1996
        wrMtrYY Order Date - Thursday, February 1 1996
        Mtr Order Date - March
        Wtr Order Date - Saturday
 
        """
         
         
        # Expect 360 rows - on or before 19960201
         
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='19960201')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '360of1000records,Page1of7', "Step 05: Expect 360 rows - on or before 19960201")
        time.sleep(5)                         
        filterselectionobj.close_filter_dialog()
        # Expect 540 rows - on or before MARCH 1, 1996
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" ,"Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='MARCH 1, 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '540of1000records,Page1of10', "Step 05: EExpect 540 rows - before MARCH 1, 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 180 rows - on or before 1996/001
         
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='1996/001')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 05: Expect 180 rows - on or before 1996/001")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 900 rows - on or before 96/122
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='96/122')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '900of1000records,Page1of16', "Step 05: Expect 900 rows - on or before 96/122")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 1000 rows - on or before Q2 1996
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='Q2 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 05: Expect 1000 rows - on or before Q2 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 360 rows - on or before Thursday, February 1 1996
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='Thursday, February 1 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '360of1000records,Page1of7', "Step 02: Expect 360 rows - on or before Thursday, February 1 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
    
        #Expect 540 rows - on or before March
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='March')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '540of1000records,Page1of10', "Step 05: Expect 540 rows - on or before March")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        # Expect 1000 rows - on or before Saturday
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Less than or equal to")
         
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='Saturday')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 05: Expect 1000 rows - on or before Saturday")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
         
 
        """Step 06: For the following DATE fields, select Filter, then Between the pair of values:
 
        YYMD Order Date - 19960201 & 19960301
        MTRDYY Order Date - MARCH 1, 1996 & MAY 1, 1996
        YYJUL Order Date - 1996/001 & 1996/092
        JULIAN Order Date - 96/092 & 96/153
        QYY Order Date - Q1 1996 & Q2 1996
        wrMtrYY Order Date - Monday, Apr 1 1996 & Wednesday, May 1 1996
        Mtr Order Date - May & June
        Wtr Order Date - Wednesday & Friday
 
        """
     
         
        #Expect 360 rows - between 19960201 and 19960301
         
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='19960201', value2='19960301')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '360of1000records,Page1of7', "Step 06: Expect 360 rows - between 19960201 and 19960301")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Issue 
         
        #Expect 540 rows - between MARCH 1, 1996 & MAY 1, 1996
         
         
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" ,"Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='MARCH 1, 1996', value2='MAY 1, 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '540of1000records,Page1of10', "Step 06: Expect 540 rows - between MARCH 1, 1996 & MAY 1, 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
         
         
        #Expect 720 rows - between 1996/001 & 1996/092
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='1996/001', value2='1996/092')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '720of1000records,Page1of13', "Step 06: Expect 183 rows - values 0.13D+02 & 0.17D+02")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 460 rows - between 96/092 & 96/153
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='96/092',value2='96/153')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '460of1000records,Page1of9', "Step 06: Expect 460 rows - between 96/092 & 96/153")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 1000 rows - between Q1 1996 & Q2 1996
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='Q1 1996', value2='Q2 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 06: Expect 1000 rows - between Q1 1996 & Q2 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 360 rows - between Monday, Apr 1 1996 & Wednesday, May 1 1996
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='Monday, April 1 1996', value2='Wednesday, May 1 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '360of1000records,Page1of7', "Step 06: Expect 360 rows - between Monday, Apr 1 1996 & Wednesday, May 1 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
   
         
        # Expect 280 rows - between May & June
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='May', value2='June')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '280of1000records,Page1of5', "Step 06: Expect 280 rows - between May & June")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 540 rows - between Wednesday & Friday
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Between")
         
        filterselectionobj.create_filter(1, 'Between',value1='Wednesday', value2='Friday')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '540of1000records,Page1of10', "Step 06: Expect 540 rows - between Wednesday & Friday")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()


        
        """Step 07:For the following DATE fields, select Filter, then Not Between the pair of values:

        YYMD Order Date - 19960201 & 19960301
        MTRDYY Order Date - MARCH 1, 1996 & MAY 1, 1996
        
        YYJUL Order Date - 1996/001 & 1996/092
        JULIAN Order Date - 96/092 & 96/153
        QYY Order Date - Q1 1996 & Q2 1996
        wrMtrYY Order Date - Monday, Apr 1 1996 & Wednesday, May 1 1996
        Mtr Order Date - May & June
        Wtr Order Date - Wednesday & Friday

        """

        
        #Expect 640 rows - not between 19960201 and 19960301
         
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='19960201', value2='19960301')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '640of1000records,Page1of12', "Step 07: Expect 767 rows - values 17.00 & 26.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #issue
        #Expect 460 rows - not between MARCH 1, 1996 & MAY 1, 1996
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" , "Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='MARCH 1, 1996', value2='MAY 1, 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '460of1000records,Page1of9', "Step 07: Expect 460 rows - not between MARCH 1, 1996 & MAY 1, 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 280 rows - not between 1996/001 & 1996/092
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='1996/001', value2='1996/092')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '280of1000records,Page1of5', "Step 07: Expect 280 rows - not between 1996/001 & 1996/092")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 540 rows - not between 96/092 & 96/153
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='96/092',value2='96/153')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '540of1000records,Page1of10', "Step 07: Expect 540 rows - not between 96/092 & 96/153")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 0 rows - not between Q1 1996 & Q2 1996
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='Q1 1996', value2='Q2 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 07:Expect 0 rows - not between Q1 1996 & Q2 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 640 rows - not between Monday, Apr 1 1996 & Wednesday, May 1 1996
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='Monday, April 1 1996', value2='Wednesday, May 1 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '640of1000records,Page1of12', "Step 07:Expect 640 rows - not between Monday, Apr 1 1996 & Wednesday, May 1 1996")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
 
        #Expect 720 rows - not between May & June
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='May', value2='June')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)  
         
        miscelanousobj.verify_page_summary(0, '720of1000records,Page1of13', "Step 07: Expect 867 rows - values 140.00CR & 125.00CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 460 rows - not between Wednesday & Friday
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Not Between")
         
        filterselectionobj.create_filter(1, 'Not Between',value1='Wednesday', value2='Friday')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '460of1000records,Page1of9', "Step 07: Expect 460 rows - not between Wednesday & Friday")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        """Step 08: For the following DATE fields, select Filter, then Contains, then enter the strings below.
        Case does NOT matter for these tests
         
        YYMD Order Date - 9602
        MTRDYY Order Date - April
        YYJUL Order Date - 6/15
        JULIAN Order Date - 96/00
        QYY Order Date - Q2
        wrMtrYY Order Date - june
         
        Mtr Order Date - Feb
        Wtr Order Date - SAT
         
        """
         
         
        #Expect 180 rows - dates of 19960201 containing '9602'
         
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Contains")
         
        filterselectionobj.create_filter(1, 'Contains',value1='9602')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 08: Expect 180 rows - dates of 19960201 containing '9602'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 180 rows - dates of APRIL 1, 1996 containing 'April'
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" , "Contains")
         
        filterselectionobj.create_filter(1, 'Contains',value1='April')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 08: Expect 180 rows - dates of APRIL 1, 1996 containing 'April'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 100 rows - dates of 96/153 containing '6/15'
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Contains")
         
        filterselectionobj.create_filter(1, 'Contains',value1='6/15')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '100of1000records,Page1of2', "Step 08: Expect 100 rows - dates of 96/153 containing '6/15'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 180 rows - dates of 96/001 containing '96/00'
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Contains")
         
        filterselectionobj.create_filter(1, 'Contains',value1='96/00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 08: Expect 180 rows - dates of 96/001 containing '96/00'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        # Expect 460 rows - dates of Q2 1996 containing 'Q2'
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Contains")
         
        filterselectionobj.create_filter(1, 'Contains',value1='Q2')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '460of1000records,Page1of9', "Step 08: Expect 460 rows - dates of Q2 1996 containing 'Q2'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 100 rows - dates of Saturday, June 1 1996 containing 'june'
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Contains")
         
        filterselectionobj.create_filter(1, 'Contains',value1='june')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '100of1000records,Page1of2', "Step 08: Expect 100 rows - dates of Saturday, June 1 1996 containing 'june'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
 
        #Expect 180 rows - dates of February containing 'Feb'
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Contains")
         
        filterselectionobj.create_filter(1, 'Contains',value1='Feb')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 08: Expect 180 rows - dates of February containing 'Feb' ")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 100 rows - dates of Saturday containing 'SAT'
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Contains")
         
        filterselectionobj.create_filter(1, 'Contains',value1='SAT')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '100of1000records,Page1of2', "Step 08: Expect 100 rows - dates of Saturday containing 'SAT'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        
        """Step 09: For the following DATE fields, select Filter, then Contains(case match), then enter the strings below.
        Case matters for these tests, the string must match exactly.
        Only fields containing multiple alphanumeric characters are included.
        
        MTRDYY Order Date - April
        MTRDYY Order Date - APRIL
        wrMtrYY Order Date - june
        wrMtrYY Order Date - June
        
        Mtr Order Date - JAN
        Mtr Order Date - Jan
        Wtr Order Date - sAT
        Wtr Order Date - Sat"""
        
    
        
        #Expect 0 rows - no dates contain 'April'
        
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Contains (match case)")
        
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='April')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09: Expect 0 rows - no dates contain 'April'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 180 rows - dates of APRIL 1, 1996 contain 'APRIL'
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" , "Contains (match case)")
        
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='APRIL')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 09: Expect 180 rows - dates of APRIL 1, 1996 contain 'APRIL'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 0 rows - no dates contain 'june'
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Contains (match case)")
        
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='june')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09: Expect 0 rows - no dates contain 'june'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 100 rows - dates of Saturday, June 1 1996 containing 'June'
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Contains (match case)")
        
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='June')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '100of1000records,Page1of2', "Step 09: Expect 100 rows - dates of Saturday, June 1 1996 containing 'June' ")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 0 rows - no dates contain 'JAN'
        
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Contains (match case)")
        
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='JAN')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09: Expect 0 rows - no dates contain 'JAN'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 180 rows - dates of January containing 'Jan'
        
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Contains (match case)")
        
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='Jan')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 09: Expect 180 rows - dates of January containing 'Jan'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()

        #Expect 0 rows - no dates contain 'sAT'
        
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Contains (match case)")
        
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='sAT')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09: Expect 0 rows - no dates contain 'sAT'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 100 rows - dates of Saturday containing 'Sat'
        
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Contains (match case)")
        
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='Sat')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '100of1000records,Page1of2', "Step 09: Expect 100 rows - dates of Saturday containing 'Sat' ")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        """Step 10: For the following DATE fields, select Filter, then Omits, then enter the strings below.
        Case does NOT matter for these tests
        
        YYMD Order Date - 9602
        MTRDYY Order Date - April
        YYJUL Order Date - 6/15
        JULIAN Order Date - 96/00
        QYY Order Date - Q2
        wrMtrYY Order Date - june
        Mtr Order Date - Feb
        Wtr Order Date - SAT
        """

        #Expect 820 rows - all dates except those containing '9602'
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Omits")
        
        filterselectionobj.create_filter(1, 'Omits',value1='9602')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '820of1000records,Page1of15', "Step 10: Expect 820 rows - all dates except those containing '9602")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 820 rows - all dates except those containing 'April'
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" , "Omits")
        
        filterselectionobj.create_filter(1, 'Omits',value1='April')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '820of1000records,Page1of15', "Step 10: Expect 820 rows - all dates except those containing 'April'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 900 rows - all dates except those containing '6/15'
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Omits")
        
        filterselectionobj.create_filter(1, 'Omits',value1='6/15')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '900of1000records,Page1of16', "Step 10: Expect 900 rows - all dates except those containing '6/15'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 180 rows - all dates except those containing '96/00'
        
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Omits")
        
        filterselectionobj.create_filter(1, 'Omits',value1='96/00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '820of1000records,Page1of15', "Step 10: Expect 820 rows - all dates except those containing '96/00'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 540 rows - all dates except those containing 'Q2'
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Omits")
        
        filterselectionobj.create_filter(1, 'Omits',value1='Q2')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '540of1000records,Page1of10', "Step 10:Expect 540 rows - all dates except those containing 'Q2'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 900 rows - all dates except those containing 'june'
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Omits")
        
        filterselectionobj.create_filter(1, 'Omits',value1='june')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '900of1000records,Page1of16', "Step 10: Expect 900 rows - all dates except those containing 'june'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()

        #Expect 820 rows - all dates except those containing 'Feb'
        
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Omits")
        
        filterselectionobj.create_filter(1, 'Omits',value1='Feb')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '820of1000records,Page1of15', "Step 10: Expect 820 rows - all dates except those containing 'Feb' ")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        # Expect 900 rows - all dates except those containing 'SAT'
        
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Omits")
        
        filterselectionobj.create_filter(1, 'Omits',value1='SAT')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '900of1000records,Page1of16', "Step 10:Expect 900 rows - all dates except those containing 'SAT' ")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        """Step 11: For the following DATE fields, select Filter, then Omits (case match), then enter the strings below.
        Case matters for these tests, the string must match exactly.
        Only fields containing multiple alphanumeric characters are included.
        
        MTRDYY Order Date - April
        MTRDYY Order Date - APRIL
        wrMtrYY Order Date - june
        wrMtrYY Order Date - June
        Mtr Order Date - JAN
        Mtr Order Date - Jan
        Wtr Order Date - sAT
        Wtr Order Date - Sat
        """
        
        
        #Expect 1000 rows - no dates omit 'April'
        
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Omits (match case)")
        
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='April')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11: Expect 1000 rows - no dates omit 'April' ")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 820 rows - all dates that omit 'APRIL'
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" , "Omits (match case)")
        
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='APRIL')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '820of1000records,Page1of15', "Step 11: Expect 820 rows - all dates that omit 'APRIL'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        #Expect 1000 rows - no dates that omit 'june'
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Omits (match case)")
        
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='june')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11: Expect 1000 rows - no dates that omit 'june'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 900 rows - all dates that omit 'June'
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Omits (match case)")
        
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='June')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '900of1000records,Page1of16', "Step 11: Expect 900 rows - all dates that omit 'June'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 1000 rows - no dates that omit 'JAN'
        
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Omits (match case)")
        
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='JAN')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11: Expect 1000 rows - no dates that omit 'JAN'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 820 rows - all dates that omit 'Jan'
        
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Omits (match case)")
        
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='Jan')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '820of1000records,Page1of15', "Step 11: Expect 820 rows - all dates that omit 'Jan'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()

        #Expect 1000 rows - no dates omit 'sAT'
        
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Omits (match case)")
        
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='sAT')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11: Expect 1000 rows - no dates omit 'sAT'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        # Expect 900 rows - all dates that omit 'Sat'
        
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Omits (match case)")
        
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='Sat')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '900of1000records,Page1of16', "Step 11: Expect 900 rows - all dates that omit 'Sat'")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
    
         
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        