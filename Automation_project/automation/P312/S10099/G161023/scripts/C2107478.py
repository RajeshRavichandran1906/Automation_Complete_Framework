
'''
Created on May09, 2016
@author: gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2107478
'''
from lib2to3.pgen2.driver import Driver
from pymsgbox import alert

__author__ = "Gobizen"
__copyright__ = "IBI"

import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from common.lib import utillity 
from common.lib.basetestcase import BaseTestCase
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, loginpage, visualization_ribbon
from common.locators import visualization_metadata_locators, visualization_properties_locators, visualization_resultarea_locators
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators
from common.locators.visualization_properties_locators import VisualizationPropertiesLocators
from common.locators.visualization_metadata_locators import VisualizationMetadataLocators
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators


class C2107478_TestClass(BaseTestCase):

    def test_C2107478(self):

        driver = self.driver #Driver reference object created
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2107478'
        #data01 = ['Sale Year:  2011', 'Revenue:  48965069']
        #data05 = ['Sale Year:  2016', 'Revenue:  452307832']
        
        """
        Launch the IA API with wf_retail_lite
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F

        """
        utillobj = utillity.UtillityMethods(self.driver)
        browser=utillobj.parseinitfile('browser')
        if browser=='IE' or browser=='Chrome':
            utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099', 'mrid', 'mrpass')
                    
            element_css="#resultArea svg>g.chartPanel rect[class*='riser!']"
            utillobj.synchronize_with_number_of_element(element_css, 12, 60)
            """
            The signon screen will be displayed.
            Login as userid devuser (autodevuser01/02/03/04/05) and blank password
            """
            """
            Step 02: Change chart type to Grid, double click on Revenue, Sale Year.
            """
                
            ribbonobj.change_chart_type("grid")
            time.sleep(3)#wait for chart changes reflect
            metaobj.datatree_field_click('Revenue', 2, 1)
            time.sleep(3)
            metaobj.datatree_field_click('Sale,Year', 2, 1)
            
            """
            Step 03 : Verify field labels.
            """
            time.sleep(8)
            title = ['Sale Year', 'Revenue']
            resultobj.verify_grid_column_heading('MAINTABLE_wbody1',title, 'Step 03: Verify field titles')
     
            """
            Step 04:Verify grid output in preview
            Sale Year:Revenue - 2011:$48,965,069.21, 2012:$61,140,962.97, 2013:$89,561,595.40, 2014:$126,675,660.19, 2015:$282,541,804.48 and 2016:$452,307,832.95
            """
            time.sleep(3)
            row_val=['2011', '$48,965,069.21']
            resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val,'Step 04.2: verify grid 1st row value')
    #         resultobj.verify_grid_data_set('MAINTABLE_wbody1',2,'C2107478_Ds01.xlsx', "Step 04.3: Verify Grid 2 measure data set")
                   
            """
            Step 05: Add Sale Quarter, Sale Month, Customer,Business,Region, Customer Business Sub Region, Customer Country, Product Category to Rows.
            """
            metaobj.datatree_field_click('Sale,Quarter', 2, 1)
            time.sleep(3)
            metaobj.datatree_field_click('Sale,Month', 2, 1)
            WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 3)
            metaobj.datatree_field_click('Customer,Business,Region', 2, 1)
            WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 4)
            metaobj.datatree_field_click('Customer,Business,Sub Region', 2, 1)       
            WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 5)
            metaobj.datatree_field_click('Customer,Country', 2, 1)        
            WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 6)
            metaobj.datatree_field_click('Product,Category', 2, 1)
     
            """
            Step 06 : Verify field labels.
            """
            browser=utillobj.parseinitfile('browser')
            if browser=='IE':
                time.sleep(50)
            WebDriverWait(self.driver, 300).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 7)
            parent_css1=".rowTitle text"
            resultobj.wait_for_property(parent_css1, 7)
            time.sleep(10)
            parent_css1=".colHeader text"
            resultobj.wait_for_property(parent_css1, 1)
            #serunner text
            ieandchrome=['Sale Year', 'Sale Quarter', 'Sale Month', 'Customer Business Region', 'Customer Business Sub Region', 'Customer Country', 'Product Category', 'Revenue']
            #old = ['Sale Y...', 'Sale Qua...', 'Sale Mo...', 'Customer Business Re...', 'Customer Business Sub Re...', 'Customer Cou...', 'Product Categ...', 'Revenue']
            resultobj.verify_grid_column_heading('MAINTABLE_wbody1',ieandchrome, 'Step 06: Verify field labels')
     
            """
            Step 07: Verify first two values, scroll down and verify last two rows values
            """
            time.sleep(10)
            row1 =['2011', '1', '1', 'EMEA', 'Europe', 'Czech Republic', 'Accessories', '$168.00']
            resultobj.verify_grid_row_val('MAINTABLE_wbody1',row1,'Step 07.1: Verify first row value')
            
            """
            Step 08 : Add Customer Country to Filter and select only United States and click ok.
            """
            time.sleep(5)
            metaobj.datatree_field_click('Customer,Country',1,1,'Filter')
            time.sleep(15)
            l='United States'
            browser=utillity.UtillityMethods.parseinitfile(self,'browser')
            if browser == 'IE':
                parent_css1="#alphaFieldPanel #avAlphaOperatorComboBox div[id^='BiButton']"
                resultobj.wait_for_property(parent_css1, 1)
    #             utillobj.select_combobox_item("#avAlphaOperatorComboBox", "Equal to")
                time.sleep(2)
                search_element = self.driver.find_element_by_css_selector("#avSearchBox > input")
                search_element.click()
                time.sleep(3)
                search_element.clear()
                time.sleep(5)
                pyautogui.typewrite('United States')
                time.sleep(20)
                metaobj.create_visualization_filters('alpha')
            else:
                time.sleep(2)   
                metaobj.create_visualization_filters('alpha',['Operator','Equal to'],['SearchValues',l])
    
            """
            Step 09:Verify query added to filter pane, scroll down in filter prompt and verify United stated is checked.
            """
            time.sleep(10)
            metaobj.verify_filter_pane_field("Customer,Country", 1, 'Step 09.1:Verify query added to filter pane')
            #Verify United states checked
            propertyobj.select_or_verify_show_prompt_item(1, 'United States', True,verify_type=True,msg="Step 09.2: Verify value in filter prompt is United Sales")        
            
            """
            Step 10: Change the Filter to dropdown.
            """
            #time.sleep(10)
            utillobj.synchronize_with_number_of_element("div#ar_Prompt_1 table span", 1, 20, 1)
            propertyobj.change_prompt_options('1', 'Dropdown (Single Select)')
            time.sleep(15)
    
            """
            Step 11 : Verify grid top 3 values and last 3 values of United States
            """
            new=['2011', '1', '1', 'North America', 'East', 'United States', 'Accessories', '$21,685.91']   
            #row2 = ['2011', '1', '1', 'North America', 'East', 'United Sta...', 'Accessories', '$21,685.91'] 
            resultobj.verify_grid_row_val('MAINTABLE_wbody1',new,'Step 11.1: verify grid 1st row value')
            
            """
            Step 12: Click "Save" in the toolbar > Type C2107478 > Click "Save" in the Save As dialog
            Save the fex with the same name as this test case.
            """
            time.sleep(2)
            #ribbonobj.select_tool_menu_item('menu_save_as')
            ribbonobj.select_top_toolbar_item('toolbar_save')
            utillobj.ibfs_save_as(Test_Case_ID)
            time.sleep(5)
                
#             except TimeoutException:
#                 WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[class^=bi-iframe iframe]')))
#                 print("except")
                
        else: 
            utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P141/S8357', 'mrid', 'mrpass')
            elem1=VisualizationResultareaLocators.__dict__['default_riser']
            resultobj._validate_page(elem1)                  
            print("Issue in Firefox browser: Adding many fields to Grid browser becomes unresponsive: Known Product Failure - IA-5727")
            time.sleep(5)

if __name__ == '__main__':
    unittest.main()

