
from .section import Section
from .container import Containers
from .filter_grid import FilterGrid
from common.pages.basepage import BasePage
from common.lib.webfocus.ibx_custom_controls import Icon
from common.locators.designer import page_canvas as Locator

class PageCanvas(BasePage):
    
    def __init__(self, parent_instance=Locator.EDIT_MODE):
        
        super().__init__()
        self.__parent_object = self._webelement._get_object(parent_instance, "Designer Edit Canvas")
        self._locator = Locator
        
    def wait_for_text(self, text, time_out=60, pause_time=0, case_sensitive=False, raise_error=True):
        
        self._webelement.wait_for_element_text(Locator.PAGE, text, time_out, pause_time, case_sensitive, raise_error)
    
    def verify_theme(self, theme_name, step_num):
        """
        Description: This Function will verify page background theme
        Usage: verify_theme('Midnight', '10')
        """
        page_object_background = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.BACKGROUND, 'Theme', self.__parent_object)
        background_color = page_object_background.value_of_css_property('background-image')
        if theme_name == 'Midnight':
            status = True if background_color in ['linear-gradient(to right, rgb(77, 64, 112) 0%, rgb(67, 110, 164) 100%)'] else False
        msg = "Step {0}: Verify [{1}] theme is applied in page canvas".format(step_num, theme_name)
        self._utils.asequal(True, status, msg)
        
    @property
    def Section(self): return Section(self.__parent_object)
    
    @property
    def Containers(self): return Containers(self.__parent_object)
    
    @property
    def Heading(self): return Heading(self.__parent_object)
    
    @property
    def FilterGrid(self): return FilterGrid(self._utils.validate_and_get_webdriver_object_using_locator(Locator.FilterGrid.filter_grid_parent, 'Filter Grid', self.__parent_object))
    
class Heading(BasePage):
    
    def __init__(self, heading_object):
        
        super().__init__()
        self._heading_object = heading_object
        self._locators = Locator.Heading
        
    def verify_heading(self, expected_page_heading, step_no):
        """
        Description: Function to verify page heading of the canvas is equal to
        Usage: verify_title(expected_title, container_object, "05.01")
        """
        msg = "Step {0} : Verify page heading of the canvas is equal to {1}.".format(step_no, expected_page_heading)
        heading_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.heading, "container title", self._heading_object)
        heading = heading_object.text.strip()
        self._utils.asequal(expected_page_heading, heading, msg)
    
    @property
    def Refresh(self): 
        refresh_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.refresh, "Refresh", self._heading_object)
        return Icon(refresh_object, self._locators.refresh_icon, "\e9ea", "Refresh")
    
    @property
    def ShowFilter(self): 
        filter_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.show_filter, "Show Filter", self._heading_object)
        return Icon(filter_object, self._locators.show_filter_icon, "\ea77", "Show Filter")
    
    @property
    def HideFilter(self): 
        filter_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.hide_filter, "Hide Filter", self._heading_object)
        return Icon(filter_object, self._locators.hide_filter_icon, "\ea77", "Hide Filter")
    
    @property
    def ExportToFile(self): 
        option_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.export_to_file, "Export To a File", self._heading_object)
        return Icon(option_object, self._locators.export_to_file_icon, "\f56e", "Export To a File")