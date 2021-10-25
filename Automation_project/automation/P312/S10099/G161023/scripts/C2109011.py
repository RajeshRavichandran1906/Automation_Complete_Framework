
'''
Created on May20, 2016
@author: gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109011
'''

__author__ = "Gobizen"
__copyright__ = "IBI"

import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea
from common.lib.basetestcase import BaseTestCase 
from selenium.webdriver.common.by import By
from common.wftools.visualization import Visualization

class C2109011_TestClass(BaseTestCase):

    def test_C2109011(self):

        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2109011'
        element_css = '#queryTreeWindow'
        
        """
        CLASS OBJECTS
        """
        visual = Visualization(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/CAROLAP&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        
        The signon screen will be displayed.
        Login as userid devuser (autodevuser01/02/03/04/05) and blank password
        """
        visual.invoke_visualization_using_api('baseapp/carolap')
 
        """
        Step 02: Double click DEALER_COST, RETAIL_COST , SALES & CAR.
        """     
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        visual.wait_for_visible_text(element_css, 'DEALER_COST')   
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        visual.wait_for_visible_text(element_css, 'RETAIL_COST')
        metaobj.datatree_field_click('SALES', 2, 1)
        visual.wait_for_visible_text(element_css, 'SALES')
#         metaobj.datatree_field_click('CAR', 2, 1)  
        visual.double_click_on_datetree_item('CAR', 1)
        visual.wait_for_visible_text(element_css, 'CAR')  
        parent_css="#MAINTABLE_wbody1 g.chartPanel rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 30, 190)       
         
        """
        Step 03 : verify x and y axis labels
        """
        label_values = ['DEALER_COST', 'RETAIL_COST', 'SALES']
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "CAR",'Step 03.01: Verify X title')
        x_val_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        y_val_list=['0', '40K', '80K', '120K', '160K', '200K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 03.02: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_riser_legends('MAINTABLE_wbody1', label_values, 'Step 03.03: Verify Y title')
         
        """
        Step 04: Drag LENGTH to Tooltip bucket.
        """
        #metaobj.datatree_field_click('LENGTH',1, 1,'Add To Query','Tooltip')
        metaobj.drag_drop_data_tree_items_to_query_tree('LENGTH',1,'Tooltip',0)
        
        """
        Step 05: Verify fields added to query pane
        """
        time.sleep(6)
        metaobj.verify_query_pane_field('Vertical Axis', 'DEALER_COST', 1, 'Step 05.01: Verify DEALER_COST added to query pane')
        metaobj.verify_query_pane_field('Vertical Axis', 'RETAIL_COST', 2, 'Step 05.02: Verify RETAIL_COST added to query pane')
        metaobj.verify_query_pane_field('Vertical Axis', 'SALES', 3, 'Step 05.03: Verify SALES added to query pane')
         
        """
        Step 06 : Right click LENGTH under Tooltip > More > Aggregation Functions > Maximum.
        """
        time.sleep(6)
        metaobj.querytree_field_click('LENGTH', 1,1,'More', 'Aggregation Functions', 'Maximum')
        time.sleep(6)
        metaobj.datatree_field_click('LENGTH',1, 1,'Filter')
        time.sleep(5)
         
        """
        Step 07: Drag LENGTH to Filter pane > leave defaults > OK.
        """
        metaobj.create_visualization_filters('alpha')
        time.sleep(5)
         
        """
        Step 08 :Verify query added to filter pane.
        """
        metaobj.verify_filter_pane_field('LENGTH', 1, 'Step 08.01 :Verify filter pane has field LENGTH.')
        time.sleep(8)
         
        """
        Step 09:Verify slider range in filter prompts.
        """
        _step09 = 'Step 09.01:Verify slider range in filter prompts.'
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min', 163,'int', msg=_step09)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max', 199, 'int', msg=_step09) 
        xaxis_value="CAR"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 09.02: Verify X-Axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 30, 'Step 09.03: Verify the total number of risers displayed on Run Chart')
        x_val_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        y_val_list=['0', '40K', '80K', '120K', '160K', '200K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 09.04: X annd Y axis Scales Values has changed or NOT')
        expected_legend_list=['DEALER_COST','RETAIL_COST','SALES']
        resultobj.verify_riser_legends('MAINTABLE_wbody1', expected_legend_list, "Step 09.05: Verify Chart Legend")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 09.06: Verify first bar color")
        time.sleep(5)
        a = ['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'MAX LENGTH:177', 'Filter Chart', 'Exclude from Chart', 'Drill up to COUNTRY', 'Drill down to MODEL']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar', a,"Step 09.06: Verify bar riser values.")
        
        """
        Step 10:  Run
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Step 11: Adjust filter prompt to start at 190, expect to see 2 stack bars (BMW & JAGUAR).
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
        time.sleep(6)
        elem1=(By.CSS_SELECTOR, "#sliderPROMPT_1")
        resultobj._validate_page(elem1)
        propertyobj.move_slider_measure('#sliderPROMPT_1','min', 'right',4,'int')
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min', 191,'int', msg="Step 11.01: Verify Slider min range")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max', 199, 'int', msg="Step 11.02: Verify slider max value") 
        
        """
        Step 12: Hover over BMW blue bar.
        Verify the tool tip:
        """
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 3)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 12.01: Verify the total number of risers displayed on Run Chart')
        x_val_list=['BMW']
        y_val_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 12.02: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 12.03: Verify first bar color")
        xaxis_value="CAR"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 12.04: Verify X-Axis Title")
        expected_legend_list=['DEALER_COST','RETAIL_COST','SALES']
        resultobj.verify_riser_legends('MAINTABLE_wbody1', expected_legend_list, "Step 12.05: Verify Chart Legend")
        a = ['CAR:BMW', 'DEALER_COST:21,000', 'MAX LENGTH:195', 'Drill up to COUNTRY', 'Drill down to MODEL']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar', a,"Step 12.06: Verify bar riser values.")
        time.sleep(5)
        
        """
        Step 13 : Hover over BMW > Drill Down.
        """
        time.sleep(8)
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1','riser!s0!g0!mbar', 'Drill down to MODEL')
 
        """
        Step 14: Verify label values
        """
        time.sleep(6)
        parent_css="#MAINTABLE_wbody1 g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 6)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1','MODEL','Step 14: Verify label values after Drill Down')
         
        """
        Step 15: Hover over "3.0 SI 4 DOOR" blue bar.
        Verify the tool tip:
        """
        time.sleep(6)
        
        tooltip_value = ['MODEL:3.0 SI 4 DOOR', 'DEALER_COST:10,000', 'MAX LENGTH:195', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to CAR']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar", tooltip_value, "Step 15.01: Verify output")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 6, 'Step 15.02: Verify the total number of risers displayed on Run Chart')
        x_val_list=['3.0 SI 4 DOOR', '3.0 SI 4 DOOR AUTO']
        y_val_list=['0', '10K', '20K', '30K', '40K', '50K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 15.03: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 15.04: Verify first bar color")
        xaxis_value="MODEL"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 15.05: Verify X-Axis Title")
        expected_legend_list=['DEALER_COST','RETAIL_COST','SALES']
        resultobj.verify_riser_legends('MAINTABLE_wbody1', expected_legend_list, "Step 15.06: Verify Chart Legend")
         
        """
        Step 16: Close the output window
        """
        visual.switch_to_previous_window()
         
        """
        Step 17 : Click "Save" in the toolbar > Type C2109011 > Click "Save" in the Save As dialog
        """
        utillobj.synchronize_until_element_is_visible("#applicationButton img", 90)
        visual.save_visualization_from_top_toolbar(Test_Case_ID)
        
        """
        Step 18 : Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()