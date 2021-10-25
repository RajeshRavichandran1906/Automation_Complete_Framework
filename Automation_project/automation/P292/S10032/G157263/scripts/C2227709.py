'''
Created on Jun 13, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227709
TestCase Name = Data pane Values context menu
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, visualization_properties
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase

class C2227709_TestClass(BaseTestCase):

    def test_C2227709(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227709'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Expand "Product" Dimension
        Step 03: Expand "Values > Computers > Tablet" > verify list of values
        """
        time.sleep(3)
        metaobj.expand_field_tree('Dimensions->Product->Product->Values->Computers->Tablet')
        time.sleep(6)
        items_list = ['GLXYT10716','GLXYT10732','GLXYT3B','GLXYT3W','GLXYT70','SGP311U1/B','SGP312U1/B','SGPT121US/S','SGPT122US/S','SGPT123US/S'] 
        metaobj.verify_fields_in_datatree('Tablet', items_list, 'step 03: verify list of values in datatree')
        
        """
        Step 04: Right-click "GLXYT10716" > verify menu
        Step 05: Select "Filter"
        """
        time.sleep(6)
        metaobj.expand_field_tree('GLXYT10716', click_opt=1, x_offset=35)
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Filter', verify='true', expected_popup_list=['Filter'], msg='Step 04: Verify popup menu')
        time.sleep(6)
        
        """
        Step 06: Verify Preview
        """
        resultobj.wait_for_property('#TableChart_1', 1)
        obj=driver.find_element_by_css_selector("#TableChart_1 text[class^='title']").text.strip()
        print(obj)
        utillobj.asequal(obj,"Drop Measures or Sorts into the Query Pane","Step06: Verify Preview")
        time.sleep(4)
        metaobj.verify_filter_pane_field('Model',1,"Step06:")
        time.sleep(4)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item(1, 'GLXYT10716', verify=True, verify_type=True, msg="Step06: Verify GLXYT10716 is checked in filter prompt", scroll_down=True)
        time.sleep(5)
        
        """
        Step 07: Check off values in the Filter Prompt:
        B00D7MOHDO
        BCG34HRE4KN
        BOSE AM10IV
        """
        propertyobj.select_or_verify_show_prompt_item(1, 'B00D7MOHDO', scroll_down=True)
        propertyobj.select_or_verify_show_prompt_item(1, 'BCG34HRE4KN')
        propertyobj.select_or_verify_show_prompt_item(1, 'BOSE AM10IV')
        
        """
        Step 08: Double-click "Model", from Product Dimension
        """
        metaobj.datatree_field_click('Model', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 4)
        
        """
        Step 09: Double-click "Cost of Goods"
        """
        time.sleep(5)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 4)
        
        """
        Step 10: Verify Preview
        """
        resultobj.wait_for_property('#MAINTABLE_wbody1', 1)
        time.sleep(6)
        metaobj.verify_filter_pane_field('Model',1,"Step10:")
        xaxis_value="Model"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step10:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step10:a(ii) Verify Y-Axis Title")
        expected_xval_list=['B00D7MOHDO', 'BCG34HRE4KN', 'BOSE AM10IV', 'GLXYT10716']
        expected_yval_list=['0', '3M', '6M', '9M', '12M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar", "bar_blue", "Step 10.c: Verify first bar color")
        time.sleep(3)
        bar=['Model:BOSE AM10IV', 'Cost of Goods:$11,092,770.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar, "Step 10.d: Verify bar value")
        time.sleep(5)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item(1, 'B00D7MOHDO', verify=True, verify_type=True, msg="Step10: Verify B00D7MOHDO is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'BCG34HRE4KN', verify=True, verify_type=True, msg="Step10: Verify BCG34HRE4KN is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'BOSE AM10IV', verify=True, verify_type=True, msg="Step10: Verify BOSE AM10IV is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'GLXYT10716', verify=True, verify_type=True, msg="Step10: Verify GLXYT10716 is checked in filter prompt", scroll_down=True)
        
        """
        Step11: Click Run > Verify output
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 4)
        xaxis_value="Model"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step11:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step11:a(ii) Verify Y-Axis Title")
        expected_xval_list=['B00D7MOHDO', 'BCG34HRE4KN', 'BOSE AM10IV', 'GLXYT10716']
        expected_yval_list=['0', '3M', '6M', '9M', '12M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar", "bar_blue", "Step 11.c: Verify first bar color")
        time.sleep(3)
        bar=['Model:BOSE AM10IV', 'Cost of Goods:$11,092,770.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar, "Step 11.d: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227709_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(1, 'B00D7MOHDO', verify=True, verify_type=True, msg="Step11: Verify B00D7MOHDO is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'BCG34HRE4KN', verify=True, verify_type=True, msg="Step11: Verify BCG34HRE4KN is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'BOSE AM10IV', verify=True, verify_type=True, msg="Step11: Verify BOSE AM10IV is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'GLXYT10716', verify=True, verify_type=True, msg="Step11: Verify GLXYT10716 is checked in filter prompt", scroll_down=True)
        
        """
        Step 12: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        resultobj.wait_for_property("#applicationButton img", 1)
         
        """
        Step 13: Click Save in the toolbar
        Step 14: Save as "C2227709" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
           
        """
        Step 15: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
                
        """
        Step 16: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227709.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
               
        """
        Step 17: Verify Preview 
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Model',1,"Step17:")
        xaxis_value="Model"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step17:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step17:a(ii) Verify Y-Axis Title")
        expected_xval_list=['B00D7MOHDO', 'BCG34HRE4KN', 'BOSE AM10IV', 'GLXYT10716']
        expected_yval_list=['0', '3M', '6M', '9M', '12M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 17:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 17.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar", "bar_blue", "Step 17.c: Verify first bar color")
        time.sleep(3)
        bar=['Model:BOSE AM10IV', 'Cost of Goods:$11,092,770.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar, "Step 17.d: Verify bar value")
        time.sleep(5)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item(1, 'B00D7MOHDO', verify=True, verify_type=True, msg="Step17: Verify B00D7MOHDO is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'BCG34HRE4KN', verify=True, verify_type=True, msg="Step17: Verify BCG34HRE4KN is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'BOSE AM10IV', verify=True, verify_type=True, msg="Step17: Verify BOSE AM10IV is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'GLXYT10716', verify=True, verify_type=True, msg="Step17: Verify GLXYT10716 is checked in filter prompt", scroll_down=True)
        time.sleep(5)
        
        """
        Step 18: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()