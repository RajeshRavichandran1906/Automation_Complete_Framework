'''
Created on Sep 28, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050536

Test case Name =Verify Sub header is displayed correctly with styling applied

'''
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,ia_styling
from common.lib import utillity
import unittest,time

class C2203714_TestClass(BaseTestCase):

    def test_C2203714(self):
        """
        Step 01: Right click on folder created in IA and select New > Report and select Reporting server as GGSALES.
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        utillobj.infoassist_api_login('report','ibisamp/ggsales','P116/S7072', 'mrid', 'mrpass')
        
        element_css="div[id='HomeTab'] div[id='HomeFormatType']"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=30)
        
        """Step 02:On the Format tab, in the Output Types group, click Active Report"""  
        ribbonobj.change_output_format_type('active_report')        
           
        """Step 03: Select data from the left pane (Dimensions and Measures) Category, Product ID, Product, State, Unit Sales, Dollar Sales."""
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
        time.sleep(15)
            
        expected_list= ['Category','Product ID','Product','State', 'Unit Sales', 'Dollar Sales']
        resobj.verify_report_titles_on_preview(6, 6, 'TableChart_1', expected_list, 'Step 02: See corresponding data is displayed in the Live Preview pane.')
        time.sleep(2)    
            
        """Step 04: Click Run command"""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        utillobj.verify_data_set('ITableData0','I0r','C2203714_Ds01.xlsx',"Step 03: Expect to see an 18 row report with Country, Car, Model, Seats")
        utillobj.switch_to_default_content(pause=2)
        ribbonobj.select_tool_menu_item("menu_save")
        time.sleep(5)
        utillobj.ibfs_save_as('AR_RP_001c')
        time.sleep(6)
         
        """Step 05: Edit the ARRP001c.fex via IA."""       
        utillobj.infoassist_api_edit('AR_RP_001c', 'Report', 'S7072')
        
        element_css="div[id='HomeTab'] div[id='HomeFormatType']"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=30)
        
        """Step 06 : Highlight 'Category' column under report."""
        metaobj.querytree_field_click('Category', 1)
        time.sleep(8)
        css = "#FieldTab_tabButton" 
        utillobj.asequal(True, (driver.find_element_by_css_selector(css).text=='Field - Category'), "Step 06 : Verify Field category menu is available")
        
        
        """Step 07: Click Sub Footer link."""
        """Step 08:Enter text as GGSALES SUB FOOTING"""
        #self.driver.find_element(*VisualizationRibbonLocators.__dict__['field_sub_footer']).click()
        ia_stylingobj.create_sub_header_footer('Sub_footer', 'GGSALES SUB FOOTING')
        time.sleep(6)
        
        """Step 09: Verify that "GGSALES SUB FOOTING" is displayed above each category. Save the fex."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        css = "[id^='THEAD_0_']"
        tr = driver.find_elements_by_css_selector(css)
        value = [td.text for td in tr]
        utillobj.asin('GGSALES SUB FOOTING', value, 'Step 09: Verify that "GGSALES SUB FOOTING" is displayed above each category. Save the fex')
        time.sleep(3)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(4)
        
if __name__ == '__main__':
    unittest.main()
        
