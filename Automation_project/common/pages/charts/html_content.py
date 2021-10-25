from common.pages.basepage import BasePage
from selenium.webdriver.support import color
from common.locators.charts import html_content as Locators


class HtmlContent(BasePage):
    
    def verify_content_background(self, color_name, step_num):
        """
        Description: This method will verify html content background color
        Usage: verify_content_background('blue', '10.01')
        """
        background_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.HtmlContent.background, 'Background color')
        actual_color = color.Color.from_string(self._utils.get_element_css_propery(background_object, "background-color")).rgb
        expected_color = self._utils.color_picker(color_name)
        msg = "Step {0} : Verify [{1}] color is applied for container content".format(step_num, color_name)
        self._utils.asequal(expected_color, actual_color, msg)
        