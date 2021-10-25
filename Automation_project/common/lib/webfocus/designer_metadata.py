from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.lib.javascript import JavaScript
import time

FILED_PARENT_CSS = {'DIMENSIONS' : "div.wfc-mdfp-dimension-tree", 'MEASURE' : "div.wfc-mdfp-measure-tree ", 'VARIABLES'  : "div.wfc-mdfp-variables-tree"}
GROUP_FIELD_CSS = "div.tnode-is-container"
GROUP_EXPAND_CSS = "div.tnode-btn-collapsed"
GROUP_FIELD_LABEL_CSS = GROUP_FIELD_CSS + ">div:nth-child(1)"
GROUP_CHILD_FIELD_CSS = "div.tnode-label"        

class DesignerMetadata(object):
    
    def __init__(self, driver):
        
        self.driver = driver
        self._util = UtillityMethods(self.driver)
        self._coreutil = CoreUtillityMethods(self.driver)
        self._javascript = JavaScript(self.driver)
    
    def get_dimension_field_element(self, field_path):
        
        split_field_path = field_path.rsplit('->', 1)
        expand_group_path = split_field_path[0]
        field_name = split_field_path[-1]
        group_object = self.expand_group_field_and_get_group_object('DIMENSIONS', expand_group_path)
        field_object = self.get_child_field_object_from_group_field('DIMENSIONS', group_object, field_name)
        return field_object
    
    def get_measures_field_element(self, field_path):
        pass
    
    def get_variables_field_element(self, field_path):
        pass
    
    
    def expand_group_field_and_get_group_object(self, field_type, expand_group_path):
        """
        Description : This method will return only group fields text as list. 
        @arg = parent_object : if pass parent object , then parent field will search only inside the parent object
        """
        parent_css = FILED_PARENT_CSS[field_type.upper()]
        group_path_list = expand_group_path.split('->')
        parent_object = self._util.validate_and_get_webdriver_object(parent_css, field_type)
        self._coreutil.python_move_to_element(parent_object)
        for group_name in group_path_list :
            group_label_object_list = self._util.validate_and_get_webdriver_objects(GROUP_FIELD_LABEL_CSS, 'Field groups labels', parent_object)
            group_index = self._javascript.find_element_index_by_text(group_label_object_list, group_name)
            if group_index != None :
                group_lable_object = group_label_object_list[group_index]
                exapanded_icon_object = group_lable_object.find_elements_by_css_selector(GROUP_EXPAND_CSS)
                if len(exapanded_icon_object) > 0 :
                    self.scroll_field_into_view(field_type, group_lable_object)
                    self._coreutil.python_left_click(exapanded_icon_object[0]) 
                group_field_objects = self._util.validate_and_get_webdriver_objects(GROUP_FIELD_CSS, 'Field groups', parent_object)
                parent_object = group_field_objects[group_index]
            else :
                error_msg = 'Unable to find {0} group field in meata data'.format(group_name)
                raise KeyError(error_msg)
        return parent_object
     
    def get_child_field_object_from_group_field(self, field_type, group_field_object, child_field_name):
        """
        Description : This method will return only group fields text as list. 
        @arg = parent_object : if pass parent object , then parent field will search only inside the parent object
        """
        child_field_objects = self._util.validate_and_get_webdriver_objects(GROUP_CHILD_FIELD_CSS, 'Group fields', group_field_object)
        child_field_index = self._javascript.find_element_index_by_text(child_field_objects, child_field_name)
        if child_field_index != None :
            child_field_object = child_field_objects[child_field_index]
            self.scroll_field_into_view(field_type, child_field_object)
            return child_field_object
        else :
            error_msg = 'Unable to find {0} field in meata data'.format(child_field_name)
            raise KeyError(error_msg)
        
    def scroll_field_into_view(self, field_type, field_object):
        """
        """
        field_container_css = FILED_PARENT_CSS[field_type.upper()]
        field_container_obj = self._util.validate_and_get_webdriver_object(field_container_css, field_type)
        field_container_bottom_y = int(self._coreutil.get_web_element_coordinate(field_container_obj, 'bottom_middle')['y'])
        field_container_top_y = int(self._coreutil.get_web_element_coordinate(field_container_obj, 'top_middle')['y'])
        max_scroll = len(field_container_obj.find_elements_by_css_selector(GROUP_CHILD_FIELD_CSS))
        scroll_count = 0
        while True :
            field_bottom_y = int(self._coreutil.get_web_element_coordinate(field_object, 'bottom_middle')['y'])
            field_top_y = int(self._coreutil.get_web_element_coordinate(field_object, 'top_middle')['y'])
            if field_container_bottom_y < field_bottom_y and scroll_count < max_scroll:
                UtillityMethods.mouse_scroll(self, 'down', '1', option='uiautomation')
                scroll_count+=1
            elif field_top_y < field_container_top_y and scroll_count < max_scroll:
                UtillityMethods.mouse_scroll(self, 'up', '1', option='uiautomation')
                scroll_count+=1
            else : 
                break
        time.sleep(1)