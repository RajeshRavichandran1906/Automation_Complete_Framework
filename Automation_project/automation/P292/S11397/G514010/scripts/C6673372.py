'''
Created on Spetember 10, 2018
@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6673372
'''
import unittest
import time
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon

class C6673372_TestClass(BaseTestCase):
    
    def test_C6673372(self):
        """
            Creating test case variables and instantiating required objects
        """
        Test_Case_ID = 'C6673372'
        util_obj = utillity.UtillityMethods(self.driver)
        metadata_obj = visualization_metadata.Visualization_Metadata(self.driver)
        resultarea_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbon_obj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visual = Visualization(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        chart_css = "#MAINTABLE_wbody1"
        
        """
        Step01: Launch the IA API with wf_retail_lite in Visualization mode:
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=idis&master=baseapp/wf_retail_lite
        """
        util_obj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        riser_element=VisualizationResultareaLocators.__dict__['default_riser']
        resultarea_obj._validate_page(riser_element)
        
        """
        Step02: Click "Change" in the Home Tab > Select "Scatter" chart type
        """
        ribbon_obj.change_chart_type('scatter')
        util_obj.synchronize_with_number_of_element("#TableChart_1 [class^='riser']", 17, 30)
        
        """
        Step03: Double-click "Cost of Goods" and "Product,Category"
        """
        metadata_obj.datatree_field_click("Cost of Goods", 2, 1)
        util_obj.synchronize_with_visble_text("#TableChart_1 [class='yaxis-title']", 'Cost of Goods', 20)
        metadata_obj.datatree_field_click("Product,Category", 2, 1)
        util_obj.synchronize_with_number_of_element("#TableChart_1 [class*='riser']", 7, 35)
        
        """
        Step04: Drag and drop "Customer,Business,Region" into the Columns bucket
        """
        metadata_obj.drag_drop_data_tree_items_to_query_tree("Customer,Business,Region", 1, 'Columns', 0)
        
        """
        Step05: Hover over point for "Media Player" in 'North America' region > Verify pop up menu with "Drill down to" sub menu.
        """
        parent_css="#MAINTABLE_wbody1 text[class*='colLabel']"
        resultarea_obj.wait_for_property(parent_css, 4, expire_time=30)
        bar=['Customer Business Region:North America', 'Cost of Goods:$79,074,473.00', 'Product Category:Media Player', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visual.verify_tooltip("riser!s0!g3!mmarker!r0!c1", bar, "Step 05: Verify bar value")
        
        """
        Step06: Select "Drill down to" > Verify options > "Customer Business Sub Region" and "Product Subcategory"
        """
        core_utils.python_move_to_element(self.driver.find_element_by_css_selector(chart_css), element_location='top_left')
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g3!mmarker!r0!c1']")
        util_obj.click_on_screen(parent_elem, 'left',mouse_duration=2.5)
        resultarea_obj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g3!mmarker!r0!c1",'Drill down to->Customer Business Sub Region',verify_menu1=['Customer Business Sub Region', 'Product Subcategory'],msg="Step06: Verify Drill down to menu")
        time.sleep(5)
        
        """
        Step07: Select "Customer Business Sub Region"
        """
        visual.select_tooltip("riser!s0!g3!mmarker!r0!c1", "Drill down to->Customer Business Sub Region")
        
        """
        Step08: Verify Preview and field "Customer Business Sub Region" in the Columns bucket (Query pane)
        """
        parent_css="#MAINTABLE_wbody1 text[class*='colLabel']"
        resultarea_obj.wait_for_property(parent_css, 8)
        metadata_obj.verify_query_pane_field('Columns', 'Customer,Business,Sub Region', 1, "Step08a: Verify Customer,Business,Sub Region in Columns")
        metadata_obj.verify_filter_pane_field('BUSINESS_REGION and PRODUCT_CATEGORY', 1, "Step08b: Verify Filter Pane")
        resultarea_obj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step08b: Verify Y-Axis Title")
        expected_label=['Canada', 'East', 'Mexico', 'Midwest', 'Northeast', 'South', 'Southeast', 'West']
        resultarea_obj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns', 'Customer Business Sub Region', expected_label, "Step08c: Verify column header and labels")
        expected_xval_list=[]
        expected_yval_list=['0', '6M', '12M', '18M']
        resultarea_obj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step08d:Verify XY labels")
        resultarea_obj.verify_number_of_circle('MAINTABLE_wbody1', 8, 9, 'Step 08e: Verify number of Circle displayed')
       
        """
        Step09: Right click filter in the Filter pane > Verify only "Delete" option is available
        """
        metadata_obj.filter_tree_field_click('BUSINESS_REGION and PRODUCT_CATEGORY', 1, 1)
        util_obj.select_or_verify_bipop_menu(verify='true',expected_popup_list=['Delete'],msg='Step09: Verify popup menu')   
        
        """
        Step10: Click Run
        """
        ribbon_obj.select_top_toolbar_item('toolbar_run')
        util_obj.switch_to_window(1)
        time.sleep(15)
        
        """
        Step11: Hover over point for "East" Sub Region > Verify menu with "Drill up to Customer Business Region" and "Drill down to" sub menu
        """
        bar=['Customer Business Sub Region:East', 'Cost of Goods:$11,455,431.00', 'Product Category:Media Player', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Business Region', 'Drill down to']
        visual.verify_tooltip("riser!s0!g0!mmarker!r0!c1", bar, "Step11: Verify bar value")
        
        """
        Step12: Select "Drill down to" sub menu > Verify options for "Customer Country" and "Product Subcategory"
        """
        core_utils.python_move_to_element(self.driver.find_element_by_css_selector(parent_css), element_location='top_left')
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mmarker!r0!c1']")
        util_obj.click_on_screen(parent_elem, 'left',mouse_duration=2.5)
        resultarea_obj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c1",'Drill down to->Customer Country',verify_menu1=['Customer Country', 'Product Subcategory'],msg="Step12: Verify Drill down to menu")
        
        """
        Step13: Select Drill down to > Customer Country"
        """
        visual.select_tooltip("riser!s0!g0!mmarker!r0!c1", "Drill down to->Customer Country")
        
        """
        Step14: Verify output
        """
        parent_css="#MAINTABLE_wbody1 text[class*='colLabel']"
        resultarea_obj.wait_for_property(parent_css, 1)
        resultarea_obj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step14a: Verify Y-Axis Title")
        expected_label=['United States']
        resultarea_obj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns', 'Customer Country', expected_label, "Step14b: Verify column header and labels")
        expected_xval_list=[]
        expected_yval_list=['0', '3.8M', '7.5M', '11.3M']
        resultarea_obj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step14c: Verify XY labels")
        resultarea_obj.verify_number_of_circle('MAINTABLE_wbody1', 1, 2, 'Step14d: Verify number of Circle displayed')
        
        """
        Step15: Hover over point > Verify pop up menu and sub menu options
        """
        bar=['Customer Country:United States', 'Cost of Goods:$11,455,431.00', 'Product Category:Media Player', 'Remove Filter', 'Drill up to Customer Business Sub Region', 'Drill down to']
        visual.verify_tooltip("riser!s0!g0!mmarker!r0!c0", bar, "Step15a: Verify bar value")
        
        """
        step16: Close the output window
        """
        self.driver.close()
        util_obj.switch_to_window(0)
        
        """
        Step17: Save as "C2158150" > Click Save
        """
        ribbon_obj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        util_obj.ibfs_save_as(Test_Case_ID)
        
        """
        Step18: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        util_obj.infoassist_api_logout()
        
        """
        Step19: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        util_obj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        
        """
        step20:Verify Preview
        """
        parent_css="#MAINTABLE_wbody1 text[class*='colLabel']"
        resultarea_obj.wait_for_property(parent_css, 8)
        metadata_obj.verify_query_pane_field('Columns', 'Customer,Business,Sub Region', 1, "Step20a: Verify Customer,Business,Sub Region in Columns")
        metadata_obj.verify_filter_pane_field('BUSINESS_REGION and PRODUCT_CATEGORY', 1, "Step20b: Verify Filter Pane")
        resultarea_obj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step20c: Verify Y-Axis Title")
        expected_label=['Canada', 'East', 'Mexico', 'Midwest', 'Northeast', 'South', 'Southeast', 'West']
        resultarea_obj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns', 'Customer Business Sub Region', expected_label, "Step20d: Verify column header and labels")
        expected_xval_list=[]
        expected_yval_list=['0', '6M', '12M','18M']
        resultarea_obj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step20e:Verify XY labels")
        resultarea_obj.verify_number_of_circle('MAINTABLE_wbody1', 8, 9, 'Step20f: Verify number of Circle displayed')

if __name__ == '__main__':
    unittest.main()
