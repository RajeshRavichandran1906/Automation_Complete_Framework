'''
Created on 22-Mar-2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227635
TestCase Name = Alphanumeric Filter format A40V
'''
import unittest,time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties, core_metadata

class C2227635_TestClass(BaseTestCase):

    def test_C2227635(self):

        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227635'
        
        """
        CLASS & OBJECTS
        """
        visualization = Visualization(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_meta = core_metadata.CoreMetaData(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
                
        """
        TESTCASE CSS
        """
        qwery_tree_css = "#queryTreeWindow"
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        time.sleep(5)
        
        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        visualization.double_click_on_datetree_item("Cost of Goods", 1)
        visualization.wait_for_visible_text(qwery_tree_css, "Cost of Goods")
        
        visualization.double_click_on_datetree_item("Product,Category", 1)
        visualization.wait_for_visible_text(qwery_tree_css, "Product,Category")
  
        """
        Step 04: Drag and drop "Product,Category" to the Filter pane
        """'Product,Category'
        core_meta.collapse_data_field_section('Filters and Variables')
        metaobj.drag_drop_data_tree_items_to_filter('Product,Category', 1)
        visualization.wait_for_visible_text("#avFilterCancelBtn", "Cancel")
        
        """
        Step 05 :Verify Filter dialog
        Step 06: Click OK
        """
        item_list=['[All]', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', Ok_button=True)
        time.sleep(5)
        
        """
        Step 07: Verify Filter appears in the Filter pane
        """
        metaobj.verify_filter_pane_field('Product,Category',1,"Step 07.01: Verify 'Product Category' appears in filter pane")
        
        """
        Step08: Verify Filter Prompt is displayed on preview canvas
        """
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type="true", msg="Step 08.01: Verify [All] is checked in filter prompt")
        
        """
        Step09: Click Run
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        visualization.switch_to_new_window()
        visualization.wait_for_visible_text("#MAINTABLE_wbody1_fmg", "Accessories")
        
        """
        Step10: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(15)

        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 10.01: Verify the total number of risers displayed on Run Chart')
        x_val_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_val_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 10.02: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 10.03: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 10.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 10.05: Verify Y-Axis Title")
        
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type="true", msg="Step 10.06: Verify [All] is checked in filter prompt")        
        time.sleep(5)
        
        """
        Step11: Close output window
        Step12: Click Save in the toolbar
        Step13: Click Save in the toolbar > Save as "C2227635" > Click Save
        Step14: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visualization.switch_to_previous_window()
        visualization.wait_for_visible_text("#MAINTABLE_wbody1_fmg", "Accessories")
        ribbonobj.select_top_toolbar_item('toolbar_save')
        visualization.wait_for_visible_text('#IbfsOpenFileDialog7_btnCancel', "Cancel")
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
        Step 15: Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227635.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1', mrid='mrid', mrpass='mrpass')
        visualization.wait_for_visible_text("#MAINTABLE_wbody1_fmg", "Accessories")
        
        """
        Step16: Verify Canvas
        """
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(5)
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 16.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 16.02: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 16.03: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 16.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 16.05: Verify Y-Axis Title")  
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type="true",msg="Step 16.06: Verify [All] is checked in filter prompt")        
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()