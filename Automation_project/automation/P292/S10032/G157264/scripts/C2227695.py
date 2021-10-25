'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227695
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon, define_compute
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver import ActionChains

class C2227695_TestClass(BaseTestCase):
    def test_C2227695(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227695'
        expected_field_value="WF_RETAIL_LITE.WF_RETAIL_SALES.COGS_US - WF_RETAIL_LITE.WF_RETAIL_SALES.GROSS_PROFIT_US "
        bar=['Product Category:Accessories', 'PROFITS:49,899,457.47', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar1=['Product Category:Televisions', 'PROFITS:44,721,085.19', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar2=['Product Category:Camcorder', 'Profits:55,268,011.76', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar3=['Product Category:Camcorder', 'PROFITS:55,268,011.76', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar4=['Product Category:Media Player', 'Profits:134,407,902.64', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar5=['Product Category:Media Player', 'PROFITS:134,407,902.64', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar6=['Product Category:Televisions', 'Profits:44,721,085.19', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '30M', '60M', '90M','120M', '150M']
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        calculate_obj=define_compute.Define_Compute(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
              
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """    2. Click Calculation > "Detail (Define)".    """
        ribbonobj.select_ribbon_item('Home','calculation',opt='Summary (Compute)')
        time.sleep(5)
        
        """    3. Set Field = "PROFITS".    """
        """    4. Double-click field "Cost of Goods".    """
        calculate_obj.enter_define_compute_parameter("PROFITS", "D12.2", "Cost of Goods", 1)
        time.sleep(5)
        
        """    5. Click minus ( - ) sign.    """
        calculate_obj.select_calculation_btns("minus")
        
        """    6. Double-click field "Gross Profit".    """
        data_field='Gross Profit'
        sf = self.driver.find_element_by_id("defineMetaData").find_element_by_id("metaDataSearchTxtFld")
        sf.click()
        time.sleep(2)
        sf.clear()
        sf.send_keys(data_field)
        time.sleep(2)
        xpath = "//div[starts-with(@id, 'defineMetaData')]//tr[*]/td[.='" + data_field + "']/img[2]"
        element1 = self.driver.find_element_by_xpath(xpath)
        try:
            element1.click()
        except ElementNotVisibleException:
            element2 = self.driver.find_element_by_xpath(xpath)
            element2.click()
        time.sleep(3)
        lastxpath = "//div[starts-with(@id, 'defineMetaData')]//tr[contains(@class, 'selected')]/td[.='" + data_field + "']//img[2]"
        newelement = self.driver.find_element_by_xpath(lastxpath)
        if utillobj.browser == 'Firefox':
            utillobj.click_on_screen(newelement, coordinate_type='middle', click_type=2)
        else:
            action = ActionChains(self.driver)
            action.double_click(newelement).perform()
            del action
        time.sleep(6)
        
        """    7. Verify the following COMPUTE has been created in the textbox.    """
        actual_field_value = self.driver.find_element_by_id("ftext").get_attribute("value")
        utillobj.asequal(expected_field_value, actual_field_value, "Step 07a: Verify the following COMPUTE has been created in the textbox.")
        
        """    8. Click "OK".    """
        calculate_obj.close_define_compute_dialog("ok")
        time.sleep(5)
        
        """    9. Verify "PROFITS" is displayed in the Query pane and the following chart is displayed.    """
        metaobj.verify_query_pane_field("Vertical Axis", "PROFITS", 1, "Step 9a: Verify 'PROFITS' is displayed in the Query pane")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'PROFITS', "Step 9b: Verify Y-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "lochmara", "Step 9c: Verify first bar color")
        
        """    10. Double click field "Product,Category".    """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(8)
        
        """    11. Verify the following chart is displayed.    """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar, "Step 11(i): Verify Profits bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step11a(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'PROFITS', "Step 11a(ii): Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11a(iii): Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 11b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 11c: Verify first bar color")
        time.sleep(1)
        
        """    12. Click Calculation > "Detail (Define)".    """
        ribbonobj.select_ribbon_item('Home','calculation',opt='Detail (Define)')
        time.sleep(5)
        
        """    13. Create a new define as shown:
         Field = Profits
         Format = D12.2 (default)
         Field used = "Cost of Goods" - "Gross Profit"    """
        calculate_obj.enter_define_compute_parameter("Profits", "D12.2", "Cost of Goods", 1)
        time.sleep(5)
        calculate_obj.select_calculation_btns("minus")
        data_field='Gross Profit'
        sf = self.driver.find_element_by_id("defineMetaData").find_element_by_id("metaDataSearchTxtFld")
        sf.click()
        time.sleep(2)
        sf.clear()
        sf.send_keys(data_field)
        time.sleep(2)
        xpath = "//div[starts-with(@id, 'defineMetaData')]//tr[*]/td[.='" + data_field + "']/img[2]"
        element1 = self.driver.find_element_by_xpath(xpath)
        try:
            element1.click()
        except ElementNotVisibleException:
            element2 = self.driver.find_element_by_xpath(xpath)
            element2.click()
        time.sleep(3)
        lastxpath = "//div[starts-with(@id, 'defineMetaData')]//tr[contains(@class, 'selected')]/td[.='" + data_field + "']//img[2]"
        newelement = self.driver.find_element_by_xpath(lastxpath)
        if utillobj.browser == 'Firefox':
            utillobj.click_on_screen(newelement, coordinate_type='middle', click_type=2)
        else:
            action = ActionChains(self.driver)
            action.double_click(newelement).perform()
            del action
        time.sleep(6)
        
        """    14. Verify the following DEFINE has been created in the textbox.    """
        actual_field_value = self.driver.find_element_by_id("ftext").get_attribute("value")
        utillobj.asequal(expected_field_value, actual_field_value, "Step 14a: Verify the following DEFINE has been created in the textbox.")
        
        """    15. Click "OK".    """
        calculate_obj.close_define_compute_dialog("ok")
        time.sleep(5)
        
        """    16. Select "Home" > "Visual" > "Change" (dropdown) > Bar.    """
        ribbonobj.change_chart_type('bar')
        
        """    17. Double click "Profits" (from Measures).    """
        metaobj.datatree_field_click("Profits", 2, 1)
        time.sleep(8)
        
        """    18. Verify following chart is displayed.    """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g5!mbar!", bar1, "Step 18(i): Verify PROFITS bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g1!mbar!", bar2, "Step 18(ii): Verify Profit bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step18:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['PROFITS','Profits'], "Step 18:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 18:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 18.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 18.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "pale_green", "Step 18.c(ii): Verify first bar color")
        time.sleep(1)
        
        """    19. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(10) 
        
        """    20. Verify output is correct..    """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar!", bar3, "Step 20(i): Verify PROFITS bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g3!mbar!", bar4, "Step 20(ii): Verify Profit bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step20:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['PROFITS','Profits'], "Step 20:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 20:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 20.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g6!mbar!", "lochmara", "Step 20.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g5!mbar!", "pale_green", "Step 20.c(ii): Verify first bar color")
        time.sleep(5)
        
        """    21. Close the output window.    """
        time.sleep(5)
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """    22. Click on "IA" > Select "Save As"    """
        """    23. Save fex as "C2227695" > Click "Save"    """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    24. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """    25. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227695.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(20)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    26. Verify Computed field (PROFITS) is displayed in the Query pane.    """
        metaobj.verify_query_pane_field("Vertical Axis", "PROFITS", 1, "Step 26a: Verify 'PROFITS' is displayed in the Query pane")
        
        """    27. Verify chart    """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!", bar5, "Step 27(i): Verify PROFITS bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g5!mbar!", bar6, "Step 27(ii): Verify Profits bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 27:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['PROFITS','Profits'], "Step 27:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 27:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 27.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!", "lochmara", "Step 27.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g4!mbar!", "pale_green", "Step 27.c(ii): Verify first bar color")
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step27', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    28. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """     
        
if __name__ == '__main__':
    unittest.main()

