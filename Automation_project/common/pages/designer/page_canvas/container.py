import keyboard
from common.pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import color
from selenium.webdriver.support.ui import WebDriverWait
from common.lib.webfocus.ibx_custom_controls import Icon
from common.lib.global_variables import Global_variables
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from common.locators.designer.page_canvas import Container as Locator
from common.pages.designer.page_canvas.filter_grid import FilterGrid
# from common.wftools.designer import Designer

class Containers(BasePage):
    
    def __init__(self, parent_object):
        
        super().__init__()
        self._parent_object = parent_object
        
    def Basic(self, title=None, index=1): return Basic(self._parent_object, title, index)
    
    def Explorer(self, title=None, index=1): return Basic(self._parent_object, title, index)
    
    def Tab(self, title=None, index=1): return Tab(self._parent_object, title, index)
    
    def Carousel(self, title=None, index=1): return Carousel(self._parent_object, title, index)
    
    def Accordion(self, title=None, index=1): return Accordion(self._parent_object, title, index)
    
    def LinkTile(self, title=None, index=1): return Basic(self._parent_object, title, index)
    
    def Grid(self, title=None, index=1): return Grid(self._parent_object, title, index)
    
    def PanelGroup(self, title=None, index=1): return PanelGroup(self._parent_object, title, index)
    
    def Workspace(self, title=None, index=1): return Workspace(self._parent_object, title, index)
        
    def verify_containers_title(self, expected_titles, step_num, assert_type= 'equal'):
        """
        Description: Verify all containers title
        """
        self._webelement.verify_elements_text(Locator.title, expected_titles, step_num, 'Containers Title', assert_type, parent_instance = self._parent_object)
        
    def verify_number_of_containers(self, expected_total, step_num):
        """
        Description: Verify number of containers
        """
        actual_total = len(self._driver.find_elements(*Locator.containers))
        msg = "Step {} : Verify number of containers is equal to {}".format(step_num, expected_total)
        self._utils.asequal(expected_total, actual_total, msg)
    
    def multi_select_containers(self, container_list):
        """
        Description: This function will multiselect the container
        Usage: multi_select_containers(['Category Sales', 'Discount by Region'])
        """
        available_containers = self._driver.find_elements(*Locator.title)
        required_containers = [containers for containers in available_containers if containers.text.strip() in container_list]
        keyboard.press('ctrl')
        if required_containers != []:
            for element in required_containers:
                self._javascript.scrollIntoView(element)
                self._core_utils.python_left_click(element, element_location = 'top_middle', xoffset=5, yoffset=5)
        else:
            msg = "{} containers not found in canvas".format(container_list)
            raise LookupError(msg)
        keyboard.release('ctrl')
        
    def _get_container_object(self, title=None, index=1):
        
        return _Common(self._parent_object, title, index)._get_container_object()
    
