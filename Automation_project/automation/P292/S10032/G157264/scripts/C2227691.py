'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227691
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.wftools.visualization import Visualization
from common.lib import utillity

class C2227691_TestClass(BaseTestCase):
    
    def test_C2227691(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227691'
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K']
        matrix_value=['2011', '2012', '2013', '2014', '2015', '2016']
        
        """
            CLASS & OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visual = Visualization(self.driver)
        
        """
            TESTCASE CSS
        """
        querytree_css = "#queryTreeWindow"
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
              
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
         
        """    2. Double click "Quantity Sold", "Product,Category".     """
        metaobj.datatree_field_click("Quantity,Sold", 2, 1)
        visual.wait_for_visible_text(querytree_css, "Quantity,Sold")
        
        metaobj.datatree_field_click("Product,Category", 2, 1)
        visual.wait_for_visible_text(querytree_css, "Product,Category")
        
        """    3. Drag "Sale,Year" to Matrix-Columns.    """
        metaobj.drag_drop_data_tree_items_to_query_tree("Sale,Year", 1, 'Columns', 0)
        visual.wait_for_visible_text(querytree_css, "Sale,Year")
        
        """    4. Verify "Query Pane" is as shown.    """
        metaobj.verify_query_pane_field('Columns', 'Sale,Year', 1, "Step 04.01: Verify Sale,Year in Column")
        metaobj.verify_query_pane_field('Vertical Axis', 'Quantity,Sold', 1, "Step 04.02: Verify Quantity,Sold in Vertical Axis")
        metaobj.verify_query_pane_field('Horizontal Axis', 'Product,Category', 1, "Step 04.03: Verify Product Category in Horizontal Axis")
        
        """    5. Verify the following chart is displayed.    """
        xaxis_value="Sale Year : Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 05.01: Verify X-Axis Title", custom_css='.gVertTitle')
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Quantity Sold', "Step 05.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 05.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 42, 'Step 05.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!r0!c0!", "lochmara", "Step 05.05: Verify first bar color")
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", "Columns", "Sale Year", matrix_value, "Step 05.06:")
        time.sleep(5)
        
        """    6. Click "Swap".    """
        ribbonobj.select_ribbon_item('Home', 'Swap')
        time.sleep(5)
        
        """    7. Verify:
         Matrix - Rows = Sale,Year
         Vertical Axis = Product,Category
         Horizontal Axis = Quantity,Sold    """
        metaobj.verify_query_pane_field('Rows', 'Sale,Year', 1, "Step 07.01: Verify Sale,Year in Rows")
        metaobj.verify_query_pane_field('Horizontal Axis', 'Quantity,Sold', 1, "Step 07.02: Verify Quantity,Sold in Horizontal Axis")
        metaobj.verify_query_pane_field('Vertical Axis', 'Product,Category', 1, "Step 07.03: Verify Product Category in Vertical Axis")
         
        """    8. Verify the following chart is displayed.    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 08.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Quantity Sold', "Step 08.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 42, 'Step 08.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!r0!c0!", "lochmara", "Step 08.05: Verify first bar color")
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", "Rows", "Sale YearProduct Category", matrix_value, "Step 08.06:")
        time.sleep(5)
        
        """    9. Click "Save" > Save As "C2160101" > click "Save" in Save As dialog    """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        
        """    10. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
        
        """    11. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160101.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
        
        """    12. Verify the following chart is displayed.    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 12.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Quantity Sold', "Step 12.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 42, 'Step 12.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!r0!c0!", "lochmara", "Step 12.05: Verify first bar color")
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", "Rows", "Sale YearProduct Category", matrix_value, "Step 12.05:")
        time.sleep(5)
        
        """    13. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
                     
        
if __name__ == '__main__':
    unittest.main()