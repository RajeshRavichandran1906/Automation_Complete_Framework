'''
Created on June'02, 2016
@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109014
'''
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators

class C2109014_TestClass(BaseTestCase):

    def test_C2109014(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2109014'
        """
            Step 01: Launch the IA API with wf_retail_lite
            http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_4', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """
        Step 02: Double click Revenue & Product,Category
        """
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(10)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(15)
        """
        Step 03: verify x and y axis labels.
        """
        resultobj.verify_xaxis_title('MAINTABLE_wbody1_f', "Product Category",'Step 03: Verify X title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1_f', "Revenue",'Step 03: Verify Y title')
        
        """
        Step 04: Verify query pane dialog.
        """
        metaobj.verify_query_pane_field("Vertical Axis", "Revenue",1,"Step 04: Verify query pane Horizontal Axis.")
        metaobj.verify_query_pane_field("Horizontal Axis","Product,Category",1,"Step 04: Verify query pane Vertical Axis.")
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 7)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 15a: Verify the total number of risers displayed on Run Chart')
        
        """
        Step 05: Lasso first 3 bars (Accessories, Camcorder, Computers) > Filter Chart
        """
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g0!mbar!', target_tag='rect', target_riser='riser!s0!g2!mbar')
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 3)
        
        """
        Step 06: Verify query added to filter pane
        """
        time.sleep(10)
        metaobj.verify_filter_pane_field("Product,Category",1,"Step 06: Verify Product,Category added to filter pane")
        
        """
        Step 07: Verify filtered riser values in tooltip.
        """        
        time.sleep(2)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 07: Verify the total number of risers displayed')
        a=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar', a, "Step 07: Verify filtered riser values in tooltip.")
        time.sleep(5)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers']
        expected_yval_list=['0', '40M', '80M', '120M', '160M']       
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 07: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 07c: Verify first bar color")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", 'Product Category', "Step 07d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", 'Revenue', "Step 07d(ii) Verify Y-Axis Title")
        time.sleep(4)
        
        """
        Step 08: Click run in toolbar.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='riser!s0!g0!mbar']")))
         
        """
        Step 09: lasso first 2 bars (Accessories, Camcorder) > Filter Chart
        """
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g0!mbar!', target_tag='rect', target_riser='riser!s0!g1!mbar')
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2) 
        """
        Step 10: Verify Accessories and camcorder values in tooltip
        """        
        time.sleep(10)
        b=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill down to Product Subcategory']
        c=['Product Category:Camcorder', 'Revenue:$154,465,702.24', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar', b, "Step 10.1: Verify Accessories values in tooltip")
        time.sleep(5)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g1!mbar', c, "Step 10.2: Verify camcorder values in tooltip")
        time.sleep(5)
        expected_xval_list=['Accessories', 'Camcorder']
        expected_yval_list=['0', '40M', '80M', '120M', '160M']       
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 10.3: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 10.3c: Verify first bar color")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", 'Product Category', "Step 10.3d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", 'Revenue', "Step 10.3d(ii) Verify Y-Axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 10: Verify the total number of risers displayed')
         
        """
        Step 11: Hover on a bar and click remove filter
        """
        time.sleep(5)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g0!mbar", 'Remove Filter') 
        time.sleep(10) 
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 3)
        time.sleep(10) 
         
        """
        Step 12: Verify output.
        """        
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 3, 'Step 12.1: Verify number of risers displayed is 3')
        time.sleep(2)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers']
        expected_yval_list=['0', '40M', '80M', '120M', '160M']       
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 12.2: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 12.3c: Verify first bar color")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", 'Product Category', "Step 12.3d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", 'Revenue', "Step 12.3d(ii) Verify Y-Axis Title")
        time.sleep(8)
        
        """
        Step 13: Close the output window.
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        
        """
        Step 14: Right click filter in filter pane > Delete
        """
        time.sleep(4)
        metaobj.filter_tree_field_click("Product,Category",1,1,"Delete")
        time.sleep(10)
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 7)
        time.sleep(10)
        """
        Step 15: Hover over first bar (Accessories) > Exclude from chart
        """        
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g0!mbar", 'Exclude from Chart')
        time.sleep(15)
         
        expected_xval_list=['Camcorder', 'Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M','250M','300M','350M']       
        time.sleep(5)
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 6, 'Step 15: Verify number of risers displayed is 6')
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 15.2: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 15.3c: Verify first bar color")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", 'Product Category', "Step 15.3d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", 'Revenue', "Step 15.3d(ii) Verify Y-Axis Title")
        
        """
        Step 16: Right click on product category in filter pane and click edit.
        """
        time.sleep(10)
        metaobj.filter_tree_field_click("Product,Category",1,1,"Edit...")
        time.sleep(10)
        elem11="#avFilterOkBtn"
        elem1=(By.CSS_SELECTOR, elem11)
        resultobj._validate_page(elem1)
        time.sleep(10)
        """
        Step 17: Verify filter dialog.
        """
        selectedValues = ["Accessories"]
        metaobj.select_or_verify_visualization_filter_values(selectedValues, verify='true',Ok_button=True)
        time.sleep(5)
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 6)
        time.sleep(10) 
        """
        Step 18: Click run in toolbar.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        """
        Step 19: Lasso first 2 bars (Camcorder, Computers) > Exclude from Chart
        """
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='riser!s0!g0!mbar']")))
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g0!mbar!', target_tag='rect', target_riser='riser!s0!g1!mbar')       
        resultobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        time.sleep(15)
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 4)
        time.sleep(10)
        """
        Step 20: Verify bar riser values
        """        
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 4, 'Step 20.1: Verify number of risers displayed is 4')
        time.sleep(6)
        e=['Product Category:Media Player', 'Revenue:$246,073,059.36', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar', e, "Step 20.2: Verify bar riser values")
        expected_xval_list=['Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M','250M','300M','350M']    
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 20.2: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 20.3c: Verify first bar color")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", 'Product Category', "Step 20.3d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", 'Revenue', "Step 20.3d(ii) Verify Y-Axis Title")
        
        """
        Step 21: hover on a bar and click remove filter
        """
        time.sleep(8)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g0!mbar", 'Remove Filter')
        time.sleep(10)
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 6)
        time.sleep(10)
        """
        Step 22: verify output
        """        
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 6, 'Step 22.1: Verify number of risers displayed is 6')
        time.sleep(8)
        #f=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        f=['Product Category:Camcorder', 'Revenue:$154,465,702.24', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar', f, "Step 22.2: verify output")
        expected_xval_list=['Camcorder', 'Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M','250M','300M','350M']          
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 22.2: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 22.3c: Verify first bar color")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", 'Product Category', "Step 22.3d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", 'Revenue', "Step 22.3d(ii) Verify Y-Axis Title")
        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2109014_Actual_step22', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 23: Close the output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        
        """
        Step 24: Click "Save" in the toolbar > Type C2109014 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)


if __name__ == '__main__':
    unittest.main()
            
            
            
    