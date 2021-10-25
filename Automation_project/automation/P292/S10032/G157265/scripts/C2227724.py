'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227724
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity

class C2227724_TestClass(BaseTestCase):
    
    def test_C2227724(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """    
            STEP 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=idis&master=baseapp/wf_retail_lite
        """
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1", 'Drop Measures', 120)
        
        """    
            STEP 02 : Select "Insert" > "Grid".    
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Grid')
        utillobj.synchronize_with_visble_text("#pfjTableChart_2", 'Drag fields', 40)
        
        """    
            STEP 03 :Double click "Revenue" and "Product,Category".
        """
        metaobj.datatree_field_click("Revenue", 2, 1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f", 'Revenue', 20)
        
        metaobj.datatree_field_click("Product,Category", 2, 1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f", 'Accessories', 20)
        
        """    
            STEP 04 : Verify the two fields are showing in the Query pane.    
        """
        metaobj.verify_query_pane_field('Rows', 'Product,Category', 1, "Step 04a: Verify Product,Category in Rows")
        metaobj.verify_query_pane_field('Measure', 'Revenue', 1, "Step 04b: Verify Revenue in Measure")
        
        """    
            STEP 05 : Click "Undo".   
        """
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(4)", 'Columns', 30,  pause_time=5)
         
        """    
            STEP 06 : Verify "Product,Category" has been removed from the Query pane.    
        """
        metaobj.verify_query_pane_field('Rows', 'Columns', 1, "Step 06a: Verify Product,Category has been removed from Rows")
        
        """    
            STEP 07 : Verify "Revenue" is still showing on the Grid.    
        """
        heading = ['Revenue']
        metaobj.verify_query_pane_field('Measure', 'Revenue', 1, "Step 07a: Verify Revenue in Measure")
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',heading, 'Step 07b: Verify column titles')
        
        """    
            STEP 08 : Click "Redo".    
        """
        ribbonobj.select_top_toolbar_item('toolbar_redo')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f", 'Accessories', 30)
        
        """    
            STEP 09 : Verify "Product,Category" has been added back to the Query pane.    
        """
        heading = ['Product Category', 'Revenue']
        metaobj.verify_query_pane_field('Rows', 'Product,Category', 1, "Step 09a: Verify Product,Category in Rows")
        metaobj.verify_query_pane_field('Measure', 'Revenue', 1, "Step 09b: Verify Revenue in Measure")
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',heading, 'Step 09c: Verify column titles')
        
        """    
            STEP 10 : Click "Undo" 3 times    
        """
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(4)", 'Columns', 20)
        
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        utillobj.synchronize_with_visble_text("#pfjTableChart_2", 'Drag fields', 20)
        
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(2)", 'Matrix', 20)
            
        """    
            STEP 11 : Verify "Undo" button is disabled.    
        """
        disabled =self.driver.find_element_by_css_selector("#undoButton").get_attribute('disabled')                
        utillobj.asequal(disabled, 'true', "Step 11a: Verify 'Undo' button is disabled")
        
        """    
            STEP 12 : Verify "Grid1" canvas has been removed.    
        """
        try:
            def_grid=self.driver.find_element_by_css_selector("#TableChart_2 svg>g>text.title").text.strip()
            utillobj.asequal(True, def_grid, "Step 12a: Verify the default Grid displayed on Preview")
        except:
            utillobj.asequal(False, False, "Step 12a: Verify the default Grid1 has been removed")
            
        """    
            STEP 13 : Verify all the data has been removed and only the default gray chart displayed.    
        """
        def_chart=self.driver.find_element_by_css_selector("#TableChart_1 svg>g>text.title").text.strip()
        utillobj.asequal("Drop Measures or Sorts into the Query Pane", def_chart, "Step 13a: Verify the default Chart displayed on Preview")
        
        """    
            STEP 14 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        
if __name__ == '__main__':
    unittest.main()