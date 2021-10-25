from common.lib.base import BasePage
from common.pages.webfocus_editor import WebfocusEditor as wfeditor_object

class Wf_Mainpage(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Wf_Mainpage, self).__init__(driver)
        
    def enter_data_to_texteditor_from_file(self, data_file_name):
        '''
        Desc:- This function will read data from text file and write on the text editor focexec input area
        data_file_name :- 'fexfilename.txt' (data_file_name should be kept underneath data folder)
        '''
        wfeditor_object.enter_data_to_texteditor_from_file(self, data_file_name)
        
    def edit_fex_in_text_editor_using_find_and_replace(self, find_string, replace_string, check_box_name=None):
        '''
        Desc:- This function will click on search and replace icon from the menu bar then click on find input box and type the string
        click on replace input box to type string then click on replace button
        edit_fex_in_text_editor_using_find_and_replace('ON TABLE SET WEBVIEWER = ON', 'ON TABLE SET WEBVIEWER = OFF')
        '''
        wfeditor_object.edit_fex_in_text_editor_using_find_and_replace(self, find_string, replace_string, button_name='replace', check_box=check_box_name)   

    def edit_fex_in_text_editor_using_find_and_replaceall(self, find_string, replace_string, check_box=None):
        '''
        Desc:- This function will click on search and replace icon from the menu bar then click on find input box and type the string
        click on replace input box to type string then click on replace button
        edit_fex_in_text_editor_using_find_and_replace('ON TABLE SET WEBVIEWER = ON', 'ON TABLE SET WEBVIEWER = OFF')
        '''
        wfeditor_object.edit_fex_in_text_editor_using_find_and_replace(self, find_string, replace_string, button_name='replace_all', check_box=check_box)
    
    def click_menu_bar_button(self, button_name):
        '''
        This function will click menu bar button : example save
        :Usage = click_menu_bar_button("Save")
        '''
        wfeditor_object(self.driver).click_menu_bar_button(button_name)
    
    def verify_tabs(self, expected_tabs, step_num, assert_type='asequal'):
        """
        Description : Verify the text editor tabs
        :Usage - verify_tabs(['New FOCEXEC File], "05.01")
        """
        wfeditor_object.verify_tabs(self, expected_tabs, step_num, assert_type)
        
class editor_toolbar(Wf_Mainpage):
    """ Inherit attributes of the parent class = Wf_Mainpage """

    def __init__(self, driver):
        super(editor_toolbar, self).__init__(driver)
        self._wf_editor = wfeditor_object(self.driver)
        
    def verify_tool_enable_or_disable(self, toolbar_name, status, display_message):
        '''
        Description: This will verify tool_bar enable or disable.
        :Usage  verify_toolbar_enable_or_disable('Save', 'enable', 'Step 09.00: Verify tool')
        '''
        self._wf_editor.verify_toolbar_enable_or_disable(toolbar_name, status, display_message)
    
    def verify_tool_icon_displayed(self, toolbar_name, status, display_message):
        '''
        Description: This will verify tool_bar icon displayed.
        :Usage  verify_toolbar_icon_displayed('Save', 'visible', 'Step 09.00: Verify tool')
        '''
        self._wf_editor.verify_toolbar_icon_displayed(toolbar_name, status, display_message)
    
    def verify_toolbar_title(self, toolbar_name, title_name, display_message):
        '''
        Description: This will verify tool_bar title.
        :Usage  verify_toolbar_title('Save', 'visible', 'Step 09.00: Verify tool')
        '''
        self._wf_editor.verify_toolbar_title(toolbar_name, title_name, display_message)
    
    def select_tool_form_toolbar(self, toolbar_name):
        '''
        Description: This will select a tool form toolbar.
        :Usage  select_tool_form_toolbar('Save')
        '''
        self._wf_editor.select_toolbar(toolbar_name)
    
    def select_application_menu_option(self, menu_name):
        '''
        Description: This will select a tool application menu option.
        :Usage  select_application_menu_option('Save')
        '''
        self._wf_editor.select_editor_application_menu(menu_name)
    
    def verify_application_menu_option(self, expected_menu_list, display_message, menu_path=None, comparision_type='asequal'):
        '''
        Description: This will select a tool application menu option.
        :Usage  verify_application_menu_option(['Save'], 'Step 09.00 Verify', menu_path='New', comparision_type='asnotin')
        '''
        self._wf_editor.verify_editor_application_menu(expected_menu_list, display_message, menu_path=menu_path, comparision_type=comparision_type)
    
    def save_page_from_application_menu(self, page_title=None, page_name=None, page_type=None, page_button_name='Save'):
        '''
        Description: This will select a tool application menu and click save form toolbar.
        :Usage  save_page_from_application_menu(page_title='C11', page_name='c11', page_type='WebFOCUS Style Sheet (sty)', page_button_name='Save')
        '''
        self._wf_editor.select_editor_application_menu('Save')
        self._wf_editor.save_page(page_title=page_title, page_name=page_name, page_type=page_type, page_button_name=page_button_name)
    
    def save_as_page_from_application_menu(self, page_title=None, page_name=None, page_type=None, page_button_name='Save'):
        '''
        Description: This will select a tool application menu and click save as form toolbar.
        :Usage  save_as_page_from_application_menu(page_title='C11', page_name='c11', page_type='WebFOCUS Style Sheet (sty)', page_button_name='Save')
        '''
        self._wf_editor.select_editor_application_menu('Save As')
        self._wf_editor.save_page(page_title=page_title, page_name=page_name, page_type=page_type, page_button_name=page_button_name)
        
     
class wf_texteditor(Wf_Mainpage):
    """ Inherit attributes of the parent class = wf_texteditor """

    def __init__(self, driver):
        super(wf_texteditor, self).__init__(driver)
        self._wf_editor = wfeditor_object(self.driver)
        
    def verify_line_in_texteditor(self, expected_text_line_list, step_num, comparison_type='asequal'):
        '''
        This will verify text line by line on text editor.
        :Usage  verify_line_in_texteditor(['SET PAGE-NUM=NOLEAD', 'ON GRAPH SET VZERO OFF', ])
        '''
        self._wf_editor.verify_line_in_texteditor(expected_text_line_list, step_num, comparison_type=comparison_type)
    
    def replace_line_in_texteditor(self, expected_text_line, replaced_text_line, expected_text_line_index=None):
        '''
        This will verify text line by line on text editor.
        :Usage  replace_line_in_texteditor('SET PAGE-NUM=NOLEAD', ['ON GRAPH SET VZERO OFF'], expected_text_line_index=9)
        '''
        self._wf_editor.replace_line_in_texteditor(expected_text_line, replaced_text_line, expected_text_line_index=expected_text_line_index)