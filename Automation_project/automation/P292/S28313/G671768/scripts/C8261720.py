'''
Created on December 31, 2018

@author: KK14897
Testcase Name : Create portal without banner
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261720
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal,page_designer
from common.lib import utillity
from common.lib import core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261720_TestClass(BaseTestCase):
    
    def test_C8261720(self):
        
        def get_back_in_folder(self,parameter):
            no_of_parameters=parameter.split('->')
            for para in no_of_parameters:
                ele=self.driver.find_elements_by_css_selector("[class='ibx-label-text']")
                folder=[a for a in ele if a.text == para][0]
                folder.click()
                 
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        portal_obj = designer_portal.Portal(self.driver)
        portal_obj_2=designer_portal.Two_Level_Top(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        pd_obj=page_designer.Design(self.driver)
        Project_ID=core_util_obj.parseinitfile("project_id")
        Suite_ID=core_util_obj.parseinitfile("suite_id")
        Group_ID=core_util_obj.parseinitfile("group_id")
        Folder_Path=str("Domains->"+Project_ID+"_"+Suite_ID+"->"+Group_ID)
        Portal_name='v5_banner_test&'
       
        '''
        Step 01:Login WF new home page as domain developer.
        '''
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
         
        '''
        Step 02 : Click on Content tree from side bar
        '''
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.click_repository_folder('Domains')
        
        '''
        3 Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Select Designer tag and click on Portal tile in action bar.
        '''
        main_page_obj.expand_repository_folder(Folder_Path)
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        
        '''
        4 Enter title as 'v5_banner_test&' in create portal dialog.
        Name text box is filled automatically as 'v5_banner_test_'
        '''
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(Portal_name)
        portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value='v5_banner_test_', step_number='4')
        
        '''
        5 Switch off banner
        Verify Show portal title in banner checkbox is unchecked and is disabled to make changes.
        '''
        portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(select_toggle='uncheck', step_number='5.1')
        portal_obj.show_portal_title_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox="uncheck", current_mode="disable", step_number="5.2")
        
        '''
        6 Select 'Three level' navigation.
        Verify 'Show top navigation in banner' checkbox is disabled.
        '''
        portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type="check", step_number="6")
        
        '''
        7 Select 'Two-level top' navigation.
        Verify 'Show top navigation in banner' checkbox is disabled.
        '''
        portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type="check", step_number="7")
        
        '''
        8 Click Create
        Verify 'New Portal' dialog is closed;
        'v5_banner_test&' portal title appears in Italic;
        Portal is unpublished.
        '''
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button='True')
        main_page_obj.verify_folders_in_grid_view([Portal_name], comparision_type='asin', msg='Step 5.1: V5 folder appears')
        main_page_obj.verify_content_area_folder_publish_or_unpublish(Portal_name, 'unpublish', msg='Step 5.2: Verify Portal unpublished')
        '''
        Step 9 : Right click on 'v5_banner_test&' and select Run
        Verify portal run mode shows no banner and title as below.
        '''
        main_page_obj.right_click_folder_item_and_select_menu(Portal_name, context_menu_item_path='Run')
        core_util_obj.switch_to_new_window()
        core_util_obj.switch_to_previous_window()
        '''
        Step 10 : Right click on 'v5_banner_test&' and select Publish
        Step 11 : Close portal run mode
        '''
        main_page_obj.right_click_folder_item_and_select_menu(Portal_name, context_menu_item_path='Publish')
         
        '''
        Step 12 : Signout WF.
        '''
        main_page_obj.signout_from_username_dropdown_menu()
         
        '''
        Step 13 : Login WF as Administrator
        '''
        login_obj.invoke_home_page('mrid', 'mrpass')
         
        '''
        Step 14 : Click on Content from side bar
        '''
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.click_repository_folder('Domains')
        
        '''
        Step 15 : Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Right click on 'v5_banner_test&' and select Properties
        '''
        main_page_obj.expand_repository_folder(Folder_Path)
        main_page_obj.right_click_folder_item_and_select_menu(Portal_name, context_menu_item_path='Properties')
        
        '''
        Step 16 : Click on Advanced tab;
        Click on 'Allow Personal Pages' checkbox and click on save button.
        Verify 'My Content' folder is created under 'v5_banner_test&' in both content area and under domains tree.
        '''
        util_obj.synchronize_with_visble_text('.properties-general-folder', 'Show', Global_variables.mediumwait,condition_type='asin')
        main_page_obj.select_property_tab_value('Advanced')
        main_page_obj.edit_property_dialog_value('Allow personal pages', 'checkbox', 'check', tab_name='Advanced')
        main_page_obj.select_property_dialog_save_cancel_button('Save')
        main_page_obj.close_property_dialog()
        main_page_obj.expand_repository_folder(Folder_Path+'->'+Portal_name)
        main_page_obj.expand_repository_folder('My Content', index=1)
        
        '''
        Step 17 : Signout WF.
        '''
        main_page_obj.signout_from_username_dropdown_menu()
         
        '''
        Step 18 : Login WF new home page as domain developer
        '''
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
         
        '''
        Step 19 : Click on Content from side bar
        '''
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.click_repository_folder('Domains')
         
        '''
        Step 20 : Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Click on 'My Content' folder from under 'v5_banner_test&';
        Click on 'Page' tile from action bar.
        '''
        main_page_obj.expand_repository_folder(Folder_Path+'->'+Portal_name)
        main_page_obj.right_click_folder_item_and_select_menu(item_name='My Content', click_option='double_click', item_name_index=1)
        main_page_obj.select_action_bar_tabs_option('Page')
         
        '''
        Step 21 : Choose Grid 2-1 template;
        '''
        core_util_obj.switch_to_new_window()
        pd_obj.select_page_designer_template('Grid 2-1')
         
        '''
        Step 22 : Move to Retail Samples domain from content section by clicking on < before G520448
        '''
        get_back_in_folder(self,"G520448->P292_S19901")
         
        '''
        Step 23 : Drag and drop 'Category Sales' from Retail Samples -> Portal -> Small Widgets to Panel2.
        '''
        pd_obj.drag_content_item_to_container("Category Sales", "Panel 2", content_folder_path="Retail Samples->Portal->Small Widgets")
        '''
        Step 24 : Save page as 'Page1' and exit designer.
        '''
        pd_obj.save_page_from_toolbar("Page1")
         
        '''
        Step 25 : Click on 'My Content' folder from under 'v5_banner_test&' in content tree;
        Click on 'Page' tile from action bar.
        '''
        core_util_obj.switch_to_previous_window()
        main_page_obj.expand_repository_folder(Folder_Path+'->'+Portal_name)
        main_page_obj.right_click_folder_item_and_select_menu(item_name='My Content', click_option='double_click', item_name_index=1)
        main_page_obj.select_action_bar_tabs_option('Page')
         
        '''
        Step 26 : Choose blank template;
        Drag and drop 'Blue' from Retail Retail Samples -> Portal ->Test widgets to Page.
        '''
        core_util_obj.switch_to_new_window()
        pd_obj.select_page_designer_template('Blank')
        get_back_in_folder(self,"G520448->P292_S19901")
        pd_obj.drag_content_item_to_blank_canvas("Blue", 1, content_folder_path="Retail Samples->Portal->Test Widgets")
        
        '''
        Step 27 : Save page as 'Page2' and exit designer.
        '''
        pd_obj.save_page_from_toolbar("Page2")
        core_util_obj.switch_to_previous_window()
        
        '''
        Step 28 : Right click on 'v5_banner_test&' and click on Run
        Verify portal run mode appears as below and pages under My Content folder.
        '''
        main_page_obj.expand_repository_folder(Folder_Path)
        main_page_obj.right_click_folder_item_and_select_menu(Portal_name, context_menu_item_path='Run')
        core_util_obj.switch_to_new_window()
        pd_obj.verify_containers_title(['Panel 1', 'Category Sales', 'Panel 3'], msg="Step 28")
        
        '''
        Step 29 : Click on Page2
        Verify Page2
        '''
        obj=self.driver.find_elements_by_css_selector("[class='ibx-label-text']")
        page2=[page for page in obj if page.text=="Page2"][0]
        page2.click()
        util_obj.synchronize_with_number_of_element("[class*='grid-stack-item-content']", 4, 50)
        portal_obj_2.verify_specific_containers_title(["Blue"], msg="Step 29")
        
        '''
        Step 30 : Close portal
        '''
        core_util_obj.switch_to_previous_window()
        '''
        Step 31 :Signout WF.
        '''
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()