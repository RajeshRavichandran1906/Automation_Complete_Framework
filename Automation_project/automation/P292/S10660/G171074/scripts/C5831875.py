'''
Created on Jul 12, 2018

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5831875
Test case Name =  Change Filter Operator from Range to Equals - verify List of Values
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity, core_utility


class C5831875_TestClass(BaseTestCase):

    def test_C5831875(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C5831875'
        
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
        Step 02: Double-click "Cost of Goods", located under Sales Measures.
        """
        metaobj.datatree_field_click("Cost of Goods",2,1)
         
        """
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, metaobj.chart_long_timesleep)
        metaobj.datatree_field_click("Product,Category", 2, 1)
         
        """
        Step 04: Drag and drop "Cost of Goods" to the Filter pane
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, metaobj.chart_long_timesleep)
        metaobj.drag_drop_data_tree_items_to_filter("Cost of Goods", 1) 
 
        """
        Step 05: Click "Operator" dropdown box > select "Equal to"
        Step 06: Verify dialog
        Step 07: Click OK
        """
        utillobj.synchronize_until_element_is_visible("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']", metaobj.chart_long_timesleep)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Equal to'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify=True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 07.00: Verify dialog') 
        item_list=['[All]']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', msg = 'step 07.01: Verify dialog')
        metaobj.verify_visualization_filters('numeric',['Aggregation','(None)','false'],['By','Product,Category','true'],['Operator','Equal to','false'],['Sort','Ascending','false'],['ShowPrompt','true'],msg="Step 07.02:")
        metaobj.create_visualization_filters('numeric')
        utillobj.synchronize_until_element_disappear("#avFilterOkBtn", metaobj.chart_long_timesleep)
        
        """
        Step 08: Verify Canvas
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step 08.00")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 08.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 08.02: Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 08.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08.05: Verify first bar color")
         
        """
        Step09: Select values $16.00 through $50.00 in the Filter Prompt
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        utillobj.synchronize_until_element_is_visible(parent_css, metaobj.chart_long_timesleep)
        propertyobj.select_or_verify_show_prompt_item(1, '$16.00')
        propertyobj.select_or_verify_show_prompt_item(1, '$23.00')
        propertyobj.select_or_verify_show_prompt_item(1, '$32.00')
        propertyobj.select_or_verify_show_prompt_item(1, '$34.00')
        propertyobj.select_or_verify_show_prompt_item(1, '$36.00')
        propertyobj.select_or_verify_show_prompt_item(1, '$42.00')
        propertyobj.select_or_verify_show_prompt_item(1, '$45.00')
        propertyobj.select_or_verify_show_prompt_item(1, '$46.00')
        propertyobj.select_or_verify_show_prompt_item(1, '$48.00')
        propertyobj.select_or_verify_show_prompt_item(1, '$50.00')
         
        """
        Step 10: Verify Canvas
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step 10.00")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10.02: Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Media Player', 'Stereo Systems', 'Televisions']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 10.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.05: Verify first bar color")
        propertyobj.select_or_verify_show_prompt_item(1, '$16.00', verify=True, verify_type=True, msg="Step 10.06: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$23.00', verify=True, verify_type=True, msg="Step 10.07: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$32.00', verify=True, verify_type=True, msg="Step 10.08: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$34.00', verify=True, verify_type=True, msg="Step 10.09: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$36.00', verify=True, verify_type=True, msg="Step 10.10: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$42.00', verify=True, verify_type=True, msg="Step 10.11: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$45.00', verify=True, verify_type=True, msg="Step 10.12: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$46.00', verify=True, verify_type=True, msg="Step 10.13: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$48.00', verify=True, verify_type=True, msg="Step 10.14: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$50.00', verify=True, verify_type=True, msg="Step 10.15: Verify values is checked in filter prompt")
         
        """
        Step11: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window()
          
        """
        Step 12: Verify output
        """
        riser_css="#MAINTABLE_wbody1 rect[class*='riser!s0!g0!mbar']"
        utillobj.synchronize_until_element_is_visible(riser_css, metaobj.chart_long_timesleep)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 12.00: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 12.01: Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Media Player', 'Stereo Systems', 'Televisions']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12.02: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 12.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 12.04: Verify first bar color")
        propertyobj.select_or_verify_show_prompt_item(1, '$16.00', verify=True, verify_type=True, msg="Step 12.05: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$23.00', verify=True, verify_type=True, msg="Step 12.06: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$32.00', verify=True, verify_type=True, msg="Step 12.07: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$34.00', verify=True, verify_type=True, msg="Step 12.08: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$36.00', verify=True, verify_type=True, msg="Step 12.09: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$42.00', verify=True, verify_type=True, msg="Step 12.10: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$45.00', verify=True, verify_type=True, msg="Step 12.11: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$46.00', verify=True, verify_type=True, msg="Step 12.12: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$48.00', verify=True, verify_type=True, msg="Step 12.13: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$50.00', verify=True, verify_type=True, msg="Step 12.14: Verify values is checked in filter prompt")
         
        """
        Step 13: Close output window
        """
        core_utilobj.switch_to_previous_window()
        parent_css= "#applicationButton img"
        utillobj.synchronize_until_element_is_visible(parent_css, metaobj.chart_long_timesleep)
          
        """
        Step 14: Click Save in the toolbar > Save as "C5831875" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", metaobj.chart_long_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
          
        """
        Step 15: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
          
        """
        Step 16: Reopen fex using IA API: http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC5831875.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_1',mrid='mrid',mrpass='mrpass')
         
        """
        Step 17: Verify Canvas
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 4, metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step 17.00")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 17.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 17.02: Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Media Player', 'Stereo Systems', 'Televisions']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 17.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 17.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 17.05: Verify first bar color")
        propertyobj.select_or_verify_show_prompt_item(1, '$16.00', verify=True, verify_type=True, msg="Step 17.06: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$23.00', verify=True, verify_type=True, msg="Step 17.07: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$32.00', verify=True, verify_type=True, msg="Step 17.08: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$34.00', verify=True, verify_type=True, msg="Step 17.09: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$36.00', verify=True, verify_type=True, msg="Step 17.10: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$42.00', verify=True, verify_type=True, msg="Step 17.11: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$45.00', verify=True, verify_type=True, msg="Step 17.12: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$46.00', verify=True, verify_type=True, msg="Step 17.13: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$48.00', verify=True, verify_type=True, msg="Step 17.14: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$50.00', verify=True, verify_type=True, msg="Step 17.15: Verify values is checked in filter prompt")
        
        """
        Step 18: Right click "Cost of Goods" filter in the Filter pane > Edit
        Step 19: Verify dialog
        Step 20: Deselect values $16.00, $23.00 and $32.00 > Click OK
        """
        metaobj.filter_tree_field_click('Cost of Goods',1,1,'Edit...')
        utillobj.synchronize_until_element_is_visible("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']", metaobj.chart_long_timesleep)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Equal to'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 20.00: Verify dialog') 
        metaobj.verify_visualization_filters('numeric',['Aggregation','(None)','false'],['By','Product,Category','true'],['Operator','Equal to','false'],['Sort','Ascending','false'],['ShowPrompt','true'],msg="Step 20.01:")
        item_list=['$16.00', '$23.00', '$32.00']
        metaobj.select_or_verify_visualization_filter_values(item_list, Ok_button=True)
        
        """
        Step 21: Verify Canvas
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels!m5!']"
        utillobj.synchronize_with_visble_text(parent_css, '1.5M', metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step 21.00")
        propertyobj.select_or_verify_show_prompt_item(1, '$34.00', verify=True, verify_type=True, msg="Step 21.01: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$36.00', verify=True, verify_type=True, msg="Step 21.02: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$42.00', verify=True, verify_type=True, msg="Step 21.03: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$45.00', verify=True, verify_type=True, msg="Step 21.04: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$46.00', verify=True, verify_type=True, msg="Step 21.05: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$48.00', verify=True, verify_type=True, msg="Step 21.06: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$50.00', verify=True, verify_type=True, msg="Step 21.07: Verify values is checked in filter prompt")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 21.07: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 21.08: Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Media Player', 'Stereo Systems', 'Televisions']
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 21.09: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 21.10: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 21.11: Verify first bar color")
        
        """
        Step 22: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()