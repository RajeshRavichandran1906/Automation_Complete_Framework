from common.locators import vfive_designer
from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods as utill_obj
from common.lib.core_utility import CoreUtillityMethods as core_utill_obj
from common.pages.wf_mainpage import Wf_Mainpage as home_page

class Vfive_portal_page(BasePage):
    
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Vfive_portal_page, self).__init__(driver)
    
    def create_vfive_portal(self, portal_name, folder_path, navigation_type, expire_time=90):
        if navigation_type.lower() not in ['two_level_side', 'three_level', 'two_level_top']:
            raise IndexError("Please pass navigation_type value 'two_level_side', 'three_level' or 'two_level_top'.")
        home_page.select_left_panel(self, 'content')
        home_page.expand_repository_folders(self, folder_path)
        home_page.select_action_bar_button(self, 'Designer')
        home_page.select_ribbon_button(self, 'Portal')
        utill_obj.synchronize_with_number_of_element(self, vfive_designer.Vfive_Designer.title_textbox_input_css, 1, expire_time)
        utill_obj.set_text_to_textbox_using_keybord(self, portal_name, text_box_css=vfive_designer.Vfive_Designer.title_textbox_input_css)
        utill_obj.synchronize_with_visble_text(self, vfive_designer.Vfive_Designer.title_textbox_input_css, portal_name, expire_time, text_option='text_value')
        button_name_elem = utill_obj.validate_and_get_webdriver_object(self, vfive_designer.Vfive_Designer.create_button_css, 'Create Button')
        core_utill_obj.left_click(self, button_name_elem)
    
    def verify_vfive_portal_create_dialog(self, button_name):
        Vfive_portal_page.close_vfive_portal_create_dialog(self, button_name)
    
    def close_vfive_portal_create_dialog(self, button_name):
        if button_name.lower() not in ['cancel', 'close']:
            raise IndexError("Please pass button_name value 'Cancel' or 'Close'.")
        if button_name.lower() == 'cancel':
            button_name_elem = utill_obj.validate_and_get_webdriver_object(self, vfive_designer.Vfive_Designer.cancle_button_css, button_name)
        else:
            button_name_elem = utill_obj.validate_and_get_webdriver_object(self, vfive_designer.Vfive_Designer.close_button_css, button_name)
        core_utill_obj.left_click(self, button_name_elem)
    
    def run_vfive_portal(self, portal_path):
        portal_item_path = portal_path.split('->')
        home_page.select_left_panel(self, 'content')
        home_page.select_repository_folder_item_context_menu(self, portal_item_path[-1], context_menu_item_path='Run', folder_path=portal_item_path[:-1], click_option='right_click')
        core_utill_obj.switch_to_new_window(self)
        
    def close_vfive_portal_run_window(self):
        core_utill_obj.switch_to_previous_window(self)