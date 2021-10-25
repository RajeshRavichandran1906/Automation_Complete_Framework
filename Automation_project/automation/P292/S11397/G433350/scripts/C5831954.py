'''
Created on August 06, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=433350&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5831954
TestCase Name = Verify action tiles for Custom folder under Page Templates
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage, page_designer
from common.lib import utillity, core_utility, javascript
from common.pages import page_designer_miscelaneous, wf_mainpage as wfmain_pages
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C5831954_TestClass(BaseTestCase):

    def test_C5831954(self):
        
        """
        TESTCASE VARIABLES
        """
        create_folder_pop=".create-new-folder.pop-top"
        create_folder_dialog_caption_title_input_css="{0} .ibx-dialog-title-box .ibx-label-text".format(create_folder_pop)
        dialog_input_box_css="{0} [data-ibx-name='sdInputDivType']".format(create_folder_pop)
        label_css="[data-ibx-type='ibxLabel'] .ibx-label-text"
        title_input_css="#sdtxtFileTitle input"
        ok_button_css="{0} .ibx-dialog-ok-button".format(create_folder_pop)
        item_disable_css="ibx-widget-disabled"
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        core_utilobj = core_utility.CoreUtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        mainpage_obj = wfmain_pages.Wf_Mainpage(driver)
        jscript_obj=javascript.JavaScript(driver)
        page_designer_misobj=page_designer_miscelaneous.PageDesignerMiscelaneous(driver)
        page_desigobj=page_designer.Design(driver)
        
        def verify_create_folder(excpected_dialog_caption_text, excpected_title_label_text, excpected_name_label_text, step_num):
            '''
            This fuction will verify create folder dialog.
            '''
            utillobj.synchronize_with_number_of_element(create_folder_pop, 1, 190)
            dilago_caption_title_text=driver.find_element_by_css_selector(create_folder_dialog_caption_title_input_css).text.strip()
            utillobj.asequal(excpected_dialog_caption_text, dilago_caption_title_text, "Step {0}.1: Verify dialog box that it displays 'New Folder' as caption title.".format(str(step_num)))
            input_elems=driver.find_elements_by_css_selector(dialog_input_box_css)
            title_elem=[elem for elem in input_elems if elem.text.strip()=='Title'][0]
            title_text=title_elem.find_element_by_css_selector(label_css).text.strip()
            utillobj.asequal(excpected_title_label_text, title_text, "Step {0}.2: Verify Title Label displayed.".format(str(step_num)))
            title_input_status=title_elem.find_element_by_css_selector(title_input_css).is_displayed()
            utillobj.asequal(True, title_input_status, "Step {0}.3: Verify Title input box displayed.".format(str(step_num)))
            name_elem=[elem for elem in input_elems if elem.text.strip()=='Name'][0]
            name_elem_text=name_elem.find_element_by_css_selector(label_css).text.strip()
            utillobj.asequal(excpected_name_label_text, name_elem_text, "Step {0}.4: Verify Name Label displayed.".format(str(step_num)))
            title_input_status=title_elem.find_element_by_css_selector(title_input_css).is_displayed()
            utillobj.asequal(True, title_input_status, "Step {0}.5: Verify Name input box displayed.".format(str(step_num)))
            ok_button_elem=driver.find_element_by_css_selector(ok_button_css)
            ok_button_text=ok_button_elem.find_element_by_css_selector('.ibx-label-text').text.strip()
            returned_obj=jscript_obj.get_element_all_attributes(ok_button_elem)
            utillobj.asequal('OK', ok_button_text, "Step {0}.6: Verify Ok button.".format(str(step_num)))
            utillobj.asin(item_disable_css, returned_obj['class'], "Step {0}.7: Verify Ok button disabled.".format(str(step_num)))
            cancel_button_elem=driver.find_element_by_css_selector(".ibx-dialog-cancel-button .ibx-label-text").text.strip()
            utillobj.asequal('Cancel', cancel_button_elem, "Step {0}.8: Verify cancel button.".format(str(step_num)))
            
        """ Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        
        """ Step 2: Click on Content tree from side bar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        wfmain_obj.click_repository_folder('Domains')
        
        """ Step 3: Click Domains from navigation bar.
                    Collapse Domains if Domains is expanded.
        """
        wfmain_obj.collapse_repository_folder('Domains')
        
        """ Step 4: Expand Global Resources node > Page Templates folder and click on Custom sub-folder.
                    Verify that it displays 'Folder' and 'Page' action bars.
        """
        mainpage_obj.expand_repository_folders('Global Resources->Page Templates->Custom')
        wfmain_obj.verify_action_bar_tab_all_options(['Folder', 'Page'], "Step 4: Verify that it displays 'Folder' and 'Page' action bars.")
        
        """ Step 5: Click on Folder action bar.
                    Verify that it displays 'New Folder' dialog box with Title text box, Name text box, OK button by default disabled and Cancel button.
        """
        wfmain_obj.select_action_bar_tabs_option('Folder')
        verify_create_folder('New Folder', 'Title', 'Name', '5')
                
        """ Step 6: Enter Title "Custom Page" > Click OK.
                    Verify folder is created.
        """
        wfmain_obj.enter_new_folder_title_in_popup_dialog('Custom Page')
        wfmain_obj.click_button_on_popup_dialog('OK')
        wfmain_obj.expand_repository_folders_and_verify('Custom', ['Custom Page'], msg="Step 6: Verify folder is created.")
        
        """ Step 7: Open Custom Page folder and click on Page action tile.
        """
        mainpage_obj.expand_repository_folders('Custom Page')
        wfmain_obj.select_action_bar_tabs_option('Page')
        core_utilobj.switch_to_new_window()

        """ Step 8: Create a PGX using blank template by clicking Page action bar.
        """
        page_designer_misobj.select_page_designer_template('Blank')
        
        """ Step 9: Click on Application menu > Close > Yes > Save.
                    Verify "Page 1" is created.
        """
        page_desigobj.close_and_save_page_with_default_name(wait_time=9)
        wfmain_obj.verify_items_in_grid_view(['Page 1'], 'asequal', 'Step 9: Verify "Page 1" is created.')
        
        """ Step 10: Revert back the Home page to its default by clicking Domains under repository tree.
        """
        wfmain_obj.collapse_repository_folder('Domains')
        
        """ Step 11: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()