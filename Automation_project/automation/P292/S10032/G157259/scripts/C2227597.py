'''
Created on Apr 24, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227597
Test case Name =  Design time 'Filter Chart'
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity

class C2227597_TestClass(BaseTestCase):

    def test_C2227597(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227597'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)

        """
        Step 02: Double-click "Cost of Goods"
        """
        
        metaobj.datatree_field_click("Cost of Goods",2,1)
        utillobj.synchronize_with_visble_text("[class='yaxis-title']", 'Cost of Goods', 10)
        
        """
        Step 03: Double-click "Product,Category"
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        utillobj.synchronize_with_visble_text("[class='xaxisOrdinal-title']", 'Product Category', 10)
        
        """
        Step 04: Hover over "Media Player" riser (bar) > Select "Filter Chart"
        """
        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 10)
        
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g3!mbar", 'Filter Chart')
        time.sleep(2) 
          
        """
        Step05: Verify Canvas 
        """        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 10)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step05a: Verify filter pane has Product Category")
        time.sleep(3)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 05:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 05:a(i) Verify Y-Axis Title")
        expected_xval_list=['Media Player']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 05:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 05.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 05.c: Verify first bar color")
        
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 05.d: Verify bar value")
        time.sleep(5)
        
        """
        Step06: Click Run
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_window(1)
        time.sleep(15) 
            
        """
        Step07: Verify output
        """
        css="#MAINTABLE_wbody1_f rect[class*='riser!s0!g0!mbar']"
        utillobj.synchronize_with_number_of_element(css, 1,25)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 07:a(i) Verify Y-Axis Title")
        expected_xval_list=['Media Player']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 7.d: Verify bar value")
          
        """
        Step08: Close output window
        """
        
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
              
        """
        Step09: Click Save in the toolbar
        Step10: Save as "C2158261" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
              
        """
        Step11: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step12: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_2',mrid='mrid',mrpass='mrpass')
        css="#MAINTABLE_wbody1 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(css, 'Product Category', 185)
             
        """
        Step13: Verify Canvas
        """
        metaobj.verify_filter_pane_field('Product,Category',1,"Step13a: Verify filter pane has Product Category")
        time.sleep(3)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step13:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step13:a(i) Verify Y-Axis Title")
        expected_xval_list=['Media Player']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step13:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step13.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step13.c: Verify first bar color")
        
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step13.d: Verify bar value")
        time.sleep(5)
          
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()
        
        