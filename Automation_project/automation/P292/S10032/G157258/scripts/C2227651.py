'''
Created on Apr 19, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227651
Test case Name =  Filter with Integer field 'Month'
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.wftools.visualization import Visualization

class C2227651_TestClass(BaseTestCase):

    def test_C2227651(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227651'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visualization = Visualization(self.driver)
        
        """
        TESTCASE CSS
        """
        query_tree_css = "#queryTreeWindow"
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        visualization.invoke_visualization_using_api('baseapp/wf_retail_lite', 'mrid', 'mrpass')
        visualization.wait_for_visible_text("#pfjTableChart_1", "Drop")
         
        """
        Step 02: Double-click "Cost of Goods" and "Gross Profit", located under Sales Measures
        """
        visualization.double_click_on_datetree_item("Cost of Goods", 1)
        visualization.wait_for_visible_text(query_tree_css, "Cost of Goods")
        
        visualization.double_click_on_datetree_item("Gross Profit", 1)
        visualization.wait_for_visible_text(query_tree_css, "Gross Profit")
                 
        """
        Step03: Expand Product Dimension > Double click "Product,Category"
        Step04: Expand Dimension "Sales_Related" > "Trasaction Date,Simple" > Drag and drop "Sale,Month" into the Rows bucket in the Query pane
        """
        visualization.double_click_on_datetree_item("Product,Category", 1)
        visualization.wait_for_visible_text(query_tree_css, "Product,Category")
        visualization.drag_field_from_data_tree_to_query_pane("Sale,Month", 1, 'Rows', 1)
        visualization.wait_for_visible_text(query_tree_css, "Sale,Month")
                 
        """
        Step05: Drag and drop "Sale,Month" into the Filter pane
        """      
        visualization.drag_and_drop_from_data_tree_to_filter("Sale,Month", 1)
        utillobj.wait_for_page_loads(20)
                         
        """
        Step06: Verify Filter dialog
        Step07: Click "Operators" dropdown box > select "Equal to"
        Step08: Uncheck values 1 through 6
        Step09: Click OK
        """  
        visualization.wait_for_number_of_element('#avfFromValue input', 1)
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"1","Step 06.01: Verify From in Filter dialog")
        
        visualization.wait_for_number_of_element("#avfToValue input", 1)
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"12","Step 06.02: Verify To in Filter dialog")
  
        l=['1','2','3','4','5','6']               
        metaobj.create_visualization_filters('numeric',['Operator','Equal to'],['GridItems',l])
        time.sleep(3)
                   
        """
        Step10: Verify Canvas
        """
        time.sleep(10)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('1', '7',verify=True, verify_type="true",msg="Step 10.01: Verify 7 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '8',verify=True, verify_type="true",msg="Step 10.02: Verify 8 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '9',verify=True, verify_type="true",msg="Step 10.03: Verify 9 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '10',verify=True, verify_type="true",msg="Step 10.04: Verify 10 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '11',verify=True, verify_type="true",msg="Step 10.05: Verify 11 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '12',verify=True, verify_type="true",msg="Step 10.06: Verify 12 checked in prompt")
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
#         resultobj.wait_for_property(parent_css, 7)
        visualization.wait_for_number_of_element(parent_css, 7, 30)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        visualization.wait_for_number_of_element(parent_css, 48, 30)
#         resultobj.wait_for_property(parent_css, 48)
#         time.sleep(2) 
        metaobj.verify_filter_pane_field('Sale,Month',1,"Step 10.07: Verify 'Sale,Month' appears in filter pane")        
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 10.08: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 10.09: Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        time.sleep(2)
        expected_yval_list=['0', '5M','10M','15M','20M','25M','30M','35M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10.10:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 84, 'Step 10.11: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c0", "bar_blue", "Step 10.12: Verify first bar color")
        time.sleep(5)
        expected=['7', '8', '9', '10', '11', '12']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month', expected,"Step 10.13: Verify Row header")
                  
        """
        Step11: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        visualization.switch_to_new_window()  
        time.sleep(15)
        
        """
        Step12: Verify output
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s']")
        resultobj._validate_page(elem1)
        propertyobj.select_or_verify_show_prompt_item('1', '7',verify=True, verify_type="true",msg="Step 12.01: Verify 7 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '8',verify=True, verify_type="true",msg="Step 12.02: Verify 8 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '9',verify=True, verify_type="true",msg="Step 12.03: Verify 9 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '10',verify=True, verify_type="true",msg="Step 12.04: Verify 10 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '11',verify=True, verify_type="true",msg="Step 12.05: Verify 11 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '12',verify=True, verify_type="true",msg="Step 12.06: Verify 12 checked in prompt")
        time.sleep(5)  
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 12.07: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 12.08: Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M','30M','35M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12.09:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 84, 'Step 12.10: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c0", "bar_blue", "Step 12.11: Verify first bar color")
        time.sleep(5)
        expected=['7', '8', '9', '10', '11', '12']
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month', expected,"Step 12.12: Verify Row header")
                        
        """
        Step13: Close output window
        """
        visualization.switch_to_previous_window()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
        
        """
        Step14: Click Save
        Step15: Click Save as "C2158200" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        visualization.wait_for_visible_text('#IbfsOpenFileDialog7_btnCancel', "Cancel")
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.synchronize_until_element_disappear("#IbfsOpenFileDialog7_btnCancel", visualization.home_page_short_timesleep)
                    
        """
        Step16: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step17: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158198.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
                 
        """
        Step18: Verify Canvas
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        metaobj.verify_filter_pane_field('Sale,Month',1,"Step18: Verify 'Sale,Month' appears in filter pane")
        propertyobj.select_or_verify_show_prompt_item('1', '7',verify=True, verify_type="true",msg="Step 18.01: Verify 7 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '8',verify=True, verify_type="true",msg="Step 18.02: Verify 8 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '9',verify=True, verify_type="true",msg="Step 18.03: Verify 9 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '10',verify=True, verify_type="true",msg="Step 18.04: Verify 10 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '11',verify=True, verify_type="true",msg="Step 18.05: Verify 11 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '12',verify=True, verify_type="true",msg="Step 18.06: Verify 12 checked in prompt")
        time.sleep(5) 
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g4!mbar!r0!c0']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True)
        time.sleep(3) 

        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 18.07: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 18.08: Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        time.sleep(2)

        expected_yval_list=['0', '5M','10M','15M','20M','25M','30M','35M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 18.09:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 84, 'Step 18.10: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c0", "bar_blue", "Step 18.11: Verify first bar color")
        time.sleep(5)
        expected=['7', '8', '9', '10', '11', '12']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month', expected,"Step 18.12: Verify Row header")
            
        """
        Step19: Check off values 3, 4 and 5 in the Filter Prompt
        Step20: Verify Canvas
        """
        time.sleep(2)
        propertyobj.select_or_verify_show_prompt_item('1', '4')
        propertyobj.select_or_verify_show_prompt_item('1', '5')
        propertyobj.select_or_verify_show_prompt_item('1', '6')
          
        time.sleep(2)
        propertyobj.select_or_verify_show_prompt_item('1', '4',verify=True, verify_type="true",msg="Step 19.01: Verify 4 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '5',verify=True, verify_type="true",msg="Step 19.02: Verify 5 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '6',verify=True, verify_type="true",msg="Step 19.03: Verify 6 checked in prompt")
        resultobj.wait_for_property("#MAINTABLE_wbody1 svg g.risers>g>rect[class^='riser']", 126)
        time.sleep(5)
        expected=['4','5','6','7', '8', '9', '10']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month', expected,"Step 20.01: Verify Row header")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 126, 'Step 20.02: Verify the total number of risers displayed on preview')
          
        """
        Step21: Click "Save"
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
        time.sleep(2)
         
        """
        Step22: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        visualization.switch_to_new_window()  
        time.sleep(15)
         
        """
        Step23: Verify output
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s']")
        resultobj._validate_page(elem1)
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 23.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 23.02: Verify Y-Axis Title")
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 54)
        time.sleep(2)
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 23.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 126, 'Step 23.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c0", "bar_blue", "Step 23.05: Verify first bar color")
        time.sleep(5)
        expected=['4','5','6','7', '8', '9', '10', '11', '12']
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month', expected,"Step 23.06: Verify Row header")
        time.sleep(20)
        propertyobj.select_or_verify_show_prompt_item('1', '4',verify=True, verify_type="true",msg="Step 23.07: Verify 3 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '5',verify=True, verify_type="true",msg="Step 23.08: Verify 4 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '6',verify=True, verify_type="true",msg="Step 23.09: Verify 5 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '7',verify=True, verify_type="true",msg="Step 23.10: Verify 7 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '8',verify=True, verify_type="true",msg="Step 23.11: Verify 8 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '9',verify=True, verify_type="true",msg="Step 23.12: Verify 9 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '10',verify=True, verify_type="true",msg="Step 23.13: Verify 10 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '11',verify=True, verify_type="true",msg="Step 23.14: Verify 11 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '12',verify=True, verify_type="true",msg="Step 23.15: Verify 12 checked in prompt")
         
        """
        Step24: Close the output window
        """
        visualization.switch_to_previous_window()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
         
        """
        Step25: Logout
        """
if __name__ == '__main__':
    unittest.main()