class _Common(BasePage):
    
    def __init__(self, parent_object, title=None, index=1):
        
        super().__init__()
        self._parent_object = parent_object
        self._locators = Locator
        self._title = title
        self._index = index
    
    def resize(self, drag_location, xoffset=0, yoffset=0):
        """
        Description: This function will resize the container
        Usage: resize('bottom_right', 100, 100)
        """
        self._core_utils.move_to_element(self._get_container_object())
        if drag_location == 'bottom_right':
            resize_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.resize_se, "Resize Bottom Right", self._parent_object)
        elif drag_location == 'middle_right':
            resize_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.resize_e, "Resize middle Right", self._parent_object)
        elif drag_location == 'bottom_left':
            resize_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.resize_sw, "Resize Bottom Left", self._parent_object)
        elif drag_location == 'middle_left':
            resize_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.resize_w, "Resize middle Left", self._parent_object)
        elif drag_location == 'bottom_middle':
            resize_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.resize_s, "Resize Bottom Middle", self._parent_object)
        self._ActionChains(self._driver).drag_and_drop_by_offset(resize_button, xoffset, yoffset).perform()
    
    def select(self, location='top_middle', x=0, y=5):
        """
        Description: Left click on container
        """
        self._core_utils.python_left_click(self._get_container_object(), location, x, y)
    
    def right_click(self):
        """
        Description: Right click on container
        """
        #self._core_utils.right_click(self._get_container_object(), pause_time=0)
        #ActionChains(self._driver).context_click(self._get_container_object()).perform()
        #self._core_utils.python_right_click(self._get_container_object(), element_location="top_middle", yoffset=15)
        self._core_utils.right_click(self._get_container_object(), element_location="top_middle", yoffset=15)
        self._webelement.wait_until_element_visible((By.CSS_SELECTOR, "div.pop-top"), 20)
        
    def switch_to_default_conent(self):
        """
        Description: Switch to default content from frame
        """
        self._core_utils.switch_to_default_content()
        
    def _get_container_object(self):
        """
        Description: Return the container object by title
        """
        container_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.containers, "Page Canvas Containers", self._parent_object)
        if self._title:
            containers_title = [container.find_element(*self._locators.title) for container in container_objects]
            index_list = self._javascript.find_all_index_of_element_by_text(containers_title, self._title)
            if index_list and len(index_list) >= self._index:
                container_object = container_objects[index_list[self._index-1]]
                self.__scroll_into_view(container_object)
                return container_object
            else:
                msg = "[{}] container not found".format(self._title)
                raise LookupError(msg)
        else:
            return self._get_container_object_by_index(container_objects)
            
    def _get_container_object_by_index(self, container_objects):
        """
        Description: Return the container object by title
        """
        if len(container_objects) >= self._index:
            container_object = container_objects[self._index-1]
            self.__scroll_into_view(container_object)
            return container_object
        else:
            msg = "{} container {} not found".format(self._title)
            raise LookupError(msg)
    
    def _switch_to_frame(self, content_object, timeout=60):
        """
        Description: Switch to content frame
        """
        self.wait_until_loading_complete()
        frame = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.frame, "Container Frame", content_object)
        frame_location = self._core_utils.get_web_element_coordinate(frame, element_location='top_left')
        WebDriverWait(self._driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(frame))
        Global_variables.current_working_area_browser_x=frame_location['x']
        Global_variables.current_working_area_browser_y=frame_location['y']
    
    def wait_until_loading_complete(self, time_out=60, pause_time=0):
        """
        Description: Current process will wait until container loading process is complete.
        """
        self._webelement.wait_until_element_invisible(self._locators.loading, time_out, pause_time, parent_obj=self._get_container_object())
    
    def verify_style_color(self, color_name, step_num):
        """
        Description: This will verify container style is applied
        Usage: verify_style_color('blue', '01')
        """
        container_object  = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.title_bar, 'Container Title Bar', self._get_container_object())
        actual_color = color.Color.from_string(self._utils.get_element_css_propery(container_object, "background-color")).rgb
        expected_color = self._utils.color_picker(color_name)
        msg = "Step {0} : Verify [{1}] color is applied for container".format(step_num, color_name)
        self._utils.asequal(expected_color, actual_color, msg)
        
    def __scroll_into_view(self, container_object):
        """
        Description: Scroll container into view area using java script.
        """
        parent_bottom = self._parent_object.location['y'] + self._parent_object.size['height']
        container_bottom = container_object.location['y'] + container_object.size['height']
        if (container_bottom > parent_bottom) or (self._parent_object.location['y'] > container_object.location['y']):
            self._javascript.scrollIntoView(container_object, wait_time=0.5)
        
class _Toolbar(BasePage):
    
    def __init__(self, container_object):
        
        super().__init__()
        self._container_object = container_object
        
    def verify_title(self, expected_title, step_no):
        """
        Description: Function to verify title of the container
        Usage: verify_title(expected_title, container_object, "05.01")
        """
        msg = "Step {0}: Verify title of the container is equal to {1}.".format(step_no, expected_title)
        toolbar_object = self._utils.validate_and_get_webdriver_object_using_locator(Locator.title, "container title", self._container_object)
        container_title = toolbar_object.text.strip()
        self._utils.asequal(expected_title, container_title, msg)
    
    def right_click(self):
        """
        Description: Right click on tool bar
        """
        toolbar = self._utils.validate_and_get_webdriver_object_using_locator(Locator.title, "Container ToolBar", self._container_object)
        self._ActionChains(self._driver).context_click(toolbar).perform()
        
    @property
    def Options(self): 
        option_object = self._utils.validate_and_get_webdriver_object_using_locator(Locator.options, "Options", self._container_object)
        return Icon(option_object, Locator.options_icon, "\e996", "Options")
    
    @property
    def Maximize(self): 
        option_object = self._utils.validate_and_get_webdriver_object_using_locator(Locator.maximize, "Maximize", self._container_object)
        return Icon(option_object, Locator.maximize_icon, "\ea77", "Maximize")
    
    @property
    def Restore(self): 
        option_object = self._utils.validate_and_get_webdriver_object_using_locator(Locator.restore, "Restore", self._container_object)
        return Icon(option_object, Locator.restore_icon, "\ea78", "Restore")
    
    
