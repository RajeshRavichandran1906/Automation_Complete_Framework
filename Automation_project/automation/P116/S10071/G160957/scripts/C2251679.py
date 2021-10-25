'''
Created on Feb 09, 2018

@author: Robert

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251679
TestCase Name = Verify that Slider Controls using Between Filtering for DATE fields data work in a Document.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_run
from common.lib import utillity

class C2251679_TestClass(BaseTestCase):

    def test_C2251679(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251679'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        
        
        """    1. Execute slider4.fex which displays a Compound Document.    """
            
        utillobj.active_run_fex_api_login('slider4.fex', 'S10071_3', 'mrid', 'mrpass')
             
        resultobj.wait_for_property("#ITableData1",1,30)
         
        time.sleep(10)
         
        """    1.1. Expect to see the following Document, with several Filters, Slider Controls in the middle and two reports below the Filters..    """
        """    1.2. Expect both reports to show 18 rows.    """
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 1.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', 'Step 1.2a: Verify the Report Heading for report 2')
        
        column_list=['COUNTRY', 'MODEL', 'DATE']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 1.2b: Verify the column heading for report 1')
        
        column_list=['COUNTRY', 'CAR', 'DATETIME']
        miscelanousobj.verify_column_heading('ITableData1', column_list, 'Step 1.2b: Verify the column heading for report 2')
        
        
        utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 1.2c: Verify data report1.')
        
        utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds02.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds02.xlsx', 'Step 1.2c: Verify data report 2.')
        
        slider_css="div[id^='LOBJobject'] [class^='ui-slider-handle']"
        slider_count=len(self.driver.find_elements_by_css_selector(slider_css))
        utillobj.asequal(slider_count,8, 'Step 1. Verify 8 slider objects visible')
        
        slider_text=['CAR', 'H slider for DATE', 'V slider for DATE', 'H slider for DATETIME', 'V slider for DATETIME']
        
        lobj_css="div[id^='LOBJobject'] table > tbody > tr > td > div[class='arFilterButton'] > span"
        actual_title=[]
        lobj_ele=self.driver.find_elements_by_css_selector(lobj_css)
        for item in lobj_ele:
            actual_title.append(item.text)
        print (actual_title)
        utillobj.as_List_equal(slider_text,actual_title, 'Step 1. Verify slider objects title')
        
        
            
            
        
        """    2. Using the upper left slider, which controls the left report and is labeled "H slider for Dealer_Cost", left-click and drag the control to the right until the value reads as close to 8000 as possible. """
        """    2.1. Expect to see the left report display 7 records, with Dealer_Cost values between 8017 and the Max value of 25,000. The right-side report remains unchanged. """
        """    2.2. Expect the right-side report to be unchanged.    """
        
        
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",1, 0, 1)
        time.sleep(4)
      
        
        miscelanousobj.verify_page_summary(0, '14of18records,Page1of1', 'Step 2.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', 'Step 2.2a: Verify the Report Heading for report 2')
        
        utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds03.xlsx', 'Step 2.1: Verify data report1.')
        
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds02.xlsx', 'Step 2.2: Verify data report 2.')
        
                
        """
            3. Drag the slider set for around 8000 all the way to the right.    
            3.1. Check the left side report.
            3.2. Expect to see a single row in the left-side report, as there is only one Dealer_Cost row between 25,000 and 25,000.
            3.3. Expect the right-side report to be unchanged.
            
        """
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "down",1, 1, 1)
        time.sleep(6)
        
        miscelanousobj.verify_page_summary(0, '7of18records,Page1of1', 'Step 3.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', 'Step 3.2a: Verify the Report Heading for report 2')
        
        utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds04.xlsx', 'Step 3.1: Verify data report1.')
        
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds02.xlsx', 'Step 3.2: Verify data report 2.')
        
        """    4. Drag the button all the way back to the left.    """
        """    4.1. Now drag the right button to the left until the value is as close to 10000 as possible.    """
        """    4.2. Expect to see the left report display 14 records, with Dealer_Cost values between the Min value 2626 and around 10000. The right-side report remains unchanged.    """
        """    4.3. Expect the right-side report to be unchanged.    """
        
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pagedown",10, 0, 1)
        time.sleep(3)
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pagedown",10, 1, 1)
        time.sleep(6)
       
        
        miscelanousobj.verify_page_summary(0, '4of18records,Page1of1', 'Step 4.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', 'Step 4.2a: Verify the Report Heading for report 2')
        utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds05.xlsx', 'Step 4.1: Verify data report1.')
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds05.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds02.xlsx', 'Step 4.2: Verify data report 2.')
        
        """    5. Drag the right button to the left as far as possible.    """
        """    5.1. Reset the button to the right most position until the left side report shows all 18 records again.    """
        """    5.2. Expect to see a single row in the left-side report, as there is only one Dealer_Cost row between 2626 and 2626.    """
        
        
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",10, 1, 1)
        time.sleep(6)
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",10, 0, 1)
        time.sleep(6)
        
        miscelanousobj.verify_page_summary(0, '7of18records,Page1of1', 'Step 5.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', 'Step 5.2a: Verify the Report Heading for report 2')
        utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds06.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds06.xlsx', 'Step 5.1: Verify data report1.')
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds06.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds02.xlsx', 'Step 5.2: Verify data report 2.')
        
       
        """    6. Using the upper right slider, which controls the right report and is labeled "V slider for Retail_Cost", left-click and drag the bottom button upward until the lower value as close to 13000 as possible.    """
        """    6.1. Expect to see the right report display 5 records, with Retail_Cost values between 13000 and the Max value of 31500. The right-side report remains unchanged.    """
        """    6.2. Expect the left-side report to be unchanged.    """
        
        
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",2, 2, 1)
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '10of18records,Page1of1', 'Step 6.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', 'Step 6.2a: Verify the Report Heading for report 2')
        utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds07.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds07.xlsx', 'Step 6.1: Verify data report1.')
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds07.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds02.xlsx', 'Step 6.2: Verify data report 2.')
        
        
        """    7. Drag the slider set for 13000 all the way to the top, showing value 31500. Check the right side report.    """
        """    7.1. Expect to see a single row in the right-side report, as there is only one Retail_Cost row between 31500 and 31500.    """
        """    7.2. Expect the left-side report to be unchanged.    """
        
        
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "down",1, 3, 1)
        time.sleep(6)
        
        miscelanousobj.verify_page_summary(0, '3of18records,Page1of1', 'Step 7.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', 'Step 7.2a: Verify the Report Heading for report 2')
        utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds08.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds08.xlsx', 'Step 7.1: Verify data report1.')
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds08.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds02.xlsx', 'Step 7.2: Verify data report 2.')
        
        """    8. Drag the bottom button all the way down to its lowest value.    """
        """    8.1. Drag the top button as far down as it can go. Both should be displaying 0.    """
        """    8.2. Expect to see a 5 row report, all displaying the minimum value of .00.    """
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pagedown",10, 2, 1)
        time.sleep(2)
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pagedown",10, 3, 1)
        time.sleep(6)
        miscelanousobj.verify_page_summary(0, '4of18records,Page1of1', 'Step 8.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', 'Step 8.2a: Verify the Report Heading for report 2')
        utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds09.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds09.xlsx', 'Step 8.1: Verify data report1.')
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds09.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds02.xlsx', 'Step 8.2: Verify data report 2.')
        
        """    9. Drag the top button all the way to the top.    """
        """    9.1. Drag the bottom button to the top as far as possible. Both buttons should be on 427.65.    """
        """    9.2. Expect to see the a report with a single row, the maximum value of 427.65.    """
        
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",10, 3, 1)
        time.sleep(6)
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",10, 2, 1)
        time.sleep(6)
        miscelanousobj.verify_page_summary(0, '7of18records,Page1of1', 'Step 9.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', 'Step 9.2a: Verify the Report Heading for report 2')
        utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds10.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds10.xlsx', 'Step 9.1: Verify data report1.')
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds10.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds02.xlsx', 'Step 9.2: Verify data report 2.')
        
        
        
if __name__=='__main__' :
    unittest.main()
        