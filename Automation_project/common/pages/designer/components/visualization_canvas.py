import time
from common.pages import charts
from common.lib import html_controls
from common.pages.basepage import BasePage
from selenium.webdriver.support import color
from common.lib.webfocus import ibx_custom_controls
from common.locators.charts import common as Locators
from selenium.webdriver.support.ui import WebDriverWait
from common.lib.global_variables import Global_variables
from selenium.webdriver.support import expected_conditions as EC
from common.locators.designer.components.visualization_canvas import VisualizationCanvas as locator


class VisualizationCanvas(BasePage):
    
    def __init__(self):
        super().__init__()
        self._name = "Visualization Canvas"
        self._locators = locator
    
    @property
    def FormattingToolbar(self): return _FormattingToolbar()
    
    @property
    def Header(self): return _Heading_and_footing(locator.Heading.iframe, 'Heading')
    
    @property
    def Footer(self): return _Heading_and_footing(locator.Footing.iframe, 'Footing') 
    
    @property
    def Bar(self): return charts.Bar(parent_locator=Locators.content_chart)
    
    @property
    def Pie(self): return charts.Pie(parent_locator=Locators.content_chart)
    
    @property
    def Area(self): return charts.Area(parent_locator=Locators.content_chart)
    
    @property
    def Arc(self): return charts.Arc(parent_locator=Locators.content_chart)
    
    @property
    def Map(self): return charts.Map(parent_locator=Locators.content_chart)
    
    @property
    def RunMode(self): return _RunMode()
    
    def wait_for_text(self, text, time_out=60):
        """
        Description: Wait until given text visible in the chart preview
        """
        self._webelement.wait_for_element_text(self._locators.chart_preview, text, time_out)


class _RunMode(BasePage):
    
    def __init__(self):
        super().__init__()
    
    @property
    def Bar(self): return charts.Bar(parent_locator=Locators.html5_run_chart)
    
    @property
    def Area(self): return charts.Area(parent_locator=Locators.html5_run_chart)
    
    @property
    def Arc(self): return charts.Arc(parent_locator=Locators.html5_run_chart)
    
    @property
    def Map(self): return charts.Map(parent_locator=Locators.html5_run_chart)
    
    @property
    def Insight(self): return charts.Insight()
    
    @property
    def Heading(self): return _RunMode_Heading_and_footing(locator.Heading.RunMode.parent, 'RunMode Heading')
    
    @property
    def Footing(self): return _RunMode_Heading_and_footing(locator.Footing.RunMode.parent, 'RunMode Footing')
    
    @property
    def AutoDrill(self): return _AutoDrill()
    
    @property
    def BreadCrumbTrail(self): return _BreadCrumbTrail()
    
    def switch_to_frame(self):
        """
        Description: Switch inside Visualizaton in run mode
        """
        self._utils.switch_to_frame(frame_css="body iframe")


class _AutoDrill(BasePage):
    
    def __init__(self):
        super().__init__()
        self._name = "AutoDrill"
        self._locators = locator.RunMode.AutoDrill
        
    def hover_chart_riser(self, riser_css):
        """
        Description: will hover over chart riser based on given chart riser css
        """
        riser_obj = self._utils.validate_and_get_webdriver_object(riser_css, 'Riser CSS')
        self._core_utils.python_move_to_element(riser_obj)
        self._webelement.wait_until_element_invisible(self._locators.auto_drill_parent, 60)
        
    def select_autodrill_option(self, option_name, riser_css=None, hover_wait=False, wait_time=1.5):
        """
        Description: selection autodrill option based on the option name
        :Usage - select_autodrill_option('Drill down to Product Subcategory')
        """
        if riser_css: 
            self.hover_chart_riser(riser_css)
        if hover_wait:
            time.sleep(wait_time)
        option_list = option_name.split('->')
        if len(option_list) == 1:
            menu_options = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.menu_options, self._name + " Options")
            if menu_options:
                expected_menu_obj = self._javascript.find_elements_by_text(menu_options, option_list[0])
                if expected_menu_obj:
                    self._core_utils.python_move_to_element(expected_menu_obj[0])
                    self._core_utils.python_left_click(expected_menu_obj[0])
                else:
                    msg = "[{0}] autodrill option not available".format(option_list[0])
                    raise ValueError(msg)
            else:
                msg = "Autodrill options are not available"
                raise LookupError(msg)
        else:
            parent_menu_option = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.parent_menu_options, self._name + " Menu")
            self._core_utils.move_to_element(parent_menu_option)
            self._webelement.wait_until_element_invisible(self._locators.sub_menu_parent, 60)
            time.sleep(1.5)
            menu_options = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.sub_menu_options, self._name + ' Sub Menu Options')
            if menu_options:
                expected_menu_obj = self._javascript.find_elements_by_text(menu_options, option_list[1])
                self._javascript.scrollIntoView(expected_menu_obj)
                self._core_utils.python_move_to_element(expected_menu_obj[0])
                self._core_utils.python_left_click(expected_menu_obj[0])
            else:
                msg = "Autodrill options are not available"
                raise LookupError(msg)
                
    def verify_autodrill_options(self, expected_options, step_num, assert_type='equal'):
        """
        Description: Verify autodrill option 
        :Usage - verify_autodrill_options(['Drill down to Product Subcategory'])
        """
        time.sleep(1)
        menu_options = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.menu_options, self._name + " Options CSS")
        if menu_options:
            self._webelement.verify_elements_text(menu_options, expected_options, step_num, self._name + " Options", assert_type)
        else:
            msg = "Autodrill options are not available"
            raise LookupError(msg)
        
    def verify_tooltip_values(self, expected_values, step_num, assert_type='equal'):   
        """
        Description: Verify tooltip values, need to pass tooltip value as list
        :Usage - verify_tooltip_values(['Product Category:', 'Computers', 'Cost of Goods:', '$69,807,664.00'])
        """
        time.sleep(1.5)
        self._webelement.verify_elements_text(self._locators.tooltip_values, expected_values, step_num, self._name + ' Tooltip Values', assert_type)
        
          
