import time, pyautogui
from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods as utillobject
from common.lib.javascript import JavaScript
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from common.lib.global_variables import Global_variables

class Infoapps_Left_Panel(BasePage):
    """ Inherit attributes of the parent class = Baseclass """
    
    leftpanel_css='form.IBI_ReportControlPanel'
    toppanel_css='form.IBI_ReportControlPanel div'
    
    def __init__(self, driver):
        super(Infoapps_Left_Panel, self).__init__(driver)
    
    def get_position_of_label(self, label_name, top_panel=False):
        index=-1
        if top_panel == True:
            label_css=Infoapps_Left_Panel.toppanel_css + ' > label'
        else:
            label_css=Infoapps_Left_Panel.leftpanel_css + ' > label'
        label_description='Labels within infoapps controlpanel'
        label_elements=utillobject.validate_and_get_webdriver_objects(self, label_css, label_description)
        for label_element in label_elements:
            index = index + 1
            if label_element.text.lower().strip() == label_name.lower():
                break
        if index != -1:
            return index
        else:
            raise_msg='Requested label [' + label_name + '] is not displaying within infoapps controlpanel.'
            raise ValueError(raise_msg)
    
    def get_required_combo_element(self, corresponding_label_name, top_panel=False):
        required_combo_element_index=Infoapps_Left_Panel.get_position_of_label(self, corresponding_label_name, top_panel=top_panel)
        if top_panel == True:
            label_css=Infoapps_Left_Panel.toppanel_css + ' > select'
        else:
            label_css=Infoapps_Left_Panel.leftpanel_css + ' > select'
        label_description='combo element within infoapps controlpanel'
        label_elements=utillobject.validate_and_get_webdriver_objects(self, label_css, label_description)
        if required_combo_element_index < len(label_elements):
            return label_elements[required_combo_element_index]
        else:
            raise_msg='Requested label [' + corresponding_label_name + '] is not displaying within infoapps controlpanel.'
            raise ValueError(raise_msg)
        
    def select_combo_item(self, label_name, item_name, top_panel=False):
        required_combo_element=Infoapps_Left_Panel.get_required_combo_element(self, label_name, top_panel=top_panel)
        required_combo_element.click()
        time.sleep(2)
        if top_panel == True:
            item_css=Infoapps_Left_Panel.toppanel_css + ' > select > option'
        else:
            item_css=Infoapps_Left_Panel.leftpanel_css + ' > select > option'
        item_description='combo items within infoapps controlpanel'
        item_elements=utillobject.validate_and_get_webdriver_objects(self, item_css, item_description)
        item=item_elements[[elem.text.strip() for elem in item_elements].index(item_name)]
        item.click()
        
    def select_listbox_item(self, listbox_index, item_list):
        for item1 in item_list:
            listbox_css=Infoapps_Left_Panel.leftpanel_css +" > select#listbox"+str(listbox_index)+" > option"
            listbox_description='listbox element within infoapps controlpanel'
            listbox_elements=utillobject.validate_and_get_webdriver_objects(self, listbox_css, listbox_description)
            if Global_variables.browser_name in ['firefox', 'chrome']:
                ActionChains(self.driver).move_to_element(listbox_elements[0]).click().perform()
            else:    
                listbox_elements[0].click()
            time.sleep(2)
            tmp_list=[el.text.strip() for el in listbox_elements]
            for item2 in tmp_list:
                if item1 == item2:
                    return 1
                else:
                    if Global_variables.browser_name in ['firefox']:
                        pyautogui.hotkey('down')
                    else:
                        action = ActionChains(self.driver)
                        action.send_keys(keys.Keys.ARROW_DOWN).perform()
    
    def click_run_option_button(self, button_name, top_panel=False):
        """
        params: button_name: 'run' OR 'reset', OR 'defer' OR 'schedule'
        Syntax: click_run_option_button('run')
        """
        if top_panel == True:
            menu_btn_css="form.IBI_ReportControlPanel div > input[class^='IBI_button IBI_btn-"+button_name+"']"
        else:
            menu_btn_css="form.IBI_ReportControlPanel > input[class^='IBI_button IBI_btn-"+button_name+"']"
        menu_btn_description='Run option button '+button_name+' in infoapps controlpanel'
        menu_btn=utillobject.validate_and_get_webdriver_object(self, menu_btn_css, menu_btn_description)
        menu_btn.click()
        time.sleep(2)
    
    def verify_from_date(self, expected_from_date_value, msg):
        from_date_css=Infoapps_Left_Panel.leftpanel_css + " > input[id='calendar1']"
        from_date_description='From date in Calender1 within infoapps controlpanel'
        from_date_obj=utillobject.validate_and_get_webdriver_object(self, from_date_css, from_date_description)
        actual_from_date_value=from_date_obj.get_attribute('value')
        utillobject.asequal(self, actual_from_date_value, expected_from_date_value, msg)
    
    def verify_to_date(self, expected_to_date_value, msg):
        to_date_css=Infoapps_Left_Panel.leftpanel_css + " > input[id='calendar2']"
        to_date_description='To date in Calender2 within infoapps controlpanel'
        to_date_obj=utillobject.validate_and_get_webdriver_object(self, to_date_css, to_date_description)
        actual_to_date_value=to_date_obj.get_attribute('value')
        utillobject.asequal(self, actual_to_date_value, expected_to_date_value, msg)
        
    def verify_combo_item(self, label_name, item_name):
        pass
    
    def select_group_items(self, label_name, *item_names):
        pass
    
    def verify_group_items(self, label_name, *item_names):
        pass
    
    def select_from_date(self, day, month, year):
        pass
    
    def set_from_date(self, formatted_date_string):
        pass
    
    def select_to_date(self, day, month, year):
        pass
    
    def set_to_date(self, formatted_date_string):
        pass    
        
        