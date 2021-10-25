from common.pages.basepage import BasePage
from common.locators.designer import dialog as Locators
from selenium.common import exceptions as SeleniumExceptions
from selenium.webdriver.common.by import By
from common.lib.webfocus import ibx_custom_controls
from common.lib import html_controls

class Dialog:
    
    @property
    def ChooseTemplate(self): return ChooseTemplate()
    
    @property
    def SelectDataSource(self): return SelectDataSource()
    
    @property
    def AddContent(self): return AddContent()
    
    @property
    def Alert(self): return Alert()
    
    @property
    def AddFilterControls(self): return AddFilterControls()
    
    @property
    def ConvertControlTo(self): return ConvertControlTo()
    
    
class Base(BasePage):
    
    def __init__(self, name):
        
        super().__init__()
        self._locators = Locators.Base
        self._name = name
        
    def wait_until_visible(self, time_out=10, pause_time=0, raise_error=True):
        """
        Description: Wait until dialog invisible
        """
        self._webelement.wait_until_element_visible(self._locators.dialog, time_out, pause_time, raise_error)
    
    def wait_for_text(self, text, time_out=10, pause_time=0, case_sensitive=False, raise_error=True):
        """
        Description: Wait until given text is present in dialog
        """
        self._webelement.wait_for_element_text(self._locators.dialog, text, time_out, pause_time, case_sensitive, raise_error)
    
    def wait_until_invisible(self, time_out=10, pause_time=0, raise_error=True):
        """
        Description: Wait until dialog invisible
        """
        self._webelement.wait_until_element_invisible(self._locators.dialog, time_out, pause_time, raise_error)
    
    def close(self, wait=True):
        """
        Description: Click on close icon to close the dialog
        :arg - wait : True if wait to until dialog not visible
        """
        close = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.close_icon, 'Modal dialog close icon', self._object)
        #self._core_utils.left_click(close)
        close.click()
        wait and self.wait_until_invisible()
        
    def verify_title(self, expected_title, step_num):
        """
        Description: Verify the modal dialog title
        """
        actual_title = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.title, 'Modal dialog title', self._object).text.strip()
        msg = "Step {0}: Verify [{1}] dialog title".format(step_num, self._name)
        self._utils.asequal(expected_title, actual_title, msg)
    
    @property
    def _object(self):
        """
        Description: Return the parent object of modal dialog.
        Raise an error if dialog is not visible
        """
        dialog_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.dialog, self._name)
        if dialog_object.is_displayed():
            return dialog_object 
        else:
            raise SeleniumExceptions.ElementNotVisibleException("[{}] dialog not visible".format(self._name))
    
class _Button(BasePage):
    
    def __init__(self, button_name, dialog_title, dialog_object):
        
        super().__init__()
        self._dialog_object = dialog_object
        self._dialog_title = dialog_title
        self._button_name = button_name
        self._button_locator = Locators.Base.buttons
    
    @property
    def _object(self):
        
        buttons_object = self._utils.validate_and_get_webdriver_objects_using_locator(
            self._button_locator, "{0} Dialog Buttons".format(self._button_name), parent_object=self._dialog_object)
        button_index = self._javascript.find_element_index_by_text(buttons_object, self._button_name)
        if button_index is None:
            msg = "[{0}] button not displayed in [{1}] dialog".format(self._button_name, self._dialog_title)
            raise LookupError(msg)
        else:
            return buttons_object[button_index]
    
    def click(self):
        """
        Description : Left click on button
        """
        self._core_utils.left_click(self._object)
        #self._object.click()
        
    def verify_enabled(self, step_num):
        """
        Description : Verify whether button is enabled
        :Usage - verify_disabled("02.01")
        """
        opacity = self._object.value_of_css_property('opacity').strip()
        pointer_events = self._object.value_of_css_property('pointer-events').strip()
        state = True if (opacity == '1' and pointer_events == 'all') else False
        msg = "Step {0} : Verify [{1}] button is enabled in [{2}] dialog".format(step_num, self._button_name, self._dialog_title)
        self._utils.asequal(True, state, msg)
    
    def verify_disabled(self, step_num):
        """
        Description : Verify whether button is disabled
        :Usage - verify_disabled("02.01")
        """
        opacity = self._object.value_of_css_property('opacity').strip()
        pointer_events = self._object.value_of_css_property('pointer-events').strip()
        state = True if (opacity == '0.5' and pointer_events == 'none') else False
        msg = "Step {0} : Verify [{1}] button is disabled in [{2}] dialog".format(step_num, self._button_name, self._dialog_title)
        self._utils.asequal(True, state, msg)

