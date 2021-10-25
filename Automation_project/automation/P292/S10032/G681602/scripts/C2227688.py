'''
Created on Apr 4, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227688
Test case Name =  Filter pane context menu - Hide Prompt
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.lib import core_utility
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


class C2227688_TestClass(BaseTestCase):

    def test_C2227688(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227688'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        data_list = ["Cost of Goods,Local Currency", "Product,Category"] 
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(elem1, 1, resultobj.chart_long_timesleep)

        """
        Step 02: Double-click "Cost of Goods, Local Currency", located under Sales Measures
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        for item in data_list:
            metaobj.datatree_field_click(item,2,1)
            utillobj.synchronize_with_visble_text("#queryTreeColumn", item, metaobj.chart_medium_timesleep)
        
        """
        Step 04: Drag and drop "Product,Category" to the Filter pane
        Step 05: Click OK
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
        metaobj.create_visualization_filters('alpha')
        
        """
        Step 06: Drag and drop "Cost of Goods, Local Currency" to the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter('Cost of Goods,Local Currency', 1) 
        
        """
        Step 07: Verify Filter dialog
        Step 08: Click OK
        """

        utillobj.synchronize_with_number_of_element('#avFilterOkBtn', 1, metaobj.chart_medium_timesleep)
        operator_combo_elem = utillobj.validate_and_get_webdriver_object("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']", 'combo-element')
        elem = 'Range'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 07.a: Verify dialog')
        elem1=utillobj.validate_and_get_webdriver_object("#avfFromValue input", "input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(float(d['float_value']),10.12,"Step07.b: Verify range from value")
        elem1=utillobj.validate_and_get_webdriver_object("#avfToValue input", 'input')
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(float(d['float_value']),3620014.67,"Step07.c: Verify range to value")  
        metaobj.create_visualization_filters('numeric')
        
        """
        Step09: Edit "Cost of Goods, Local Currency" filter on canvas > Drag left slider handle to the right at value > 2830300.3
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        action1 = ActionChains(self.driver)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser=utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillobj.click_on_screen(move1, coordinate_type='bottom_middle', click_type=0)
            time.sleep(5)
            utillobj.click_type_using_pyautogui(move1)
            start_point=driver.find_elements_by_css_selector("#ar_Prompt_2 div[id^='slider_'] [class^='ui-slider-handle']")
            utillobj.click_on_screen(start_point[0], coordinate_type='middle', click_type=0)
        else:
            action1.move_to_element_with_offset(move1,1,1).perform()
        utillobj.synchronize_with_number_of_element("form[id^='slider']", 1, metaobj.chart_medium_timesleep)
        propertyobj.move_slider_measure('#ar_Prompt_2','min', 'right', 3, 'float') #2172012.85
        
        
        """
        Step10: Verify Canvas 
        """
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','min',2172012.85,'float',msg="Step10: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','max',3620014.67,'float',msg="Step10: Verify filter prompt range max values")
        utillobj.synchronize_with_number_of_element('#MAINTABLE_wbody1', 1, metaobj.chart_medium_timesleep)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step10.a:")
        metaobj.verify_filter_pane_field('Cost of Goods,Local Currency',2,"Step10.b:")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.c: Verify first bar color")
          
        """
        Step 11: Right click "Product,Category" filter in the Filter pane > Select "Hide Prompt"
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.change_prompt_options("1","Hide Prompt")
          
        """
        Step12: Verify Canvas 
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.synchronize_with_number_of_element("form[id^='sliderLOB']", 1, metaobj.chart_medium_timesleep)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','min',2172012.85,'float',msg="Step12: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','max',3620014.67,'float',msg="Step12: Verify filter prompt range max values")
        utillobj.synchronize_with_number_of_element('#MAINTABLE_wbody1', 1, metaobj.chart_medium_timesleep)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step12.a:")
        metaobj.verify_filter_pane_field('Cost of Goods,Local Currency',2,"Step12.b:")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 12:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 12:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 12.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 12.c: Verify first bar color")
           
        """
        Step 13: Right click "Cost of Goods, Local Currency" filter in the Filter pane > Select "Edit"
        """
        metaobj.filter_tree_field_click('Cost of Goods,Local Currency',1,1, 'Edit...')
          
        """
        Step 14: Verify Filter dialog
        Step 15: Uncheck "Show Prompt" > click OK
        """
        utillobj.synchronize_with_number_of_element('#avFilterOkBtn', 1, metaobj.chart_medium_timesleep)
        operator_combo_elem = utillobj.validate_and_get_webdriver_object("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']", 'operator combo')
        elem = 'Range'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 14.a: Verify dialog')
        elem1 = utillobj.validate_and_get_webdriver_object("#avfFromValue input", 'input')
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(float(d['float_value']),2172012.85,"Step14.b: Verify range from value")
        elem1=utillobj.validate_and_get_webdriver_object("#avfToValue input", "input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(float(d['float_value']),3620014.67,"Step14.c: Verify range to value")  
        metaobj.create_visualization_filters('numeric',['ShowPrompt'])
          
        """
        Step16: Verify Canvas 
        """
        try:
            if utillobj.validate_and_get_webdriver_object("div[id^='BoxLayoutFilterBox']", "filterbox").is_displayed():
                utillity.UtillityMethods.asequal(self, 'a', 'b', "Step 16: Verify Filter Prompts not removed from canvas")
        except (NoSuchElementException, AttributeError):
            utillity.UtillityMethods.asequal(self, 'a', 'a', "Step 16: Verify Filter Prompts are removed from canvas")
        utillobj.synchronize_with_number_of_element('#MAINTABLE_wbody1', 1, metaobj.chart_medium_timesleep)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step16.a:")
        metaobj.verify_filter_pane_field('Cost of Goods,Local Currency',2,"Step16.b:")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 16:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.c: Verify first bar color")
          
        """
        Step17: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_util_obj.switch_to_new_window()
          
        """
        Step 18: Verify output
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 16:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.c: Verify first bar color")
          
        """
        Step 19: Close output window
        """
        core_util_obj.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element("#applicationButton img", 1, metaobj.chart_medium_timesleep)
            
        """
        Step 20: Click Save in the toolbar
        Step 21: Save as "C2158261" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
            
        """
        Step 22: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
            
        """
        Step 23: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_ia_2',mrid='mrid',mrpass='mrpass')
           
        """
        Step 24: Verify Canvas and Filter pane
        """
        utillobj.synchronize_with_number_of_element('#MAINTABLE_wbody1', 1, metaobj.chart_medium_timesleep)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step24.a:")
        metaobj.verify_filter_pane_field('Cost of Goods,Local Currency',2,"Step24.b:")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 24:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 24:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 24:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 24.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 24.c: Verify first bar color")
        
        """
        Step 25: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()