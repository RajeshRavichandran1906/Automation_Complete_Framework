'''
Created on Sep 17, 2018

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6742316
TestCase Name = Home Tab - Define field
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import ia_metadata
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, define_compute
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import core_metadata
from common.wftools.visualization import Visualization

class C6742316_TestClass(BaseTestCase):
    
    def test_C6742316(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C6742316'
        expected_field_value='"Revenue" * - 1'
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['-400M', '-300M', '-200M', '-100M','0', '100M', '200M', '300M', '400M']
        
        """
            CLASS & OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        calculate_obj=define_compute.Define_Compute(self.driver)
        define = define_compute.DefineCompute(self.driver)
        coreobj = core_metadata.CoreMetaData(self.driver)
        visualization = Visualization(self.driver)
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """    2. Click Calculation > "Detail (Define)".    """
        ribbonobj.select_ribbon_item('Home','calculation',opt='Detail (Define)')
        time.sleep(5)
        
        """    3. Set Field = "NEG_REVENUE".    """
        """    4. Change Format to "D20.2".    """
        """    5. Double click field "REVENUE".    """
        calculate_obj.enter_define_compute_parameter("NEG_REVENUE", "D20.2", "Revenue", 1)
        time.sleep(5)
        
        """    6. Verify it got inserted into the textbox.    """
        actual_field_value = self.driver.find_element_by_id("ftext").get_attribute("value")
        utillobj.asequal(expected_field_value[:-5], actual_field_value, "Step 06.00: Verify the define field value")
        
        """    7. Add "* -1" in the textbox.    """
        calculate_obj.select_calculation_btns("mult->minus->one")
        
        """    8. Verify the entry is same as shown.    """
        actual_field_value = self.driver.find_element_by_id("ftext").get_attribute("value")
        utillobj.asequal(expected_field_value, actual_field_value, "Step 08.00: Verify the define field value")
        
        """    9. Click "OK".    """
        define.click_ok_button()
        time.sleep(5)
        
        """    10. Verify the define (NEG_REVENUE) has been added to the Data pane (Measures fields list).    """
        
        coreobj.expand_data_field_section('Sales')
        metaobj.verify_all_data_panel_fields(["NEG_REVENUE"], 'Step 10.00: Verify data panel fields', comparison_type='asin')
#         metaobj.verify_data_pane_field("Sales", "NEG_REVENUE", 15, "Step 10.00")
        
        """    11. Click Calculation > "Detail (Define)".    """
        ribbonobj.select_ribbon_item('Home','calculation',opt='Detail (Define)')
        time.sleep(5)
        
        """    12. Create a new define as shown:
         Field = DEFN_PROD
         Format = A40
         Field used = Product,Category    """
        calculate_obj.enter_define_compute_parameter("DEFN_PROD", "A40", "Product,Category", 1)
        time.sleep(5)
        
        """    13. Click "OK".    """
        define.click_ok_button()
        time.sleep(5)
        
        """    14. Verify "DEFN_PROD" has been added to the Data pane (Dimensions fields list).    """
        coreobj.expand_data_field_section('Product->Product')
        metaobj.verify_data_pane_field("Sales_Related", "DEFN_PROD", 6, "Step 14.00")
        
        """    15. Double click "NEG_REVENUE", "Revenue", "DEFN_PROD".    """
        visualization.double_click_on_datetree_item("Measure Groups->NEG_REVENUE", 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        visualization.wait_for_number_of_element(parent_css, 7, 180)
        visualization.double_click_on_datetree_item("Revenue", 1)
        riser_css = "#MAINTABLE_wbody1_f g[class=risers] rect[class^=riser]"
        visualization.wait_for_number_of_element(riser_css, 2, 120)
        visualization.double_click_on_datetree_item("Product->Product->DEFN_PROD", 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        visualization.wait_for_number_of_element(parent_css,9 , 100)
        
        """    16. Verify following chart is displayed.    """
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'DEFN_PROD', "Step 16.02: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['NEG_REVENUE','Revenue'], "Step 16.03: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16.04:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 16.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 16.06: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "pale_green", "Step 16.07: Verify first bar color")
        time.sleep(1)
        
        """    17. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        visualization.switch_to_new_window()
        time.sleep(15) 
        
        """    18. Verify output at Runtime is correct.    """
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'DEFN_PROD', "Step 18.02:  Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['NEG_REVENUE','Revenue'], "Step 18.03: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 18.04:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 18.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g6!mbar!", "lochmara", "Step 18.06: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g5!mbar!", "pale_green", "Step 18.07: Verify first bar color")
        time.sleep(5)
        
        """    19. Close the output window.    """
        visualization.switch_to_previous_window()
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """    20. Click "IA" > "Save" > Save As "C2160105".    """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save')
        visualization.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    21. Close IA from X in the tool's upper right corner.    """
        """    22. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """    23. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160105.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10660_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(20)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    24. Verify Define fields (NEG_REVENUE, DEFN_PROD) are displayed in the fields List.    """
        coreobj.expand_data_field_section('Sales')
        metaobj.verify_all_data_panel_fields(["NEG_REVENUE"], 'Step 24.00: Verify data panel fields', comparison_type='asin')
#         metaobj.verify_data_pane_field("Sales", "NEG_REVENUE", 15, "Step 24.00")
        coreobj.collapse_data_field_section('Sales')
        coreobj.expand_data_field_section('Product->Product')
        metaobj.verify_data_pane_field("Product", "DEFN_PROD", 5, "Step 24.01")
         
        """    25. Verify chart displayed on canvas is correct.    """
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'DEFN_PROD', "Step 25.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['NEG_REVENUE','Revenue'], "Step 25.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 25.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 25.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!", "lochmara", "Step 25.05: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g4!mbar!", "pale_green", "Step 25.06: Verify first bar color")
        time.sleep(5)
        
        """    26. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """     
        
if __name__ == '__main__':
    unittest.main()