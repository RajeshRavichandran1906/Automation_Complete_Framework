'''
Created on October 17, 2018

@author: Robert
Testcase Name : Edit portal without banner 
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779497
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.lib import utillity,core_utility

class C6779497_TestClass(BaseTestCase):
    
    def test_C6779497(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        Crumb_css=".crumb-box"
        Long_wait=90
        medium_wait=40
        folder_css=".content-title-label"
        folder_name_path="P292_S19901->G520448"
        portals_css = "div[title='Portals'] .ibx-label-text"
        expected_title = "v5-alias-test2"
        content_area_text = "There are no pages available"
        content_area_css = ".files-no-search-results .ibx-label-text"
        content_css='div[class="ibx-label-glyph ibx-label-icon fa fa-bar-chart"]'
        crumb_css='div[data-ibx-type="breadCrumbTrail"]'
        user_css = ".pvd-menu-admin .ibx-label-text"
        user_name_parsed = core_util_obj.parseinitfile('mriddev')
        pop_top_css=".pop-top [data-ibx-name='vbMain'] [data-ibxp-text='Banner']"
        portal_name="v5_banner_test&"
        

        """
        Step 1: Login WF new home page as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(content_css, '1', 30)
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, '1', 15)
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Right click on 'v5-alias-test2' portal and select Edit
        
        Verify dialog title appears as 'Edit Portal''
        Verify title appears as ' 'v5_banner_test&' and name appears as 'v5_banner_test_'
        Banner switch is off
        Alias is empty
        Logo is Not Selected
        'Two-level top' navigation type is selected
        Theme should be 'Default'
        URL field shows : https://machinename:port/alias/domain_name/v5_banner_test_
        Save button is disabled
        
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        main_page_obj.right_click_folder_item_and_select_menu(portal_name,'Edit')
        util_obj.synchronize_with_number_of_element(pop_top_css, '1', medium_wait)
        
        designer_portal_obj.verify_caption_in_new_or_edit_portal_dialog('Edit Portal', step_number='Step 3.')
        designer_portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value='v5_banner_test&',  step_number='Step 3.')
        designer_portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value='v5_banner_test_', step_number='Step 3.')
        designer_portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle='uncheck',  step_number='Step 3.')
        designer_portal_obj.alias_textbox_in_new_or_edit_portal_dialog(verify_value='', step_number='Step 3.')
        designer_portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='Not Selected', step_number='Step 3.')
        designer_portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', current_mode='enable', step_number='Step 3.')
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Default', current_mode='enable', step_number='Step 3.')
        designer_portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/P292_S19901/G520448/v5_banner_test_', step_number='Step 3.')
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(verify_button='Save', current_mode='disable', step_number='Step 3.')
        
        """
        Step 4.Click on Browse button next to Logo
        Select resource dialog opens.
        step 5. Click cancel in resource dialog.
        """
        
        designer_portal_obj.logo_browse_button_in_new_or_edit_portal_dialog(verify_resource_dialog=True, step_number='Step 4.')
        
        """
        Step 6.Click on cancel button in edit portal dialog.
        Edit portal dialog closes.
        """
        designer_portal_obj.cancel_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.synchronize_until_element_disappear(".pop-top", 30)
        
        designer_portal_obj.verify_portal_dialog_open_or_close("Close", "Step 6. Verify Edit Portal dialog closed")
       
        """
        Step 7. Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        