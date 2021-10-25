'''
Created on Jul 13, 2018

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5831876
Test case Name =  Change Filter Operator from Range to Equals for list with negative values
'''

import unittest
from common.lib import utillity, core_utility
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, visualization_properties
from common.lib.basetestcase import BaseTestCase

class C5831876_TestClass(BaseTestCase):

    def test_C5831876(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C5831876'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']", metaobj.chart_long_timesleep)
        
        """
        Step 02: Double-click "Gross Profit", located under Sales Measures
        """
        metaobj.datatree_field_click("Gross Profit",2,1)
         
        """
        Step 03: Double-click "Product,Subcategory", located under Product Dimension
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, metaobj.chart_long_timesleep)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
         
        """
        Step 04: Drag and drop "Gross Profit" to the Filter pane
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 21, metaobj.chart_long_timesleep)
        metaobj.drag_drop_data_tree_items_to_filter("Gross Profit", 1) 
         
        """
        Step 05: Verify Filter dialog
        Step 06: Click OK
        """
        utillobj.synchronize_until_element_is_visible("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']", metaobj.chart_long_timesleep)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Range'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify=True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 06.00: Verify dialog')
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "posneg_float_value")
        utillobj.asequal(float(d['posneg_float_value']),-2402.4,"Step 06.01: Verify range from value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),3996,"Step 06.02: Verify range to value")  
        metaobj.verify_visualization_filters('numeric',['Aggregation','(None)','false'],['By','Product,Subcategory','true'],['Operator','Range','false'],['Sort','Ascending','true'],['ShowPrompt','true'],msg="Step 06.03:")   
        metaobj.create_visualization_filters('numeric')
        utillobj.synchronize_until_element_disappear("#avFilterOkBtn", metaobj.chart_long_timesleep)
        
        """
        Step 07: Verify Canvas
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Gross Profit',1,"Step 07.00")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',-2402.4,'float',msg="Step 07.01: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',3996,'int',msg="Step 07.02: Verify filter prompt range max values")
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1  svg g.risers >g>rect[class^='riser']", 21, metaobj.chart_long_timesleep)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 07.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 07.04: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.05: Verify first bar color")
        xaxis_value="Product Subcategory"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 07.06: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 07.07: Verify Y Axis Title") 
        expected_tooltip=['Product Subcategory:Blu Ray', 'Gross Profit:$51,771,195.13', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 07.08: verify the default tooltip values")
        
        """
        Step 08: Click on Prompt menu > select "Equals"
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        utillobj.synchronize_until_element_is_visible(parent_css, metaobj.chart_long_timesleep)
        propertyobj.change_prompt_options("1","Equals")
        
        """
        Step 09: Verify Filter Prompt
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        utillobj.synchronize_with_visble_text(parent_css, '[All]', metaobj.chart_long_timesleep)
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step 09.00: Verify [All] is checked in filter prompt")
        
        """
        Step10: Select values -$2,402.40 through -$1,700.18
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item(1, '-$2,402.40')
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,801.80')
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,800.42')
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,700.18')
        
        """
        Step 11: Verify Canvas
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Gross Profit',1,"Step 11.00")
        xaxis_value="Product Subcategory"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 11.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 11.02: Verify Y-Axis Title")
        expected_xval_list=['Flat Panel TV', 'Professional']
        expected_yval_list=['-20K', '-16K', '-12K', '-8K', '-4K', '0']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 11.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.05: Verify first bar color")
        bar=['Product Subcategory:Flat Panel TV', 'Gross Profit:-$15,502.10', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 11.06: Verify bar value")
        propertyobj.select_or_verify_show_prompt_item(1, '-$2,402.40', verify=True, verify_type=True, msg="Step 11.07: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,801.80', verify=True, verify_type=True, msg="Step 11.08: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,800.42', verify=True, verify_type=True, msg="Step 11.09: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,700.18', verify=True, verify_type=True, msg="Step 11.10: Verify values is checked in filter prompt")
        
        """
        Step 12: Right-click "Gross Profit" in the Filter pane > Edit...
        """
        metaobj.filter_tree_field_click('Gross Profit',1,1,'Edit...')
        
        """
        Step 13: Verify dialog
        Step 14: Click Cancel
        """
        utillobj.synchronize_until_element_is_visible("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']", metaobj.chart_long_timesleep)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Equal to'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify=True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 14.00: Verify dialog') 
        item_list=['-$2,402.40','-$1,801.80','-$1,800.42','-$1,700.18' ]
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', msg = 'step 14.01: Verify dialog')
        metaobj.verify_visualization_filters('numeric',['Aggregation','(None)','false'],['By','Product,Subcategory','true'],['Operator','Equal to','false'],['Sort','Ascending','false'],['ShowPrompt','true'],msg="Step 14.02:")
        metaobj.create_visualization_filters('numeric', ok=False)
        utillobj.synchronize_until_element_disappear("#avFilterOkBtn", metaobj.chart_long_timesleep)
        
        """
        Step15: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window()
          
        """
        Step 16: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        utillobj.synchronize_until_element_is_visible(chart_type_css, metaobj.chart_long_timesleep)
        xaxis_value="Product Subcategory"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16.00: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 16.01: Verify Y-Axis Title")
        expected_xval_list=['Flat Panel TV', 'Professional']
        expected_yval_list=['-20K', '-16K', '-12K', '-8K', '-4K', '0']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16.02: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 16.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.04: Verify first bar color")
        bar=['Product Subcategory:Flat Panel TV', 'Gross Profit:-$15,502.10', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 16.05: Verify bar value")
        propertyobj.select_or_verify_show_prompt_item(1, '-$2,402.40', verify=True, verify_type=True, msg="Step 16.06: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,801.80', verify=True, verify_type=True, msg="Step 16.07: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,800.42', verify=True, verify_type=True, msg="Step 16.08: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,700.18', verify=True, verify_type=True, msg="Step 16.09: Verify values is checked in filter prompt")
        
        """
        Step 17: Close output window
        """
        core_utilobj.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible("#applicationButton img", metaobj.chart_long_timesleep)
          
        """
        Step 18: Click Save in the toolbar > Save as "C5831876" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", metaobj.chart_long_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
          
        """
        Step 19: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
          
        """
        Step 20: Restore the fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC5831876.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_1',mrid='mrid',mrpass='mrpass')
         
        """
        Step 21: Verify Canvas
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Gross Profit',1,"Step 21.00")
        xaxis_value="Product Subcategory"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 21.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 21.02: Verify Y-Axis Title")
        expected_xval_list=['Flat Panel TV', 'Professional']
        expected_yval_list=['-20K', '-16K', '-12K', '-8K', '-4K', '0']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 21.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 21.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 21.05: Verify first bar color")
        bar=['Product Subcategory:Flat Panel TV', 'Gross Profit:-$15,502.10', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 21.06: Verify bar value")
        
        expected_list= ['-$2,402.40', '-$1,801.80', '-$1,800.42', '-$1,700.18']
        checked_elems=self.driver.find_elements_by_css_selector("div[id*='Prompt_1'] table[style*=hidden] tr")[:6]
        checked_list=[t.text.strip() for t in checked_elems if len(t.find_elements_by_css_selector("input[checked='checked']"))==1]
        utillobj.as_List_equal(expected_list,checked_list,"Step 21.07: Verify values is checked in filter prompt")
        
        """
        Step 22: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()