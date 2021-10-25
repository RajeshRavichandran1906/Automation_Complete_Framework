from common.pages.basepage import BasePage
from selenium.webdriver.support import color
from common.lib.webfocus import ibx_custom_controls
from common.lib.html_controls import Button
from common.locators.designer.components.visualization_tool_bar import VisualizationToolBar as Locators

class VisualizationToolBar(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locators = Locators
        self._name = "Designer VisualizationToolbar "
        
    @property  
    def AddData(self):
        """
        Description : It returns outline object to perform actions
        """
        name = self._name + "AddData"
        add_data_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.add_data, name)
        return ibx_custom_controls.Icon(add_data_obj, self._locators.add_data_icon, "\f1c0", name)
    
    @property  
    def AddVisualization(self):
        """
        Description : It returns fields object to perform actions
        """
        name = self._name + "AddVisualization"
        add_visualization_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.add_visualization, name)
        return ibx_custom_controls.Icon(add_visualization_obj, self._locators.add_visualization_icon, "\f080", name)
    
    @property  
    def ConvertToPage(self):
        """
        Description : It returns container object to perform actions
        """
        name = self._name + "ConvertToPage"
        convert_to_page_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.convert_to_page, name)
        return ibx_custom_controls.Icon(convert_to_page_obj, self._locators.convert_to_page_icon, "\f15b", name)
    
    @property  
    def FilterOptions(self):
        """
        Description : It returns content object to perform actions
        """
        name = self._name + "FilterOptions"
        filter_options_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.filter_options, name)
        return ibx_custom_controls.Icon(filter_options_obj, self._locators.filter_options_icon, "\f0b0", name)
    
    @property  
    def LiveData(self):
        """
        Description : It returns controls object to perform actions
        """
        name = self._name + "LiveData"
        live_data_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.live_data, name)
        return ibx_custom_controls.Icon(live_data_obj, self._locators.live_data_icon, "\e9d3", name)
    
    @property  
    def HideShowPanes(self):
        """
        Description : It returns controls object to perform actions
        """
        name = self._name + "HideShowPanes"
        hide_show_panes_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.hide_show_panes, name)
        return ibx_custom_controls.Icon(hide_show_panes_obj, self._locators.hide_show_panes_icon, "\e9d3", name)
    
    @property  
    def RunInNewWindow(self):
        """
        Description : It returns controls object to perform actions
        """
        name = self._name + "RuninNewWindow"
        run_in_new_window_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.run_in_new_window, name)
        return ibx_custom_controls.Icon(run_in_new_window_obj, self._locators.run_in_new_window_icon, "\e9e9", name)
    
    @property  
    def AddContainer(self):
        """
        Description : It returns object to perform actions
        """
        name = self._name + "AddContainer"
        add_container_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.add_container, name)
        return ibx_custom_controls.Icon(add_container_obj, self._locators.add_visualization_icon, "\f080", name)
    
    @property  
    def Info(self):
        """
        Description : It returns control object to perform actions
        """
        name = self._name + "Info"
        info_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.info, name)
        return ibx_custom_controls.Icon(info_obj, self._locators.info_icon, "\f002", name)
    
    @property
    def QuickFilter(self): 
        """
        Description : It returns control object to perform actions
        """
        name = self._name + "QuickFilter"
        quickfilter_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.add_all_filters_to_page, name)
        return _QuickFilter(quickfilter_obj, self._locators.filter_options_icon, "\f0b0", name)
    
    @property
    def OutputFormat(self): return _OutputFormat()
    
    
class _OutputFormat(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators
        self._name = 'Output Format '
        
    def __sync_decorator(func):
        """
        This decorator will wait for Output format pop up to visible and
         execute the passed function and again wait for pop up to invisible
        """
        def wrapper_func(self, *args, **kwargs):
            self._webelement.wait_until_element_visible(self._locators.output_format_parent, 30)
            func(self, *args, **kwargs)
            self._webelement.wait_until_element_invisible(self._locators.output_format_parent, 30)
        return wrapper_func
        
    @property
    def button(self):
        """
        Description : It returns button object to perform actions
        """
        name = self._name + "Button"
        button_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.output_format, name)
        return Button(button_obj, name)
    
    @__sync_decorator
    def select_output_format(self, option_name):
        """
        Description: Select output from the output format
        :Usage - select_output_format('AHTML')
        """
        self._webelement.select_object_based_on_name(self._locators.different_output_format, option_name)
        
    
class _QuickFilter(ibx_custom_controls.Icon):
    
    def __init__(self, quickfilter_obj, icon_locator, unicode_icon, name):
        super().__init__(quickfilter_obj, icon_locator, unicode_icon, name)
        self.object = quickfilter_obj
        self.icon_locator = icon_locator
        self.unicode_icon = unicode_icon
        self._locators = Locators
        self.name = name
    
    def verify_filter_control_value(self, expected_value, step_no):
        """
        Description : Verify filter control text with no of parameters to bound to the page.
        Usage: verify_filter_control_value("6", "07.02")
        """
        msg = "Step {0}: Verify quick filter control value is equal to {1}".format(step_no, expected_value)
        actual_value = self._javascript.get_element_before_style_properties(self.object, "content").strip('"')
        self._utils.asequal(actual_value, expected_value, msg)
    
    def verify_filter_control_color(self, step_num):
        """
        Description : Verify filter control text with no of parameters to bound to the page.
        Usage: verify_filter_control_color(07.02")
        """
        actual_color = color.Color.from_string(self._javascript.get_element_before_style_properties(self.object, "background-color")).rgb
        expected_color = self._utils.color_picker('mandy')
        msg = "Step {0} : Verify quick filter control color".format(step_num)
        self._utils.asequal(expected_color, actual_color, msg)
    
    def click_dropdown(self):
        """
        Description: This will click on the quick filter dropdown
        """
        button_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.filter_dropdown, self.name + ' Dropdown', self.object)
        button_obj.click()
    