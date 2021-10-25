from common.pages.basepage import BasePage
from common.lib.webfocus import ibx_custom_controls
from common.locators.designer.components.sidebar import SideBar as Locators

class SideBar(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locators = Locators
        self._name = "Designer SideBar "
        
    @property  
    def Outline(self):
        """
        Description : It returns outline object to perform actions
        """
        name = self._name + "Outline"
        outline_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.outline, name)
        return ibx_custom_controls.Icon(outline_obj, self._locators.outline_icon, "", name)
    
    @property  
    def Fields(self):
        """
        Description : It returns fields object to perform actions
        """
        name = self._name + "Fields"
        fields_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.fields, name)
        return ibx_custom_controls.Icon(fields_obj, self._locators.fields_icon, "", name)
    
    @property  
    def Container(self):
        """
        Description : It returns container object to perform actions
        """
        name = self._name + "Container"
        container_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.container, name)
        return ibx_custom_controls.Icon(container_obj, self._locators.container_icon, "", name)
    
    @property  
    def Content(self):
        """
        Description : It returns content object to perform actions
        """
        name = self._name + "Content"
        content_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.content, name)
        return ibx_custom_controls.Icon(content_obj, self._locators.content_icon, "", name)
    
    @property  
    def Controls(self):
        """
        Description : It returns controls object to perform actions
        """
        name = self._name + "Controls"
        control_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.controls, name)
        return ibx_custom_controls.Icon(control_obj, self._locators.controls_icon, "", name)
    
    @property  
    def Filters(self):
        """
        Description : It returns filters object to perform actions
        """
        name = self._name + "Filters"
        filter_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.filters, name)
        return ibx_custom_controls.Icon(filter_obj, None, "", name)
    