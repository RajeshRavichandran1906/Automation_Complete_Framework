'''
Created on Nov 7, 2017

@author: BM13368
Testcase_Name :Create Datagrid Chart 
Testcase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2333145&group_by=cases:section_id&group_id=171044&group_order=asc
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib import utillity

class C2333145_TestClass(BaseTestCase):

    def test_C2333145(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2333145'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        parent_css="#queryTreeWindow"
        
        """
            Step 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10660_chart_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1", 1, 65)
        
        """
            Step 02 : Select Format > Chart type > Other > HTML5 > Datagrid
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('html5', 'html5_DataGrid', 6, ok_btn_click=True)
        
        """
            Step 03 : Double click Product,Category
        """
        metadataobj.datatree_field_click('Product,Category', 2, 0)
        utillobj.synchronize_with_visble_text(parent_css, 'Product,Category', 20)        
        heading = ['Product Category']
        resultobj.verify_grid_column_heading('TableChart_1', heading, 'Step 03.01: Verify first column title')
        row_val=['Accessories']
        
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step 03.02: verify grid 1st row value')
        
        """
            Verification : Product Category is added to Rows bucket and shows in preview as first column.
        """
        metadataobj.verify_query_pane_field('Rows', 'Product,Category', 1, "Step 03.03")
        
        """
            Step 04 : Double click Cost of Goods, Discount, Gross Profit and Revenue
        """
        metadataobj.datatree_field_click('Cost of Goods', 2, 0)
        utillobj.synchronize_with_visble_text(parent_css, 'Cost of Goods', 20)
        
        metadataobj.datatree_field_click('Gross Profit', 2, 1)
        utillobj.synchronize_with_visble_text(parent_css, "Gross Profit", 15)

        metadataobj.datatree_field_click('Discount', 2, 2)
        utillobj.synchronize_with_visble_text(parent_css, "Discount", 15)

        metadataobj.datatree_field_click('Revenue', 2, 3)
        utillobj.synchronize_with_visble_text(parent_css, "Revenue", 15)
        
        """
            Verification : All measures are added to Measures bucket and show as additional columns in preview.
        """
        metadataobj.verify_query_pane_field('Measure', 'Cost of Goods', 1, "Step 04.01")
        metadataobj.verify_query_pane_field('Cost of Goods', 'Gross Profit', 1, "Step 04.02")
        metadataobj.verify_query_pane_field('Gross Profit', 'Discount', 1, "Step 04.03")
        metadataobj.verify_query_pane_field('Discount', 'Revenue', 1, "Step 04.04")
        
        heading = ['Product Category', 'Cost of Goods', 'Gross Profit','Discount','Revenue']
        resultobj.verify_grid_column_heading('TableChart_1',heading, 'Step 04.05: Verify data-grid column title')
        
        row_val=['Accessories','$89,753,898.00','$39,854,440.53','$6,014,845.52','$129,608,338.53']
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step 04.06: verify grid 1st row values')
        
        """
            Step 05 : Click Auto Drill button in the Run With section of Format tab.
        """
        ribbonobj.select_visualization_ribbon_item('Format', 'auto_drill')
        time.sleep(3)
        
        """
            Step 06 : Run, hover over measure columns
            Verification : Each cell is a link (the cursor changes to pointing finger).
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(frame_css="iframe[src*='contentDrill']")
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 rect[class='riser!s0!g0!mcellFill!r0!c0!'] + text", "$89,753,898.00", 60)
        
        expected_tooltip=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step 06.01: verify the default tooltip values")
        
        """
            Step 07 : Click Drill down to Product, Subcategory of the cell of Accessories and Cost of Goods
        """
        resultobj.select_drilldown_tooltip_menu("jschart_HOLD_0", "riser!s0!g0!mcellFill!r0!c0!", "Drill down to Product Subcategory")
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 rect[class='riser!s0!g0!mcellFill!r0!c0!'] + text", "$2,052,711.00", 30)
        
        """
            Verification : Chart for Accessories subcategories displays.
        """
        heading = ['Product Subcategory', 'Cost of Goods', 'Gross Profit','Discount','Revenue']
        resultobj.verify_grid_column_heading('jschart_HOLD_0',heading, 'Step 07.01: Verify data-grid column title')
        row_val=['Charger','$2,052,711.00','$1,970,123.91','$187,485.88','$4,022,834.91']
        resultobj.verify_grid_row_val('jschart_HOLD_0',row_val,'Step 07.02: verify grid 1st row values')
        
        """
            Step 08: Click Save in the toolbar > Save as "C2333145" > Click Save 
        """
        utillobj.switch_to_default_content(pause=1)  
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 09 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
    
        """
            Step 10 : Run the chart from bip\
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10660&BIP_item=C2333145.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10660_chart_2", 'mrid', 'mrpass')
        utillobj.switch_to_frame(frame_css="iframe[src*='contentDrill']")
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 rect[class='riser!s0!g0!mcellFill!r0!c0!'] + text", "$89,753,898.00", 60)
        resultobj.verify_grid_column_heading('jschart_HOLD_0',heading, 'Step 10.01: Verify data-grid column title')
        
        """
            Step 11 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 12: Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2333145.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_2', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1", 'Product Category', 65)        
        heading = ['Product Category', 'Cost of Goods', 'Gross Profit','Discount','Revenue']
        resultobj.verify_grid_column_heading('pfjTableChart_1',heading, 'Step 11.01: Verify data-grid column title')
        row_val=['Accessories','$89,753,898.00','$39,854,440.53','$6,014,845.52','$129,608,338.53']
        resultobj.verify_grid_row_val('pfjTableChart_1',row_val,'Step 11.02: verify grid 1st row values')
        
        """
            Step 13: Logout using API
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == "__main__":
    unittest.main()