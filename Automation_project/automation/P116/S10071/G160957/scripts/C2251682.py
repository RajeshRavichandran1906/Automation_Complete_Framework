'''
Created on Feb 12, 2018

@author: Praveen Ramkumar

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251682
TestCase Name = Verify that Slider Controls using a single Button(GT & LT) work in a Document.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous
from common.lib import utillity

class C2251682_TestClass(BaseTestCase):

    def test_C2251682(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251682'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)       
        
        """    1. Execute slider_GT_LT.fex which displays a Compound Document. """
            
        utillobj.active_run_fex_api_login('slider_GT_LT.fex', 'S10071_3', 'mrid', 'mrpass')
        resultobj.wait_for_property("#ITableData1",1,30)
        time.sleep(10)
        
        """    1.1. Expect to see the following Document, with several Filters, Slider Controls in the middle and two reports below the Filters..    """
        """    1.2. Expect both reports to show 18 rows.    """
         
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 1.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', 'Step 1.2a: Verify the Report Heading for report 2')           
        column_list=['COUNTRY', 'CAR', 'RETAIL_COST', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 1.2b: Verify the column heading for report 1')
           
        column_list=['COUNTRY', 'MODEL', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_column_heading('ITableData1', column_list, 'Step 1.2b: Verify the column heading for report 2')           
           
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 1.2c: Verify data report1.')
           
#         utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds02.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds02.xlsx', 'Step 1.2c: Verify data report 2.')
           
        slider_css="div[id^='LOBJobject'] [class^='ui-slider-handle']"
        slider_count=len(self.driver.find_elements_by_css_selector(slider_css))
        utillobj.asequal(slider_count,4, 'Step 1. Verify 4 slider objects visible')
           
        slider_text=['CAR', 'H slider for Dealer_Cost Greater Than', 'V slider for Dealer_Cost Less Than', 'H slider for Retail_Cost Greater Than', 'V slider for Retail_Cost Less Thanl']
           
        lobj_css="div[id^='LOBJobject'] table > tbody > tr > td > div[class='arFilterButton'] > span"
        actual_title=[]
        lobj_ele=self.driver.find_elements_by_css_selector(lobj_css)
        for item in lobj_ele:
            actual_title.append(item.text)
        print (actual_title)
        utillobj.as_List_equal(slider_text,actual_title, 'Step 1. Verify slider objects title')
          
          
        """    2. Using the top left slider, which controls the right side report and is labeled slider for Dealer_Cost Greater Than', move the control to the right until the value is as close to but not over 10000.
               2.1. Expect to see the right side report display 5 rows, all greater than a value slightly less than 10000.. 
          
        """
        
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",1, 0, 1)
        time.sleep(4)
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "up",1850, 0, 0)
        time.sleep(4)
  
        
        miscelanousobj.verify_page_summary(1, '5of18records,Page1of1', 'Step 2.2a: Verify the Report Heading for report 1')        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 2.2a: Verify the Report Heading for report 2')
          
  
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds03.xlsx', 'Step 2.1: Verify data report1.')
               
#         utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds04.xlsx', 'Step 2.2: Verify data report 2.')                
         
         
         
        """    3.Continue dragging the button to the right until the value 25000 appears, this is the maximum Dealer_Cost.
               3.1. Expect to see an empty report, since no value is Greater Than 25000. 
          
        """
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",5, 0, 1)
        time.sleep(6)        
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds05.xlsx', 'Step 3.1: Verify data report1.')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 3.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '0of18records,Page1of1', 'Step 3.2a: Verify the Report Heading for report 2')
          
        """
            4. Drag the button back to its full left position.
            4.1. Expect to see the full 18 row report once again, all values greater than or equal to 3139.
              
        """          
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pagedown",10, 0, 1)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 4.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '17of18records,Page1of1', 'Step 4.2a: Verify the Report Heading for report 2')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 4.1: Verify data report1.')
#         utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds06.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds06.xlsx', 'Step 4.2: Verify data report 2.')          
         
        """
            5. Using the top right slider, which controls the right side report and is labeled 'V slider for Dealer_Cost Less Than', move the control towards the top until the value is as close to 15000, making sure the value is under 15000.
            5.1.Expect to see the right side report display 16 rows, all Less Than 15,000.
        """                      
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",2, 1, 1)
        time.sleep(6)
  
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 5.1: Verify data report1.')
#         utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds07.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds07.xlsx', 'Step 5.2: Verify data report 2.')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 5.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '16of18records,Page1of1', 'Step 5.2a: Verify the Report Heading for report 2')
          
          
        """
            6. Continue dragging the button to the top until the value 25000 appears, this is the maximum.
            6.1. Expect to see a 17 row report with only 25,000 excluded because it is Equal to that value not Less Than.
        """       
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",5, 1, 1)
        time.sleep(3)          
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 6.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '17of18records,Page1of1', 'Step 6.2a: Verify the Report Heading for report 2')          
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 6.1: Verify data report1.')
#         utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds08.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_Ds08.xlsx', 'Step 6.2: Verify data report 2.')
          
        """
            7. Drag the button back to its lowest position, displaying 2626.
            7.1. Expect to see an empty report because no value is Less Than 2,626.
        """
          
          
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pagedown",5, 1, 1)
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 7.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '0of18records,Page1of1', 'Step 7.2a: Verify the Report Heading for report 2')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', 'Step 7.1: Verify data report1.')          
         
        """
            8. Using the bottom left slider, which controls the left side report and is labeled 'H slider for Retail_Cost Greater Than', move the control to the right until the value is as close to 7500.
            8.1. Expect to see an 8 row report with all Retail_Cost values Greater Than 7,000.
        """
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",1, 2, 1)
        time.sleep(2)
         
        miscelanousobj.verify_page_summary(0, '8of18records,Page1of1', 'Step 8.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '0of18records,Page1of1', 'Step 8.2a: Verify the Report Heading for report 2')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds08a.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds08a.xlsx', 'Step 8.1: Verify data report1.')
         
        
        """
            9. Continue to drag the button to the right most position until it displays 31500.
            9.1. Expect to see an empty report, because no value is Greater Than 31,500.
 
        """
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",5, 2, 1)
        time.sleep(2)
         
        miscelanousobj.verify_page_summary(0, '0of18records,Page1of1', 'Step 9.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '0of18records,Page1of1', 'Step 9.2a: Verify the Report Heading for report 2')
         
         
        """
            10. Return the button to its full left position, so that it displays 3139 again.
            10.1. Expect to see a 17 row report, only 3139 is excluded because it is not Greater Than 3139.
        """
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pagedown",5, 2, 1)
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds10.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds10.xlsx', 'Step 10.1: Verify data report1.')
         
        miscelanousobj.verify_page_summary(0, '17of18records,Page1of1', 'Step 10.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '0of18records,Page1of1', 'Step 10.2a: Verify the Report Heading for report 2')
         
        
        """
            11. Using the bottom right slider, which controls the left side report and is labeled 'V slider for Retail_Cost Less Than', move the control upwards until the value is as near to 10000 as possible.
            11.1. Expect to see a 13 row report showing all values Less Than 10,000.
        """        
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",1,3, 1)
        time.sleep(6)
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "up",1211, 3, 0)
        time.sleep(6)
        miscelanousobj.verify_page_summary(0, '13of18records,Page1of1', 'Step 11.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '0of18records,Page1of1', 'Step 11.2a: Verify the Report Heading for report 2')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds11.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds11.xlsx', 'Step 11.1: Verify data report1.')

        """
            12.Continue to drag the button all the way to the top until it displays 31500.
            12.1. Expect to see an 17 row report with the only value excluded bring 31,500 because it's not Less Than 31500.
        """
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pageup",5, 3, 1)
        time.sleep(6)
       
        miscelanousobj.verify_page_summary(0, '17of18records,Page1of1', 'Step 12.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '0of18records,Page1of1', 'Step 12.2a: Verify the Report Heading for report 2')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds12.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds12.xlsx', 'Step 12.1: Verify data report1.')
        
        """
            13. Drag the button all the way back down to its minimum value of 3139.
            13.1. Expect to see an empty report, because no value is Less Than 3,139.

        """
        utillobj.drag_slider_using_pageup_or_pagedown("#orgdiv0", "[class^='ui-slider-handle']", "pagedown",6, 3, 1)
        time.sleep(6)       
        miscelanousobj.verify_page_summary(0, '0of18records,Page1of1', 'Step 13.2a: Verify the Report Heading for report 1')
        miscelanousobj.verify_page_summary(1, '0of18records,Page1of1', 'Step 13.2a: Verify the Report Heading for report 2')
        
        
if __name__=='__main__' :
    unittest.main()      
        