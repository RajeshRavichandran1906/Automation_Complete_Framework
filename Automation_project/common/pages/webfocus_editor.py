from selenium.common.exceptions import ElementNotVisibleException
import time
import os
import sys
from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods as utillobject
from common.lib.core_utility import CoreUtillityMethods
from common.pages.wf_mainpage import Wf_Mainpage
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard

class WebfocusEditor(BasePage) :
    parent_textarea_css = 'div.wf-ace-text-editor'
    parent_line_number_css = parent_textarea_css + ' .ace_gutter-layer'
    first_tab_focexec_name_css = 'div.ibx-csl-items-box .ibx-csl-item'
    menu_bar_buttons_css = ".te-menu-bar div[class*='te-menu-button'][title]"
    file_menu_button_css=".te-menu-bar div[data-ibx-name='_menuFile']"
    search_and_replace_parent_css=".te-search-panel"
    textarea_input_css=parent_textarea_css+" .ace_content"
    textarea_text_line_css = textarea_input_css + " .ace_text-layer .ace_line"
    
    def __init__(self, driver):
        '''
        constructor
        '''
        super(WebfocusEditor, self).__init__(driver)
        self._core_utill=CoreUtillityMethods(self.driver)
        self._wf_mainpage = Wf_Mainpage(self.driver)
        self._utils = utillobject(self.driver)
    
    def get_menu_bar_buttons_object(self):
        '''
        This function will return the list of top menu bar button objects which is displayed that means clickable.
        Example : Save, Run
        '''
        menu_bar_buttons_object = utillobject.validate_and_get_webdriver_objects(self, self.menu_bar_buttons_css, "Autoprompt fieled labels")
        menu_bar_buttons_object_list = [obj for obj in menu_bar_buttons_object if obj.is_displayed()]
        return menu_bar_buttons_object_list
    
    def get_file_menu_button_object(self):
        '''
        This function will return file menu button object which is in top menu bar. 
        '''
        file_menu_button_object=utillobject.validate_and_get_webdriver_object(self, self.file_menu_button_css, 'File menu button')
        return file_menu_button_object
        
    def get_menu_bar_buttons_name(self):
        '''
        This function will return menu bar button's name such as Save, Help
        '''
        menu_button_objects=self.get_menu_bar_buttons_object()
        menu_button_name_list = [button.get_attribute('title') for button in menu_button_objects] 
        return menu_button_name_list
    
    def get_menu_bar_button_object(self, button_name):
        '''
        This function will return menu bar button object which is in clickable or enable mode.
        '''
        menu_button_objects=self.get_menu_bar_buttons_object()
        menu_button_name_list = self.get_menu_bar_buttons_name()
        if button_name in menu_button_name_list:
            button_index=menu_button_name_list.index(button_name)
            button_object=menu_button_objects[button_index]
            return button_object
        else:
            error_msg="{0} button does not display in test editor menu bar".format(button_name)
            raise ElementNotVisibleException(error_msg)
        
    def click_menu_bar_button(self, button_name):
        '''
        This function will click menu bar button : example save
        '''
        button_obj=self.get_menu_bar_button_object(button_name)
        self._core_utill.left_click(button_obj)
        
    def click_on_file_menu_button(self):
        '''
        This function will click on file menu button
        '''
        button_obj=self.get_file_menu_button_object()
        self._core_utill.left_click(button_obj)
        
    def invoke_focexec_text_editor(self):
        '''
        To invoke dataformatTesterDlgOnly.jsp page, 
        first call Api  http://machine:port/{alias} to login in setup then call "http://machine:port/{alias}/junit/dataformatTesterDlgOnly.jsp?"
        
        :usage invoke_dataformattesterdlgonly_jsp()
        '''
        default_focexec_name='New FOCEXEC File'
        setup_url = utillobject.get_setup_url(self)
        jsp_file_directory_name = utillobject.parseinitfile(self, 'jsp_file_directory')
        jsp_file_name = utillobject.parseinitfile(self, 'jsp_file_name')
        required_url=setup_url.replace('home', '') + jsp_file_directory_name + '/' + jsp_file_name + '.jsp?'
        self.driver.get(setup_url)
        utillobject.wf_login(self)
        self.driver.get(required_url)
        utillobject.synchronize_with_visble_text(self, WebfocusEditor.first_tab_focexec_name_css, default_focexec_name, 60)
    
    def invoke_fex_using_text_editor(self, folder_path, fex_name, mrid=None, mrpass=None):
        '''
        Description: This function is used to invoke the Fex through the text editor directly through api
        Usage: invoke_fex_using_text_editor('P116_S10670/G427909', 'AR-AD-09a')
        ''' 
        setup_url = utillobject.get_setup_url(self)
        api_url = setup_url.replace('home', '') + 'tools/portlets/resources/markup/sharep/SPEditorBoot.jsp?folderPath=IBFS%253A%252FWFC%252FRepository%252F' + folder_path + '&description=' + fex_name + '&itemName=' + fex_name + '.fex&isReferenced=true&type=items'
        self.driver.get(api_url)
        utillobject.wf_login(self, mrid=mrid, mrpass=mrpass, add_home_path=False)
        utillobject.synchronize_with_number_of_element(self, "#bipEditorArea", 1, BasePage.report_medium_timesleep)
       
    def verify_max_linenumber(self, expected_max_linenumber, msg):
        '''
        This function will Click on show data format button.
        
        :usage click_show_data_format_button()
        '''
        line_number_css = WebfocusEditor.parent_line_number_css + ' > div.ace_gutter-cell'
        line_number_elements=self.driver.find_elements_by_css_selector(line_number_css)
        if len(line_number_elements)==0:
            raise AttributeError("Either the line number is not displaying at this moment OR The property provided to fetch them is incorrect.")
        actual_max_linenumber = line_number_elements[-1].text.strip()
        utillobject.asequal(self, expected_max_linenumber, actual_max_linenumber, msg)

    def enter_data_to_texteditor_from_file(self, data_file_name):
        """
        Syntax: click_text_editor_ribbon_button('Run')
        :Param btn_name: Save or Run...
        @author = Niranjan
        """
        data_file=os.getcwd() + "\data\\" + data_file_name
        webdriver_object_name="Text area inside text editor"
        textarea_input_elem=utillobject.validate_and_get_webdriver_object(self, WebfocusEditor.textarea_input_css, webdriver_object_name)
        try:
            with open(data_file) as f:
                line=f.read()
                utillobject.set_text_field_using_actionchains(self, textarea_input_elem, line)
        except FileNotFoundError:
            raise ("The " + data_file + "file does not exist in the specified path.")    
    
    def edit_fex_in_text_editor_using_find_and_replace(self, find_string, replace_string, button_name=None, check_box=None):
        """
        search_icon="Search and Replace"
        button_name='find_next','replace','replace_all'
        Syntax: edit_fex_in_text_editor(find='xxx',repl='yyy')
        @author = Niranjan
        """
        find_text_css=WebfocusEditor.search_and_replace_parent_css+" .findText input"
        WebfocusEditor.click_menu_bar_button(self, 'Search and Replace')
        utillobject.synchronize_with_visble_text(self, find_text_css, 'Find Next button')
        find_text_name="Find text input box"
        find_text_elem=utillobject.validate_and_get_webdriver_object(self, find_text_css, find_text_name)
        replace_text_css=WebfocusEditor.search_and_replace_parent_css+" .replaceText input"
        replace_text_name="Replace text input box"
        replace_text_elem=utillobject.validate_and_get_webdriver_object(self, replace_text_css, replace_text_name)
        utillobject.set_text_field_using_actionchains(self, find_text_elem, find_string)
        utillobject.set_text_field_using_actionchains(self, replace_text_elem, replace_string)
        if button_name:
            if button_name == 'find_next':
                findnext_button_css=WebfocusEditor.search_and_replace_parent_css+" .btnFindNext"
                findnext_name="Find Next button"
                findnext_elem=utillobject.validate_and_get_webdriver_object(self, findnext_button_css, findnext_name)
                CoreUtillityMethods.left_click(self, findnext_elem)
            if button_name == 'replace':
                replace_button_css=WebfocusEditor.search_and_replace_parent_css+" .btnReplaceNext"
                replace_button_name="Replace button"
                replace_button_elem=utillobject.validate_and_get_webdriver_object(self, replace_button_css, replace_button_name)
                CoreUtillityMethods.left_click(self, replace_button_elem)
            if button_name == 'replace_all':
                replace_all_button_css=WebfocusEditor.search_and_replace_parent_css+" .btnReplaceAll"
                replace_all_button_name="Replace All button"
                replace_all_button_elem=utillobject.validate_and_get_webdriver_object(self, replace_all_button_css, replace_all_button_name)
                CoreUtillityMethods.left_click(self, replace_all_button_elem)
        if check_box:
            '''#To do'''   
    
    def get_texteditor_text_data_line(self):
        '''
        Description: This will get each line of text data object and return it.
        :Usage get_texteditor_text_data_line()
        '''
        utillobject.synchronize_until_element_is_visible(self, WebfocusEditor.textarea_text_line_css, self.home_page_long_timesleep)
        text_line_data = utillobject.validate_and_get_webdriver_objects(self, WebfocusEditor.textarea_text_line_css, 'textarea_text_line_css')
        return text_line_data
    
    def verify_line_in_texteditor(self, expected_text_line_list, step_num, comparison_type='asequal'):
        '''
        Description: This will verify text line by line on text editor.
        :Usage  verify_line_in_texteditor(['SET PAGE-NUM=NOLEAD', 'ON GRAPH SET VZERO OFF'], '09.00')
        '''
        display_message = "Step {0}: Verify the list of lines'{1}' of text exist inside editor.".format(step_num, expected_text_line_list)
        editor_data = WebfocusEditor.get_texteditor_text_data_line(self)
        text_line_data_text = [text_data.text.strip() for text_data in editor_data]
        if type(expected_text_line_list) != list:
            expected_text_line_list = [expected_text_line_list]
        utillobject.verify_list_values(self, expected_text_line_list, text_line_data_text, display_message, assert_type=comparison_type)
    
    def replace_line_in_texteditor(self, expected_text_line, replaced_text_line_list, expected_text_line_index=None):
        '''
        Description: This will verify text line by line on text editor.
        :Usage  replace_line_in_texteditor('SET PAGE-NUM=NOLEAD', ['ON GRAPH SET VZERO OFF'], expected_text_line_index=9)
        '''
        editor_data = WebfocusEditor.get_texteditor_text_data_line(self)
        for index_, data_line in enumerate(editor_data, 1):
            if expected_text_line_index:
                if data_line.text.strip() == expected_text_line.strip() and index_ == int(expected_text_line_index):
                    CoreUtillityMethods.python_left_click(self, data_line)
                    if sys.platform == 'linux':
                        pykeyboard.tap_key(pykeyboard.end_key)
                    else:
                        keyboard.send('end')
                    time.sleep(3)
                    for _ in range(len(data_line.text)):
                        if sys.platform == 'linux':
                            pykeyboard.tap_key(pykeyboard.backspace_key)
                        else:
                            keyboard.send('backspace')
                    break
            else:
                if data_line.text.strip() == expected_text_line.strip():
                    CoreUtillityMethods.python_left_click(self, data_line, element_location ='top_left')
                    if sys.platform == 'linux':
                        pykeyboard.tap_key(pykeyboard.end_key)
                    else:
                        keyboard.send('end')
                    time.sleep(3)
                    for _ in range(len(data_line.text)):
                        if sys.platform == 'linux':
                            pykeyboard.tap_key(pykeyboard.backspace_key)
                        else:
                            keyboard.send('backspace')
                    break
        time.sleep(3)
        for new_line in replaced_text_line_list:
            if sys.platform == 'linux':
                pykeyboard.type_string(str(new_line), interval=1)
            else:
                keyboard.write(new_line, delay=1)
            time.sleep(2)
            if sys.platform == 'linux':
                pykeyboard.tap_key(pykeyboard.escape_key)
            else:
                keyboard.send('esc')
            time.sleep(2)
            if new_line != replaced_text_line_list[-1]:
                if sys.platform == 'linux':
                    pykeyboard.tap_key(pykeyboard.enter_key)
                else:
                    keyboard.send('enter')
                
    def get_toolbar(self, toolbar_name):
        '''
        Description: This will get toolbar object.
        :Usage  get_toolbar('Save')
        '''
        tool_name_css = "[data-ibx-name='_menu{0}']".format(str(toolbar_name).capitalize())
        tool_css = ".te-menu-bar .te-menu-button{0}".format(tool_name_css)
        help_css = ".te-menu-bar .te-menu-button-help{0}".format(tool_name_css)
        tool_description = '{0} toolbar'.format(str(toolbar_name).capitalize())
        if toolbar_name.lower() == 'help':
            toolbar_obj = utillobject.validate_and_get_webdriver_object(self, help_css, tool_description)
        else:
            toolbar_obj = utillobject.validate_and_get_webdriver_object(self, tool_css, tool_description)
        return toolbar_obj
    
    def verify_toolbar_enable_or_disable(self, toolbar_name, status, message):
        '''
        Description: This will verify tool_bar enable or disable.
        :Usage  verify_toolbar_enable_or_disable('Save', 'enable', 'Step 09.00: Verify tool')
        '''
        if status.lower() not in ['enable', 'disable']:
            raise KeyError("Please pass 'enable' or 'disable' as status value.")
        disable_class = 'ibx-widget-disabled'
        toolbar_obj = WebfocusEditor.get_toolbar(self, toolbar_name)
        class_data = utillobject.get_element_attribute(self, toolbar_obj, 'class')
        if disable_class in class_data:
            utillobject.asequal(self, status.lower(), 'disable', message)
        else:
            utillobject.asequal(self, status.lower(), 'enable', message)

    def verify_toolbar_icon_displayed(self, toolbar_name, status, message):
        '''
        Description: This will verify tool_bar icon displayed.
        :Usage  verify_toolbar_icon_displayed('Save', 'visible', 'Step 09.00: Verify tool')
        '''
        if status.lower() not in ['visible', 'not_visible']:
            raise KeyError("Please pass 'enable' or 'disable' as status value.")
        tool_dict = {'save':'.ibx-glyph-floppy', 'reset':'.ibx-glyph-reset-thin', 'undo':'.ibx-glyph-arrow-left', 'redo':'.ibx-glyph-arrow-right',
                     'copy':'.fa-copy', 'cut':'.fa-cut', 'paste':'.fa-paste', 'preview':'.ibx-glyph-preview', 'search':'.fa-search', 'options':'.ibx-glyph-layout',
                     'help':'.fa-question'}
        toolbar_obj = WebfocusEditor.get_toolbar(self, toolbar_name)
        try:
            tool_obj = utillobject.validate_and_get_webdriver_object(self, tool_dict[toolbar_obj.lower()], toolbar_obj, parent_object=toolbar_obj)
            status=tool_obj.is_displayed()
        except:
            status=False
        if status:
            utillobject.asequal(self, status, 'visible', message)
        else:
            utillobject.asequal(self, status, 'not_visible', message)
                 
    def verify_toolbar_title(self, toolbar_name, title_name, message):
        '''
        Description: This will verify toolbar _title.
        :Usage  verify_toolbar_title('Save', 'Save', 'Step 09.00: Verify tool')
        '''
        toolbar_obj = WebfocusEditor.get_toolbar(self, toolbar_name)
        acutal_title = utillobject.get_element_attribute(self, toolbar_obj, 'title')
        utillobject.asequal(self, title_name, acutal_title, message)
    
    def select_toolbar(self, toolbar_name):
        '''
        Description: This will select toolbar.
        :Usage  select_toolbar('Save')
        '''
        toolbar_obj = WebfocusEditor.get_toolbar(self, toolbar_name)
        CoreUtillityMethods.left_click(self, toolbar_obj)
    
    def select_editor_application_menu(self, menu_name):
        """
        Descriptions : This method used to select editor application menu such as Save, Save as, close, open
        Application menus : 'Open...' ,'New', 'Save', 'Save as...', 'Close'
        example usage : select_editor_application_menu('Save as...')
        """
        WebfocusEditor.select_toolbar(self, 'File')
        self._wf_mainpage.select_context_menu_item(menu_name)
        
    def verify_editor_application_menu(self, expected_menu_list, message, menu_path=None, comparision_type='asequal'):
        """
        Descriptions : This method used to select editor application menu such as Save, Save as, close, open
        Application menus : 'Open...' ,'New', 'Save', 'Save as...', 'Close'
        example usage : verify_editor_application_menu('Save as...')
        """
        WebfocusEditor.select_toolbar(self, 'File')
        if menu_path:
            self._wf_mainpage.select_context_menu_item(menu_path)
        self._wf_mainpage.verify_context_menu_item(expected_menu_list, message, comparision_type=comparision_type)
        
    def save_page(self, page_title=None, page_name=None, page_type=None, page_button_name='Save'):
        if page_title:
            self._wf_mainpage.open_popup_dialog_from_action_bar('Title', 'text_box', property_value=page_title)
        if page_name:
            self._wf_mainpage.open_popup_dialog_from_action_bar('Name', 'text_box', property_value=page_name)
        if page_type:
            '''#TODO'''
        if page_button_name:
            self._wf_mainpage.button_in_popup_dialog_from_action_bar(page_button_name, 'click')
    
    def get_autocomplete_text_elements(self, autocomplete_text):
        """
        Descriptions : This method is used to return autocomplete text element in the text editor
        :Usage get_autocomplete_text_elements()
        """
        parent_css = "div[class*='ace_autocomplete'] div.ace_scroller"
        text_css = parent_css + " div[class*='ace_line'] span[class='ace_']"
        autocomplete_prompt = self._utils.validate_and_get_webdriver_object(parent_css, "Text editor auto complete prompt")
        self._core_utill.python_move_to_element(autocomplete_prompt) 
        time.sleep(1.5)
        self._utils.scroll_down_and_find_item_using_mouse(text_css, autocomplete_text)
        xpath = "//div[contains(@class, 'ace_autocomplete')]//span[normalize-space()='{0}']".format(autocomplete_text)
        ele_list = self.driver.find_elements_by_xpath(xpath)
        if ele_list != []:
            return ele_list[0]
        else:
            error_msg="{0} autocomplete text is not available in the text editor".format(autocomplete_text)
            raise ElementNotVisibleException(error_msg)

    def verify_autocomplete_text_in_texteditor(self, autocomplete_text_list, msg, assert_type = "asequal"):
        """
        Description : This method is used to verify autocomplete text is present in the texteditor
        :Usage verify_autocomplete_text_in_texteditor(["SAVE", "SQL"], "1.01")
        """
        actual_autocomplete_text_list = []
        for autocomplete_text in autocomplete_text_list:
            actual_element = self.driver.get_autocomplete_text_elements(autocomplete_text)
            autocomplete_text_list.append(actual_element.text.strip())
        self._utils.verify_list_values(autocomplete_text_list, actual_autocomplete_text_list, msg = msg, assert_type = assert_type)
        
    def select_autocomplete_text_in_texteditor_mouse_scroll(self, autocomplete_text):
        """
        Description : This method is used to select autocomplete text in text editor by using mouse scroll
        :Usage select_autocomplete_text_in_texteditor_mouse_scroll("SQL")
        """
        actual_ele = self.driver.get_autocomplete_text_elements(autocomplete_text)
        self._core_utill.python_left_click(actual_ele)
    
    def verify_tabs(self, expected_tabs, step_num, assert_type='asequal'):
        """
        Description : Verify the text editor tabs
        :Usage - verify_tabs(['New FOCEXEC File], "05.01")
        """
        tabs_object = self.driver.find_elements_by_css_selector(".ibx-tab-button")
        actual_tabs = [tab.text.strip() for tab in tabs_object if tab.is_displayed()]
        msg = "Step {0} : Verify {1} tabs displayed in Text Editor".format(step_num, expected_tabs)
        utillobject.verify_list_values(self, expected_tabs, actual_tabs, msg, assert_type)