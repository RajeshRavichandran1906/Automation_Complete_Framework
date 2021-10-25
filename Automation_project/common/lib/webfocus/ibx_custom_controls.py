"""--------------------------------------------------------------------------------------------
This file contains verify and action methods for ibx custom controls.
ibx custom controls means if element has data-ibx-type="ibxCheckBoxSimple" attribute then
we can consider as ibx cutom checkbox control.
--------------------------------------------------------------------------------------------"""
from common.pages.basepage import BasePage
from selenium.webdriver.common.by import By
from common.lib.html_controls import Button
from selenium.webdriver.support.color import Color
from common.locators import ibx_custom_controls as Locators
from selenium.common import exceptions as SeleniumExceptions
from common.locators.ibx_custom_controls import ContextMenu as ContextMenuLoc
  
class ibxCheckBoxSimple(BasePage):
    
    def __init__(self, checkbox_name):
        
        self._name_ = checkbox_name
        self._locators_ = Locators.ibxCheckBoxSimple
        super().__init__()
        
    def verify_displayed(self, step_num):
        """
        Description : Verify whether checkbox displayed 
        :Usage - verify_displayed("03.04")
        """
        msg = "Step {0} : Verify [{1}] CheckBox is displayed".format(step_num, self._name_)
        self._utils.asequal(True, self._object_.is_displayed(), msg)
        
    def verify_checked(self, step_num):
        """
        Description : Verify whether check box is checked
        :Usage - verify_unchecked("02.01")
        """
        msg = "Step {0} : Verify [{1}] CheckBox is checked".format(step_num, self._name_)
        marker_value = self._javascript.get_element_before_style_properties(self._object_, "content")
        state = True if marker_value == '"\ue834"' else False
        self._utils.asequal(True, state, msg)
    
    def verify_unchecked(self, step_num):
        """
        Description : Verify whether check box is unchecked
        :Usage - verify_unchecked("02.01")
        """
        msg = "Step {0} : Verify [{1}] CheckBox is unchecked".format(step_num, self._name_)
        marker_value = self._javascript.get_element_before_style_properties(self._object_, "content")
        state = True if marker_value == '"\ue835"' else False
        self._utils.asequal(True, state, msg)
        
    def check(self):
        """
        Description : Left click on checkbox to check if unchecked else won't click
        """
        ("uncheck" in self._object_.get_attribute('class')) and self._core_utils.left_click(self._object_)
    
    def uncheck(self):
        """
        Description : Left click on checkbox to uncheck if checked else won't click
        """
        ("uncheck" not in self._object_.get_attribute('class')) and self._core_utils.left_click(self._object_)
    
    def verify_disabled(self, step_num):
        """
        Description : Verify whether checkbox is disabled or not
        :Usage - verify_disabled("01.02")
        """
        opacity = self._object_.value_of_css_property('opacity')
        pointer_events = self._object_.value_of_css_property('pointer-events')
        status = all([opacity=='1', pointer_events=='none'])
        msg = "Step {0} : Verify [{1}] checkbox is disabled".format(step_num, self._name_)
        self._utils.asequal(True, status, msg)
        
    @property
    def _object_(self):
        
        error_msg = "[{0}] CheckBox does not exist".format(self._name_)
        checkbox_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators_.checkbox, self._name_ + "CheckBox")
        checkbox_object = self._core_utils.get_element_object_by_text(checkbox_objects, self._name_, error_msg=error_msg, scroll_into_view=False)
        return self._utils.validate_and_get_webdriver_object_using_locator(self._locators_.marker, self._name_ + " CheckBox Marker", parent_object=checkbox_object)

