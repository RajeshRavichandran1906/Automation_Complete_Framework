'''
Created on May 15, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227612
TestCase Name = Lasso Filter using Scatter chart type
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class C2227612_TestClass(BaseTestCase):

    def test_C2227612(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227612'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
          
        """
        Step 02: Click "Change" in the Home Tab > Select "Scatter" chart type
        """
        ribbonobj.change_chart_type("scatter")
         
        """
        Step 03: Double-click "Cost of Goods " and "Product,Category"
        """
        time.sleep(5)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(4)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
         
        """
        Step 04: Drag and drop "Customer,Business,Region" into the Columns bucket
        """
        time.sleep(4)
        metaobj.drag_drop_data_tree_items_to_query_tree('Customer,Business,Region', 1, 'Columns', 0)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 4)
         
        """
        Step 05: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(5)
        resultobj.verify_number_of_circle("MAINTABLE_wbody1", 1, 29, 'Step 05a: Verify number of Circle displayed')
        expected_header='Customer Business Region'
        expected_label=['EMEA', 'North America', 'Oceania', 'South America']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns',expected_header,expected_label,"Step 05:")
        yaxis_value="Cost of Goods"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step05:d(ii) Verify Y-Axis Title")
        time.sleep(2)
         
        """
        Step 06:  Lasso the top 7 points for EMEA and North America, as displayed in the images
        Step 07:  Select "Filter Chart"
        """
        time.sleep(6)
        raiser="#MAINTABLE_wbody1 [class*='riser!s0!g4!mmarker!r0!c0!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        browser = utillobj.parseinitfile('browser')
        move_riser = driver.find_element_by_css_selector(raiser)
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move_riser)
        else:
            action = ActionChains(driver)
            action.move_to_element(move_riser).perform()
        resultobj.create_lasso('MAINTABLE_wbody1','circle', 'riser!s0!g4!mmarker!r0!c0!', target_tag='circle', target_riser='riser!s0!g1!mmarker!r0!c1!')
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        
        """
        Step 08: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(3)
        metaobj.verify_filter_pane_field('BUSINESS_REGION and PRODUCT_CATEGORY',1,"Step08.a:")
        time.sleep(5)
        resultobj.verify_number_of_circle("MAINTABLE_wbody1", 1, 8, 'Step 08a: Verify number of Circle displayed')
        expected_header='Customer Business Region'
        expected_label=['EMEA', 'North America']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns',expected_header,expected_label,"Step 08:")
        yaxis_value="Cost of Goods"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step08:d(ii) Verify Y-Axis Title")
        time.sleep(2)
        """
        Step09: Click Run > Verify output
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        chart_type_css="circle[class*='riser!s0!g3!mmarker!r0!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        resultobj.verify_number_of_circle("MAINTABLE_wbody1", 1, 8, 'Step 09a: Verify number of Circle displayed')
        expected_header='Customer Business Region'
        expected_label=['EMEA', 'North America']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns',expected_header,expected_label,"Step 09:")
        yaxis_value="Cost of Goods"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step09:d(ii) Verify Y-Axis Title")
        time.sleep(5)
        
        """
        Step 10:  Lasso the top 4 points > select "Filter Chart" from pop menu
        """
        action1 = ActionChains(self.driver)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser = utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move1, move=True)
        else:
            action1.move_to_element_with_offset(move1,1,1).perform()
        raiser="#MAINTABLE_wbody1 [class*='riser!s0!g3!mmarker!r0!c0!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        browser = utillobj.parseinitfile('browser')
        move_riser = driver.find_element_by_css_selector(raiser)
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move_riser)
        else:
            action = ActionChains(driver)
            action.move_to_element(move_riser).perform()
        time.sleep(2)
        resultobj.create_lasso('MAINTABLE_wbody1','circle', 'riser!s0!g3!mmarker!r0!c0!', target_tag='circle', target_riser='riser!s0!g1!mmarker!r0!c1!')
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
         
        """
        Step 11: Verify output
        """
        chart_type_css="circle[class*='riser!s0!g1!mmarker!r0!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(5)
        resultobj.verify_number_of_circle("MAINTABLE_wbody1", 1, 5, 'Step 11a: Verify number of Circle displayed')
        expected_header='Customer Business Region'
        expected_label=['EMEA', 'North America']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns',expected_header,expected_label,"Step 11:")
        yaxis_value="Cost of Goods"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step11:d(ii) Verify Y-Axis Title")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227612_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 12: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 13: Click "Save" > Save as "C2166452" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
         
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step 15: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 16: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="circle[class*='riser!s0!g3!mmarker!r0!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(3)
        metaobj.verify_filter_pane_field('BUSINESS_REGION and PRODUCT_CATEGORY',1,"Step16.a:")
        time.sleep(5)
        resultobj.verify_number_of_circle("MAINTABLE_wbody1", 1, 8, 'Step 16a: Verify number of Circle displayed')
        expected_header='Customer Business Region'
        expected_label=['EMEA', 'North America']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns',expected_header,expected_label,"Step 16:")
        yaxis_value="Cost of Goods"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step16:d(ii) Verify Y-Axis Title")
        time.sleep(5)
        
        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()  
        