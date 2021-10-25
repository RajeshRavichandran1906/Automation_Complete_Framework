'''
Created on June 27, 2016

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404 
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2140684
'''
from selenium.webdriver.common.action_chains import ActionChains

__author__ = "Gobinath Thiyagarajan"
__copyright__ = "IBI"

import unittest
import time, pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, core_metadata, visualization_properties
from common.lib import utillity  
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators

class C2140684_TestClass(BaseTestCase):
    
    def test_C2140684(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2140684'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        core_metaobj = core_metadata.CoreMetaData(self.driver)
        vis_prop_obj=visualization_properties.Visualization_Properties(self.driver)
        
        '''Step 01: Launch the IA API '''
        driver = self.driver #Driver reference object created   
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        '''Step 02: Change to Grid..'''
        ribbonobj.change_chart_type('grid') 

        '''Step 03: Double click "Revenue" and "Sale,Year".'''
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(10)
        metaobj.datatree_field_click('Sale,Year', 2, 1)
        time.sleep(10)
        sync_css="#MAINTABLE_wbody1 .tablePanel .rowTitle text"
        elem1=(By.CSS_SELECTOR, sync_css)
        resultobj._validate_page(elem1)
        time.sleep(5)
        
        '''  Step 04: Verify grid title and data values '''
        title = ['Sale Year', 'Revenue']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',title, 'Step 04.1: Verify grid title')
        row_val=['2011', '$48,965,069.21']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val,'Step 04.2: verify grid 1st row value')   
        
        '''Step 05:Add "Sale, Year" to Filter, Change operator to Equal to and click Ok '''
        metaobj.querytree_field_click('Sale,Year', 1,1,'Filter Values...') 
        elem1=(By.CSS_SELECTOR, "#avFilterOkBtn")
        resultobj._validate_page(elem1)
        time.sleep(2)
        metaobj.create_visualization_filters('numeric',['Operator','Equal to'])
        time.sleep(4)
        
        '''Step 06: Verify query added to filter pane'''
        metaobj.verify_filter_pane_field('Sale,Year',1,'Step 06:  Verify Query added to filter pane')
        time.sleep(10)
        
        '''Step 07: Insert stacked bar. '''
        ribbonobj.select_ribbon_item('Home','Insert',opt='Chart')
        time.sleep(10)
        
        '''Step 08: Add Product Category and Revenue. '''
        core_metaobj.expand_data_field_section('Dimensions->Product->Product')
        time.sleep(9)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(6)
        
        '''Step 09:  Verify label values.'''
        elem = "#MAINTABLE_wbody2 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 300).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 7)
        time.sleep(3)
        resultobj.verify_xaxis_title('MAINTABLE_wbody2', "Product Category", "Step 09: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody2', "Revenue", "Step 09: verify Y axis title") 
        time.sleep(6)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step09: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 7, 'Step09: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g0!mbar", "bar_blue", "Step09: Verify bar color")
#         bar_riser = ['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
#         resultobj.verify_default_tooltip_values('MAINTABLE_wbody2', "riser!s0!g0!mbar",bar_riser,"Step09: Verify all bar riser values ")
        
        '''Step 10:  Add Sale Quarter to Color. '''
        time.sleep(5)
        metaobj.datatree_field_click('Sale,Quarter', 1, 1, 'Add To Query', 'Color') 
        time.sleep(5)
        parent_css="#MAINTABLE_wbody2 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(1)
        
        '''Step 11: Verify query pane'''
        metaobj.verify_query_pane_field('Vertical Axis','Revenue',1,'Step 11:  verify query pane Vertical Axis')
        metaobj.verify_query_pane_field('Horizontal Axis', 'Product,Category',1,'Step 11:  verify query pane Horizontal Axis')
        metaobj.verify_filter_pane_field('Sale,Year', 1,'Step 11: Verify Sale year query added to filter pane')
        move = driver.find_element_by_css_selector("#orgdiv0")
        browser=utillobj.parseinitfile("browser")
        if browser=="Firefox":
            '''x_fr=move.location['x']
            y_fr=move.location['y']'''
            pyautogui.moveTo(1,1)
        else:
            action = ActionChains(driver)
            action.move_to_element_with_offset(move,1,1).perform()
            time.sleep(5)
        
        '''Step 12. Select 2012 from sale Year.'''
        '''Step 13: Select "Accessories, Sale Quarter 4" from chart and click filter chart''' 
        vis_prop_obj.select_or_verify_show_prompt_item('1', '2012')
        time.sleep(10) 
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody2','riser!s3!g0!mbar','Filter Chart')
        time.sleep(15)
        elem = "#MAINTABLE_wbody2 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1)
        time.sleep(2)
        
        '''Step 14 : Verify query added to filter pane'''
        metaobj.verify_filter_pane_field('TIME_QTR and PRODUCT_CATEGORY',2,'Step 14: Verify query added to filter pane')
        time.sleep(5)
        
        '''Step 15: Verify filtered value in stacked bar and grid.'''
        tooltip_val=['Product Category:Accessories', 'Revenue:$2,268,524.84', 'Sale Quarter:4', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g0!mbar',tooltip_val,"Step 15: Verify filtered value in stacked bar and grid")
        time.sleep(5)
        row_val=['2012', '$2,268,524.84']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val,'Step 15.2: verify grid 1st row value')
        
        '''Step 16: Click Run in the toolbar'''
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        '''Step 17: Verify output'''
        raiser="[id^='MAINTABLE_2'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(5)
        expected_xval_list=['Accessories']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step17: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 1, 'Step17: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g0!mbar", "bar_blue", "Step 17: Verify bar color")
        expected_legend_list=['Sale Quarter','4']
        resultobj.verify_riser_legends('MAINTABLE_wbody2', expected_legend_list, "Step 17: Verify Chart Legend")
        time.sleep(2)
#         tooltip_val=['Product Category:Accessories', 'Revenue:$2,268,524.84', 'Sale Quarter:4', 'Drill up to Sale Year', 'Drill down to']
#         resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g0!mbar',tooltip_val,"Step 17: Verify output value")
        time.sleep(15)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2140684_Actual_step17', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        ''' Step 18: Close the output window'''
        time.sleep(2)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        '''Step 19: Click "Save" in the toolbar > Type C2140684 > Click "Save" in the Save As dialog'''
        ribbonobj.select_tool_menu_item("menu_save_as")
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(4)
        
if __name__ == '__main__':
    unittest.main()