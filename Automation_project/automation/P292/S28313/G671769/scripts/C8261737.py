'''
Created on April 4,2019

@author: Niranjan/Samuel
Testcase Name : Check navigations with PX setting then back to %
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261737
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools import designer_portal

class C8261737_TestClass(BaseTestCase):
    
    def test_C8261737(self):
        
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        loc_obj = wf_mainpage_locators.WfMainPageLocators()
        design_por_obj = designer_portal.Portal(self.driver)
        portal_banner_obj = designer_portal.Banner(self.driver)
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        page_canvas_css = '#pagespane'
        container_css = ".pvd-container"
           
        """
        Test case variables
        """
        expected_domain = "P292_S19901"
        expected_folder = 'G671769'
        portal_title_one = 'Portal with 1500px Two side nav'
        portal_title_two = 'Portal with 900px Three level nav'
        portal_title_three = 'Portal with 1500px Two top level nav'
        input_list_one = ['90px','90px','0px','0px']
        input_list_one_1 = ['210px','210px','0px','0px']
        input_list_two = ['390px','390px','0px','0px']
        input_list_two_1 = ['210px','210px','0px','0px']
        input_list_three = ['0px','0px','0px','0px']
        input_list_three_1 = ['0px','0px','0px','0px']
        padding_sides = ['left','right','top','bottom']
        
        '''
        Local function
        '''
        def padding_verification(input_list, msg):
            '''
            Desc: This function is used to verify the portal width padding property 
            '''
            util_obj = utillity.UtillityMethods(self.driver)
            container_obj = util_obj.validate_and_get_webdriver_object(container_css, "container")
            padding_list = []
            for side in padding_sides:
                padding_list.append(util_obj.get_element_css_propery(container_obj,'padding-{0}'.format(side)).strip())
            util_obj.as_List_equal(input_list, padding_list, msg)
            
        """
        Step 1: Login WF as domain developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """ 
        Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains')
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 3: Expand 'P292_S19901' domain-> Click on 'G671769' folder;
        Select Designer tag and click on Portal tile in action bar    
        """
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder)
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab('Designer')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Portal',main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Portal')
        
        """
        Step 4: Enter title as 'Portal with 1500px Two side nav';
                Enter 1500px inside maximum width text box;
                Click on 'Create My pages menu' check box;
                Click create
        """
        
        design_por_obj.title_textbox_in_new_or_edit_portal_dialog(portal_title_one)
        design_por_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='1500px')
        design_por_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog('check')
        design_por_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(5)
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, portal_title_one, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Right click on 'Portal with 1500px Two side nav' and select Publish
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title_one, 'Publish')
        util_obj.wait_for_page_loads(5)
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        
        """
        Step 6: Right click on 'Portal with 1500px Two side nav' and select Run
        Verify portal width and navigation appears as below
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title_one, 'Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(page_canvas_css, main_page_obj.home_page_long_timesleep)
        portal_banner_obj.verify_portal_top_banner_title(portal_title_one, 'Step 6.1: Verify portal banner title')
        padding_verification(input_list_one, 'Step 6.2: Verify portal width and navigation appears as below')
        
        """
        Step 7: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        
        """
        Step 8: Right click on 'Portal with 1500px Two side nav' and select Edit
        """
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(portal_title_one, 'Edit')
        
        """
        Step 9: Enter 75% on maximum width and click save
        """
        design_por_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='75%')
        design_por_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(5)
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        
        """
        Step 10: Right click on 'Portal with 1500px Two side nav' and select Run
        Verify portal width and navigation appears as below
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title_one, 'Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(page_canvas_css, main_page_obj.home_page_long_timesleep)
        padding_verification(input_list_one_1, 'Step 10.1: Verify portal width and navigation appears as below')
        
        """
        Step 11: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
           
        """
        Step 12: Click on 'G671769' folder;
                 Select Designer tag and click on Portal tile in action bar.
        """  
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder)
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab('Designer')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Portal',main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Portal')
        
        """
        Step 13: Enter title as 'Portal with 900px Three level nav';
                 Enter 900px inside maximum width text box;
                 Click on 'Create My pages menu' check box;
                 Click create.
        """
        design_por_obj.title_textbox_in_new_or_edit_portal_dialog(portal_title_two)
        design_por_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='900px')
        design_por_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog('check')
        design_por_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog('check')
        design_por_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(5)
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, portal_title_two, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 14: Right click on 'Portal with 900px Three level nav' and select Publish
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title_two, 'Publish')
        util_obj.wait_for_page_loads(5)
        
        """
        Step 15: Right click on 'Portal with 900px Three level nav' and select Run
        Verify portal width and navigation appears as below
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title_two, 'Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(page_canvas_css, main_page_obj.home_page_long_timesleep)
        portal_banner_obj.verify_portal_top_banner_title(portal_title_two, 'Step 15.1: Verify portal banner title')
        padding_verification(input_list_two, 'Step 15.2: Verify portal width and navigation appears as below')
        
        """
        Step 16: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        
        """
        Step 17: Right click on 'Portal with 900px Three level nav' and select Edit
        """
        util_obj.wait_for_page_loads(5)
        main_page_obj.right_click_folder_item_and_select_menu(portal_title_two, 'Edit')
        
        """
        Step 18: Enter 75% on maximum width and click save
        """
        design_por_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='75%')
        design_por_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(5)
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        
        """
        Step 19: Right click on 'Portal with 900px Three level nav' and select Run
        Verify portal width and navigation appears as below
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title_two, 'Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(page_canvas_css, main_page_obj.home_page_long_timesleep)
        padding_verification(input_list_two_1, 'Step 19.1: Verify portal width and navigation appears as below')
        
        """
        Step 20: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        
        """
        Step 21: Click on 'G671769' folder;
                 Select Designer tag and click on Portal tile in action bar.
        """
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder)
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab('Designer')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Portal',main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Portal')
        
        """
        Step 22: Enter title as 'Portal with 1500px Two top level nav';
                 Enter 1500px inside maximum width text box;
                 Click on 'Create My pages menu' check box;
                 Click create.
        """
        design_por_obj.title_textbox_in_new_or_edit_portal_dialog(portal_title_three)
        design_por_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='1500px')
        design_por_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog('check')
        design_por_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog('check')
        design_por_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(5)
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, portal_title_three, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 23: Right click on 'Portal with 1500px Two top level nav' and select Publish
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title_three, 'Publish')
        util_obj.wait_for_page_loads(5)
        
        """
        Step 24: Right click on 'Portal with 1500px Two top level nav' and select Run
        Verify that the portal appears in maximum width (full screen)
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title_three, 'Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(page_canvas_css, main_page_obj.home_page_long_timesleep)
        portal_banner_obj.verify_portal_top_banner_title(portal_title_three, 'Step 24.1: Verify portal banner title')
        padding_verification(input_list_three, 'Step 24.2: Verify that the portal appears in maximum width (full screen)')
        
        """
        Step 25: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        
        """
        Step 26: Right click on 'Portal with 1500px Two top level nav' and select Edit
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title_three, 'Edit')
        
        """
        Step 27: Enter 75% on maximum width and click save
        """
        design_por_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='75%')
        design_por_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(5)
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        
        """
        Step 28: Right click on 'Portal with 1500px Two top level nav' and select Run
        Verify portal width and navigation appears as below
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title_three, 'Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(page_canvas_css, main_page_obj.home_page_long_timesleep)
        padding_verification(input_list_three_1, 'Step 28.1: Verify portal width and navigation appears as below')
        
        """
        Step 29: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        
if __name__ == '__main__':
    unittest.main()