class Alert(Base):
    
    def __init__(self):
        
        super().__init__("Alert")
        self._locators = Locators.Alert
        
    @property
    def Yes(self):
        button = _Button("Yes", self._name, self._object)
        button._button_locator = self._locators.buttons
        return button
    
    @property
    def No(self):
        button = _Button("No", self._name, self._object)
        button._button_locator = self._locators.buttons
        return button
    
    @property
    def Cancel(self):
        button = _Button("Cancel", self._name, self._object)
        button._button_locator = self._locators.buttons
        return button
    
class ChooseTemplate(Base):
    
    def __init__(self):
        
        super().__init__("Choose Template")
        self._locators = Locators.ChooseTemplate
    
    @property
    def Common(self): return self._Templates(self._locators.common_templates, self._object, "Common")    
    
    @property
    def Custom(self): return self._Templates(self._locators.custome_templates, self._object, "Custom")    
    
    class _Templates(BasePage):
        
        def __init__(self, locator, parent_object, name):
            
            self._locator = locator
            self._parent_object = parent_object
            self._name = name
            super().__init__()
            
        def select(self, name):
            """
            Description: Select the given template from Choose Template dialog
            """
            self._webelement.wait_for_element_text(Locators.ChooseTemplate.dialog, name, 20)
            templates = self._utils.validate_and_get_webdriver_objects_using_locator(self._locator, "Designer Page templates", self._parent_object)
            error_msg = "[{}] {} template not found in Choose Template dialog".format(name, self._name)
            template_obj = self._core_utils.get_element_object_by_text_using_javascript(templates, name, error_msg, scroll_into_view=False)
            #self._core_utils.left_click(template_obj)
            template_obj.click()
            self._webelement.wait_for_element_text((By.CSS_SELECTOR, "div.pd-page-header"), "Page", 60)
            self._utils.wait_for_page_loads(10)
            
        def verify(self, expected_list, step_num, assert_type='equal'):
            """
            Description: Verify the templates
            """
            name = "{} Templates".format(self._name) 
            self._webelement.verify_elements_text(self._locator, expected_list, step_num, name, assert_type=assert_type, parent_instance=self._parent_object)
            
class AddContent(Base):
    
    def __init__(self):
        
        super().__init__('Add Content')
        
    def select(self, content_name):
        """
        Description: Select the given menu in the add content dialog
        Usage: select('Add content', '10')
        """
        add_content_objects = self._utils.validate_and_get_webdriver_objects_using_locator(Locators.AddContent.add_content, self._name, self._object)
        add_content_object_index = self._javascript.find_element_index_by_text(add_content_objects, content_name)
        if add_content_object_index != None:
            add_content_objects[add_content_object_index].click()
            self._utils.wait_for_page_loads(30)
        else:
            msg = "{1} options not available in Add Content Dialog".format(content_name)
            raise LookupError(msg)   
        
    def  click_dropdown(self):
        """
        Description: Click on the dropdown button in Add content dialog
        """
        dropdown_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.AddContent.dropdown_button, 'Dropdown '+ self._name, self._object)
        self._core_utils.python_left_click(dropdown_object)
        self._utils.wait_for_page_loads(30)

