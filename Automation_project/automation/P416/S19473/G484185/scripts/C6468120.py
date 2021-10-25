from common.lib.basetestcase import BaseTestCase
from common.wftools.pyunit_iatree import Pyunit_IAtree as pyunit_test_object
import unittest

class C6468120_TestClass(BaseTestCase):
        
    def test_C6468120(self):
        
        master_file_name = 'retail_lite'
        root_level_child_component_css="[data-ibx-type='mdTree'] > [data-ibx-type='ibxTreeNode']"
        max_number_of_field_component=3
        synchronize_time=60
        '''
        Step 01: Open a browser
        Go to your WF environment where stand-alone metadata tree container is hosted
        i.e : http://machine:port/{alias}/{yourDirectory}/{yourFile.jsp}?{patameter=value}
        param = "IBIMR_folder"
        value = masterFile (retail_lite.json)
        http://wfqa1:58080/ibi_apps/zand/iaTreeTestQA.jsp?IBIMR_folder=retail_lite.json
        '''
        pyunit_test_object.invoke_metadata_tree_container_page(self, master_file_name)
        pyunit_test_object.wait_for_number_of_element(self, root_level_child_component_css, max_number_of_field_component, synchronize_time)
        root_node_expected_items_list=pyunit_test_object.get_expected_child_list(self, master_file_name, 'root')
        root_elements_image_name_dict=pyunit_test_object.get_expected_child_and_image_dict(self, master_file_name, 'root')
        for tree_item_name in root_node_expected_items_list:
            icon_type = root_elements_image_name_dict[tree_item_name]
            pyunit_test_object.verify_root_icon_type(self, tree_item_name, icon_type, '01')
        '''
        Step 02: Expand "Filters and Variables" node".
        Step 03: Expand "Measures Groups" node.
        Step 03: Expand "Dimension"
        '''
        step_no = '2'
        for parent_node_name in ['Filters and Variables', 'Measure Groups', 'Dimensions', 'Shipment_Related']:
            pyunit_test_object.expand_plus_tree_node(self, master_file_name, parent_node_name)
            parent_node_expected_items_list=pyunit_test_object.get_expected_child_list(self, master_file_name, parent_node_name)
            child_elements_image_name_dict=pyunit_test_object.get_expected_child_and_image_dict(self, master_file_name, parent_node_name)
            for tree_item_name in parent_node_expected_items_list:
                icon_type = child_elements_image_name_dict[tree_item_name]
                pyunit_test_object.verify_treenode_icon_type(self, parent_node_name, tree_item_name, icon_type, str(step_no))
            step_no = str(eval(step_no) + 1)
        '''
        Step 04: Close browser
        '''
if __name__ == '__main__':
    unittest.main()