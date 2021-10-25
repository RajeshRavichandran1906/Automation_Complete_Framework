'''
Created on Sep 16, 2017

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
from selenium.webdriver import ActionChains
from common.wftools.visualization import Visualization
from common.lib.global_variables import Global_variables

class C2333394_TestClass(BaseTestCase):

    def test_C2333394(self):
        
        driver = self.driver #Driver reference object created
        visual_obj = Visualization(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2333394'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        time.sleep(5)        
                 
        """
        Step 02: Double-click "Cost of Goods" and "Gross Profit", located under Sales Measures
        """
        time.sleep(5)
        visual_obj.double_click_on_datetree_item('Cost of Goods', 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        visual_obj.double_click_on_datetree_item('Gross Profit', 1)
         
        """
        Step03: Expand Dimension "Sales_Related" > "Trasaction Date,Components" > Double click "Sale,Day"
        """
        time.sleep(5)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        visual_obj.double_click_on_datetree_item("Dimensions->Sales_Related->Transaction Date, Components->Sale,Day", 1)
                 
        """
        Step04: Drag and drop "Sale,Day" to the Filter pane
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        visual_obj.drag_and_drop_from_data_tree_to_filter("Dimensions->Sales_Related->Transaction Date, Components->Sale,Day", 1)
                
        """
        Step 05: Verify Filter dialog    Screenshot should be updated
        Step 06: Click OK      
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        
        elem=self.driver.find_element_by_css_selector("#avOperatorComboBox")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Range',"Step 05.01: Verify Operator dialog")
        
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb1 input")
        d=utillobj.get_attribute_value(elem1, "text_value")
        utillobj.asequal(d['text_value'],'Jan',"Step 05.02: Verify range from value")
        
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb2 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],'01',"Step 05.03: Verify range from value")  
        
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb3 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),2011,"Step 05.04: Verify range from value")
        
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb1 input")
        d=utillobj.get_attribute_value(elem1, "text_value")
        utillobj.asequal(d['text_value'],'Mar',"Step 05.05: Verify range to value")
        
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb2 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],'19',"Step 05.06: Verify range to value") 
         
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb3 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),2017,"Step 05.07: Verify range to value")
        
        time.sleep(2)
        metaobj.create_visualization_filters('numeric')
        
        """
        Step07: Drag left slider handle and change "From" value to 06/15/14
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(2)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser=Global_variables.browser_name
        if browser == 'firefox':
            utillobj.click_on_screen(move1, coordinate_type='start')
            utillobj.click_on_screen(move1, coordinate_type='start', click_type=0)
            time.sleep(8)
            start_point=driver.find_elements_by_css_selector("#ar_Prompt_1 div[id^='slider_'] [class^='ui-slider-handle']")
            utillobj.click_on_screen(start_point[0], coordinate_type='middle')
            utillobj.click_on_screen(start_point[0], coordinate_type='middle', click_type=0)
            time.sleep(5)
            propertyobj.move_slider_measure('#ar_Prompt_1','min', 'right', 1,'str')
            time.sleep(10)
            chart_type_css="rect[class*='riser!s0!g0!mbar']"
            elem1=(By.CSS_SELECTOR, chart_type_css)
            resultobj._validate_page(elem1)
            utillobj.click_on_screen(move1, coordinate_type='start')
            utillobj.click_on_screen(move1, coordinate_type='start', click_type=0)
            time.sleep(8)
            utillobj.click_type_using_pyautogui(move1)
            start_point=driver.find_elements_by_css_selector("#ar_Prompt_1 div[id^='slider_'] [class^='ui-slider-handle']")
            utillobj.click_on_screen(start_point[0], coordinate_type='middle')
            utillobj.click_on_screen(start_point[0], coordinate_type='middle', click_type=0)
            time.sleep(5)
            propertyobj.move_slider_measure('#ar_Prompt_1','min', 'right', 1,'str')
        else:
            action1 = ActionChains(self.driver)
            action1.move_to_element_with_offset(move1,1,1).perform()
            time.sleep(10)
            propertyobj.move_slider_measure('#ar_Prompt_1','min', 'right', 1, 'str') 
            time.sleep(10)
            propertyobj.move_slider_measure('#ar_Prompt_1','min', 'right', 1, 'str')
        time.sleep(8)
        
        """
        Step08: Verify Canvas  
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.synchronize_with_visble_text("div[id*='slider_dLOBJLOBJ']", '2013/06/26', 20)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','2013/06/26','str',msg="Step 08.01: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','2017/03/19','str',msg="Step 08.02: Verify filter prompt range values- max")
        time.sleep(2)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1284)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Sale,Day',1,"Step 08.03:")
        time.sleep(2)        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 1284, 'Step 08.04: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2013/07/09', '2013/07/10', '2013/07/11', '2013/07/12', '2013/07/13', '2013/07/14', '2013/07/15', '2013/07/16']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 08.05: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08.06: Verify first bar color")
        xaxis_value="Sale Day"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 08.07: Verify X-Axis Title")
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 08.08: Verify Y-Axis Title")

        """
        Step09: Click Run
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)
          
        """
        Step 10: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1284)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min','2013/06/26','str',msg="Step 10.01: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max','2017/03/19','str',msg="Step 10.02: Verify filter prompt range values- max")         
        time.sleep(2)
        xaxis_value="Sale Day"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10.03: Verify X-Axis Title")
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 10.04: Verify Y-Axis Title")
        expected_xval_list=['2013/07/09', '2013/07/10', '2013/07/11', '2013/07/12', '2013/07/13', '2013/07/14', '2013/07/15', '2013/07/16']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10.05:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 1284, 'Step 10.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.07: Verify first bar color")
 
        """
        Step 11: Close output window
        """
        self.driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
            
        """
        Step 12: Click Save in the toolbar
        Step 13: Save as "C2158207" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
            
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
            
        """
        Step 15: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_1',mrid='mrid',mrpass='mrpass')
                
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
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','2013/06/26','str',msg="Step 16.01: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','2017/03/19','str',msg="Step 16.02: Verify filter prompt range values- max")         
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1284)
#         parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
#         resultobj.wait_for_property(parent_css, 6)
        time.sleep(3)
        metaobj.verify_filter_pane_field('Sale,Day',1,"Step 16.03:")
        xaxis_value="Sale Day"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16.04: Verify X-Axis Title")
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 16.05: Verify Y-Axis Title")
        expected_xval_list=['2013/07/09', '2013/07/10', '2013/07/11', '2013/07/12', '2013/07/13', '2013/07/14', '2013/07/15', '2013/07/16']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16.06:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 1284, 'Step 16.07: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.08: Verify first bar color")
        time.sleep(2)

        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()