class _BreadCrumbTrail(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = locator.RunMode.BreadCrumbTrail
        self._name = "Bread Crumb Trail"
        
    def verify_bread_crumb_trail(self, expected_trail, step_num, assert_type='equal'):
        """
        Description: Verify bread crumb trail in the run chart
        :Usage - verify_bread_crumb_trail(['Home', '(Product Category) Media Player'], "06")
        """
        bread_crumb_trail_objects = self._get_bread_crumb_trail_objects()
        self._webelement.verify_elements_text(bread_crumb_trail_objects, expected_trail, step_num, self._name, assert_type)
        
    def _get_bread_crumb_trail_objects(self):
        """
        Description: return only text bread crumb trail object as list
        """
        bread_crumb_trail_objects = self._webelement._get_objects(self._locators.bread_crumb_trail)
        actual_bread_crumb_trail_objects = []
        for bread_crumb in range(0, len(bread_crumb_trail_objects), 2):
            actual_bread_crumb_trail_objects.append(bread_crumb_trail_objects[bread_crumb])
        return actual_bread_crumb_trail_objects
        
class _FormattingToolbar(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = locator.FormattingToolbar
        self._name = "Formatting Toolbar"
    
    @property
    def SelectItem(self): return ibx_custom_controls.ibxSelectItemList()
            
    @property
    def Close(self):
        """
        Description : Return close Icon class object and we can inform icon based actions
        """
        name = self._name + " Close"
        close_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.close, name)
        return ibx_custom_controls.Icon(close_obj, self._locators.close, "", name)
    
    @property  
    def Bold(self):
        """
        Description : Return Bold Icon class object and we can inform icon based actions
        """
        name = self._name + " Bold"
        bold_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.bold, name)
        return ibx_custom_controls.Icon(bold_obj, self._locators.bold, "", name)
    
    @property
    def Color(self):
        """
        Description : Return color Icon class object and we can inform icon based actions
        """
        name = self._name + " Text color"
        color_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.text_color, name)
        return ibx_custom_controls.Icon(color_obj, self._locators.text_color, "", name)
    
    @property
    def BackgroundColor(self):
        """
        Description : Return Background color Icon class object and we can inform icon based actions
        """
        name = self._name + " Background color"
        background_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.background_color, name)
        return ibx_custom_controls.Icon(background_obj, self._locators.background_color, "", name)
        
    @property
    def FontName(self):
        """
        Description : Return Font Name Icon class object and we can inform icon based actions
        """
        name = self._name + " Font Name"
        fontname_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.font_name, name)
        return html_controls.TextBox(fontname_obj, name)
    
    def click_font_size_dropdown(self):
        """
        Description : Return Font Size Icon class object and we can inform icon based actions
        """
        name = self._name + " Font Size"
        fontsize_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.font_size, name)
        self._core_utils.python_left_click(fontsize_obj)
    
    def select_color_palette(self, color):
        """
        Description: Select color in color palette
        :Usage - select_color_palette('#ed1c24')
        """
        color = self._driver.find_element_by_css_selector(self._locators.color.format(color))
        color.click()
        self._webelement.wait_until_element_invisible(self._locators.color_palette, 30)


