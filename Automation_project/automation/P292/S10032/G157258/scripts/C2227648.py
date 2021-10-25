'''
Created on Apr 20, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227648
TestCase Name = Date Filter with decomposed date format YYMD
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from datetime import datetime

class C2227648_TestClass(BaseTestCase):

    def test_C2227648(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227648'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        time.sleep(5)        
                 
        """
        Step 02: Double-click "Cost of Goods" and "Gross Profit", located under Sales Measures
        """
        time.sleep(5)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        metaobj.datatree_field_click('Gross Profit', 2, 1)
         
        """
        Step03: Expand Dimension "Sales_Related" > "Trasaction Date,Components" > Double click "Sale,Day"
        """
        time.sleep(5)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.datatree_field_click('Sale,Day', 2, 2)
                 
        """
        Step04: Drag and drop "Sale,Day" to the Filter pane
        """
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1000)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        metaobj.drag_drop_data_tree_items_to_filter('Dimensions->Sales_Related->Transaction Date, Components->Sale,Day', 1)
#         metaobj.datatree_field_click('Sale,Day', 1, 2, 'Filter')
                
        """
        Step 05: Verify Filter dialog    Screenshot should be updated
        Step 06: Click OK      
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        
        elem=self.driver.find_element_by_css_selector("#avOperatorComboBox")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Range',"Step05.a: Verify Operator dialog")
        
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb1 input")
        d=utillobj.get_attribute_value(elem1, "text_value")
        utillobj.asequal(d['text_value'],'Jan',"Step05.1: Verify range from value")
        
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb2 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],'01',"Step05.2: Verify range from value")  
        
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb3 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),2011,"Step05.3: Verify range from value")
        
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb1 input")
        d=utillobj.get_attribute_value(elem1, "text_value")
        utillobj.asequal(d['text_value'],'Mar',"Step05.4: Verify range to value")
        
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb2 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],'19',"Step05.5: Verify range to value") 
         
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb3 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),2017,"Step05.6: Verify range to value")
        
        time.sleep(2)
        metaobj.create_visualization_filters('numeric')
        
        """
        Step07: Drag left slider handle and change "From" value to 06/15/14
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(2)
        propertyobj.move_slider_measure('#ar_Prompt_1','min', 'right', 1, 'str') 
        time.sleep(5)
        propertyobj.move_slider_measure('#ar_Prompt_1','min', 'right', 1, 'str')
        time.sleep(8)
        
        """
        Step08: Verify Canvas  
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        browser=utillobj.parseinitfile('browser')
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','07/12/2013','str',msg="Step08: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','03/19/2017','str',msg="Step08: Verify filter prompt range values- max")
        time.sleep(2)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1000)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Sale,Day',1,"Step08.a:")
        time.sleep(2)        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 1000, 'Step08a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2013/07/09', '2013/07/10', '2013/07/11', '2013/07/12', '2013/07/13', '2013/07/14', '2013/07/15', '2013/07/16']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        print(str(datetime.now()))
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step08b: X and Y axis Scales Values has changed or NOT')
        print(str(datetime.now()))
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step08.c(i) Verify first bar color")
        xaxis_value="Sale Day"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step08:d(i) Verify X-Axis Title")
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step08:d(ii) Verify Y-Axis Title")
        time.sleep(2)
        browser=utillobj.parseinitfile('browser')
        if browser=='Firefox':
            expected_tooltip=['Sale Day:2013/07/12', 'Cost of Goods:$160,296.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year/Month']
        else:
            expected_tooltip=['Sale Day:2013/06/26', 'Cost of Goods:$143,962.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year/Month']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step08e: verify the default tooltip values", browser_height=80, x_offset=0, y_offset=-10)      
        time.sleep(10)
         
        """
        Step09: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
          
        """
        Step 10: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1000)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        browser=utillobj.parseinitfile('browser')
        if browser=='Firefox':
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min','2013/07/12','str',msg="Step10: Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max','2017/03/19','str',msg="Step10: Verify filter prompt range values- max")
        else:
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min','2013/06/26','str',msg="Step10: Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max','2017/03/19','str',msg="Step10: Verify filter prompt range values- max")         
        time.sleep(2)
        xaxis_value="Sale Day"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10:a(i) Verify X-Axis Title")
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step10:d(ii) Verify Y-Axis Title")
        expected_xval_list=['2013/07/09', '2013/07/10', '2013/07/11', '2013/07/12', '2013/07/13', '2013/07/14', '2013/07/15', '2013/07/16']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        print(str(datetime.now()))
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10:a(iii):Verify XY labels")
        print(str(datetime.now()))
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 1000, 'Step 10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.c: Verify first bar color")
        time.sleep(5)
        browser=utillobj.parseinitfile('browser')
        if browser=='Firefox':
            expected_tooltip=['Sale Day:2013/07/12', 'Cost of Goods:$160,296.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year/Month']
        else:
            expected_tooltip=['Sale Day:2013/06/26', 'Cost of Goods:$143,962.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year/Month']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", expected_tooltip, "Step 10.d: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step10_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 11: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
            
        """
        Step 12: Click Save in the toolbar
        Step 13: Save as "C2158207" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
            
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
            
        """
        Step 15: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
        
        
        """
        Step 16: Verify Canvas and Filter pane
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(2)        
        browser=utillobj.parseinitfile('browser')
        if browser=='Firefox':
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','2013/07/12','str',msg="Step16: Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','2017/03/19','str',msg="Step16: Verify filter prompt range values- max")
        else:
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','2013/06/26','str',msg="Step16: Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','2017/03/19','str',msg="Step16: Verify filter prompt range values- max")         
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1000)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(3)
        metaobj.verify_filter_pane_field('Sale,Day',1,"Step24.b:")
        xaxis_value="Sale Day"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16:a(i) Verify X-Axis Title")
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step16:a(ii) Verify Y-Axis Title")
        expected_xval_list=['2013/07/09', '2013/07/10', '2013/07/11', '2013/07/12', '2013/07/13', '2013/07/14', '2013/07/15', '2013/07/16']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        print(str(datetime.now()))
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16:a(iii):Verify XY labels")
        print(str(datetime.now()))
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 1000, 'Step 16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.c: Verify first bar color")
        time.sleep(2)
        browser=utillobj.parseinitfile('browser')
        if browser=='Firefox':
            expected_tooltip=['Sale Day:2013/07/12', 'Cost of Goods:$160,296.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year/Month']
        else:
            expected_tooltip=['Sale Day:2013/06/26', 'Cost of Goods:$143,962.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year/Month']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", expected_tooltip, "Step 16.d: Verify bar value")
        time.sleep(5)
        
        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()