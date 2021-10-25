'''
Created on July 3, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234974
TestCase Name = Matrix Pie chart throws type error with field in size bucket (166183)
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_resultarea,metadata
from common.lib import utillity
from common.lib.utillity import UtillityMethods


class C2234974_TestClass(BaseTestCase):

    def test_C2234974(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        metadataobj1=metadata.MetaData(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        Test_Case_ID="C2234974"
        
        
        """ Step 1: Launch WF, New > Visualization 
                    using the wf-retail-lite file.
                    Select "Change" (dropdown) > Pie.
                    Expect to see the following Visualization preview pane.
        """
        
        utillobj.infoassist_api_login('idis', 'baseapp/wf_retail_lite', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 text[class='title']"
        #result_obj.wait_for_property(parent_css, 1, string_value="DropMeasuresorSortsintotheQueryPane", with_regular_exprestion=True)
        utillobj.synchronize_with_visble_text(parent_css,"DropMeasuresorSortsintotheQueryPane", 15)
        parent_css="#TableChart_1 .chartPanel rect[class*='riser']"
        #result_obj.wait_for_property(parent_css, 12)
        utillobj.synchronize_with_number_of_element(parent_css,12,25)
        time.sleep(2)
        ribbonobj.change_chart_type("pie")
        parent_css="#TableChart_1 text[class='title']"
        result_obj.wait_for_property(parent_css, 1, string_value="DropMeasuresorSortsintotheQueryPane", with_regular_exprestion=True)
        parent_css="#TableChart_1 .chartPanel path[class*='riser']"
        #result_obj.wait_for_property(parent_css, 8)
        utillobj.synchronize_with_number_of_element(parent_css,8,25)
        time.sleep(2)
          
        """ step 2: Double click "Quantity,Sold", "Sale,Day".
                    Drag "Store Type" to Matrix - Rows.
                    Drag "Product,Subcategory" to Matrix - Columns.
                    Drag "Cost of Goods" to Metric - Size
        """
        metadataobj.datatree_field_click('Quantity,Sold', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class*='pieLabel']"
        utillobj.synchronize_with_visble_text(parent_css, "QuantitySold", 20)
        metadataobj.datatree_field_click('Sale,Day', 2, 1)
        parent_css="#TableChart_1 g.legend-clip g.legend text[class*='legend-title']"
        utillobj.synchronize_with_visble_text(parent_css, "SaleDay", 20)
        parent_css="#TableChart_1 g.legend-clip g.legend path[class*='legend-marker']"
        utillobj.synchronize_with_number_of_element(parent_css,31,25) 
        #metadataobj.datatree_field_click('Store Type', 1, 1, 'Add To Query', 'Rows')
        metadataobj1.collapse_data_field_section("Filters and Variables")
        metadataobj1.collapse_data_field_section("Sales->Measure Groups")
        metadataobj.drag_drop_data_tree_items_to_query_tree('Dimensions->Store->Store Name->Store, Name Details->Store Type', 1, 'Rows', 0)
        parent_css="#TableChart_1 text[class*='rowHeader-label']"
        utillobj.synchronize_with_visble_text(parent_css, "StoreType", 15)
        time.sleep(2)
          
        #metadataobj.datatree_field_click('Product,Subcategory', 1, 1, 'Add To Query', 'Columns')
        metadataobj1.collapse_data_field_section("Store, Name Details->Store Name->Store")
        metadataobj.drag_drop_data_tree_items_to_query_tree('Product->Product,Subcategory', 1,'Columns', 0)
        parent_css="#TableChart_1 text[class*='colHeader-label']"
#         utillobj.synchronize_with_visble_text(parent_css, "ProductSubcategory", 15)
        time.sleep(5) 
        metadataobj.datatree_field_click('Cost of Goods', 1, 1, 'Add To Query', 'Size')
        parent_css="#TableChart_1 g.legend text[class='sizeLegend-title']"
        utillobj.synchronize_with_visble_text(parent_css, "CostofGoods", 15)
        parent_css="#TableChart_1 g.legend circle[class*='sizeLegend']"
        utillobj.synchronize_with_number_of_element(parent_css,3,25)  
        """ Step 3: Hover over the lowest slice for the upper-left PIE for 
                    Store Front/Blu Ray.
                    Verify the larger magnitude of the values in the Tooltip data.
        """
        br1 = UtillityMethods.parseinitfile(self,'browser')
        expected_tooltip_list=['Store Type:Store Front', 'Product Subcategory:Blu Ray', 'Sale Day:16', 'Quantity Sold:15,494  (3.28%)', 'Cost of Goods:$4,124,029.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to', 'Drill down to Model']
        result_obj.verify_default_tooltip_values('TableChart_1', 'riser!s15!g0!mwedge!r0!c0', expected_tooltip_list, 'Step 3.1: verify the default tooltip values', cord_type='bottom_left', x_offset=5, y_offset=-7, mouse_duration=2.5)
        result_obj.verify_visualization_row_column_header_labels('TableChart_1', 'Rows', 'Store Type', ['Store Front', 'Web'], 'Step 3.2: Verify Row header and Row label')
        colheader_ff=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Po...', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Sy...', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote...', 'Video Editing', 'iPod Docking Stat...']
        colheader_def=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Po...', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Sy...', 'Portable TV', 'Professional']
        
        if br1=="Firefox":
            result_obj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Product Subcategory', colheader_ff, 'Step 3.3: Verify columns header and Row label')
        else:
            result_obj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Product Subcategory', colheader_def, 'Step 3.3: Verify columns header and Row label')
        
        expected_list_def=['Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold']
        result_obj.verify_data_labels('TableChart_1', expected_list_def, "Step 3.4:",data_label_length=5,custom_css="text[class*='pieLabel']")
        expected_label_list=['Sale Day', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', 
                             '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 3.5 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s15!g0!mwedge!r0!c0', 'pale_yellow_3', 'Step 3.6: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1175, 'Step 3.7: Verify Number of circle')
        time.sleep(5)
         
        
        """ Step 4: Hover over the lowest slice for the bottom-right PIE for Web/Flat Panel TV.
                    Verify the smaller magnitude of the values in the Tooltip data.
        """
        tooltip_list_cr=['Store Type:Web', 'Product Subcategory:Flat Panel TV', 'Sale Day:18', 'Quantity Sold:881  (3.13%)', 'Cost of Goods:$550,704.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to', 'Drill down to Model']
        tooltip_list_ff=['Store Type:Web', 'Product Subcategory:Flat Panel TV', 'Sale Day:17', 'Quantity Sold:879  (3.12%)', 'Cost of Goods:$547,296.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to', 'Drill down to Model']
        
        if br1=="Firefox" or br1=="IE":
            result_obj.verify_default_tooltip_values('TableChart_1', 'riser!s16!g0!mwedge!r1!c6', tooltip_list_ff, 'Step 4.1: verify the default tooltip values', cord_type='bottom_left', x_offset=1.9, y_offset=-2.7, mouse_duration=2.5)
        else:
            result_obj.verify_default_tooltip_values('TableChart_1', 'riser!s16!g0!mwedge!r1!c6', tooltip_list_cr, 'Step 4.1: verify the default tooltip values', cord_type='bottom_left', x_offset=1.9, y_offset=-2.7, mouse_duration=2.5)
        
        time.sleep(5)
        utillobj.switch_to_default_content(pause=5)
        time.sleep(7)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step4', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        
        
if __name__ == '__main__':
    unittest.main()