class Basic(_Common):
    
    def __init__(self, parent_object, title=None, index=1):
        
        super().__init__(parent_object, title, index)
    
    @property
    def ToolBar(self): return _Toolbar(self._get_container_object())
     
    def switch_to_frame(self):
        """
        Description: Switch to frame
        """
        self._switch_to_frame(self._get_container_object())
        self._utils.wait_for_page_loads(60)

    
class Tab(_Common):
    
    def __init__(self, parent_object, title=None, index=1):
        
        super().__init__(parent_object, title, index)
       
    
    @property
    def ToolBar(self): return _Toolbar(self._get_container_object()) 
          
         
    def _get_tab_object(self, tab, index = 1):
        """
        Description:return tab object in container
        Usage: _get_tab_object('Tab 1')
        """

        tab_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.Tab.tab, "Page Canvas Containers", self._get_container_object())
        if tab:
            tab_title = [tab.find_element(*self._locators.Tab.title) for tab in tab_objects]
            index_list = self._javascript.find_all_index_of_element_by_text(tab_title, tab)
            if index_list and len(index_list) >= index:
                tab_object = tab_objects[index_list[index-1]]
                return tab_object
            else:
                msg = "[{}] container not found".format(tab)
                raise LookupError(msg)          
        
    def click_overflow_icon(self):
        """
        Description: Left click on Variables tab
        """
        tab_overflow_object = self._utils.validate_and_get_webdriver_object_using_locator(Locator.Tab.overflow_icon, "Ellipse or Overflow Icon",  self._get_container_object())
        self._core_utils.left_click(tab_overflow_object)        
           
    def select(self, tab, index=1, location='top_middle', x=0, y=5):
        """
        Description: Left click on container
        Usage: Select('Tab 1')
        """
        self._core_utils.python_left_click(self._get_tab_object(tab, index), location, x, y)
        
    def switch_to_frame(self):
        """
        Description: Switch to frame
        """
        tab_content_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.Tab.tab_content, 'Tab content', self._get_container_object())
        actual_tab_content_object = [tab_content for tab_content in tab_content_objects if tab_content.is_displayed()]
        if actual_tab_content_object != []:
            self._switch_to_frame(actual_tab_content_object[0])
            self._utils.wait_for_page_loads(60)
        else:
            msg = "Tab Content not found"
            raise LookupError(msg)
        
    def add_new_tab(self, no_of_clicks=1):
        """
        Description: Function will add new tab in tab container
        Usage: add_new_tab()
        """
        add_icon = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.Tab.new_button, 'New tab icon', self._get_container_object())
        tab_overflow_icon = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.Tab.overflow_icon, 'Tab overflow icon', self._get_container_object())
        if no_of_clicks >= 1:
            for _ in range(no_of_clicks):
                if add_icon.is_displayed(): 
                    add_icon.click()
                    self._utils.wait_for_page_loads(10)
                elif tab_overflow_icon.is_displayed(): 
                    tab_overflow_icon.click()
                    self._utils.wait_for_page_loads(10)
                    add_icon_in_overflow = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.Tab.new_tab_icon_in_overflow_menu, "New tab")
                    self._core_utils.python_left_click(add_icon_in_overflow)
                    self._utils.wait_for_page_loads(10)
                else:
                    msg = "Add Tab icon not found"
                    raise LookupError(msg)
                
    def verify_overflow_icon(self, step_num):
        """
        Description: Verify overflow icon is displayed
        """
        tab_overflow_object = self._utils.validate_and_get_webdriver_object_using_locator(Locator.Tab.overflow_icon, "Ellipse or Overflow Icon",  self._get_container_object())
        try:
            if tab_overflow_object.is_displayed():
                status = True         
        except NoSuchElementException:
            status = False
        msg = 'Step {0}: verify overflow icon'.format(step_num)
        self._utils.asequal(True, status, msg)
        
    def verify_plus_icon(self, step_num):
        """
        Description: Verify plus icon is displayed
        """
        new_tab_object = self._utils.validate_and_get_webdriver_object_using_locator(Locator.Tab.new_button, "Plus icon or add new tab",  self._get_container_object())
        try:
            if new_tab_object.is_displayed():
                status = True          
        except NoSuchElementException:
            status = False
        msg = 'Step {0}: verify plus icon'.format(step_num)
        self._utils.asequal(True, status, msg)
        
    def verify_tabs_title(self, expected_titles, step_num, assert_type='equal'):
        """
        Description: Verify tab titles in tab container
        """
        self._webelement.verify_elements_text(Locator.Tab.title, expected_titles, step_num, 'Tabs Title', assert_type, parent_instance= self._get_container_object())

