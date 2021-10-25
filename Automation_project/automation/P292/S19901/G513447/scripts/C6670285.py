'''
Created on Nov 8, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6670285
Testcase Name : Create Portal
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.wftools import designer_portal
from common.lib import utillity
from common.lib import core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6670285_TestClass(BaseTestCase):

    def test_C6670285(self):
        """
        TESTCASE VARIABLES
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utillobj=core_utility.CoreUtillityMethods(self.driver)
        portal_obj=designer_portal.Portal(self.driver)
         
        folder_name='P292_S19901'
        group_name='G513445'
        title_name='Portal for Context Menu Testing1'
        
        """
        CSS
        """
        designer_css=".ibx-tab-button:nth-child(3) .ibx-label-text"
        
        """
        Step 1:Sign into WebFOCUS Home Page as Admin User
        
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
    
        """
        Step 2:Click Content View from the side bar > Click on Domains from the resource tree
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_option_from_crumb_box('Domains')
 
        """
        Step 3:If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder('{0}->{1}'.format(folder_name, group_name))
 
        """
        Step 4:Click on 'Designer' category button > click on 'Portal'
        Verify 'New Portal' dialog appears
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        util_obj.synchronize_with_visble_text(designer_css, 'Designer', Global_variables.mediumwait)
        portal_obj.verify_caption_in_new_or_edit_portal_dialog(label_text='New Portal', step_number='4:1')
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value="", label_text='Title', focused=True, current_mode='enable', step_number='4:2')
        portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value="", current_mode='enable', label_text='Name', step_number='4:3')
        portal_obj.alias_textbox_in_new_or_edit_portal_dialog(verify_value="", current_mode='enable',label_text='Alias', step_number='4:4')
        
        portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle='check', current_mode='enable',label_text='Banner', step_number='4:5')
        portal_obj.show_portal_title_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='check', current_mode='enable',label_text='Show portal title in banner', step_number='4:6')
        portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='Not Selected', current_mode='disable',label_text='Logo', step_number='4:7')
        portal_obj.logo_browse_button_in_new_or_edit_portal_dialog(verify_value='Browse', current_mode='enable',step_number='4:8')
       
        portal_obj.verify_navigation_label_text('Navigation', '4:9')
        portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', current_mode='enable',title_tooltip='Two-level side', step_number='4:10')
        portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', current_mode='enable',title_tooltip='Three-level', step_number='4:11')
        portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', current_mode='enable',title_tooltip='Two-level top', step_number='4:12')
        portal_obj.show_top_navigation_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='uncheck', current_mode='disable',label_text='Show top navigation in banner', step_number='4:13')
        portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Default', current_mode='enable',label_text='Theme', dropdown_list_value=['Default','Light','Midnight'], step_number='4:14')
         
        project_id = core_utillobj.parseinitfile('project_id')
        suite_id = core_utillobj.parseinitfile('suite_id')
        group_id= core_utillobj.parseinitfile('group_id')
        folder_path='portal/'+project_id+'_'+suite_id+'/'+group_id
        portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value=folder_path, readonly_mode=True, label_text='URL', step_number='4:15')
        portal_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='uncheck', label_text='Create My Pages menu', step_number='4:16')
         
        portal_obj.create_button_inside_new_or_edit_portal_dialog(verify_button='Create', current_mode='disable', color_name='curious_blue', step_number='4:17')
        portal_obj.cancel_button_inside_new_or_edit_portal_dialog(verify_button='Cancel', current_mode='enable', color_name='black', step_number='4:18')
                
        """
        Step 5:Enter Title as "Portal for Context Menu Testing1" > Click 'Create'
        Verify 'Portal for Context Menu ...' appear as a folder with the grayed dotter line around the rectangular box (which means it is unpublished).
        """
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=title_name)
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.synchronize_with_visble_text(".content-box.ibx-widget .files-box", title_name, 90)
        main_page_obj.verify_folders_in_grid_view([title_name], 'asin', "Step 5: Verify 'Portal for Context Menu ...' appear as a folder.")
        main_page_obj.verify_folder_icon_in_content_area(title_name, 'portal', '5.1', verify_color_name='grey')
        main_page_obj.verify_content_area_folder_publish_or_unpublish(title_name, 'unpublish', "Step 5.2: Verify folder is Unpublished")
        
        """
        Step 6:Right click on 'Portal for Context Menu Testing1' > Publish
        Verify that 'Portal for Context Menu T...' gets published and there is no greyed dotted line outside the folder
        """
        main_page_obj.right_click_folder_item_and_select_menu(title_name,'Publish', '{0}->{1}'.format(folder_name, group_name))
        util_obj.synchronize_with_visble_text(".content-box.ibx-widget .files-box", title_name, 90)
        main_page_obj.verify_content_area_folder_publish_or_unpublish(title_name, 'publish', "Step 6: Verify folder is published")
        main_page_obj.verify_folder_icon_in_content_area(title_name, 'portal', '6.1', verify_color_name='lochmara')
        
        """
        Step 7:In the banner link, click on the top right username > Click Sign Out.
        """    
        main_page_obj.signout_from_username_dropdown_menu()


if __name__ == '__main__':
    unittest.main()