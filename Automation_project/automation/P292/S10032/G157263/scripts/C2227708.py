'''
Created on Jun 1, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227708
TestCase Name = Data pane Dimension field context menu
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, metadata
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227708_TestClass(BaseTestCase):

    def test_C2227708(self):
                
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227708'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        new_meta = metadata.MetaData(self.driver)
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Expand "Product" Dimension > right-click "Product,Category" > verify menu
        """
        time.sleep(4)
        metaobj.datatree_field_click('Product,Category',1, 1)
        time.sleep(4)
        utillobj.select_or_verify_bipop_menu('Add To Query', verify='true', expected_popup_list=['Sum', 'Create Group...', 'Add To Query', 'Filter'], msg='Step 02.00:')
        
        """
        Step 03: Select "Add to Query > Columns"
        """
        time.sleep(4)
        new_meta.collapse_data_field_section("Product")
        metaobj.datatree_field_click('Product,Category',1, 1, 'Add To Query', 'Columns')
        time.sleep(4)
        
        """
        Step 04: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 g.scrollColTitle"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='colLabel!']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        expected_label= ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Columns','Product Category',expected_label, "Step 04.00:")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 04.01: Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 7, 'Step 04.02: Verify number of risers displayed')
        time.sleep(2)
    
        """
        Step 05: Right-click "Product,Subcategory" > Select "Add to Query > Tooltip"
        """
        time.sleep(4)
        metaobj.datatree_field_click('Product,Subcategory',1, 1, 'Add To Query', 'Tooltip')
        time.sleep(4)
          
        """
        Step 06: Verify Query pane
        """
        metaobj.verify_query_pane_field('Columns',"Product,Category",1,"Step 06.00")
        metaobj.verify_query_pane_field('Tooltip',"FST.Product,Subcategory",1,"Step 06.01")
        
        """
        Step 07: Expand Customer Dimension > right-click "Customer,Business,Region" > select "Add to Query > Color"
        """
        time.sleep(4)
        metaobj.datatree_field_click('Customer,Business,Region',1, 1, 'Add To Query', 'Color')
        time.sleep(4)
        
        """
        Step 08: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        parent_css="#MAINTABLE_wbody1 g.scrollColTitle"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='colLabel!']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 28)
        time.sleep(5)
        expected_label= ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Columns','Product Category',expected_label, "Step 08.00:")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 08.01: Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 4, 7, 'Step 08.02: Verify number of risers displayed')
        legend=['Customer Business Region', 'EMEA', 'North America', 'Oceania', 'South America']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 08.03: Verify Y-Axis Title")
        time.sleep(2)
       
        """
        Step 09: Double-click "Gross Profit" from Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click('Gross Profit', 2, 1)
        time.sleep(4)
        
        """
        Step 10: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css="#MAINTABLE_wbody1 g.scrollColTitle"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='colLabel!']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 28)
        time.sleep(5)
        expected_label= ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Columns','Product Category',expected_label, "Step 10.00:")
        expected_xval_list=[]
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 10.01: X and Y axis Scales Values has changed or NOT')
        yaxis_value="Gross Profit"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10.02: Verify Y-Axis Title")  
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 10.03: Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 4, 7, 'Step 10.04: Verify number of risers displayed')
        legend=['Customer Business Region', 'EMEA', 'North America', 'Oceania', 'South America']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 10.05: Verify Y-Axis Title")
        time.sleep(2)
        
        """
        Step 11: Click Save in the toolbar
        Step 12: Save as "C2164828" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        
        """
        Step 13: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
             
        """
        Step 14: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
            
        """
        Step 15: Verify Preview
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar!r0!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css="#MAINTABLE_wbody1 g.scrollColTitle"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='colLabel!']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 28)
        time.sleep(5)
        expected_label= ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Columns','Product Category',expected_label, "Step 15.00:")
        expected_xval_list=[]
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 15.01: X and Y axis Scales Values has changed or NOT')
        yaxis_value="Gross Profit"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 15.02: Verify Y-Axis Title")  
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 15.03 Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 4, 7, 'Step 15.04: Verify number of risers displayed')
        legend=['Customer Business Region', 'EMEA', 'North America', 'Oceania', 'South America']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 15.05: Verify Y-Axis Title")
                
        """
        Step 16: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
                
if __name__ == '__main__':
    unittest.main()