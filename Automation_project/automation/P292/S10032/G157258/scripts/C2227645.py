'''
Created on Apr 13, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227645
Test case Name =  Date Filter with decomposed date format YYMDy
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.wftools.visualization import Visualization

class C2227645_TestClass(BaseTestCase):

    def test_C2227645(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227645'
        
        """
        TESTCASE CSS
        """
        qwery_tree_css = "#queryTreeWindow"
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visualization = Visualization(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        visualization.wait_for_visible_text("#pfjTableChart_1", "Drop")

        """
        Step 02: Double-click "Cost of Goods" and "Gross Profit", located under Sales Measures
        """
        visualization.double_click_on_datetree_item("Cost of Goods", 1)
        visualization.wait_for_visible_text(qwery_tree_css, "Cost of Goods")
        
        visualization.double_click_on_datetree_item("Gross Profit", 1)
        visualization.wait_for_visible_text(qwery_tree_css, "Gross Profit")
        
        """
        Step 03: Expand Dimension "Sales_Related" > "Trasaction Date,Components" > Double click "Sale,Year"
        """
        visualization.double_click_on_datetree_item("Sale,Year", 1)
        visualization.wait_for_visible_text(qwery_tree_css, "Sale,Year")
        
        """
        Step 04: Drag and drop "Sale,Year" to the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter('Sale,Year', 1)
        visualization.wait_for_visible_text("#avFilterCancelBtn", "Cancel")
         
        """
        Step 05: Verify Filter dialog
        Step 06: Click OK
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(3)
        
        elem=self.driver.find_element_by_css_selector("#avAggregationComboBox")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'(None)',"Step 05.01 : Verify Aggregation in Filter dialog")
        
        elem=self.driver.find_element_by_css_selector("#avOperatorComboBox")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'Range',"Step 05.02 : Verify Operator dialog")
        
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        print(d['int_value'])
        utillobj.asequal(d['int_value'],"2011","Step 05.03 : Verify range to value")
        
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        print(d['int_value'])
        utillobj.asequal(d['int_value'],"2017","Step 05.04 : Verify range to value")  
        time.sleep(2)
        metaobj.create_visualization_filters('numeric')
        time.sleep(5)
         
        """
        Step07: Verify Canvas 
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, visualization.home_page_long_timesleep)
        time.sleep(5)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2011,'int',msg="Step 07.01 : Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',2017,'int',msg="Step 07.02 : Verify filter prompt range max values")
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, visualization.home_page_long_timesleep)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, visualization.home_page_long_timesleep)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Sale,Year',1,"Step 07.03 :")
        time.sleep(3)
        xaxis_value="Sale Year"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 07.04 : Verify X-Axis Title")
        expected_xval_list=['2011', '2012', '2013', '2014', '2015', '2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 07.05 : Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 07.06 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.07 : Verify first bar color")
        time.sleep(5)
        #bar=['Sale Year:2016', 'Cost of Goods:$325,821,316.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        #resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g5!mbar", bar, "Step 07.d: Verify bar value")
        time.sleep(5)
         
        """
        Step08: Drag left slider handle to the right > change "From" value to 2014
        """
        visualization.drag_minimum_value_slider_in_filter_prompt('2014')
        
        """
        Step09: Verify Canvas 
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 3, visualization.home_page_long_timesleep)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, visualization.home_page_long_timesleep)
        browser=utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2014,'int',msg="Step 09.01 : Verify filter prompt range min values")
        if browser in ['IE', 'Chrome']:
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2014,'int',msg="Step 09.01 : Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',2017,'int',msg="Step 09.02 : Verify filter prompt range max values")
        metaobj.verify_filter_pane_field('Sale,Year',1,"Step 09.03 :")
        time.sleep(3)
        xaxis_value="Sale Year"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 09.04 : Verify X-Axis Title")
        expected_xval_list=['2014', '2015', '2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09.05 :Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 3, 'Step 09.06 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09.07 : Verify first bar color")
        time.sleep(5)
         
        """
        Step10: Click Run
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        visualization.switch_to_new_window()
        visualization.wait_for_visible_text("#MAINTABLE_wbody1", "Cost")
           
        """
        Step 11: Verify output
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 3, visualization.home_page_long_timesleep)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, visualization.home_page_long_timesleep)
        if browser == 'Firefox':
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',2014,'int',msg="Step 11.01 :Verify filter prompt range min values")
        if browser in ['IE', 'Chrome']:
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',2014,'int',msg="Step 11.01 : Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',2017,'int',msg="Step 11.02 : Verify filter prompt range max values")
        time.sleep(3)
        xaxis_value="Sale Year"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 11.03 : Verify X-Axis Title")
        expected_xval_list=['2014', '2015', '2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11.04 : Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 3, 'Step 11.05 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.06 : Verify first bar color")
        time.sleep(20)

        """
        Step 12: Close output window
        """
        visualization.switch_to_previous_window()
        visualization.wait_for_visible_text("#MAINTABLE_wbody1", "Cost")
        
        """
        Step 13: Click Save in the toolbar
        Step 14: Save as "C2227645" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        visualization.wait_for_visible_text('#IbfsOpenFileDialog7_btnCancel', "Cancel")
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.synchronize_until_element_disappear("#IbfsOpenFileDialog7_btnCancel", visualization.home_page_short_timesleep)
        
        """
        Step 15: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
             
        """
        Step 16: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227645.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
            
        """
        Step 17: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 3, visualization.home_page_long_timesleep)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, visualization.home_page_long_timesleep)
        if browser == 'Firefox':
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2014,'int',msg="Step 17.01 :Verify filter prompt range min values")
        if browser in ['IE', 'Chrome']:
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2014,'int',msg="Step 17.01 : Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',2017,'int',msg="Step 17.02 : Verify filter prompt range max values")
        time.sleep(3)
        metaobj.verify_filter_pane_field('Sale,Year',1,"Step 17.03 :")
        time.sleep(3)
        xaxis_value="Sale Year"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 17.04 : Verify X-Axis Title")
        expected_xval_list=['2014', '2015', '2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 17.05 :Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 3, 'Step 17.06 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 17.07 : Verify first bar color")
        time.sleep(5)
         
        """
        Step 18: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()