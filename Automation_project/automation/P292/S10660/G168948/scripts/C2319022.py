'''
Created on Oct 6, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2319022
TestCase Name = Home Tab - Edit multiple Compute fields
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, define_compute
from common.lib import utillity, core_utility
import pyautogui

class C2319022_TestClass(BaseTestCase):
    
    def test_C2319022(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2319022'
        expected_field_value='"Cost of Goods" + 1000'
        bar3=['Product Category:Accessories', 'NEWCOST:89,754,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '100M', '200M', '300M','400M', '500M', '600M']
        
        """
            CLASS & OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        calculate_obj=define_compute.Define_Compute(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        define = define_compute.DefineCompute(self.driver)
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """ 
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']", metaobj.chart_long_timesleep)
         
        """    2. Double click "Product,Category".    """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, ribbonobj.home_page_long_timesleep)
 
        """    3. Select Calculation -> Compute in the Home Tab    """
        ribbonobj.select_visualization_ribbon_item('Home', 'calculation->Summary (Compute)')
        utillobj.synchronize_with_number_of_element("#fldCreatorOkBtn", 1, ribbonobj.home_page_long_timesleep)
         
        """    4. Double-click "Cost of Goods" under Sales, Measures    """
        calculate_obj.enter_define_compute_parameter("Compute_1", "D12.2", "Cost of Goods", 1)
         
        """    5. Click OK to create Compute    """
        define.click_ok_button()
        utillobj.synchronize_until_element_disappear("#fldCreatorOkBtn", metaobj.chart_long_timesleep)
         
        """    6. Select Calculation -> Compute    """
        ribbonobj.select_visualization_ribbon_item('Home', 'calculation->Summary (Compute)')
        utillobj.synchronize_with_number_of_element("#fldCreatorOkBtn", 1, ribbonobj.home_page_long_timesleep)
         
        """    7. Double-click "Revenue" under Sales, Measures    """
        calculate_obj.enter_define_compute_parameter("Compute_2", "D12.2", "Revenue", 1)
         
        """    8. Click OK to create Compute    """   
        define.click_ok_button()
        utillobj.synchronize_until_element_disappear("#fldCreatorOkBtn", metaobj.chart_long_timesleep)
         
        """    9. Right-click "Compute_1" in the Query Pane -> Select "Edit Compute"    """
        """    10. Change name to NEWCOST, click OK    """
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 14, ribbonobj.home_page_long_timesleep)
        metaobj.querytree_field_click("Compute_1", 1, 1, "Edit Compute")
        utillobj.synchronize_with_number_of_element("#fldCreatorOkBtn", 1, ribbonobj.home_page_long_timesleep) 
        define.enter_values_in_field_textbox('NEWCOST')
        define.click_ok_button()
        utillobj.synchronize_until_element_disappear("#fldCreatorOkBtn", metaobj.chart_long_timesleep)
         
        """    11. Verify Query Pane is updated    """
        metaobj.verify_query_pane_field('Vertical Axis', 'NEWCOST', 1, "Step 11.00: Verify Compute_1 is updated as NEWCOST in Query pane")
         
        """    12. Click "Save" > save as "C2319022" > Click "Save"    """
        ribbonobj.select_visualization_application_menu_item('save_as')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", metaobj.chart_long_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
         
        """    13. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
         
        """    14. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2250722.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10660_visual_1', mrid='mrid', mrpass='mrpass')
 
        """    15. Right-click "Compute_2" in the Query Pane -> Select "Edit Compute"    """
        """    16. Rename to NEWREV, click ok    """
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 14, ribbonobj.chart_long_timesleep)
        metaobj.querytree_field_click("Compute_2", 1, 1, "Edit Compute")
        utillobj.synchronize_with_number_of_element("#fldCreatorOkBtn", 1, ribbonobj.home_page_long_timesleep) 
        define.enter_values_in_field_textbox('NEWREV')
        define.click_ok_button()
        utillobj.synchronize_until_element_disappear("#fldCreatorOkBtn", metaobj.chart_long_timesleep)
         
        """    17. Right-click NEWCOST in the Query Pane -> "Edit Compute"    """
        metaobj.querytree_field_click("NEWCOST", 1, 1, "Edit Compute")
        utillobj.synchronize_with_number_of_element("#fldCreatorOkBtn", 1, ribbonobj.home_page_long_timesleep)
         
        """    18. Add + 1000 to the Compute expression, click OK    """
        define.click_on_text_area()
        pyautogui.hotkey("end")
        time.sleep(1) 
        calculate_obj.select_calculation_btns("plus->one->zero->zero->zero")
        define.verify_text_area_expression(expected_field_value, '18.00')
        define.click_ok_button()
        utillobj.synchronize_until_element_disappear("#fldCreatorOkBtn", metaobj.chart_long_timesleep)
         
        """    19. Verify Query Pane    """
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 14, ribbonobj.home_page_long_timesleep)
        metaobj.verify_query_pane_field("Vertical Axis", "NEWCOST", 1, "Step 19.00: Verify 'NEWCOST' is displayed in Vertical Axis in the Query pane")
        metaobj.verify_query_pane_field("Vertical Axis", "NEWREV", 2, "Step 19.01: Verify 'NEWREV' is displayed in Vertical Axis in the Query pane")
        metaobj.verify_query_pane_field("Horizontal Axis", "Product,Category", 1, "Step 19.02: Verify 'Product,Cateory' is displayed in Horizontal Axis in the Query pane")
         
        """    20. Verify Preview    """
        time.sleep(5)        
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 20.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['NEWCOST','NEWREV'], "Step 20.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 20.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 20.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 20.05: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "pale_green", "Step 20.06: Verify first bar color")
        time.sleep(1)
         
        """    21. Click Run> Verify output    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utils.switch_to_new_window() 
        utillobj.synchronize_with_number_of_element('#MAINTABLE_wbody1 [class*="riser!s0!g0!mbar!"]', 1, ribbonobj.home_page_long_timesleep)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar3, "Step 21.00: Verify PROFITS bar value")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 21.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['NEWCOST','NEWREV'], "Step 21.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 21.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 21.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g6!mbar!", "lochmara", "Step 21.05: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g5!mbar!", "pale_green", "Step 21.06: Verify first bar color")
        core_utils.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible('#applicationButton img', ribbonobj.home_page_long_timesleep)
        ribbonobj.select_visualization_application_menu_item('save')
        time.sleep(3)
        btn_css="div[id^='BiDialog']>div[class*='window-active'] div[class=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('OK')].click()
        utillobj.synchronize_until_element_disappear(btn_css, metaobj.chart_long_timesleep)
         
        """    22. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
         
        """    23. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2250722.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10660_visual_1',mrid='mrid',mrpass='mrpass')
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 14, ribbonobj.chart_long_timesleep)
        
        """    24. Verify Query pane and Preview    """ 
        metaobj.verify_query_pane_field("Vertical Axis", "NEWCOST", 1, "Step 24.00: Verify 'NEWCOST' is displayed in Vertical Axis in the Query pane")
        metaobj.verify_query_pane_field("Vertical Axis", "NEWREV", 2, "Step 24.01: Verify 'NEWREV' is displayed in Vertical Axis in the Query pane")
        metaobj.verify_query_pane_field("Horizontal Axis", "Product,Category", 1, "Step 24.02: Verify 'Product,Cateory' is displayed in Horizontal Axis in the Query pane")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 24.05: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['NEWCOST','NEWREV'], "Step 24.06: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 24.07:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 24.08: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "lochmara", "Step 24.09: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g5!mbar!", "pale_green", "Step 24.10: Verify first bar color")
        
        """    25. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """     
        
if __name__ == '__main__':
    unittest.main()