class ibxSelectItemList(BasePage):
    
    def __init__(self, item_list_parent_locator=Locators.ibxSelectItemList.item_list, item_list_options_locator=Locators.ibxSelectItemList.options):
        
        self._item_list_locator = item_list_parent_locator
        self._item_list_options_locator = item_list_options_locator
        self._name = 'Select Item List'
        super().__init__()
    
    @property
    def _list_object(self):
        """
        Description: It will return visible Select Item List object 
        """
        item_list_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._item_list_locator, self._name)
        actual_item_list_objects = [item_list for item_list in item_list_objects if item_list.is_displayed()]
        if actual_item_list_objects != []:
            item_list_options = self._utils.validate_and_get_webdriver_objects_using_locator(self._item_list_options_locator, self._name + ' Options', actual_item_list_objects[0])
        else:
            msg = "[{}] not found".format(self._name)
            raise LookupError(msg)
        actual_item_list_options = [item_list_option for item_list_option in item_list_options if item_list_option.is_displayed()]
        return actual_item_list_options
    
    def _list_option_object(self, option_name):
        """
        Description: It will return list option object based on option name
        Usage: _list_option_object('Radio')
        """
        actual_item_list_options = self._list_object
        error_msg = "[{0}] list option does not exist".format(option_name)
        list_option_object = self._core_utils.get_element_object_by_text(actual_item_list_options, option_name, error_msg=error_msg, scroll_into_view=True)
        return list_option_object
        
    def select(self, option):
        """
        Description: It will select list option based on based option name
        Usage: select('Radio')
        """
        list_option_object = self._list_option_object(option)
        self._core_utils.left_click(list_option_object)
        
    def verify_options(self, expected_list, step_num, assert_type='equal'):
        """
        Description: It will verify list options 
        Usage: verify_options(['Checkbox', 'Radio']), '01')
        """
        self._webelement.verify_elements_text(self._list_object, expected_list, step_num, self._name + ' Options', assert_type)
        
    def select_multiple_options(self, options, click_outside=False):
        """
        Description: select multiple options in drop down list
        :Usage - select_multiple_options(['ENGLAND', 'ITALY', 'JAPAN'])
        """
        for option in options:
            list_option_object = self._list_option_object(option)
            if list_option_object:
                self._core_utils.left_click(list_option_object)
            else:
                msg = "Given option {} is not available".format(option)
                raise ValueError(msg)
        if click_outside: self._core_utils.python_left_click(self._utils.validate_and_get_webdriver_object("div[data-ibx-type='dfToolbar']", 'Top Toolbar'), element_location='middle', xoffset=250)
    
class ibxSwitch(BasePage):
    
    __slider_css = ".ibx-switch-slider"
    
    def __init__(self, ibx_switch_object, name):
        
        self._name_ = name
        self._object_ = ibx_switch_object
        super().__init__()
        
    def verify_displayed(self, step_num):
        """
        Description : Verify whether toggle button displayed 
        :Usage - verify_displayed("03.04")
        """
        msg = "Step {0} : Verify [{1}] toggle button is displayed".format(step_num, self._name_)
        self._utils.asequal(True, self._object_.is_displayed(), msg)
    
    def verify_on(self, step_num):
        """
        Description : Verify whether toggle button is On
        :Usage - verify_on("02.01")
        """
        msg = "Step {0} : Verify [{1}] toggle button is on".format(step_num, self._name_)
        slider_obj = self._utils.validate_and_get_webdriver_object(self.__slider_css, 'Toggle button slider', self._object_)
        transform_value = self._javascript.get_element_before_style_properties(slider_obj, "transform")
        bg_color = Color.from_string(slider_obj.value_of_css_property('background-color')).rgb
        transform_status = ((transform_value == 'matrix(1, 0, 0, 1, 18, 0)') or (transform_value == 'matrix(1, 0, 0, 1, 16, 0)'))
        status = all([transform_status, bg_color=='rgb(35, 183, 229)'])
        self._utils.asequal(True, status, msg)
    
    def verify_off(self, step_num):
        """
        Description : Verify whether toggle button is Off
        :Usage - verify_off("02.01")
        """
        msg = "Step {0} : Verify [{1}] toggle button is off".format(step_num, self._name_)
        slider_obj = self._utils.validate_and_get_webdriver_object(self.__slider_css, 'Toggle button slider', self._object_)
        transform_value = self._javascript.get_element_before_style_properties(slider_obj, "transform")
        bg_color = Color.from_string(slider_obj.value_of_css_property('background-color')).rgb
        status = all([transform_value=='none', bg_color=='rgb(204, 204, 204)'])
        self._utils.asequal(True, status, msg)
        
    def on(self):
        """
        Description : Left click on toggle button to on. If already toggle is On then won't click
        """
        ("checked" not in self._object_.get_attribute('class')) and self._core_utils.left_click(self._object_)
    
    def off(self):
        """
        Description : Left click on toggle button to off. If already toggle is Off then won't click
        """
        ("checked" in self._object_.get_attribute('class')) and self._core_utils.left_click(self._object_)
    
    def verify_disabled(self, step_num):
        """
        Description : Verify whether toggle button is disabled
        :Usage - verify_disabled("01.02")
        """
        opacity = self._object_.value_of_css_property('opacity')
        pointer_events = self._object_.value_of_css_property('pointer-events')
        status = all([opacity=='0.5', pointer_events=='none'])
        msg = "Step {0} : Verify [{1}] toggle button disabled".format(step_num, self._name_)
        self._utils.asequal(True, status, msg)
        
