'''
Created on Jan 11, 2018

@author: Kiruthika
TestSuite : 8202 New Features and product changes for existing functionality
TestCase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348444
TestCase Name: If bin field added to Columns it is treated as BY
'''
import unittest,time
from common.lib import utillity
from common.pages import ia_resultarea,visualization_resultarea,visualization_metadata,visualization_ribbon
from common.wftools.visualization import Visualization
from common.lib.basetestcase import BaseTestCase

class C2348444_TestClass(BaseTestCase):

    def test_C2348444(self):

        utillobj = utillity.UtillityMethods(self.driver)
        iaresult= ia_resultarea.IA_Resultarea(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj=visualization_ribbon.Visualization_Ribbon(self.driver)
        visual = Visualization(self.driver)
        Test_Case_ID = 'C2348444'
        
        
        """
        Step01: Restore C2348443.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348443.fex
        """
        utillobj.infoassist_api_edit('C2348444_Base', 'idis', 'P312/S10664_binning_2',mrid='mrid',mrpass='mrpass')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 28, iaresult.home_page_long_timesleep)
          
        """
        Step02: Drag and drop "QUANTITY_SOLD_BIN_1" bin from Rows to Columns
        """
        metaobj.drag_and_drop_query_items("QUANTITY_SOLD_BIN_1", "Columns")
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", 'Quantity Sold', 80)
         
        """
        Step03: Verify bin added to columns bucket and preview updated
        4 columns are showing in preview.
        """
        expected_fields=['Bar Stacked1', 'Matrix', 'Rows', 'Columns','QUANTITY_SOLD_BIN_1', 'Axis', 'Vertical Axis', 'Quantity,Sold', 'Horizontal Axis','Product,Category','Marker', 'Color', 'Size', 'Tooltip']
        metaobj.verify_query_panel_all_field(expected_fields, "Step 03.01: Verify query pane")
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 28, expire_time=45)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 28,'Step 03.02: Verify the total number of risers displayed on preview')
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns','QUANTITY_SOLD_BIN_1 : Product Category', ['1', '2', '3', '4'], "Step 03.c: Verify Column header",1)
        
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step 03.03: Verify first bar color")
        bar=['QUANTITY_SOLD_BIN_1:1', 'Product Category:Accessories', 'Quantity Sold:236,127', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", bar, "Step 03.04: Verify bar value")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1",'Quantity Sold', "Step 03.05: Verify Y-Axis Title")        
#         resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 03:a(ii) Verify X-Axis Title")
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', ['Acc','Cam','Com','Med'], ['0','100K','200K','300K','400K','500K','600K'], 'Step 03.06: Verify X, Y Label',3)
            
        """ 
        Step04: Click view source icon to view fex code generated
        Verify "QUANTITY_SOLD_BIN_1" added as by field
        Step05: Close view source code window
        """
        expected_syntax_list=["SUM WF_RETAIL_LITE.WF_RETAIL_SALES.QUANTITY_SOLD","BY QUANTITY_SOLD_BIN_1","BY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY","TYPE=DATA, COLUMN=N1, BUCKET=column, $"]
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 05.01: Verify bin is showing as BY')
        
        """
        Step06: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        visual.switch_to_new_window()
        parent_css="#MAINTABLE_wbody1 [class^='riser!']"
        utillobj.synchronize_with_number_of_element(parent_css, 28, iaresult.home_page_long_timesleep)
        
        """
        Step07: Hover on the run time chart and verify tool tip values
        """
       
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 28,'Step 07.01: Verify the total number of risers displayed on preview')
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns','QUANTITY_SOLD_BIN_1 : Product Category', ['1', '2', '3', '4'], "Step 07.02: Verify Column header",1)
        
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step 07.03: Verify first bar color")
        bar=['QUANTITY_SOLD_BIN_1:1', 'Product Category:Accessories', 'Quantity Sold:236,127', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", bar, "Step 07.04: Verify bar value")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1",'Quantity Sold', "Step 07.05: Verify Y-Axis Title")        
#         resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 07:a(ii) Verify X-Axis Title")
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', ['Acc','Cam','Com','Med'], ['0','100K','200K','300K','400K','500K','600K'], 'Step 07.06: Verify X, Y Label',3)
#         utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_07', 'actual')
        
        """
        Step08: Dismiss run window
        Step09: Click IA > Save as "C2348444" > Click Save
        Step10: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp 
        """
        visual.switch_to_previous_window()
        time.sleep(2)
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 28, iaresult.home_page_long_timesleep)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(0.3)
        utillobj.ibfs_save_as(Test_Case_ID)
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 28, iaresult.home_page_long_timesleep)
        utillobj.infoassist_api_logout()
        time.sleep(2)
           
        """
        Step11: Restore saved fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348443.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'P312/S10664_binning_2',mrid='mrid',mrpass='mrpass')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 28, iaresult.home_page_long_timesleep)
        
        expected_fields=['Bar Stacked1', 'Matrix', 'Rows', 'Columns','QUANTITY_SOLD_BIN_1', 'Axis', 'Vertical Axis', 'Quantity,Sold', 'Horizontal Axis','Product,Category','Marker', 'Color', 'Size', 'Tooltip']
        metaobj.verify_query_panel_all_field(expected_fields, "Step 11.01: Verify query pane")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 28,'Step 11.02: Verify the total number of risers displayed on preview')
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns','QUANTITY_SOLD_BIN_1 : Product Category', ['1', '2', '3', '4'], "Step 11.03: Verify Column header",1)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step 11.04: Verify first bar color")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1",'Quantity Sold', "Step 11.05: Verify Y-Axis Title")        
#         resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 11.6: Verify X-Axis Title")
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', ['Acc','Cam','Com','Med'], ['0','100K','200K','300K','400K','500K','600K'], 'Step 11.07: Verify X, Y Label',3)
         
        """
        Step12: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == "__main__":
    unittest.main()