'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227723
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227725_TestClass(BaseTestCase):
    def test_C2227725(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227725'
        bar=['Product Category:Camcorder', 'MSRP:161,574,103.08', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar1=['Product Category:Stereo Systems', 'MSRP:304,825,764.06', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
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
        
        """    2. Select "Home" > "Visual" > "Change" (dropdown) > "Bar".    """
        ribbonobj.change_chart_type('bar')
        
        """    3. Double click "MSRP","Product,Category".    """
        metaobj.datatree_field_click("MSRP", 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(8)
        
        """    4. Verify the following chart is displayed.    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 4a(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'MSRP', "Step 4a(ii): Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 4a(iii): Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 4b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!", "lochmara", "Step 4c: Verify bar color")
        time.sleep(1)
        
        """    5. Verify hover (tooltip) is working properly.    """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar!", bar, "Step 5(i): Verify MSRP bar value")
        time.sleep(5)
        
        """    6. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(10) 
        
        """    7. Verify the following chart is displayed.    """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!", bar1, "Step 7(i): Verify MSRP bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 7a(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'MSRP', "Step 7a(ii): Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 7a(iii): Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 7b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g6!mbar!", "lochmara", "Step 7c: Verify bar color")
        time.sleep(1)
        
        """    8. Dismiss the "Run" window.    """
        time.sleep(5)
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """    9. Click "IA" > "Save" > "C2160065" > "Save".    """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    10. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """    11. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160065.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(20)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    12. Verify the following chart is displayed.    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 12a(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'MSRP', "Step 12a(ii): Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12a(iii): Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 12b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!", "lochmara", "Step 12c: Verify bar color")
        time.sleep(1)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(1)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar!", bar, "Step 12(i): Verify MSRP bar value")
        time.sleep(5)
        
        """    13. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
                
if __name__ == '__main__':
    unittest.main()

