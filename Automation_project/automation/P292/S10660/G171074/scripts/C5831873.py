'''
Created on Jun 27, 2018

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5831873
Test case Name =  Hide Filter Prompt from dialog
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity, core_utility
from selenium.common.exceptions import NoSuchElementException


class C5831873_TestClass(BaseTestCase):

    def test_C5831873(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C5831873'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']", metaobj.chart_long_timesleep)
        
        """
        Step 02: Double-click "Cost of Goods, Local Currency", located under Sales Measures
        """
        metaobj.datatree_field_click("Cost of Goods,Local Currency",2,1)
        
        """
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, metaobj.chart_long_timesleep)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        
        """
        Step 04: Drag and drop "Product,Category" to the Filter pane
        Step 05: Click OK
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, metaobj.chart_long_timesleep)
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
        metaobj.create_visualization_filters('alpha')
        utillobj.synchronize_until_element_disappear("#avFilterOkBtn", metaobj.chart_long_timesleep)
        
        """
        Step 06: Drag and drop "Cost of Goods, Local Currency" to the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter('Cost of Goods,Local Currency', 1)
        
        """
        Step 07: Verify Filter dialog
        Step 08: Click OK
        """
        utillobj.synchronize_until_element_is_visible("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']", metaobj.chart_long_timesleep)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Range'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify=True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 07.00: Verify dialog')
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(float(d['float_value']),10.12,"Step 07.01: Verify range from value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(float(d['float_value']),3620014.67,"Step 07.02: Verify range to value")  
        metaobj.verify_visualization_filters('numeric',['Aggregation','(None)','false'],['By','Product,Category','true'],['Operator','Range','false'],
                                             ['Sort','Ascending','true'],['ShowPrompt','true'],msg="Step 07.03:")  
        metaobj.create_visualization_filters('numeric')
        utillobj.synchronize_until_element_disappear("#avFilterOkBtn", metaobj.chart_long_timesleep)
        
        """
        Step09: Edit "Cost of Goods, Local Currency" filter on canvas > Drag left slider handle to the right at value > 2830300.3
        """
        propertyobj.move_slider_measure('#ar_Prompt_2','min', 'right', 3, 'float') #2195070.2
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1_f rect[class*='riser']", 2, metaobj.chart_long_timesleep)
        
        """
        Step10: Verify Canvas 
        """
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','min',2172012.85,'float',msg="Step 10.00: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','max',3620014.67,'float',msg="Step 10.01: Verify filter prompt range max values")
        metaobj.verify_filter_pane_field('Product,Category',1,"Step 10.02")
        metaobj.verify_filter_pane_field('Cost of Goods,Local Currency',2,"Step 10.03")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10.05: Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10.06: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 10.07: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.08: Verify first bar color")
          
        """
        Step 11: Right click "Product,Category" filter in the Filter pane > Select "Hide Prompt"
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        utillobj.synchronize_until_element_is_visible(parent_css, metaobj.chart_long_timesleep)
        metaobj.filter_tree_field_click("Product,Category", 1, 1, "Hide Prompt")
          
        """
        Step12: Verify Canvas 
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        utillobj.synchronize_until_element_is_visible(parent_css, metaobj.chart_long_timesleep)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','min',2172012.85,'float',msg="Step 12.00: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','max',3620014.67,'float',msg="Step 12.01: Verify filter prompt range max values")
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step 12.02")
        metaobj.verify_filter_pane_field('Cost of Goods,Local Currency',2,"Step 12.03")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 12.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 12.05: Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12.06: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 12.07: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 12.08: Verify first bar color")
           
        """
        Step 13: Right click "Cost of Goods, Local Currency" filter in the Filter pane > Select "Edit"
        """
        metaobj.filter_tree_field_click('Cost of Goods,Local Currency',1,1, 'Edit...')
          
        """
        Step 14: Verify Filter dialog
        Step 15: Uncheck "Show Prompt" > click OK
        """
        utillobj.synchronize_until_element_is_visible("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']", metaobj.chart_long_timesleep)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Range'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify=True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 15.00: Verify dialog')
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        browser=utillobj.parseinitfile('browser')
        if browser=='IE':
            ran=2172013.35
        else:
            ran=2172012.85
        utillobj.asequal(float(d['float_value']),ran,"Step 15.01: Verify range from value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(float(d['float_value']),3620014.67,"Step 15.02: Verify range to value")  
        metaobj.verify_visualization_filters('numeric',['Aggregation','(None)','false'],['By','Product,Category','true'],['Operator','Range','false'],
                                             ['Sort','Ascending','true'],['ShowPrompt','true'],msg="Step 15.03:")  
        metaobj.create_visualization_filters('numeric',['ShowPrompt'])
        utillobj.synchronize_until_element_disappear("#avFilterOkBtn", metaobj.chart_long_timesleep)
          
        """
        Step16: Verify Canvas 
        """
        try:
            if self.driver.find_element_by_css_selector("div[id^='BoxLayoutFilterBox']").is_displayed():
                utillity.UtillityMethods.asequal(self, 'displayed', 'should not display', "Step 16.00: Verify Filter Prompts not removed from canvas")
        except NoSuchElementException:
            utillity.UtillityMethods.asequal(self, 'displayed', 'displayed', "Step 16.01: Verify Filter Prompts are removed from canvas")
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step 16.02")
        metaobj.verify_filter_pane_field('Cost of Goods,Local Currency',2,"Step 16.03")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 16.05: Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16.06: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 16.07: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.08: Verify first bar color")
          
        """
        Step17: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window()
          
        """
        Step 18: Verify output
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, metaobj.chart_long_timesleep)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 18.00: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 18.01: Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 18.02: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 18.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 18.04: Verify first bar color")
          
        """
        Step 19: Close output window
        """
        core_utilobj.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible("#applicationButton img", metaobj.chart_long_timesleep)
            
        """
        Step 20: Click Save in the toolbar > Save as "C5831873" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", metaobj.chart_long_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
            
        """
        Step 21: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
            
        """
        Step 22: Restore the fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227680.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_1',mrid='mrid',mrpass='mrpass')
           
        """
        Step 23: Verify Canvas and Filter pane
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Product,Category', 1, "Step 23.00")
        metaobj.verify_filter_pane_field('Cost of Goods,Local Currency', 2, "Step 23.01")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 23.02: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 23.03: Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 23.04: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 23.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 23.06: Verify first bar color")
        
        """
        Step 24: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()