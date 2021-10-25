'''
Created on Apr 21, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227654
Test case Name =  Range with Attributes field Sale,Year Month
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.wftools.visualization import Visualization

class C2227654_TestClass(BaseTestCase):

    def test_C2227654(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227654'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visualization = Visualization(self.driver)
        
        """
        TESTCASE CSS
        """
        qwery_tree_css = "#queryTreeWindow"
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        visualization.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02: Double-click "Cost of Goods"
        """
        visualization.double_click_on_datetree_item("Cost of Goods", 1)
        visualization.wait_for_visible_text(qwery_tree_css, "Cost of Goods")
                 
        """
        Step03: Expand Product Dimension > Double click "Product,Category"
        """
        visualization.double_click_on_datetree_item("Product,Category", 1)
        visualization.wait_for_visible_text(qwery_tree_css, "Product,Category")
         
        """
        Step04: Expand Dimension "Sales_Related" > "Trasaction Date,Simple" > "Sale,Day" > "Attributes" > Drag and drop "Sale, Year Month" into the Rows bucket in the Query pane
        """
        metaobj.drag_drop_data_tree_items_to_query_tree("Sale,Year Month", 1, 'Rows', 0)
        visualization.wait_for_visible_text(qwery_tree_css, "Sale,Year Month")
        
        """
        Step05: Drag and drop "Sale,Year Month" into the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter("Sale,Year Month", 1)       
        visualization.wait_for_visible_text("#avFilterCancelBtn", "Cancel")
         
        """
        Step06: Verify Filter dialog
        Step07: Click OK
        """      
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
         
        elem=self.driver.find_element_by_css_selector("#avOperatorComboBox div")
        d=utillobj.get_attribute_value(elem,'text')
        utillobj.asequal(d['text'],'Range',"Step 06.01 : Verify Operator dialog")
                  
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"201101","Step 06.02 : Verify From in Filter dialog")
                 
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"201703","Step 06.03 : Verify To in Filter dialog")
         
        time.sleep(2)
        metaobj.create_visualization_filters('numeric')
        time.sleep(3)
         
        """
        Step08: Verify Canvas
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',201101,'int',msg="Step 08.01 : Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',201703,'int',msg="Step 08.02 : Verify filter prompt range values- max")
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, visualization.home_page_long_timesleep)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 432, visualization.home_page_long_timesleep)
        metaobj.verify_filter_pane_field('Sale,Year Month',1,"Step 08.03 : Verify 'Sale,Day' appears in filter pane")
        time.sleep(2)  
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 08.04 : Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08.05 :Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 504, 'Step 08.06 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", "bar_blue", "Step 08.07 : Verify first bar color")
        time.sleep(5)
        expected=['Sale Year Month', '201101','201102','201103','201104','201105','201106','201107']
        visualization.verify_rows_label(expected,  msg="Step 08.08", label_length=4)
        time.sleep(5) 
         
        """
        Step09: Drag the left slider handle in the Filter Prompt to the right > change value to 201505
        """
        visualization.drag_minimum_value_slider_in_filter_prompt(201221)
          
        """
        Step10: Verify Canvas
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, visualization.home_page_long_timesleep)
        time.sleep(5)
        browser=utillobj.parseinitfile('browser')
        if browser=='Firefox':
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',201221,'int',msg="Step 10.01 : Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',201703,'int',msg="Step 10.01 : Verify filter prompt range values- max")
        else:
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',201221,'int',msg="Step 10.01 : Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',201703,'int',msg="Step 10.01 : Verify filter prompt range values- max")         
        time.sleep(2)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, visualization.home_page_long_timesleep)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 288, visualization.home_page_long_timesleep)
        time.sleep(2)
        metaobj.verify_filter_pane_field('Sale,Year Month',1,"Step 10.02 : Verify 'Sale,Day' appears in filter pane")
        time.sleep(5)  
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 10.03 : Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10.04 :Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 336, 'Step 10.05 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", "bar_blue", "Step 10.06 : Verify first bar color")
        time.sleep(5)
        expected=['Sale Year Month', '201301','201301','201303','201304','201305','201306','201307']
        visualization.verify_rows_label(expected,  msg="Step 10.07", label_length=4)
        
        """
        Step11: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        visualization.switch_to_new_window()
                 
        """
        Step12: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g3!mbar!r0!c0']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, visualization.home_page_long_timesleep)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 288, visualization.home_page_long_timesleep)
        browser=utillobj.parseinitfile('browser')
        if browser=='Firefox':
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',201221,'int',msg="Step 12.01 : Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',201703,'int',msg="Step 12.01 : Verify filter prompt range values- max")
        else:
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',201221,'int',msg="Step 12.01 : Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',201703,'int',msg="Step 12.01 : Verify filter prompt range values- max")         
        time.sleep(2)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 12.02 : Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12.03 :Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 336, 'Step 12.04 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", "bar_blue", "Step 12.05 : Verify first bar color")
        time.sleep(5)
        expected=['Sale Year Month', '201301','201301','201303','201304','201305','201306','201307']
        visualization.verify_rows_label(expected,  msg="Step 12.06", label_length=4)
        
        """
        Step13: Close output window
        """
        visualization.switch_to_previous_window()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
      
        """
        Step14: Click Save in the toolbar
        Step15: Save as "C2227654" > Click Save
        """
        visualization.save_visualization_from_top_toolbar(Test_Case_ID)
        utillobj.synchronize_until_element_disappear("#IbfsOpenFileDialog7_btnCancel", visualization.home_page_short_timesleep)
                  
        """
        Step16: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visualization.logout_visualization_using_api()
              
        """
        Step17: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227654.fex&tool=idis
        """
        visualization.edit_visualization_using_api(Test_Case_ID)
                 
        """
        Step18: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g3!mbar!r0!c0']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, visualization.home_page_medium_timesleep)
        browser=utillobj.parseinitfile('browser')
        if browser=='Firefox':
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',201221,'int',msg="Step 18.01 : Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',201703,'int',msg="Step 18.01 : Verify filter prompt range values- max")
        else:
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',201221,'int',msg="Step 18.01 : Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',201703,'int',msg="Step 18.01 : Verify filter prompt range values- max")         
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, visualization.home_page_long_timesleep)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 288, visualization.home_page_long_timesleep)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 18.02 : Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 18.03 : Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 336, 'Step 18.04 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", "bar_blue", "Step 18.05: Verify first bar color")
        time.sleep(5)
        expected=['Sale Year Month', '201301','201301','201303','201304','201305','201306','201307']
#         resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows',, expected,"Step 18.06 : Verify Row header")
        visualization.verify_rows_label(expected,  msg="Step 18.06", label_length=4) 
        time.sleep(2)
         
        """
        Step19: Logout
        """
        
if __name__ == '__main__':
    unittest.main()