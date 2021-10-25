'''
Created on June24, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=147037&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2140681
TestCase Name : IA-4406:Vis: Show Data doesn't display correct output when Exclude from Chart with 2 dimensions in Preview
'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators

class C2140681_TestClass(BaseTestCase):

    def test_C2140681(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2140681'
        
        """
        Step 01: Launch the IA API with wf_retail_lite (Folder - S8404 and Master - wf_retail_lite) and login as "autodevuser03"
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
#         utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','S8404', 'mrid04', 'mrpass04')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
          
          
        """
        Step 02: Double click "Revenue" and "Product,SubCategory"
        """
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(10)
        metaobj.datatree_field_click('Product,Subcategory',2,1)
        time.sleep(10)
          
        sync_css="#MAINTABLE_wbody1 text[class='yaxis-title']"
        elem1=(By.CSS_SELECTOR, sync_css)
        resultobj._validate_page(elem1)
        time.sleep(5)
        """
        Step 03: Verify label values
        """
          
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 03:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 03:a(ii) Verify Y-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03.b(i) Verify first bar color")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Co...', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 3c: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 0d: Verify the total number of risers displayed')
          
        """
        Step 04: Verify bar riser values
        """        
        a = ['Product Subcategory:Blu Ray', 'Revenue:$232,884,116.13', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
          
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', 'riser!s0!g0!mbar', a,
                                         "Step 04: Verify Blu Ray values")
          
        """
        Step 05: Add "Product,Category" to Horizontal axis.
        """        
        metaobj.datatree_field_click('Product,Category',1,1,'Add To Query','Horizontal Axis')
        time.sleep(8)
        parent_css="#MAINTABLE_wbody1 text[class^='xaxis'][class$='title']"
        expected_obj="Product Subcategory : Product Category"
        timeout=0
        while True:
            temp_obj = self.driver.find_element_by_css_selector(parent_css).text
            if temp_obj == expected_obj:
                break
            else:
                time.sleep(1)
                timeout+=1
                if timeout == 250:
                    break
        time.sleep(1)
          
        """
        Step 06: verify query pane
        """        
        a = ['Vertical Axis', 'Revenue','Horizontal Axis','Product,Subcategory','Product,Category']
        metaobj.verify_query_pane_field('Horizontal Axis', 'Product,Category', 2,"Step 06: Verify query pane")
          
        expected_xval_list=['Blu Ray : Media Player', 'Boom Box : Stereo Sys...', 'CRT TV : Televisions', 'Charger : Accessories', 'DVD Players : Media Pl...', 'DVD Players - Portable...', 'Flat Panel TV : Televisi...', 'Handheld : Camcorder', 'Headphones : Access...', 'Home Theater System...', 'Portable TV : Televisions', 'Professional : Camcor...', 'Receivers : Stereo Sys...', 'Smartphone : Comput...', 'Speaker Kits : Stereo...', 'Standard : Camcorder', 'Streaming : Media Player', 'Tablet : Computers', 'Universal Remote Cont...', 'Video Editing : Video P...', 'iPod Docking Station :...']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step06: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step06: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g8!mbar", "bar_blue", "Step06: Verify bar color")
          
        """
        Step 07: Hover over on Accessories:Headphones and Click Exclude From Chart.
        """
        time.sleep(2)
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1','riser!s0!g8!mbar','Exclude from Chart')
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g8!mbar']")
        resultobj._validate_page(elem1)
        time.sleep(8)
          
        """
        Step 08: Verify Accessories:Headphones values excluded
        """
        xaxis = self.driver.find_element_by_xpath(VisualizationResultareaLocators.bar_xlabel)
        utillity.UtillityMethods.as_notin(self,xaxis.text, "Accessories:Headphones", "Step08:Accessories:Headphones is excluded from X Label")
  
        expected_xval_list=['Blu Ray : Media Player', 'Boom Box : Stereo Systems', 'CRT TV : Televisions', 'Charger : Accessories', 'DVD Players : Media Player', 'DVD Players - Portable : Media Player', 'Flat Panel TV : Televisions', 'Handheld : Camcorder', 'Home Theater Systems : Stereo Syst...', 'Portable TV : Televisions', 'Professional : Camcorder', 'Receivers : Stereo Systems', 'Smartphone : Computers', 'Speaker Kits : Stereo Systems', 'Standard : Camcorder', 'Streaming : Media Player', 'Tablet : Computers', 'Universal Remote Controls : Accessor...', 'Video Editing : Video Production', 'iPod Docking Station : Stereo Systems']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 08b: X annd Y axis Scales Values has changed or NOT')
        resultobj.wait_for_property("#MAINTABLE_wbody1 svg g.risers>g>rect[class^='riser']", 20)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 20, 'Step 08b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g8!mbar", "bar_blue", "Step 08b(i): Verify bar color")
        time.sleep(4)
        a=['Product Subcategory:Home Theater Systems', 'Product Category:Stereo Systems', 'Revenue:$84,359,685.22', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g8!mbar',a,"Step 08: Verify Accessories:Headphones values excluded")
        
        """
        Step 09: Click on Show Data from dropdown in right corner.
        """        
        time.sleep(5)
        resultobj.select_panel_caption_btn(0, select_type='menu', menu_item='Show Data')
          
        """
        Step 10: Verify the data values (Accessories:Headphones should not display)
        """
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(10) 
        utillobj.verify_data_set('ITableData0','I0r','C2140681_Ds01.xlsx',"Step 10: Verify the data values (Accessories:Headphones should not display)")
          
        """
        Step 11: Close the active report window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
          
        """
        Step 12: Click Run in the toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(15)
          
          
        """
        Step 13:  Verify output
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g8!mbar']")
        resultobj._validate_page(elem1)
        time.sleep(10)
        expected_xval_list=['Blu Ray : Media Player', 'Boom Box : Stereo Systems', 'CRT TV : Televisions', 'Charger : Accessories', 'DVD Players : Media Player', 'DVD Players - Portable : Media Player', 'Flat Panel TV : Televisions', 'Handheld : Camcorder', 'Home Theater Systems : Stereo Syst...', 'Portable TV : Televisions', 'Professional : Camcorder', 'Receivers : Stereo Systems', 'Smartphone : Computers', 'Speaker Kits : Stereo Systems', 'Standard : Camcorder', 'Streaming : Media Player', 'Tablet : Computers', 'Universal Remote Controls : Accessor...', 'Video Editing : Video Production', 'iPod Docking Station : Stereo Systems']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 13b: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 20, 'Step 13b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g8!mbar", "bar_blue", "Step 13b(i): Verify bar color")
          
        a = ['Product Subcategory:Home Theater Systems', 'Product Category:Stereo Systems', 'Revenue:$84,359,685.22', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', 'riser!s0!g8!mbar', a, "Step 13: Verify Accessories:Headphones values excluded")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2140681_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1)
          
        """
        Step 14: Close the output window.
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(10)
         
        """
        Step 15: Click "Save" in the toolbar > Type C2140681 > Click "Save" in the Save As dialog
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item("menu_save_as")
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(4)
        
        """
        Step 14: Logout of the IA API using the following URL.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        

if __name__ == '__main__':
    unittest.main()