class Carousel(_Common):
    
    
    def __init__(self, parent_object, title=None, index=1):
        super().__init__(parent_object, title, index)
    
    @property
    def ToolBar(self): return _Toolbar(self._get_container_object())
     
    def switch_to_frame(self, slider_no=1):
        """
        Description: Switch to frame
        """
        self._switch_to_frame(self._get_slider_object(slider_no))
        self._utils.wait_for_page_loads(60)
        
    def click_on_previous_slide(self, no_of_clicks=1):
        """
        Description: Function will select the previous slide
        Usage: click_on_previous_slide()
        """
        
        previous_slide = self._utils.validate_and_get_webdriver_object_using_locator(Locator.Carousel.previous_slide, "Previous Slide", self._get_container_object())
        if no_of_clicks >= 1:
            for _ in range(no_of_clicks):
                previous_slide.click()
                self._utils.wait_for_page_loads(20)
        else:
            msg = "[{}] invalid no of clicks value".format(no_of_clicks)
            raise ValueError(msg)
            
        
    def click_on_next_slide(self, no_of_clicks=1):
        """
        Description: Function will select the next slide
        Usage: click_on_next_slide()
        """
        next_slide = self._utils.validate_and_get_webdriver_object_using_locator(Locator.Carousel.next_slide, "Next Slide", self._get_container_object())
        if no_of_clicks >= 1:
            for _ in range(no_of_clicks):
                next_slide.click()
                self._utils.wait_for_page_loads(20)
        else:
            msg = "[{}] invalid no of clicks value".format(no_of_clicks)
            raise ValueError(msg)
        
    def click_on_slide_pin(self, slide_no=1):
        """
        Description: Function will click on the go to slide pin in the carousel container
        Usage: click_on_go_to_slide_pin(1)
        """
        slider_pins = self._utils.validate_and_get_webdriver_objects_using_locator(Locator.Carousel.go_to_slide_pin, "Go to slide", self._get_container_object())
        if len(slider_pins) >= slide_no:
            slider_pins[slide_no-1].click()
            self._utils.wait_for_page_loads(20)
        else:
            msg = "[{}] invalid slide_no value".format(slide_no)
            raise ValueError(msg)
        
        
    def verify_no_of_sliders(self, expected_no_of_sliders, step_num=None):
        """
        Description: Function will verify no of sliders available in the Carousel container.
        Usage: verify_no_of_sliders(3, "07.01")
        """
        self._webelement.wait_until_element_visible(Locator.Carousel.slides, 20, 2, False, self._get_container_object())
        slider_objects = self._utils.validate_and_get_webdriver_objects_using_locator(Locator.Carousel.slides, "Carousel Sliders", self._get_container_object())
        msg = "Step {} : Verify number of slides in carousel container is equal to {}".format(step_num, expected_no_of_sliders)
        self._utils.asequal(len(slider_objects), expected_no_of_sliders, msg)
        
    def _get_slider_object(self, slider_no=1):
        """
        Description: Function will return the slider object
        """
        slider_objects = self._utils.validate_and_get_webdriver_objects_using_locator(Locator.Carousel.slides, "Carousel Sliders", self._get_container_object())
        if len(slider_objects) >= slider_no:
            slider_object = slider_objects[slider_no-1]
            if slider_object.is_displayed():
                return slider_object
            else:
                msg = "Slider {} is not in view".format(slider_no)
            raise LookupError(msg)
        else:
            msg = "Invalid slider_no value [{}]".format(slider_no)
            raise ValueError(msg)
        
