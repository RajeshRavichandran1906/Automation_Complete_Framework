from common.lib.base import BasePage
from common.lib.javascript import JavaScript
from common.lib.utillity import UtillityMethods as utillobject
from common.lib.core_utility import CoreUtillityMethods as coreutilobj

class Context_Menu(BasePage):
    
    any_context_menu_css=None
    context_menu_name = None 
    context_menu_rows_name = None
    banner_css = None
    
    def __init__(self, driver):
        super(Context_Menu, self).__init__(driver)
    
    def verify_context_menu_is_visible(self, msg):
        '''
        '''
        utillobject.verify_object_visible(self, Context_Menu.any_context_menu_css, True, msg)
    
    def get_row_elements(self):
        row_elements_css=Context_Menu.any_context_menu_css + Context_Menu.context_menu_rows_name
        row_elements_description=Context_Menu.context_menu_name + ' rows'
        row_elements=utillobject.validate_and_get_webdriver_objects(self, row_elements_css, row_elements_description)
        return row_elements
    
    def get_row_element_values(self):
        row_elements=Context_Menu.get_row_elements(self)
        return [row_element.text.strip().replace('\n', ' ') for row_element in row_elements]
    
    def get_row_element_by_row_value(self, row_value):
        row_elements=Context_Menu.get_row_elements(self)
        token=False
        for row_element in row_elements:
            if row_element.text.strip() == row_value:
                token=True
                return row_element
        if token==False:
            error_msg='The requested row with value [' + row_value + '] is not available in the ' + Context_Menu.context_menu_name + ' context menu.'
            raise LookupError(error_msg)     
    
    def get_row_element_by_index(self, index_number):
        row_elements=Context_Menu.get_row_elements(self)
        try:
            return row_elements[index_number]
        except IndexError:
            error_msg='The requested row with index [' + str(index_number) + '] is not available in the ' + Context_Menu.context_menu_name + ' context menu.'
            raise IndexError(error_msg) 
       
    def select_menu_item(self, menu_item_path):
        for row_value in menu_item_path.split('->'):
            row_element = Context_Menu.get_row_element_by_row_value(self, row_value)
            coreutilobj.python_left_click(self, row_element)
    
    def verify_menu_item_availability(self, menu_item_value, msg, availability=True):
        row_element_values=Context_Menu.get_row_element_values(self)
        if availability == True:
            utillobject.asin(self, menu_item_value, row_element_values, msg)
        else:
            utillobject.as_notin(self, menu_item_value, row_element_values, msg)
            
    def verify_menu_items_available(self, expected_menu_item_list, msg):
        token=True
        row_element_values=Context_Menu.get_row_element_values(self)
        for expected_menu_item in expected_menu_item_list:
            if expected_menu_item not in row_element_values:
                token=False
                break
        if token == False:
            utillobject.asin(self, expected_menu_item, row_element_values, msg)
        else:
            utillobject.asequal(self, token, True, msg)
    
    def close_contex_menu(self):
        banner_elements_css = Context_Menu.banner_css
        banner_elements_description = Context_Menu.banner_name
        banner_element=utillobject.validate_and_get_webdriver_object(self, banner_elements_css, banner_elements_description)
        coreutilobj.python_left_click(self, banner_element)

class Main_Page(Context_Menu):
    Context_Menu.context_menu_name = 'Main Page context menu'
    Context_Menu.any_context_menu_css='div.pop-top > div.ibx-menu-box'
    Context_Menu.context_menu_rows_name = " > [data-ibx-type='ibxMenuItem']"
    Context_Menu.banner_css = ".banner-group-spacer"
    Context_Menu.banner_name = 'Main Page banner'

