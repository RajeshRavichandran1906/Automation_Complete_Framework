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
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.locators.visualization_metadata_locators import VisualizationMetadataLocators
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity  
from selenium.webdriver import ActionChains
from common.pages import core_metadata

class C2140686_TestClass(BaseTestCase):
    def test_C2140686(self):
        #Test Variables 
        Test_Case_ID = 'C2140686'
        driver = self.driver 
        core_meta_obj = core_metadata.CoreMetaData(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        browser=utillobj.parseinitfile('browser')
        '''Step 01: Launch the IA API 
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/swbc_data&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F'''
        driver = self.driver #Driver reference object created      
        utillobj.infoassist_api_login('idis','baseapp/swbc_data','P312/S10099_5', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        '''Step 02:Add AVG.Time on page to vertical axis, drop Day Index, M-D-Y into horizontal axis bucket.'''
        metaobj.datatree_field_click('Measure Groups->Data->Avg. Time on Page', 1, 1, 'Add To Query', 'Vertical Axis')
        core_meta_obj.collapse_data_field_section('Measure Groups')
        metaobj.datatree_field_click('Dimensions->Data->Day Index,Compound->Day Index,M-D-Y', 1, 1,'Add To Query', 'Horizontal Axis')
        time.sleep(10)
        
        '''Step 03: Verify label values '''
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Day Index M-D-Y",'Step 03: Verify X title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Avg. Time on Page",'Step 03: Verify Y title')
        x=['.', '10/01/2014', '10/02/2014', '10/03/2014', '10/04/2014', '10/05/2014']
        y=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 03b: X annd Y axis Scales Values has changed ')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03: Verify bar color")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 427, 'Step03: Verify the total number of risers displayed on Run Chart')
        
        ''' Step 04:Verify query pane '''
        metaobj.verify_query_pane_field('Vertical Axis','Avg. Time on Page', 1, 'Step 04:Verify query pane')
        
        '''Step 05:Verify  bar values (Day Index M-D-Y: Entrances) '''
        time.sleep(5)
        tooltip_val=['Day Index M-D-Y:.', 'Avg. Time on Page:40,755.96', 'Filter Chart', 'Exclude from Chart', 'Drill up to Day Index Y-M']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar',tooltip_val,"Step 05:Verify  bar values (Day Index M-D-Y: Entrances)") 
        
        '''Step 06: Drop Day Index, M- into filter panel and create filter, select EQ operator, and click ok..'''
        metaobj.drag_drop_data_tree_items_to_filter('Dimensions->Data->Day Index,Compound->Day Index,M-D-Y', 1)
        time.sleep(10)
        range_operatorDropdown = "//div[contains(@id,'avOperatorComboBox')]/div/div[2]"
        elem1=(By.XPATH, range_operatorDropdown)
        resultobj._validate_page(elem1)
        driver.find_element(*VisualizationMetadataLocators.range_operatorDropdown).click()
        driver.find_element_by_xpath(VisualizationMetadataLocators.aggregation_val.format('Equal to')).click()
        metaobj.create_visualization_filters('numeric')
        time.sleep(5)
        
        '''Step 07: Verify query added to filter pane'''
        metaobj.verify_filter_pane_field('Day Index,M-D-Y',1,'Step 07: Verify Sale year query added to filter pane')
        
        '''Step 08: Select 'MISSING' value in filter prompt'''
        prompt_css = "div[id*='Prompt_1'] table[style*=hidden] tr"
        elem1=(By.CSS_SELECTOR, prompt_css)
        resultobj._validate_page(elem1)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(1, '[MISSING]')
        action = ActionChains(driver)
        move = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move,5,0)
        else:
            action.move_to_element_with_offset(move,1,1).perform()
        time.sleep(15)
        
        '''Step 09:  Verify filtered bar values'''
        tooltip_val=['Day Index M-D-Y:.', 'Avg. Time on Page:40,755.96', 'Drill up to Day Index Y-M']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar',tooltip_val,"Step 09:Verify filtered bar values)") 
        time.sleep(8)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09: Verify bar color")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step09: Verify the total number of risers displayed on Run Chart')
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Day Index M-D-Y",'Step 09: Verify X title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Avg. Time on Page",'Step 09: Verify Y title')
        x=[]
        y=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 09b: X annd Y axis Scales Values has changed ')
        
        
        '''Step 10:  Click Run in the toolbar'''
        elem1=(By.ID, 'applicationButton')
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
   
        '''Step 11: Verify output.'''
        #elem1=(By.CSS_SELECTOR, "rect[class*='riser!s0!g0']")
        #resultobj._validate_page(elem1)
        elem=(By.CSS_SELECTOR,"div[id*='ibi$container$inner$HBOX_1']")
        resultobj._validate_page(elem)
        time.sleep(15)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2140686_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        try:
            time.sleep(10)
            WebDriverWait(self.driver, 70).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='riser!s0!g0!mbar']")))
            x=[]
            y=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K']
            parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
            resultobj.wait_for_property(parent_css1, 1)
            resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 11b: X annd Y axis Scales Values has changed ')
            resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Day Index M-D-Y",'Step 11: Verify X title')
            resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Avg. Time on Page",'Step 11: Verify Y title')
            tooltip_val=['Day Index M-D-Y:.', 'Avg. Time on Page:40,755.96', 'Drill up to Day Index Y-M']
            resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar', tooltip_val,"Step 11: Verify output")
            time.sleep(10)
            utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11(i): Verify bar color")
            resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step11: Verify the total number of risers displayed on Run Chart')
        except TimeoutException:
            utillity.UtillityMethods.asequal(self, 'no', 'yes',
                                             "Step 11: Verify filtered output throws error: Known Product Failure - IA-4397")
        
        
        
        
        '''Step 12. Close the output window'''
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15) 
        elem1=(By.ID, 'applicationButton')
        resultobj._validate_page(elem1)
        
        '''Step 13: Click "Save" in the toolbar > Type C2140686 > Click "Save" in the Save As dialog'''
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID) 
        
        
if __name__ == '__main__':
    unittest.main()

