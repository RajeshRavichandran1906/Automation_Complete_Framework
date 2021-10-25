'''
Created on June7, 2016
@author: Kiruthika

Test Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109018&group_by=cases:section_id&group_id=146864&group_order=asc
TestCase Name : IA-4328:BUE: Lasso Filter in Visualization with Prompt, Color By with different Date Formats are not working in Preview
'''
import unittest,time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea
from common.lib import utillity
from common.wftools.visualization import Visualization

class C2109018_TestClass(BaseTestCase):
    
    def test_C2109018(self):
        
        """
        TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        Test_Case_ID = 'C2109018'
        element_css = '#queryTreeWindow'
        
        """
        CLASS OBJECTS
        """
        visual = Visualization(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step 01: Launch API (Folder - S8357 and Master - wf_retail_lite) and login as "autodevuser03"
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')

        """
        Step 02: Add Sales Related > Transaction Date, Compound >Sale,Year(YYMDy) to Horizontal axis
        """
        metaobj.datatree_field_click('Dimensions->Sales_Related->Transaction Date, Components->Sale,Year', 1, 1,'Add To Query','Horizontal Axis')
        visual.wait_for_visible_text(element_css, 'Sale,Year')   
        
        """
        Step 03: Add Revenue to Vertical axis.
        """
        metaobj.datatree_field_click('Revenue',2,1)
        visual.wait_for_number_of_element('#MAINTABLE_wbody1 rect[class*="riser"]', 6)
        visual.wait_for_visible_text('#MAINTABLE_wbody1 text[class="yaxis-title"]', 'Revenue')

        """
        Step 04: Verify chart labels in preview.
        """
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Sale Year",'Step 04.01: Verify X title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue",'Step 04.02: Verify Y title')
        
        """
        Step 05: Verify query pane
        Vertical Axis > Revenue, Horizontal Axis> Sale,Year
        """
        metaobj.verify_query_pane_field('Horizontal Axis', 'Sale,Year',1,"Step 05.01")
        metaobj.verify_query_pane_field('Vertical Axis', 'Revenue',1,"Step 05.02")
        
        """
        Step 06: drag and drop Sales Related > Transaction Date, Compound >Sale,Day (YYMD) to filter pane and change the operator from 01/01/2015 To 05/03/2016
        """
        metaobj.drag_drop_data_tree_items_to_filter('Dimensions->Sales_Related->Transaction Date, Components->Sale,Day', 1)
        utillobj.synchronize_until_element_is_visible('#avFilterOkBtn', 190)
        time.sleep(5)
        start_date=['Jan','01','2015']
        end_date=['May','03','2016']
        metaobj.create_visualization_filters('numeric',['Starting Date',start_date], ['Ending Date',end_date])
        time.sleep(5)
        
        """
        Step 08: Verify output in preview
        """
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        time.sleep(8)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 08.01: Verify the total number of risers displayed on Run Chart')
        a=['Sale Year:2015', 'Revenue:$282,541,804.48', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Year/Quarter']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar',a,"Step 08.02: Verify output in preview - first bar")
        
        """
        Step 09: Add Customer Business Region to Color.
        """
        metaobj.datatree_field_click('Customer,Business,Region',1,1,'Add To Query','Color')
        visual.wait_for_visible_text(element_css, 'Customer,Business,Region') 
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s1']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        time.sleep(8)
        
        """
        Step 10: Verify output in preview.
        """
        a=['Sale Year:2016', 'Revenue:$68,053,741.09', 'Customer Business Region:EMEA', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g1!mbar',a,"Step 10.01: Verify output in preview - 2016-EMEA bar")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 4, 2, 'Step 10.02: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2015', '2016']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M']       
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 10.03: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s3!g1!mbar!", "pale_yellow", "Step 10.04: Verify first bar color")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", 'Sale Year', "Step 10.05: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", 'Revenue', "Step 10.06: Verify Y-Axis Title")
        
        """
        Step 11: Verify customer business region added to query pane
        """
        metaobj.verify_query_pane_field('Color BY','Customer,Business,Region',1,"Step 11.01")

        """
        Step 12: Lasso 2015 and 2016 EMEA points and filter chart.
        """ 
        time.sleep(5)
        source_element = self.driver.find_element_by_css_selector('#MAINTABLE_wbody1 rect[class*="riser!s0!g0!mbar!"]')
        target_element = self.driver.find_element_by_css_selector('#MAINTABLE_wbody1 rect[class*="riser!s0!g1!mbar!"]')
        visual.create_lasso(source_element, target_element, source_element_location='bottom_middle', target_element_location='bottom_middle')
        visual.select_lasso_tooltip('Filter Chart')
        visual.wait_for_number_of_element('#MAINTABLE_wbody1 rect[class*="riser"]', 2)
        
        """
        Step 13: Verify riser values
        """
        a =['Sale Year:2015', 'Revenue:$140,440,022.62', 'Customer Business Region:EMEA', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar', a, "Step 13.01: Verify riser values - 2015-EMEA bar")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 13.02: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2015', '2016']
        expected_yval_list=['0', '40M', '80M', '120M', '160M']       
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 13.03: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 13.04: Verify first bar color")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", 'Sale Year', "Step 13.05: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", 'Revenue', "Step 13.06: Verify Y-Axis Title") 
        resultobj.verify_riser_legends("MAINTABLE_wbody1_f",['Customer Business Region','EMEA'],"Step 13.07: Verify legends")
         
        """
        Step 14: Click run in toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
         
        """
        Step 15: Verify output.
        """
        utillobj.synchronize_until_element_is_visible('[class*="riser!s0!g0!mbar"]', 190)
        a = ['Sale Year:2015', 'Revenue:$140,440,022.62', 'Customer Business Region:EMEA', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",a,"Step 15.01: Verify riser values - 2015-EMEA bar")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 15.02: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2015', '2016']
        expected_yval_list=['0', '40M', '80M', '120M', '160M']       
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 15.03: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 15.04: Verify first bar color")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", 'Sale Year', "Step 15.05: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", 'Revenue', "Step 15.06: Verify Y-Axis Title") 
        resultobj.verify_riser_legends("MAINTABLE_wbody1_f",['Customer Business Region','EMEA'],"Step 15.07: Verify legends")
                 
        """
        Step 16: Close the output window
        """
        visual.switch_to_previous_window()
         
        """
        Step 17: Click "Save" in the toolbar > Type C2109018 > Click "Save" in the Save As dialog
        """
        utillobj.synchronize_until_element_is_visible("#applicationButton img", 90)
        visual.save_visualization_from_top_toolbar(Test_Case_ID)
        
        """
        Step 18 : Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()