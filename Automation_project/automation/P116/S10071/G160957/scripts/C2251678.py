'''
Created on Feb 08, 2018

@author: Robert

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251678
TestCase Name = Verify that Slider Controls using Between Filtering for Packed data work in a Document.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_run
from common.lib import utillity

class C2251678_TestClass(BaseTestCase):

    def test_C2251678(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251678'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        
        
        """    1. Execute slider3.fex which displays a Compound Document.    """
            
        utillobj.active_run_fex_api_login('slider3.fex', 'S10071_3', 'mrid', 'mrpass')
             
        resultobj.wait_for_property("#ITableData1",1,50)
         
        time.sleep(10)
         
        """    1.1. Expect to see the following Document, with several Filters, Slider Controls in the middle and two reports below the Filters..    """
        """    1.2. Expect both reports to show 18 rows.    """
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 1.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', 'Step 1.2a: Verify the Report Heading for report 2')
        
        column_list=["COUNTRY", "MODEL", "Negative Integer"]
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 1.2b: Verify the column heading for report 1')
        
        column_list=["COUNTRY", "CAR", "Packed Data with decimal"]
        miscelanousobj.verify_column_heading('ITableData1', column_list, 'Step 1.2b: Verify the column heading for report 2')
        
        
        #utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 1.2c: Verify data report1.')
        
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds02.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds02.xlsx', 'Step 1.2c: Verify data report 2.')
        
        slider_css="div[id^='LOBJobject'] [class^='ui-slider-handle']"
        slider_count=len(self.driver.find_elements_by_css_selector(slider_css))
        utillobj.asequal(slider_count,8, 'Step 1. Verify 8 slider objects visible')
        
        slider_text=['CAR', 'H slider for INTEGER', 'V slider for INTEGER', 'H slider for PACKED', 'V slider for PACKED']
        
        lobj_css="div[id^='LOBJobject'] table > tbody > tr > td > div[class='arFilterButton'] > span"
        actual_title=[]
        lobj_ele=self.driver.find_elements_by_css_selector(lobj_css)
        for item in lobj_ele:
            actual_title.append(item.text)
        
        utillobj.as_List_equal(slider_text,actual_title, 'Step 1. Verify slider objects title')
        
        
            
            
        
        """    2. Using the bottom left slider, which controls the right side report and is labeled "H slider for PACKED", left-click and drag the left button slightly to the right until the left value reads the smallest positive value as possible. """
        """    2.1. Expect to see the right side report display 13 rows, all values except .00. """
        
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "up",2, 4, 1)
        time.sleep(4)
      
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 2.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '13of18records,Page1of1', 'Step 2.2a: Verify the Report Heading for report 2')
        
        #utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 2.1: Verify data report1.')
        
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds03.xlsx', 'Step 2.2: Verify data report 2.')
        
                
        """
            3. Drag the right side button to the left by the smallest possible amount.    
            3.1. Expect to see a 12 row report on the right side.
            3.2. The small drag to the left should eliminate the one record with the maximum value of 427.65.
            3.3. The right side report remains unchanged.
            
        """
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "down",2, 5, 1)
        time.sleep(6)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 3.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '12of18records,Page1of1', 'Step 3.2a: Verify the Report Heading for report 2')
        
        #utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 3.1: Verify data report1.')
        
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds04.xlsx', 'Step 3.2: Verify data report 2.')
        
        """    4. Drag the both buttons all the way to the left so they display 0. No decimals should appear.    """
        """    4.1. Expect to see the right side report display 5 records, all containing .00.    """
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pagedown",10, 4, 1)
        time.sleep(3)
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pagedown",10, 5, 1)
        time.sleep(6)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 4.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '5of18records,Page1of1', 'Step 4.2a: Verify the Report Heading for report 2')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 4.1: Verify data report1.')
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds05.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds05.xlsx', 'Step 4.2: Verify data report 2.')
        
        """    5. Drag the both buttons all the way to the right so they display 427.65, the maximum value.    """
        """    5.1. Expect to see the right side report display a single record with value 427.65.    """
        
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",10, 5, 1)
        time.sleep(3)
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",10, 4, 1)
        time.sleep(6)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 5.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '1of18records,Page1of1', 'Step 5.2a: Verify the Report Heading for report 2')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds06.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 5.1: Verify data report1.')
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds06.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds06.xlsx', 'Step 5.2: Verify data report 2.')
        
        """    6. Using the bottom right slider, which controls the right side report and is labeled "V slider for PACKED", left-click and drag the bottom button very slightly up.    """
        """    6.1. Expect to see a 13 row report, displaying all positive values, eliminating the 5 rows with .00.    """
        
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "up",2, 6, 1)
        time.sleep(6)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 6.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '13of18records,Page1of1', 'Step 6.2a: Verify the Report Heading for report 2')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds07.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 6.1: Verify data report1.')
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds07.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds07.xlsx', 'Step 6.2: Verify data report 2.')
        
        
        """    7. Drag the top button very slightly down until the value 427.65 decreases by the smallest amount possible.    """
        """    7.1. Expect to see a 12 row report, all records between the small positive value and the next highest positive value, that is eliminating the maximum value 427.65.    """
        
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "down",2, 7, 1)
        time.sleep(6)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 7.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '12of18records,Page1of1', 'Step 7.2a: Verify the Report Heading for report 2')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 7.1: Verify data report1.')
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds08.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds08.xlsx', 'Step 7.2: Verify data report 2.')
        
        """    8. Drag the bottom button all the way down to its lowest value.    """
        """    8.1. Drag the top button as far down as it can go. Both should be displaying 0.    """
        """    8.2. Expect to see a 5 row report, all displaying the minimum value of .00.    """
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pagedown",10, 6, 1)
        time.sleep(2)
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pagedown",10, 7, 1)
        time.sleep(6)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 8.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '5of18records,Page1of1', 'Step 8.2a: Verify the Report Heading for report 2')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds09.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 8.1: Verify data report1.')
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds09.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds09.xlsx', 'Step 8.2: Verify data report 2.')
        
        """    9. Drag the top button all the way to the top.    """
        """    9.1. Drag the bottom button to the top as far as possible. Both buttons should be on 427.65.    """
        """    9.2. Expect to see the a report with a single row, the maximum value of 427.65.    """
        
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",10, 7, 1)
        time.sleep(2)
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",10, 6, 1)
        time.sleep(6)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 9.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '1of18records,Page1of1', 'Step 9.2a: Verify the Report Heading for report 2')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds10.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 9.1: Verify data report1.')
        #utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds10.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds10.xlsx', 'Step 9.2: Verify data report 2.')
        
        
        
if __name__=='__main__' :
    unittest.main()
        