class ContextMenu:
    
    _root_css_ = ".pop-top"
    _menu_css_ = _root_css_ + " div[role][data-ibx-type$='Item']"
    _menu_label_css_ = _menu_css_ + " .ibx-label-text"

    def __init__(self, driver):
        
        self.driver = driver
        self._core_utils = coreutilobj(self.driver)
        self._utils = utillobject(self.driver)
        self._javascript = JavaScript(self.driver)
        
    def select(self, menu_path):
        """
        Description : Left click on context menu
        :Usage - select("Security->Owner...")
        """
        menu_path_list = menu_path.split("->")
        for loop, menu in enumerate(menu_path_list):
            self._utils.synchronize_until_element_is_visible(ContextMenu._root_css_, 10)
            menu_label_objects = self._utils.validate_and_get_webdriver_objects(ContextMenu._menu_label_css_, "Context menu labels")
            menu_index = self._javascript.find_element_index_by_text(menu_label_objects, menu)
            if menu_index is None :
                msg = "[{0}] Menu does not exit in context menu".format(menu)
                raise LookupError(msg)
            if loop != 0 and (menu_index!=0):
                context_menu_popup = self._utils.validate_and_get_webdriver_object(ContextMenu._root_css_, "Context menu popup")
                self._core_utils.python_move_to_element(context_menu_popup, "top_middle", yoffset=8)
            menu_objects = self._utils.validate_and_get_webdriver_objects(ContextMenu._menu_css_, "Context menu")
            self._core_utils.python_left_click(menu_objects[menu_index])
    
    def verify(self, expected_menus, step_num, assert_type='asequal', menu_path=None):
        """
        Description : Verify the visible context menu options text
        :Usage - verify(["Run", "Run...", "Edit", "Remove from Recents", "Add to Favorites", "Properties"], "02.01")
        """
        (menu_path != None) and self.select(menu_path)
        self._utils.synchronize_until_element_is_visible(ContextMenu._root_css_, 5)
        menu_objects = self._utils.validate_and_get_webdriver_objects(ContextMenu._menu_css_, "Context menu")
        actual_menus = [menu.text.strip().replace("\n", " ") for menu in menu_objects if menu.is_displayed()]
        msg = "Step {0} : Verify the context menu".format(step_num)
        self._utils.verify_list_values(expected_menus, actual_menus, msg, assert_type)
    
    def verify_bold_text_options(self, expected_menus, step_num, assert_type='asequal', menu_path=None):
        """
        Description : Verify the bold text context menu options
        :Usage - verify(["P292_S10660"], "02.01")
        """
        (menu_path != None) and self.select(menu_path)
        self._utils.synchronize_until_element_is_visible(ContextMenu._root_css_, 5)
        menu_objects = self._utils.validate_and_get_webdriver_objects(ContextMenu._menu_css_, "Context menu")
        actual_menus = [menu.text.strip().replace("\n", " ") for menu in menu_objects if menu.is_displayed() and menu.value_of_css_property('font-weight').strip() == '700']
        msg = "Step {0} : Verify the bold text context menu".format(step_num)
        self._utils.verify_list_values(expected_menus, actual_menus, msg, assert_type)
    
    def verify_disabled_options(self, expected_menus, step_num, assert_type='asequal', menu_path=None):
        """
        Description : Verify the disabled menu options text
        :Usage - verify(["Past Ctrl+V"], "02.01")
        """
        (menu_path != None) and self.select(menu_path)
        self._utils.synchronize_until_element_is_visible(ContextMenu._root_css_, 5)
        menu_objects = self._utils.validate_and_get_webdriver_objects(ContextMenu._menu_css_, "Context menu")
        actual_menus = []
        for menu in menu_objects :
            opacity = menu.value_of_css_property('opacity').strip()
            pointer_events = menu.value_of_css_property('pointer-events').strip()
            if opacity == '0.5' and pointer_events == 'none' :
                actual_menus.append(menu.text.strip().replace("\n", " "))
        msg = "Step {0} : Verify {1} options are disabled in context menu".format(step_num, expected_menus)
        self._utils.verify_list_values(expected_menus, actual_menus, msg, assert_type)
    
    def verify_selected_options(self, expected_menus, step_num, assert_type='asequal', menu_path=None):
        """
        Description : Verify the selected menu options text
        :Usage - verify(["Users"], "02.01")
        """
        (menu_path != None) and self.select(menu_path)
        self._utils.synchronize_until_element_is_visible(ContextMenu._root_css_, 5)
        menu_objects = self._utils.validate_and_get_webdriver_objects(ContextMenu._menu_css_, "Context menu")
        actual_menus = []
        for menu in menu_objects :
            marker_object = menu.find_elements_by_css_selector(".ibx-start-marker")
            if marker_object != []:
                marker_value = self._javascript.get_element_before_style_properties(marker_object[0], 'content')
                if marker_value == '"\uf00c"' :
                    actual_menus.append(menu.text.strip().replace("\n", " "))
        msg = "Step {0} : Verify {1} options selected in context menu".format(step_num, expected_menus)
        self._utils.verify_list_values(expected_menus, actual_menus, msg, assert_type)
        
    def verify_vertical_scrollbar_displayed(self, step_num):
        """
        Description : Verify whether vertical scroll bar displayed in context menu.
        :Usage - verify_vertical_scrollbar_displayed("01.02")
        """
        context_menu_popup = self._utils.validate_and_get_webdriver_object(ContextMenu._root_css_, "Context menu popup")
        status = self._javascript.check_element_has_vertical_scrollbar(context_menu_popup)
        msg = "Step {0} : Verify vertical scroll bar displayed in context menu".format(step_num)
        self._utils.asequal(True, status, msg)
    
    def close(self, element_object=None, location='top_left', x=-4, y=-4):
        """
        Description : Close the context menu by click on top left corner of context menu
        """
        element_object = element_object if element_object is not None else self._utils.validate_and_get_webdriver_object(ContextMenu._root_css_, "Context menu popup")
        self._core_utils.python_left_click(element_object, location,  xoffset=x, yoffset=y)