class Accordion(_Common):
    
    def __init__(self, parent_object, title=None, index=1):
        super().__init__(parent_object, title, index)
        
    @property
    def ToolBar(self): return _Toolbar(self._get_container_object())
        
    def _get_area_object(self, area, area_index=1):
        """
        Description: Return the area object by title
        Usage: _get_area_object('Blue')
        """
        container = self._get_container_object()
        area_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.Accordion.area, "Area", container)
        if area:
            areas_title = [area.find_element(*self._locators.Accordion.title) for area in area_objects]
            index_list = self._javascript.find_all_index_of_element_by_text(areas_title, area)
            if index_list and len(index_list) >= area_index:
                area_object = area_objects[index_list[area_index-1]]
                return area_object
            else:
                msg = "[{}] area object not found".format(area)
                raise LookupError(msg)
            
    def verify_areas_title(self, expected, step_num, assert_type='equal'):
        """
        Description: This function will verify area title
        Usage: verify_areas_title(['Blue', 'Green'], '10')
        """
        container = self._get_container_object()
        area_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.Accordion.area, "Area", container)
        area_title_objects = [area.find_element(*self._locators.Accordion.title) for area in area_objects]
        actual_area_title = [area_title.text.strip() for area_title in area_title_objects]
        self._utils.list_values_verification(expected, actual_area_title, step_num, 'Area title', assert_type)
    
    def expand_area(self, area, area_index=1):
        """
        Description: Expand area
        Usage: expand_area('Blue')
        """
        area_object  = self._get_area_object(area, area_index)
        actual = area_object.get_attribute('class')
        if 'acc-pg-closed' in actual:
            area_object.click()
        
    def collapse_area(self, area, area_index=1):
        """
        Description: Collapse area
        Usage: collapse_area('Blue')
        """
        area_object = self._get_area_object(area, area_index)
        actual = area_object.get_attribute('class')
        if 'acc-pg-closed' not in actual:
            self._core_utils.python_left_click(area_object, element_location = 'top_middle', yoffset=5)
        
    def switch_to_frame(self, area, area_index=1):
        """
        Description: Switch to Frame 
        """
        self._switch_to_frame(self._get_area_object(area, area_index))
        self._utils.wait_for_page_loads(40)
        
    def add_new_area(self):
        """
        Description: Add new area
        """
        container = self._get_container_object()
        add = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.Accordion.Add, 'Add', container)
        add.click()
    
    def verify_area_content_text(self, area, expected, step_num, area_index=1):
        """
        Description: Area content text 
        Usage: verify_area_content_text('Blue', 'Drop content here', '01')
        """
        area_object = self._get_area_object(area, area_index)
        context_text_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.Accordion.area_content, 'Area Content', area_object)
        actual_context_text = context_text_object.text.strip()
        msg = 'Step {}: verify area context text'.format(step_num)
        self._utils.asequal(expected, actual_context_text, msg)

class Grid(_Common):
    
    def __init__(self, parent_object, title=None, index=1):   
        super().__init__(parent_object, title, index)
        
    @property
    def ToolBar(self): return _Toolbar(self._get_container_object())
        
    @property
    def FilterGrid(self): return FilterGrid(self._get_container_object())

class PanelGroup(_Common):
    
    def __init__(self, parent_object, title=None, index=1):   
        super().__init__(parent_object, title, index)
        
    @property
    def ToolBar(self): return _Toolbar(self._get_container_object())
    
class Workspace(_Common):
    
    def __init__(self, parent_object, title=None, index=1):
        super().__init__(parent_object, title, index)
    
    @property
    def ToolBar(self): return _Toolbar(self._get_container_object())
    
    @property
    def Content(self): return _Content(self._get_container_object())
    
class _Content(BasePage):
    
    def __init__(self, parent_object):
        super().__init__()
        self._parent_object = parent_object
        self._locators = Locator
        self._title = 'Content Tree'
    
    def select(self, item_path):
        """
        Description: Expand the parent folder and select the item
        """
        item_obj = self._get_item_object(item_path)
        #self._core_utils.left_click(item_obj)
        item_obj.click()
    
    def double_click(self, item_path):
        """
        Description: Expand the parent folder and double click the items
        """
        item_obj = self._get_item_object(item_path)
        self._core_utils.double_click(item_obj)
        
    def right_click(self, item_path):
        """
        Description: Expand the parent folder and right click the items
        """
        item_obj = self._get_item_object(item_path)
        self._ActionChains(self._driver).context_click(item_obj).perform()
        self._webelement.wait_until_element_visible((By.CSS_SELECTOR, "div.pop-top"), 20)
        
    def wait_for_text(self, text, time_out, pause_time=0, case_sensitive=False, raise_error=True, javascript=False):
        
        self._webelement.wait_for_element_text(self._locators.Workspace.content_resource, text, time_out, pause_time, case_sensitive, raise_error, javascript)
    
    def _get_item_object(self, item_path):
        """
        Description: Expand the folders and return item object
        """
        items_list = item_path.split("->")
        for index, item in enumerate(items_list, 1):
            self.wait_for_text(item, 30, raise_error=False, javascript=True)
            items_obj = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.Workspace.content_items, 'Workspace Content Items', self._parent_object)
            item_index = self._javascript.find_element_index_by_text(items_obj, item)
            if item_index != None:
                if index == len(items_list):
                    return items_obj[item_index]
                else:
                    #self._core_utils.left_click(items_obj[item_index], pause_time=0)
                    items_obj[item_index].click()
                    self._utils.wait_for_page_loads(10, pause_time=0)
            else:
                raise FileNotFoundError("[{0}] not found in designer content tree".format(item))
    
    
