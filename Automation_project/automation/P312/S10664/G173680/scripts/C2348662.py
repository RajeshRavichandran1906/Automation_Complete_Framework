'''
Created on Jan 11, 2018

@author: Kiruthika
TestSuite : 8202 New Features and product changes for existing functionality
TestCase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348662
TestCase Name: If Bin field added to Size bucket it is treated as the measure
'''
import unittest,time
from common.lib import utillity
from common.pages import ia_resultarea,visualization_resultarea,visualization_metadata,visualization_ribbon
from common.lib.basetestcase import BaseTestCase

class C2348662_TestClass(BaseTestCase):


    def test_C2348662(self):
        utillobj = utillity.UtillityMethods(self.driver)
        iaresult= ia_resultarea.IA_Resultarea(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj=visualization_ribbon.Visualization_Ribbon(self.driver)
        Test_Case_ID = 'C2348662'
        
        """
        Step01: Restore C2348443.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348443.fex
        """
        utillobj.infoassist_api_edit('C2348662_Base', 'idis', 'P312/S10664_binning_2',mrid='mrid',mrpass='mrpass')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 28, expire_time=10)
          
        """
        Step02: Drag and drop "QUANTITY_SOLD_BIN_1" bin from Rows to Size
        """
        metaobj.drag_and_drop_query_items('QUANTITY_SOLD_BIN_1', "Size")
        time.sleep(0.2) 
         
        """
        Step03: Verify bin added to Size bucket and preview updated
        """
#         utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'P312/S10664_binning_2',mrid='mrid',mrpass='mrpass')
#         parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
#         resultobj.wait_for_property(parent_css, 28, expire_time=10)
        expected_fields=['Bar Stacked1', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Quantity,Sold', 'Horizontal Axis','Product,Category','Marker', 'Color', 'Size','CNT.QUANTITY_SOLD_BIN_1', 'Tooltip']
        metaobj.verify_query_panel_all_field(expected_fields, "Step 03.1: Verify query pane")
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7, expire_time=10)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7,'Step 03.b: Verify the total number of risers displayed on preview')
            
        """ 
        Step04: Click view source icon to view fex code generated
        Verify "QUANTITY_SOLD_BIN_1" added as by field
        Step05: Close view source code window
        """
        expected_syntax_list=["SUM WF_RETAIL_LITE.WF_RETAIL_SALES.QUANTITY_SOLD","CNT.QUANTITY_SOLD_BIN_1","BY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY","TYPE=DATA, COLUMN=N3, BUCKET=size, $"]
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 05: Verify bin is showing as BY')
        
        """
        Step06: Hover on the preview riser and verify tool tip values
        """
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7, expire_time=10)
        
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 06.c: Verify first bar color")
        bar=['Product Category:Accessories', 'Quantity Sold:511,667', 'CNT QUANTITY_SOLD_BIN_1:362992', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 06.d: Verify bar value")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1",'Quantity Sold', "Step 06:a(i) Verify Y-Axis Title")        
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 06:a(ii) Verify X-Axis Title")
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', ['Acc','Cam','Com','Med'], ['0','0.3M','0.6M','0.9M','1.2M'], 'Step06: Verify X, Y Label',3)
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_07', 'actual')
        
        """
        Step07: Click IA > Save as "C2348662" > Click Save
        Step08: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp 
        """
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7, expire_time=10)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(0.3)
        utillobj.ibfs_save_as(Test_Case_ID)
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7, expire_time=10)

        utillobj.infoassist_api_logout()
        time.sleep(2)
           
        """
        Step09: Restore saved fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348662.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'P312/S10664_binning_2',mrid='mrid',mrpass='mrpass')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7, expire_time=10)
        expected_fields=['Bar Stacked1', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Quantity,Sold', 'Horizontal Axis','Product,Category','Marker', 'Color', 'Size','CNT.QUANTITY_SOLD_BIN_1', 'Tooltip']
        metaobj.verify_query_panel_all_field(expected_fields, "Step 09.1: Verify query pane")
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7,'Step 09.2: Verify the total number of risers displayed on preview')
        
        """
        Step10: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == "__main__":
    unittest.main()