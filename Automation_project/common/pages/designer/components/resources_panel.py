import time
from uisoup import uisoup
from common.pages.basepage import BasePage
from common.lib.html_controls import TextBox
from common.lib.webfocus import ibx_custom_controls
from common.pages.designer.page_canvas import PageCanvas
from common.locators.designer.components.filter_toolbar import FilterToolbar as filter_locators
from common.lib.webfocus.ibx_custom_controls import bucket 
from common.locators.designer.components.visualization_canvas import VisualizationCanvas as visual_locators
from common.locators.designer.components import resources_panel as Locators

class ResourcesPanel:
    
    @property
    def Fields(self): return _Fields()
    
    @property
    def Content(self): return _Content()
    
    @property
    def Containers(self): return _Containers()
    
    @property
    def Outline(self): return Outline()
    
    @property
    def Filters(self): return _Filters()
    
class _Fields(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locator = Locators.Fields
    
    @property
    def Dimensions(self):
        """
        Description: Return Dimensions data field object
        """
        dimensions = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.dimension_section, "Dimensions Field Section")
        return _Fields._Tree(dimensions, "Dimensions")
    
    @property
    def Measures(self):
        """
        Description: Return Measures data field object
        """
        measure = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.measure_section, "Measure Field Section")
        return _Fields._Tree(measure, "Measure")
    
    @property
    def Variables(self):
        """
        Description: Return Variables data field object
        """
        variables = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.variables_section, "Variables Field Section")
        return _Fields._Tree(variables, "Variables")
    
    @property
    def SearchTextBox(self):
        """
        Description: Return SearchTextBox object
        """
        search_textbox = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.search_textbox, "Field Search TextBox")
        return TextBox(search_textbox, "Field search")
    
    def select_fields_tab(self):
        """
        Description: Left click on Fields tab
        """
        self._core_utils.left_click(self.__get_tab_btn_obj("Fields"))
    
    def select_variables_tab(self):
        """
        Description: Left click on Variables tab
        """
        self._core_utils.left_click(self.__get_tab_btn_obj("Variables"))
        
    def __get_tab_btn_obj(self, tab_name):
        """
        Description: Return the tab button object
        """
        tab_btns = self._utils.validate_and_get_webdriver_objects_using_locator(self._locator.tab_buttons, "Designer Field Tabs")
        tab_index = self._javascript.find_element_index_by_text(tab_btns, tab_name)
        if tab_index != None:
            return tab_btns[tab_index]
        else:
            raise KeyError("[{0}] tab button not found in Fields panel".format(tab_name))
        
    class _Tree(ibx_custom_controls.ibxTree):
        
        def __init__(self, parent_object, tree_name):
            
            super().__init__(parent_object, tree_name)
            self.__name = tree_name
            self.__parent_object = parent_object
            
        def drag_to_bucket(self, item, bucketname, field=None, item_loc="middle", sx=0, sy=0, target_obj_loc="middle", tx=0, ty=0): 
            """
            Description: This drag and drop field item to query bucket
            :Usage - 1. drag_to_bucket('COUNTRY', 'Horizontal')
                     2. drag_to_bucket('CAR', 'Horizontal', 'COUNTRY', target_obj_loc="bottom_middle") # Use this way, if we try to drag and drop under bucket field
            """
            bucket_obj = bucket(bucket_name=bucketname)._get_field_object(field) if field else bucket(bucket_name=bucketname)._get_bucket_object()
            self._drag_and_drop_(item, bucket_obj, item_loc, sx, sy, target_obj_loc, tx, ty)
        
        def click_menu_button(self): 
            """
            Description: Left click on Menu button icon
            """
            menu_btn = self._utils_.validate_and_get_webdriver_object_using_locator(Locators.Fields.section_menu_button, self.__name + " Menu Button", self.__parent_object)
            self._core_utils_.left_click(menu_btn)
        
        def drag_to_container(self, item, container_name, container_index=1, item_loc="middle", sx=0, sy=0, target_obj_loc="middle", tx=0, ty=0):
            """
            Description: This function will drag and drop resource tree item to container
            Usage: drag_to_container('COUNTRY', 'CONTAINER 1')
            """
            container_obj = PageCanvas().Containers._get_container_object(container_name, container_index)
            self._drag_and_drop_(item, container_obj, item_loc, sx, sy, target_obj_loc, tx, ty)
            
        def drag_to_heading(self, item, item_loc="middle", sx=0, sy=0, target_obj_loc="middle", tx=0, ty=0):
            """
            Description: This function will drag and drop resource tree item to visualization heading
            Usage: drag_to_heading('COUNTRY')
            """
            heading_obj = self._utils.validate_and_get_webdriver_object_using_locator(visual_locators.Heading.heading, "Visualization Heading")
            self._drag_and_drop_(item, heading_obj, item_loc, sx, sy, target_obj_loc, tx, ty)
            
        def drag_to_footing(self, item, item_loc="middle", sx=0, sy=0, target_obj_loc="middle", tx=0, ty=0):
            """
            Description: This function will drag and drop resource tree item to visualization footing
            Usage: drag_to_footing('COUNTRY')
            """
            footing_obj = self._utils.validate_and_get_webdriver_object_using_locator(visual_locators.Footing.footing, "Visualization Footing")
            self._drag_and_drop_(item, footing_obj, item_loc, sx, sy, target_obj_loc, tx, ty)
        
        def drag_to_visual_filter_toolbar(self, item, item_loc="middle", sx=0, sy=0, target_obj_loc="middle", tx=0, ty=0):
            """
            Description: Drag and drop fields into Visualization Filter Tool bar
            :Usage - drag_to_visual_filter_toolbar('COUNTRY')
            """
            visual_filter_toolbar = self._utils.validate_and_get_webdriver_object_using_locator(filter_locators.visual_filter_toolbar, "Visual Filter Toolbar")
            self._drag_and_drop_(item, visual_filter_toolbar, item_loc, sx, sy, target_obj_loc, tx, ty)
            self._webelement.wait_for_element_text(filter_locators.visual_filter_toolbar, item, 60)
        
        def drag_to_page_fitler_toolbar(self, item, item_loc="middle", sx=0, sy=0, target_obj_loc="middle", tx=0, ty=0):
            """
            Description: Drag and drop fields into Page Filter Tool bar
            :Usage - drag_to_page_fitler_toolbar('COUNTRY')
            """
            page_filter_toolbar = self._utils.validate_and_get_webdriver_object_using_locator(filter_locators.page_filter_toolbar, "Page Filter Toolbar")
            self._drag_and_drop_(item, page_filter_toolbar, item_loc, sx, sy, target_obj_loc, tx, ty)
            self._webelement.wait_for_element_text(filter_locators.page_filter_toolbar, item, 60)
        
        