class ibxRadioButtonSimple(BasePage):
    
    def __init__(self, name, parent_object=None):
        
        self._name_ = name
        self._parent_obj = parent_object
        self._locators_ = Locators.ibxRadioButtonSimple
        super().__init__()
    
    def click(self):
        """
        Description : Left click on Radio button
        """
        self._core_utils.left_click(self._object_)
        
    def verify_disabled(self, step_num):
        """
        Description : Verify whether textbox is disabled or not
        :Usage - verify_disabled("01.02")
        """
        parent_obj = self._javascript.get_parent_element(self._object_)
        opacity = parent_obj.value_of_css_property('opacity')
        pointer_events = parent_obj.value_of_css_property('pointer-events')
        status = all([opacity=='0.5', pointer_events=='none'])
        msg = "Step {0} : Verify [{1}] Radio Button disabled".format(step_num, self._name_)
        self._utils.asequal(True, status, msg)
    
    def verify_checked(self, step_num):
        """
        Description : Verify whether Radio Button is checked
        :Usage - verify_unchecked("02.01")
        """
        msg = "Step {0} : Verify [{1}] Radio Button is checked".format(step_num, self._name_)
        marker_value = self._javascript.get_element_before_style_properties(self._object_, "content")
        state = True if marker_value == '"\ue837"' else False
        self._utils.asequal(True, state, msg)
    
    def verify_unchecked(self, step_num):
        """
        Description : Verify whether Radio Button is unchecked
        :Usage - verify_unchecked("02.01")
        """
        msg = "Step {0} : Verify [{1}] Radio Button is unchecked".format(step_num, self._name_)
        marker_value = self._javascript.get_element_before_style_properties(self._object_, "content")
        state = True if marker_value == '"\ue836"' else False
        self._utils.asequal(True, state, msg)
        
    @property
    def _object_(self):
        error_msg = "[{0}] Radio Button does not exist".format(self._name_)
        checkbox_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators_.radio_button, self._name_ + " Radio Button", self._parent_obj)
        checkbox_object = self._core_utils.get_element_object_by_text(checkbox_objects, self._name_, error_msg=error_msg, scroll_into_view=False)
        return self._utils.validate_and_get_webdriver_object_using_locator(self._locators_.marker, self._name_ + " CheckBox Marker", parent_object=checkbox_object)
    
class ibxTree(BasePage):
    
    """ We can inherit or use this class for tree based actions(exp: expand, collapse, verify and etc)"""
    
    def __init__(self, parent_object, tree_name):
        
        super().__init__()
        self._parent_obj_ = parent_object
        self._locators_ = Locators.ibxTree
        self._tree_name_ = tree_name
        
    def expand(self, item):
        """
        Description: Expand the given tree path one by one
        :arg - item : tree item name. Example : Dimensions or Dimensions->Product
        :Usage - expand("Dimensions->Product")
        """
        self._expand_tree_(item.split("->"))
    
    def right_click(self, item):
        """
        Description: Right click on tree item. 
        :Usage - right_click("Dimensions->Product")
        """
        item_object = self._get_tree_object_(item)
        #self._core_utils.right_click(item_object, pause_time=0)
        self._ActionChains(self._driver).context_click(item_object).perform()
        
    def select(self, item):
        """
        Description: Left click on tree item to select. 
        :Usage - right_click("Dimensions->Product")
        """
        item_object = self._get_tree_object_(item)
        item_object.click()
    
    def double_click(self, item):
        """
        Description: Right click on tree item. 
        :Usage - double_click("Dimensions->Product")
        """
        item_object = self._get_tree_object_(item)
        self._core_utils.python_doubble_click(item_object)
