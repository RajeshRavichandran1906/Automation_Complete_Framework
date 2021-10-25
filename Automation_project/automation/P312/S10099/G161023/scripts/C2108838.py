
'''
Created on May09, 2016
@author: gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2107478
'''

__author__ = "Gobinath Thiyagarajan"
__copyright__ = "IBI"

import unittest
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from selenium.webdriver import ActionChains 
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class C2108838_TestClass(BaseTestCase):

    def test_C2108838(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2108838'

        """
        Step 01:
        Launch the IA API with wf_retail_lite
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
    
        """
        The signon screen will be displayed.
        Login as userid devuser (autodevuser01/02/03/04/05) and blank password
        """
        driver = self.driver #Driver reference object created
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        browser = utillobj.parseinitfile('browser')
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
  
        """
        Step 02: Double click Product,Category, Gross Profit
        """
        metaobj.datatree_field_click('Product,Category',2,1)
        metaobj.datatree_field_click('Gross Profit',2,1) 
        time.sleep(10)
        
        """
        Step 03 : Verify x, y  labels.
        """
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Category",'Step 03: Verify X title Product Category')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Gross Profit",'Step 03: Verify Y title Gross Profit')
        
        """
        Step 04:verify bar riser values
        """
        time.sleep(5)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        tooltip_value =['Product Category:Accessories', 'Gross Profit:$39,854,440.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']       
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', 'riser!s0!g0!mbar', tooltip_value, 'Step 04:verify bar riser values')
        expected_xval_list=['Accessories', 'Camcorder', 'Computer', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 04: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 04: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 04: Verify first bar color")
        time.sleep(8)             
        
        """
        Step 05: Lasso the first 3 risers > Exclude from Chart 
        """ 
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(@class,"riser!s0!g0!mbar")]')))
        action = ActionChains(driver)
        move1 = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        if browser=='Firefox':
            utillobj.click_type_using_pyautogui(move1, move=True)
        else:
            action.move_to_element_with_offset(move1,1,1).perform()
        time.sleep(8)
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g0!mbar!', target_tag='rect', target_riser='riser!s0!g2!mbar')
        time.sleep(3)
        resultobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        time.sleep(5)    

        """
        Step 06 :Verify query added to filter
        """
        parent_css="#qbFilterWindow #qbFilterBox img"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-label']"
        resultobj.wait_for_property(parent_css, 4)
        metaobj.verify_filter_pane_field("Product,Category",1, "Step 06 : Verify query added to filter")
 
        """
        Step 07: Edit the filter query
        """              
        metaobj.filter_tree_field_click('Product,Category',1,1,'Edit...')
         
        """
        Step 08 : Verify operator 'Not equal to' and Accessories, Camcorder and Computer values is checked.
        """
        time.sleep(15)            
        not_equal = driver.find_element_by_css_selector('#alphaFieldPanel #avAlphaOperatorComboBox').text
        if not_equal[:-2] == 'Not equal to':
            print('Step 08 :operator Not equal selected')
        else:
            print('Step 08: Operator not equal not selected ')
        item_list=["Accessories", "Camcorder", "Computers"]   
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', Ok_button='true')
        time.sleep(6)
         
        """
        Step 09:Verify preview does not display Accessories, Camcorder and Computer values
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Category",'Step 09: Verify X title Product Category')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Gross Profit",'Step 09: Verify Y title Gross Profit')
        x=['Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 09: Verify preview X Label')
        tooltip_value =['Product Category:Media Player', 'Gross Profit:$55,832,578.36', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']       
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', 'riser!s0!g0!mbar', tooltip_value, 'Step 09:verify bar riser values')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 09: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 09: Verify first bar color")
        time.sleep(8) 
         
        """
        Step 10: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(12)
        utillobj.switch_to_window(1)
        time.sleep(15)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        """
        Step 11 : Lasso the first 3 risers > Filter Chart
        """
        time.sleep(15)
        action = ActionChains(driver)
        move1 = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        if browser=='Firefox':
            utillobj.click_type_using_pyautogui(move1, move=True)
        else:
            action.move_to_element_with_offset(move1,1,1).perform()
        time.sleep(8)
        action = ActionChains(driver)
        raiser="#MAINTABLE_wbody1 [class*='riser!s0!g0!mbar']"
        move_riser = driver.find_element_by_css_selector(raiser)
        if browser=='Firefox':
            utillobj.click_type_using_pyautogui(move_riser)
        else:
            action.move_to_element(move_riser).perform()
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g0!mbar!', target_tag='rect', target_riser='riser!s0!g2!mbar')
        time.sleep(3)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        parent_css="#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-label']"
        resultobj.wait_for_property(parent_css, 4)
        
         
        """
        Step 12: Verify output.
        """ 
        time.sleep(5)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Category",'Step 12: Verify X title Product Category')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Gross Profit",'Step 12: Verify Y title Gross Profit')
        x=['Media Player', 'Stereo Systems', 'Televisions']
        y=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 12: Verify preview X Label')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 12: Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 3, 'Step 12.1: Verify number of risers displayed')
        time.sleep(5)
        tooltip_value = ['Product Category:Media Player', 'Gross Profit:$55,832,578.36', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill down to Product Subcategory']       
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', 'riser!s0!g0!mbar', tooltip_value, 'Step 12.2: Verify output.')        
        time.sleep(25)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2108838_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        """
        Step 13 : close the output window
        """
        self.driver.close()
        time.sleep(7)
        utillobj.switch_to_window(0)
        time.sleep(9)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 14 : Click "Save" in the toolbar > Type C2108838 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(6)
        

if __name__ == '__main__':
    unittest.main()