'''
Created on Apr 13, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227647
Test case Name =  Date Filter with decomposed format YYMDm
'''

import unittest, time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.locators import visualization_resultarea_locators
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon

class C2227647_TestClass(BaseTestCase):

    def test_C2227647(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227647'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)

        """
        Step 02: Double-click "Cost of Goods" and "Gross Profit", located under Sales Measures
        """
        metaobj.datatree_field_click("Cost of Goods",2,1)
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        metaobj.datatree_field_click("Gross Profit",2,1)
        
        """
        Step 03: Expand Dimension "Sales_Related" > "Trasaction Date,Components" > Double click "Sale,Year/Month"
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.datatree_field_click("Sale,Year/Month", 2, 1)
        
        """
        Step 04: Drag and drop "Sale,Year/Month" to the Filter pane
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 72)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.drag_drop_data_tree_items_to_filter("Sale,Year/Month", 1)
        time.sleep(2)   
        
        """
        Step 05: Click "From" dropdown box > select value "2014/04"
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avfFromDateComboBox div[id^='BiButton']")
        elem = '2014/04'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['2011/01', '2011/02', '2011/03', '2011/04', '2011/05', '2011/06', '2011/07', '2011/08', '2011/09', '2011/10', '2011/11', '2011/12', '2012/01', '2012/02', '2012/03', '2012/04', '2012/05', '2012/06', '2012/07', '2012/08', '2012/09', '2012/10', '2012/11', '2012/12', '2013/01', '2013/02', '2013/03', '2013/04', '2013/05', '2013/06', '2013/07', '2013/08', '2013/09', '2013/10', '2013/11', '2013/12', '2014/01', '2014/02', '2014/03', '2014/04', '2014/05', '2014/06', '2014/07', '2014/08', '2014/09', '2014/10', '2014/11', '2014/12', '2015/01', '2015/02', '2015/03', '2015/04', '2015/05', '2015/06', '2015/07', '2015/08', '2015/09', '2015/10', '2015/11', '2015/12', '2016/01', '2016/02', '2016/03', '2016/04', '2016/05', '2016/06', '2016/07', '2016/08', '2016/09', '2016/10', '2016/11', '2016/12', '2017/01', '2017/02', '2017/03'], msg='Step 05.01: Verify dialog')
        time.sleep(3)
        
        """
        Step 06: Verify Filter dialog
        Step 07: Click OK
        """
        elem=self.driver.find_element_by_css_selector("#avOperatorComboBox")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'Range',"Step 06.01: Verify Operator dialog")
        
        elem1=driver.find_element_by_css_selector("#avfFromDateComboBox")
        d=utillobj.get_attribute_value(elem1, "dom_visible_text")
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'2014/04',"Step 06.02: Verify range from value")
        
        elem1=driver.find_element_by_css_selector("#avfToDateComboBox")
        d=utillobj.get_attribute_value(elem1, "dom_visible_text")
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'2017/03',"Step 06.03: Verify range to value")  
        
        metaobj.create_visualization_filters('numeric')
        time.sleep(5)     
         
        """
        Step08: Verify Canvas 
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','2014/04',msg="Step 08.01: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','2017/03',msg="Step 08.02: Verify filter prompt range max values")
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Sale,Year/Month',1,"Step08.a:")
        time.sleep(3)
        xaxis_value="Sale Year/Month"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 08.03: Verify X-Axis Title")
        expected_xval_list=['2014/04', '2014/05', '2014/06', '2014/07', '2014/08', '2014/09', '2014/10', '2014/11', '2014/12', '2015/01', '2015/02', '2015/03', '2015/04', '2015/05', '2015/06', '2015/07', '2015/08', '2015/09', '2015/10', '2015/11', '2015/12', '2016/01', '2016/02', '2016/03', '2016/04', '2016/05', '2016/06', '2016/07', '2016/08', '2016/09', '2016/10', '2016/11', '2016/12']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08.04:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 33, 'Step 08.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08.06: Verify first bar color")
        time.sleep(5)
         
        """
        Step09: Click Run
        """
        time.sleep(8)
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
        resultobj.wait_for_property(parent_css, 33)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min','2014/04',msg="Step 10.01:Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max','2017/03',msg="Step 10.02: Verify filter prompt range max values")
        time.sleep(3)
        xaxis_value="Sale Year/Month"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10.03: Verify X-Axis Title")
        expected_xval_list=['2014/04', '2014/05', '2014/06', '2014/07', '2014/08', '2014/09', '2014/10', '2014/11', '2014/12', '2015/01', '2015/02', '2015/03', '2015/04', '2015/05', '2015/06', '2015/07', '2015/08', '2015/09', '2015/10', '2015/11', '2015/12', '2016/01', '2016/02', '2016/03', '2016/04', '2016/05', '2016/06', '2016/07', '2016/08', '2016/09', '2016/10', '2016/11', '2016/12']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10.04:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 33, 'Step 10.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.06: Verify first bar color")
        time.sleep(5)

        """
        Step 11: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
             
        """
        Step 12: Click Save in the toolbar
        Step 13: Save as "C2227645" > Click Save
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
        Step 15: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227645.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
            
        """
        Step 16: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(3)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','2014/04',msg="Step 16.01:Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','2017/03',msg="Step 16.02: Verify filter prompt range max values")
        time.sleep(3)
        metaobj.verify_filter_pane_field('Sale,Year/Month',1,"Step 16.03:")
        time.sleep(3)
        xaxis_value="Sale Year/Month"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16.04: Verify X-Axis Title")
        expected_xval_list=['2014/04', '2014/05', '2014/06', '2014/07', '2014/08', '2014/09', '2014/10', '2014/11', '2014/12', '2015/01', '2015/02', '2015/03', '2015/04', '2015/05', '2015/06', '2015/07', '2015/08', '2015/09', '2015/10', '2015/11', '2015/12', '2016/01', '2016/02', '2016/03', '2016/04', '2016/05', '2016/06', '2016/07', '2016/08', '2016/09', '2016/10', '2016/11', '2016/12']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16.05:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 33, 'Step 16.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.07: Verify first bar color")
    
        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()    