#         self._ActionChains(self._driver).double_click(item_object).perform()
        self._javascript.wait_for_page_loads(15, pause_time=0)
    
    def verify_items(self, expected, step_num, assert_type="equal", parent_node=None):
        
        if parent_node:
            parent_node = self._get_tree_object_(parent_node)
            tree_items_label_css = "#{} + {}".format(parent_node.get_attribute("id"), self._locators_.tree_items_label[1])
            tree_items_locator = (By.CSS_SELECTOR, tree_items_label_css)
        else:
            tree_items_locator = self._locators_.tree_items_label
        self._webelement.verify_elements_text(tree_items_locator, expected, step_num, self._tree_name_ + " Fields", assert_type, parent_instance=self._parent_obj_)    
        
    def collapse(self, tree_path, collapse_parent=True):
        """
        Description : Collapse the tree by clicking collapse icon
        arg : collapse_parent = if True then collapse then parent node otherwise collapse child nodes except parent
        :Usage - collapse("Product->Dimensions")
        """
        child_note_xpath = self._locators_.child_tree_xpath
        tree_path = tree_path.split("->")[::-1]
        parent_node_xpath = self._locators_.tree_xpath.format(tree_path[0])
        for index in range(len(tree_path), 0, -1):
            if not collapse_parent and index == 1:
                break
            target_node_xpath = child_note_xpath*(index-1)
            target_node_xpath = parent_node_xpath + target_node_xpath.format(*tree_path[1:index])
            nodes = self._parent_obj_.find_elements_by_xpath(target_node_xpath)
            if nodes != []:
                self._javascript.scrollIntoView(nodes[0], wait_time=0.5)
                collapse_icon = nodes[0].find_elements(*self._locators_.collapse_icon)
                (collapse_icon != []) and collapse_icon[0].click()
                self._utils.wait_for_page_loads(15, pause_time=0.5)
            else:
                msg = "[{0}] item not found in '{1} tree.".format("->".join(tree_path[:index]), self._tree_name_)
                raise KeyError(msg)
                
    def _drag_and_drop_(self, item, target_obj,  item_loc="middle", sx=0, sy=0, target_obj_loc="middle", tx=0, ty=0):
        """
        Description: Drag the given item tree and drop into given target object.
        :Usage - double_click("Dimensions->Product")
        """
        item_object = self._get_tree_object_(item)
        self._core_utils.python_left_click(item_object)
        source_loc = self._core_utils.get_web_element_coordinate(item_object, item_loc, sx, sy)
        target_loc = self._core_utils.get_web_element_coordinate(target_obj, target_obj_loc, tx, ty)
        self._core_utils.drag_and_drop_without_using_click(source_loc['x'], source_loc['y'], target_loc['x'], target_loc['y'])
        
    def _expand_tree_(self, tree_path_list):
            """
            Description : Expand tree path and return the last tree path xpath value.
            :Usage : _expand_tree_("Dimensions->Product")
            """
            parent_obj_id = self._parent_obj_.get_attribute("id")
            tree_xpath = "//div[@id='{}']".format(parent_obj_id) + self._locators_.tree_xpath
            for tree in tree_path_list:
                tree_xpath = tree_xpath.format(tree)
                tree_objects = self._parent_obj_.find_elements_by_xpath(tree_xpath)
                if tree_objects != [] :
                    tree_object = tree_objects[0]
                    self._javascript.scrollIntoView(tree_object, wait_time=0.5)
                    expand_icon_objs = tree_object.find_elements(*self._locators_.exapnd_icon)
                    if expand_icon_objs != [] :
                        expand_icon_obj = expand_icon_objs[0]
                        #self._core_utils.left_click(expand_icon_obj, pause_time=0)
                        expand_icon_obj.click()
                        self._utils.wait_for_page_loads(15, pause_time=0.5)
                else :
                    msg = "[{0}] item not found in '{1} tree.".format(tree, self._tree_name_)
                    raise LookupError(msg)
                tree_xpath = tree_xpath + self._locators_.child_tree_xpath
            return tree_xpath
        
    def _get_tree_object_(self, tree_path):
        """
        Description : Return the tree object
        :Usage - _get_tree_object_("Dimensions->Product")
        """
        tree_path = tree_path.split("->")
        target_tree = tree_path[-1]
        tree_path = tree_path[:-1]
        tree_xpath = self._expand_tree_(tree_path)
        tree_objects = self._parent_obj_.find_elements_by_xpath(tree_xpath.format(target_tree))
        if tree_objects == [] :
            msg = "[{0}] item not found in '{1} tree.".format(target_tree, self._tree_name_)
            raise LookupError(msg)
        tree_object = tree_objects[0]
        self._javascript.scrollIntoView(tree_object, wait_time=0.5)
        return tree_object

class Icon(BasePage):
    
    """ We can inherit or use this class for Icon elements"""
    
    def __init__(self, parent_object, icon_loc, icon_unicode, name):
        
        super().__init__()
        self._name_ = name
        self._object_ = parent_object
        self._icon_loc_ = icon_loc
        self._unicode_ = icon_unicode
        
    def verify_text(self):
        pass
    
    def verify_disabled(self, step_num):
        """
        Description: Verify whether element is disabled by using 'opacity' and 'pointer-events' value.
        """
        opacity = self._object_.value_of_css_property('opacity')
        pointer_events = self._object_.value_of_css_property('pointer-events')
        status = all([opacity=='0.5', pointer_events=='none'])
        msg = "Step {0} : Verify [{1}] option is disabled.".format(step_num, self._name_)
        self._utils.asequal(True, status, msg)
    
    def verify_enabled(self):
        pass
    
    def click(self):
        """
        Description: Left click on Icon
        """
        #self._core_utils.left_click(self._object_)
        self._object_.click()
    
    def verify_color(self, color_name, step_num):
        """
        Description : Verify the color
        :Usage - verify_color('blue', '04.01')
        """
        msg = 'Step {0} : Verify [{1}] option color'.format(step_num, self._name_)
        self._utils.verify_element_color_using_css_property(None, color_name, msg, attribute='color', element_obj=self._object_)
    
    def verify_background_color(self, color_name, step_num):
        """
        Description : Verify the background color
        :Usage - verify_background_color('blue', '04.01')
        """
        msg = 'Step {0} : Verify [{1}] option background color'.format(step_num, self._name_)
        self._utils.verify_element_color_using_css_property(None, color_name, msg, attribute='background-color', element_obj=self._object_)

    def verify_displayed(self, step_num):
        icon_object = self._utils.validate_and_get_webdriver_object_using_locator(self._icon_loc_, self._name_, self._object_)
        actual_value = self._javascript.get_element_before_style_properties(icon_object, "content")
        icon_status = (True if actual_value == self._unicode_ else False) and icon_object.is_displayed()
        msg = 'Step {0} : Verify {1} icon is displayed'.format(step_num, self._name_)
        self._utils.asequal(True, icon_status, msg)

