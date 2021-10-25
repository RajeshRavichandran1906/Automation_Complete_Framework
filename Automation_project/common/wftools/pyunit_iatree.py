from common.lib.base import BasePage
from common.pages.pyunit_ia_tree import PyUnit_IA_Tree
from common.lib.utillity import UtillityMethods as utillobject

class Pyunit_IAtree(BasePage):
    
    def __init__(self, driver):
        super(Pyunit_IAtree).__init__(driver)
    
    """****************************************** This is for Common Section. ************************************"""
    
    def wait_for_number_of_element(self, element_css, expected_number, time_out=60):
        utillobject.synchronize_with_number_of_element(self, element_css, expected_number, time_out)
        
    def wait_for_visible_text(self, element_css, visble_text, time_out=60):
        utillobject.synchronize_with_visble_text(self, element_css, visble_text, time_out)
    
    def invoke_metadata_tree_container_page(self, master_file):
        '''
        master_file: This is a json file. This argument needs only the file name, not the extension.
        '''
        node = utillobject.parseinitfile(self, 'nodeid1')
        port = utillobject.parseinitfile(self, 'httpport1')
        context = utillobject.parseinitfile(self, 'wfcontext1')
        setup_url = 'http://' + node + ':' + port + context + '/'
        jsp_file_directory_name = utillobject.parseinitfile(self, 'jsp_file_directory')
        jsp_file_name = utillobject.parseinitfile(self, 'jsp_file_name')
        required_url=setup_url + jsp_file_directory_name + '/' + jsp_file_name + '.jsp?IBIMR_folder=' + master_file + '.json'
        self.driver.get(required_url)
                    
    def expand_plus_tree_node(self, master_file_name, node_name, node_index=0):
        PyUnit_IA_Tree.expand_data_field_section(self, master_file_name, node_name, node_index)
    
    def colapse_plus_tree_node(self, tree_node_path):
        PyUnit_IA_Tree.collapse_data_field_section(self, tree_node_path)
    
    def click_tree_node_item(self, data_field_treepath, click_type = 'left'):
        PyUnit_IA_Tree.select_data_field(self, data_field_treepath, click_type)
    
    def verify_child_list_in_expanded_tree_node(self, master_file_name, node_name, step_no, node_index=0):
        expected_node_items_list = PyUnit_IA_Tree.get_expected_child_list(self, master_file_name, node_name, node_index)
        PyUnit_IA_Tree.verify_treenode_items_list(self, node_name, expected_node_items_list, step_no)
        
    def verify_number_of_child_elements_in_expanded_tree_node(self, node_name, expected_number_of_node_items, step_no):
        PyUnit_IA_Tree.verify_number_of_treenode_items(self, node_name, expected_number_of_node_items, step_no)
    
    def verify_all_visible_nodes(self, expected_node_items_list, step_no):
        PyUnit_IA_Tree.verify_all_visible_nodes(self, expected_node_items_list, step_no)
    
    def verify_treenode_icon_type(self, parent_node_name, node_name, expected_verify_icon_type, step_no):
        PyUnit_IA_Tree.verify_treenode_icon_type(self, parent_node_name, node_name, expected_verify_icon_type, step_no)
        
    def get_expected_child_list(self, master_file_name, node_name, node_index=0):
        expected_node_items_list = PyUnit_IA_Tree.get_expected_child_list(self, master_file_name, node_name, node_index)
        return expected_node_items_list
    
    def get_expected_child_and_image_dict(self, master_file_name, node_name, node_index=0):
        expected_node_child_and_image_dict = PyUnit_IA_Tree.get_expected_child_and_image_dict(self, master_file_name, node_name, node_index)
        return expected_node_child_and_image_dict
    
    def verify_root_icon_type(self, node_name, expected_verify_icon_type, step_no):
        PyUnit_IA_Tree.verify_root_icon_type(self, node_name, expected_verify_icon_type, step_no)
        
    def veryfy_if_a_row_is_expanded(self, row_text, step_no, row_index=0):
        PyUnit_IA_Tree.veryfy_if_a_row_is_expanded_or_collapsed(self, row_text, step_no, row_index=0, expand = True)
        
    def veryfy_if_a_row_is_collapsed(self, row_text, step_no, row_index=0):
        PyUnit_IA_Tree.veryfy_if_a_row_is_expanded_or_collapsed(self, row_text, step_no, row_index=0, expand = False)