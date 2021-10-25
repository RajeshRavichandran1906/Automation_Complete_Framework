from common.lib.basetestcase import BaseTestCase
from common.wftools.pyunit_iatree import Pyunit_IAtree as pyunit_test_object
import unittest

class C6461070_TestClass(BaseTestCase):
        
    def test_C6461070(self):
        
        master_file_name = 'retail_lite'
        expected_number_of_field_component_css="[data-ibx-type='mdTree'] > [data-ibx-type='ibxTreeNode']"
        max_number_of_field_component=3
        synchronize_time=60
        parent_node_name = 'Sales'
        '''
        Step 01: Open a browser
        Go to your WF environment where stand-alone metadata tree container is hosted
        i.e : http://machine:port/{alias}/{yourDirectory}/{yourFile.jsp}?{patameter=value}
        param = "IBIMR_folder"
        value = masterFile (retail_lite.json)
        http://wfqa1:58080/ibi_apps/zand/iaTreeTestQA.jsp?IBIMR_folder=retail_lite.json
        '''
        pyunit_test_object.invoke_metadata_tree_container_page(self, master_file_name)
        pyunit_test_object.wait_for_number_of_element(self, expected_number_of_field_component_css, max_number_of_field_component, synchronize_time)
        '''
        Step 02: Expand "Measure Groups" and "Sales" nodes.
        '''
        pyunit_test_object.expand_plus_tree_node(self, master_file_name, parent_node_name)
        parent_node_expected_items_list=pyunit_test_object.get_expected_child_list(self, master_file_name, parent_node_name)
        child_elements_image_name_dict=pyunit_test_object.get_expected_child_and_image_dict(self, master_file_name, parent_node_name)
        for tree_item_name in parent_node_expected_items_list:
            icon_type = child_elements_image_name_dict[tree_item_name]
            pyunit_test_object.verify_treenode_icon_type(self, parent_node_name, tree_item_name, icon_type, '02')
            
        '''
        Step 03: Close browser
        '''
if __name__ == '__main__':
    unittest.main()