class CommonUtils(BasePage):
    
    def __init__(self):
        
        super().__init__() 
        
    def verify_pd_component_border_property(self, component_obj, expected, msg):
        """
        Description: Verify the page component border property like color, width, style and position.
        """
        directions = ['north', 'south', 'east', 'west']
        selection_xpath="./div[@class='pd-selection {}']"
        for direction in directions :
            selection_obj = component_obj.find_element_by_xpath(selection_xpath.format(direction))
            border_width = self._utils.get_element_border_property_value(selection_obj, 'width')
            border_color = Color.from_string(self._utils.get_element_border_property_value(selection_obj, 'color')).rgb
            border_style = self._utils.get_element_border_property_value(selection_obj, 'style')
            position = selection_obj.value_of_css_property('position')
            actual = {'with' : border_width, 'color' : border_color, 'style' : border_style, 'position' : position}
            if actual != expected :
                break
        self._utils.asequal(expected, actual, msg)
            
class ContextMenu(BasePage):
    
    def __init__(self, 
                context_menu_locator=ContextMenuLoc.context_menu, 
                options_locator=ContextMenuLoc.options, 
                options_label_locator=ContextMenuLoc.option_labels, 
                name='Context Menu'):
        
        super().__init__()
        self._context_menu_locator = context_menu_locator
        self._options_locator = options_locator
        self._options_label_locator = options_label_locator
        self._name = name
    
    def __get_visible_context_menu_dialog_objects(self):
        """
        Return all visible context menu objects as list
        """
        ibxmenus_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._context_menu_locator, self._name)
        visible_ibxmenus_objects = [menu for menu in ibxmenus_objects if menu.is_displayed()]
        if visible_ibxmenus_objects:
            return visible_ibxmenus_objects
        else:
            msg = "[{}] not visible".format(self._name)
            raise SeleniumExceptions.ElementNotVisibleException(msg)
    
    def select(self, menu_path):
        """
        Description: Left click on given item to select
        :arg- menu_path - Menu item name or menu item path. Exp: Run or Run...->Run in new window
        """
        menu_list = menu_path.split("->")
        for index, menu in enumerate(menu_list):
            context_menu_dialog = self.__get_visible_context_menu_dialog_objects()[index]
            option_labels = self._utils.validate_and_get_webdriver_objects_using_locator(self._options_label_locator, self._name + " Options label", context_menu_dialog)
            actual_option_labels = [option for option in option_labels if option.is_displayed()]
            option_index = self._javascript.find_element_index_by_text(actual_option_labels, menu)
            if option_index != None:
                options = self._utils.validate_and_get_webdriver_objects_using_locator(self._options_locator, self._name + " Options", context_menu_dialog)
                actual_option = [option for option in options if option.is_displayed()]
