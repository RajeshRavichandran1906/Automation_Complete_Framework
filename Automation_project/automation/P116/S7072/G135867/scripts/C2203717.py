'''
Created on Oct 04, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203717

Test case Name = Verify Pivot Table status for problem - Filter/Equals options are not accessible.

'''
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea
from common.lib import utillity
import unittest,time

class C2203717_TestClass(BaseTestCase):

    def test_C2203717(self):        
        def drilldown(URL):
            driver.find_element_by_css_selector("#rBtnUrl input").click()
            time.sleep(4)
            driver.find_element_by_css_selector("input#tfUrl").send_keys(URL)
            time.sleep(3)
            driver.find_element_by_css_selector("div#ok").click()       
            time.sleep(4)
        
        """
        Step 01:Right click on folder created in IA and select New > Report and select Reporting server as GGSALES.
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.infoassist_api_login('report','ibisamp/ggsales','P116/S7072', 'mrid', 'mrpass')
        element_css="div[id='HomeTab'] div[id='HomeFormatType']"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=30)
        
        """Step 02: On the Format tab, in the Output Types group, click Active Report"""
         
        ribbonobj.change_output_format_type('active_report')
        time.sleep(4)
        
        """Step 03: Select data from the left pane (Dimensions and Measures) Category, Product ID, Product, State, Unit Sales, Dollar Sales""" 
        metaobj.datatree_field_click("Category",2,1)
        time.sleep(6)
        metaobj.datatree_field_click("Product ID", 2, 1)
        time.sleep(6)
        metaobj.datatree_field_click("Product",2,1)
        time.sleep(6)
        metaobj.datatree_field_click("State",2,1)
        time.sleep(6)
        metaobj.datatree_field_click("Unit Sales",2,1)
        time.sleep(6)
        metaobj.datatree_field_click("Dollar Sales",2,1)
        time.sleep(10)
         
        expected_list= ['Category','Product ID','Product','State', 'Unit Sales', 'Dollar Sales']
        resobj.verify_report_titles_on_preview(6, 6, 'TableChart_1', expected_list, 'Step 03: See corresponding data is displayed in the Live Preview pane.')
         
        """Step 04: Click Run command"""
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        #Verify Active Report is displayed and all the report menu options are present on a report Save as AR-RP-001 and exit the report.
        #Expect to see an 18 row report with Country, Car, Model, Seats.
         
        utillobj.verify_data_set('ITableData0','I0r','C2203717_Ds01.xlsx',"Step 04: Expect to see an 107 row report")
        time.sleep(2)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(8) 
        ribbonobj.select_tool_menu_item("menu_save")
        time.sleep(5)
        utillobj.ibfs_save_as('AR_RP_C2203717')
        time.sleep(8)
         
        """Step 05: Edit the AR-RP-001.fex via IA."""
        utillobj.infoassist_api_edit('AR_RP_C2203717', 'Report', 'S7072')
        element_css="div[id='HomeTab'] div[id='HomeFormatType']"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=30)
        
        """Step 06 : Highlight Product column under report.."""
        metaobj.querytree_field_click('Product', 1)
        time.sleep(6)
        
        
        """Step 07: Click Links > Hyperlink option."""
        ribbonobj.select_ribbon_item('Field', 'DrillDown')
        time.sleep(8)
        
        """Step 08: Select Web Page (default option) and add URL as 'http://www.google.com'. Set Target as New Window and click Ok."""
        drilldown('http://www.google.com') 
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(2)
        
        drilldown_count = len(driver.find_elements_by_css_selector("#ITableData0 [id$='C2'] [title='Drill Down 1']"))
      
        utillobj.asequal(6, drilldown_count, 'Step 08: Verify Drill down present in all titles')
        
        """Step 09: Click on the Google link."""
        driver.find_element_by_css_selector("[id^=I0r0][id$=C2]").click()
        time.sleep(4)
        
        driver.switch_to.default_content()
        time.sleep(5)
        s = driver.window_handles
        time.sleep(5)
        driver.switch_to.window(s[-1])
        time.sleep(5)
        title = driver.title
        utillobj.asin('Google', title, 'Step 09: Verify that user will be redirected to Google.com correctly. ')
        time.sleep(3)
        driver.switch_to.window(s[0])
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()
           