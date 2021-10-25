'''
Created on November 2, 2018

@author: vpriya
Testcase Name : Create portal dialog defaults
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779485
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.lib import utillity
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6779485_TestClass(BaseTestCase):
    
    def test_C6779485(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        folder_name_path="P292_S19901->G520448"
        designer_css=".ibx-tab-button:nth-child(3) .ibx-label-text"
        vfive_main_dialog_css = ".pop-top [data-ibx-name='vbMain']"
        title_text_box_css="[data-ibx-type='ibxTextField'].pvd-title"
        
        """
        Step 1: Login WF new home page as domain developer.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
          
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Select Designer tag and click on Portal
        Verify 'Create Portal' dialog opens
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_visble_text(designer_css, 'Designer', Global_variables.mediumwait)
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        
        """
        Step 4: Check Title/Name/Alias text box defaults.
        """
        util_obj.synchronize_with_number_of_element(title_text_box_css,1,Global_variables.mediumwait)
        designer_portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value="", current_mode="enable",focused=True,label_text='Title',step_number='4')
        designer_portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value="", current_mode="enable",label_text='Name',step_number='4.1')
        designer_portal_obj.alias_textbox_in_new_or_edit_portal_dialog(verify_value="", current_mode="enable",label_text='Alias',step_number='4.2')
        
        """
        Step 5: Check buttons.
        Verify Create and cancel buttons are disabled by default.
        Create button is highlighted.
        """
        designer_portal_obj.create_button_inside_new_or_edit_portal_dialog(verify_button='Create', current_mode="disable",color_name='curious_blue',step_number='5.1')
        designer_portal_obj.cancel_button_inside_new_or_edit_portal_dialog(verify_button='Cancel', current_mode="enable",color_name='black',step_number='5.2')
        
        """
        Step 6: Check Banner switch defaults.
        """
        designer_portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle="check", current_mode='enable',label_text='Banner',step_number='6')
        
        """
        Step 7: Test 'Show portal title in banner box' defaults
        Show portal title in banner box is checked by default.
        """
        designer_portal_obj.show_portal_title_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox="check",current_mode='enable',label_text='Show portal title in banner',step_number='7')
        
        """
        Step 8:Check Logo defaults.
        Logo is not selected and disabled by default;
        'Not Selected' message appears in the text box;
        """
        designer_portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='Not Selected', current_mode="disable", label_text='Logo', step_number='8')
        
        
        """
        Step 9:Check Navigation defaults.
        3 types of navigation are available;
        Two-level side is selected by default;
        Show top navigation in banner is unchecked and is disabled by defaul
        
        """
        designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', step_number='9')
        designer_portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='9.1')
        designer_portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='9.2')
        designer_portal_obj.show_top_navigation_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='uncheck',current_mode='disable',step_number='9.2')
        
        """
        Step 10:Hover over navigation types one by one.
        """
        designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(title_tooltip='Two-level side', step_number='10')
        designer_portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(title_tooltip='Three-level', step_number='10.1')
        designer_portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(title_tooltip='Two-level top', step_number='10.2')
        
        """
        Step 11:Check Theme defaults.
        """
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Default',step_number='11')
        
        """
        Step 12:Click on Theme dropdown.
        Default, Light and Midnight themes are available for selection.
        """
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(dropdown_list_value=['Default','Light','Midnight'],step_number='12')
        
        """
        Step 13:Check URL defaults.
        """
        
        designer_portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/P292_S19901/G520448', readonly_mode=True, label_text='URL', step_number='13')
        
        """
        Step 14:Check 'My Pages menu' defaults.
        """
        designer_portal_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='uncheck', current_mode='enable',step_number='14')
        
        """
        Step 15:Hover over (*).
        Verify it brings up Close tool tip
        """
        designer_portal_obj.close_button_inside_new_or_edit_portal_dialog(title_tooltip='Close', step_number='15')
        
        """
        Step 16:Click close..
        Verify New Portal dialog disappears.
        """
        designer_portal_obj.cancel_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.synchronize_until_element_disappear(vfive_main_dialog_css,2)
        designer_portal_obj.verify_portal_dialog_open_or_close('Close',"verify dialog are closed")
        
        """
        Step 17.Signout
        """
        
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()
    
        