'''
Created on June28, 2016
@author: Kiruthika

Test Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=147037&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2140847
TestCase Name : IA-4551:Displaying empty chart if filter on data value containing ampersand
'''
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.pages import core_metadata

class C2140847_TestClass(BaseTestCase):

    def test_C2140847(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2140847'
        """
        Step 01: Launch the IA API with customer_data (Folder - S8404 and Master - customer_data) and login as "autodevuser03"
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/Customer_Data&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F
        """
        core_meta_obj = core_metadata.CoreMetaData(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/customer_data','P312/S10099_5', 'mrid', 'mrpass')
        
#         utillobj.infoassist_api_login('idis','baseapp/customer_data','S8404', 'mrid04', 'mrpass04')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        
        """
        Step 02: Add Company Name to Horizontal axis
        """
        core_meta_obj.collapse_data_field_section('Measure Groups')
        metaobj.datatree_field_click('Dimensions->Sheet1->Company->Company Name', 2, 1)
        time.sleep(5)
        
        """
        Step 03: Add Number of Days Since Contact to vertical axis
        """
        core_meta_obj.collapse_data_field_section('Dimensions')
        metaobj.datatree_field_click('Measure Groups->Sheet1->Number of Days Since Contact',2,1)
        
        """
        Step 04: Verify label values
        """ 
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', 'Company Name', "Step 04: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', 'Number of Days Since Contact', "Step 04: verify Y axis title")
            
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1000, 'Step 04a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['1-800-FLOWERS.CO...', '1199SEIU Benefit an...', '3M Company', '99 Cents Only Stores', 'A. M. Castle & Co.']
        expected_yval_list=['0', '10', '20', '30', '40', '50', '60', '70']
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 04b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 04b(i): Verify bar color")
        
        """
        Step 05: verify query pane
        """
        metaobj.verify_query_pane_field('Horizontal Axis', 'Company Name', 1,"Step 05: Verify query pane")
        metaobj.verify_query_pane_field('Vertical Axis', 'Number of Days Since Contact', 1,"Step 05: Verify query pane")
        
        """
        Step 06: Verify bar riser values
        """
        a =['Company Name:1-800-FLOWERS.COM, Inc.', 'Number of Days Since Contact:15', 'Filter Chart', 'Exclude from Chart', 'Drill down to Company Industry']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar',a,"Step 06: Verify bar riser values")
        
        """
        Step 07:  Hover over a company name that contains '&', like Abercrombie & Fitch Co. > Filter
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g4!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', 'riser!s0!g4!mbar', 'Filter Chart')
        time.sleep(10)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, "#MAINTABLE_wbody1 svg g.risers >g>rect")) == 1)
        
        """
        Step 08: Verify query added to filter
        """
        metaobj.verify_filter_pane_field('Company Name',1,"Step 08: Verify query added to filter")
        
        """
        Step 09: Verify filtered bar values.
        """
        try:
            elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g0!mbar']")
            resultobj._validate_page(elem1)
            resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 09a: Verify the total number of risers displayed on Run Chart')
            expected_xval_list=['A. M. Castle & Co.']
            expected_yval_list=['0', '3', '6', '9', '12']
            raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
            elem1=(By.CSS_SELECTOR, raiser)
            resultobj._validate_page(elem1)
            resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 09: X annd Y axis Scales Values has changed or NOT')
            utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09: Verify bar color")
        
            a =['Company Name:A. M. Castle & Co.', 'Number of Days Since Contact:11', 'Drill down to Company Industry']
            resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar', a, "Step 09: Verify filtered bar values")
        except TimeoutException:
            utillity.UtillityMethods.asequal(self,'no','yes',"Step 09: Verify filtered bar values- Product Failure")
        
        """
        Step 10: Click Run in the toolbar
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)
        
        
        """
        Step 11: Verify output
        """      
        elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
        try:
            WebDriverWait(self.driver, 70).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='riser!s0!g0!mbar']")))
            time.sleep(10)
            resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step11: Verify the total number of risers displayed on Run Chart')
            expected_xval_list=['A. M. Castle & Co.']
            expected_yval_list=['0', '3', '6', '9', '12']
            raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
            elem1=(By.CSS_SELECTOR, raiser)
            resultobj._validate_page(elem1)
            resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step11: X and Y axis Scales Values has changed or NOT')
            
            a =['Company Name:A. M. Castle & Co.', 'Number of Days Since Contact:11', 'Drill down to Company Industry']
            resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', 'riser!s0!g0!mbar', a, "Step 11: Verify filtered bar values")
            utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11(i): Verify bar color")
        except TimeoutException:
            utillity.UtillityMethods.asequal(self, 'no', 'yes',
                                             "Step 11: Verify filtered bar values- Product Failure")
        
        time.sleep(10)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2140847_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)         
        
        """
        Step 12: Close the output window.
        """
        time.sleep(3)
        self.driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        """
        Step 13: Click "Save" in the toolbar > Type C2140687 > Click "Save" in the Save As dialog
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
                              
        """
        Step 14: Logout of the IA API using the following URL.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """