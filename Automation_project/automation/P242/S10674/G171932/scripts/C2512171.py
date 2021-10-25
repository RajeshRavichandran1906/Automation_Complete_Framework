'''
Created on 03 July, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2512171
TestCase Name = Error in fex syntax,Query Detail does not display error as in legacy home page
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.pages import wf_mainpage
from common.lib import utillity, core_utility
from selenium.common.exceptions import NoSuchElementException


class C2512171_TestClass(BaseTestCase):

    def test_C2512171(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        proj_id = str(project_id)
        proj_sub_folder="{0}->My Content".format(proj_id)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        property_dialog_css='.properties-page.propPage'
        ribbon_button_css="[class^='main-panel'] [class^='right-main-panel'] [class^='create-new-items-box'] [role='button'][onclick*='newEditor'] .ibx-label-text"
        text_editor_css="#bipEditor #bipEditorArea"
        text_editor_text='? GEN'
        text_editor_save_button_css='#editor_toolbar #toolbar_button_save'
        save_dialog_save_input_css=".window-active #IbfsOpenFileDialog7_cbFileName .text-field"
        file_name='GEN'
        save_dialog_save_button_css=".window-active #IbfsOpenFileDialog7_btnOK"
        query_detail_tab_error_message_css=".properties-query-detail-folder .ibx-label-text"
        expected_error_message='Error getting details'
        
        """ Step 1: Login to WebFOCUS as a Developer
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Open P242_S10674_G171304/My Content in tree
        """
        wf_mainobj.expand_repository_folders(proj_sub_folder)
         
        """ Step 4: Click More in Action Bar
        """
        wf_mainobj.select_ribbon_button('More')
        utillobj.synchronize_with_visble_text(ribbon_button_css, 'Text Editor', 190)
         
        """ Step 5: Click Text Editor in Action Bar
        """
        wf_mainobj.select_ribbon_button('Text Editor')
        core_utilobj.switch_to_new_window()
         
        """ Step 6: Type ? GEN in text editor
                    Click Save in text editor
                    Title: GEN
                    Save
                    Close text editor
        """
        try:
            text_editor_elem=self.driver.find_element_by_css_selector(text_editor_css)
        except NoSuchElementException:
            raise AttributeError("Text editor window not able to found.")
        utillobj.set_text_to_textbox_using_keybord(text_editor_text, text_box_elem=text_editor_elem)
        utillobj.synchronize_with_visble_text(text_editor_css, text_editor_text, 190, text_option='text_value')
        try:
            text_editor_elem=self.driver.find_element_by_css_selector(text_editor_save_button_css)
            core_utilobj.left_click(text_editor_elem)
        except NoSuchElementException:
            raise AttributeError("Save button not exists under 'Text editor window' toolbar.")
        try:
            save_dialog_save_input_elem=self.driver.find_element_by_css_selector(save_dialog_save_input_css)
            utillobj.set_text_to_textbox_using_keybord(file_name, text_box_elem=save_dialog_save_input_elem)
            utillobj.synchronize_with_visble_text(save_dialog_save_input_css, file_name, 190, text_option='text_value')
        except NoSuchElementException:
            raise AttributeError("Save dialog window not able to found.")
        try:
            save_dialog_save_input_elem=self.driver.find_element_by_css_selector(save_dialog_save_button_css)
            core_utilobj.left_click(save_dialog_save_input_elem)
        except NoSuchElementException:
            raise AttributeError("Save button not exist under save dialog window.")
        core_utilobj.switch_to_previous_window()
        
        """ Step 7: Right click GEN and select Properties
        """
        wf_mainobj.select_repository_folder_item_context_menu(file_name, context_menu_item_path='Properties', folder_path=proj_sub_folder)
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        
        """ Step 8: Click Query Detail tab
                    Verify 'error getting details' error message appears:
        """
        wf_mainobj.edit_property_dialog_value('Query Detail', 'tab_value', 'Query Detail')
        acutal_error_message=self.driver.find_element_by_css_selector(query_detail_tab_error_message_css).text.strip()
        utillobj.asequal(expected_error_message, acutal_error_message, "Step 8: Verify 'error getting details' error message appears")
            
        """ Step 9: Close Properties panel
        """
        wf_mainobj.close_property_dialog()
        
        """ Step 10: Sign out
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()