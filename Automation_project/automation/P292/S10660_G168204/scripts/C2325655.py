'''
Created on Oct 12, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325655
TestCase Name = Verify converting Bar chart with Drill Down to Ring Pie to Scatter chart types
'''

import unittest, time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea
from common.locators import visualization_resultarea_locators
from common.lib import utillity

class C2325655_TestClass(BaseTestCase):

    def test_C2325655(self):
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2325655'

        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10660_visual_2', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
           
        """
        Step02: Double-click "Cost of Goods" from Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1) 
                       
        """
        Step03: Double-click "Product,Category", located under Product Dimension
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
           
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step03:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step03:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step03:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step03.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step03.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step03: Verify bar value")
        time.sleep(5)
           
        """
        Step04: Select "Cost of Goods" in the Query pane > Click on "Drill Down" button in the Ribbon
        """
        metaobj.querytree_field_click("Cost of Goods", 1)
        time.sleep(5)
        parent_css="#FieldDrillDown img"
        resultobj.wait_for_property(parent_css, 1)
        ribbon_item=driver.find_element_by_css_selector("#FieldDrillDown img")
        utillobj.default_left_click(object_locator=ribbon_item)
         
        """
        Step05: Select "Web Page"
        Step06: Type URL http://www.ibi.com
        Step07: Click "OK"
        """
        time.sleep(8)
        parent_css="div[id^='QbDialog'] div[id^='IABottomBar'] #ok"
        resultobj.wait_for_property(parent_css, 1)
        iaribbonobj.create_drilldown_report("webpage", url_value="http://www.ibi.com", click_ok=True)
         
        """
        Step08: Hover over "Accessories" riser > Verify "Drill Down 1" is displayed in the pop up menu
        """
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step08:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step08:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step08:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step08.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory', 'Drill Down 1']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step08: Verify drill down to 'Drill Down 1' is displayed in the pop up menu")
        time.sleep(5)
         
        """
        Step09: Select the "Change" button in the Home Tab ribbon > Select "Ring Pie" chart type
        """
        ribbonobj.change_chart_type('ring_pie')
        time.sleep(5)
         
        """
        Step10: Hover over "Stereo Systems" area in the Ring Pie > Verify "Drill Down 1" is displayed in the pop up menu
        """
        parent_css="#MAINTABLE_wbody1 svg g path[class*='riser']"
        resultobj.wait_for_property(parent_css, 7)
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g0!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Cost of Goods',"Step10.a Verify X-axis label")
        resultobj.verify_number_of_pie_segments("MAINTABLE_wbody1", 1, 7, 'Step 10.b: Verify the total number of pie segments displayed on pie Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s4!g0!mwedge", "brick_red", "Step10.c: Verify first piesegment color")
        legend=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step10.d: Verify Legends Title")
        time.sleep(5)
        bar=['Product Category:Stereo Systems', 'Cost of Goods:$205,113,863.00  (26.94%)', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory', 'Drill Down 1']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s4!g0!mwedge", bar,"Step10.e: Verify drill down to 'Drill Down 1' is displayed in the pop up menu")
        time.sleep(5)
         
        """
        Step11: Select "Drill Down 1"
        """
        time.sleep(5)
        resultobj.select_drilldown_tooltip_menu("MAINTABLE_wbody1", "riser!s4!g0!mwedge", 'Drill Down 1')
        time.sleep(8)
         
        """
        Step12: Verify Information Builders Web page is displayed in a new window (or tab)
        """
        utillobj.switch_to_window(1,window_title='Business')
        time.sleep(15)
        elem=(By.CSS_SELECTOR,"[class*=top-bar-title] [id^='branding'] a img")
        resultobj._validate_page(elem)
        alternate_text=driver.find_element_by_css_selector("[class*=top-bar-title] [id^='branding'] a img").get_attribute('alt')
        print(alternate_text)
        utillobj.asequal('logo',alternate_text,'Step 12: Verify Information Builders Web page is displayed in a new window (or tab)')
        time.sleep(8)
        ele=driver.find_element_by_css_selector("#page_wrapper")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """
        Step13: Close the output winow
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 14: Select the "Change" button in the Home Tab ribbon > Select "Scatter" chart type
        """
        ribbonobj.change_chart_type("scatter")
        time.sleep(5)
         
        """
        Step15: Hover over "Computers" point in the Scatter chart > Verify "Drill Down 1" is displayed in the pop up menu
        """
        time.sleep(5)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        yaxis_value="Cost of Goods"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step15.a: Verify Y-Axis Title")
        expected_xval_list=[]
        expected_yval_list=['0', '40M','80M','120M','160M','200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step15.b:Verify XY labels")
        ia_resultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 7, 'Step 15.c: Verify number of scatter displayed',custom_css="svg g circle[class^='riser']")
        legend=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step15.d: Verify Legends Title")
        time.sleep(5)
        expected_tooltip=['Cost of Goods:$69,807,664.00', 'Product Category:Computers', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory', 'Drill Down 1']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s2!g0!mmarker!",expected_tooltip, "Step15.e: verify the default tooltip values")
          
        """
        Step16: Select "Drill Down 1"
        """
        time.sleep(5)
        resultobj.select_drilldown_tooltip_menu("MAINTABLE_wbody1", "riser!s2!g0!mmarker", 'Drill Down 1')
        time.sleep(8)
         
        """
        Step17: Verify Information Builders Web page is displayed in a new window (or tab)
        """
        utillobj.switch_to_window(1,window_title='Business')
        time.sleep(10)
        elem=(By.CSS_SELECTOR,"[class*=top-bar-title] [id^='branding'] a img")
        resultobj._validate_page(elem)
        alternate_text=driver.find_element_by_css_selector("[class*=top-bar-title] [id^='branding'] a img").get_attribute('alt')
        print(alternate_text)
        utillobj.asequal('logo',alternate_text,'Step 17: Verify Information Builders Web page is displayed in a new window (or tab)')
        time.sleep(8)
        ele=driver.find_element_by_css_selector("#page_wrapper")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step17', image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """
        Step18: Close the output winow
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step19: Click "Save" in the toolbar > Save As "C2325655" > Click "Save"
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
         
        """
        Step20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step21: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2325655.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_2', mrid='mrid', mrpass='mrpass')
        time.sleep(10)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Step22: Click "Run" in the toolbar
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)                 
        time.sleep(15)
                  
        """
        Step23: Hover over "Stereo Systems" point > Verify drill down to "Drill Down 1" is displayed in the pop up menu
        """
        chart_type_css="circle[class*='riser!s0!g0!mmarker']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        yaxis_value="Cost of Goods"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step23.a: Verify Y-Axis Title")
        expected_xval_list=[]
        expected_yval_list=['0', '40M','80M','120M','160M','200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step23.b:Verify XY labels")
        ia_resultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 7, 'Step 23.c: Verify number of scatter displayed',custom_css="svg g circle[class^='riser']")
        legend=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step23.d: Verify Legends Title")
        time.sleep(5)
        expected_tooltip=['Cost of Goods:$205,113,863.00', 'Product Category:Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory', 'Drill Down 1']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s4!g0!mmarker!",expected_tooltip, "Step23.e: verify the default tooltip values")
         
        """
        Step24: Select "Drill Down 1"
        """
        time.sleep(5)
        wind_handle=driver.window_handles 
        print(wind_handle)       
        resultobj.select_drilldown_tooltip_menu("MAINTABLE_wbody1", "riser!s4!g0!mmarker!", 'Drill Down 1')
        wind_handle1=driver.window_handles 
        time.sleep(5)
        print(wind_handle1)
        
        """
        Step25: Verify Information Builders Web page is displayed in a new window (or tab)
        """
        time.sleep(10)
        utillobj.switch_to_window(2, custom_windows=wind_handle, window_title='Business')                 
        time.sleep(15)
        elem=(By.CSS_SELECTOR,"[class*=top-bar-title] [id^='branding'] a img")
        resultobj._validate_page(elem)
        alternate_text=driver.find_element_by_css_selector("[class*=top-bar-title] [id^='branding'] a img").get_attribute('alt')
        print(alternate_text)
        utillobj.asequal('logo',alternate_text,'Step 25: Verify Information Builders Web page is displayed in a new window (or tab)')
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(1,win_num=1)                 
        time.sleep(15)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step25', image_type='actual',x=1, y=1, w=-1, h=-1)
          
        """
        Step26: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
    
        """
        Step27: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()        