'''
Created on Oct 5, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2319021
TestCase Name = Home Tab - Compute
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, define_compute
from common.lib import utillity, core_utility
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver import ActionChains

class C2319021_TestClass(BaseTestCase):
    
    def test_C2319021(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2319021'
        
        expected_field_value='"Cost of Goods" - "Gross Profit"'
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '30M', '60M', '90M','120M', '150M']
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        calculate_obj=define_compute.Define_Compute(self.driver)
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']", metaobj.chart_long_timesleep)
        
        """    2. Click Calculation > "Detail (Define)".    """
        ribbonobj.select_ribbon_item('Home','calculation',opt='Summary (Compute)')
        utillobj.synchronize_until_element_is_visible("#fname", metaobj.chart_long_timesleep)
        
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
        actual_field_value = self.driver.find_element_by_id("ftext").get_attribute("value").strip()
        utillobj.asequal(expected_field_value, actual_field_value, "Step 07a: Verify the following COMPUTE has been created in the textbox.")
        
        """    8. Click "OK".    """
        calculate_obj.close_define_compute_dialog("ok")
        utillobj.synchronize_until_element_disappear("#fldCreatorOkBtn", metaobj.chart_long_timesleep)
        
        """    9. Verify "PROFITS" is displayed in the Query pane and the following chart is displayed.    """
        metaobj.verify_query_pane_field("Vertical Axis", "PROFITS", 1, "Step 9a: Verify 'PROFITS' is displayed in the Query pane")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'PROFITS', "Step 9b: Verify Y-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "lochmara", "Step 9c: Verify first bar color")
        
        """    10. Double click field "Product,Category".    """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, metaobj.chart_long_timesleep)
        
        """    11. Verify the following chart is displayed.    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step11a(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'PROFITS', "Step 11a(ii): Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11a(iii): Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 11b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 11c: Verify first bar color")
        
        """    12. Click Calculation > "Detail (Define)".    """
        ribbonobj.select_ribbon_item('Home','calculation',opt='Detail (Define)')
        utillobj.synchronize_until_element_is_visible("#fname", metaobj.chart_long_timesleep)
        
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
        actual_field_value = self.driver.find_element_by_id("ftext").get_attribute("value").strip()
        utillobj.asequal(expected_field_value, actual_field_value, "Step 14a: Verify the following DEFINE has been created in the textbox.")
        
        """    15. Click "OK".    """
        calculate_obj.close_define_compute_dialog("ok")
        utillobj.synchronize_until_element_disappear("#fldCreatorOkBtn", metaobj.chart_long_timesleep)
        
        """    16. Select "Home" > "Visual" > "Change" (dropdown) > Bar.    """
        ribbonobj.change_chart_type('bar')
        parent_css= "div[class*='bi-label dv-caption-label']"
        utillobj.synchronize_with_visble_text(parent_css, 'Bar1', metaobj.chart_long_timesleep)
        
        """    17. Double click "Profits" (from Measures).    """
        metaobj.datatree_field_click("Measure Groups->Profits", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 14, metaobj.chart_long_timesleep)
        
        """    18. Verify following chart is displayed.    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step18:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['PROFITS','Profits'], "Step 18:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 18:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 18.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 18.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "pale_green", "Step 18.c(ii): Verify first bar color")
        time.sleep(1)
        
        """    19. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window()
        utillobj.synchronize_until_element_is_visible("#MAINTABLE_wbody1 [class*='riser!s0!g3!mbar']", metaobj.chart_long_timesleep)
        
        """    20. Verify output is correct..    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step20:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['PROFITS','Profits'], "Step 20:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 20:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 20.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g6!mbar!", "lochmara", "Step 20.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g5!mbar!", "pale_green", "Step 20.c(ii): Verify first bar color")
        
        """    21. Close the output window.    """
        core_utilobj.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible("#applicationButton img", metaobj.chart_long_timesleep)
        
        """    22. Click on "IA" > Select "Save As"    """
        """    23. Save fex as "C2319021" > Click "Save"    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    24. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        
        """    25. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160105.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10660_visual_1',mrid='mrid',mrpass='mrpass')
        utillobj.synchronize_until_element_is_visible("#MAINTABLE_wbody1 [class*='riser!s0!g3!mbar']", metaobj.chart_long_timesleep)
        
        """    26. Verify Computed field (PROFITS) is displayed in the Query pane.    """
        metaobj.verify_query_pane_field("Vertical Axis", "PROFITS", 1, "Step 26a: Verify 'PROFITS' is displayed in the Query pane")
        
        """    27. Verify chart    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 27:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['PROFITS','Profits'], "Step 27:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 27:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 27.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!", "lochmara", "Step 27.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g4!mbar!", "pale_green", "Step 27.c(ii): Verify first bar color")
        
        """    28. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """     
        
if __name__ == '__main__':
    unittest.main()