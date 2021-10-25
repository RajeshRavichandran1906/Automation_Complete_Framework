'''
Created on May'27, 2016
@author: Kiruthika

Test Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2107484&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case Name: IA-4560:Filter Chart does Exclusion at run time if design time includes exclude
'''
import unittest
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea
from common.lib import utillity,core_utility
from common.wftools import visualization

class C2107484_TestClass(BaseTestCase):

    def test_C2107484(self):
       
        driver = self.driver #Driver reference object created
        
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2107484'
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        visual = visualization.Visualization(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        browser=utillobj.parseinitfile("browser")
        
        """
        Step 01: Launch the IA API with wf_retail_lite
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02: Double click "Product,Category", "Gross Profit".
        """
        visual.double_click_on_datetree_item('Product,Category', 1)
        parent_css="#queryTreeWindow"
        visual.wait_for_visible_text(parent_css, 'Product,Category')
        visual.double_click_on_datetree_item('Cost of Goods', 1)
        visual.wait_for_visible_text(parent_css, 'Cost of Goods')
        
        """
        Step 03: Verify x and y axis labels
        """
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        visual.wait_for_number_of_element(parent_css1, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        visual.wait_for_number_of_element(parent_css, 7)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 03.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 03.02: Verify Y-Axis Title")
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 03.03: Verify the total number of risers displayed on Run Chart')
        
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 03.04: X annd Y axis Labels -')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03.05: Verify first bar color")
        
        """
        Step 04: Hover over "Accessories" bar.
        Verify the tool tip:
        """
        tip4=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",tip4, "Step 04.01: verify the default tooltip values")
        
        """
        Step 05: Lasso the first 3 risers > 'Exclude from Chart'.
        """
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(@class,"riser!s0!g0!mbar")]')))
        source_element = self.driver.find_element_by_css_selector('#MAINTABLE_wbody1 [class="riser!s0!g0!mbar!"]')
        target_element = self.driver.find_element_by_css_selector('#MAINTABLE_wbody1 [class="riser!s0!g2!mbar!"]')
        visual.create_lasso(source_element, target_element, target_element_location='bottom_middle')
        visual.select_lasso_tooltip('Exclude from Chart')
        
        """
        Step 06: Verify query added to filter pane.
        """
        visual.wait_for_visible_text('#qbFilterBox', 'Product,Category')
        visual.verify_field_in_filterbox("Product,Category", 1, "Step 06.01")

        """
        Step 07:Verify output (3 bar risers (Accessories,Camcorder and Computers) should be removed).
        """
        time.sleep(8)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        xval_list=['Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', xval_list, yval_list, 'Step 07.01: ')
        time.sleep(5)
        tip7=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar',tip7,"Step 07.02: Verify Accessories not in Preview 1st bar")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 07.03: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 07.04: Verify Y-Axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 07.05: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.06: Verify first bar color")
                
        """
        Step 08: Click Run
        """
        visual.run_visualization_from_toptoolbar()
        core_utils.switch_to_new_window()
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        
        """
        Step 09: Lasso the first 3 risers > 'Filter Chart'.
        """
        source_element = self.driver.find_element_by_css_selector('#MAINTABLE_wbody1 [class="riser!s0!g0!mbar!"]')
        target_element = self.driver.find_element_by_css_selector('#MAINTABLE_wbody1 [class="riser!s0!g2!mbar!"]')
        visual.create_lasso(source_element, target_element, target_element_location='bottom_middle')
        visual.select_lasso_tooltip('Filter Chart')
        
        """
        Step 10: Verify output (3 bar risers (Media Player, Stereo Systems and Televisions) should be filtered).
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        move3 = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        if browser=='Firefox' :
            utillobj.click_type_using_pyautogui(move3,move=True)
        else :
            action = ActionChains(driver)
            action.move_to_element_with_offset(move3,1,1).perform()
        
        time.sleep(5)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Category",'Step 10.01: Verify X title Product Category')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Cost of Goods",'Step 10.02: Verify Y title Gross Profit')
        x=['Media Player', 'Stereo Systems', 'Televisions']
        y=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 10.03: Verify preview X Label')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 10.04: Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 3, 'Step 10.05: Verify number of risers displayed')
                
        """
        Step: close the output window
        """
        core_utils.switch_to_previous_window()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 11: Click "Save" in the toolbar > Type C2107484 > Click "Save" in the Save As dialog
        """        
        visual.save_visualization_from_top_toolbar(Test_Case_ID)
        
        """
        Step12 : Logout of the IA API using the following URL.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()