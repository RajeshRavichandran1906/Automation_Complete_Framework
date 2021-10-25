import sys
from common.locators.ia_group_dialog import GroupDialog as GroupDialogLocators
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard as Keyboard

class GroupDialog:
     
    def __init__(self, driver):
        
        self.driver = driver
        self._utils = UtillityMethods(self.driver)
        self._coreutils = CoreUtillityMethods(self.driver)
    
    def enter_values_in_field_textbox(self, values, clear=True):
        """
        Description : This method will click and field textox and clear current text and enter given text
        :arg - clear - True if you want clear current text else False
        :Usage - enter_values_in_field_textbox("Group 1")
        """
        field_textbox_obj = self._utils.validate_and_get_webdriver_object(GroupDialogLocators.field_textbox_css, "Field textbox")
        self._coreutils.left_click(field_textbox_obj)
        clear and field_textbox_obj.clear()
        field_textbox_obj.send_keys(values)
    
    def enter_values_in_search_box(self, values, clear=True):
        """
        Description : This method will click on search box and clear current text and enter given text
        :arg - clear - True if you want clear current text else False
        :Usage - enter_values_in_search_box("North America")
        """
        search_obj = self._utils.validate_and_get_webdriver_object(GroupDialogLocators.search_box_css, "Search box")
        self._coreutils.left_click(search_obj)
        clear and search_obj.clear()
        search_obj.send_keys(values)
    
    def click_search_icon(self):
        """
        Description : This method will left click on search button
        """        
        search_icon_obj = self._utils.validate_and_get_webdriver_object(GroupDialogLocators.search_icon_css, "Search icon")
        self._coreutils.left_click(search_icon_obj)
    
    def click_search_clear_icon(self):
        """
        Description : This method will left click on search clear icon to clear the search text box
        """
        clear_icon_obj = self._utils.validate_and_get_webdriver_object(GroupDialogLocators.search_clear_icon_css, "Search clear icon")
        self._coreutils.left_click(clear_icon_obj)
    
    def verify_field_textbox_values(self, expected_values, step_num):
        """
        Description : This method will verify field text box value
        :Usage - verify_field_textbox_values("Group 1", "02.02")
        """
        field_textbox_obj = self._utils.validate_and_get_webdriver_object(GroupDialogLocators.field_textbox_css, "Field textbox")
        actual_values = field_textbox_obj.get_attribute('value').strip()
        msg = "Step {0} : Verify [{1}] is displayed in field text box".format(step_num, expected_values)
        self._utils.asequal(expected_values, actual_values, msg)
    
    def click_group_button(self):
        """
        Description : This method will left click on group button
        """
        button_obj = self._utils.validate_and_get_webdriver_object(GroupDialogLocators.group_button_css, "Group button")
        self._coreutils.left_click(button_obj)
    
    def click_ok_button(self):
        """
        Description : This method will left click on OK button
        """
        button_obj = self._utils.validate_and_get_webdriver_object(GroupDialogLocators.ok_button_css, "Group button")
        self._coreutils.left_click(button_obj)
        self._utils.synchronize_until_element_disappear(GroupDialogLocators.ok_button_css, 90)
        
    def click_apply_button(self):
        """
        Description : This method will left click on Apply button
        """
        button_obj = self._utils.validate_and_get_webdriver_object(GroupDialogLocators.apply_button_css, "Apply button")
        self._coreutils.left_click(button_obj)
    
    def select_multiple_fields(self, fields_list):
        """
        Description : This method will select multiple fields by using ctrl.
        :Usage - select_multiple_fields(['2100', 'Canon HFR11', 'GS4W', 'N1000'])
        """
        for loop, field in enumerate(fields_list, 1) :
            field_obj = self.__get_field_object(field, 1)
            if sys.platform == 'linux':
                (loop!=1) and pykeyboard.press_key(pykeyboard.control_key)
                self._coreutils.python_left_click(field_obj)
                (loop!=1) and pykeyboard.release_key(pykeyboard.control_key)
            else:
                (loop!=1) and Keyboard.press('ctrl')
                self._coreutils.python_left_click(field_obj)
                (loop!=1) and Keyboard.release('ctrl')
    
    def __get_field_object(self, field_name, index=1):
        """
        Description : This method will scroll mouse and find the given field and return the field object
        :arg - field_name - Name of the field.
        """
        group_dialog_obj = self._utils.validate_and_get_webdriver_object(GroupDialogLocators.parent_css, "Group dialog")
        self._coreutils.python_move_to_element(group_dialog_obj)
        self._utils.scroll_down_and_find_item_using_mouse(GroupDialogLocators.fields_css, field_name)
        xpath = "//div[@id='dynaGrpsValuesTree']//table//td[normalize-space() = '{0}']".format(field_name)
        fields_object = self.driver.find_elements_by_xpath(xpath)
        if fields_object != [] :
            return fields_object[index - 1]
        else :
            error = "[{0}] field not exists in group field list".format(field_name)
            raise KeyError(error)