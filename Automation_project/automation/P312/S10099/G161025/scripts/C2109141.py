'''
Created on June20, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=147037&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109141&group_by=cases:section_id&group_id=147037&group_order=asc
TestCase Name : IA-4037:"metadataField cannot be null" error in event.log
'''
import unittest
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from common.lib import take_screenshot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run, ia_run
from common.locators import visualization_metadata_locators, visualization_properties_locators, visualization_resultarea_locators
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators

class C2109141_TestClass(BaseTestCase):

    def test_C2109141(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2109141'
        """
        Step 01: Launch the IA API with wf_retail_lite (Folder - S8404 and Master - wf_retail_lite) and login as "autodevuser03"
        http://machine:port/ibi_apps/ia?tool=idis&master=retail_samples/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        iarun=ia_run.IA_Run(self.driver)
        """
        Step 02: Change to matrix chart
        """
        ribbonobj.change_chart_type('matrix_marker')
        """
        Step 03: Add Gross profit and Product Category
        """
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Gross Profit', 2, 1)
        time.sleep(5)
        
        
        """
        Step 04: Verify label values
        """
        utillobj._validate_page((By.CSS_SELECTOR,"text[class*='rowHeader-label"))
        row_header=self.driver.find_element_by_css_selector("text[class*='rowHeader-label']").text
        
        
        utillobj._validate_page((By.CSS_SELECTOR,"text[class*='sizeLegend-title']"))
        size_legend=self.driver.find_element_by_css_selector("text[class*='sizeLegend-title']").text
        
        utillity.UtillityMethods.asequal(self,row_header,'Product Category',"Step 04: Verify label row header values")
        utillity.UtillityMethods.asequal(self,size_legend,'Gross Profit',"Step 04: Verify label size legend values")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 1, 8, 'Step04: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0", "bar_blue", "Step04: Verify bar color")
        
        """
        Step 05: Verify riser values
        """
        time.sleep(5)
        a =['Product Category:Accessories', 'Gross Profit:$39,854,440.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mmarker!r0!c0', a, "Step 05: Verify riser values")
        """
        Step 06: verify query pane
        """
        metaobj.verify_query_pane_field('Rows', 'Product,Category', 1, "Step 06: Verify query pane")
        """
        Step 07: Click Run in the toolbar
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        """
        Step 08:  Lasso on Camcorder and computers and select filter chart
        """
        time.sleep(5)        
#         action = ActionChains(driver)
#         move = driver.find_element_by_css_selector("#orgdiv0")
#         action.move_to_element_with_offset(move,1,1).perform()
#         time.sleep(8)
        raiser="#MAINTABLE_wbody1 [class*='riser!s0!g0!mmarker!r1!c0']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        time.sleep(10)
        browser = utillobj.parseinitfile('browser')
        move_riser = driver.find_element_by_css_selector(raiser)
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move_riser)
        else:
            action = ActionChains(driver)
            action.move_to_element(move_riser).perform()
        resultobj.create_lasso('MAINTABLE_wbody1','circle', 'riser!s0!g0!mmarker!r1!c0', target_tag='circle', target_riser='riser!s0!g0!mmarker!r2!c0')
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        
        elem = "#MAINTABLE_wbody1 g.chartPanel circle[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        a =['Product Category:Camcorder', 'Gross Profit:$49,598,845.24', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mmarker!r0!c0', a, "Step 08: Verify riser values")
        row_header=self.driver.find_element_by_css_selector("text[class*='rowHeader-label']").text
        utillity.UtillityMethods.asequal(self,row_header,'Product Category',"Step 08: Verify label row header values")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 1, 3, 'Step08: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0", "bar_blue", "Step08: Verify bar color")
                
        move1 = driver.find_element_by_css_selector("#orgdiv0")
        if browser == 'Firefox':
            utillity.UtillityMethods.click_type_using_pyautogui(self, move1, move=True)
        else:
            action = ActionChains(driver)
            action.move_to_element_with_offset(move1,1,1).perform()
        time.sleep(20)
        ele=driver.find_element_by_css_selector("#orgdiv0")
        utillobj.take_screenshot(ele,'C2109141_Actual_step08', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(3)
        
        """
        Step 09: Click on the icon at bottom right corner and select show data
        """
        time.sleep(8)
        runobj.select_run_menu_option('MAINTABLE_menuContainer1',"show_report")
        ele=driver.find_element_by_css_selector("div[id*='orgdiv0']")
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(5)
        
        """
        Step 10: Verify Gross Profit and product category values
        """
        show_data=driver.find_elements_by_css_selector("#MAINTABLE_wbody2 table td span")
        actual_data=[]
        for data in show_data:
            actual_data.append(data.text)
        expected_data=['Product Category', 'Gross Profit', 'Camcorder', 'Computers']
        for data in expected_data:
            if data in actual_data:
                statey= True
            else:
                statey=False   
                break
        utillobj.asequal(statey, True,  "Step 10.a: Verify string grid values")
        actual_interger_data=[]
        actual_interger_data.append((actual_data[-3])[:-3])
        actual_interger_data.append((actual_data[-1])[:-3])
        expected_interger_data=['$49,598,845', '$33,508,818']
        utillobj.as_List_equal(expected_interger_data, actual_interger_data, 'Step 10.b: Verify Integer grid values')
#         iarun.create_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table", "C2109141_Ds01.xlsx")
#         iarun.verify_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table", "C2109141_Ds01.xlsx", "Step 10: Verify Gross Profit and product category values")
        
        """
        Step 11: Close the output window.
        """
        time.sleep(2)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 12: Click "Save" in the toolbar > Type C2109141 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        """
        Step 13: Logout of the IA API using the following URL.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()
