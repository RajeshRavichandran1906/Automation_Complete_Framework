'''
Created on Jun 15, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227719
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, metadata
from common.lib import utillity

class C2227719_TestClass(BaseTestCase):

    def test_C2227719(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227719'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        new_metaobj = metadata.MetaData(self.driver)
        
        """
            STEP  01 : Launch the IA API with wf_retail_lite, Visualization mode:
            http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
         
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1", 'Drop Measures', 120)
         
        """
            STEP 02 : Select "Insert" > "Grid".
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Grid')
        utillobj.synchronize_with_visble_text("#pfjTableChart_2", 'Drag fields', 40)
        resultobj.verify_panel_caption_label(0, 'Grid1', "Step 02.01 : Verify Grid1 is displayed")
        resultobj.verify_panel_caption_label(1, 'Bar Stacked1', "Step 02.02 : Verify Bar Stacked1 is displayed")
            
        """
            STEP 03 : Double click "Product,Category"
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f", 'Accessories', 40)
         
        """
            STEP 04 : Verify that report with relevant data is displayed in the canvas area. 
        """
        heading = ['Product Category']
        row_val=['Accessories']
        resultobj.verify_grid_column_heading('TableChart_2',heading, 'Step 04.01 : Verify column titles')
        resultobj.verify_grid_row_val('TableChart_2',row_val,'Step 04.02 : verify grid 1st row value')
         
        """
            STEP 05 : Select "Insert" > "Grid".
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Grid')
        utillobj.synchronize_with_visble_text("#pfjTableChart_3", 'Drag fields', 40)
         
        """
            STEP 06 : Verify that the canvas has split into three and left side is empty to build the new report.
        """        
        resultobj.verify_panel_caption_label(0, 'Grid2', "Step 06.01 : Verify Grid2 is displayed")
        resultobj.verify_panel_caption_label(1, 'Grid1', "Step 06.02 : Verify Grid1 is displayed")
        resultobj.verify_panel_caption_label(2, 'Bar Stacked1', "Step 06.03 : Verify Bar Stacked1 is displayed")
 
        parent_css1=self.driver.find_element_by_css_selector("#TableChart_3 .rowTitle text")
        d=utillobj.get_attribute_value(parent_css1, 'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'',"Step 06.04 : Verify Grid2 is empty")
                 
        """
            STEP 07 : Select "Product,Category", "Gender", "Sale,Quarter" and "Revenue".
        """
        metaobj.datatree_field_click("Product,Category", 2,1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody2_f", 'Product Category', 20)
         
        new_metaobj.collapse_data_field_section('Product')
        time.sleep(4)
         
        new_metaobj.collapse_data_field_section('Filters and Variables')
        time.sleep(4)
       
        metaobj.datatree_field_click("Gender", 2, 1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody2_f", 'Gender', 20)
         
        metaobj.datatree_field_click("Sale,Quarter", 2,1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody2_f", 'Sale Qua', 20)
         
        new_metaobj.collapse_data_field_section('Dimensions')
         
        metaobj.datatree_field_click("Revenue", 2,1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody2_f", 'Revenue', 20)
         
        """
            STEP 08 : Verify that those fields are displayed in the Query Pane (under Grid2 node).
        """
        metaobj.verify_query_pane_field('Grid1',"Grid2",1,"Step 08.01 : Verify Grid2")
        metaobj.verify_query_pane_field('Rows',"Product,Category",1,"Step 08.02 : Verify Rows")
        metaobj.verify_query_pane_field('Rows',"Gender",2,"Step 08.03 : Verify Rows")
        metaobj.verify_query_pane_field('Rows',"Sale,Quarter",3,"Step 08.04 : Verify Rows")
        metaobj.verify_query_pane_field('Measure',"Revenue",1,"Step 08.05 : Verify Revenue in measure")
            
        """
            STEP 09 : Verify that report with relevant data is displayed in the canvas area.
        """
        resultobj.verify_number_of_riser("TableChart_1", 1, 12, 'Step 09.01 : Verify the total number of risers in Bar Stacked1')
           
        parent_css="#TableChart_2 rect[class^='riser']"
        rise=len(self.driver.find_elements_by_css_selector(parent_css))
        utillobj.asequal(rise,7,"Step 09.02 : Verify Grid1 risers")
         
        parent_css="#TableChart_3 rect[class^='riser']"
        rise=len(self.driver.find_elements_by_css_selector(parent_css))
        utillobj.asequal(rise,56,"Step 09.03 : Verify Grid2 risers")
           
        heading = ['Product Cat...','Ge...','Sale Qu...','Revenue']
        row_val=['Accessories', 'F','1','$15,704,375.50']
        resultobj.verify_grid_column_heading('TableChart_3',heading, 'Step 09.04 : Verify column titles')
        resultobj.verify_grid_row_val('TableChart_3',row_val,'Step 09.05 : verify grid 1st row value')
           
        """
            STEP 10: Click "IA" > "Save" > "C2160087" > "Save"
        """        
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
                         
        """
            STEP 11 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
         
        """
            STEP  12: Reopen fex using IA API:
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        
        parent_css="#TableChart_2 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 90)
        
        parent_css="#TableChart_3 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 56, 45)
        
        """
            STEP 13 : Verify the following is displayed.
        """
        resultobj.verify_panel_caption_label(0, 'Grid2', "Step 13.01 : Verify Grid2 is displayed")
        resultobj.verify_panel_caption_label(1, 'Grid1', "Step 13.02 : Verify Grid1 is displayed")
        resultobj.verify_panel_caption_label(2, 'Bar Stacked1', "Step 13.03 : Verify Bar Stacked1 is displayed")
          
        heading = ['Product Category']
        row_val=['Accessories']
        
        resultobj.verify_grid_column_heading('TableChart_2',heading, 'Step 13.04 : Verify column titles')
        resultobj.verify_grid_row_val('TableChart_2',row_val,'Step 13.05 : verify grid 1st row value')
        metaobj.verify_query_pane_field('Grid1',"Grid2",1,"Step13.06 : Verify Grid2")
        metaobj.verify_query_pane_field('Rows',"Product,Category",1,"Step 13.07 : Verify Rows")
        metaobj.verify_query_pane_field('Rows',"Gender",2,"Step 13.08 : Verify Rows")
        metaobj.verify_query_pane_field('Rows',"Sale,Quarter",3,"Step 13.09 : Verify Rows")
        metaobj.verify_query_pane_field('Measure',"Revenue",1,"Step 13.10 : Verify Revenue in measure")
        resultobj.verify_number_of_riser("TableChart_1", 1, 12, 'Step 13.11 : Verify the total number of risers in Bar Stacked1')
          
        parent_css="#TableChart_2 rect[class^='riser']"
        rise=len(self.driver.find_elements_by_css_selector(parent_css))
        utillobj.asequal(rise,7,"Step 13.12 : Verify Grid1 risers")
        
        parent_css="#TableChart_3 rect[class^='riser']"
        rise=len(self.driver.find_elements_by_css_selector(parent_css))
        utillobj.asequal(rise,56,"Step 13.13 : Verify Grid2 risers")
          
        heading = ['Product Cat...','Ge...','Sale Qu...','Revenue']
        row_val=['Accessories', 'F','1','$15,704,375.50']
       
        resultobj.verify_grid_column_heading('TableChart_3',heading, 'Step 13.14 : Verify column titles')
        resultobj.verify_grid_row_val('TableChart_3',row_val,'Step 13.15 : verify grid 1st row value')
        
        
        """
            STEP 14 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
if __name__ == '__main__':
    unittest.main()