'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227691
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity

class C2227691_TestClass(BaseTestCase):
    def test_C2227691(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227691'
        bar=['Sale Year:2013', 'Product Category:Stereo Systems', 'Quantity Sold:100,263', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K']
        matrix_value=['2011', '2012', '2013', '2014', '2015', '2016']
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
              
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
         
        """    2. Double click "Quantity Sold", "Product,Category".     """
        metaobj.datatree_field_click("Quantity,Sold", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(8)
        
        """    3. Drag "Sale,Year" to Matrix-Columns.    """
        metaobj.datatree_field_click("Sale,Year", 1, 1, "Add To Query", "Columns")
        time.sleep(8)
        
        """    4. Verify "Query Pane" is as shown.    """
        metaobj.verify_query_pane_field('Columns', 'Sale,Year', 1, "Step04a: Verify Sale,Year in Column")
        metaobj.verify_query_pane_field('Vertical Axis', 'Quantity,Sold', 1, "Step04b: Verify Quantity,Sold in Vertical Axis")
        metaobj.verify_query_pane_field('Horizontal Axis', 'Product,Category', 1, "Step04c: Verify Product Category in Horizontal Axis")
        
        """    5. Verify the following chart is displayed.    """
        time.sleep(5)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c2!", bar, "Step05: Verify bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step05:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Quantity Sold', "Step05:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step05:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 42, 'Step05.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!r0!c0!", "lochmara", "Step05.c: Verify first bar color")
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", "Columns", "Sale Year", matrix_value, "Step05.d:")
        time.sleep(5)
        
        """    6. Click "Swap".    """
        ribbonobj.select_ribbon_item('Home', 'Swap')
        time.sleep(5)
        
        """    7. Verify:
         Matrix - Rows = Sale,Year
         Vertical Axis = Product,Category
         Horizontal Axis = Quantity,Sold    """
        metaobj.verify_query_pane_field('Rows', 'Sale,Year', 1, "Step07a: Verify Sale,Year in Rows")
        metaobj.verify_query_pane_field('Horizontal Axis', 'Quantity,Sold', 1, "Step07b: Verify Quantity,Sold in Horizontal Axis")
        metaobj.verify_query_pane_field('Vertical Axis', 'Product,Category', 1, "Step07c: Verify Product Category in Vertical Axis")
         
        """    8. Verify the following chart is displayed.    """
        time.sleep(5)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!r2!c0!", bar, "Step08: Verify bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step08:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Quantity Sold', "Step08:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step08:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 42, 'Step08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!r0!c0!", "lochmara", "Step08.c: Verify first bar color")
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", "Rows", "Sale YearProduct Category", matrix_value, "Step08.d:")
        time.sleep(5)
        
        """    9. Click "Save" > Save As "C2160101" > click "Save" in Save As dialog    """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        
        """    10. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
        
        """    11. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160101.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    12. Verify the following chart is displayed.    """
        time.sleep(5)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!r2!c0!", bar, "Step12: Verify bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step12:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Quantity Sold', "Step12:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 42, 'Step08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!r0!c0!", "lochmara", "Step12.c: Verify first bar color")
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", "Rows", "Sale YearProduct Category", matrix_value, "Step12.d:")
        time.sleep(5)
        
        """    13. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
                     
        
if __name__ == '__main__':
    unittest.main()

