'''
Created on June 9, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234972
TestCase Name = AHTML: JSCHART: Pie showing empty circle for null data (166076)
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_resultarea,metadata
from common.lib import utillity

class C2234972_TestClass(BaseTestCase):

    def test_C2234972(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        metadataobj1=metadata.MetaData(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        
        """ Step 1: Launch WF, New > Visualization 
                    using the wf-retail-lite file.
                    Select "Change" (dropdown) > Pie.
        """
        utillobj.infoassist_api_login('idis', 'baseapp/wf_retail_lite', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 text[class='title']"
        utillobj.synchronize_with_visble_text(parent_css, 'DropMeasuresorSortsintotheQueryPane',ia_resultobj.home_page_long_timesleep )
                
        ribbonobj.change_chart_type("pie")
        parent_css="#TableChart_1 text[class='title']"
        utillobj.synchronize_with_visble_text(parent_css, 'DropMeasuresorSortsintotheQueryPane',ia_resultobj.home_page_medium_timesleep)
        
        
        """ step 2: Double click "Quantity,Sold", "Sale,Day".
                    Drag "Store Type" to Matrix - Rows.
                    Drag "Product,Subcategory" to Matrix - Columns.
        """
        metadataobj.datatree_field_click('Quantity,Sold', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class*='pieLabel']"
        utillobj.synchronize_with_visble_text(parent_css, 'QuantitySold', ia_resultobj.home_page_medium_timesleep)
        
        metadataobj.datatree_field_click('Sale,Day', 2, 1)
        parent_css="#TableChart_1 g.legend-clip g.legend text[class*='legend-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'SaleDay', ia_resultobj.home_page_medium_timesleep)
        
        parent_css="#TableChart_1 g.legend-clip g.legend path[class*='legend-marker']"
        utillobj.synchronize_with_number_of_element(parent_css, 31, ia_resultobj.home_page_medium_timesleep)
        
#         metadataobj1.collapse_data_field_section("Sales->Measure Groups")
        metadataobj1.collapse_data_field_section("Filters and Variables")
        metadataobj.drag_drop_data_tree_items_to_query_tree_('Store Type', 1, 'Rows', 0)
        
        parent_css="#TableChart_1 text[class*='rowHeader-label']"
        utillobj.synchronize_with_visble_text(parent_css, 'StoreType', ia_resultobj.home_page_medium_timesleep)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree_('Product,Subcategory', 1,'Columns', 0)
        parent_css="#TableChart_1 text[class*='colHeader-label']"
        utillobj.synchronize_with_visble_text(parent_css, 'ProductSubcategory', ia_resultobj.home_page_medium_timesleep)
        
        result_obj.verify_visualization_row_column_header_labels('TableChart_1', 'Rows', 'Store Type', ['Store Front', 'Web'], 'Step 02.01:')
        expected_label_cr=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Po...', 'Flat Panel TV', 'Handheld']

        result_obj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Product Subcategory', expected_label_cr, 'Step 02.02:')

        expected_list_cr=['Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold']
        result_obj.verify_data_labels('TableChart_1', expected_list_cr, "Step 02.03: Verify data labels",data_label_length=5,custom_css="text[class*='pieLabel']")
        expected_label_list=['Sale Day', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', 
                             '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 02.04:')
        utillobj.verify_chart_color('TableChart_1', 'riser!s2!g0!mwedge!r1!c4', 'dark_green', 'Step 02.05: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1175, 'Step 02.06: Verify Number of circle')
        
         
        """ Step 3: Select "Change" (dropdown) > Ring Pie.
        """
        
        ribbonobj.change_chart_type("ring_pie")
        time.sleep(8) #its added as its not loading it just became blank
        parent_css="#TableChart_1 text[class*='pieLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 38, ia_resultobj.home_page_long_timesleep)
        
        
        result_obj.verify_visualization_row_column_header_labels('TableChart_1', 'Rows', 'Store Type', ['Store Front', 'Web'], 'Step 03.01: Verify Row header and Row label')
        expected_label_cr=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Po...', 'Flat Panel TV', 'Handheld']

        result_obj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Product Subcategory',expected_label_cr , 'Step 03.02: Verify columns header and Row label')
            
        expected_list_def=['Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold']
        result_obj.verify_data_labels('TableChart_1', expected_list_def, "Step 03.03: Verify data label",data_label_length=5,custom_css="text[class*='pieLabel']")
        
        expected_list1_cr=['472K', '9,370', '4,638', '73,006', '18,742', '5,694']
        result_obj.verify_data_labels('TableChart_1', expected_list1_cr, "Step 03.04: Verify data label",data_label_length=6,custom_css="text[class*='totalLabel']")
        expected_label_list=['Sale Day', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', 
                             '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 03.05: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s2!g0!mwedge!r1!c4', 'dark_green', 'Step 03.06: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1175, 'Step 03.07: Verify Number of circle')
        
        utillobj.switch_to_default_content(pause=5)
        
if __name__ == '__main__':
    unittest.main()