import time
from uisoup import uisoup
from common.pages.basepage import BasePage
from selenium.webdriver.support import color
from common.lib.webfocus.ibx_custom_controls import CommonUtils, ibxSelectItemList, ibxDualListBox
from common.locators.designer.page_canvas import FilterGrid as Locators

class FilterGrid(BasePage):
    
    def __init__(self, parent_object):
        
        super().__init__()
        self._parent_object = parent_object
        self._locator = Locators
    
    def Control(self, label, index=1): return Control(self._parent_object, label, index)
    
    @property
    def Dropdown(self): return ibxSelectItemList()
    
    def verify_number_of_cells(self):
        pass
    
    def verify_cell_border_color(self, cell_index):
        pass
    
    def verify_control_labels(self, expected_labels, step_num, assert_type='equal'):
        """
        Description: Verify all control labels
        """
        self._webelement.verify_elements_text(self._locator.control_labels, expected_labels, step_num,
            "Page Filter Controls Label", assert_type=assert_type, parent_instance=self._parent_object)
    
    def wait_for_text(self, text, time_out=30, pause_time=0):
        """
        Description: Wait until given text present in Filter Grid
        """
        self._webelement.wait_for_element_text(self._locator.filter_grid, text, time_out, pause_time, parent_obj=self._parent_object)
        
    def verify_displayed(self, step_num):
        """
        Description: This will verify filter grid is displayed
        Usage: verify_displayed('02')
        """
        filter_grid_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.filter_grid, 'Filter Grid', self._parent_object)
        actual = filter_grid_obj.is_displayed()
        msg = 'Step {0}: Filter Grid is displayed'.format(step_num)
        self._utils.asequal(True, actual, msg)
    
    def verify_not_displayed(self, step_num):
        """
        Description: This will verify filter grid is not displayed
        Usage: verify_not_displayed('02')
        """
        filter_grid_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.filter_grid, 'Filter Grid', self._parent_object)
        actual = filter_grid_obj.is_displayed()
        msg = 'Step {0}: Filter Grid is not displayed'.format(step_num)
        self._utils.asequal(False, actual, msg)
        
    def right_click_on_cell(self, cell_index):
        """
        Description: Right click on filter grid cell based on index
        Usage: right_click_on_cell(1)
        """
        cell_object = self._get_cell_object(cell_index)
        self._core_utils.right_click(cell_object)
        
    def _get_cell_object(self, cell_index):
        """
        Description: returns filter grid cell object based on cell index
        Usage: _get_cell_object(1)
        """
        filter_cells_object = self._utils.validate_and_get_webdriver_objects_using_locator(self._locator.grid_cells, 'Filter Grid Cells', self._parent_object)
        if cell_index > len(filter_cells_object):
            msg = 'Filter Cell not available for given cell index [{0}]'.format(cell_index)
            raise IndexError(msg)
        else:
            return filter_cells_object[cell_index - 1]
    
    def verify_grid_style_color(self, color_name, step_num):
        """
        Description: This function will verify grid style color is applied 
        Usage: verify_grid_style_color('Style 2', '10')
        """
        grid_object  = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.filter_grid, 'Filter Grid', self._parent_object)
        actual_color = color.Color.from_string(self._utils.get_element_css_propery(grid_object, "background-color")).rgb
        expected_color = self._utils.color_picker(color_name)
        msg = "Step {0} : Verify [{1}] color is applied for filter grid".format(step_num, color_name)
        self._utils.asequal(expected_color, actual_color, msg)
        
class Control(BasePage):
    
    def __init__(self, parent_object, label, index=1):
        
        super().__init__()
        self._parent_object = parent_object
        self._label = label
        self._index = index
        self._locator = Locators
    
    @property
    def Dropdown(self): return ibxSelectItemList()
        
    @property
    def Slider(self): return Slider(self._object)
    
    @property
    def Toggle(self): return _Toggle(self._object)
    
    @property
    def DoubleList(self): return _DoubleList(self._object)
    
    def verify_border_properties(self, step_num, expected={'with': '1px', 'style': 'solid', 'color': 'rgb(1, 149, 228)', 'position': 'absolute'}):
        """
        Description: 
        """
        msg = "Step {} : Verify {} control border properties".format(step_num, self._label)
        CommonUtils().verify_pd_component_border_property(self._object, expected, msg)
    
    def click(self, location='top_middle', x=0, y=2):
        """
        Description: Click on top middle of control to select
        """
        self._core_utils.python_left_click(self._object, location, x, y)
        
    def wait_for_text(self, text, time_out):

        self._webelement.wait_for_element_text(self._locator.control_box, text, time_out, parent_obj=self._object)
        
    @property
    def _object(self):
        """
        Description: Return the filter control object by label and index
        """
        controls = self._utils.validate_and_get_webdriver_objects_using_locator(self._locator.controls, "Filter controls", self._parent_object)
        control_labels = self._utils.validate_and_get_webdriver_objects_using_locator(self._locator.control_labels, "Filter controls", self._parent_object)
        label_index_list = self._javascript.find_all_index_of_element_by_text(control_labels, self._label)
        if len(label_index_list) >= self._index:
            index = label_index_list[self._index - 1]
            return controls[index]
        else:
            msg = "[{}] control not found in Filter Grid".format(self._label)
            raise LookupError(msg)
        
        