#                 self._core_utils.python_left_click(actual_option[option_index])
#                 self._core_utils.left_click(actual_option[option_index])
                (actual_option[option_index]).click()
            else:
                msg = "[{}] option not found in [{}]".format(menu, self._name)
                raise SeleniumExceptions.NoSuchElementException(msg)
        return index + 1
    
    def verify_disabled_options(self, expected_options, step_num, assert_type='equal', menu_path=None):
        """
        Description : Verify the disabled menu options text
        :Usage - verify(["Past Ctrl+V"], "02.01")
        """
        if menu_path:
            context_menu_dialog_index =  self.select(menu_path) 
        else:
            context_menu_dialog_index = 0 
        context_menu_dialog = self.__get_visible_context_menu_dialog_objects()[context_menu_dialog_index] 
        actual_options = []
        context_menu_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._options_locator, self._name, context_menu_dialog)
        for context_menu in context_menu_objects:
            opacity = context_menu.value_of_css_property('opacity').strip()
            pointer_events = context_menu.value_of_css_property('pointer-events').strip()
            if opacity == '0.5' and pointer_events == 'none' :
                actual_options.append(context_menu.text.strip().replace("\n", " "))
        self._utils.list_values_verification(expected_options, actual_options, step_num, self._name, assert_type)
        
    def verify_options(self, expected_list, step_num, menu_path=None, assert_type='equal'):
        """
        Description : Verify all the available options in the context menu dialog.
        :Usage - verify_options(['Tab', 'Accordion', 'Carousel'], "07.01", "Convert to")
        """
        if menu_path:
            context_menu_dialog_index =  self.select(menu_path) 
        else:
            context_menu_dialog_index = 0
        context_menu_dialog = self.__get_visible_context_menu_dialog_objects()[context_menu_dialog_index]
        self._webelement.verify_elements_text(self._options_locator, expected_list, step_num, self._name, assert_type, parent_instance=context_menu_dialog)
        
    def verify_checked_options(self, expected_options, step_num, assert_type='equal', menu_path= None):
        """
        Description : Verify checked items in context menus
        :Usage - verify_checked_options('['color', 'text']', '04.01')
        """
        if menu_path != None:
            context_menu_dialog_index = self.select(menu_path)
        else:
            context_menu_dialog_index = 0
        context_menu_object = self.__get_visible_context_menu_dialog_objects()[context_menu_dialog_index]
        context_menu_options_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._options_locator, self._name, context_menu_object)
        actual_options = []
        for menu in context_menu_options_objects:
            try:
                marker_object = menu.find_element_by_css_selector(".ibx-start-marker")
            except:
                continue
            if marker_object.is_displayed() and marker_object != None:
                marker_value = self._javascript.get_element_before_style_properties(marker_object, 'content')
                if marker_value == '"\uf00c"' :
                    actual_options.append(menu.text.strip().replace("\n", " "))
        self._utils.list_values_verification(expected_options, actual_options, step_num, "Disabled " + self._name, assert_type)
     
class ibxAccordionPage(BasePage):
    
    def __init__(self, parent_instance, name):
        
        super().__init__()
        self._name = name
        self._panel_object = self._webelement._get_object(parent_instance, self._name)
        self._loctors = Locators.ibxAccordionPage
        
    def _get_accordion_page_object(self):
        """
        Description: Return the accordion page object by name
        """
        accordions = self._utils.validate_and_get_webdriver_objects_using_locator(self._loctors.accordion_pages, "Accordion Panels", self._panel_object)
        labels = self._utils.validate_and_get_webdriver_objects_using_locator(self._loctors.labels, "Accordion Panel Labels", self._panel_object)
        visible_accordions =  [accordion for accordion in accordions if accordion.is_displayed()]
        visible_labels =  [label for label in labels if label.is_displayed()]
        label_index = self._javascript.find_element_index_by_text(visible_labels, self._name)
        if label_index != None:
            return visible_accordions[label_index]
        else:
            msg = "[{}] Accordion panel not found".format(self._name)
            raise LookupError(msg)
        
class ibxAccordionPane(BasePage):
    
    def __init__(self, parent_instance, name):
        
        super().__init__()
        self._name = name
        self._panel_object = self._webelement._get_object(parent_instance, self._name)
        self._loctors = Locators.ibxAccordionPane
        
    def _get_accordion_page_object(self):
        """
        Description: Return the accordion page object by name
        """
        accordions = self._utils.validate_and_get_webdriver_objects_using_locator(self._loctors.accordion_panes, "Accordion Panels", self._panel_object)
        labels = self._utils.validate_and_get_webdriver_objects_using_locator(self._loctors.labels, "Accordion Panel Labels", self._panel_object)
        visible_accordions =  [accordion for accordion in accordions if accordion.is_displayed()]
        visible_labels =  [label for label in labels if label.is_displayed()]
        label_index = self._javascript.find_element_index_by_text(visible_labels, self._name)
        if label_index != None:
            return visible_accordions[label_index]
        else:
            msg = "[{}] Accordion panel not found".format(self._name)
            raise LookupError(msg)
        
        
class ibxSpinner(BasePage):

    def __init__(self, name="Spinner box", index=0, parent_object=None):
        self._name = name
        self._index = index
        self._parent_obj = parent_object
        self._locators = Locators.ibxSpinner
        super().__init__()
        
    def verify_text(self, expected_text, step_no):
        """
        Description : Verify text in spinner text box
        :Usage - verify_text('7', '04.01')
        """
        actual_text = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.text_box, self._name, self._get_spinner_object()).get_attribute("aria-valuenow").strip()
        msg = 'Step {0} : Verify [{1}] text in spinner box'.format(step_no, expected_text)
        self._utils.asequal(expected_text, actual_text, msg)
        
    def click_on_up_arrow(self, no_of_clicks=1):
        """
        Description : Verify text in spinner text box
        :Usage - click_on_up_arrow()
        """
        up_arrow_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.up_button, self._name, self._get_spinner_object())
        for _ in range(no_of_clicks):
            up_arrow_object.click()

    def click_on_down_arrow(self, no_of_clicks=1):
        """
        Description : Verify text in spinner text box
        :Usage - click_on_down_arrow()
        """
        up_arrow_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.down_button, self._name, self._get_spinner_object())
        for _ in range(no_of_clicks):
            up_arrow_object.click()
        
    def enter_text(self, text, clear="yes"):
        """
        Description : Verify text in spinner text box
        :Usage - verify_text('7', '04.01')
        """
        text_box_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.text_box, self._name, self._get_spinner_object())
        backspace = '\ue003'
        enter = '\ue007'
        if clear == "no":
            pass
        else:
            text_value = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.text_box, self._name, self._get_spinner_object()).get_attribute("aria-valuenow").strip()
            for _ in range(len(text_value)):
                text_box_object.send_keys(backspace)
        text_box_object.send_keys(text)
        text_box_object.send_keys(enter)
        
    def _get_spinner_object(self):
        """
        Description: Return the spinner box object.
        """
        spinner_box_objs = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.spinner_box, self._name, self._parent_obj)
        curr_spinner_box = [spinner_box for spinner_box in spinner_box_objs if spinner_box.is_displayed()]
        return curr_spinner_box[self._index]        
        
        
