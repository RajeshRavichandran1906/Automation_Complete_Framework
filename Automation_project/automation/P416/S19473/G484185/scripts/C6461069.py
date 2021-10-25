from common.lib.basetestcase import BaseTestCase
from common.wftools.pyunit_iatree import Pyunit_IAtree as pyunit_test_object
import unittest

class C6461069_TestClass(BaseTestCase):
        
    def test_C6461069(self):
        
        master_file_name = 'retail_lite'
        expected_number_of_field_component_css="[data-ibx-type='mdTree'] > [data-ibx-type='ibxTreeNode']"
        max_number_of_field_component=3
        synchronize_time=60
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
        Step 02: Expand "Filters and Variables" node and it's child nodes
        '''
        pyunit_test_object.expand_plus_tree_node(self, master_file_name, 'Filters and Variables')
        pyunit_test_object.verify_child_list_in_expanded_tree_node(self, master_file_name, 'Filters and Variables', '02')
        pyunit_test_object.expand_plus_tree_node(self, master_file_name, 'Geography, Customer')
        pyunit_test_object.verify_child_list_in_expanded_tree_node(self, master_file_name, 'Geography, Customer', '02.2')
        pyunit_test_object.expand_plus_tree_node(self, master_file_name, 'Geography, Store')
        pyunit_test_object.verify_child_list_in_expanded_tree_node(self, master_file_name, 'Geography, Store', '02.3')
        '''
        Step 03: Close browser
        '''
if __name__ == '__main__':
    unittest.main()