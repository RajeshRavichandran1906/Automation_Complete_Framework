from common.lib.basetestcase import BaseTestCase
from common.wftools.pyunit_iatree import Pyunit_IAtree as pyunit_test_object
import unittest

class C6522007_TestClass(BaseTestCase):
        
    def test_C6522007(self):
        
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
        
        '''
        Step 2. Double click on "Filters and Variables" node
        Verify:
        - Node expanded and
        - it's child nodes are visible
        '''
        pyunit_test_object.click_tree_node_item(self, 'Filters and Variables', click_type = 'double')
        pyunit_test_object.veryfy_if_a_row_is_expanded(self, 'Filters and Variables', '02.01')
        pyunit_test_object.verify_child_list_in_expanded_tree_node(self, master_file_name, 'Filters and Variables', '02.02')
        '''
        Step3. Double click on "Filters and Variables" node
        Verify:
        Node is collapsed
        '''
        pyunit_test_object.click_tree_node_item(self, 'Filters and Variables', click_type = 'double')
        pyunit_test_object.veryfy_if_a_row_is_collapsed(self, 'Filters and Variables', '03.01')
        '''
        Step 4.Double click on "Measure Groups" node
        Verify:
        - Node expanded and
        - it's child nodes are visible
        '''
        pyunit_test_object.click_tree_node_item(self, 'Measure Groups', click_type = 'double')
        pyunit_test_object.veryfy_if_a_row_is_expanded(self, 'Measure Groups', '04.01')
        pyunit_test_object.verify_child_list_in_expanded_tree_node(self, master_file_name, 'Measure Groups', '04.02')
        '''
        Step 5. Double click on "Measure Groups" node
        Verify:
        Node is collapsed
        '''
        pyunit_test_object.click_tree_node_item(self, 'Measure Groups', click_type = 'double')
        pyunit_test_object.veryfy_if_a_row_is_collapsed(self, 'Measure Groups', '05.01')
        '''
        Step 6. Double click on "Dimension" node
        Verify:
        - Node expanded and
        - it's child nodes are visible
        '''
        pyunit_test_object.click_tree_node_item(self, 'Dimensions', click_type = 'double')
        pyunit_test_object.veryfy_if_a_row_is_expanded(self, 'Dimensions', '06.01')
        pyunit_test_object.verify_child_list_in_expanded_tree_node(self, master_file_name, 'Dimensions', '06.02')
        '''
        Step 7. Double click on "Dimension" node
        Verify:
        Node is collapsed
        '''
        pyunit_test_object.click_tree_node_item(self, 'Dimensions', click_type = 'double')
        pyunit_test_object.veryfy_if_a_row_is_collapsed(self, 'Dimensions', '07.01')
        '''
        Step 8. 
        Close browser
        '''
if __name__ == '__main__':
    unittest.main()

