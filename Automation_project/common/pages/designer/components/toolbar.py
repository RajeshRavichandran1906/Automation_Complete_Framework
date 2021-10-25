from common.lib import html_controls
from common.pages.basepage import BasePage
from common.lib.webfocus import ibx_custom_controls
from common.lib.webfocus.modal_dialog import Resources
from selenium.webdriver.common.by import By
from common.locators.designer.components.toolbar import Toolbar as Locators

class ToolBar(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locators = Locators
        self._name = "Designer Toolbar "
    
    @property  
    def Save(self):
        """
        Description : Return Icon class object and we can inform icon based actions
        """
        name = self._name + "Save"
        save_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.save, name)
        return ibx_custom_controls.Icon(save_obj, self._locators.save_icon, "", name)
    
    @property  
    def Undo(self):
        """
        Description : Return Icon class object and we can inform icon based actions
        """
        name = self._name + "Undo"
        save_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.undo, name)
        return ibx_custom_controls.Icon(save_obj, self._locators.undo_icon, "", name)

    @property  
    def Redo(self):
        """
        Description : Return Icon class object and we can inform icon based actions
        """
        name = self._name + "Redo"
        save_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.redo, name)
        return ibx_custom_controls.Icon(save_obj, self._locators.redo_icon, "", name)
    
    @property  
    def Help(self):
        """
        Description : Return Icon class object and we can inform icon based actions.
        """
        name = self._name + "Help"
        save_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.help, name)
        return ibx_custom_controls.Icon(save_obj, self._locators.help_icon, "", name)
    
    @property  
    def Advanced(self):
        """
        Description : Return Icon class object and we can inform icon based actions.
        """
        name = self._name + "Advanced"
        save_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.advanced, name)
        return ibx_custom_controls.Icon(save_obj, self._locators.advanced_icon, "", name)
    
    @property  
    def ApplicationMenu(self):
        """
        Description : Return Icon class object and we can inform icon based actions.
        """
        name = self._name + "Application Menu"
        application_menu_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.application_menu, name)
        return ibx_custom_controls.Icon(application_menu_obj, self._locators.application_menu_dropdown_icon, "\f0d7", name)
    
    @property
    def Data(self):
        """
        Description : Return Button class object and we can perform button based actions.
        """
        name = self._name + "Data Tab"
        data_tab_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.data, name)
        return html_controls.Button(data_tab_obj, name)
    
    @property
    def Visualization(self):
        """
        Description : Return Button class object and we can perform button based actions.
        """
        name = self._name + "Visualization Tab"
        visualziation_tab_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.visualization, name)
        return html_controls.Button(visualziation_tab_obj, name)
        
    def save(self, title=None, folder=None):
        """
        Description: Save the current designer file
        """
        resources = Resources(self._driver)
        self.Save.click()
        is_resources = self._webelement.wait_for_element_text(resources._locators_.base, "Save", 3, raise_error=False)
        if is_resources:
            (title != None) and resources.Title.enter_text(title)
            (folder != None) and resources.GridView.Folders.double_click(folder)
            resources.SaveButton.click()
            ok_button_loc = (By.CSS_SELECTOR, "div.pop-top .ibx-dialog-ok-button")
            ok_button = self._webelement.wait_for_element_text(ok_button_loc, "OK", 2, raise_error=False)
            ok_button and self._core_utils.python_left_click(ok_button)