class _Content(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locator = Locators.Content
        
    def drag_to_page_section(self, item_path, section_index=1, section_location='top_left', x=0, y=0):
        """
        Description: Drag the content to page section
        """
        item_obj = self._get_item_object(item_path)
        item_loc = self._core_utils.get_web_element_coordinate(item_obj)
        section_loc = PageCanvas().Section._get_section_grid_location(section_index, section_location, x, y)
        self._core_utils.python_left_click(item_obj)
        uisoup.mouse.drag(item_loc['x'], item_loc['y'], section_loc['x'], section_loc['y'])
        PageCanvas().wait_for_text(item_path.split("->")[-1], 45)
        self._utils.wait_for_page_loads(30)
    
    def drag_to_container(self, item_path, container_title=None, container_index=1, container_location='middle', x=0, y=0):
        """
        Description: Drag content to container
        """
        item_obj = self._get_item_object(item_path)
        item_loc = self._core_utils.get_web_element_coordinate(item_obj)
        container_obj = PageCanvas().Containers._get_container_object(container_title, container_index)
        container_loc = self._core_utils.get_web_element_coordinate(container_obj, container_location, x, y)
        self._core_utils.python_left_click(item_obj)
        uisoup.mouse.press_button(item_loc['x'], item_loc['y'])
        uisoup.mouse.move(container_loc['x'], container_loc['y'])
        time.sleep(0.5)
        uisoup.mouse.release_button()
        self._utils.wait_for_page_loads(30)
        
    def select(self, item_path):
        """
        Description: Expand the parent folder and select the item
        """
        item_obj = self._get_item_object(item_path)
        #self._core_utils.left_click(item_obj)
        item_obj.click()
    
    def wait_for_text(self, text, time_out, pause_time=0, case_sensitive=False, raise_error=True, javascript=False):
        
        self._webelement.wait_for_element_text(Locators.RESOURCE, text, time_out, pause_time, case_sensitive, raise_error, javascript)
        
    def _get_item_object(self, item_path):
        """
        Description: Expand the folders and return item object
        """
        items_list = item_path.split("->")
        for index, item in enumerate(items_list, 1):
            self.wait_for_text(item, 30, raise_error=False, javascript=True)
            items_obj = self._driver.find_elements(*self._locator.items)
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

class _Containers(ibx_custom_controls.ibxAccordionPage):
    
    def __init__(self):
        
        self._name = 'Containers'
        super().__init__(Locators.RESOURCE, self._name)
        self._object = self._get_accordion_page_object()
    
    def drag_to_page_section(self, container_name, section_index=1, section_location='top_left', x=0, y=0):
        """
        Description: Drag the container to page section
        """
        basic_container_object = self._get_container_object(container_name)
        basic_container_loc = self._core_utils.get_web_element_coordinate(basic_container_object)
        section_loc = PageCanvas().Section._get_section_grid_location(section_index, section_location, x, y)
        self._core_utils.python_left_click(basic_container_object)
        uisoup.mouse.drag(basic_container_loc['x'], basic_container_loc['y'], section_loc['x'], section_loc['y'])
        self._utils.wait_for_page_loads(30)
    
    def drag_to_container(self, container_name, container_title=None, container_index=1, container_location='middle', x=0, y=0):
        """
        Description: Drag container to container
        """
        basic_container_object = self._get_container_object(container_name)
        basic_container_loc = self._core_utils.get_web_element_coordinate(basic_container_object)
        container_obj = PageCanvas().Containers._get_container_object(container_title, container_index)
        container_loc = self._core_utils.get_web_element_coordinate(container_obj, container_location, x, y)
        self._core_utils.python_left_click(basic_container_object)
        uisoup.mouse.press_button(basic_container_loc['x'], basic_container_loc['y'])
        uisoup.mouse.move(container_loc['x'], container_loc['y'])
        time.sleep(0.5)
        uisoup.mouse.release_button()
        self._utils.wait_for_page_loads(30)
    
    def double_click(self, container_name):
        """
        Description: Double click on container
        """
        container_element = self._get_container_object(container_name)
        self._core_utils.double_click(container_element, pause_time=0)
        
    def verify_containers(self, expected_list, step_num, assert_type='equal'):
        """
        Description: will verify containers
        :Usage - verify_containers(['Basic', 'Tab', 'Carosual'], '01')
        """
        self._webelement.verify_elements_text(Locators.BasicContainers.containers, expected_list, step_num, self._name, assert_type, parent_instance=self._object)
        
    def _get_container_object(self, name):
        """
        Description: Return the container object by name
        """
        container_objects = self._utils.validate_and_get_webdriver_objects_using_locator(
            Locators.BasicContainers.containers, self._name, self._object)
        error_msg = "[{}] Container not found in [{}] panel".format(name, self._name)
        return self._core_utils.get_element_object_by_text_using_javascript(container_objects, name, error_msg)

class Outline(ibx_custom_controls.ibxAccordionPane):
    
    def __init__(self):
        
        self._name = 'Outline'
        super().__init__(Locators.RESOURCE, self._name)
        self._tree = ibx_custom_controls.ibxTree(self._get_accordion_page_object(), self._name)
        self._tree._locators_ = Locators.Outline
    
    def click_on_item(self, item_path):
        """
        Description: Left click on outline item
        :Usage = click_on_item("Section 1->Container 1")
        """
        self._tree.select(item_path)
    
    def right_click_on_item(self, item_path):
        """
        Description: Right click on Outline item
        :Usage = right_click_on_item("Section 1->Container 1")
        """
        self._tree.right_click(item_path)
    
    def double_click_on_item(self, item_path):
        """
        Description: Double click on Outline item
        :Usage = right_click_on_item("Section 1->Container 1")
        """
        self._tree.double_click(item_path)
    
    def expand_item(self, item_path):
        """
        Description: Expand  Outline item
        :Usage = expand_item("Section 1->Container 1")
        """
        self._tree.expand(item_path)
    
    def collapse_item(self, item_path, collapse_parent=True):
        """
        Description: Collapse Outline item
        :Usage = collapse_item("Section 1->Container 1")
        """
        self._tree.collapse(item_path, collapse_parent)
        
    def verify_items(self, expected, step_num, assert_type='equal', parent_node=None):
        """
        Description: Verify the Outline items
        :USage = verify_items(['Section 1'], '05.02', assert_type='in')
        """
        self._tree.verify_items(expected, step_num, assert_type, parent_node)
        
class _Filters(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locator = Locators
        
    def click_add_all_filters_to_page_button(self): 
        """
        Description: Left click on Menu button icon
        """
        add_filters_btn = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.Filters.add_all_filters_to_page, "Add all filters to page")
        self._core_utils.left_click(add_filters_btn)
            
    def drag_to_container_grid(self, container_title, filter_name, grid_index, container_index=1):
        """
        Description: Drag and drop filter options to container grid cell
        :Usage- drag_to_container_grid('Container 2', 'Region:', 1)
        """
        filter_tree_obj = self._get_filter_tree_object(filter_name)
        grid_cell_obj = PageCanvas().Containers.Grid(container_title, container_index).FilterGrid._get_cell_object(grid_index)
        filter_item_loc = self._core_utils.get_web_element_coordinate(filter_tree_obj)
        grid_cell_loc = self._core_utils.get_web_element_coordinate(grid_cell_obj)
        self._core_utils.python_left_click(filter_tree_obj)
        uisoup.mouse.press_button(filter_item_loc['x'], filter_item_loc['y'])
        uisoup.mouse.move(grid_cell_loc['x'], grid_cell_loc['y'])
        time.sleep(0.5)
        uisoup.mouse.release_button()
        self._utils.wait_for_page_loads(30)
        
    def drag_to_filter_bar(self, filter_name, filter_bar_cell_index):
        """
        Description: Drag and drop filter options to filter bar cell
        :Usage- drag_to_filter_bar('Region:', 1)
        """
        filter_tree_obj = self._get_filter_tree_object(filter_name)
        filter_cell_obj = PageCanvas().FilterGrid._get_cell_object(filter_bar_cell_index)
        filter_item_loc = self._core_utils.get_web_element_coordinate(filter_tree_obj)
        filter_cell_loc = self._core_utils.get_web_element_coordinate(filter_cell_obj)
        self._core_utils.python_left_click(filter_tree_obj)
        uisoup.mouse.press_button(filter_item_loc['x'], filter_item_loc['y'])
        uisoup.mouse.move(filter_cell_loc['x'], filter_cell_loc['y'])
        time.sleep(0.5)
        uisoup.mouse.release_button()
        self._utils.wait_for_page_loads(30)
        
    def right_click(self, filter_name):
        """
        Description: Right click on filter based on filter tree name
        :Usage - right_click('Category:')
        """
        filter_tree_obj = self._get_filter_tree_object(filter_name)
        self._core_utils.right_click(filter_tree_obj)
        
    def _get_filter_tree_object(self, tree_name):
        """
        Description: will return filter grid tree object
        """
        filter_tree_objects = self._webelement._get_objects(self._locator.Filters.filter_options)
        actual_fitler_index = self._javascript.find_element_index_by_text(filter_tree_objects, tree_name)
        return filter_tree_objects[actual_fitler_index]
    