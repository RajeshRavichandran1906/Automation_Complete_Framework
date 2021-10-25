from common.pages.basepage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from common.lib.global_variables import Global_variables
from common.locators.designer.components import data as locator
from selenium.webdriver.support import expected_conditions as EC


class Data(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = locator.Data
        self._name = "Data"
    
    @property
    def Source(self): return _Source()
    
    @property
    def Canvas(self): return _Canvas()
    
    @property
    def SampleData(self): return _SampleData()
    
    @property
    def DataToolbar(self): return _DataToolbar()
    
    def switch_to_frame(self, timeout=90):
        """
        Description: Switch inside Data Tab Frame
        """
        frame = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.FRAME, "Data Frame")
        frame_location = self._core_utils.get_web_element_coordinate(frame, element_location='top_left')
        WebDriverWait(self._driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(frame))
        Global_variables.current_working_area_browser_x=frame_location['x']
        Global_variables.current_working_area_browser_y=frame_location['y']
        
        
class _Source(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = locator.Data.Source
        self._name = "Data Source"
        
    def drag_to_original_data(self, data_source, original_data, item_loc="middle", sx=0, sy=0, target_obj_loc="middle", tx=0, ty=0):
        """
        Description: drag source item to original data in canvas to create a join
        """
        item_object = self._get_content_tree_row_object(data_source)
        self._core_utils.python_left_click(item_object)
        source_loc = self._core_utils.get_web_element_coordinate(item_object, item_loc, sx, sy)
        original_data_obj = _Canvas()._get_original_data_object(original_data)
        target_loc = self._core_utils.get_web_element_coordinate(original_data_obj, target_obj_loc, tx, ty)
        self._core_utils.drag_and_drop_without_using_click(source_loc['x'], source_loc['y'], target_loc['x'], target_loc['y'])
        _Canvas()._wait_for_text(original_data)
        
    def _get_content_tree_row_object(self, data_source):
        """
        Description : This method will return content view tree items element object as list
        """
        content_tree_items_object = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.row_css, 'Data content view items')
        required_obj = self._javascript.find_elements_by_text(content_tree_items_object, data_source)
        self._javascript.scrollIntoView(required_obj[0])
        return required_obj[0]
    
    
class _Canvas(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = locator.Data.Canvas
        self._name = "Canvas"
        
    def verify_join_created(self, expected_join, step_num):
        """
        Description: Verifying created in join labels in canvas
        :Usage - verify_join_created(['Join 1', 'empdata (T01)', 'training (T02)'])
        """
        join_title_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.join_label_css, self._name + ' Join Label')
        self._webelement.verify_elements_text(join_title_objects, expected_join, step_num, self._name + ' Join Label')
        
    def _get_original_data_object(self, data_name):
        """
        Description: returns original data field object in canvas
        """
        original_data_object_css = self._locators.original_data_css.format(data_name)
        original_data_objects = self._utils.validate_and_get_webdriver_objects(original_data_object_css, 'Original Data')
        required_object = self._javascript.find_elements_by_text(original_data_objects, data_name)
        return required_object[0]
    
    def _wait_for_text(self, text, timeout=60):
        """
        Description: wait for text in the data canvas
        """
        self._webelement.wait_for_element_text(self._locators.canvas_css, text, timeout)
    
class _SampleData(BasePage):
    
    def __init__(self):
        super().__init__()
    
    
class _DataToolbar():
        
    def __init(self):
        super().__init()
    
    
    