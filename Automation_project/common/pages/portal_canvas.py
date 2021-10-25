from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from selenium.webdriver.support import expected_conditions as EC
from common.locators.portal_designer import Vfive_Designer
from common.lib.webfocus.designer_canvas import Designer_Canvas
from common.lib.webfocus.poptop_dialog import Share_With_Others
from selenium.webdriver.support.ui import WebDriverWait
from common.lib.global_variables import Global_variables
import time
from selenium.webdriver.support.color import Color
from common.lib.webfocus import resource_dialog
    
    
class Portal_canvas(BasePage):
    
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Portal_canvas, self).__init__(driver)
        self._utillobject = UtillityMethods(self.driver)
        self._coreutilobj = CoreUtillityMethods(self.driver)
        self._designer_canvas = Designer_Canvas(self.driver)
        self._share_with_others = Share_With_Others(self.driver)
        self._resource_dialog = resource_dialog.Resource_Dialog(self.driver)
    
    def verify_blank_canvas_text(self, msg, expected_text) :
        """
        Description : This method will verify page header title
        """
        actual_text = self._designer_canvas.get_blank_canvas_text()
        self._utillobject.asequal(expected_text, actual_text, msg)
    
    def verify_page_header_title(self, expected_title, msg):
        """
        Description : This method will verify page header title
        """
        actual_title = self._designer_canvas.get_page_header_title()
        self._utillobject.asequal(expected_title, actual_title, msg)
        
    def verify_page_header_buttons(self, expected_buttons_name_list, msg, assert_type='asequal'):
        """
        Description : This method will all or specific visible buttons on page header
        example usage : verify_page_header_buttons(['Share', 'Refresh', 'Delete'], 'Step 01 : Verify page header button', assert_type='asequal')
        """
        actual_buttons = self._designer_canvas.get_page_header_visible_buttons()
        self._utillobject.verify_list_values(expected_buttons_name_list, actual_buttons, msg, assert_type)
    
    def verify_page_heading_button_tooltip(self, button_name, msg) :
        """
        Description : This method will mouse move on page header button and verify tooltip using uiautomation
        example usage : verify_page_heading_button_tooltip('Share', 'Step 01.1 : Verify Share button tooltip')
        """
        page_heading_button = self._designer_canvas.get_page_header_button_obj(button_name)
        self.verify_canvas_button_tooltip(page_heading_button, button_name, msg)
    
    def verify_page_header_button_color(self, button_name, expected_color, msg) :
        """
        Description : This method will verify page header button color 
        example usage : verify_page_heading_button_color('Share', 'blue', 'Step 01.1 : Verify Share button color')
        """
        page_heading_button = self._designer_canvas.get_page_header_button_obj(button_name)
        self._utillobject.verify_element_color_using_css_property(None, expected_color, msg, 'color', element_obj=page_heading_button)
    
    def click_on_page_header_button(self, button_name) :
        """
        Description : This method will click on page header button
        example usage : click_on_page_header_button('Share')
        """
        page_heading_button = self._designer_canvas.get_page_header_button_obj(button_name)
        self._coreutilobj.left_click(page_heading_button)
    
    def verify_containers_title(self, expected_containers_title, msg, assert_type='asequal') :
        """
        Description : This method will verify all or specific containers title in canvas
        example usage : verify_containers_title(['Panel 1', 'Panel 2', 'Panel 3'], 'Step 01 : Verify 3 containers displayed in canvas')
        example usage : verify_containers_title(['Panel 1', 'Panel 2'], 'Step 01 : Verify Panel 1 and Panel 2 containers displayed in canvas', assert_type='asin')
        """
        actual_containers_title = self._designer_canvas.get_containers_title()
        self._utillobject.verify_list_values(expected_containers_title, actual_containers_title, msg, assert_type)
    
    def click_on_containers_title_bar_button(self, container_title, button_name, container_title_index=1) :
        """
        Description : This method will click on page header button
        example usage : click_on_page_header_button('Share')
        """
        button_obj = self._designer_canvas.get_container_title_bar_button_obj(container_title, button_name, container_title_index)
        self._coreutilobj.left_click(button_obj)
    
    def verify_container_title_bar_buttons(self, container_title, expected_buttons_name_list, msg, container_title_index=1, assert_type='asequal'):
        """
        Description : This method will all or specific container title bar buttons
        example usage : verify_container_title_bar_options('Panel 1', ['Maximize', 'Options'], 'Step 01.1 : Verify ['Maximize', 'Options'] buttons are visible in Panel 1 container')
        """
        actual_buttons = self._designer_canvas.get_container_title_bar_visible_buttons(container_title, container_title_index)
        self._utillobject.verify_list_values(expected_buttons_name_list, actual_buttons, msg, assert_type)
    
    def verify_container_title_bar_button_tooltip(self, container_title, button_name, msg, container_title_index=1) :
        """
        Description : This method will mouse move on container title bar button and verify tooltip using uiautomation
        example usage : verify_container_title_bar_button_tooltip('Panel 1', 'Maximize', 'Step 01.1 : Verify Maximize button tooltip')
        """
        page_heading_button = self._designer_canvas.get_container_title_bar_button_obj(container_title, button_name, container_title_index)
        self.verify_canvas_button_tooltip(page_heading_button, button_name, msg)
    
    def verify_container_title_bar_button_color(self, container_title, button_name, expected_color, msg, container_title_index=1):
        """
        Description : This method will verify container title button color 
        example usage : verify_container_title_bar_button_color(''Panel 1', 'Maximize', 'blue', 'Step 01.1 : Verify Maximize button color')
        """
        container_title_bar_button = self._designer_canvas.get_container_title_bar_button_obj(container_title, button_name, container_title_index)
        self._utillobject.verify_element_color_using_css_property(None, expected_color, msg, 'color', element_obj=container_title_bar_button)
    
    def click_on_add_content_button_in_container(self, container_object, container_type):
        """
        Description : This method will click on add content button on panel container in canvas 
        example usage : click_on_add_content_button_in_panel_container(container_object)
        """
        add_content_button_obj = self._designer_canvas.get_panel_add_container_object(container_object, container_type)
        self._coreutilobj.left_click(add_content_button_obj)
    
    def verify_tab_panel(self, container_object, msg, tab_name_list=None, selected_tab=None, comparison_type=None):
        """
        Description : This method will verify number of tabs in panel 
        """
        tab_css = ".ibx-tab-button[data-ibx-type*='Button'] .ibx-label-text"
        selected_tab_css = ".ibx-tab-button[data-ibx-type*='Button'].checked .ibx-label-text"
        panel_object = self._designer_canvas.get_panel_type(container_object, 'tab')
        if tab_name_list:
            tab_objectes = self._utillobject.validate_and_get_webdriver_objects(tab_css, 'Tab list', parent_object=panel_object)
            tab_names_list = [tab_name.text.strip() for tab_name in tab_objectes]
            if comparison_type == 'asin':
                for page_name in tab_name_list:
                    if page_name in tab_names_list:
                        status = True
                    else:
                        status = page_name
                        break
                self._utillobject.asequal(True, status, msg)
            if comparison_type == 'asequal':
                self._utillobject.as_List_equal(tab_name_list, tab_names_list, msg)
            if comparison_type == 'asnotin':
                for page_name in tab_name_list:
                    if page_name not in tab_names_list:
                        status = True
                    else:
                        status = page_name
                        break
                self._utillobject.asequal(True, status, msg)
        if selected_tab:
            selected_tab_text = self._utillobject.validate_and_get_webdriver_object(selected_tab_css, 'Selected Tab', parent_object=panel_object).text.strip()
            self._utillobject.asequal(selected_tab, selected_tab_text, msg)
    
    def get_panel_container(self, panel_name, panel_index):
        """
        Description : This method will return in panel container object
        """
        container_obj = self._designer_canvas.get_container_parent_object(panel_name, container_title_index=panel_index)
        return container_obj
    
    def verify_carousel_panel(self, container_object, msg, number_of_slide=None, slide_title_list=None, selected_slide=None, comparison_type=None):
        """
        Description : This method will verify number of carousel in panel 
        """
        slide_css = ".ibx-csl-page-marker"
        slide_selected_css = "ibx-csl-page-selected"
        panel_object = self._designer_canvas.get_panel_type(container_object, 'carousel')
        if number_of_slide:
            number_of_slides = len(self._utillobject.validate_and_get_webdriver_objects(slide_css, 'Number of Slides', parent_object=panel_object))
            self._utillobject.asequal(number_of_slide, number_of_slides, msg)
        if slide_title_list:
            slides_object = self._utillobject.validate_and_get_webdriver_objects(slide_css, 'Number of Slides', parent_object=panel_object)
            slides_title_list = [self._utillobject.get_element_attribute(tab_name, 'title') for tab_name in slides_object]
            if comparison_type == 'asin':
                for page_name in slide_title_list:
                    if page_name in slides_title_list:
                        status = True
                    else:
                        status = page_name
                        break
                self._utillobject.asequal(True, status, msg)
            if comparison_type == 'asequal':
                self._utillobject.as_List_equal(slide_title_list, slides_title_list, msg)
            if comparison_type == 'asnotin':
                for page_name in slide_title_list:
                    if page_name not in slides_title_list:
                        status = True
                    else:
                        status = page_name
                        break
                self._utillobject.asequal(True, status, msg)
        if selected_slide:
            selected_object = self._utillobject.validate_and_get_webdriver_object('{0}{1}'.format(slide_css, slide_selected_css), 'Selected Tab', parent_object=panel_object)
            selcted_slide_title_text = self._utillobject.get_element_attribute(selected_object, 'title')
            self._utillobject.asequal(selected_slide, selcted_slide_title_text, msg)
    
    def verify_add_content_button_displayed_in_container(self, container_object, container_type, msg):
        """
        Description : This method will verify whether add content button is displayed in panel container in canvas 
        example usage : verify_add_content_button_displayed_in_container(container_object)
        """
        add_content_button_obj = self._designer_canvas.get_panel_add_container_object(container_object, container_type)
        visible_status = self._designer_canvas.get_add_content_button_icon_visible_status(add_content_button_obj)
        self._utillobject.asequal(True, visible_status, msg)
    
    def verify_add_content_button_color_in_container(self, container_object, container_type, expected_color, msg):
        """
        Description : This method will verify content button color in container 
        example usage : verify_add_content_button_color_in_container(container_object)
        """
        add_content_button_obj = self._designer_canvas.get_panel_add_container_object(container_object, container_type)
        self._utillobject.verify_element_color_using_css_property(None, expected_color, msg, 'color', element_obj=add_content_button_obj)
    
    def mouse_move_on_add_content_button_and_verify_color_in_container(self, container_object, container_type, expected_color, msg):
        """
        Description : This method will mouse move on add content button and verify color on container in canvas 
        example usage : mouse_move_on_add_content_button_and_verify_color_in_container(container_object, 'blue', 'Step 01.1 : Verify add content color after mouse move on it')
        """
        add_content_button_obj = self._designer_canvas.get_panel_add_container_object(container_object, container_type)
        self._coreutilobj.python_move_to_element(add_content_button_obj)
        time.sleep(3)
        add_content_button_obj = self._designer_canvas.get_add_content_button_obj(container_object)
        self._utillobject.verify_element_color_using_css_property(None, expected_color, msg, 'color', element_obj=add_content_button_obj)
        
    def verify_add_content_button_tooltip_in_container(self, container_object, container_type, expected_tooltip, msg):
        """
        Description : This method will verify add content button tooltip in container
        example usage : verify_add_content_button_tooltip_in_container(container_object, 'Add Content', 'Step 01.1 : Verify Add Content tooltip display')
        """
        add_content_button_obj = self._designer_canvas.get_panel_add_container_object(container_object, container_type)
        self.verify_canvas_button_tooltip(add_content_button_obj, expected_tooltip, msg)
    
    def click_on_panel_add_content_button_in_container(self, panel_name, container_type, panel_index=1):
        """
        Description : This method will click on add content button on panel container in canvas 
        example usage : click_on_panel_add_content_button_in_container('Panel 1')
        """
        container_obj = self._designer_canvas.get_container_parent_object(panel_name, container_title_index=panel_index)
        self.click_on_add_content_button_in_container(container_obj, container_type)
        self._utillobject.synchronize_with_number_of_element(self._resource_dialog.resource_dialog_css, 1, self.home_page_medium_timesleep)
    
    def select_repository_file_using_add_content_in_panel_container(self, file_path, crumb_box_option=None, select_button='Select'):
        '''
        Description : This function will select file from resource dialog.
        @param panel_name: 'Panel 1'
        @param file_path: 'P292_S19901->G513445->test'
        @param panel_index = Position of Panel. Some times two or more containers have same title that time we can pass panel_index. panel_index start form 1
        :Usage select_repository_file_using_add_content_in_panel_container('Panel 1', 'P292_S19901->G513445->test')
        '''
        if crumb_box_option:
            resource_dialog.OpenDialog.select_crumb_item(self, crumb_box_option)
        item_path = file_path.split('->')
        for resource_name in item_path:
            if resource_name is item_path[-1]:
                resource_dialog.OpenDialog.select_resource_from_gridview(self, resource_name)
            else:
                resource_dialog.OpenDialog.select_resource_from_gridview(self, resource_name, selection_type='double')
        select_button_element = resource_dialog.OpenDialog.get_button_object(self, select_button)
        self._coreutilobj.left_click(select_button_element)
    
    def verify_add_content_in_container(self, panel_name, container_type, msg, panel_index=1, expected_color=None, mouse_move_expected_color=None, expected_tooltip=None):
        """
        Description : This method will verify whether add content button is displayed in panel container in canvas 
        example usage : verify_panel_add_content_displayed_in_container('Panel 1', 'Step 9: Verify')
        """
        container_obj = self._designer_canvas.get_container_parent_object(panel_name, container_title_index=panel_index)
        self.verify_add_content_button_displayed_in_container(container_obj, container_type, msg)
        if expected_color:
            self.verify_add_content_button_color_in_container(container_obj, container_type, expected_color, msg)
        if mouse_move_expected_color:
            self.mouse_move_on_add_content_button_and_verify_color_in_container(container_obj, container_type, mouse_move_expected_color, msg)
        if mouse_move_expected_color:
            self.verify_add_content_button_tooltip_in_container(container_obj, container_type, expected_tooltip, msg)
    
    def verify_canvas_button_tooltip(self, button_obj, tooltip_value, msg):
        """
        Description : This method will verify any page canvas button tooltip using uiautomation
        @param : tooltip_value = title attribute value of element (Example element dom css = <div title="Delete" class="pd-header-button>)
        @param : button_obj - button object. This object should has title attribute in DOM
        """
