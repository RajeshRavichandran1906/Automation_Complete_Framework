
'''
Created on May20, 2016
@author: gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2107478
'''

__author__ = "Gobizen"
__copyright__ = "IBI"

import unittest
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, define_compute
from common.locators import visualization_resultarea_locators
from common.lib import utillity
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



class C2140678_TestClass(BaseTestCase):

    def test_C2140678(self):

        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2140678'
        name = 'MYDATE_MYY' #date format to select
        unit = 'Unit Price'
        
        """
        Step 01: Launch the IA API with wf_retail_lite
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/GGORDER&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
        """
        The signon screen will be displayed.
        Login as userid devuser (autodevuser01/02/03/04/05) and blank password
        
        """
        utillobj = utillity.UtillityMethods(self.driver)
        #utillobj.infoassist_api_login('idis','baseapp/ggorder','S8357', 'mrid02', 'mrpass02')
        utillobj.infoassist_api_login('idis','baseapp/ggorder','P312/S10099_4', 'mrid', 'mrpass')
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        time.sleep(6)
         
        """
        Step 02: Create a new Calculation -> Define.
        Step 03 : In the DEFINE dialog box, enter field name of MYDATE_MYY
        Step 04: Click on the Format button, select "Date", and choose the format of "MYY", click OK
        Step 05: Select "Order,Date" from the field list, Click OK.
        """
        defcomp.calculate_define_compute('Define', name, 'MYY', 'Order,Date', 1, 'ok')         
        time.sleep(8)
         
        """
        Step 06 : Verify define is added to data pane.
        """
        metaobj.verify_data_pane_field('Dimensions', 'MYDATE_MYY', 9, 'Step 06')
        time.sleep(3)
        
        """
        Step 07, 08: Add MYDATE_MYY to Horizontal Axis and Unit, Price to Vertical Axis.
        """
        metaobj.datatree_field_click('Dimensions->MYDATE_MYY', 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click('Unit,Price', 2, 1)
        time.sleep(10)        
         
        """
        Step 09:Verify label values
        """       
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 25) 
        time.sleep(3)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 25, 'Step 08a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['11/1990', '01/1996', '02/1996', '03/1996', '04/1996', '05/1996', '06/1996', '07/1996', '08/1996', '09/1996', '10/1996', '11/1996', '12/1996', '01/1997', '02/1997', '03/1997', '04/1997', '05/1997', '06/1997', '07/1997', '08/1997', '09/1997', '10/1997', '11/1997', '12/1997']
        expected_yval_list=['0', '2K', '4K', '6K', '8K', '10K', '12K']        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 08b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 08.c(i) Verify first bar color")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", name, "Step 09:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", unit, "Step 09:d(ii) Verify Y-Axis Title")
      
        """
        Step 10: Verify query pane
        """    
        metaobj.verify_query_pane_field("Vertical Axis", "Unit,Price", 1, "Step 10a")
        metaobj.verify_query_pane_field("Horizontal Axis", "MYDATE_MYY", 1, "Step 10b")
        
        """
        Step 11: Verify first and last 3 bar riser values
        """
        step11 = 'Step 11:Verify first 3 and last 3 chart/grid values (tooltip values)'
        tooltip_value = ["MYDATE_MYY:01/1996","Unit Price:10,698.00",'Filter Chart', 'Exclude from Chart' ]
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", 'riser!s0!g1!mbar', tooltip_value, step11)
        
        #Last 1 Values verifications
        expected_tooltip=['MYDATE_MYY:12/1997', 'Unit Price:10,797.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g24!mbar",expected_tooltip, "Step 11.b: verify the default tooltip values")
        time.sleep(4)

        """
        Step 12: Hover over one of the bars and select "Filter".
        """
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', 'riser!s0!g5!mbar', 'Filter Chart')
        time.sleep(10)
        
        """
        Step 13 : Verify filtered tooltip.
        Step 13: Verify exact value got filtered.
        """
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1) 
        time.sleep(5)
        tooltip_value = ["MYDATE_MYY:05/1996","Unit Price:10,698.00"]
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", 'riser!s0!g0!mbar', tooltip_value,"Step 13a: verify tooltip values")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 13b: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['05/1996']
        expected_yval_list=['0', '2K', '4K', '6K', '8K', '10K', '12K']        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 13b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 13c: Verify first bar color")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", name, "Step 13d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", unit, "Step 13dd(ii) Verify Y-Axis Title")
        metaobj.verify_filter_pane_field(name,1, 'Step 13e : Verify Query is added to filter pane.')
        
        """
        Step 14: Click Run in the toolbar
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(4)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        """
        Step 15: Verify output
        """
        time.sleep(10)
        tooltip_value = ["MYDATE_MYY:05/1996","Unit Price:10,698.00"]
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", 'riser!s0!g0!mbar', tooltip_value,"Step 15a: verify tooltip values")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 15b: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['05/1996']
        expected_yval_list=['0', '2K', '4K', '6K', '8K', '10K', '12K']        
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 15b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 15c: Verify first bar color")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", name, "Step 15d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", unit, "Step 15d(ii) Verify Y-Axis Title")
        time.sleep(2)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2140678_Actual_step15', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)
        """
        Step 16: Close the output window 
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        
        """
        Step 17 : Click "Save" in the toolbar > Type C2140678 > Click "Save" in the Save As dialog
        """
        time.sleep(2)  
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
      

if __name__ == '__main__':
    unittest.main()

