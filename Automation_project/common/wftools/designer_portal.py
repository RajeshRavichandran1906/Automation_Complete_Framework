from common.lib.base import BasePage
from common.pages import portal_designer
from common.pages.portal_canvas import Portal_canvas
from common.pages.portal_sidebar import Two_Level_SideBar
from common.pages.portal_sidebar import Three_Level_SideBar
from common.lib.webfocus.designer_canvas import Designer_Canvas
from common.pages.portal_sidebar import New_Page_Template_Window as NewPageTemplate
from common.pages import portal_banner

class Portal(BasePage):
    
    """ Inherit attributes of the parent class = Baseclass """
    
    NAVIGATION_MODE = None 
    
    def __init__(self, driver):
        super(Portal, self).__init__(driver)
    
    def verify_caption_in_new_or_edit_portal_dialog(self, label_text, step_number):
        '''
        Desc:This function will verify Caption label text.
        @param label_text: 'New Portal'
        @param step_number: '9'
        :Usage verify_caption_in_new_or_edit_portal_dialog('New Portal', '9')
        '''
        msg='Step {0}.a: Verify Caption label text in portal dialog.'.format(str(step_number))
        portal_designer.Portal_Designer.verify_portal_dialog(self, label_text, 'label_text', label_text, msg)
    
    def title_textbox_in_new_or_edit_portal_dialog(self, edit_value=None, verify_value=None, current_mode=None, label_text=None, focused=None, click_on_label=False, step_number=None):
        '''
        Desc:This function will edit, verify Title text-box in create new or edit portal dialog.
        @param edit_value: 'V5 portal'
        @param verify_value: 'V5 portal'
        @param current_mode: 'enable' or 'disable'
        @param label_text: 'Title'
        @param focused: True or False
        @param step_number: '9'
        :Usage title_textbox_new_or_edit_portal_dialog(edit_value='V5 portal', verify_value='V5 portal', current_mode='enable', label_text='Title', focused=True, step_number='9')
        '''
        if edit_value != None:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Title', 'text_box', edit_value)
        if verify_value != None:
            msg='Step {0}.a: Verify Title text value.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Title', 'text_box', verify_value, msg)
        if current_mode != None:
            msg='Step {0}.b: Verify Title text {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Title', 'text_box', current_mode, msg)
        if label_text != None:
            msg='Step {0}.c: Verify Title label text.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Title', 'label_text', label_text, msg)
        if focused != None:
            msg='Step {0}.d: Verify Title Focus {1}.'.format(str(step_number), focused)
            portal_designer.Portal_Designer.verify_focus_in_portal_dialog(self, 'Title', 'text_box', focused, msg)
        if click_on_label:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Title', 'label_text', 'Title')
        
    def name_textbox_in_new_or_edit_portal_dialog(self, edit_value=None, verify_value=None, current_mode=None, label_text=None, focused=None, click_on_label=False,step_number=None):
        '''
        Desc:This function will edit, verify Name text-box in create new or edit portal dialog.
        @param edit_value: 'V5 portal'
        @param verify_value: 'V5 portal'
        @param current_mode: 'enable' or 'disable'
        @param label_text: 'Name'
        @param focused: True or False
        @param step_number: '9'
        :Usage name_textbox_in_new_or_edit_portal_dialog(edit_value='V5 portal', verify_value='V5 portal', current_mode='enable', label_text='Name', focused=True, step_number='9')
        '''
        if edit_value != None:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Name', 'text_box', edit_value)
        if verify_value != None:
            msg='Step {0}.a: Verify Name text value.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Name', 'text_box', verify_value, msg)
        if current_mode != None:
            msg='Step {0}.b: Verify Name text {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Name', 'text_box', current_mode, msg)
        if label_text != None:
            msg='Step {0}.c: Verify Name label text.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Name', 'label_text', label_text, msg)
        if focused != None:
            msg='Step {0}.d: Verify Name Focus {1}.'.format(str(step_number), focused)
            portal_designer.Portal_Designer.verify_focus_in_portal_dialog(self, 'Name', 'text_box', focused, msg)
        if click_on_label:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Name', 'label_text', 'Name')
        
    def alias_textbox_in_new_or_edit_portal_dialog(self, edit_value=None, verify_value=None, current_mode=None, label_text=None, focused=None,click_on_label=False,step_number=None):
        '''
        Desc:This function will edit, verify Alias text-box in create new or edit portal dialog.
        @param edit_value: 'V5 portal'
        @param verify_value: 'V5 portal'
        @param current_mode: 'enable' or 'disable'
        @param label_text: 'Alias'
        @param focused: True or False
        @param step_number: '9'
        :Usage alias_textbox_in_new_or_edit_portal_dialog(edit_value='V5 portal', verify_value='V5 portal', current_mode='enable', label_text='Alias', focused=True, step_number='9')
        '''
        if edit_value != None:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Alias', 'text_box', edit_value)
        if verify_value != None:
            msg='Step {0}.a: Verify Alias text value.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Alias', 'text_box', verify_value, msg)
        if current_mode != None:
            msg='Step {0}.b: Verify Alias text {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Alias', 'text_box', current_mode, msg)
        if label_text != None:
            msg='Step {0}.c: Verify Alias label text.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Alias', 'label_text', label_text, msg)
        if focused != None:
            msg='Step {0}.d: Verify Alias Focus {1}.'.format(str(step_number), focused)
            portal_designer.Portal_Designer.verify_focus_in_portal_dialog(self, 'Alias', 'text_box', focused, msg)
        if click_on_label:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Alias', 'label_text', 'Alias')
        
    def banner_toggle_button_in_new_or_edit_portal_dialog(self, select_toggle=None, verify_toggle=None, current_mode=None, label_text=None, step_number=None):
        '''
        Desc:This function will toggle, verify Banner in create new or edit portal dialog.
        @param select_toggle: 'check' or 'uncheck'
        @param verify_toggle: 'check' or 'uncheck'
        @param current_mode: 'enable' or 'disable'
        @param label_text: 'Banner'
        @param step_number: '9'
        :Usage banner_toggle_button_in_new_or_edit_portal_dialog(select_toggle='check', verify_toggle='check', current_mode='enable', label_text='Banner', step_number='9')
        '''
        if select_toggle != None:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Banner', 'toggle_button', select_toggle)
        if verify_toggle != None:
            msg='Step {0}.a: Verify Banner toggle {1}.'.format(str(step_number), verify_toggle)
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Banner', 'toggle_button', verify_toggle, msg)
        if current_mode != None:
            msg='Step {0}.b: Verify Banner toggle {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Banner', 'toggle_button', current_mode, msg)
        if label_text != None:
            msg='Step {0}.c: Verify Banner label text.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Banner', 'label_text', label_text, msg)
        
    def show_portal_title_in_banner_checkbox_inside_new_or_edit_portal_dialog(self, select_checkbox=None, verify_checkbox=None, current_mode=None, label_text=None, step_number=None):
        '''
        Desc:This function will check and uncheck, verify show_portal_title_in_banner inside create new or edit portal dialog.
        @param select_checkbox: 'check' or 'uncheck'
        @param verify_checkbox: 'check' or 'uncheck'
        @param current_mode: 'enable' or 'disable'
        @param label_text: 'Show portal title in banner'
        @param step_number: '9'
        :Usage show_portal_title_in_banner_inside_new_or_edit_portal_dialog(select_toggle='check', verify_toggle='check', current_mode='enable', label_text='Show portal title in banner', step_number='9')
        '''
        if select_checkbox != None:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Show portal title in banner', 'checkbox', select_checkbox)
        if verify_checkbox != None:
            msg='Step {0}.a: Verify Show portal title in banner checkbox {1}.'.format(str(step_number), verify_checkbox)
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Show portal title in banner', 'checkbox', verify_checkbox, msg)
        if current_mode != None:
            msg='Step {0}.b: Verify Show portal title in banner checkbox {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Show portal title in banner', 'checkbox', current_mode, msg)
        if label_text != None:
            msg='Step {0}.c: Verify Show portal title in banner checkbox label text.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Show portal title in banner', 'checkbox_label', label_text, msg)
        
    def logo_textbox_in_new_or_edit_portal_dialog(self, verify_value=None, verify_placeholder_value=None, current_mode=None, label_text=None, step_number=None):
        '''
        Desc:This function will verify Logo text-box in create new or edit portal dialog.
        @param verify_value: 'V5 portal'
        @param current_mode: 'enable' or 'disable'
        @param label_text: 'Logo'
        @param step_number: '9'
        :Usage logo_textbox_in_new_or_edit_portal_dialog(verify_value='V5 portal', current_mode='enable', label_text='Logo', step_number='9')
        '''
        if verify_value != None:
            msg='Step {0}.a: Verify Logo text value.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Logo', 'text_box', verify_value, msg)
        if verify_placeholder_value != None:
            msg='Step {0}.a: Verify Logo text value.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Logo', 'text_box', None, msg, placeholder=verify_placeholder_value)
        if current_mode != None:
            msg='Step {0}.b: Verify Logo text {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Logo', 'text_box', current_mode, msg)
        if label_text != None:
            msg='Step {0}.c: Verify Logo label text.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Logo', 'label_text', label_text, msg)
    
    def logo_browse_button_in_new_or_edit_portal_dialog(self, verify_value=None, current_mode=None, select_logo_name=None, verify_resource_dialog=None, button_location=None, step_number=None):
        '''
        Desc:This function will verify Logo Browse button in create new or edit portal dialog.
        @param verify_value: 'Browse'
        @param current_mode: 'enable' or 'disable'
        @param select_logo_name: 'cat.jpg'
        @param step_number: '9'
        @param verify_resource_dialog: True
        @param button_location: True
        :Usage logo_browse_button_in_new_or_edit_portal_dialog(verify_value='Browse', current_mode='enable', select_logo_name='cat.jpg', verify_resource_dialog=True, button_location=True, step_number='9')
        '''
        if verify_value != None:
            msg='Step {0}.a: Verify Logo browse button.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Browse', 'button', verify_value, msg)
        if current_mode != None:
            msg='Step {0}.b: Verify Logo browse button {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Browse', 'button', current_mode, msg)
        if select_logo_name != None:
            portal_designer.Portal_Designer.select_logo_in_portal_dialog(self, logo_name=select_logo_name, button='Select')
        if verify_resource_dialog != None:
            disp_msg = 'Step {0}.c: Verify Logo browse resource dialog.'.format(str(step_number))
            portal_designer.Portal_Designer.select_logo_in_portal_dialog(self,  verify_resource_dilaog=verify_resource_dialog, msg=disp_msg, button='Cancel')
        if button_location != None:
            disp_msg = 'Step {0}.d: Verify Logo browse location.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_browse_button_position_in_edit_or_create_portal(self, disp_msg)
        
    def verify_navigation_label_text(self, label_text, step_number):
        '''
        Desc:This function will verify Navigation label text.
        @param label_text: 'Navigation'
        @param step_number: '9'
        :Usage verify_navigation_label_text('Navigation', '9')
        '''
        msg='Step {0}.a: Verify Navigation label text.'.format(str(step_number))
        portal_designer.Portal_Designer.verify_portal_dialog(self, 'Navigation', 'label_text', label_text, msg)
    
    def two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(self, select_type=None, verify_navigation=None, current_mode=None, title_tooltip=None, step_number=None):
        '''
        Desc:This function will check and uncheck, verify Two-level side inside create new or edit portal dialog.
        @param select_type: 'check' or 'uncheck'
        @param verify_navigation: 'check' or 'uncheck'
        @param current_mode: 'enable' or 'disable'
        @param title_tooltip: 'Two-level side'
        @param step_number: '9'
        :Usage two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check', verify_navigation='check', current_mode='enable', title_tooltip='Two-level side', step_number='9')
        '''
        if select_type != None:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Navigation', 'radio_button', select_type)
        if verify_navigation != None:
            msg='Step {0}.a: Verify Two-level side navigation {1}.'.format(str(step_number), verify_navigation)
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Navigation', 'radio_button', verify_navigation, msg)
        if current_mode != None:
            msg='Step {0}.b: Verify Two-level side navigation {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Navigation', 'radio_button', current_mode, msg)
        if title_tooltip != None:
            msg='Step {0}.c: Verify Two-level side navigation title tooltip.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_title_in_portal_dialog(self, 'two-level-side', title_tooltip, msg)
    
    def three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(self, select_type=None, verify_navigation=None, current_mode=None, title_tooltip=None, step_number=None):
        '''
        Desc:This function will check and uncheck, verify Three-level side inside create new or edit portal dialog.
        @param select_type: 'check' or 'uncheck'
        @param verify_navigation: 'check' or 'uncheck'
        @param current_mode: 'enable' or 'disable'
        @param title_tooltip: 'Three-level'
        @param step_number: '9'
        :Usage three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check', verify_navigation='check', current_mode='enable', title_tooltip='Three-level', step_number='9') 
        '''
        if select_type != None:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Navigation', 'radio_button', select_type, navigation_type='Three-level')
        if verify_navigation != None:
            msg='Step {0}.a: Verify Three-level navigation {1}.'.format(str(step_number), verify_navigation)
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Navigation', 'radio_button', verify_navigation, msg, navigation_type='Three-level')
        if current_mode != None:
            msg='Step {0}.b: Verify Three-level navigation {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Navigation', 'radio_button', current_mode, msg, navigation_type='Three-level')
        if title_tooltip != None:
            msg='Step {0}.c: Verify Three-level navigation title tooltip.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_title_in_portal_dialog(self, 'three-level', title_tooltip, msg)
    
    def two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(self, select_type=None, verify_navigation=None, current_mode=None, title_tooltip=None, step_number=None):
        '''
        Desc:This function will check and uncheck, verify Two-level top side inside create new or edit portal dialog.
        @param select_type: 'check' or 'uncheck'
        @param verify_navigation: 'check' or 'uncheck'
        @param current_mode: 'enable' or 'disable'
        @param title_tooltip: 'Two-level-top'
        @param step_number: '9'
        :Usage two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check', verify_navigation='check', current_mode='enable', title_tooltip='Three-level', step_number='9')
        '''
        if select_type != None:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Navigation', 'radio_button', select_type, navigation_type='Two-level-top')
        if verify_navigation != None:
            msg='Step {0}.a: Verify Two-level-top navigation {1}.'.format(str(step_number), verify_navigation)
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Navigation', 'radio_button', verify_navigation, msg, navigation_type='Two-level-top')
        if current_mode != None:
            msg='Step {0}.b: Verify Two-level-top navigation {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Navigation', 'radio_button', current_mode, msg, navigation_type='Two-level-top')
        if title_tooltip != None:
            msg='Step {0}.c: Verify Two-level-top navigation title tooltip.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_title_in_portal_dialog(self, 'two-level-top', title_tooltip, msg)
    
    def show_top_navigation_in_banner_checkbox_inside_new_or_edit_portal_dialog(self, select_checkbox=None, verify_checkbox=None, current_mode=None, label_text=None, step_number=None):
        '''
        Desc:This function will check and uncheck, verify Show top navigation in banner inside create new or edit portal dialog.
        @param select_checkbox: 'check' or 'uncheck'
        @param verify_checkbox: 'check' or 'uncheck'
        @param current_mode: 'enable' or 'disable'
        @param label_text: 'Show top navigation in banner'
        @param step_number: '9'
        :Usage show_top_navigation_in_banner_checkbox_inside_new_or_edit_portal_dialog(select_toggle='check', verify_toggle='check', current_mode='enable', label_text='Show top navigation in banner', step_number='9')
        '''
        if select_checkbox != None:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Show top navigation in banner', 'checkbox', select_checkbox)
        if verify_checkbox != None:
            msg='Step {0}.a: Verify Show top navigation in banner checkbox {1}.'.format(str(step_number), verify_checkbox)
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Show top navigation in banner', 'checkbox', verify_checkbox, msg)
        if current_mode != None:
            msg='Step {0}.b: Verify Show top navigation in banner checkbox {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Show top navigation in banner', 'checkbox', current_mode, msg)
        if label_text != None:
            msg='Step {0}.c: Verify Show top navigation in banner checkbox label text.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Show top navigation in banner', 'checkbox_label', label_text, msg)
    
    def maximum_width_textbox_in_new_or_edit_portal_dialog(self, verify_value=None, edit_value=None, verify_placeholder_value=None, current_mode=None, label_text=None, focused=None,click_on_label=False,step_number=None):
        '''
        Desc:This function will verify maximum width text-box in create new or edit portal dialog.
        @param verify_value: 'Maximum width'
        @param current_mode: 'enable' or 'disable'
        @param label_text: 'Maximum width'
        @param step_number: '9'
        :Usage maximum_width_textbox_in_new_or_edit_portal_dialog(verify_value='Maximum width', current_mode='enable', label_text='Logo', step_number='9')
        '''
        if edit_value != None:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Maximum width', 'max_width_textbox', edit_value)
        if verify_value != None:
            msg='Step {0}.a: Verify Title text value.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Maximum width', 'max_width_textbox', verify_value, msg)
        if current_mode != None:
            msg='Step {0}.b: Verify Title text {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Maximum width', 'max_width_textbox', current_mode, msg)
        if focused != None:
            msg='Step {0}.c: Verify Title Focus {1}.'.format(str(step_number), focused)
            portal_designer.Portal_Designer.verify_focus_in_portal_dialog(self, 'Maximum width', 'max_width_textbox', focused, msg)
        if verify_placeholder_value != None:
            msg='Step {0}.d: Verify Maximun width text value.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Maximum width', 'max_width_textbox', None, msg, placeholder=verify_placeholder_value)
        if current_mode != None:
            msg='Step {0}.e: Verify Maximun width text {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Maximum width', 'max_width_textbox', current_mode, msg)
        if label_text != None:
            msg='Step {0}.f: Verify Maximun width label text.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Maximum width', 'label_text', label_text, msg)
        if click_on_label:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Maximum width', 'label_text', 'Maximum width')
        
    def theme_dropdown_in_new_or_edit_portal_dialog(self, select_theme=None, verify_theme=None, current_mode=None, label_text=None, dropdown_list_value=None, step_number=None):
        '''
        Desc:This function will select, verify Theme inside create new or edit portal dialog.
        @param select_theme: 'Light'
        @param verify_theme: 'Light'
        @param current_mode: 'enable' or 'disable'
        @param label_text: 'Theme'
        @param dropdown_list_value: ['Light']
        @param step_number: '9'
        :Usage theme_dropdown_in_new_or_edit_portal_dialog(select_theme='Light', verify_theme='Light', current_mode='enable', label_text='Theme', dropdown_list_value=['Light'], step_number='9')
        '''
        if select_theme != None:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Theme', 'drop_down', select_theme)
        if verify_theme != None:
            msg='Step {0}.a: Verify Theme selected value {1}.'.format(str(step_number), verify_theme)
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Theme', 'drop_down', verify_theme, msg)
        if current_mode != None:
            msg='Step {0}.b: Verify Theme is {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Theme', 'drop_down', current_mode, msg)
        if label_text != None:
            msg='Step {0}.c: Verify Theme label text.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Theme', 'label_text', label_text, msg)
        if dropdown_list_value != None:
            msg='Step {0}.d: Verify Theme drop-down list {1} value.'.format(str(step_number), dropdown_list_value)
            portal_designer.Portal_Designer.verify_theme_drop_down_options_list_in_portal_dialog(self, dropdown_list_value, msg)
            
    def url_textbox_in_new_or_edit_portal_dialog(self, verify_value=None, readonly_mode=None, label_text=None, step_number=None):
        '''
        Desc:This function will verify URl text-box in create new or edit portal dialog.
        @param verify_value: 'V5 portal'
        @param readonly_mode: True or False
        @param label_text: 'URL'
        @param step_number: '9'
        :Usage url_textbox_in_new_or_edit_portal_dialog(verify_value='V5 portal', readonly_mode='enable', label_text='URL', step_number='9')
        '''
        if verify_value != None:
            msg='Step {0}.a: Verify URL text value {1}.'.format(str(step_number), verify_value)
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'URL', 'text_box', verify_value, msg)
        if readonly_mode != None:
            msg='Step {0}.b: Verify URL read-mode {1}.'.format(str(step_number), readonly_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'URL', 'text_box', 'enable', msg, text_box_readonly=readonly_mode)
        if label_text != None:
            msg='Step {0}.c: Verify URL label text.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'URL', 'label_text', label_text, msg)
        
    def create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(self, select_checkbox=None, verify_checkbox=None, current_mode=None, label_text=None, step_number=None):
        '''
        Desc:This function will check and uncheck, verify Create My Pages menu inside create new or edit portal dialog.
        @param select_checkbox: 'check' or 'uncheck'
        @param verify_checkbox: 'check' or 'uncheck'
        @param current_mode: 'enable' or 'disable'
        @param label_text: 'Create My Pages menu'
        @param step_number: '9'
        :Usage create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(select_toggle='check', verify_toggle='check', current_mode='enable', label_text='Create My Pages menu', step_number='9')
        '''
        if select_checkbox != None:
            portal_designer.Portal_Designer.create_or_edit_portal(self, 'Create My Pages menu', 'checkbox', select_checkbox)
        if verify_checkbox != None:
            msg='Step {0}.a: Verify Create My Pages menu checkbox {1}.'.format(str(step_number), verify_checkbox)
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Create My Pages menu', 'checkbox', verify_checkbox, msg)
        if current_mode != None:
            msg='Step {0}.b: Verify Create My Pages menu checkbox {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Create My Pages menu', 'checkbox', current_mode, msg)
        if label_text != None:
            msg='Step {0}.c: Verify Create My Pages menu checkbox label text.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Create My Pages menu', 'checkbox_label', label_text, msg)
        
    def create_button_inside_new_or_edit_portal_dialog(self, select_button=False, verify_button=None, current_mode=None, color_name=None, step_number=None):
        '''
        Desc:This function will select, verify Create Button inside create new or edit portal dialog.
        @param select_button: True or False
        @param verify_button: 'Create'
        @param current_mode: 'enable' or 'disable'
        @param color_name: 'blue'
        @param step_number: '9'
        :Usage create_button_inside_new_or_edit_portal_dialog(select_button=True, verify_button='Create', current_mode='enable', color_name='blue', step_number='9')
        '''
        if select_button:
            portal_designer.Portal_Designer.close_portal_dialog(self, 'Create')
        if verify_button != None:
            msg='Step {0}.a: Verify Create button.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Create', 'button', verify_button, msg)
        if current_mode != None:
            msg='Step {0}.b: Verify Create button {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Create', 'button', current_mode, msg)
        if color_name != None:
            msg='Step {0}.c: Verify Create button color {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_button_color_in_portal_dialog(self, 'Create', color_name, msg)
    
    def save_button_inside_new_or_edit_portal_dialog(self, select_button=False, verify_button=None, current_mode=None, color_name=None, step_number=None):
        '''
        Desc:this function is used to save a portal inside new or edit portal dialog
        @param select_button: True or False
        @param verify_button: 'Save'
        @param current_mode: 'enable' or 'disable'
        @param color_name: 'blue'
        @param step_number: '9'
        :Usage save_button_inside_new_or_edit_portal_dialog(select_button=True, verify_button='Save', current_mode='enable', color_name='blue', step_number='9')
        '''
        if select_button == True:
            portal_designer.Portal_Designer.close_portal_dialog(self, 'Save')
        if verify_button != None:
            msg='Step {0}.a: Verify Save button.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Save', 'button', verify_button, msg)
        if current_mode != None:
            msg='Step {0}.b: Verify Save button {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Save', 'button', current_mode, msg)
        if color_name != None:
            msg='Step {0}.c: Verify Save button color {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_button_color_in_portal_dialog(self, 'Save', color_name, msg)
    
    def cancel_button_inside_new_or_edit_portal_dialog(self, select_button=False, verify_button=None, current_mode=None, color_name=None, step_number=None):
        '''
        Desc:This function will select, verify Cancel Button inside create new or edit portal dialog.
        @param select_button: True or False
        @param verify_button: 'Save'
        @param current_mode: 'enable' or 'disable'
        @param color_name: 'blue'
        @param step_number: '9'
        :Usage cancel_button_inside_new_or_edit_portal_dialog(select_button=True, verify_button='Cancel', current_mode='enable', color_name='blue', step_number='9')
        '''
        if select_button == True:
            portal_designer.Portal_Designer.close_portal_dialog(self, 'Cancel')
        if verify_button != None:
            msg='Step {0}.a: Verify Cancel button.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_portal_dialog(self, 'Cancel', 'button', verify_button, msg)
        if current_mode != None:
            msg='Step {0}.b: Verify Cancel button {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'Cancel', 'button', current_mode, msg)
        if color_name != None:
            msg='Step {0}.c: Verify Cancel button color {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_button_color_in_portal_dialog(self, 'Cancel', color_name, msg, color_rgba_alpha_value='0')
    
    def close_button_inside_new_or_edit_portal_dialog(self, select_button=False, current_mode=None, color_name=None, title_tooltip=None, step_number=None):
        '''
        Desc:This function will select, verify Close Button inside create new or edit portal dialog.
        @param select_button: True or False
        @param verify_button: 'Save'
        @param current_mode: 'enable' or 'disable'
        @param color_name: 'blue'
        @param step_number: '9'
        :Usage cancel_button_inside_new_or_edit_portal_dialog(select_button=True, verify_button='close', current_mode='enable', color_name='blue', step_number='9')
        '''
        if select_button == True:
            portal_designer.Portal_Designer.close_portal_dialog(self, 'close')
        if current_mode != None:
            msg='Step {0}.a: Verify Close button {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_portal_dialog_content_enable_disable(self, 'close', 'button', current_mode, msg)
        if color_name != None:
            msg='Step {0}.b: Verify close button color {1}.'.format(str(step_number), current_mode)
            portal_designer.Portal_Designer.verify_button_color_in_portal_dialog(self, 'close', color_name, msg, color_rgba_alpha_value='0')
        if title_tooltip != None:
            msg='Step {0}.c: Verify close button title tooltip.'.format(str(step_number))
            portal_designer.Portal_Designer.verify_title_in_portal_dialog(self, 'close', title_tooltip, msg)
    
    def verify_portal_dialog_open_or_close(self, dialog_mode, msg):
        '''
        Desc:This function will verify portal dialog is open or close.
        @param dialog_mode: 'open'
        @param msg: 'Step 9: Verify'
        :Usage  verify_portal_dialog_open_or_close('open', 'Step 9: Verify')
        '''
        portal_designer.Portal_Designer.verify_portal_dialog_open_or_close(self, dialog_mode, msg)
        
    def verify_alert_message_in_portal_dialog(self, warning_msg, step_number, verify_color_name=None):
        '''
        This function will verify alert message in create or edit portal
        verify_alert_message_in_portal_dialog('Alias already exists', '1')
        '''
        portal_designer.Portal_Designer.verify_alert_message_in_portal_dialog(self, warning_msg, step_number, verify_color_name=verify_color_name)
    
    def delete_portal_if_exists(self, portal_name):
        """
        Description : Delete the portal if already exists. 
        Most of test cases are getting failed due to exists portal during the suite runs. To overcomes this problem.
        We should call this method from script which is creating new portal. 
        """
        portal_designer.Portal_Designer.delete_portal_if_exists(self, portal_name)
        
