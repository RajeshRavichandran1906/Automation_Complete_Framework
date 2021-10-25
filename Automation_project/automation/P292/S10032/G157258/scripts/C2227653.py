'''
Created on Apr 20, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227653
Test case Name =  List of Values with Attributes field
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, core_metadata
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.wftools.visualization import Visualization

class C2227653_TestClass(BaseTestCase):

    def test_C2227653(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227653'
        qwery_tree_css = "#queryTreeWindow"
        
        utillobj = utillity.UtillityMethods(self.driver)
        core_meta = core_metadata.CoreMetaData(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        visualization = Visualization(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        visualization.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02: Double-click "Cost of Goods", "Gross Profit" and "Revenue"
        """
        visualization.double_click_on_datetree_item("Cost of Goods", 1)
        visualization.wait_for_visible_text(qwery_tree_css, "Cost of Goods")
        visualization.double_click_on_datetree_item("Gross Profit", 1)
        visualization.wait_for_visible_text(qwery_tree_css, "Gross Profit")
        visualization.double_click_on_datetree_item("Revenue", 1)
        visualization.wait_for_visible_text(qwery_tree_css, "Revenue")
                  
        """
        Step03: Expand Product Dimension > Double click "Product,Category"
        Step04: Expand Dimension "Sales_Related" > "Transaction Date,Simple" > "Sale,Month" > "Attributes" > Drag and drop "Sale,Month Name" into the Rows bucket under Matrix in the Query pane.
        """
        visualization.double_click_on_datetree_item("Product,Category", 1)
        visualization.wait_for_visible_text(qwery_tree_css, "Product,Category")
        core_meta.collapse_data_field_section('Sales')
        visualization.drag_field_from_data_tree_to_query_pane("Sale,Month Name", 1, 'Rows')
                  
        """
        Step05: Drag and drop "Sale,Month Name" into the Filter pane
        """
        visualization.wait_for_number_of_element("text[class*='rowHeader-label']", 1)
        visualization.drag_and_drop_from_data_tree_to_filter("Sale,Month Name", 1)
        visualization.wait_for_number_of_element('#avFilterOkBtn',1)
                  
        """
        Step06: Verify Filter dialog
        Step07: Click OK
        """            
        field_value_list=['[All]', 'APR','AUG','DEC','FEB','JAN','JUL','JUN','MAR','MAY','NOV','OCT','SEP']
        visualization.verify_filter_field_values(field_value_list, verify_type='true')
        visualization.close_filter_dialog('ok')
                     
        """
        Step08: Verify Canvas
        """
        visualization.wait_for_visible_text('#qbFilterBox', 'Sale,Month Name')
        visualization.verify_field_in_filterbox('Sale,Month Name',1, msg= 'Step 08.01')             
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type="true",msg="Step 08.02:Verify prompt [All] is checked")
        time.sleep(5)                      
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit','Revenue']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 08.03: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 08.04: Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0','14M','28M','42M','56M','70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08.05:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 3, 84, 'Step 08.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", "dark_green", "Step 08.07: Verify first bar color")
        expected=['Sale Month Name', 'APR', 'AUG', 'DEC', 'FEB', 'JAN', 'JUL', 'JUN']
        visualization.verify_rows_label(expected,  msg="Step 08.08: Verify Row label", label_length=4)   
          
        """
        Step09: Click Run
        """
        visualization.run_visualization_from_toptoolbar()
        visualization.switch_to_new_window()
                  
        """
        Step10: Verify output
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s']")
        resultobj._validate_page(elem1)
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit','Revenue']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 10.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 10.02: Verify Y-Axis Title")
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 72)
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0','14M','28M','42M','56M','70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 3, 84, 'Step 10.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", "dark_green", "Step 10.05: Verify first bar color")
        time.sleep(5)
        expected=['Sale Month Name', 'APR', 'AUG', 'DEC', 'FEB', 'JAN', 'JUL', 'JUN', 'MAR', 'MAY']
        visualization.verify_rows_label(expected,  msg="Step 10.06: Verify Row label", label_length=4) 
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type="true",msg="Step 10.07:Verify prompt [All] is checked")
                             
        """
        Step11: Close output window
        """
        visualization.switch_to_previous_window()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
       
        """
        Step12: Click Save in the toolbar
        Step13: Save as "C2227653" > Click Save
        """
        visualization.save_visualization_from_top_toolbar(Test_Case_ID)
        utillobj.synchronize_until_element_disappear("#IbfsOpenFileDialog7_btnCancel", visualization.home_page_short_timesleep)
                   
        """
        Step14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visualization.logout_visualization_using_api()
               
        """
        Step15: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227653.fex&tool=idis
        """
        visualization.edit_visualization_using_api(Test_Case_ID)  
        
        """
        Step16: Verify Canvas
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        metaobj.verify_filter_pane_field('Sale,Month Name',1,"Step 16.01: Verify 'Sale,Month Name' appears in filter pane")
        time.sleep(5)
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit','Revenue']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 16.02: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 16.03: Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0','14M','28M','42M','56M','70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16.04: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 3, 84, 'Step 16.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", "dark_green", "Step 16.06: Verify first bar color")
        time.sleep(5)
        expected=['Sale Month Name', 'APR', 'AUG', 'DEC', 'FEB', 'JAN', 'JUL', 'JUN']
        visualization.verify_rows_label(expected,  msg="Step 16.07", label_length=4) 
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type="true",msg="Step 16.08: Verify prompt [All] is checked")
        time.sleep(5)
        
        """
        Step17: Check off values JAN, FEB, MAR in the Filter Prompt
        Step18: Verify Canvas
        """
        propertyobj.select_or_verify_show_prompt_item('1', 'JAN')
        time.sleep(2)
        propertyobj.select_or_verify_show_prompt_item('1', 'FEB')
        time.sleep(2)
        propertyobj.select_or_verify_show_prompt_item('1', 'MAR')
        time.sleep(2)
        
        propertyobj.select_or_verify_show_prompt_item('1', 'FEB',verify=True, verify_type="true",msg="Step 17.01: Verify prompt FEB is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'JAN',verify=True, verify_type="true",msg="Step 17.02: Verify prompt JAN is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'MAR',verify=True, verify_type="true",msg="Step 17.03: Verify prompt MAR is checked")
        time.sleep(5)
                    
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit','Revenue']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 17.04: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 17.05: Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 17.06:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 3, 21, 'Step 17.07: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", "dark_green", "Step 17.08: Verify first bar color")
        time.sleep(5)
        expected=['Sale Month Name', 'FEB', 'JAN', 'MAR']
        visualization.verify_rows_label(expected,  msg="Step 18.01: Verify Row label", label_length=4) 
        
        """
        Step19: Click Run
        """
        visualization.run_visualization_from_toptoolbar()
        visualization.switch_to_new_window()
                  
        """
        Step20: Verify output
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s']")
        resultobj._validate_page(elem1)
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit','Revenue']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 20.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 20.02: Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 20.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 3, 21, 'Step 20.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", "dark_green", "Step 20.05: Verify first bar color")
        time.sleep(5)
        expected=['Sale Month Name', 'FEB', 'JAN','MAR']
        visualization.verify_rows_label(expected,  msg="Step 20.06", label_length=4) 
        propertyobj.select_or_verify_show_prompt_item('1', 'FEB',verify=True, verify_type="true",msg="Step 20.07: Verify prompt FEB is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'JAN',verify=True, verify_type="true",msg="Step 20.08: Verify prompt JAN is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'MAR',verify=True, verify_type="true",msg="Step 20.09: Verify prompt MAR is checked")
        time.sleep(5)
                 
        """
        Step21: Close the output
        """
        visualization.switch_to_previous_window()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
        
        """
        Step22: Logout
        """
        
if __name__ == '__main__':
    unittest.main()
        