#         self._coreutilobj.python_move_to_element(button_obj, element_location='bottom_middle')
#         time.sleep(1)
#         self._coreutilobj.python_move_to_element(button_obj)
#         time.sleep(2)
#         try :
#             uiautomation.ToolTipControl(Name = tooltip_value).Name
#             tooltip_status = True
#         except LookupError :
#             tooltip_status = False
#         self._utillobject.asequal(True, tooltip_status, msg)
        actual_title_value = self._utillobject.get_element_attribute(button_obj, 'title')
        self._utillobject.asequal(tooltip_value, actual_title_value, msg)
        
    def switch_to_container_frame(self, parent_obj, frame_css="div[data-ibx-type='pdIFrame']>iframe", timeout=120):
        """
        Description : This method will switch to ant container iframe
        :@param - parent_obj - container object. There are difference type of containers in canvas.  parent_obj should has iframe
        """
        frame_element_obj = self._utillobject.validate_and_get_webdriver_object(frame_css, 'Canvas container frame', parent_object=parent_obj)
        frame_actual_location = self._coreutilobj.get_web_element_coordinate(frame_element_obj, element_location='top_left')
        WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(frame_element_obj))
        time.sleep(Global_variables.mediumwait)
        Global_variables.current_working_area_browser_x=frame_actual_location['x']
        Global_variables.current_working_area_browser_y=frame_actual_location['y']
        time.sleep(Global_variables.shortwait)
    
    def click_on_dialog_button(self, button_name):
        """
        Description : This method will click on dialog button 
        @arg : button_name = name of button
        """
        button_object = self._designer_canvas.get_dialog_button_object(button_name)
        self._coreutilobj.left_click(button_object)
    
    def verify_dialog_title(self, expected_title, msg):
        """
        Description : This method will verify the title of dialog 
        """ 
        title_object = self._utillobject.validate_and_get_webdriver_object(Vfive_Designer.dialog_title_css, 'Dialog title')
        actual_title = title_object.text.strip()
        self._utillobject.asequal(expected_title, actual_title, msg)
    
    def verify_dialog_msg(self, expected_msg, msg):
        """
        Description : This method will verify the message of dialog 
        """ 
        msg_object = self._utillobject.validate_and_get_webdriver_object(Vfive_Designer.dialog_msg_css, 'Dialog Message')
        actual_msg = msg_object.text.strip()
        self._utillobject.asequal(expected_msg, actual_msg, msg)
        
    def verify_share_with_others_dialog_open_close(self, dialog_mode, msg):
        '''
        This function will verify share with others dialog open close
        @param dialog_mode: 'open'
        @param msg: 'Step 9: Verify'
        :Usage  verify_advanced_folder_search_dialog_open_or_close('open', 'Step 9: Verify')
        '''
        share_with_others_dialog_css = ".share-with-others-dialog.pop-top .ibx-dialog-main-box"
        if dialog_mode.lower() not in ['open', 'close']:
                raise IndexError("Please pass dialog_mode as 'open' or 'close'.")
        current_mode = True if dialog_mode == 'open' else False
        self._utillobject.verify_object_visible(share_with_others_dialog_css, current_mode, msg)
    
    def search_input_in_share_with_others_dialog(self, edit_value=None, verify_value=None, verify_placeholder=None, search_icon=None, verify_drop_down_button=None, msg=None):
        '''
        This function will edit, verify Search input in share with others dialog
        @param edit_value: 'autodevuser19'
        @param verify_value: 'autodevuser19'
        @param verify_placeholder: 'Enter users and groups'
        @param search_icon: 'display' or 'not display'
        @param verify_drop_down_button: 'display' or 'not display'
        @param msg: 'Step 9: Verify'
        :Usage search_input_in_share_with_others_dialog(self, edit_value='autodevuser19', verify_value='autodevuser19', verify_placeholder='Enter users and groups', search_icon='display', verify_drop_down_button='display', msg='Step 9: Verify')
        '''
        searchbox_element = self._share_with_others.get_searchbox_element()
        text_box_element = self._share_with_others.get_searchbox_input_element()
        if edit_value != None:
            self._utillobject.set_text_to_textbox_using_keybord(edit_value, text_box_elem=text_box_element)
            self._utillobject.synchronize_with_visble_text(None, edit_value, self.home_page_medium_timesleep, text_option='text_value', parent_elem=text_box_element)
        if verify_value != None:
            actual_value = self._utillobject.get_element_attribute(text_box_element, 'value')
            self._utillobject.asequal(verify_value, actual_value, msg)
        if verify_placeholder != None:
            actual_value = self._utillobject.get_element_attribute(text_box_element, 'placeholder')
            self._utillobject.asequal(verify_placeholder, actual_value, msg)
        if search_icon != None:
            if search_icon.lower() not in ['display', 'not display']:
                raise AttributeError("Please pass value as 'display', 'not display'")
            search_icon_element = self._utillobject.validate_and_get_webdriver_object(".share-with-btn-search .ibx-label-icon", 'Search icon in share with others dialog', parent_object=searchbox_element)
            element_class_attribute = self._utillobject.get_element_attribute(search_icon_element, 'class')
            actual_status = 'display' if 'material-icons' in element_class_attribute and search_icon_element.text.strip() == 'search' and search_icon_element.is_displayed() else 'not display'
            self._utillobject.asequal(search_icon, actual_status, msg)
        if verify_drop_down_button != None:
            if verify_drop_down_button.lower() not in ['display', 'not display']:
                raise AttributeError("Please pass value as 'display', 'not display'")
            search_drop_down_element = self._utillobject.validate_and_get_webdriver_object(".Share-with-menu-btn .ibx-label-icon:not([style*='none'])", 'Search drop down in share with others dialog', parent_object=searchbox_element)
            element_class_attribute = self._utillobject.get_element_attribute(search_drop_down_element, 'class')
            actual_status = 'display' if 'ds-icon-caret-down' in element_class_attribute and search_drop_down_element.is_displayed() else 'not display'
            self._utillobject.asequal(verify_drop_down_button, actual_status, msg)
    
    def verify_caption_title_in_share_with_others_dialog(self, title_name, msg):
        '''
        This function will verify caption title.
        @param title_name: 'Share with Others'
        @param msg: 'Step 9: Verify'
        :Usage verify_caption_title_in_share_with_others_dialog(self, 'Share with Others', 'Step 9: Verify')
        '''
        search_input_element = self._share_with_others.get_element_in_dialog(title_name, '.ibx-label-text', title_name).text.strip()
        self._utillobject.asequal(title_name, search_input_element, msg)
    
    def button_in_share_with_others_dialog(self, button_name, select=None, color_name=None, label_text=None, current_mode=None, msg=None, color_rgba_alpha_value='1'):
        '''
        This function will select, verify button inside share with others dialog.
        @param button_name: 'Reset'
        @param select: True
        @param color_name: 'blue'
        @param location: True
        @param msg: 'Step 9: Verify'
        :Usage button_in_share_with_others_dialog('Reset', , select=True, color_name='blue', location=True, msg='Step 9: Verify')
        '''
        button_css = "[class*='close-button']"  if button_name.lower() == 'close' else "[class*='{0}-button']".format(button_name.lower())
        button_name_label = "Share with Others"  if button_name.lower() == 'close' else button_name
        button_element = self._share_with_others.get_element_in_dialog(self, button_name_label, button_css, button_name_label)
        if select == True:
            self._coreutilobj.left_click(self, button_element)
        if color_name:
            expected_color_name = self._utillobject.color_picker(self, color_name, rgb_type='rgba').replace('1)','{0})'.format(str(color_rgba_alpha_value)))
            actual_color_name = Color.from_string(self._utillobject.get_element_css_propery(self, button_element, 'background-color')).rgba
            self._utillobject.asequal(expected_color_name, actual_color_name, msg)
        if label_text != None:
            actual_text = button_element.text.strip()
            self._utillobject.asequal(label_text, actual_text, msg)
        if current_mode != None:
            if current_mode not in ['enable', 'disable']:
                raise IndexError("Please pass value as 'enable', 'disable'.")
            element_class_attribute = self._utillobject.get_element_attribute(button_element, 'class')
            actual_value = 'disable' if "ibx-widget-disabled" in element_class_attribute else 'enable'
            self._utillobject.asequal(self, current_mode, actual_value, msg)
    
    def click_show_filters(self):
        """
        Descriptions : This method used to click on show filters button
        """
        show_filters_obj = self._utillobject.validate_and_get_webdriver_object(".pg-runner:not([style*='none']) div[title='Show filters'][class*='pd-header-button-filter']", 'show filters button')
        self._coreutilobj.left_click(show_filters_obj)