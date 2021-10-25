'''
Created on Oct 9, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2319016
TestCase Name = Query pane Horizontal Axis context menu
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea 
from common.locators import visualization_resultarea_locators
from common.lib import utillity

class C2319016_TestClass(BaseTestCase):

    def test_C2319016(self):
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2319016'

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step02: Double-click "Cost of Goods", located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1) 
                    
        """
        Step03: Double-click "Product,Category", from Product Dimension
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)  
        metaobj.verify_query_pane_field('Vertical Axis',"Cost of Goods",1,"Step03: Verify vertical axis")
        metaobj.verify_query_pane_field('Horizontal Axis',"Product,Category",1,"Step03: Verify horizontal axis")
             
        """
        Step04: Right-click "Horizontal Axis" in the Query pane > verify menu
        """
        time.sleep(2)
        metaobj.querytree_field_click("Horizontal Axis", 1, 1)
        time.sleep(2)
        a=['Suppress Empty Group','Sort By Total Value']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,msg='Step04: Verify menu in querypane')
        time.sleep(2)
        utillobj.verify_object_visible("[class='icon-column checkbox']",False,'"Step04:checkbox checked')
        
        """
        Step05: Select "Suppress Empty Group"
        """
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Suppress Empty Group')
        
        """
        Step06: Right-click "Horizontal Axis" again > verify option is de-selected
        """
        time.sleep(2) 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        metaobj.querytree_field_click("Horizontal Axis", 1, 1)
        time.sleep(2)
        stat=self.driver.find_element_by_css_selector("[class='icon-column checkbox']").is_displayed()
        utillobj.asequal(stat,True,"Step06: checkbox notchecked")        
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#resultAreaSplitPane")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
        metaobj.verify_query_pane_field('Vertical Axis',"Cost of Goods",1,"Step06: Verify vertical axis")
        metaobj.verify_query_pane_field('Horizontal Axis',"Product,Category",1,"Step06: Verify horizontal axis")
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step06:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step06:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step06:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step06.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step06.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step06: Verify bar value")
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
    