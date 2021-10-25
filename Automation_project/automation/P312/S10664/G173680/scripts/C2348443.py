'''
Created on Jan 10, 2018

@author: Kiruthika
'''
import unittest,time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import ia_resultarea,visualization_resultarea,visualization_metadata,visualization_ribbon,metadata

class C2348443_TestClass(BaseTestCase):

    def test_C2348443(self):
        
        """
            CLASS OBJECTS
        """
        driver = self.driver #Driver reference object created
        metadataobj = metadata.MetaData(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        iaresult= ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj=visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2348443'
        
        """
        Step01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_binning_2', 'mrid', 'mrpass')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 12, expire_time=15) 
         
        """
        Step02: Double click "Quantity, Sold" and "Product, Category"
        """
        metadataobj.collapse_data_field_section('Filters and Variables')
        time.sleep(3)
        metaobj.datatree_field_click("Quantity,Sold",2,1)
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
         
        """
        Step03: Right click on "Quantity, Sold" > Create Bins...
        Step04: Set Width of bins = 1
        Step05: Click OK
        """
        metaobj.datatree_field_click('Quantity,Sold',1,1,'Create Bins...')
        wd_of_bin="input[id^='qbBinWidthTextField']"
        resultobj.wait_for_property(wd_of_bin, 1, expire_time=10)
        wd_elem=self.driver.find_element_by_css_selector(wd_of_bin)
        utillobj.set_text_field_using_actionchains(wd_elem,"1",keyboard_type=True)
        bin_ok_btn=driver.find_element_by_css_selector("[id^='qbBinsOkBtn']")   
        utillobj.click_on_screen(bin_ok_btn, "middle", click_type=0)
        time.sleep(8)
         
        """
        Step06: Add bin "QUANTITY_SOLD_BIN_1" to Rows bucket
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Measure Groups->Sales->QUANTITY_SOLD_BIN_1',1,"Rows",0) 
        time.sleep(3) 
         
        """
        Step07: Verify bin added to Rows bucket and preview updated
        """
        expected_fields=['Bar Stacked1', 'Matrix', 'Rows','QUANTITY_SOLD_BIN_1', 'Columns', 'Axis', 'Vertical Axis', 'Quantity,Sold', 'Horizontal Axis','Product,Category','Marker', 'Color', 'Size', 'Tooltip']
        metaobj.verify_query_panel_all_field(expected_fields, "Step 07.01: Verify query pane")
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 28, expire_time=10)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 28,'Step 07.02: Verify the total number of risers displayed on preview')

        
        """ 
        Step08: Click view source icon to view fex code generated
        Step09: Close view source code window
        """
        expected_syntax_list=["SUM WF_RETAIL_LITE.WF_RETAIL_SALES.QUANTITY_SOLD","BY QUANTITY_SOLD_BIN_1","BY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY","TYPE=DATA, COLUMN=N1, BUCKET=row, $"]
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 09.01: Verify bin is showing as BY')
          
        """
        Step10: Hover on the preview chart and verify tool tip values
        """
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.01: Verify first bar color")
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 28, expire_time=10)
        bar=['QUANTITY_SOLD_BIN_1:1', 'Product Category:Accessories', 'Quantity Sold:236,127', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 10.02: Verify bar value")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1",'QUANTITY_SOLD_BIN_1', "Step 10.03: Verify Y-Axis Title",custom_css="text[class*='rowHeader-label']")        
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 10.04: Verify X-Axis Title")
           
        """
        Step11: Click Save in the toolbar > Save as "C2348443" > Click Save
        """
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 28, expire_time=10)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(0.3)
        utillobj.ibfs_save_as(Test_Case_ID)
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 28, expire_time=10)
          
        """
        Step12: Logout using API
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
          
        """
        Step13: Restore saved fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348443.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'P312/S10664_binning_2',mrid='mrid',mrpass='mrpass')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 28, expire_time=10)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 13.01: Verify first bar color")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1",'QUANTITY_SOLD_BIN_1', "Step 13.02: Verify Y-Axis Title",custom_css="text[class*='rowHeader-label']")        
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 13.03: Verify X-Axis Title")
          
        """
        Step14: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == "__main__":
    unittest.main()