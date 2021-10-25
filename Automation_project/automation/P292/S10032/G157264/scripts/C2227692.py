'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227692
'''
import unittest
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon

class C2227692_TestClass(BaseTestCase):
    
    def test_C2227692(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227692'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """    
            STEP 01 : Launch the IA API with wf_retail_lite, Visualization mode:
            http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1", 'Drop Measures', 160)
        
        """    
            STEP 02 : Select "Home" > "Visual" > "Insert" (dropdown) > "Grid".    
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Grid')
        utillobj.synchronize_with_visble_text("#pfjTableChart_2", 'Drag fields', 15)

        """    
            STEP 03 : Verify the following is displayed.    
        """
        def_grid=driver.find_element_by_css_selector("#TableChart_2 svg>g>text.title").text.strip()
        utillobj.asequal("Drag fields here to create grid", def_grid, "Step 03a: Verify the default Grid displayed on Preview")
        def_chart=driver.find_element_by_css_selector("#TableChart_1 svg>g>text.title").text.strip()
        utillobj.asequal("Drop Measures or Sorts into the Query Pane", def_chart, "Step 03b: Verify the default Chart displayed on Preview")
        
        """    
            STEP 04 : Double click "Revenue","Product,Category".    
        """
        metaobj.datatree_field_click("Revenue", 2, 1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f", 'Revenue', 30)
        
        metaobj.datatree_field_click("Product,Category", 2, 1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f", 'Product Category', 30)
        
        """    
            STEP 05 : Verify the following is displayed in the Query pane.    
        """
        metaobj.verify_query_pane_field('Rows', 'Product,Category', 1, "Step05a: Verify Product,Category in Rows")
        metaobj.verify_query_pane_field('Measure', 'Revenue', 1, "Step05b: Verify Revenue in Measure")
        
        """    
            STEP 06 : Verify the following grid is displayed.    
        """
        heading = ['Product Category', 'Revenue',]
        row_val=['Accessories', '$129,608,338.53']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',heading, 'Step 06.1: Verify column titles')
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val,'Step 06.2: verify grid 1st row value')
        
        """    
            STEP 07 : Verify the following chart is displayed.    
        """
        def_chart=driver.find_element_by_css_selector("#TableChart_1 svg>g>text.title").text.strip()
        utillobj.asequal("Drop Measures or Sorts into the Query Pane", def_chart, "Step 07a: Verify the default Chart displayed on Preview")
        
        """    
            STEP 08 : Click "Swap".    
        """
        ribbonobj.select_ribbon_item('Home', 'Swap')
        utillobj.synchronize_with_visble_text("#queryTreeWindow table>tbody>tr:nth-child(4)", "Columns", 40)
        
        """    
            STEP 09 : Verify the following is displayed in the Query pane.    
        """
        metaobj.verify_query_pane_field('Columns', 'Product,Category', 1, "Step09a: Verify Product,Category in Columns")
        metaobj.verify_query_pane_field('Measure', 'Revenue', 1, "Step09b: Verify Revenue in Measure")
        
        """    
            STEP 10 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()