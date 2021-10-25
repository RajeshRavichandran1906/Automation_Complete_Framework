from common.lib import utillity
from common.lib.base import BasePage
from configparser import ConfigParser
from selenium.webdriver.support import expected_conditions as EC
import os, time, re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color
from common.pages import visualization_resultarea
from common.locators import root_path
import sys
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard

class Vfour_Portal_Properties(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Vfour_Portal_Properties, self).__init__(driver)
        
    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
    
    def get_vbox_object(self, parent_css, bihbox_item_name): 
        '''
        This function return the index number of bihbox_item_name in Property section.
        :param parent_css = "[id^='idProperties']:not([style*='hidden'])"
        :param bihbox_item_name="page icon" or any item name 
        :usage get_vbox_object("[id^='idProperties']:not([style*='hidden'])", 'Page Icon')
        '''  
        if bool(re.match('(.+)\s[U|u]nit$',bihbox_item_name)):
            bihbox_item_name = re.match('(.+)\s[U|u]nit$',bihbox_item_name).group(1) 
        if bool(re.match('[a-zA-Z]*.*(%)$',bihbox_item_name)):
            bihbox_item_name = '%'
        if bool(re.match('^[E|e]asy\s[s|S]elector\s(.+)',bihbox_item_name)):
            bihbox_item_name = re.match('^[E\e]asy\s[s|S]elector\s(.+)',bihbox_item_name).group(1)
        vbox_css=parent_css + " [id^='BIPTab']:not([style*='hidden']) div[id^='PropertiesCluster']  > div[id^='BiHBox']  > div[id*='Box']:not([style*='hidden'])"
        elems=self.driver.find_elements_by_css_selector(vbox_css)
        return(elems[[bihbox_item_name in el1 for el1 in [el.text.strip() for el in elems]].index(True)])
        
    def edit_input_control(self, property_section, bihbox_item_name, input_control, **kwargs):
        """
        This function is used to Edit/select all control in property section.
        :param property_section='pageview' or 'page'            ''' To know property_section check 'vfour_properties.data' file '''
        :param bihbox_item_name="page icon" or any item name 
        :param input_control='checkbox' or 'radoibutton' or 'combobox' or 'textbox'
        :kwargs['textbox_input']='textbox value'
        :kwargs['combobox_input']='combobox value'
        :kwargs['checkbox_input']='check' OR 'uncheck'                 
        :kwargs['msg'] = 'some massage to print'
        :usage edit_input_control('page', 'page icon', 'checkbox')
            OR
        :usage edit_input_control('page', 'Container Defaults', 'button')
        """
        bihbox_item_name1 = bihbox_item_name.lower()
        vfour_properties_file=os.path.join(root_path.ROOT_PATH, 'vfour_properties.data')
        parser = ConfigParser()
        parser.optionxform=str
        parser.read(vfour_properties_file)
        parent_css="[id^='idProperties']:not([style*='hidden'])"
        elem=Vfour_Portal_Properties.get_vbox_object(self, parent_css, bihbox_item_name)
        if input_control == 'checkbox':
            checkbox_elems=elem.find_elements_by_css_selector("div[id^='BiCheckBox']:not([style*='hidden'])")
            if bihbox_item_name1 in ('hide new page','hide link to page', 'page icon', 'panel icons', 'hide new area', 'hide new tab'):
                checkox_index = parser[property_section][bihbox_item_name1 + " checkbox"]
                elem=checkbox_elems[int(checkox_index)]
            else:
                elem=checkbox_elems[[el.text.strip() for el in checkbox_elems].index(bihbox_item_name)]
            try:
                elem.find_element_by_css_selector("input[checked]")
                current_status=True
            except NoSuchElementException:
                current_status=False
            verify_status=False if kwargs['checkbox_input']=='check' else True
            verify_status_msg='UnCheck' if kwargs['checkbox_input']=='check' else 'Check'
            utillity.UtillityMethods.asequal(self, current_status, verify_status, kwargs['msg']+": Verify the "+bihbox_item_name+" default status "+verify_status_msg+".")
            utillity.UtillityMethods.default_click(self, elem)
        elif input_control == 'combobox':
            combobox_index = parser[property_section][bihbox_item_name1 + " combobox"]
            combobox_elems=elem.find_elements_by_css_selector("div[id^='BiComboBox']:not([style*='hidden']) div[id^='BiButton']")
            utillity.UtillityMethods.select_any_combobox_item(self, combobox_elems[int(combobox_index)], kwargs['combobox_input'])
        elif input_control == 'textbox':
            textbox_index = parser[property_section][bihbox_item_name1 + " textbox"]
            textbox_elems=elem.find_elements_by_css_selector("input[type=text]")
            utillity.UtillityMethods.set_text_to_textbox_using_keybord(self, kwargs['textbox_input'], text_box_elem=textbox_elems[int(textbox_index)])
            visualization_resultarea.Visualization_Resultarea.wait_for_property(self, None, None, expire_time=90, text_option='text_value', string_value=kwargs['textbox_input'], parent_object=textbox_elems[int(textbox_index)])
        elif input_control == 'button':
            button_elems = elem.find_elements_by_css_selector("div[id^='BiButton'] [class*='button']")
            elem=button_elems[[el.text.strip() for el in button_elems].index(bihbox_item_name)]
            utillity.UtillityMethods.default_click(self, elem)
        elif input_control == 'panel_area':
            tools_list = ['add', 'edit', 'delete', 'move_up', 'move_down']
            for tool in tools_list:
                try:
                    verify_tool = elem.find_element_by_css_selector("[id^='BiImage'][src*='"+tool+"']").is_displayed()
                except NoSuchElementException:
                    print(tool+" Image is missing from Area tools.")
                utillity.UtillityMethods.asequal(self, True, verify_tool, "Step X: Verify Panel Area tool "+tool+" is Displayed.")
        elif input_control == 'menu_area':
            try:
                menu_list=elem.find_element_by_css_selector("table tr td")
                utillity.UtillityMethods.default_click(self, menu_list)
                time.sleep(1)
                if sys.platform == 'linux':
                    pykeyboard.press_key(pykeyboard.control_key)
                    pykeyboard.tap_key(character=u'\u0061')
                    pykeyboard.release_key(pykeyboard.control_key)
                else:
                    keyboard.send('ctrl+a')
                menu_button = 'add' if 'add' in kwargs else 'remove' if 'remove' in kwargs else 'none'
                try:
                    elem = self.driver.find_element_by_css_selector("[id^='BiImage'][src*='"+menu_button+"']")
                    utillity.UtillityMethods.default_click(self, elem)
                except NoSuchElementException:
                    print(menu_button+" Button not found.")
            except NoSuchElementException:
                print("Available Menu option is not found.")
        elif input_control == 'sort_menu':
            try:
                menu_list=elem.find_element_by_css_selector("table tr td")
                utillity.UtillityMethods.default_click(self, menu_list)
                time.sleep(1)
                menu_button = 'up' if 'up' in kwargs else 'down' if 'down' in kwargs else 'none'
                try:
                    elem = self.driver.find_element_by_css_selector("[id^='BiImage'][src*='move_"+menu_button+"']")
                    utillity.UtillityMethods.default_click(self, elem)
                except NoSuchElementException:
                    print("Move_"+menu_button+" Button not found.")
            except NoSuchElementException:
                print("Selected Menu option is not found.")
        else:
            print("Please pass input control")
        time.sleep(2)
        
    def verify_input_control(self, property_section, bihbox_item_name, input_control, msg, **kwargs):
        """
        This function is used to verify all control in property section.
        :param property_section='pageview' or 'page'            ''' To know property_section check 'vfour_properties.data' file '''
        :param bihbox_item_name="page icon" or any item name 
        :param input_control='checkbox' or 'radoibutton' or 'combobox' or 'textbox'
        :param msg = 'some massage to print'
        :kwargs['textbox_input']='textbox value'
        :kwargs['combobox_value']='combobox value'
        :kwargs['checkbox_input']='check' OR 'uncheck'
        :usage verify_input_control('page', 'page icon', 'checkbox', "Step 1: Verify page icon checked")
            OR
        :usage verify_input_control('page', 'Container Defaults', 'button', "Step 1: Verify 'Container Defaults' button is displayed.")
        """
        step_number = re.search(r'\d+', msg).group()
        bihbox_item_name1 = bihbox_item_name.lower()
        vfour_properties_file = os.path.join(root_path.ROOT_PATH, 'vfour_properties.data')
        #vfour_properties_file=os.getcwd() + "\\common\\locators\\vfour_properties.data"
        parser = ConfigParser()
        parser.optionxform=str
        parser.read(vfour_properties_file)
        parent_css="[id^='idProperties']:not([style*='hidden'])"
        elem=Vfour_Portal_Properties.get_vbox_object(self, parent_css, bihbox_item_name)
        if input_control == 'checkbox':
            checkbox_elems=elem.find_elements_by_css_selector("div[id^='BiCheckBox']:not([style*='hidden'])")
            if bihbox_item_name1 in ('hide new page','hide link to page', 'page icon', 'panel icons', 'hide new area', 'hide new tab'):
                checkox_index = parser[property_section][bihbox_item_name1 + " checkbox"]
                elem=checkbox_elems[int(checkox_index)]
            else:
                elem=checkbox_elems[[el.text.strip() for el in checkbox_elems].index(bihbox_item_name)]
            try:
                elem.find_element_by_css_selector("input[checked]")
                current_status=True
            except NoSuchElementException:
                current_status=False
            verify_status=True if kwargs['checkbox_input']=='check' else False
            utillity.UtillityMethods.asequal(self, current_status, verify_status, msg)
        elif input_control == 'combobox':
            combobox_index = parser[property_section][bihbox_item_name1 + " combobox"]
            combobox_elems=elem.find_elements_by_css_selector("div[id^='BiComboBox']:not([style*='hidden'])")
            actual_comboitem=combobox_elems[int(combobox_index)].text.replace('\n', '').strip()
            utillity.UtillityMethods.asequal(self, actual_comboitem, kwargs['combobox_value'], msg)
        elif input_control == 'textbox':
            textbox_index = parser[property_section][bihbox_item_name1 + " textbox"]
            textbox_elems=elem.find_elements_by_css_selector("input[type='text']")
            actual_textitem=textbox_elems[int(textbox_index)].get_attribute('value')
            utillity.UtillityMethods.asequal(self, actual_textitem, kwargs['textbox_value'], msg)
        elif input_control == 'button':
            button_elems = elem.find_elements_by_css_selector("div[id*='Button'] [class*='button']")
            elem=button_elems[[el.text.strip() for el in button_elems].index(bihbox_item_name)]
            utillity.UtillityMethods.asequal(self, elem.text, bihbox_item_name, msg)
            utillity.UtillityMethods.verify_object_visible(self, "pass", kwargs['elem_visible'], "Step "+step_number+".a: Verify "+ bihbox_item_name + " Visible in Page.", elem_obj=elem)
        elif input_control == 'text':
            actual_list = elem.text.strip().split('\n')
            utillity.UtillityMethods.asequal(self, actual_list, kwargs['text_list'], msg)
        elif input_control == 'image':
            image_elem = elem.find_element_by_css_selector("img")
            image_elem_src = utillity.UtillityMethods.get_attribute_value(self, image_elem, 'src')
            print(image_elem_src)
            utillity.UtillityMethods.asin(self, kwargs['page_icon_image_name'], image_elem_src['src'], msg)
        elif input_control == 'panel_area':
            tools_list = ['add', 'edit', 'delete', 'move_up', 'move_down']
            for tool in tools_list:
                try:
                    verify_tool = elem.find_element_by_css_selector("[id^='BiImage'][src*='"+tool+"']").is_displayed()
                except NoSuchElementException:
                    print(tool+" Image is missing from Area tools.")
                utillity.UtillityMethods.asequal(self, True, verify_tool, "Step "+step_number+".a: Verify "+tool+" Image is displayed within Area tools.")
            area_elems = elem.find_elements_by_css_selector("table tr")
            actual_list = [elem_text for elem_text in [elem.text.strip() for elem in area_elems] if elem_text != '']
            utillity.UtillityMethods.as_List_equal(self, actual_list, kwargs['area_list'], msg)
        else:
            print("Please pass input control")
    
    def verify_input_control_enable_or_disable(self, property_section, bihbox_item_name, input_control, msg, **kwargs):
        """
        This function is similar to verify_input_control function. But here we will verify only enable or disable in property.
        :param property_section='pageview' or 'page'            ''' To know property_section check 'vfour_properties.data' file '''
        :param bihbox_item_name="page icon" or any item name 
        :param input_control='checkbox' or 'radoibutton' or 'combobox' or 'textbox'
        :param msg = 'some massage to print'
        :kwargs['enable_status']='enabled' or 'disabled'
        :kwargs['enable_value']=True or False
        :usage verify_element_property('page', 'page icon', 'checkbox', "Step 1: Verify page icon checked", enable_status='disabled', enable_value=True)
            OR
        :usage verify_element_property('page', 'page icon', 'checkbox', "Step 1: Verify page icon checked", enable_status='disabled', enable_value=False)
        """
        bihbox_item_name1 = bihbox_item_name.lower()
        vfour_properties_file = os.path.join(root_path.ROOT_PATH, 'vfour_properties.data')
        #vfour_properties_file=os.getcwd() + "\\common\\locators\\vfour_properties.data"
        parser = ConfigParser()
        parser.optionxform=str
        parser.read(vfour_properties_file)
        parent_css="[id^='idProperties']:not([style*='hidden'])"
        elem=Vfour_Portal_Properties.get_vbox_object(self, parent_css, bihbox_item_name)
        if input_control == 'checkbox':
            checkbox_elems=elem.find_elements_by_css_selector("div[id^='BiCheckBox']:not([style*='hidden'])")
            if bihbox_item_name1 in ('hide new page','hide link to page', 'page icon', 'panel icons', 'hide new area', 'hide new tab'):
                checkox_index = parser[property_section][bihbox_item_name1 + " checkbox"]
                elem=checkbox_elems[int(checkox_index)]
            else:
                elem=checkbox_elems[[el.text.strip() for el in checkbox_elems].index(bihbox_item_name)]
            try:
                if kwargs['enable_status'] == 'disabled':
                    current_status=elem.find_element_by_css_selector("input").get_property(kwargs['enable_status'])
                else:
                    current_status=elem.find_element_by_css_selector("input").is_enabled()
            except NoSuchElementException:
                current_status='none'
            actual_color = Color.from_string(elem.value_of_css_property('color')).rgba
            utillity.UtillityMethods.asequal(self, current_status, kwargs['enable_value'], msg)
        elif input_control == 'combobox':
            combobox_index = parser[property_section][bihbox_item_name1 + " combobox"]
            combobox_elems=elem.find_elements_by_css_selector("div[id^='BiComboBox']:not([style*='hidden'])")
            actual_comboitem = combobox_elems[int(combobox_index)].get_property(kwargs['enable_status'])
            actual_color = Color.from_string(combobox_elems[int(combobox_index)].value_of_css_property('color')).rgba
            utillity.UtillityMethods.asequal(self, actual_comboitem, kwargs['enable_value'], msg)
        elif input_control == 'textbox':
            textbox_index = parser[property_section][bihbox_item_name1 + " textbox"]
            textbox_elems=elem.find_elements_by_css_selector("input[type=text]")
            actual_textitem=textbox_elems[int(textbox_index)].get_property(kwargs['enable_status'])
            actual_color = Color.from_string(textbox_elems[int(textbox_index)].value_of_css_property('color')).rgba
            utillity.UtillityMethods.asequal(self, actual_textitem, kwargs['enable_value'], msg)
        elif input_control == 'button':
            button_elems = elem.find_elements_by_css_selector("div[id^='BiButton'] [class*='button']")
            button_elem=button_elems[[el.text.strip() for el in button_elems].index(bihbox_item_name)]
            actual_status = button_elem.get_property(kwargs['enable_status'])
            actual_color = Color.from_string(button_elem.value_of_css_property('color')).rgba
            utillity.UtillityMethods.asequal(self, actual_status, kwargs['enable_value'], msg)
        else:
            print("Please pass input control")
        if kwargs['enable_status'] == 'disabled':
            expected_color = utillity.UtillityMethods.color_picker(self, kwargs['color_name'], rgb_type='rgba')
            utillity.UtillityMethods.asequal(self, expected_color, actual_color, "Step X: Verify "+bihbox_item_name+" is Gray color.")
            
    def select_property_tab(self, tab_name):
        """
        This function is used to select tab in Property section.
        :param tab_name='Properties' or 'Title' or 'Content'
        :Usage select_property_tab('Properties')
        """
        tab_css="[id^='idProperties']:not([style*='hidden']) [id^='BiTabBar'] [id^='BiTabButton']" 
        elems=self.driver.find_elements_by_css_selector(tab_css)  
        tab_elem = elems[[el.text.strip() for el in elems].index(tab_name)]
        utillity.UtillityMethods.default_click(self, tab_elem)

    def select_breadcrumb_panel(self, panle_name, **kwargs):
        """
        This function is used to select bread crumb option.
        :Param panle_name='BIP_xxx_Portal123_V41' or 'Page 1'
        :kwargs['next']=your item to be selected                        ''' This will select option form arrow mark. ''' 
        :Usage select_breadcrumb_panel('BIP_xxx_Portal123_V4')
            OR
        :Usage select_breadcrumb_panel('BIP_xxx_Portal123_V4', next='Pages')
        """
        panel_css="#BreadCrumbPanelID > [id^='Bi'][id*='MenuButton']"
        elems=self.driver.find_elements_by_css_selector(panel_css) 
        elem_index=[el.text.strip() for el in elems].index(panle_name)
        if 'next' in kwargs:
            utillity.UtillityMethods.default_click(self, elems[elem_index+1])
            time.sleep(2)
            utillity.UtillityMethods.select_or_verify_bipop_menu(self, kwargs['next'])
        else: 
            utillity.UtillityMethods.default_click(self, elems[elem_index])
        time.sleep(2)
    
    def verify_breadcrumb_panel(self, panle_name, expected_element, msg, **kwargs):
        """
        This function is used to select bread crumb option.
        :Param panle_name='BIP_xxx_Portal123_V41' or 'Page 1'
        :kwargs['next']=your item to be selected                        ''' This will select option form arrow mark. ''' 
        :Usage select_breadcrumb_panel('BIP_xxx_Portal123_V4')
            OR
        :Usage select_breadcrumb_panel('BIP_xxx_Portal123_V4', next='Pages')
        """
        panel_css="#BreadCrumbPanelID > [id^='Bi'][id*='MenuButton']"
        elems=self.driver.find_elements_by_css_selector(panel_css) 
        elem_index=[el.text.strip() for el in elems].index(panle_name)
        if 'next' in kwargs:
            utillity.UtillityMethods.default_click(self, elems[elem_index+1])
            time.sleep(2)
            utillity.UtillityMethods.select_or_verify_bipop_menu(self, kwargs['next'])
        time.sleep(2)
        elems=self.driver.find_elements_by_css_selector(panel_css) 
        actual_element=[elem for elem in [el.text.strip().replace('>','') for el in elems if el != ''] if elem != '']
        utillity.UtillityMethods.as_List_equal(self, expected_element, actual_element, msg)
        
    def manage_container_defaults_popup(self, input_control, item_name, verification=True, **kwargs):
        """
        This function to handle Container Defaults dialog, Verify or select the appropriate options.
        :param: input_control = "checkbox" or "textbox" or "button"
        :param: item_name = 'width' or 'Reset to Default' or 'Move'
        :kwarg :param: verification = True or False    ''' 'Verify=True if user need only verification', 'Verify=False if user need only verification'  '''
        :kwargs['msg'] = "Step 9: Verify Move option selected."
        :kwargs['checkbox_input'] = "check" or "uncheck"
        :kwargs['textbox_value'] = '440' or any number as per condition
        :Usage manage_container_defaults_popup("checkbox", "Move", verify = True, msg="Step 9: Verify Move option selected.")
            OR
        :Usage manage_container_defaults_popup("button", "Ok", verification=False)
        """
        parent_css = "#idContainerDefaults [class*='active']"
        textbox_css = parent_css + " [id^='BiGridPanel'] [id^='BiHBox'] input[type='text']"
        CheckBox_Css = parent_css + " [id^='BiGridPanel'] [id^='BiHBox'] div[id^='BiVBox']:not([style*='hidden']) div[id^='BiCheckBox']:not([style*='hidden'])"
        button_CSS = parent_css + " [id^='BiGridPanel'] [id^='BiHBox'] [id^='BiButton']:not([class*='spinner'])"
        if verification == True:
            if input_control == 'checkbox':
                checkbox_elems=self.driver.find_elements_by_css_selector(CheckBox_Css)
                elem=checkbox_elems[[el.text.strip() for el in checkbox_elems].index(item_name)]
                try:
                    elem.find_element_by_css_selector("input[checked]")
                    current_status=True
                except NoSuchElementException:
                    current_status=False
                verify_status=True if kwargs['checkbox_input']=='check' else False
                utillity.UtillityMethods.asequal(self, current_status, verify_status, kwargs['msg'])
            elif input_control == 'textbox':
                textbox_index = 0 if item_name == 'Width' else 1 if item_name == 'Height' else 'none'
                textbox_elems=self.driver.find_elements_by_css_selector(textbox_css)
                actual_text=textbox_elems[textbox_index].get_attribute('value')
                utillity.UtillityMethods.asequal(self, actual_text, kwargs['textbox_value'], kwargs['msg'])
            elif input_control == 'button':
                button_elems = self.driver.find_elements_by_css_selector(button_CSS)
                actual_text=button_elems[[el.text.strip() for el in button_elems].index(item_name)].text.strip()
                utillity.UtillityMethods.asequal(self, item_name, actual_text, kwargs['msg'])
            else:
                print("Please pass input control")
        else:
            if input_control == 'checkbox':
                checkbox_elems=self.driver.find_elements_by_css_selector(CheckBox_Css)
                elem=checkbox_elems[[el.text.strip() for el in checkbox_elems].index(item_name)]
                try:
                    elem.find_element_by_css_selector("input[checked]")
                    current_status=True
                except AttributeError:
                    current_status=False
                verify_status=True if kwargs['checkbox_input']=='check' else False
                utillity.UtillityMethods.asequal(self, current_status, verify_status, kwargs['msg'])
                utillity.UtillityMethods.default_click(self, elem)
            elif input_control == 'textbox':
                textbox_index = 0 if item_name == 'width' else 1 if item_name == 'height' else 'none'
                textbox_elems=self.driver.find_elements_by_css_selector(textbox_css)
                utillity.UtillityMethods.set_text_to_textbox_using_keybord(self, kwargs['textbox_value'], text_box_elem=textbox_elems[int(textbox_index)])
                visualization_resultarea.Visualization_Resultarea.wait_for_property(self, None, None, expire_time=90, text_option='text_value', string_value=kwargs['textbox_value'], parent_object=textbox_elems[int(textbox_index)])
            elif input_control == 'button':
                button_elems = self.driver.find_elements_by_css_selector(button_CSS)
                elem=button_elems[[el.text.strip() for el in button_elems].index(item_name)]
                utillity.UtillityMethods.default_click(self, elem)
            else:
                print("Please pass input control")
    
    def manage_responsive_properties_popup(self, item_name, input_control, verification=True, **kwargs):
        """
        This function is used to manage responsive properties popup window
        :param item_name='custom css classes'
        :param item_name='textbox'
        :param verification=True or False             ''' verification=True if only need to verify Responsive Properties PopUp; Otherwise verification=False to edit the elements.'''
        :kwargs combobox_value='Auto'
        :kwargs textbox_value='auto'
        :kwargs textbox_input='auto'
        :kwargs msg='Step 9: Verify 'Ok' button visible in Responsive Properties window.'
        :Usage manage_responsive_properties_popup('custom css classes', 'textbox', verification=True, textbox_value='bip-container', msg='Step 7:')
        """
        parent_css = "#flexItemPropertyDialog [class*='active']"
        hbox_css = parent_css + " [id^='BiHBox']:not([style*='hidden'])"
        combobox_css = parent_css + "  [id^='BiComboBox'] [id^='BiButton']" 
        elems=self.driver.find_elements_by_css_selector(hbox_css)
        vfour_properties_file = os.path.join(root_path.ROOT_PATH, 'vfour_properties.data')
        #vfour_properties_file=os.getcwd() + "\\common\\locators\\vfour_properties.data"
        parser = ConfigParser()
        parser.optionxform=str
        parser.read(vfour_properties_file)
        item_name1 = item_name.lower()
        if bool(re.match('(.+)\s[W|w]idth$',item_name)):
            item_name = re.match('(.+)\s[W|w]idth$',item_name).group(1)
        elif bool(re.match('(.+)\s[H|h]eight$',item_name)):
            item_name = re.match('(.+)\s[H|h]eight$',item_name).group(1)
        if verification==True:
            if input_control == 'combobox':
                actual_combobox_item = self.driver.find_element_by_css_selector("#flexItemPropertyDialog [class*='active'] [id^='BiComboBox']").text.strip()
                utillity.UtillityMethods.asequal(self, actual_combobox_item, kwargs['combobox_value'], kwargs['msg'])
            elif input_control == 'textbox':
                elem = elems[[item_name in el1 for el1 in [el.text.strip() for el in elems]].index(True)]
                textbox_index = parser['responsive_properties'][item_name1 + " textbox"]
                textbox_elems=elem.find_elements_by_css_selector("input[type=text]")
                actual_textitem=textbox_elems[int(textbox_index)].get_attribute('value')
                utillity.UtillityMethods.asequal(self, actual_textitem, kwargs['textbox_value'], kwargs['msg'])
            elif input_control == 'button':
                elem = elems[[item_name in el1 for el1 in [el.text.strip() for el in elems]].index(True)]
                button_elems=elem.find_elements_by_css_selector("[id^='BiButton']")
                elem_list=[el.text.strip() for el in button_elems]
                utillity.UtillityMethods.asin(self, item_name, elem_list, kwargs['msg'])
            else:
                print("Please pass appropriate input control option.")
        else:
            if input_control == 'combobox':
                combo_btn_elem = self.driver.find_element_by_css_selector(combobox_css)
                utillity.UtillityMethods.select_any_combobox_item(self, combo_btn_elem, item_name)
            elif input_control == 'textbox':
                elem = elems[[item_name in el1 for el1 in [el.text.strip() for el in elems]].index(True)]
                textbox_index = parser['responsive_properties'][item_name1 + " textbox"]
                textbox_elems=elem.find_elements_by_css_selector("input[type=text]")
                utillity.UtillityMethods.set_text_to_textbox_using_keybord(self, kwargs['textbox_input'], text_box_elem=textbox_elems[int(textbox_index)])
                visualization_resultarea.Visualization_Resultarea.wait_for_property(self, None, None, expire_time=90, text_option='text_value', string_value=kwargs['textbox_input'], parent_object=textbox_elems[int(textbox_index)])
            elif input_control == 'button':
                elem = elems[[item_name in el1 for el1 in [el.text.strip() for el in elems]].index(True)]
                button_elems=elem.find_elements_by_css_selector("[id^='BiButton']")
                elem=button_elems[[el.text.strip() for el in button_elems].index(item_name)]
                utillity.UtillityMethods.default_click(self, elem)
            else:
                print("Please pass appropriate input control option.")