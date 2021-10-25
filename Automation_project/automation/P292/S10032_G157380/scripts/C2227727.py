'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227727
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227727_TestClass(BaseTestCase):
    def test_C2227727(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227727'
        bar1=['Product Category:Camcorder', 'MSRP:161,574,103.08', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar2=['Product Category:Televisions', 'Revenue:$78,381,132.81', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar3=['Product Category:Accessories', 'MSRP:135,623,183.37', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar4=['Product Category:Media Player', 'Revenue:$246,073,059.36', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar5=['Product Category:Televisions', 'MSRP:82,016,823.33', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar6=['Product Category:Camcorder', 'Revenue:$154,465,702.24', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M','100M', '150M', '200M', '250M', '300M', '350M']
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
              
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """    2. Select "Home" > "Visual" > "Change" (dropdown) > "Line".    """
        ribbonobj.change_chart_type('line')
        
        """    3. Double click Product,Category".    """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(8)
        
        """    4. Double click "MSRP" and "Revenue".    """
        metaobj.datatree_field_click("MSRP", 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(8)
        
        """    5. Verify the following chart is displayed.    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 5:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['MSRP','Revenue'], "Step 5:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 5:a(iii):Verify XY labels")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mline!", "lochmara", "Step 5.b(i): Verify first bar color", attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mline!", "pale_green", "Step 5.b(ii): Verify first bar color", attribute_type='stroke')
        
        """    6. Verify hover (tooltip) is working properly.    """
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'bottom_middle')         
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g1!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g1!mmarker!", bar1, "Step 6(i): Verify MSRP line value", default_move=True)
        time.sleep(1)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s1!g5!mmarker']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s1!g5!mmarker!", bar2, "Step 6(ii): Verify Revenue line value", default_move=True)
        time.sleep(5)
        
        """    7. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(10) 
        
        """    8. Verify the following chart is displayed.    """
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'bottom_middle')         
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'start',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker!", bar3, "Step 8(i): Verify MSRP bar value", default_move=True)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s1!g3!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s1!g3!mmarker!", bar4, "Step 8(ii): Verify Revenue bar value", default_move=True)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 8:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['MSRP','Revenue'], "Step 8:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 8:a(iii):Verify XY labels")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mline!", "lochmara", "Step 8.b(i): Verify first bar color", attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mline!", "pale_green", "Step 8.b(ii): Verify first bar color", attribute_type='stroke')
        time.sleep(1)
        
        """    9. Dismiss the "Run" window.    """
        time.sleep(5)
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """    10. Click "IA" > "Save" > "C2160065" > "Save".    """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    11. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """    12. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160065.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(20)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    Verify the following chart is displayed.    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 12:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['MSRP','Revenue'], "Step 12:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12:a(iii):Verify XY labels")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mline!", "lochmara", "Step 12.b(i): Verify first bar color", attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mline!", "pale_green", "Step 12.b(ii): Verify first bar color", attribute_type='stroke')
        time.sleep(1)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(1)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'bottom_middle')         
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g5!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g5!mmarker!", bar5, "Step 12(i): Verify MSRP bar value", default_move=True)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s1!g1!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s1!g1!mmarker!", bar6, "Step 12(ii): Verify Revenue bar value", default_move=True)
        time.sleep(5)
        
        """    13. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
                
if __name__ == '__main__':
    unittest.main()

