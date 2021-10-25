import time
import pyautogui
from common.locators import portal_designer
from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods as utill_obj
from common.lib.core_utility import CoreUtillityMethods as core_utill_obj
from common.pages.wf_mainpage import Wf_Mainpage as home_page
from common.lib.webfocus import poptop_dialog
from common.lib.webfocus import resource_dialog
from common.lib.javascript import JavaScript as j_script
from selenium.webdriver.support.color import Color

class Portal_Designer(BasePage):
    
    """ Inherit attributes of the parent class = Baseclass """
    
    def __init__(self, driver):
        super(Portal_Designer, self).__init__(driver)
    
    def create_or_edit_portal(self, label_name, property_type, property_value, navigation_type='Two-level-side', expire_time=90):
        '''
        This function will verify portal dialog window.
        @param label_name: 'Title'
        @param property_type: 'text_box'
        @param property_value: 'V5 portal'
        @param msg: 'Step 9: Verify'
        @param navigation_type: 'Two-level-side'
        @param expire_time: 90
        :Usage create_or_edit_portal('Title', 'text_box', 'V5 portal', 'Step 9: Verify', navigation_type='Two-level-side', expire_time=90)
        '''
        if navigation_type not in ['Two-level-side', 'Three-level', 'Two-level-top']:
            raise IndexError("Please pass navigation_type as 'two-level-side', 'three-level' or two-level-top'.")
        if label_name.lower() == 'create':
            row_element = utill_obj.validate_and_get_webdriver_object(self, ".pop-top [class*='ok-button']", label_name)
        else:
            button_name = 'ok'  if label_name.lower() == 'save' else label_name
            property_type_dict = {'text_box': '.pvd-{0}'.format(label_name.lower()), 'label_text':'.ibx-label-text',
                                  'toggle_button':'.portal-show-banner', 'radio_button':'.navigation-{0}'.format(navigation_type.lower()), 
                                  'drop_down':'.hp-select-picker .ibx-select-open-btn', 'checkbox':"[role='checkbox'] .ibx-check-box-simple-marker", 
                                  'button': "[class*='{0}-button']".format(button_name.lower()), 'max_width_textbox': '.pvd-max-width'}
            if property_type not in property_type_dict.keys():
                raise IndexError("Please pass property_type value from {0} list values.".format(list(property_type_dict.keys())))
            property_element_css = property_type_dict[property_type]
            row_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, label_name, property_element_css, label_name)
        if property_type in ['text_box', 'max_width_textbox']:
            text_box_element = utill_obj.validate_and_get_webdriver_object(self, 'input', label_name, parent_object=row_element)
            utill_obj.set_text_to_textbox_using_keybord(self, property_value, text_box_elem=text_box_element)
            if label_name!='Alias':
                utill_obj.synchronize_with_visble_text_within_parent_object(self, row_element, 'input', property_value, expire_time, text_option='text_value')
        elif property_type in ['toggle_button', 'radio_button', 'checkbox']:
            if property_value.lower() not in ['check', 'uncheck']:
                raise IndexError("Please pass property_value as 'check' or 'uncheck'")
            element_class_attribute = utill_obj.get_element_attribute(self, row_element, 'class')
            if property_type == 'checkbox':
                status_value = 'check' if 'ibx-check-box-simple-marker-check' in element_class_attribute else 'uncheck'
            else:
                status_value = 'check' if 'checked' in element_class_attribute else 'uncheck'
            if property_value == status_value:
                raise LookupError("'{0}' {1} already {2}.".format(label_name, property_type, property_value))
            core_utill_obj.left_click(self, row_element)
        elif property_type == 'drop_down':
            core_utill_obj.left_click(self, row_element)
            poptop_dialog.Poptop_Dialog.row_css=".ibx-select-item"
            popup_row_element = poptop_dialog.Select_Popup.get_element_in_dialog(self, property_value, '.ibx-label-text', property_value)
            poptop_dialog.Poptop_Dialog.row_css="> .ibx-dialog-main-box .ibx-flexbox-horizontal"
            core_utill_obj.left_click(self, popup_row_element)
        elif property_type == 'button':
            core_utill_obj.left_click(self, row_element)
        elif property_type in ['label_text']:
            core_utill_obj.left_click(self, row_element)
        
    
    def verify_portal_dialog(self, label_name, property_type, property_value, msg, navigation_type='Two-level-side', placeholder=None):
        '''
        This function will verify portal inside create/edit portal.
        Note: if lable name is 'URL' means url text box verification then only pass alias url path example('portal/P292_S19901/G513445/Portal_for_Context_Menu_Testing')
        @param label_name: 'Title'
        @param property_type: 'text_box'
        @param property_value: 'V5 portal'
        @param msg: 'Step 9: Verify'
        @param navigation_type: 'Two-level-side'
        @param placeholder: 'Not selected'
        :Usage verify_portal_dialog('Title', 'text_box', 'V5 portal', 'Step 9: Verify', navigation_type='Two-level-side', placeholder='Not selected')
        '''
        if navigation_type not in ['Two-level-side', 'Three-level', 'Two-level-top']:
            raise IndexError("Please pass navigation_type as 'two-level-side', 'three-level' or two-level-top'.")
        if label_name.lower() in ['create', 'save']:
            row_element = utill_obj.validate_and_get_webdriver_object(self, ".pop-top [class*='ok-button']", label_name)
        else:
            button_name = 'ok'  if label_name.lower() == 'save' else label_name
            property_type_dict = {'text_box': '.pvd-{0} input'.format(label_name.lower()), 
                                  'label_text':'.ibx-label-text', 'toggle_button':'.portal-show-banner',
                                  'radio_button':'.navigation-{0}'.format(navigation_type.lower()), 'drop_down':'.hp-select-picker input',
                                  'checkbox':"[role='checkbox'] .ibx-check-box-simple-marker", 'checkbox_label':"[role='checkbox'] .ibx-label-text", 
                                  'button': "[class*='{0}-button']".format(button_name.lower()), 'max_width_textbox': '.pvd-max-width input' }
            if property_type not in property_type_dict.keys():
                raise IndexError("Please pass property_type value from {0} list values.".format(list(property_type_dict.keys())))
            property_element_css = property_type_dict[property_type]
            row_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, label_name, property_element_css, label_name)
        if property_type in ['text_box', 'max_width_textbox']:
            if label_name.lower() == 'url':
                property_value = '{0}{1}'.format(str(utill_obj.get_setup_url(self)), str(property_value)).replace('home8206', '')
            if placeholder:
                actual_value = utill_obj.get_element_attribute(self, row_element, 'placeholder')
                utill_obj.asequal(self, placeholder, actual_value, msg)
            else:
                actual_value = utill_obj.get_element_attribute(self, row_element, 'value')
                utill_obj.asequal(self, property_value, actual_value, msg)
        elif property_type in ['label_text', 'checkbox_label']:
            actual_value = row_element.text.strip()
            utill_obj.asequal(self, property_value, actual_value, msg)
        elif property_type == 'toggle_button':
            if property_value.lower() not in ['check', 'uncheck']:
                raise IndexError("Please pass property_value as 'check' or 'uncheck'")
            element_class_attribute = utill_obj.get_element_attribute(self, row_element, 'class')
            actual_value = 'check' if 'checked' in element_class_attribute else 'uncheck'
            utill_obj.asequal(self, property_value, actual_value, msg)
        elif property_type == 'radio_button':
            if property_value.lower() not in ['check', 'uncheck']:
                raise IndexError("Please pass property_value as 'check' or 'uncheck'")
            element_class_attribute = utill_obj.get_element_attribute(self, row_element, 'class')
            actual_value = 'check' if 'checked' in element_class_attribute else 'uncheck'
            utill_obj.asequal(self, property_value, actual_value, msg)
        elif property_type == 'drop_down':
            actual_value = utill_obj.get_element_attribute(self, row_element, 'value')
            utill_obj.asequal(self, property_value, actual_value, msg)
        elif property_type == 'checkbox':
            if property_value.lower() not in ['check', 'uncheck']:
                raise IndexError("Please pass property_value as 'check' or 'uncheck'")
            element_class_attribute = utill_obj.get_element_attribute(self, row_element, 'class')
            actual_value = 'check' if 'ibx-check-box-simple-marker-check' in element_class_attribute else 'uncheck'
            utill_obj.asequal(self, property_value, actual_value, msg)
        elif property_type == 'button':
            actual_value = row_element.text.strip()
            utill_obj.asequal(self, property_value, actual_value, msg)
    
    def verify_portal_dialog_content_enable_disable(self, label_name, property_type, property_value, msg, navigation_type='Two-level-side', text_box_readonly=None):    
        '''
        This function will verify portal dialog window content enable or disable.
        @param label_name: 'Title'
        @param property_type: 'text_box'
        @param property_value: 'enable' or 'disable'
        @param msg: 'Step 9: Verify'
        @param navigation_type: 'Two-level-side'
        @param text_box_readonly: True
        :Usage verify_portal_dialog_content_enable_disable('Title', 'text_box', 'V5 portal', 'Step 9: Verify', navigation_type='Two-level-side', text_box_readonly=True) 
        '''
        disable_css = "ibx-widget-disabled"
        if navigation_type not in ['Two-level-side', 'Three-level', 'Two-level-top']:
            raise IndexError("Please pass navigation_type as 'two-level-side', 'three-level' or two-level-top'.")
        if label_name.lower() == 'create':
            row_element = utill_obj.validate_and_get_webdriver_object(self, ".pop-top [class*='ok-button']", label_name)
        elif label_name.lower() == 'close':
            row_element = utill_obj.validate_and_get_webdriver_object(self, ".pop-top [class*='close-button']", label_name)
        else:
            button_name = 'ok'  if label_name.lower() == 'save' else label_name
            if property_value not in ['enable', 'disable']:
                raise IndexError("Please pass property_value as 'enable', 'disable'.")
            property_type_dict = {'text_box': '.pvd-{0}'.format(label_name.lower()), 
                                  'label_text':'.ibx-label', 'toggle_button':'.portal-show-banner',
                                  'radio_button':'.navigation-{0}'.format(navigation_type.lower()), 'drop_down':'.hp-select-picker',
                                  'checkbox':"[role='checkbox']", 'button': "[class*='{0}-button']".format(button_name.lower()),'max_width_textbox': '.pvd-max-width'}
            if property_type not in property_type_dict.keys():
                raise IndexError("Please pass property_type value from {0} list values.".format(list(property_type_dict.keys())))
            property_element_css = property_type_dict[property_type]
            row_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, label_name, property_element_css, label_name)
        if text_box_readonly != None:
            utill_obj.verify_object_visible(self, 'input[readonly]', text_box_readonly, msg, elem_obj=row_element)
        else:  
            element_class_attribute = utill_obj.get_element_attribute(self, row_element, 'class')
            actual_value = 'disable' if disable_css in element_class_attribute else 'enable'
            utill_obj.asequal(self, property_value, actual_value, msg)
    
    def verify_browse_button_position_in_edit_or_create_portal(self, msg, position='right'):
        '''
        This function will verify 'Browse' button position under edit or create portal.
        @param msg: 'Step 9: verify'
        @param position: 'right'
        :Usage verify_browse_button_position_in_edit_or_create_portal('Step 9: verify', position='right')
        '''
        label_name, logo_text_box_css, logo_browse_button_css = 'Logo', '.pvd-logo', "[class*='browse-button']"
        logo_text_box_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, label_name, logo_text_box_css, label_name)
        logo_browse_button_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, label_name, logo_browse_button_css, label_name)
        if position.lower() == 'right':
            logo_text_box_element_middle_right_coordinate = core_utill_obj.get_web_element_coordinate(self, logo_text_box_element, 'middle_right')
            logo_browse_button_element_middle_left_coordinate = core_utill_obj.get_web_element_coordinate(self, logo_browse_button_element, 'middle_left')
            if int(logo_text_box_element_middle_right_coordinate['x']) < int(logo_browse_button_element_middle_left_coordinate['x']):
                if int(logo_text_box_element_middle_right_coordinate['y']) == int(logo_browse_button_element_middle_left_coordinate['y']):
                    expected,actual=True,True
                else:
                    expected,actual=int(logo_text_box_element_middle_right_coordinate['y']), int(logo_browse_button_element_middle_left_coordinate['y'])
            else:
                expected,actual=int(logo_text_box_element_middle_right_coordinate['x']), int(logo_browse_button_element_middle_left_coordinate['y'])
            utill_obj.asequal(self, expected, actual, msg)
            
    def close_portal_dialog(self, button_name):
        '''
        This function will close portal dialog.
        @param button_name: 'Create'
        :Usage  close_portal_dialog('close')
        '''
        if button_name.lower() in ['create']:
            current_button_name_element = utill_obj.validate_and_get_webdriver_object(self, ".pop-top [class*='ok-button']", button_name)
        else:    
            current_button_name_css = "[class*='ok-button']" if button_name.lower() in ['save'] else "[class*='{0}-button']".format(button_name.lower())
            button_label_name = 'Portal' if button_name.lower() == 'close' else button_name
            current_button_name_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, button_label_name, current_button_name_css, button_label_name)
        core_utill_obj.left_click(self, current_button_name_element)
    
    def verify_portal_dialog_open_or_close(self, dialog_mode, msg):
        '''
        This function will verify portal dialog is open or close.
        @param dialog_mode: 'open'
        @param msg: 'Step 9: Verify'
        :Usage  verify_portal_dialog_open_or_close('open', 'Step 9: Verify')
        '''
        portal_dialog_css = '.ibx-dialog-main-box'
        if dialog_mode.lower() not in ['open', 'close']:
                raise IndexError("Please pass dialog_mode as 'open' or 'close'.")
        current_mode = True if dialog_mode == 'open' else False
        poptop_dialog.New_Portal_Dialog.verify_poptop_dialog_is_visible(self, portal_dialog_css, current_mode, msg)
    
    def verify_alert_message_in_portal_dialog(self, warning_msg, step_number, verify_color_name=None):
        '''
        This function will verify alert/warning message inside create/edit portal dialog.
        @param warning_msg: 'Portal already exists'
        @param step_number: '9'
        @param verify_color_name: 'persian_red4'
        :Usage  verify_alert_message_in_portal_dialog('Portal already exists', '9', verify_color_name='persian_red4')
        '''
        alert_message_css = ".pop-top .form-fill-error-text"
        expected_alert_icon_value='\uf06a'
        disp_warning_msg = "Step {0}.a: Verify warning/alert message as '{1}'.".format(str(step_number), warning_msg)
        disp_icon_msg = "Step {0}.b: Verify warning/alert icon.".format(str(step_number))
        disp_color_msg = "Step {0}.c: Verify warning/alert color.".format(str(step_number))
        alert_message_element = utill_obj.validate_and_get_webdriver_object(self, alert_message_css, warning_msg)
        utill_obj.asequal(self, warning_msg, alert_message_element.text.strip(), disp_warning_msg)
        actual_alert_icon_value = j_script.get_element_before_style_properties(self, alert_message_element, 'content').replace('"', '')
        utill_obj.asequal(self, expected_alert_icon_value.encode('utf-8'), actual_alert_icon_value.encode('utf-8'), disp_icon_msg)
        if verify_color_name:
            expected_color_name = utill_obj.color_picker(self, verify_color_name, rgb_type='rgba')
            actual_color_name = Color.from_string(utill_obj.get_element_css_propery(self, alert_message_element, 'background-color')).rgba
            utill_obj.asequal(self, expected_color_name, actual_color_name, disp_color_msg)
    
    def verify_title_in_portal_dialog(self, element_name, title_value, msg):
        '''
        This function will verify title inside create/edit portal.
        @param element_name:'two-level-side', 'three-level', 'two-level-top' or 'close'
        @param title_value: 'Two-level side', 'Three-level', 'Two-level top' or 'Close'
        @param msg: 'Step 9: Verify'
        :Usage verify_title_in_portal_dialog(self, 'two-level-side', 'Two-level side', 'Step 9: Verify')
        '''
        if element_name.strip().replace(' ','-').lower() in ['two-level-side', 'three-level', 'two-level-top']:
            element_css = '.navigation-{0}'.format(element_name.strip().replace(' ','-').lower())
            label_name = 'Navigation'
            element_type = label_name
        elif element_name.strip().replace(' ','-').lower() in ['close']:
            element_css = "[class*='close-button']"
            label_name = 'Portal'
            element_type = 'Close button'
        row_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, label_name, element_css, element_type)
        title_text = utill_obj.get_element_attribute(self, row_element, 'title')
        utill_obj.asequal(self, title_value, title_text, msg)
    
    def verify_focus_in_portal_dialog(self, label_name, property_type, focus_status, msg):
        '''
        This function will verify current focus inside create/edit portal.
        @param label_name: 'Title'
        @param property_type: 'text_box'
        @param focused_status: True
        @param msg: 'Step 9: Verify'
        :Usage verify_portal_dialog('Title', 'text_box', True, 'Step 9: Verify', navigation_type='Two-level-side')
        '''
        time.sleep(9)
        focused_css= "ibx-sm-focused"
        if focus_status not in [True, False]:
                raise IndexError("Please pass focused_status as True or False")
        if label_name.lower() in ['create', 'save']:
            row_element = utill_obj.validate_and_get_webdriver_object(self, ".pop-top [class*='ok-button']", label_name)
        else:
            button_name = 'ok'  if label_name.lower() == 'save' else label_name
            property_type_dict = {'text_box': '.pvd-{0} input'.format(label_name.lower()), 
                                  'toggle_button':'.portal-show-banner',
                                  'checkbox':"[role='checkbox']", 'button': "[class*='{0}-button']".format(button_name.lower()), 'max_width_textbox': '.pvd-max-width input'}
            if property_type not in property_type_dict.keys():
                raise IndexError("Please pass property_type value from {0} list values.".format(list(property_type_dict.keys())))
            property_element_css = property_type_dict[property_type]
            row_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, label_name, property_element_css, label_name)
        element_class_attribute = utill_obj.get_element_attribute(self, row_element, 'class')
        actual_value = True if focused_css in element_class_attribute else False
        utill_obj.asequal(self, focus_status, actual_value, msg)
    
    def verify_button_color_in_portal_dialog(self, label_name, button_color_name, msg, color_rgba_alpha_value='1'):
        '''
        This function will verify button color inside create/edit portal.
        @param label_name: 'Save'
        @param button_color_name: 'blue'
        @param msg: 'Step 9: Verify'
        :Usage verify_portal_dialog('Save', 'blue', 'Step 9: Verify')
        '''
        if label_name.lower() == 'create':
            row_element = utill_obj.validate_and_get_webdriver_object(self, ".pop-top [class*='ok-button']", label_name)
        else:
            if label_name.lower() in ['save']:
                property_element_css = "[class*='ok-button']"
                element_type = label_name
            elif label_name.lower() in ['close']:
                property_element_css = "[class*='close-button']"
                label_name = 'Portal'
                element_type = 'Close button'
            else:
                property_element_css = "[class*='{0}-button']".format(label_name.lower())
                element_type = label_name
            row_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, label_name, property_element_css, element_type)
        expected_color_name = utill_obj.color_picker(self, button_color_name, rgb_type='rgba').replace('1)','{0})'.format(str(color_rgba_alpha_value)))
        actual_color_name = Color.from_string(utill_obj.get_element_css_propery(self, row_element, 'background-color')).rgba
        utill_obj.asequal(self, expected_color_name, actual_color_name, msg)
        
    def verify_theme_drop_down_options_list_in_portal_dialog(self, drop_down_option_list, msg):
        '''
        This function will verify drop down list inside create/edit portal.
        @param drop_down_option_list: ['Light']
        @param msg: 'Step 9: Verify'
        :Usage verify_portal_dialog(['Light'], 'Step 9: Verify')
        '''
        poptop_dialog.Poptop_Dialog.row_css="> .ibx-dialog-main-box .ibx-flexbox-horizontal"
        drop_down_css = '.hp-select-picker .ibx-select-open-btn'
        label_name = 'Theme'
        row_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, label_name, drop_down_css, label_name)
        core_utill_obj.left_click(self, row_element)
        poptop_dialog.Poptop_Dialog.row_css=".ibx-select-item"
        current_drop_down_option_list = []
        for option in drop_down_option_list:
            popup_row_element = poptop_dialog.Select_Popup.get_element_in_dialog(self, option, '.ibx-label-text', option)
            current_drop_down_option_list.append(popup_row_element.text.strip())
        poptop_dialog.Poptop_Dialog.row_css="> .ibx-dialog-main-box .ibx-flexbox-horizontal"
        core_utill_obj.python_move_to_element(self, row_element)
        current_mouse_postion = pyautogui.position()
        core_utill_obj.python_click_with_offset(self, int(current_mouse_postion[0])+19, int(current_mouse_postion[1]))
        utill_obj.as_List_equal(self, drop_down_option_list, current_drop_down_option_list, msg)
    
    def select_logo_in_portal_dialog(self, logo_name=None, verify_resource_dilaog=None, msg=None, button=None):
        '''
        This function will select logo image or verify resource dialog using browse button inside create/edit portal dialog.
        @param logo_name: 'cat.jpg'
        @param verify_resource_dilaog: True or False
        @param msg: 'Step 9: Verify.'
        @param button: 'Select' or 'Cancel'
        :Usage select_logo_in_portal_dialog(logo_name='cat.jpg', verify_resource_dilaog=True, msg='Step 9: Verify.', button='Select')
        '''
        Portal_Designer.create_or_edit_portal(self, 'Browse', 'button', None)
        utill_obj.synchronize_with_number_of_element(self, resource_dialog.OpenDialog.resource_dialog_css, 1, self.home_page_medium_timesleep)
        if verify_resource_dilaog:
            resource_dialog.OpenDialog.verify_resource_dialog_is_visible(self, verify_resource_dilaog, msg)
        if logo_name:
            resource_dialog.OpenDialog.select_resource_from_gridview(self, logo_name)
        select_button_element = resource_dialog.OpenDialog.get_button_object(self, button)
        core_utill_obj.left_click(self, select_button_element)
    
    def delete_portal_if_exists(self, portal_name):
        """
        Description : Delete the portal if already exists. 
        Most of test cases are getting failed due to exists portal during the suite runs. To overcomes this probles.
        We have to call this method from script which is creating new portal. 
        """
        try :
            ok_button_css = ".pop-top .ibx-dialog-ok-button"
            portal = home_page.get_content_item_object_by_type(self, portal_name, "portal")
            core_utill_obj.right_click(self, portal)
            home_page.select_context_menu_item(self, "Delete")
            utill_obj.synchronize_with_visble_text(self, ok_button_css, "OK", 10)
            ok_button = self.driver.find_element_by_css_selector(ok_button_css)
            core_utill_obj.left_click(self, ok_button)
            time.sleep(5)
        except :
            pass
        