class AddFilterControls(Base):
    
    def __init__(self):
        super().__init__('Add Filter Controls')
        self._locators = Locators.AddFilterControls
    
    @property    
    def ExcludeOptionalParameters(self):
        """
        Description : It returns exclude optional parameters checkbox object to perform actions
        """
        name = "Exclude optional parameters"
        return ibx_custom_controls.ibxCheckBoxSimple(name)
    
    @property
    def CancelButton(self):
        """
        Description : It returns cancel button object to perform actions
        """
        button = _Button("Cancel", self._name, self._object)
        button._button_locator = self._locators.buttons
        return button
    
    @property
    def AddFilterControlsButton(self):
        """
        Description : It returns add filter controls button object to perform actions
        """
        button = _Button("Add filter controls", self._name, self._object)
        button._button_locator = self._locators.buttons
        return button
    
    @property
    def ControlDropdownOptions(self):
        """
        Description: It will return control dropdown options object to perform actions
        """
        return ibx_custom_controls.ibxSelectItemList() 
    
    def _get_parameter_checkbox_object(self):
        """
        Description: It will return parameter checkbox object
        """
        return self._utils.validate_and_get_webdriver_object_using_locator(self._locators.parameter_checkbox, 'Parameter Checkbox', self._object)
        
    def _get_parameter_option_checkbox_object(self, parameter_option_name):
        """
        Description: It will return parameter option checkbox object based on parameter option name
        Usage: _get_parameter_option_checkbox_object('MODEL') 
        """
        return self._object.find_element_by_xpath(self._locators.parameter_option_checkbox_xpath.format(parameter_option_name))
    
    def _get_parameter_model_dropdown_object(self, parameter_option_name):
        """
        Description: It will retrun model dropdown object based on parameter option name
        Usage: _get_parameter_model_dropdown_object('MODEL') 
        """
        return self._object.find_element_by_xpath(self._locators.parameter_control_dropdown_xpath.format(parameter_option_name))
        
    @property
    def ParameterCheckbox(self):
        """
        Description: Returns Parameter check box object to perform actions
        """
        return html_controls.CheckBox(self._get_parameter_checkbox_object(), self._name + ' Parameter Checkbox')
    
    def ParameterOptionCheckbox(self, parameter_option_name):
        """
        Description: Returns parameter option checkbox object based on parameter option name
        Usage: ParameterOptionCheckbox('MODEL') 
        """
        return html_controls.CheckBox(self._get_parameter_option_checkbox_object(parameter_option_name), self._name + ' Paramter Option Checkbox')
    
    def click_control_dropdown(self, parameter_option_name):
        """
        Description: It will click control dropdown based on parameter option name
        Usage: click_control_dropdown('MODEL')
        """
        control_object = self._get_parameter_model_dropdown_object(parameter_option_name)
        self._core_utils.left_click(control_object)
        
    def verify_selected_control(self, parameter_option_name, expected_selected_control, step_num):
        """
        Description: It will verify selected control based on parameter option name
        Usage: verify_selected_control('MODEL', 'Checkbox', '10')
        """
        actual_object = self._get_parameter_model_dropdown_object(parameter_option_name)
        actual_selected_control = actual_object.get_attribute('aria-label')
        state = True if expected_selected_control == actual_selected_control else False
        msg = "Step {0}: Verify [{1}] parameter has [{2}] selected as control".format(step_num, parameter_option_name, expected_selected_control)
        self._utils.asequal(True, state, msg)

class SelectDataSource(Base):
    
    def __init__(self):
        super().__init__("Select Data Source")
        self._locators = Locators.DataSourceDialog
    
    @property
    def CancelButton(self):
        """
        Description : It returns cancel button object to perform actions
        """
        button = _Button("Cancel", self._name, self._object)
        button._button_locator = self._locators.buttons
        return button
    
    @property
    def SelectButton(self):
        """
        Description : It returns add filter controls button object to perform actions
        """
        button = _Button("Select", self._name, self._object)
        button._button_locator = self._locators.buttons
        return button
        
    @property
    def ToolBar(self): return self._ToolBar()
    
    @property
    def GridView(self): return self._GridView()
    
    @property
    def ListView(self): return self._ListView()
    
    class _ToolBar(BasePage):
        
        @property
        def Workspace(self):
            pass
            
        @property
        def FilterByType(self):
            pass
        
        @property
        def SwitchToGridView(self):
            pass
        
        @property
        def SwitchToListView(self):
            pass
        
        @property
        def SwitchToFlatView(self):
            pass
        
        @property
        def SwitchToFolderView(self):
            pass
        
        @property
        def Search(self):
            pass
        
        
    class _GridView(BasePage):
        pass
    
    class _ListView(BasePage):
        
        def __init__(self):
            super().__init__()
            self._locator = Locators.DataSourceDialog
            
        def select_masterfile(self, path):
            """
            Description: This function will select master file in list view
            :Usage- select_master('ibisamp->car.mas')
            """
            path_list = path.split('->')  
            for path in path_list:
                self._webelement.wait_for_element_text(Locators.DataSourceDialog.dialog, path, 30)
                path_row_css = self._locator.ListView.rows.format(path)
                path_row_object = self._utils.validate_and_get_webdriver_object(path_row_css, 'Path Rows')
                self._javascript.scrollIntoView(path_row_object)
                if path != path_list[-1]:
                    self._core_utils.python_doubble_click(path_row_object) 
                else:
                    self._core_utils.python_left_click(path_row_object) 


class ConvertControlTo(Base):
    
    def __init__(self):
        
        super().__init__("Convert Control To")
        self._locators = Locators.ConvertControlTo
        
    def verify_options(self, expected_options, step_num, assert_type='equal'):
        """
        Description: verify convert control to options in dialog
        :Usage - verify_options()
        """
        self._webelement.verify_elements_text(self._locators.convert_options, expected_options, step_num, "Convert Control to Options", assert_type)
    
    def select_options(self, option_name):
        """
        Description: select convert option in the dialog based on option name
        :Usage - select_options("Toggle")
        """
        self._webelement.select_object_based_on_name(self._locators.convert_options, option_name)
    
    
    
        