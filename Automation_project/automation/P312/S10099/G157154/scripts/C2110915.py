'''
Created on Feb 28, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2110915
Test_Case Name : Chart selection menu remains on canvas when lassoing multiple times
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.lib import core_utility

class C2110915_TestClass(BaseTestCase):

    def test_C2110915(self):
        
        Test_Case_ID = "C2110915"
        metadata_browser_query_variables__css = "#iaMetaDataBrowser td"  
        metadata_browser_css = "#iaMetaDataBrowser"    
        changed_bar_text_css="[class*='bi-component dv-caption'] div"    
        total_no_of_riser_css = "#MAINTABLE_1 rect[class^='riser']"  
        long_wait_time_in_sec = 120
        short_wait_time_in_sec = 60
        yaxis_title_css = "#MAINTABLE_wbody1_f text[class='yaxis-title']"
        xaxis_title_css = "#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']"
        toolbar_run="#topToolBar #runButton img"
        no_of_riser = 7
        
        visual = visualization.Visualization(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Step01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        visual.invoke_visualization_using_api('new_retail/wf_retail_lite')
        visual.wait_for_visible_text(metadata_browser_query_variables__css, 'QueryVariables', short_wait_time_in_sec)
        
        """
        Step02: Add Product Category and Cost of Goods to Canvas
        """
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text(xaxis_title_css, "ProductCategory", 45)
        visual.double_click_on_datetree_item('Cost of Goods', 1)
        visual.wait_for_visible_text(yaxis_title_css, "CostofGoods", 45)
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        
        """
        Step03: Use mouse to lasso several riser (first three)
        """
        Accessories_css = "#MAINTABLE_wbody1 [class*='riser!s0!g0!mbar']"
        source_element = self.driver.find_element_by_css_selector(Accessories_css)
        Computers_css = "#MAINTABLE_wbody1 [class*='riser!s0!g2!mbar']"
        target_element = self.driver.find_element_by_css_selector(Computers_css)
        visual.create_lasso(source_element, target_element, source_xoffset=-35, source_element_location='middle_left', target_element_location='middle_right')
        
        """
        Step04: Notice chart selection menu appears
        """
        tooltip_css="[class*='tdgchart-tooltip'][style*='visible']"
        visual.wait_for_number_of_element(tooltip_css,1, 25)
        expected_tooltip_list = ['3 points', 'Filter Chart', 'Exclude from Chart']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg="Step04: Verify lasso tooltip")
        
        """
        Step05: Lasso several risers again other than selected previous (last two)
        Step06 :Verify the first chart selection menu does not remain on canvas
        """
        visual.wait_for_number_of_element(tooltip_css, expected_number=1, time_out=25) 
        elem = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        core_utilobj.python_left_click(elem, element_location='top_left', xoffset=9, yoffset=9)
        Televisions_css = "#MAINTABLE_wbody1 [class*='riser!s0!g5!mbar']"
        source_element = self.driver.find_element_by_css_selector(Televisions_css)
        Video_production_css = "#MAINTABLE_wbody1 [class*='riser!s0!g6!mbar']"
        target_element = self.driver.find_element_by_css_selector(Video_production_css)
        visual.create_lasso(source_element, target_element ,source_xoffset=-35, source_element_location='middle_left', target_element_location='middle_right')
        
        visual.wait_for_number_of_element(tooltip_css, expected_number=1, time_out=25)
        expected_tooltip_list = ['2 points', 'Filter Chart', 'Exclude from Chart']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg="Step06: Verify New lasso tooltip")
        
        visual.take_preview_snapshot(Test_Case_ID, '06')
                 
        """
        Step07: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """        
        visual.wait_for_number_of_element(toolbar_run,1, 25)
#         visual.logout_visualization_using_api()

if __name__ == '__main__':
    unittest.main()        