class _Heading_and_footing(BasePage):
        
    def __init__(self, parent, name):
        super().__init__()
        self._parent = parent
        self._name = name
        self._locators = locator
    
    def switch_to_frame(self, timeout=60):
        """
        Description: switch to frame heading or footing
        """
        frame = self._utils.validate_and_get_webdriver_object_using_locator(self._parent, self._name + " Frame")
        frame_location = self._core_utils.get_web_element_coordinate(frame, element_location='top_left')
        WebDriverWait(self._driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(frame))
        Global_variables.current_working_area_browser_x=frame_location['x']
        Global_variables.current_working_area_browser_y=frame_location['y']

    def verify_text_color(self, color_name, step_num):
        """
        Description: verify text color header or footer
        :Usage - verify_text_color('blue', '03')
        """
        text = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.Heading.title, self._name + " Color")
        actual_color = color.Color.from_string(self._utils.get_element_css_propery(text, "color")).rgb
        expected_color = self._utils.color_picker(color_name)
        msg = "Step {0} : Verify text color".format(step_num)
        self._utils.asequal(expected_color, actual_color, msg)
            
    def verify_text(self, expected_text, step_num, assert_type="equal"):
        """
        Description: Will verify the heading text 
        :Usage - verify_heading_text(["COUNTRY], '03')
        """
        self._webelement.verify_elements_text(self._locators.Heading.title, expected_text, step_num, self._name + " text", assert_type=assert_type)

    def verify_text_size(self, expected_size, step_num):
        """
        Description: Verify heading or footing text size
        :Usage -  verify_text_size("14", "03")
        """
        text_size_obj = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.Heading.title, self._name + " size")
        text_size_value = text_size_obj[1].get_attribute('style')
        value = True if expected_size in text_size_value else False
        msg = "Step: {} Verify header text size".format(step_num)
        self._utils.asequal(True, value, msg)
    
    def verify_text_background_color(self, color_name, step_num):
        """
        Description: verify heading or footing background color
        :Usage - verify_text_background_color('blue', '05')
        """
        text = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.Heading.title, self._name + " Background Color")
        actual_color = color.Color.from_string(self._utils.get_element_css_propery(text, "background-color")).rgb
        expected_color = self._utils.color_picker(color_name)
        msg = "Step {0} : Verify background color of text".format(step_num)
        self._utils.asequal(expected_color, actual_color, msg)
        
    def verify_highlighted_text(self, expected_text, step_num):
        """
        Description: verify heading or footing highlighted text
        :Usage - verify_highlighted_text("COUNTRY", "01")
        """
        highligted_text = self._javascript.get_highlighted_text()
        msg = "Step {}: verify highlighted text".format(step_num)
        self._utils.asequal(expected_text, highligted_text, msg)

    def wait_for_text(self, text, timeout=60):
        """
        Description: Wait for text in header or footer
        """
        self._webelement.wait_for_element_text(self._locators.Heading.parent, text, timeout)
        
        
class _RunMode_Heading_and_footing(BasePage):
        
    def __init__(self, parent, name):
        super().__init__()
        self._parent = parent
        self._name = name
        self._locators = locator
        
    def _parent_object(self):
        """
        Description: Will return parent object based on Heading or Footing
        """
        return self._utils.validate_and_get_webdriver_object_using_locator(self._parent, "Parent Object")

    def verify_text_color(self, color_name, step_num):
        """
        Description: verify text color heading or footing in Runmode
        :Usage - verify_text_color('blue', '03')
        """
        text = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.Heading.title, self._name + " Color", parent_object=self._parent_object())
        actual_color = color.Color.from_string(self._utils.get_element_css_propery(text, "color")).rgb
        expected_color = self._utils.color_picker(color_name)
        msg = "Step {0} : Verify text color".format(step_num)
        self._utils.asequal(expected_color, actual_color, msg)
            
    def verify_text(self, expected_text, step_num, assert_type="equal"):
        """
        Description: Will verify the heading text in Runmode
        :Usage - verify_heading_text(["COUNTRY], '03')
        """
        self._webelement.verify_elements_text(self._locators.Heading.title, expected_text, step_num, self._name + " text", assert_type=assert_type, parent_instance=self._parent_object())

    def verify_text_size(self, expected_size, step_num):
        """
        Description: Verify heading or footing text size in Runmode
        :Usage -  verify_text_size("14", "03")
        """
        text_size_obj = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.Heading.title, self._name + " size", parent_object=self._parent_object())
        text_size_value = text_size_obj[1].get_attribute('style')
        value = True if expected_size in text_size_value else False
        msg = "Step: {} Verify header text size".format(step_num)
        self._utils.asequal(True, value, msg)
    
    def verify_text_background_color(self, color_name, step_num):
        """
        Description: verify heading or footing background color in Runmode
        :Usage - verify_text_background_color('blue', '05')
        """
        text = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.Heading.title, self._name + " Background Color", parent_object=self._parent_object())
        actual_color = color.Color.from_string(self._utils.get_element_css_propery(text, "background-color")).rgb
        expected_color = self._utils.color_picker(color_name)
        msg = "Step {0} : Verify background color of text".format(step_num)
        self._utils.asequal(expected_color, actual_color, msg)
        
    def wait_for_text(self, text, timeout=60):
        """
        Description: Wait for text in header or footer in Runmode
        """
        self._webelement.wait_for_element_text(self._locators.Heading.RunMode.parent, text, timeout)
