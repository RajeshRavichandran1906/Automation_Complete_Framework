'''
Created on Jun 06, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227706
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, metadata
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2227706_TestClass(BaseTestCase):

    def test_C2227706(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227706'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        new_metaobj = metadata.MetaData(self.driver)
        
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
   
        """
        Step02: Expand 'Query Variables' in the Data pane
        Step03: Right-click "Web Store" filter > verify menu
        Step04: Select "Filter".
        """
        time.sleep(6)
        metaobj.expand_field_tree('Query Variables')
        time.sleep(2)
        metaobj.expand_field_tree('Query Variables')
        time.sleep(2)
        metaobj.expand_field_tree('Web Store', click_opt=1, x_offset=50)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=['Filter'],msg='Step03: Verify popup menu')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Filter')
        time.sleep(6)
        
        """
        Step05: Verify filter is created in the Filter pane
        """
        parent_css="#qbFilterBox"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.verify_filter_pane_field('Web Store', 1, "Step05: Verify Filter created")
        
        """
        Step06: Right-click "Web Store" in the Filter pane > verify menu
        Step07: Select "Edit..."
        """
        time.sleep(2)
        metaobj.filter_tree_field_click("Web Store", 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=['Edit...', 'Show Prompt','Delete'],msg='Step06: Verify popup menu')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Edit...')
        time.sleep(2) 
          
        """
        Step08: Verify dialog > click Cancel
        """        
        obj=self.driver.find_element_by_css_selector("[id*='QbDialog'] div[id*='BiLabel']")
        utillobj.asequal(obj.text,"Filter for Web Store", "Step08: Verify message is displayed")
        time.sleep(2)
        try:
            elem=self.driver.find_element_by_css_selector("#rBtnTrue input")        
            utillobj.asequal(elem.get_attribute('checked'),"true", "Step08: Verify true is checked")
        except:
            print("True radio button not present")
        time.sleep(2)
        metaobj.create_visualization_filters('alpha',ok=False)
        time.sleep(2)

        """
        Step09: Right-click "Web Store" in the Filter pane > select "Show Prompt"
        Step10: Verify Prompt is displayed
        """
        time.sleep(2)
        metaobj.filter_tree_field_click("Web Store", 1, 1,'Show Prompt')
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item(1, 'true', verify=True, verify_type=True, msg="Step10: Verify 2014 is checked in filter prompt")

        """
        Step11: Double-click "Store Name", from Store Dimension
        """
        time.sleep(4)
        new_metaobj.double_click_on_data_filed('Dimensions->Store->Store->Store Name', 2)
                    
        """
        Step12: Double-click "Cost of Goods", from Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2227706_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
 
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
                 
        """
        Step13: Click Save in the toolbar
        Step14: Save as "C2158261" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
                 
        """
        Step15: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)  
         
        """
        Step16: Reopen
        Step17: Verify canvas
        """ 
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(2)
                  
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        xaxis_value="Store Name"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step17:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step17:a(i) Verify Y-Axis Title")
        expected_xval_list=['Web']
        expected_yval_list=['0', '40M','80M','120M','160M','200M','240M','280M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step17:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step17.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step17.c: Verify first bar color")
        time.sleep(5)
        bar=['Store Name:Web', 'Cost of Goods:$234,676,170.00','Drill up to Store Postal Code']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step17: Verify bar value")
        time.sleep(5) 
 

if __name__ == '__main__':
    unittest.main()



    
     
        