'''
Created on June 17, 2016

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404 
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109128
'''
__author__ = "Gobinath Thiyagarajan"
__copyright__ = "IBI"

import unittest, time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization
from common.pages import visualization_metadata, visualization_resultarea

class C2109128_TestClass(BaseTestCase):
    
    def test_C2109128(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2109128'
        element_css = '#queryTreeWindow'
        
        """
        CLASS OBJECTS
        """
        visual = Visualization(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        '''Step 01: Launch the IA API with wf_retail_lite
        http://machine:port/ibi_apps/ia?tool=idis&master=s8357/wfretail&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F'''
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        '''Step 02: Add Revenue to the vertical axis.'''
        metaobj.datatree_field_click('Revenue', 1, 1,'Add To Query','Vertical Axis')
        time.sleep(4)
        
        '''Step 03: Add Sale,Year, Sale Quarter and Sale Month to the horizontal axis.'''
        metaobj.datatree_field_click('Sale,Year', 1, 1, 'Add To Query', 'Horizontal Axis')
        visual.wait_for_visible_text(element_css, 'Sale,Year')
        metaobj.datatree_field_click('Sale,Quarter', 1, 1,'Add To Query', 'Horizontal Axis')
        visual.wait_for_visible_text(element_css, 'Sale,Quarter')
        metaobj.datatree_field_click('Sale,Month', 1, 1,'Add To Query','Horizontal Axis')
        visual.wait_for_visible_text(element_css, 'Sale,Month')
        
        '''  Step 04: Verify labels'''
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class^='xaxisOrdinal-labels'][class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 72)
        xaxis_value="Sale Year : Sale Quarter : Sale Month"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 04.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 04.02: Verify Y-Axis Title")
        expected_xval_list=['2011 : 1 : 1', '2011 : 1 : 2', '2011 : 1 : 3', '2011 : 2 : 4', '2011 : 2 : 5', '2011 : 2 : 6', '2011 : 3 : 7', '2011 : 3 : 8', '2011 : 3 : 9', '2011 : 4 : 10']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 04.03: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 72, 'Step 04.04: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 04.05: Verify bar color") 
        time.sleep(8)
        
        '''Step 05: Verify query pane'''
        metaobj.verify_query_pane_field('Vertical Axis','Revenue',1,"Step 05.01")
        metaobj.verify_query_pane_field('Horizontal Axis','Sale,Year',1,"Step 05.02")
        metaobj.verify_query_pane_field('Horizontal Axis','Sale,Quarter',2,"Step 05.03")
        metaobj.verify_query_pane_field('Horizontal Axis','Sale,Month',3,"Step 05.04")
        
        '''Step 06: Add Product Category to color'''
        metaobj.datatree_field_click('Product,Category', 1, 1,'Add To Query','Color')
        visual.wait_for_number_of_element('rect[class*="riser!s4!g10!mbar!"]', 1)
        
        '''Step 07: Verify label values'''
        parent_css="#MAINTABLE_wbody1 svg g text[class='legend-title']"
        elem=(By.CSS_SELECTOR,parent_css)
        resultobj._validate_page(elem)
        resultobj.wait_for_property(parent_css, 1)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 6, 84, 'Step 07.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2011 : 1 : 1', '2011 : 1 : 2', '2011 : 1 : 3', '2011 : 2 : 4', '2011 : 2 : 5', '2011 : 2 : 6', '2011 : 3 : 7', '2011 : 3 : 8', '2011 : 3 : 9', '2011 : 4 : 10']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 07.02: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s4!g0!mbar", "brick_red", "Step 07.03: Verify first bar color")
        xaxis_value="Sale Year : Sale Quarter : Sale Month"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 07.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 07.05: Verify Y-Axis Title")
        lab_val = ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", lab_val,'Step 07.06: Verify label values' ) 
        
        '''Step 08: Verify tooltip values for riser '''
        time.sleep(5)
        tooltip_val=['Sale Year:2015', 'Sale Quarter:1', 'Sale Month:2', 'Revenue:$6,223,574.78', 'Product Category:Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill up to', 'Drill down to']
        visual.verify_tooltip('riser!s4!g49!mbar!', tooltip_val, msg="Step 08.01: Verify tooltip values for riser")
        
        '''Step 09:  Click Run in the toolbar'''
        
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
         
        '''   Step 10:  Verify output'''
         
        parent_css="#MAINTABLE_wbody1 svg g text[class='legend-title']"
        elem1=(By.CSS_SELECTOR, parent_css)
        resultobj._validate_page(elem1)
        time.sleep(5)
        resultobj.wait_for_property(parent_css, 1)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 6, 84, 'Step 10.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2011 : 1 : 1', '2011 : 1 : 2', '2011 : 1 : 3', '2011 : 2 : 4', '2011 : 2 : 5', '2011 : 2 : 6', '2011 : 3 : 7', '2011 : 3 : 8', '2011 : 3 : 9', '2011 : 4 : 10']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 10.02: X annd Y axis Scales Values has changed or NOT')
        visual.verify_chart_color_using_get_css_property("rect[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 10.03")
        xaxis_value="Sale Year : Sale Quarter : Sale Month"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10.05: Verify Y-Axis Title")
                    
        '''  Step 11: Close the output window'''
        visual.switch_to_previous_window()
        
        '''  Step 12. Click "Save" in the toolbar > Type C2109128 > Click "Save" in the Save As dialog'''
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        visual.save_visualization_from_top_toolbar(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()