from common.pages.basepage import BasePage
from selenium.common import exceptions as SeleniumExceptions
from common.locators.designer.components.content_picker import ContentPicker as Locators

class ContentPicker(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locators = Locators
        self._name = "Designer Content picker "
    
    def expand(self):
        """
        Description : Click on content picker expand arrow icon
        """
        expand = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.exapnd_icon, self._name + "expand arrow")
        self._core_utils.left_click(expand)
        self._utils.synchronize_with_visble_text(self._locators.base_css, "Common", 10, pause_time=0)
    
    def collapse(self):
        """
        Description : Click on content picker expand arrow icon
        """
        collpase = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.collapse_icon, self._name + "collapse arrow")
        self._core_utils.left_click(collpase)
        self._utils.synchronize_until_element_is_visible(self._locators.exapnd_icon[1], 10, pause_time=1)
    
    @property
    def All(self): 
        content_picker = self._utils.validate_and_get_webdriver_object_using_locator(Locators.all_content_container, "Designer Content picker")
        return _Contents(content_picker)
    
    @property
    def Common(self): return _Section("Common")
    
    @property
    def Report(self): return _Section("Report")
    
    @property
    def Business(self): return _Section("Business")
    
    @property
    def Custom(self): return _Section("Common")

class _Contents(BasePage):
    
    def __init__(self, section_object=None):
    
        super().__init__()
        self._section_object = section_object
    
    def select(self, title):
        """
        Description: Left click on content to select
        :Usage - select("grid")
        """
        self._core_utils.left_click(self._get_content_object(title))
        self._utils.wait_for_page_loads(30, pause_time=0)
    
    def verify_tooltip(self, title, expected_tooltip, step_num):
        """
        Description: Verify the content tooltip
        :Usage: verify_tooltip("Ring", "Ring Pie1 measure and 1 dimension", "02.01")
        """
        actual_tooltip = self._get_content_object(title).get_attribute("title").strip()
        msg = "Step {0} : Verify [{1}] content tooltip in Designer Content picker".format(title, expected_tooltip)
        self._utils.asequal(expected_tooltip, actual_tooltip, msg)
    
    def verify_disabled(self, title, step_num):
        pass
    
    def _get_content_object(self, title):
        """
        Description: Return the content picker section object
        """
        content_css = "div[title^='{}']".format(title)
        content = self._section_object.find_elements_by_css_selector(content_css)
        if content:
            content_obj = content[0]
            self._javascript.scrollIntoView(content_obj,  wait_time=0)
            if content_obj.is_displayed():
                return content[0]
            else:
                raise SeleniumExceptions.ElementNotVisibleException("[{0}] content not visible in Designer Content Picker".format(title))
        else:
            raise KeyError("Unable to find [{0}] content in Designer Content Picker".format(title))
        
class _Section(_Contents):
    
    def __init__(self, section_name):
    
        self._name_ = section_name
        super().__init__()
        self._section_object = self._get_section_object()
        
    def expand(self):
        pass
    
    def collapse(self):
        pass
    
    def select(self, title, collapse=True):
        """
        Description: Left click on content to select
        :arg - collapse:bool = Collapse content picker container after selected content if True 
        :Usage - select("grid")
        """
        super().select(title)
        if collapse:
            ContentPicker().collapse()
        
    def _get_section_object(self):
        """
        Description: Return the content picker section object
        """
        section_object = self._driver.find_elements_by_xpath(Locators.section_xapth.format(self._name_))
        if section_object:
            return section_object[0]
        else:
            raise KeyError("Unable to find [{0}] section in Designer Content Picker".format(self._name_))