class Slider(BasePage):
    
    def __init__(self, control_object):
        
        super().__init__()
        self._control_object = control_object
        self._locator = Locators.Slider
    
    def verify_values(self, expected, step_num):
        """
        Description: Verify the Slider Min, Max and select values
        :Usage - verify_values(['5', '1', '10'], '03.02')
        """
        slider = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.slider, "Slider Control", self._control_object)
        actual = slider.text.strip().split("\n")
        msg = "Step {} : Verify the Slider values is equal to {}".format(step_num, expected)
        self._utils.asequal(expected, actual, msg)
    
    def move_pin(self, set_value, pin=1):
        """
        Descriptions : This method used to move slider to specific value by drag and drop slider marker. 
        :arg - pin : If you want to select slider value by using slider pin 1 (left side) then pass pin=1 else pin=2 (right side)
        example usage : move_pin(4)
        example usage : move_pin(4, pin=2)
        """
        marker_locator = self._locator.marker1 if pin==1 else self._locator.marker2
        min_value_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.min_value, "Slider Min Value", self._control_object)
        max_value_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.max_value, "Slider Max Value", self._control_object)
        min_value = int(min_value_obj.text.strip())
        max_value = int(max_value_obj.text.strip())
        if set_value in range(min_value, max_value+1) :
            slider_line = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.line, "Slider Line", self._control_object)
            slider_line_width = slider_line.size['width']
            slider_line_x = self._core_utils.get_web_element_coordinate(slider_line, element_location='middle_left')['x']
            slider_range = max_value - min_value
            slider_value_distance = slider_line_width / slider_range
            slider_value_range = set_value - min_value
            slider_value_xoffset = slider_value_distance * slider_value_range
            marker = self._utils.validate_and_get_webdriver_object_using_locator(marker_locator, "Slider Marker", self._control_object)
            marker_location = self._core_utils.get_web_element_coordinate(marker)
            source_x = marker_location['x']
            source_y = marker_location['y']
            target_x = slider_line_x + slider_value_xoffset
            target_y = source_y
            uisoup.mouse.move(source_x,source_y)
            time.sleep(1)
            uisoup.mouse.drag(source_x,source_y, target_x, target_y)
        else :
            error_msg = "Set value {} not in range({}, {})".format(set_value, min_value, max_value)
            raise ValueError(error_msg)
        

class _Toggle(BasePage):
    
    def __init__(self, control_object):
        
        super().__init__()
        self._control_object = control_object
        self._locator = Locators.Toggle
        self._name = "Toggle"
        
    def verify_converted(self, step_num):
        """
        Description: This function will verify control is converted to Toggle 
        :Usage - verify_converted("01")
        """
        toggle_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.toggle, self._name, parent_object=self._control_object)
        self._utils.verify_element_visiblty(toggle_obj, msg="Step {0}: Verify converted to Toggle".format(step_num))
        
    def check(self):
        """
        Description: This function will check the toggle button
        :Usage - check()
        """
        toggle_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.toggle_unchecked, self._name + " Button", parent_object=self._control_object)
        self._core_utils.python_left_click(toggle_button)
        
    def verify_lables(self, expected_lables, step_num, assert_type="equal"):
        """
        Description: This function will verify the toggle button labels
        :Usage - verify_lables([])
        """
        self._webelement.verify_elements_text(self._locator.toggle_labels, expected_lables, step_num, self._name + " Lables", assert_type, parent_instance=self._control_object)
        
    def uncheck(self):
        pass
    
    def verify_checked(self):
        pass
        
    def verify_unchecked(self):
        pass
    

class _DoubleList(BasePage):
    
    def __init__(self, control_object):
    
        super().__init__()
        self._control_object = control_object
        self._locator = Locators.DoubleList
        self._name = "Double List"
        
    @property
    def DualListBox(self): return ibxDualListBox('Double List', self._utils.validate_and_get_webdriver_object_using_locator(self._locator.double_list_pop_up, "Double List Pop Up"))
        
    def verify_converted(self, step_num):
        """
        Description: This function will verify control is converted to Double List 
        :Usage - verify_converted("01")
        """
        toggle_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.double_list, self._name, parent_object=self._control_object)
        self._utils.verify_element_visiblty(toggle_obj, msg="Step {0}: Verify converted to Toggle".format(step_num))
    
    def wait_for_text(self, text, time_out):

        self._webelement.wait_for_element_text(self._locator.double_list_pop_up, text, time_out)
    
    