from common.pages.basepage import BasePage
from selenium.webdriver.support import color
from common.locators.designer.page_canvas import Section as Locator
from common.locators.designer.page_canvas import Container as Container_Locator

class Section(BasePage):
    
    def __init__(self, parent_object):
        
        super().__init__()
        self.__parent_object = parent_object
        self._locators = Locator
    
    def _get_section_object(self, index=1):
        """
        Description: Return the section object
        """
        section_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.section, "Page Sections", self.__parent_object)
        if len(section_objects) >= index:
            return section_objects[index-1]
        else:
            raise IndexError("Page section {} not found".format(index))
    
    def _get_section_grid_object(self, section_index=1):
        """
        Description: Return the section grid object
        """
        section_object = self._get_section_object(section_index)
        grid_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.grid, "Page Section grid", section_object)
        return grid_object
    
    def _get_section_grid_location(self, section_index=1, location='top_left', x=0, y=0):
        """
        Description: Return the section grid x and y value
        """
        grid_object = self._get_section_grid_object(section_index)
        grid_location = self._core_utils.get_web_element_coordinate(grid_object, location, x, y)
        return grid_location
    
    def select(self, index, element_location='middle', xoffset=0, yoffset=0):
        
        """
        Description: select section based on index
        """
        self._javascript.scrollIntoView(self._get_section_object(index))
        self._core_utils.python_left_click(self._get_section_object(index), element_location, xoffset, yoffset)
        
    def verify_style_color(self, color_name, step_num, index=1):
        """
        Description: Will verify section background color based on section index
        :Usage - verify_style_color('blue', '05')
        """
        section_object  = self._get_section_object(index)
        actual_color = color.Color.from_string(self._utils.get_element_css_propery(section_object, "background-color")).rgb
        expected_color = self._utils.color_picker(color_name)
        msg = "Step {0} : Verify [{1}] color is applied for section".format(step_num, color_name)
        self._utils.asequal(expected_color, actual_color, msg)
        
    def right_click(self, index, element_location='middle', xoffset=0, yoffset=0):
        """
        Description: right click on the section basesd on index
        :Usage - right_click(1)
        """
        self._javascript.scrollIntoView(self._get_section_object(index))
        self._core_utils.python_right_click(self._get_section_object(index), element_location, xoffset, yoffset)
        
    def verify_containers_in_section(self, expected_titles, section_index, step_num, assert_type= 'equal'):
        """
        Description: verify container available in given section
        :Usage - verify_containers_in_section(['Container 1'], 1, '01.10')
        """
        section_object = self._get_section_object(section_index)
        self._webelement.verify_elements_text(Container_Locator.title, expected_titles, step_num, 'Containers in given section', assert_type, parent_instance = section_object)
        
        