class Banner(BasePage):
    
    """ Inherit attributes of the parent class = Baseclass """
    
    NAVIGATION_MODE = None 
    
    def __init__(self, driver):
        super(Banner, self).__init__(driver)
        
    def verify_portal_top_banner_title(self, expected_title, msg):
        '''
        Desc:This function will verify portal top banner title at runtime.
        '''
        portal_banner.Portal_banner.verify_portal_title(self, expected_title, msg)
    
class Canvas(BasePage):
    
    """ Inherit attributes of the parent class = Baseclass """
    def __init__(self, driver):
        super(Canvas, self).__init__(driver)
        self._portal_canvas = Portal_canvas(self.driver)
        
    def verify_blank_canvas_text(self, msg, expected_text='There are no pages available'):
        """
        Desc: This method will verify page header title
        """
        self._portal_canvas.verify_blank_canvas_text(msg, expected_text)
    
    def verify_page_header_title(self, expected_title, msg):
        """
        Desc: This method will verify page header title
        """
        self._portal_canvas.verify_page_header_title(expected_title, msg)
    
    def verify_page_header_all_buttons(self, expected_buttons_name_list, msg):
        """
        Desc: This method will all visible buttons on page header
        example usage : verify_page_header_all_buttons(['Share', 'Refresh', 'Delete'], 'Step 01 : Verify page header button')
        """
        self._portal_canvas.verify_page_header_buttons(expected_buttons_name_list, msg)
        
    def verify_page_header_specific_buttons(self, expected_buttons_name_list, msg):
        """
        Desc: This method will any specific visible buttons on page header
        example usage : verify_page_header_specific_buttons(['Share', 'Delete'], 'Step 01 : Verify Share and Delete buttons are displayed in page header')
        """
        self._portal_canvas.verify_page_header_buttons(expected_buttons_name_list, msg,  assert_type='asin')
        
    def verify_page_header_button_tooltip(self, button_name, msg):
        """
        Desc: This method will mouse move on page header and verify tooltip using uiautomation
        example usage : verify_page_header_button_tooltip('Share', 'Step 01.1 : Verify Share button tooltip')
        """
        self._portal_canvas.verify_page_heading_button_tooltip(button_name, msg)
        
    def verify_page_header_button_color(self, button_name, msg, expected_color='night_rider'):
        """
        Desc: This method will verify page header button color 
        example usage : verify_page_header_button_color('Share', 'blue', 'Step 01.1 : Verify Share button color')
        """
        self._portal_canvas.verify_page_header_button_color(button_name, expected_color, msg)
        
    def delete_page(self):
        """
        Desc: This method will click on delete button in page header
        example usage : delete_page()
        """
        self._portal_canvas.click_on_page_header_button('Delete')
        
    def refresh_page(self):
        """
        Desc: This method will click on Refresh button in page header
        example usage : refresh_page()
        """
        self._portal_canvas.click_on_page_header_button('Refresh')
    
    def click_on_page_header_button(self, button_name):
        """
        Desc: This method will click on page header buttons
        example usage : click_on_page_header_button('Share')
        """
        self._portal_canvas.click_on_page_header_button(button_name)
    
    def verify_all_containers_title(self, expected_containers_title, msg):
        """
        Desc: This method will verify all containers title in canvas
        example usage : verify_all_containers_title(['Panel 1', 'Panel 2', 'Panel 3'], 'Step 01 : Verify 3 containers displayed in canvas')
        """
        self._portal_canvas.verify_containers_title(expected_containers_title, msg)
        
    def verify_specific_containers_title(self, expected_containers_title, msg):
        """
        Desc: This method will verify specific containers title in canvas
        example usage : verify_specific_containers_title(['Panel 1'], 'Step 01.1 : Verify Panel 1 container is displayed in canvas')
        """
        self._portal_canvas.verify_containers_title(expected_containers_title, msg, assert_type='asin')
        
    def maximize_container(self, container_title, container_title_index=1):
        """
        Desc: This method will click on maximize button in given container title bar
        example usage : maximize_container('Panel 1')
        """
        self._portal_canvas.click_on_containers_title_bar_button(container_title, 'Maximize', container_title_index)
    
    def restore_container(self, container_title, container_title_index=1):
        """
        Desc: This method will click on Restore button in given container title bar
        example usage : restore_container('Panel 1')
        """
        self._portal_canvas.click_on_containers_title_bar_button(container_title, 'Restore', container_title_index)
    
    def select_container_title_bar_option(self, container_title, option_name, container_title_index=1):
        pass
    
    def verify_container_title_bar_options(self, container_title, expected_options, msg, container_title_index=1):
        pass
        
    def verify_container_title_bar_all_buttons(self, container_title, expected_buttons_list, msg, container_title_index=1):
        """
        Desc: This method will verify all visible container title bar buttons
        example usage : verify_container_title_bar_options('Panel 1', ['Maximize', 'Options'], 'Step 01.1 : Verify ['Maximize', 'Options'] buttons are visible in Panel 1 container')
        """
        self._portal_canvas.verify_container_title_bar_buttons(container_title, expected_buttons_list, msg, container_title_index)
    
    def verify_container_title_bar_specific_buttons(self, container_title, expected_buttons_list, msg, container_title_index=1):
        """
        Desc: This method will verify specific visible container title bar buttons
        example usage : verify_container_title_bar_all_buttons('Panel 1', ['Maximize'], 'Step 01.1 : Verify ['Maximize'] button is visible in Panel 1 container')
        """
        self._portal_canvas.verify_container_title_bar_buttons(container_title, expected_buttons_list, msg, container_title_index, assert_type='asin')
    
    def verify_container_title_bar_button_tooltip(self, container_title, button_name, msg, container_title_index=1) :
        """
        Desc: This method will mouse move on container title bar button and verify tooltip using uiautomation
        example usage : example usage : verify_container_title_bar_button_tooltip('Panel 1', 'Maximize', 'Step 01.1 : Verify Maximize button tooltip')
        """
        self._portal_canvas.verify_container_title_bar_button_tooltip(container_title, button_name, msg, container_title_index)
    
    def verify_container_title_bar_button_color(self, container_title, button_name, msg, expected_color='night_rider', container_title_index=1):
        """
        Desc: This method will verify container title button color 
        example usage : verify_container_title_bar_button_color(''Panel 1', 'Maximize', 'blue', 'Step 01.1 : Verify Maximize button color')
        """
        self._portal_canvas.verify_container_title_bar_button_color(container_title, button_name, expected_color, msg, container_title_index)
    
    def click_on_panel_add_content_button_in_container(self, panel_name, panel_index=1):
        """
        Desc: This method will click on add content button on panel container in canvas 
        example usage : click_on_panel_add_content_button_in_container('Panel 1')
        """
        self._portal_canvas.click_on_panel_add_content_button_in_container(panel_name, 'panel', panel_index)
    
    def click_on_tab_add_content_button_in_container(self, panel_name, panel_index=1):
        """
        Desc: This method will click on add content button on tab panel container in canvas 
        example usage : click_on_tab_add_content_button_in_container('Panel 1')
        """
        self._portal_canvas.click_on_panel_add_content_button_in_container(panel_name, 'tab', panel_index)
    
    def click_on_carousel_add_content_button_in_container(self, panel_name, panel_index=1):
        """
        Desc: This method will click on add content button on carousel panel container in canvas 
        example usage : click_on_carousel_add_content_button_in_container('Panel 1')
        """
        self._portal_canvas.click_on_panel_add_content_button_in_container(panel_name, 'carousel', panel_index)
    
    def click_on_accordion_add_content_button_in_container(self, panel_name, panel_index=1):
        """
        Desc: This method will click on add content button on accordion panel container in canvas 
        example usage : click_on_accordion_add_content_button_in_container('Panel 1')
        """
        self._portal_canvas.click_on_panel_add_content_button_in_container(panel_name, 'accordion', panel_index)
    
    def select_repository_file_using_add_content_in_panel_container(self, file_path, select_button='Select'):
        """
        Desc:This function will select file from resource dialog using crumb path.
        :Usage select_repositoiry_file_using_add_content_in_panel_container(P292_S19901->G513445->test')
        """
        self._portal_canvas.select_repository_file_using_add_content_in_panel_container(file_path,select_button=select_button)
    
    def select_repository_file_using_add_content_using_crumb_in_panel_container(self, crumb_box_option, file_path, select_button='Select'):
        """
        Desc: This function will select file from resource dialog. 
        :Usage select_repositoiry_file_using_add_content_using_crumb_path_in_panel_container('Domain', 'P292_S19901->G513445->test')
        """
        self._portal_canvas.select_repository_file_using_add_content_in_panel_container(file_path, crumb_box_option=crumb_box_option, select_button=select_button)
        
    def verify_panel_add_content_displayed_in_container(self, panel_name, msg, panel_index=1):
        """
        Desc: This method will verify whether add content button is displayed in panel container in canvas 
        example usage : verify_panel_add_content_displayed_in_container('Panel 1', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'panel', msg, panel_index)
    
    def verify_panel_add_content_color_in_container(self, panel_name, expected_color, msg, panel_index=1):
        """
        Desc: This method will verify content button color in container 
        example usage : verify_panel_add_content_color_in_container('Panel 1', 'grey', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'panel', msg, panel_index, expected_color=expected_color)
    
    def verify_panel_add_content_color_in_container_after_mouse_move(self, panel_name, expected_color, msg, panel_index=1):
        """
        Desc: This method will mouse move on add content button and verify color on container in canvas 
        example usage : verify_panel_add_content_color_in_container_after_mouse_move('Panel 1', 'grey', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'panel', msg, panel_index, mouse_move_expected_color=expected_color)
    
    def verify_panel_add_content_tooltip_in_container(self, panel_name, expected_tooltip, msg, panel_index=1):
        """
        Desc: This method will verify add content button tool-tip in container
        example usage : verify_panel_add_content_tooltip_in_container('Panel 1', 'Add Content', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'panel', msg, panel_index, expected_tooltip=expected_tooltip)
    
    def verify_tab_list_in_container(self, panel_name, expected_tab_list, msg, panel_index=1):
        """
        Desc: This method will verify tab name list
        example usage : verify_tab_list_in_container('Panel 1', ['tab1'], 'Step 9: Verify')
        """
        container_object = self._portal_canvas.get_panel_container(panel_name, panel_index)
        self._portal_canvas.verify_tab_panel(container_object, msg, tab_name_list=expected_tab_list, comparison_type='asequal')
    
    def verify_number_of_slide_in_carousel_panel_container(self, panel_name, number_of_slide, msg, panel_index=1):
        """
        Desc: This method will verify number of slide
        example usage : verify_number_of_slide_in_carousel_panel_container('Panel 1', 6, 'Step 9: Verify')
        """
        container_object = self._portal_canvas.get_panel_container(panel_name, panel_index)
        self._portal_canvas.verify_carousel_panel(container_object, msg, number_of_slide=number_of_slide)
         
    def verify_tab_panel_add_content_displayed_in_container(self, panel_name, msg, panel_index=1):
        """
        Desc: This method will verify whether add content button is displayed in tab panel container. 
        example usage : verify_tab_panel_add_content_displayed_in_container('Panel 1', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'tab', msg, panel_index)
    
    def verify_tab_panel_add_content_color_in_container(self, panel_name, expected_color, msg, panel_index=1):
        """
        Desc: This method will verify content button color in tab panel container. 
        example usage : verify_tab_panel_add_content_color_in_container('Panel 1', 'grey', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'tab', msg, panel_index, expected_color=expected_color)
    
    def verify_tab_panel_add_content_color_in_container_after_mouse_move(self, panel_name, expected_color, msg, panel_index=1):
        """
        Desc: This method will mouse move on add content button and verify color on container in tab panel container. 
        example usage : verify_tab_panel_add_content_color_in_container_after_mouse_move('Panel 1', 'grey', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'tab', msg, panel_index, mouse_move_expected_color=expected_color)
    
    def verify_tab_panel_add_content_tooltip_in_container(self, panel_name, expected_tooltip, msg, panel_index=1):
        """
        Desc: This method will verify add content button tool-tip in tab panel container.
        example usage : verify_tab_panel_add_content_tooltip_in_container('Panel 1', 'Add Content', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'tab', msg, panel_index, expected_tooltip=expected_tooltip)
    
    def verify_carousel_panel_add_content_displayed_in_container(self, panel_name, msg, panel_index=1):
        """
        Desc: This method will verify whether add content button is displayed in carousel panel container. 
        example usage : verify_carousel_panel_add_content_displayed_in_container('Panel 1', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'carousel', msg, panel_index)
    
    def verify_carousel_panel_add_content_color_in_container(self, panel_name, expected_color, msg, panel_index=1):
        """
        Desc: This method will verify content button color in carousel panel container. 
        example usage : verify_carousel_panel_add_content_color_in_container('Panel 1', 'grey', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'carousel', msg, panel_index, expected_color=expected_color)
    
    def verify_carousel_panel_add_content_color_in_container_after_mouse_move(self, panel_name, expected_color, msg, panel_index=1):
        """
        Desc: This method will mouse move on add content button and verify color on container in carousel panel container. 
        example usage : verify_carousel_panel_add_content_color_in_container_after_mouse_move('Panel 1', 'grey', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'carousel', msg, panel_index, mouse_move_expected_color=expected_color)
            
    def verify_carousel_panel_add_content_tooltip_in_container(self, panel_name, expected_tooltip, msg, panel_index=1):
        """
        Desc: This method will verify add content button tool-tip in carousel panel container.
        example usage : verify_carousel_panel_add_content_tooltip_in_container('Panel 1', 'Add Content', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'carousel', msg, panel_index, expected_tooltip=expected_tooltip)
        
    def verify_accordion_panel_add_content_displayed_in_container(self, panel_name, msg, panel_index=1):
        """
        Desc: This method will verify whether add content button is displayed in accordion panel container. 
        example usage : verify_accordion_panel_add_content_displayed_in_container('Panel 1', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'accordion', msg, panel_index)
    
    def verify_accordion_panel_add_content_color_in_container(self, panel_name, expected_color, msg, panel_index=1):
        """
        Desc: This method will verify content button color in accordion panel container. 
        example usage : verify_accordion_panel_add_content_color_in_container('Panel 1', 'grey', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'accordion', msg, panel_index, expected_color=expected_color)
    
    def verify_accordion_panel_add_content_color_in_container_after_mouse_move(self, panel_name, expected_color, msg, panel_index=1):
        """
        Desc: This method will mouse move on add content button and verify color on container in accordion panel container. 
        example usage : verify_accordion_panel_add_content_color_in_container_after_mouse_move('Panel 1', 'grey', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'accordion', msg, panel_index, mouse_move_expected_color=expected_color)
    
    def verify_accordion_panel_add_content_tooltip_in_container(self, panel_name, expected_tooltip, msg, panel_index=1):
        """
        Desc: This method will verify add content button tool-tip in accordion panel container.
        example usage : verify_accordion_panel_add_content_tooltip_in_container('Panel 1', 'Add Content', 'Step 9: Verify')
        """
        self._portal_canvas.verify_add_content_in_container(panel_name, 'accordion', msg, panel_index, expected_tooltip=expected_tooltip)
    
    def switch_to_panel_frame(self, panel_title, panel_title_index=1):
        """
        Desc: This method will switch to panel container frame 
        example usage : switch_to_panel_frame('Panel 1')
        """
        panel_object = Designer_Canvas.get_container_parent_object(self, panel_title, panel_title_index)
        self._portal_canvas.switch_to_container_frame(panel_object)
    
    def verify_page_delete_dialog_is_displayed(self, msg):
        """
        Desc: This method will verify page delete dialog in displayed
        """
        self._portal_canvas.verify_dialog_title('Delete', msg)
    
    def verify_page_delete_dialog_message(self, expected_msg, msg):
        """
        Desc: This method will verify page delete dialog message
        """
        self._portal_canvas.verify_dialog_msg(expected_msg, msg)
    
    def click_ok_button_in_page_delete_dialog(self):
        """
        Desc: This method will click on OK button in page delete 
        """
        self._portal_canvas.click_on_dialog_button('OK')
    
    def click_show_filters(self):
        """
        Descriptions : This method used to click on show filters button
        """
        self._portal_canvas.click_show_filters()
        
class New_Page_Template_Window(BasePage):
    
    """ Inherit attributes of the parent class = Baseclass """
    def __init__(self, driver):
        
        super(New_Page_Template_Window, self).__init__(driver)
        self._new_page_template = NewPageTemplate(self.driver)
        
    def select_new_page_template(self, template_name):
        """
        Desc: This method will select new page template
        example usage : select_new_page_template('Grid')
        """
        self._new_page_template.select_template(template_name)
    
    def click_on_link_to_an_existing_page_button(self):
        """
        Desc: This method will click on Link to an existing page button 
        example usage : click_on_link_to_an_existing_page_button()
        """
        self._new_page_template.click_on_link_to_an_existing_page_button()
    
    def close_new_page_template_window(self):
        """
        Desc: This method will click on close widow icon in new page template window 
        example usage : close_new_page_template_window()
        """
        self._new_page_template.close_new_page_template_window()
    
    def verify_new_page_template_window_is_displayed(self, msg):
        """
        Desc: This method will verify whether new page template window is displayed 
        ample usage : verify_new_page_template_window_is_displayed('Step 01.1 : Verify new page template is displayed')
        """ 
        self._new_page_template.verify_new_page_template_window_is_displayed(msg)
    
    def verify_new_page_templates(self, expected_templates, msg):
        """
        Desc: This method will verify visible all templates
        example usage : verify_new_page_templates(['Grid 2-1', 'Grid 2-1 Side', 'Grid 3-3-3', 'Grid 4-2-1'], 'Step 01.1 : Verify 4 templates are displayed' in new page template window)
        """
        self._new_page_template.verify_templates(expected_templates, msg)
        
        
class Share_With_Others_Window(BasePage):
    
    """ Inherit attributes of the parent class = Baseclass """
    def __init__(self, driver):
        super(Share_With_Others_Window, self).__init__(driver)
    
    def verify_share_window_title(self, expected_title, msg):
        pass    
        
    def verify_share_window_search_textbox_value(self, expected_value, msg):
        pass
     
    def verify_share_window_search_textbox_placeholder_value(self, expected_value, msg):
        pass    
    
    def verify_share_with_everyone_option_is_checked_in_share_window(self, msg):
        pass
    
    def verify_share_with_everyone_option_is_unchecked_in_share_window(self, msg):
        pass
    
    def verify_search_dropdown_options_in_share_window(self, expected_options_list, msg):
        pass
    
    def verify_selected_search_dropdown_option_in_share_window(self, expected_selected_option, msg):
        pass
    
    def verify_buttons_in_share_window(self, msg, expected_buttons_list=['OK', 'Cancel'] ):
        pass
    
    def verify_ok_button_is_enabled_in_share_window(self, msg):
        pass
    
    def verify_ok_button_is_disabled_in_share_window(self, msg):
        pass
    
    def verify_cancel_button_is_enabled_in_share_window(self, msg):
        pass
    
    def verify_ok_button_color_in_share_window(self, expected_color, msg):
        pass
    
    def verify_cancel_button_color_in_share_window(self, expected_color, msg):
        pass
    
    def verify_searched_all_result_items_in_share_window(self, expected_items_list, msg):
        pass
    
    def verify_searched_specific_result_items_in_share_window(self, expected_items_list, msg):
        pass
    
    def verify_already_selected_items_in_searched_result_items_list(self, expected_items_result, msg):
        pass
    
    def verify_selected_all_users_and_groups_in_share_window(self, expected_groups_users_list, msg):
        pass
    
    def verify_all_users_and_groups_are_removed_in_share_window(self, msg):
        pass
    
    def verify_selected_specific_users_and_groups_in_share_window(self, expected_groups_users_list, msg):
        pass

    def verify_share_with_label_value_in_share_window(self, msg, expected_value='Shared with'):
        pass

    def click_on_search_textbox_dropdown_icon_in_share_window(self):
        pass
    
    def select_search_dropdown_option(self, option_name):
        pass
    
    def serach_users_or_groups_in_share_window(self, search_value):
        pass
    
    def select_searched_result_item_in_search_window(self, item_to_select):
        pass
    
    def remove_selected_users_and_groups_in_share_window(self, users_or_groups):
        pass
    
    def click_on_ok_button_in_share_window(self):
        pass
    
    def click_on_cancel_button_in_share_window(self):
        pass
    
    def click_on_close_icon_in_share_window(self):
        pass
    
    def click_on_share_with_everyone_checbox_in_share_window(self):
        pass


class Two_Level_Side(Portal, Canvas, Share_With_Others_Window, New_Page_Template_Window):
    
    """ Inherit attributes of the parent class =  Common_Portal, Canvas"""
    def __init__(self, driver):
        super(Two_Level_Side, self).__init__(driver)
        self._left_sidebar = Two_Level_SideBar(self.driver)
    
    def select_page_from_folder_in_left_sidebar(self, folder_name, page_name):
        """
        Desc: This method will left click on page under the folder to select
        Example usage : select_page_from_folder_in_left_sidebar('My Pages', 'Page 1')
        """
        self._left_sidebar.select_page_from_folder(folder_name, page_name)
    
    def click_on_plus_icon_under_the_folder_in_left_sidebar(self, folder_name):
        """
        Desc: This method will left click on plus icon button to create new page under the folder
        Example usage : click_on_plus_icon_under_the_folder_in_left_sidebar('My Pages')
        """
        self._left_sidebar.select_page_from_folder(folder_name, '+')
    
    def expand_folder_in_left_sidebar(self, folder_name):
        """
        Desc: This method will expand the folder
        Example usage : expand_folder_in_left_sidebar('My Pages')
        """
        self._left_sidebar.expand_or_collapse_folder(folder_name)
    
    def collapse_folder_in_left_sidebar(self, folder_name):
        """
        Desc: This method will collapse the folder
        Example usage : collapse_folder_in_left_sidebar('My Pages')
        """
        self._left_sidebar.expand_or_collapse_folder(folder_name, action='collapse')
    
    def rename_page_under_the_folder_in_left_sidebar(self, folder_name, page_name, name_to_change):
        """
        Desc: This method will change name by double click on page under the folder
        Example usage : rename_page_under_the_folder_in_left_sidebar('My Pages', 'Page 1', 'Page')
        """
        self._left_sidebar.rename_page_under_the_folder(folder_name, page_name, name_to_change)
    
    def select_page_from_top_folder(self, page_name):
        """
        Desc: This method will select page from bundle top folder.
        """
        self._left_sidebar.select_page_from_top_folder(page_name)
    
    def click_on_new_page_from_top_folder(self):
        """
        Desc: This method will click on new page + icon from bundle top folder.
        """
        self._left_sidebar.click_on_new_page_from_top_folder()
    
    def rename_page_name_from_top_folder(self, page_name, name_to_change):
        """
        Desc: This method used to double click on page name and enter value.
        """
        self._left_sidebar.rename_page_name_from_top_folder(page_name, name_to_change)
        
    def verify_page_name_in_from_top_folder(self, page_name, msg):
        """
        Desc: This method will verify page in bundle top folder.
        """
        self._left_sidebar.verify_page_from_top_folder([page_name], 'asin', msg)
    
    def verify_page_name_not_in_from_top_folder(self, page_name, msg):
        """
        Desc: This method will verify page not in bundle top folder.
        """
        self._left_sidebar.verify_page_from_top_folder([page_name], 'asnotin', msg)
        
    def verify_all_pages_from_top_folder(self, page_name_list, msg):
        """
        Desc: This method will verify all pages from bundle top folder.
        """
        self._left_sidebar.verify_page_from_top_folder(page_name_list, 'asequal', msg)
    
    def verify_selected_page_from_top_folder(self, page_name, msg):
        """
        Desc: This method will verify selected page from bundle top folder.
        """
        self._left_sidebar.verify_selected_page_from_top_folder(page_name, msg)
    
    def verify_folders_in_left_sidebar(self, expected_folders_list, msg,assert_type="asequal"):
        """
        Desc: This method will verify all displayed folders in left side bar
        Example usage : 
        """
        self._left_sidebar.verify_folders(expected_folders_list, msg,assert_type=assert_type)
    
    def verify_specific_folders_in_left_sidebar(self, expected_folders_list, msg):
        """
        Desc: This method will verify specific displayed folders in left side bar
        Example usage : 
        """
        self._left_sidebar.verify_folders(expected_folders_list, msg, assert_type='asin')
    
    def verify_pages_under_the_folder_in_left_sidebar(self, folder_name, expected_pages_list, msg):
        """
        Desc: This method will verify all displayed pages under the folder in left side bar
        Example usage : 
        """
        self._left_sidebar.verify_pages_in_folder(folder_name, expected_pages_list, msg)
    
    def verify_specific_pages_under_the_folder_in_left_sidebar(self, folder_name, expected_pages_list, msg):
        """
        Desc: This method will verify specific pages are displayed folders in left side bar
        Example usage : 
        """
        self._left_sidebar.verify_pages_in_folder(folder_name, expected_pages_list, msg, assert_type='asin')
    
    def verify_pages_not_displayed_under_the_folder_in_left_sidebar(self, folder_name, expected_pages_list, msg):
        """
        Desc: This method will verify whether specific pages are not displayed under the folder in lef side bar
        Example usage : 
        """
        self._left_sidebar.verify_pages_in_folder(folder_name, expected_pages_list, msg, assert_type='asnotin')
    
    def verify_folder_expanded_icon_in_left_sidebar(self, folder_name, msg):
        """
        Desc: This method will verify expanded icon
        Example usage : 
        """
        self._left_sidebar.verify_folder_expanded_or_collapsed_icon(folder_name, 'expanded', msg)
    
    def verify_folder_collapsed_icon_in_left_sidebar(self, folder_name, msg):
        """
        Desc: This method will verify collapsed icon
        Example usage : 
        """
        self._left_sidebar.verify_folder_expanded_or_collapsed_icon(folder_name, 'collapsed', msg)
    
      
class Three_Level(Portal, Canvas, Share_With_Others_Window, New_Page_Template_Window):
    
    """ Inherit attributes of the parent class =  Common_Portal, Canvas"""
    def __init__(self, driver):
        super(Three_Level, self).__init__(driver)
        self._three_level_sidebar = Three_Level_SideBar(self.driver) 
 
    def verify_all_top_folders(self, folder_list, msg):
        """
        Desc: This function will verify all folders in the top folder
        usage: verify_all_top_folders_list(['Page 1', 'My Pages'], 'Step 01.1 : Verify ')   
        """
        self._three_level_sidebar.verify_three_level_top_folders(folder_list, msg)
        
    def verify_specific_folder_in_top_folders(self, folder_list, msg):
        """
        Desc: Verify a specific folder in top folders list
        usage: verify_specific_folder_in_top_folders(['Page 1'], msg) 
        """
        self._three_level_sidebar.verify_three_level_top_folders(folder_list, msg, assert_type='asin')
    
    def verify_specific_folder_not_in_top_folders(self, folder_list, msg):
        """
        Desc: Verify a folder not in the top folders list
        usage: verify_specific_folder_not_in_top_folders(['Page 1'], msg)
        """
        self._three_level_sidebar.verify_three_level_top_folders(folder_list, msg, assert_type='asnotin')
        
    def verify_specific_top_folder_color(self, folder_name, color_name, msg):
        """
        Desc: Verify the colour of the specific folder
        usage: verify_specific_top_folder_color('Pages 1', 'blue', 'Step 01.01 : Verify 'page 1' folder color')
        """
        self._three_level_sidebar.verify_three_level_top_folder_color(folder_name, color_name, msg)
        
    def verify_selected_folder_in_top_folders(self, folder_list, msg):
        """
        Desc: verify the selected folder in the top list
        usage: verify_selected_folder_in_top_folders(['Page 1'])
        """
        self._three_level_sidebar.verify_selected_three_level_top_folder(folder_list, msg)
    
    def select_a_specific_top_folder(self, folder_name):
        """
        Desc: select a specific top folder
        usage: select_a_specific_top_folder('Designer')
        """
        self._three_level_sidebar.select_three_level_top_folder(folder_name)
        
    def verify_items_in_left_navigation_bar(self, item_list, msg):
        """
        Desc: verifies all the items in left navigation bar
        usage: verify_items_in_left_navigation_bar(['Page 1', 'Page 2'], 'Step 01.1 : Verify')  
        """
        self._three_level_sidebar.verify_top_folder_items(item_list, msg)
        
    def verify_specific_item_in_left_navigation_bar(self, item_list, msg):
        """
        Desc: verifies if a specific item is present in the left navigation bar
        usage: verify_specific_item_in_left_navigation_bar(['Page 2'], 'Step 01.1 : Verify')
        """
        self._three_level_sidebar.verify_top_folder_items(item_list, msg, assert_type='asin')
        
    def verify_specific_item_not_in_left_navigation_bar(self, item_list, msg):
        """
        Desc: verifies a specific item not in the navigation bar 
        usage: verify_specific_item_not_in_left_navigation_bar(['Page 2'], 'Step 01.1 : Verify')
        """
        self._three_level_sidebar.verify_top_folder_items(item_list, msg, assert_type='asnotin')
        
    def verify_item_color_in_left_navigation_bar(self, folder_name, color, msg):
        """
        Desc: verifies the color of the item in the left navigation bar
        usage: verify_item_color_in_left_navigation_bar('Pages 1', 'blue', 'Step 01.01 : Verify 'page 1' folder color')
        """
        self._three_level_sidebar.verify_top_folder_item_color(folder_name, color, msg)
    
    def verify_selected_item_in_the_left_navigation_bar(self, item_list, msg):
        """
        Desc: Verifies the selected item in left navigation bar
        usage: verify_selected_item_in_the_left_navigation_bar(['Page 1'],'Step 1.2: ')
        """
        self._three_level_sidebar.verify_selected_top_folder_item(item_list, msg)
    
    def select_item_from_left_navigation_bar(self, folder_name):
        """
        Desc: Selects the item from the left naigation bar
        usage: select_item_from_left_navigation_bar('Page 1')
        """
        self._three_level_sidebar.select_top_folder_item(folder_name)
        
    def click_new_page_from_left_navigation_bar(self):
        """
        Desc: Used to click the '+' icon on the navigation bar to add a new page
        usage: click_new_page_from _left_navigation_bar()
        """
        self._three_level_sidebar.click_on_new_page_from_top_folder_item()
    
    def verify_new_page_plus_icon_from_left_navigation_bar(self, msg):
        """
        Desc: Used to verify the '+' icon on the navigation bar to add a new page
        usage: verify_new_page_plus_icon_from_left_navigation_bar('Step 9 Verify')
        """
        self._three_level_sidebar.verify_plus_sign_from_top_folder_item(msg)
       
    def rename_page_from_left_navigation_bar(self, item_name, name_to_change):
        """
        Desc: Used to change the folder or item name on the left navigation bar
        usage: rename_page_from_left_navigation_bar('Page 1','Content page')
        """
        self._three_level_sidebar.rename_page_name_from_top_folder(item_name, name_to_change)
        
class Two_Level_Top(Portal, Canvas, Share_With_Others_Window, New_Page_Template_Window):
    
    """ Inherit attributes of the parent class =  Common_Portal, Canvas"""
    def __init__(self, driver):
        super(Two_Level_Top, self).__init__(driver)