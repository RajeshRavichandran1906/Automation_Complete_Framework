'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227695
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, define_compute
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By
import pyautogui

class C2227696_TestClass(BaseTestCase):
    def test_C2227696(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227696'
        expected_field_value="WF_RETAIL_LITE.WF_RETAIL_SALES.COGS_US + 1000"
        bar1=['Product Category:Televisions', 'NEWCOST:61,552,109.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar2=['Product Category:Camcorder', 'NEWREV:154,465,702.24', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar3=['Product Category:Accessories', 'NEWCOST:89,754,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar4=['Product Category:Media Player', 'NEWREV:246,073,059.36', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '100M', '200M', '300M','400M', '500M', '600M']
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        calculate_obj=define_compute.Define_Compute(self.driver)
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        
        """    2. Double click "Product,Category".    """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(8)
        
        """    3. Select Calculation -> Compute in the Home Tab    """
        ribbonobj.select_ribbon_item('Home','calculation',opt='Summary (Compute)')
        time.sleep(5)
        
        """    4. Double-click "Cost of Goods" under Sales, Measures    """
        calculate_obj.enter_define_compute_parameter("Compute_1", "D12.2", "Cost of Goods", 1)
        time.sleep(5)
        
        """    5. Click OK to create Compute    """
        calculate_obj.close_define_compute_dialog("ok")
        time.sleep(5)
        
        """    6. Select Calculation -> Compute    """
        ribbonobj.select_ribbon_item('Home','calculation',opt='Summary (Compute)')
        time.sleep(5)
        
        """    7. Double-click "Revenue" under Sales, Measures    """
        calculate_obj.enter_define_compute_parameter("Compute_2", "D12.2", "Revenue", 1)
        time.sleep(5)
        
        """    8. Click OK to create Compute    """
        calculate_obj.close_define_compute_dialog("ok")
        time.sleep(5)
        
        """    9. Right-click "Compute_1" in the Query Pane -> Select "Edit Compute"    """
        """    10. Change name to NEWCOST, click OK    """
        metaobj.querytree_field_click("Compute_1", 1, 1, "Edit Compute")
        time.sleep(8)
        field_name = self.driver.find_element_by_id("fname")
        field_name.clear() 
        time.sleep(1)                                                    
        field_name.send_keys("NEWCOST")
        time.sleep(1) 
        calculate_obj.close_define_compute_dialog("ok")
        time.sleep(5)
        
        """    11. Verify Query Pane is updated    """
        metaobj.verify_query_pane_field('Vertical Axis', 'NEWCOST', 1, "Step08a: Verify Compute_1 is updated as NEWCOST in Query pane")
        
        """    12. Select Exit from ID menu > click Yes    """
        """    13. Name fex "C2160106" > click "Save"    """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    14. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """    15. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160106.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(20)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    16. Right-click "Compute_2" in the Query Pane -> Select "Edit Compute"    """
        """    17. Rename to NEWREV, click ok    """
        metaobj.querytree_field_click("Compute_2", 1, 1, "Edit Compute")
        time.sleep(8)
        field_name = self.driver.find_element_by_id("fname")
        field_name.clear() 
        time.sleep(1)                                                    
        field_name.send_keys("NEWREV")
        time.sleep(1) 
        calculate_obj.close_define_compute_dialog("ok")
        time.sleep(5)
        
        """    18. Right-click NEWCOST in the Query Pane -> "Edit Compute"    """
        metaobj.querytree_field_click("NEWCOST", 1, 1, "Edit Compute")
        time.sleep(8)
        
        """    19. Add + 1000 to the Compute expression, click OK    """
        driver.find_element_by_id("ftext").click()
        time.sleep(1) 
        pyautogui.hotkey("end")
        time.sleep(1) 
        calculate_obj.select_calculation_btns("plus->one->zero->zero->zero")
        time.sleep(1)
        actual_field_value = self.driver.find_element_by_id("ftext").get_attribute("value")
        utillobj.asequal(expected_field_value, actual_field_value, "Step 19a: Verify the COMPUTE 'NEWCOST' has been updatd with '+ 1000' in the textbox.")
        time.sleep(1)
        calculate_obj.close_define_compute_dialog("ok")
        time.sleep(5)
        
        """    20. Verify Query Pane    """
        metaobj.verify_query_pane_field("Vertical Axis", "NEWCOST", 1, "Step 20a: Verify 'NEWCOST' is displayed in Vertical Axis in the Query pane")
        metaobj.verify_query_pane_field("Vertical Axis", "NEWREV", 2, "Step 20b: Verify 'NEWREV' is displayed in Vertical Axis in the Query pane")
        metaobj.verify_query_pane_field("Horizontal Axis", "Product,Category", 1, "Step 20c: Verify 'Product,Cateory' is displayed in Horizontal Axis in the Query pane")
        
        """    21. Verify Canvas    """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g5!mbar!", bar1, "Step 21(i): Verify NEWCOST bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g1!mbar!", bar2, "Step 21(ii): Verify NEWREV bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 21:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['NEWCOST','NEWREV'], "Step 21:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 21:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 21.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 21.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "pale_green", "Step 21.c(ii): Verify first bar color")
        time.sleep(1)
        
        """    22. Click "Save"    """
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        btn_css="div[id^='BiDialog']>div[class*='window-active'] div[class=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('OK')].click()
        time.sleep(5)
        
        """    23. Click Run> Verify output    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(10) 
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar3, "Step 23(i): Verify PROFITS bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g3!mbar!", bar4, "Step 23(ii): Verify Profit bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step23:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['NEWCOST','NEWREV'], "Step 23:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 23:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 23.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g6!mbar!", "lochmara", "Step 23.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g5!mbar!", "pale_green", "Step 23.c(ii): Verify first bar color")
        time.sleep(5)
        
        """    24. Close the output window    """
        time.sleep(5)
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step24', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    25. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """     
        
if __name__ == '__main__':
    unittest.main()

