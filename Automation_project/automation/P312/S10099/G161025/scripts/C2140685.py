'''
Created on June27, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=147037&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2140685
TestCase Name : IA-4442:Vis: 'Filter Chart' after Remove filter does not have effect on the filter Prompt at runtime
'''
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators


class C2140685_TestClass(BaseTestCase):

    def test_C2140685(self):
        driver = self.driver
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2140685'
        """
        Step 01: Launch the IA API with wf_retail_lite (Folder - S8404 and Master - wf_retail_lite) and login as "autodevuser03"
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Double click "Revenue" and "Product,Category"
        """
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Product,Category',2,1)
        time.sleep(5)
        
        """
        Step 03: Verify label values
        """
        resultobj.verify_xaxis_title('MAINTABLE_wbody1_f', "Product Category",'Step 03: Verify X title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1_f', "Revenue",'Step 03a: Verify Y title')
        x=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 03b: X and Y axis Scales Values has changed or NOT')
        
        """
        Step 04: Verify bar riser values
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        a =['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar',a,"Step 04: Verify bar riser values")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 04: Verify bar color")
        
        """
        Step 05: verify query pane
        """
        time.sleep(5)
        metaobj.verify_query_pane_field('Horizontal Axis','Product,Category',1, "Step 05a: Verify query pane")
        metaobj.verify_query_pane_field('Vertical Axis', 'Revenue',1, "Step 05b: Verify query pane")
        
        """
        Step 06: Add "Product,Category" to Filter, accept default and click ok.
        """
        metaobj.datatree_field_click('Product,Category',1,1,'Filter')
        elem1=(By.CSS_SELECTOR, "#avFilterOkBtn")
        resultobj._validate_page(elem1)
        time.sleep(2)
        metaobj.create_visualization_filters('alpha')
        time.sleep(10)
        
        """
        Step 07: Verify query added to filter
        """
        metaobj.verify_filter_pane_field('Product,Category',1,"Step 07: Verify query added to filter")
        time.sleep(8)
        x=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        time.sleep(5)
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 07a: X and Y axis Scales Values has changed or NOT')
        time.sleep(5)
        a =['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', 'riser!s0!g0!mbar', a, "Step 07b: Verify filtered bar(Accessories)")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07b(i): Verify bar color")
        
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', True,verify_type=True,msg="Step 07c: Verify 'All' checked in filter prompt value")
        time.sleep(5)
        
        """
        Step 08: Click Run in the toolbar
        """
        elem1=(By.ID, 'applicationButton')
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        
        """
        Step 09:  Hover over on "Accessories" and click Filter Chart.
        """
        time.sleep(10)
        raiser="[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(10)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g0!mbar", 'Filter Chart')
        time.sleep(20)
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1)
        """
        Step 10: Verify filtered bar(Accessories) and prompt value
        """
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, "Step 10: Verify 1 raiser present after filter chart")
        x=['Accessories']
        y=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 10a: X and Y axis Scales Values has changed or NOT')
        time.sleep(10)
        a =['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Remove Filter', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', 'riser!s0!g0!mbar', a, "Step 10b: Verify filtered bar(Accessories)")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10b(i): Verify bar color")
        
        propertyobj.select_or_verify_show_prompt_item(1, 'Accessories', True,verify_type=True,msg="Step 10c: Verify 'Accessories' checked in filter prompt value")
        time.sleep(5)
        
        """
        Step 11: Hover over on "Accessories" and click Remove Filter
        """
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g0!mbar", 'Remove Filter')
        time.sleep(15)
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 7)
        
        """
        Step 12: Verify 'All' checked in filter prompt
        """
        x=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 12a: X annd Y axis Scales Values has changed or NOT')
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', True,verify_type=True,msg="Step 12b: Verify 'All' checked in filter prompt- ")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, "Step 12c: Verify 7 raisers present after fRemove Filter")
        
        """
        Step 13: Hover over on "Computers" and click Filter Chart
        """
        raiser="[class*='riser!s0!g2!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g2!mbar", 'Filter Chart')
        time.sleep(15)
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1)
        
        """
        Step 14: Verify filtered bar (Computers) and prompt value
        """
        x=['Computers']
        y=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 14a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, "Step 14b: Verify 1 raiser present after filter chart")
        time.sleep(5)
        a =['Product Category:Computers', 'Revenue:$103,316,482.12', 'Remove Filter', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', 'riser!s0!g0!mbar', a, "Step 14c: Verify filtered bar(Computers)")
        propertyobj.select_or_verify_show_prompt_item(1, 'Computers', True,verify_type=True,msg="Step 14d: Verify 'Computers' checked in filter prompt value")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 14e: Verify bar color")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2140685_Actual_step14', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 15: Close the output window.
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        
        """
        Step 16: Click "Save" in the toolbar > Type C2140685 > Click "Save" in the Save As dialog
        """
        elem1=(By.ID, 'applicationButton')
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
        Step 17: Logout of the IA API using the following URL.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
    
if __name__ == '__main__':
    unittest.main()