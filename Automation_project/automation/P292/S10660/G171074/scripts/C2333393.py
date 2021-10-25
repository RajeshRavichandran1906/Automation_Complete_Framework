'''
Created on Sep 16, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2333393
Test case Name =  Date Filter with decomposed date format YYMDq
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity, core_utility


class C2333393_TestClass(BaseTestCase):

    def test_C2333393(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2333393'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']", metaobj.chart_long_timesleep)

        """
        Step 02: Double-click "Cost of Goods" and "Gross Profit", located under Sales Measures
        """
        metaobj.datatree_field_click("Cost of Goods",2,1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, metaobj.chart_long_timesleep)
        metaobj.datatree_field_click("Gross Profit",2,1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, metaobj.chart_long_timesleep)
        
        """
        Step 03: Expand Dimension "Sales_Related" > "Trasaction Date,Components" > Double click "Sale,Year/Quarter"
        """
        metaobj.datatree_field_click("Sale,Year/Quarter", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 24, metaobj.chart_long_timesleep)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, metaobj.chart_long_timesleep)
        
        """
        Step 04: Drag and drop "Sale,Year/Quarter" to the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter("Sale,Year/Quarter", 1)
        
        """
        Step 05: Verify Filter dialog
        Step 06: Click OK
        """
        utillobj.synchronize_until_element_is_visible("#avOperatorComboBox", metaobj.chart_long_timesleep)
        
        elem=self.driver.find_element_by_css_selector("#avOperatorComboBox")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Range',"Step 05.01: Verify Operator dialog")
        
        elem1=driver.find_element_by_css_selector("#avfFromDateComboBox")
        d=utillobj.get_attribute_value(elem1, 'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'2011 Q1',"Step 05.02: Verify range from value")
        
        elem1=driver.find_element_by_css_selector("#avfToDateComboBox")
        d=utillobj.get_attribute_value(elem1, 'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'2017 Q1',"Step 05.03: Verify range to value")  
        
        metaobj.create_visualization_filters('numeric')
        
        """
        Step07: Verify Canvas 
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        utillobj.synchronize_until_element_is_visible(parent_css, metaobj.chart_long_timesleep)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','2011 Q1',msg="Step 07.01: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','2017 Q1',msg="Step 07.02: Verify filter prompt range max values")
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Sale,Year/Quarter',1,"Step 07.03")
        xaxis_value="Sale Year/Quarter"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 07.04: Verify X-Axis Title")
        expected_xval_list=['2011 Q1', '2011 Q2', '2011 Q3', '2011 Q4', '2012 Q1', '2012 Q2', '2012 Q3', '2012 Q4', '2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 07.05: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 24, 'Step 07.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.07: Verify first bar color")
        
        """
        Step 08: Right click "Sale,Year/Quarter" filter in the Filter pane > Select Edit
        """
        metaobj.filter_tree_field_click('Sale,Year/Quarter',1,1,'Edit...')
        
        """
        Step09: Click "From" dropdown box > verify list of values
        Step10: Select "2013 Q4" > click OK
        """
        utillobj.synchronize_until_element_is_visible('#avFilterOkBtn', metaobj.chart_long_timesleep)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avfFromDateComboBox div[id^='BiButton']")
        elem = '2013 Q4'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['2011 Q1', '2011 Q2', '2011 Q3', '2011 Q4', '2012 Q1', '2012 Q2', '2012 Q3', '2012 Q4', '2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4', '2017 Q1'], msg='Step 09.01: Verify dialog')
        time.sleep(3)
        metaobj.create_visualization_filters('numeric')
        time.sleep(5)
                
        """
        Step11: Verify Canvas 
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        utillobj.synchronize_until_element_is_visible(parent_css, metaobj.chart_long_timesleep)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','2013 Q4',msg="Step 11.01: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','2017 Q1',msg="Step 11.02: Verify filter prompt range max values")
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Sale,Year/Quarter',1,"Step 11.03")
        xaxis_value="Sale Year/Quarter"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 11.04: Verify X-Axis Title")
        expected_xval_list=['2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11.05: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 13, 'Step 11.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.07: Verify first bar color")
      
        """
        Step12: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window()
          
        """
        Step 13: Verify output
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, metaobj.chart_long_timesleep)
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min','2013 Q4',msg="Step 13.01: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max','2017 Q1',msg="Step 13.02: Verify filter prompt range max values")
        xaxis_value="Sale Year/Quarter"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 13.03: Verify X-Axis Title")
        expected_xval_list=['2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 13.04: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 13, 'Step 13.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 13.06: Verify first bar color")
   
        """
        Step 14: Close output window
        """
        core_utilobj.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible("#applicationButton img", metaobj.home_page_long_timesleep)
            
        """
        Step 15: Click Save in the toolbar
        Step 16: Save as "C2158206" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", metaobj.home_page_medium_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
            
        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
            
        """
        Step 18: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_1',mrid='mrid',mrpass='mrpass')
           
        """
        Step 19: Verify Canvas
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, metaobj.chart_long_timesleep)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','2013 Q4',msg="Step 19.01: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','2017 Q1',msg="Step 19.02: Verify filter prompt range max values")
        metaobj.verify_filter_pane_field('Sale,Year/Quarter',1,"Step 19.03")
        xaxis_value="Sale Year/Quarter"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 19.04: Verify X-Axis Title")
        expected_xval_list=['2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 19.05: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 13, 'Step 19.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 19.07: Verify first bar color")

        """
        Step 20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()