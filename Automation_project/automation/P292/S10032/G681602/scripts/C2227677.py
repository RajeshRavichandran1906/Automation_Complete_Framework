'''
Created on Apr 7, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227677
Test case Name =  Filter Aggregation - Median
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.wftools.visualization import Visualization

class C2227677_TestClass(BaseTestCase):

    def test_C2227677(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227677'
        
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
        query_tree_css = "#queryTreeWindow"
        
        """
        Step 01: Launch the IA API with car, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','ibisamp/car','P292/S10032_visual_1', 'mrid', 'mrpass')
        visualization.wait_for_visible_text("#pfjTableChart_1", "Drop")
    
        """
        Step 02: Double-click "Dealer_Cost"
        """
        visualization.double_click_on_datetree_item("DEALER_COST", 1)
        visualization.wait_for_visible_text(query_tree_css, "DEALER_COST")
            
        """
        Step 03: Double-click "Car"
        """
        visualization.double_click_on_datetree_item("CAR", 1)
        visualization.wait_for_visible_text(query_tree_css, "CAR")
            
        """
        Step04: Drag and drop "Dealer_Cost" to the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter("DEALER_COST", 1)  
        visualization.wait_for_visible_text("#avFilterCancelBtn", "Cancel")
        
        """
        Step05: Click "Aggregation" dropdown menu > Select "Median"
        Step06: Verify Filter dialog
        Step07: Click OK
        """ 
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        elem=self.driver.find_element_by_css_selector("#avAggregationComboBox")
        combo=['(None)', 'Sum', 'Average', 'Count', 'Distinct Count', 'Maximum', 'Minimum', 'Percent', 'Median']
        utillobj.select_any_combobox_item(elem,'Median',verify=True,expected_combobox_list=combo, msg="Step 05.01 : Verify list of aggregation functions")
        time.sleep(8)   
         
        elem=self.driver.find_element_by_css_selector("#avAggregationComboBox div")
        d=utillobj.get_attribute_value(elem,'text')
        print(d)
        print(d['text'])
        utillobj.asequal(d['text'],'Median',"Step 06.01 : Verify Aggregation in Filter dialog")
             
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"2626","Step 06.02 : Verify From in Filter dialog")
             
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"25000","Step 06.03 : Verify To in Filter dialog")
             
        metaobj.create_visualization_filters('numeric')
        time.sleep(3)  
        
        """
        Step 08: Verify Canvas
        """
        time.sleep(6)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.verify_filter_pane_field('MDN (DEALER_COST)',1,"Step 07.01 :")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2626,'int',msg="Step 08.01 : Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',25000,'int',msg="Step 08.02 : Verify filter prompt range max values")
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 10)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        xaxis_value="CAR"
        yaxis_value="DEALER_COST"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 08.03 : Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 08.04 : Verify Y-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08.05 :Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 10, 'Step 08.06 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar", "bar_blue", "Step 08.07 : Verify first bar color")
        time.sleep(5)
        
        """
        Step09: Drag left slider handle in the filter Prompt to the right > "14810"
        """
        visualization.drag_minimum_value_slider_in_filter_prompt(11705)
        
        """
        Step 10: Verify Canvas
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        metaobj.verify_filter_pane_field('MDN (DEALER_COST)',1,"Step 10.01 :")
        time.sleep(2)
        xaxis_value="CAR"
        yaxis_value="DEALER_COST"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10.02 : Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10.03 : Verify Y-Axis Title")
        expected_xval_list=['JENSEN', 'MASERATI']
        expected_yval_list=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10.04 : Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 10.05 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.06 : Verify first bar color")
        time.sleep(5)
        
        """
        Step11: Click Save in the toolbar
        Step12: Save as "C2158189" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        visualization.wait_for_visible_text('#IbfsOpenFileDialog7_btnCancel', "Cancel")
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.synchronize_until_element_disappear("#IbfsOpenFileDialog7_btnCancel", visualization.home_page_short_timesleep)
             
        """
        Step13: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
             
        """
        Step14: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158198.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Sep15: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        time.sleep(3)
        metaobj.verify_filter_pane_field('MDN (DEALER_COST)',1,"Step 15.01 :")
        time.sleep(5)  
        xaxis_value="CAR"
        yaxis_value="DEALER_COST"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 15.02 : Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 15.03 : Verify Y-Axis Title")
        expected_xval_list=['JENSEN', 'MASERATI']
        expected_yval_list=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 15.04 :Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 15.05 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 15.06 : Verify first bar color")
        time.sleep(5)
        
        """
        Step 16: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()