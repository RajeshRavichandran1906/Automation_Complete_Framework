from common.lib.base import BasePage
from selenium.common.exceptions import NoSuchElementException
from common.lib.utillity import UtillityMethods as utilobject
from common.lib.core_utility import CoreUtillityMethods as coreutilobj
from common.lib.javascript import JavaScript as jsobject
import os, time

DATA_FIELDS_CSS = "div[class*='metadata-tree'] div[class*='tnode-label']"
SELECTED_FIELD_SEE = "div[class*='metadata-tree'] div[class*='tnode-label'][class*='ibx-sm-selected']"

class PyUnit_IA_Tree(BasePage) :
    
    icon_types={'\ue981' : 'ruler', '\ue986' : 'gliph', '\ue98a' : 'funnel', '\ue982' : 'abc', '\ue984' : 'bulb'}
    expand_collapse_image_type={'\ue145' : 'collapsed', '\ue15b' : 'expanded'}
    
    def __init__(self, driver):
        super(PyUnit_IA_Tree, self).__init__(driver)
        
    def select_data_field(self, data_field_path, click_type):
        """
        This method used to click on specific field row
        """
        #PyUnit_IA_Tree.mouse_move_on_metadata_tree(self)
        data_field_path_list=data_field_path.rsplit('->', 1)
        data_field_section_path=None if len(data_field_path_list) == 1 else data_field_path_list[0]
        field_name=data_field_path_list[-1]
        if data_field_section_path != None :
            last_section_index = PyUnit_IA_Tree.expand_data_field_section(self, data_field_section_path)
            last_section_index+=1
        else :
            last_section_index = 0
        filed_index=PyUnit_IA_Tree.find_data_filed_index(self, field_name, last_section_index)
        filed_obj = self.driver.find_elements_by_css_selector(DATA_FIELDS_CSS)[filed_index]
        filed_obj.click()
        utilobject.synchronize_with_number_of_element(self, SELECTED_FIELD_SEE, 1, expire_time=10)
        if click_type != 'left':
            if click_type == 'right':
                coreutilobj.right_click(self, filed_obj)
            if click_type == 'double':
                coreutilobj.double_click(self, filed_obj)
        time.sleep(2)  
              
    def collapse_data_field_section(self, data_field_section_path):
        """
        This method used to collapse the data field. data_field_section_path should be in reverse order. for example if 'Product->Product->Model' already expanded then 
        we should pass data_field_section_path as 'Model->Product->Product' to close section
        """
        PyUnit_IA_Tree.__expand_or_collapse_data_field_section(self, data_field_section_path, 'COLLAPSE')

    def expand_data_field_section(self, master_file_name, field_name, field_index):
        """
        This method used to expand the data field
        """
        masterfile_data = os.getcwd() + "\data\\" + master_file_name.lower() + ".data"
        section = 'EXPANDABLE NODE'
        parser_key = field_name + '_' + str(field_index)
        data_field_section_path=utilobject.read_configparser_key_value(self, masterfile_data, section, parser_key)
        last_section_index = PyUnit_IA_Tree.__expand_or_collapse_data_field_section(self, data_field_section_path, 'EXPAND')
        return last_section_index
    
    def __expand_or_collapse_data_field_section(self, data_field_section_path, action):
        """
        This method used to expand or collapse the data field section.  
        """
        #PyUnit_IA_Tree.mouse_move_on_metadata_tree(self)
        start_index = 0
        if action.upper() == 'EXPAND' :
            icon_css="div[class*='node-btn-collapsed']"
        if action.upper() == 'COLLAPSE' :
            icon_css="div[class*='tnode-btn-expanded']"
        field_section_list=data_field_section_path.split('->')
        for section in field_section_list :
            section_index = PyUnit_IA_Tree.find_data_filed_index(self, section, start_index)
            section_obj = self.driver.find_elements_by_css_selector(DATA_FIELDS_CSS)[section_index]
            icon_obj=section_obj.find_elements_by_css_selector(icon_css)
            if len(icon_obj) > 0 : #check whether field section is already closed or expanded. section is closed or expanded if icon_obj length is 0
                icon_obj[0].click()
            start_index = section_index + 1 if action.upper() == 'EXPAND' else 0
        return section_index
    
    def find_data_filed_index(self, field_name, index):
        """
        """
        data_field_obj_list = self.driver.find_elements_by_css_selector(DATA_FIELDS_CSS)
        for index_count in range(index, len(data_field_obj_list)) :
            if data_field_obj_list[index_count].text == field_name  :
                found_filed_index = index_count
                break
            else :
                found_filed_index = None
        if found_filed_index == None:
            msg="[{0}] data field not found in data tree".format(field_name)
            raise NoSuchElementException(msg)
        else :
            return found_filed_index
    
    def get_child_row_elements(self, node_name):
        all_expanded_section=self.driver.find_elements_by_css_selector(".tnode-expanded")
        required_expanded_section_index=[el.text.strip() for el in self.driver.find_elements_by_css_selector(".tnode-expanded > .tnode-label")].index(node_name)
        required_children_element=all_expanded_section[required_expanded_section_index].find_elements_by_css_selector(".tnode-children")[0]
        required_children_element_dynamic_id=required_children_element.get_attribute('id')
        child_row_elements=self.driver.find_elements_by_css_selector("#"+required_children_element_dynamic_id + " > div")
        return child_row_elements
    
    def get_child_items(self, node_name):
        child_elements=PyUnit_IA_Tree.get_child_row_elements(self, node_name)
        child_list=[el.find_elements_by_css_selector(".tnode-label")[0].text.strip() for el in child_elements]
        return child_list
    
    def verify_all_visible_nodes(self, expected_node_items_list, step_no):
        actual_node_items_list=[el.text.strip() for el in self.driver.find_elements_by_css_selector(".tnode-label") if len(el.text.strip())>0]
        verify_msg='Step ' +step_no + ' : Verify the all visible nodes.'
        utilobject.asequal(self, expected_node_items_list, actual_node_items_list, verify_msg)
        
    def verify_treenode_items_list(self, node_name, expected_node_items_list, step_no):
        actual_node_items_list=PyUnit_IA_Tree.get_child_items(self, node_name)
        verify_msg='Step ' +step_no + ' : Verify the requested child items are available under ' + node_name
        utilobject.asequal(self, expected_node_items_list, actual_node_items_list, verify_msg) 

    def verify_number_of_treenode_items(self, node_name, expected_number_of_node_items, step_no):
        actual_number_of_node_items=len(PyUnit_IA_Tree.get_child_items(self, node_name))
        verify_msg='Step ' +step_no + ' : Verify the requested number of child items are available under ' + node_name
        utilobject.asequal(self, expected_number_of_node_items, actual_number_of_node_items, verify_msg)
    
    def get_expected_child_list(self, master_file_name, field_name, field_index):
        masterfile_data = os.getcwd() + "\data\\" + master_file_name.lower() + ".data"
        section = 'CHILD ELEMENTS'
        parser_key = field_name + '_' + str(field_index)
        data_field_list=eval(utilobject.read_configparser_key_value(self, masterfile_data, section, parser_key))
        return data_field_list 
    
    def get_expected_child_and_image_dict(self, master_file_name, field_name, field_index):
        masterfile_data = os.getcwd() + "\data\\" + master_file_name.lower() + ".data"
        section = 'CHILD ELEMENTS WITH SYMBOL'
        parser_key = field_name + '_' + str(field_index)
        child_and_image_dict=eval(utilobject.read_configparser_key_value(self, masterfile_data, section, parser_key))
        return child_and_image_dict 
        
    def verify_treenode_icon_type(self, parent_node_name, node_name, expected_verify_icon_type, step_no):
        child_elements=PyUnit_IA_Tree.get_child_row_elements(self, parent_node_name)
        verify_msg='Step ' +step_no + ' : Verify the requested ' + expected_verify_icon_type + ' image is available for ' + node_name + ' row.'
        for elem in child_elements:
            if elem.find_elements_by_css_selector(".tnode-label")[0].text.strip() == node_name:
                image_element=elem.find_element_by_css_selector(".ibx-label-icon")
                actual_verify_icon_type=jsobject.get_element_before_style_properties(self, image_element, 'content').replace('"', '')
                icon_name=PyUnit_IA_Tree.icon_types[actual_verify_icon_type]
                utilobject.asequal(self, expected_verify_icon_type, icon_name, verify_msg)
                break
    
    def get_root_level_elements(self):
        root_level_child_component_css="[data-ibx-type='mdTree'] > [data-ibx-type='ibxTreeNode']"
        self.driver.find_elements_by_css_selector(root_level_child_component_css)
        root_node_parent_element_list=self.driver.find_elements_by_css_selector(root_level_child_component_css)
        root_node_element_list=[el.find_elements_by_css_selector(".tnode-label")[0] for el in root_node_parent_element_list]
        return root_node_element_list
    
    def verify_root_icon_type(self, node_name, expected_verify_icon_type, step_no):
        root_node_element_list = PyUnit_IA_Tree.get_root_level_elements(self)
        verify_msg='Step ' +step_no + ' : Verify the requested ' + expected_verify_icon_type + ' image is available for ' + node_name + ' row.'
        for root_node_element in root_node_element_list:
            if root_node_element.text.strip() == node_name:
                image_element=root_node_element.find_element_by_css_selector(".ibx-label-icon")
                actual_verify_icon_type=jsobject.get_element_before_style_properties(self, image_element, 'content').replace('"', '')
                icon_name=PyUnit_IA_Tree.icon_types[actual_verify_icon_type]
                utilobject.asequal(self, 'gliph', icon_name, verify_msg)

    def get_any_row_element(self, row_text, row_index=0):
        row_elements=self.driver.find_elements_by_css_selector("[data-ibx-type='mdTree'] .tnode-label")
        for row_element in row_elements:
            if row_element.text.strip() == row_text:
                return row_element
    
    def veryfy_if_a_row_is_expanded_or_collapsed(self, row_text, step_no, row_index=0, expand = True):
        current_row=PyUnit_IA_Tree.get_any_row_element(self, row_text, row_index=row_index)
        image_element=current_row.find_element_by_css_selector(".tnode-btn")
        actual_expand_colapse_image_type=jsobject.get_element_before_style_properties(self, image_element, 'content').replace('"', '')
        expand_or_collapse_name=PyUnit_IA_Tree.expand_collapse_image_type[actual_expand_colapse_image_type]
        if expand == True:
            verify_msg='Step ' +step_no + ' : Verify the requested [' + row_text + '] node is expanded.'
            utilobject.asequal(self, 'expanded', expand_or_collapse_name, verify_msg)
        else:
            verify_msg='Step ' +step_no + ' : Verify the requested [' + row_text + '] node is collapsed.'
            utilobject.asequal(self, 'collapsed', expand_or_collapse_name, verify_msg)
        