class Portal_run(BasePage):
    
    def __init__(self, driver):
        super(Portal_run, self).__init__(driver)
    
    def run_portal(self, portal_path):
        portal_item_path = portal_path.split('->')
        home_page.select_left_panel(self, 'content')
        home_page.select_repository_folder_item_context_menu(self, portal_item_path[-1], context_menu_item_path='Run', folder_path=portal_item_path[:-1], click_option='right_click')
        core_utill_obj.switch_to_new_window(self)
        
    def close_portal_run_window(self):
        core_utill_obj.switch_to_previous_window(self)
        
    def verify_page_heading(self, expected_heading, msg):
        """
        Description : This method used to verify v5 portal page header title
        """
        page_header_obj = utill_obj.validate_and_get_webdriver_object(self, portal_designer.Vfive_Designer.page_heading_css, 'Page Heading')
        actual_heading = page_header_obj.text.strip()
        utill_obj.asequal(self, actual_heading, expected_heading, msg)
    
    def verify_page_heading_button_is_visible(self, button_name, msg):
        """
        Description : 
        """
        button_icon_fa = {'Share' : 'fa fa-share-alt', 'Stop sharing' : 'fa fa-share-alt', 'Refresh' : 'fa fa-refresh', 'Delete' : 'fa fa-trash', 'Show filters' : 'fa fa-filter'}
        button_css = portal_designer.Vfive_Designer.page_heading_css + " div[title='" + button_name + "']>div[class*='" + button_icon_fa[button_name] + "']"
        button_obj = utill_obj.validate_and_get_webdriver_object(self, button_css, button_name)
        button_visible_status = button_obj.is_displayed()
        utill_obj.asequal(self, True, button_visible_status, msg)
    
    def verify_page_heading_button_color(self, button_name, expected_color, msg):
        """
        """
        button_css = portal_designer.Vfive_Designer.page_heading_css + " div[title='" + button_name + "']"
        utill_obj.verify_element_color_using_css_property(self, button_css, expected_color, msg, 'color')
    
    def verify_page_heading_button_tooltip(self, button_name, msg):
        """
        """
        button_css = portal_designer.Vfive_Designer.page_heading_css + " div[title='" + button_name + "']"
        button_obj = utill_obj.validate_and_get_webdriver_object(self, button_css, button_name)
        utill_obj.verify_object_visible(self, None, True, msg, elem_obj=button_obj)
#         
#         core_utill_obj.python_move_to_element(self, button_obj, element_location='bottom_middle')
#         time.sleep(1)
#         core_utill_obj.python_move_to_element(self, button_obj)
#         time.sleep(2)
#         try :
#             uiautomation.ToolTipControl(Name = button_name).Name
#             tooltip_status = True
#         except LookupError :
#             tooltip_status = False
#         utill_obj.asequal(self, True, tooltip_status, msg)
        
    def select_page_heading_button(self, button_name):
        """
        """
        button_css = portal_designer.Vfive_Designer.page_heading_css + " div[title='" + button_name + "']"
        button_obj = utill_obj.validate_and_get_webdriver_object(self, button_css, button_name)
        core_utill_obj.left_click(self, button_obj)
    