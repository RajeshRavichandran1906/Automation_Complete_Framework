'''
Created on Jun 10, 2016

@author: Sindhuja
'''
"""
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2107479
"""
import unittest,pyautogui,time
from common.lib import utillity 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon

class C2107479_TestClass(BaseTestCase):
    
    def test_C2107479(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2107479'
        
        """
            Class & Objects
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        
        """
            Step 01: Launch the IA API with mutualfunds http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/mutualfunds&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/mutual_funds','P141/S8357', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
            Step 02: Add volatility and Fund Category to the canvas
        """
        metaobj.datatree_field_click('Measures->Volatility (%)', 2, 1)
        metaobj.datatree_field_click('Dimensions->Mutual Funds->Funds->Fund Category', 2, 1)
        
        """
            Step 03: Vefiry field titles.
        """
        riser_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(riser_css, 7)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1_f', "Fund Category",'Step 03.01: Verify X title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1_f', "Volatility (%)",'Step 03.02: Verify Y title')
        time.sleep(5)
        ele = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser = utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillity.UtillityMethods.click_type_using_pyautogui(self, ele, move=True)
        else:
            action = ActionChains(driver)
            action.move_to_element_with_offset(ele,1,1).perform()
        time.sleep(5)
        tooltip_value = ['Fund Category:Balanced', 'Volatility (%):487.78', 'Filter Chart', 'Exclude from Chart', 'Drill up to Fund Type', 'Drill down to Fund Family']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar', tooltip_value, "Step 03.03: Verify tooltip value is correct in preview.")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03.04: Verify bar color")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 03.05: Verify the total number of risers displayed on Run Chart')
        x=['Balanced']
        y=['0', '100', '200', '300', '400', '500', '600', '700', '800']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 03.06: X annd Y axis Scales Values has changed ')
        
        """
            Step 04: Add Fund Name filed to filter panel and select 'DREYFUS 100% TREAS LONG' value and click ok.
        """
        metaobj.drag_drop_data_tree_items_to_filter('Dimensions->Mutual Funds->Funds->Fund Name', 0)
#         metaobj.datatree_field_click("Fund Name", 1, 1,"Filter")
        time.sleep(5)
#         l=['[All]','DREYFUS 100% TREAS LONG']
#         metaobj.create_visualization_filters('alpha',['Operator','Equal to'],['GridItems',l])
        l='DREYFUS 100% TREAS LONG'
        browser=utillity.UtillityMethods.parseinitfile(self,'browser')
        if browser == 'IE':
            parent_css1="#alphaFieldPanel #avAlphaOperatorComboBox div[id^='BiButton']"
            resultobj.wait_for_property(parent_css1, 1)
#             utillobj.select_combobox_item("#avAlphaOperatorComboBox", "Equal to")
            time.sleep(2)
            search_element = self.driver.find_element_by_css_selector("#avSearchBox > input")
            search_element.click()
            time.sleep(3)
            search_element.clear()
            time.sleep(3)
            pyautogui.typewrite('DREYFUS 100% TREAS LONG')
            time.sleep(20)
            metaobj.create_visualization_filters('alpha')
#             driver.find_element_by_id("avFilterOkBtn").click()
        else:
            metaobj.create_visualization_filters('alpha',['Operator','Equal to'],['SearchValues',l])
            time.sleep(15)
        """
            Step 05: Verify query added to filter pane.
        """
        metaobj.verify_filter_pane_field("Fund Name", 1, 'Step 05.01')
        
        """
            Step 06: Verify 'DREYFUS 100% TREAS LONG' value is selected in filter prompt.
        """
        propertyobj.select_or_verify_show_prompt_item(1, 'DREYFUS 100% TREAS LONG', True,verify_type=True,scroll_down= True, msg="Step 06.01: Verify 'DREYFUS 100% TREAS LONG' value is selected in filter prompt")
        time.sleep(5)
#         propertyobj.verification_filter_prompt_checkbox_values("Fund Name","DREYFUS 100% TREAS LONG", "Step 06: Verify 'DREYFUS 100% TREAS LONG' value is selected in filter prompt")
        """
            Step 07: Verify filtered value is correct in preview.
        """
        resultobj.wait_for_property(riser_css, 1)
        ele = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser = utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillity.UtillityMethods.click_type_using_pyautogui(self, ele, move=True)
        else:
            action = ActionChains(driver)
            action.move_to_element_with_offset(ele,1,1).perform()
        time.sleep(5)
        tooltip_value = ['Fund Category:Treasuries', 'Volatility (%):2.05', 'Drill up to Fund Type', 'Drill down to Fund Family']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar', tooltip_value, "Step 07.01: Verify filtered value is correct in preview.")
        time.sleep(8)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.02: Verify bar color")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 07.03: Verify the total number of risers displayed on Run Chart')
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Fund Category",'Step 07.04: Verify X title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Volatility (%)",'Step 07.05: Verify Y title')
        x=['Treasuries']
        y=['0', '0.4', '0.8', '1.2', '1.6', '2', '2.4']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 07.06: X annd Y axis Scales Values has changed ')
        time.sleep(5)
        
        """
            Step 08: Click "Save" in the toolbar > Type C2107479 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()