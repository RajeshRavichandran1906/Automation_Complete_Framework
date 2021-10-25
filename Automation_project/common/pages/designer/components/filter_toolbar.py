from common.pages.basepage import BasePage
from common.lib.webfocus import ibx_custom_controls
from common.locators import ibx_custom_controls as ibx_locators
from common.locators.designer.components.filter_toolbar import FilterToolbar as locators

class FilterToolbar(BasePage):
    
    def __init__(self, parent=locators.visual_filter_toolbar, name='Visualization Filter Toolbar'):
        super().__init__()
        self._parent = self._webelement._get_object(parent, name)
        self._name = name
        self._locators = locators
        
    @property
    def Dropdown(self): return _Dropdown()
    
    def _field_name_objects(self):
        """
        Description: Will return field name object in filter toolbar
        """
        return self._webelement._get_objects(self._locators.field_name, parent_instance=self._parent)
    
    def _field_value_objects(self):
        """
        Description: Will return field value object in filter toolbar
        """
        return self._webelement._get_objects(self._locators.field_value, parent_instance=self._parent)
    
    def verify_field_names(self, expected_names, step_num, assert_type='equal'):
        """
        Description: Will verify field names in the filter toolbar
        :Usage - verify_field_names([], '01')
        """
        self._webelement.verify_elements_text(self._locators.field_name, expected_names, step_num, self._name + ' Field names', assert_type, parent_instance=self._parent)
        
    def verify_field_values(self, expected_values, step_num, assert_type='equal'):  
        """
        Description: Will verify field values in the filter toolbar
        :Usage - verify_field_values([], '01')
        """  
        self._webelement.verify_elements_text(self._locators.field_value, expected_values, step_num, self._name + ' Field names', assert_type, parent_instance=self._parent)
        
    def click_on_field(self, field_name):
        """
        Description: click on the filter based on field name
        :Usage - click_on_filter('COUNTRY')
        """
        filter_field_objects = self._field_name_objects()
        required_filter_obj = self._javascript.find_elements_by_text(filter_field_objects, field_name)
        if required_filter_obj:
            self._core_utils.python_left_click(required_filter_obj[0])
        else:
            msg = 'Filter Cell not available for the given field name [{0}]'.format(field_name)
            raise KeyError(msg)
        
class _Dropdown():
    
    @property
    def Option(self): return ibx_custom_controls.ibxSelectItemList(item_list_options_locator=ibx_locators.ibxSelectItemList.multiselect_options)
        
    
        