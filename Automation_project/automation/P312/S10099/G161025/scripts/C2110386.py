'''
Created on June 21, 2016

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404 
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109128
'''
__author__ = "Gobinath Thiyagarajan"
__copyright__ = "IBI"

import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, metadata
from common.lib import utillity  
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators

class C2110386_TestClass(BaseTestCase):
    def test_C2110386(self):
        #Test Variables 
        Test_Case_ID = 'C2110386'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        
        '''Step 01: Launch the IA API 
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F'''
        driver = self.driver #Driver reference object created 
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        '''Step 02: Add field 'Cost of Goods' from Sales Measures.'''
        metadataobj.collapse_data_field_section('Filters and Variables')
        time.sleep(3)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        
        '''Step 03: Add fields 'Product,Category' from Product Dimension '''
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(10)
        
        ''' Step 04:Verify label values. '''
        utillobj._validate_page((By.CSS_SELECTOR,"#MAINTABLE_wbody1_f text[class^='xaxis'][class$='title']"))
        resultobj.verify_xaxis_title('MAINTABLE_wbody1_f', "Product Category",'Step 04: Verify X title')
        
        utillobj._validate_page((By.CSS_SELECTOR,"#MAINTABLE_wbody1_f text[class='yaxis-title']"))
        resultobj.verify_yaxis_title('MAINTABLE_wbody1_f', 'Cost of Goods','Step 04: Verify Y title')
        
        '''Step 05:Verify query pane '''
        metaobj.verify_query_pane_field('Vertical Axis' ,'Cost of Goods', 1, 'Step 05:  verify query pane')
        
        '''Step 06: Verify  bar riser values'''
        time.sleep(10)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step06: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step06: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step06: Verify bar color")
        
        tooltip_val=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1_f','riser!s0!g0!mbar',tooltip_val,"Step 06: Verify output value")
        
        '''Step 07: Drag/drop 'Product,Category' to Filter bucket, click ok  '''
        metaobj.querytree_field_click('Product,Category', 1,1, 'Filter Values...')
        metaobj.create_visualization_filters('alpha')
        time.sleep(10)
        
        '''Step 08: Verify query added to fitler pane'''
        metaobj.verify_filter_pane_field('Product,Category',1, 'Step 08: Verify query added to filter pane')
        
        '''Step 09:  Click Run in the toolbar'''
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        elem1=(By.CSS_SELECTOR, '[class*="riser!s"]')
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step09: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step09: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step09: Verify bar color")
        
        tooltip_val=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1_f','riser!s0!g0!mbar',tooltip_val,"Step09: Verify output value")
        
        '''Step 10:  Lasso 'Media Player' and 'Stereo Systems' bars select Filter Chart'''
        time.sleep(5)
        resultobj.create_lasso('MAINTABLE_wbody1','rect', 'riser!s0!g3!mbar', target_tag='rect', target_riser='riser!s0!g4!mbar')
        time.sleep(5)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(15)
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        time.sleep(2)  
        
        '''Step 11: Verify filtered bar values
        Step 12. Verify Filter prompt values (Media player and stereo systems should only be checked)'''
        propertyobj.select_or_verify_show_prompt_item(1, 'Media Player', True,verify_type=True,msg="Step 12. Verify Filter prompt values Media player")
        propertyobj.select_or_verify_show_prompt_item(1, 'Stereo Systems', True,verify_type=True,msg="Step 12. Verify Filter prompt values Stereo Systems")
        time.sleep(4)
        
        '''Step 13: Verify output'''
        expected_xval_list=['Media Player', 'Stereo Systems']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step13: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step13: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step13: Verify bar color")
        
        tooltip_val=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar', tooltip_val,"Step 13: Verify output")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2110386_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1) 
         
        '''Step 14 : Close the output window'''
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        '''Step 15: Click "Save" in the toolbar > Type C2110386 > Click "Save" in the Save As dialog'''
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()