class ibxRadioButton(BasePage):

    def __init__(self, name="Radio button", parent_object=None):
        self._name = name
        self._parent_obj = parent_object
        self._locators = Locators.ibxRadioButton
        super().__init__()       
        
    def select(self, button_name): 
        """
        Description : Selects the radio button.
        :Usage - select("Style 1")
        """
        radio_buttons = self._get_radio_button_object()
        for button in radio_buttons:
            if button.text.strip() == button_name:
                button.click()
                self._utils.wait_for_page_loads(10)
    
    def verify_options(self, expected_list, step_num, assert_type='equal'):
        """
        Description: Verify the radio button options
        :Usage - verify_options(['Default', 'Style 2', 'Style 3'])
        """
        self._webelement.verify_elements_text(self._get_radio_button_object(), expected_list, step_num, self._name + ' options', assert_type)
        
    def _get_radio_button_object(self):
        """
        Description: Return the spinner box object.
        """
        button_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.radio_button, self._name, self._parent_obj)
        curr_button_objects = [button_object for button_object in button_objects if button_object.is_displayed()]
        return curr_button_objects
        
        
class bucket(BasePage):
    
    def __init__(self, bucket_name="Vertical", name="bucket component", parent_object=None):
        self._bucket_name = bucket_name
        self._name = name
        self._parent_obj = parent_object
        self._locators = Locators.bucket
        super().__init__() 
        
    def right_click(self, field_name):
        """
        Description : Right click on field 
        """
        self._core_utils.right_click(self._get_field_object(field_name))

    def click_on_bucket_ellipsis(self):
        """
        Description : Click on the vertical ellipsis button in the bucket component.
        :Usage - click_on_bucket_ellipsis()
        """
        ellipsis_icon =  self._utils.validate_and_get_webdriver_object_using_locator(self._locators.bucket_ellipsis, self._bucket_name + "bucket ellipsis icon", self._get_bucket_object())
        self._core_utils.left_click(ellipsis_icon, pause_time=2)
    
    def delete_field(self, field_name):
        """
        Description : Delete a field available in the bucket.
        :Usage - delete_field("Product Category")
        """
        parent_obj = self._get_field_object(field_name)
        self._core_utils.python_move_to_element(parent_obj)
        self._webelement.wait_until_element_invisible(self._locators.field_delete_icon, 5, pause_time=2, parent_obj=parent_obj)
        delete_icon_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.field_delete_icon, "Delete icon", parent_obj)
        delete_icon_obj.click()
    
    def delete_all_fields(self):
        """
        Description : Deletes all available fields.
        :Usage - delete_all_fields()
        """
        self.click_on_bucket_ellipsis()
        ContextMenu().select("Clear")
    
    def click_on_field_axis_icon(self, field_name):
        """
        Description : Clicks the axis icon.
        :Usage - click_on_field_axis_icon("Product Category")
        """
        axis_icon_object =  self._utils.validate_and_get_webdriver_object_using_locator(self._locators.field_axis_icon, self._name, self._get_field_object(field_name))
        axis_icon_object.click()
    
    def click_on_field_sort_icon(self, field_name):
        """
        Description : Clicks the sort icon.
        :Usage - click_on_field_sort_icon("Product Category")
        """
        sort_icon_object =  self._utils.validate_and_get_webdriver_object_using_locator(self._locators.field_sort_icon, self._name, self._get_field_object(field_name))
        sort_icon_object.click()
    
    def verify_available_fields(self, field_names, step_num):
        """
        Description : To verify all available fields in bucket.
        :Usage - verify_available_fields(["Product Category", "Revenue", "Cost of Goods"], "10.11")
        """
        bucket = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.field_pill, self._bucket_name, self._get_bucket_object())
        fields = [field.text.strip() for field in bucket if field.is_displayed()]
        msg = 'Step {0} : Verify [{1}] fields are available'.format(step_num, field_names)
        self._utils.as_List_equal(field_names, fields, msg)
       
    def verify_left_axis_icon(self, field_name, step_num):
        """
        Description : To verify left axis icon.
        :Usage - verify_left_axis_icon("Revenue", "07.01")
        """
        icon = Icon(self._get_field_object(field_name), self._locators.left_axis, self._locators.left_axis_icon, "left_axis_icon")
        icon.verify_displayed(step_num)
    
    def verify_right_axis_icon(self, field_name, step_num):
        """
        Description : To verify Right axis icon.
        :Usage - verify_right_axis_icon("Revenue", "07.02")
        """
        icon = Icon(self._get_field_object(field_name), self._locators.right_axis, self._locators.right_axis_icon, "Right_axis_icon")
        icon.verify_displayed(step_num)
    
    def verify_bottom_axis_icon(self, field_name, step_num):
        """
        Description : To verify Bottom axis icon.
        :Usage - verify_bottom_axis_icon("Product Category", "07.03")
        """
        icon = Icon(self._get_field_object(field_name), self._locators.bottom_axis, self._locators.bottom_axis_icon, "Bottom_axis_icon")
        icon.verify_displayed(step_num)
    
    def verify_top_column_axis_icon(self, field_name, step_num):
        """
        Description : To verify Top column axis icon.
        :Usage - verify_top_column_axis_icon("Product Category", "07.04")
        """
        icon = Icon(self._get_field_object(field_name), self._locators.top_column, self._locators.top_column_icon, "Top_column_axis_icon")
        icon.verify_displayed(step_num)
    
    def verify_ascending_sort_icon(self, field_name, step_num):
        """
        Description : To verify ascending sort icon.
        :Usage - verify_ascending_sort_icon("Revenue", "07.05")
        """
        icon = Icon(self._get_field_object(field_name), self._locators.sort_ascending, self._locators.sort_ascending_icon, "Ascending_sort_icon")
        icon.verify_displayed(step_num)
    
    def verify_descending_sort_icon(self, field_name, step_num):
        """
        Description : To verify descending sort icon.
        :Usage - verify_descending_sort_icon("Revenue", "07.06")
        """
        icon = Icon(self._get_field_object(field_name), self._locators.sort_decending, self._locators.sort_decending_icon, "Descending_sort_icon")
        icon.verify_displayed(step_num)
        
    def wait_for_text(self, text, time_out=30):
        """
        Description : To wait for text available inside the bucket
        :Usage -  wait_for_text('COUNTRY')
        """
        self._webelement.wait_for_element_text(self._locators.field_pill, text, time_out, case_sensitive=True, parent_obj=self._get_bucket_object())
    
    def _get_bucket_object(self):
        """
        Description : Returns bucket object
        """
        bucket_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.bucket, self._name, self._parent_obj)
        bucket_obj = [bucket for bucket in bucket_objects if self._bucket_name in bucket.text.strip()][0]
        if bucket_obj != None:
            return bucket_obj
        else:
            msg = "[{}] bucket not found".format(self._bucket_name)
            raise LookupError(msg)
        
    def _get_field_object(self, field_name):
        """
        Description : Returns field object
        """
        field_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.field_pill, self._name, self._get_bucket_object())
        field_obj = [field for field in field_objects if field_name == field.text.strip()]
        if field_obj != None:
            return field_obj[0]
        else:
            msg = "[{0}] field not found in the [{1}] bucket".format(field_name, self._bucket_name)
            raise LookupError(msg)
        
        
class ibxDualListBox(BasePage):
    
    def __init__(self, name, parent_object=None):
        super().__init__()
        self._name = name
        self._parent_obj = parent_object
        self._locators_ = Locators.ibxDualListBox
           
    def select_options_in_all_options_area(self, options_name):
        """
        Description: Select options in all options area
        :Usage - select_options_in_all_options_area(['Canon FS300', 'Canon HFR11', 'Canon XHA1S'])
        """
        options_obj = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators_.all_options_side_rows, self._name + " Options Row", parent_object=self._parent_obj)
        options_checkbox_obj = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators_.all_option_area_row_checkbox, self._name + " Options Row Checkbox", parent_object=self._parent_obj)
        if options_obj and options_checkbox_obj:
            for option_name in options_name:
                for option, option_checkbox in zip(options_obj, options_checkbox_obj):
                    if option.text.strip() == option_name:
                        self._core_utils.python_left_click(option_checkbox)
        else:
            msg = "Given Options [{0}] not available".format(options_name)
            raise ValueError(msg)
        
    @property 
    def AddSelections(self): 
        add_selection_button_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators_.add_items, "Add Selections")
        return Button(add_selection_button_obj, "Add Selection")
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        