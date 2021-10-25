from common.lib.basetestcase import BaseTestCase
from common.wftools.pyunit_iatree import Pyunit_IAtree as pyunit_test_object
import unittest

class C6461068_TestClass(BaseTestCase):
        
    def test_C6461068(self):
        
        master_file_name = 'retail_lite'
        expected_number_of_field_component_css="[data-ibx-type='mdTree'] > [data-ibx-type='ibxTreeNode']"
        max_number_of_field_component=3
        synchronize_time=60
        colapse_dimensions_node = 'Dimensions'
        colapse_sales_related_node = 'Sales_Related'
        colapse_product_node = 'Product'
        colapse_shipment_related_node = 'Shipment_Related'
        colapse_store_node = 'Store'
        colapse_customer_node = 'Customer'
        '''
        Step 01: Go to your WF environment where stand-alone metadata tree container is hosted 
        i.e : http://machine:port/{alias}/{yourDirectory}/{yourFile.jsp}?{patameter=value}
        param = "IBIMR_folder"
        value = masterFile (retail_lite.json)
        
        http://wfqa1:58080/ibi_apps/zand/iaTreeTestQA.jsp?IBIMR_folder=retail_lite.json
        '''
        pyunit_test_object.invoke_metadata_tree_container_page(self, master_file_name)
        pyunit_test_object.wait_for_number_of_element(self, expected_number_of_field_component_css, max_number_of_field_component, synchronize_time)
        '''
        Step 02: Expand "Dimension" node
        '''
        pyunit_test_object.expand_plus_tree_node(self, master_file_name, 'Dimensions')
        pyunit_test_object.verify_child_list_in_expanded_tree_node(self, master_file_name, 'Dimensions', '02')
        '''
        Step 03: Expand all child nodes:
                Sales_Related
                Product
                Shipment_Related
                Store
                Customer
        '''
        pyunit_test_object.expand_plus_tree_node(self, master_file_name, 'Sales_Related')
        pyunit_test_object.verify_child_list_in_expanded_tree_node(self, master_file_name, 'Sales_Related', '03.01')
        pyunit_test_object.expand_plus_tree_node(self, master_file_name, 'Product')
        pyunit_test_object.verify_child_list_in_expanded_tree_node(self, master_file_name, 'Product', '03.02')
        pyunit_test_object.expand_plus_tree_node(self, master_file_name, 'Shipment_Related')
        pyunit_test_object.verify_child_list_in_expanded_tree_node(self, master_file_name, 'Shipment_Related', '03.03')
        pyunit_test_object.expand_plus_tree_node(self, master_file_name, 'Store')
        pyunit_test_object.verify_child_list_in_expanded_tree_node(self, master_file_name, 'Store', '03.04')
        pyunit_test_object.expand_plus_tree_node(self, master_file_name, 'Customer')
        pyunit_test_object.verify_child_list_in_expanded_tree_node(self, master_file_name, 'Customer', '03.05')
        '''
        Step 04: Expand all grand-child node:
        Customer,Postal,Code >> Customer, Postal Code Details
        '''
        pyunit_test_object.expand_plus_tree_node(self, master_file_name, 'Customer, Postal Code Details')
        pyunit_test_object.verify_child_list_in_expanded_tree_node(self, master_file_name, 'Customer, Postal Code Details', '04')
        '''
        Step 05: Collapse all expanded nodes
        '''
        pyunit_test_object.colapse_plus_tree_node(self, colapse_customer_node)
        pyunit_test_object.colapse_plus_tree_node(self, colapse_store_node)
        pyunit_test_object.colapse_plus_tree_node(self, colapse_shipment_related_node)
        pyunit_test_object.colapse_plus_tree_node(self, colapse_product_node)
        pyunit_test_object.colapse_plus_tree_node(self, colapse_sales_related_node)
        pyunit_test_object.colapse_plus_tree_node(self, colapse_dimensions_node)
        expected_node_items_list=['Filters and Variables', 'Measure Groups', 'Dimensions']
        pyunit_test_object.verify_all_visible_nodes(self, expected_node_items_list, '05')
        '''
        Step 06: Close browser
        '''
if __name__ == '__main__':
    unittest.main()