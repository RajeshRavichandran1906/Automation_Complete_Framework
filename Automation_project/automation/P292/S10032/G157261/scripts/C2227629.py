'''
Created on May 08, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227629
Test case Name =  Show Data via runtime menu
'''

import unittest, time
from selenium.webdriver.common.by import By
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase
from common.locators import visualization_resultarea_locators
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon,visualization_run

class C2227629_TestClass(BaseTestCase):

    def test_C2227629(self):
        
        """
        TESTCASE OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        vis_runobj = visualization_run.Visualization_Run(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)    
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
 
        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
        time.sleep(4)
         
        """
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
         
        """
        Step04: Drag and drop "Product,Category" to the Filter pane
        Step05: Deselect "All"
        Step06: Select "Camcorder", "Computers"
        Step07: Click OK
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
        time.sleep(4)
        item_list=['[All]','Camcorder','Computers']
        metaobj.select_or_verify_visualization_filter_values(item_list, Ok_button=True)
        time.sleep(2) 
                
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step 07.01: Verify filter pane has Product Category")
        time.sleep(3) 
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 07.02: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 07.03: Verify Y-Axis Title")
        expected_xval_list=['Camcorder','Computers']
        expected_yval_list=['0','20M','40M','60M', '80M','100M', '120M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 07.04: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 07.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.06: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 07.07: Verify bar value")
        time.sleep(5)
        
        """
        Step08: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
            
        """
        Step09: Verify output
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 09.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 09.02: Verify Y-Axis Title")
        expected_xval_list=['Camcorder','Computers']
        expected_yval_list=['0','20M','40M','60M', '80M','100M', '120M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step  09.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09.05: Verify first bar color")
        time.sleep(5)
        
        bar=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 09.06: Verify bar value")
        time.sleep(5)
        
        """
        Step10: Click "Media Player" in the Filter prompt
        """
        propertyobj.select_or_verify_show_prompt_item('1', 'Media Player')#selecting Stereo Systems in FF
        time.sleep(4)
        
        """
        Step11: Verify output
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        propertyobj.select_or_verify_show_prompt_item('1', 'Media Player',verify=True,verify_type=True,msg="Step11:Verify Media Player is checked")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 11.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 11.02: Verify Y-Axis Title")
        expected_xval_list=['Camcorder','Computers','Media Player']
        expected_yval_list=['0','40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 11.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.05: Verify first bar color")
        time.sleep(5)
        
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar, "Step 11.06: Verify bar value")
        time.sleep(5)
        """
        Step12: Expand Filter menu in the lower right corner
        Step13: Click the Undo icon in the Filter menu (icon after grid)
        """
        time.sleep(5)
        vis_runobj.select_run_menu_option('MAINTABLE_menuContainer1',"reset")
        time.sleep(5)
        
        """
        Step14: Verify "Media Player" is deselected and Chart updated
        Step15: Verify output
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 15.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 15.02: Verify Y-Axis Title")
        expected_xval_list=['Camcorder','Computers']
        expected_yval_list=['0','20M','40M','60M', '80M','100M', '120M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 15.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 15.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 15.05: Verify first bar color")
        time.sleep(5)
        
        bar=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 15.06: Verify bar value")

        """
        Step16: Close output window
        """
        core_utils.switch_to_previous_window()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
               
        """
        Step17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """   
        
if __name__ == '__main__':
    unittest.main()