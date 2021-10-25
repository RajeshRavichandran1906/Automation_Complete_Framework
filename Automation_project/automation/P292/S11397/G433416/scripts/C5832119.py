'''
Created on April, 2019

@author: Vpriya

Test Suite = http://172.19.2.180/testrail/index.php?/runs/view/88934&group_by=cases:section_id&group_order=asc&group_id=433416
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5832119
TestCase Name = Verify context menus for Web Content node
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators
from common.pages import wf_mainpage as mainpage_obj

class C5832119_TestClass(BaseTestCase):

    def test_C5832119(self):
        
        """
        TESTCASE OBJECTS
        """
        
        driver = self.driver #Driver reference object created
        utill_obj = utillity.UtillityMethods(driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        wftools_login_obj = login.Login(driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(driver)
        main_page_object=mainpage_obj.Wf_Mainpage(driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        
        folder_name='Web Content'
        folder_name_list=['baseapp','ibisamp']
        verify_list=['Expand','Refresh','Security']
        access_rules_window_title='Access Rules'
        rules_window_title='Rules'
        policy_title='Effective Policy'
        selcted_user='autoadmuser01 autoadmuser01'
        exp_dict={'Create Folders': 'Permitted', 'Resource Export': 'Permitted', 'Resource Import': 'Permitted', 'Open Items': 'Permitted', 'Access Resource': 'Permitted', 'Create Items': 'Permitted', 'Resource Export Download': 'Permitted', 'Manage Rules on Resources': 'Permitted', 'Edit Items': 'Permitted', 'View Rules on a Resource': 'Permitted', 'Permitted': 'Permitted', 'Delete Resources': 'Permitted', 'Resource Import Upload': 'Permitted'}
        
        """
        TESTCASE CSS
        """
        group_tab_css="div[id='SecurityResourceDialog_tabBtnGroups']"
        access_rules_cancel_button='#SecurityResourceDialog_btnCancel'
        rules_css='#ruleList'
        roles_applied_text='SelfServiceDevelopers Permitted SystemFullControl Folder and Children /WEB Subject Access Role Apply To Set On  '
        close_button_css='#btnOK'
        username_css="#userList .bi-tree-view-body-content tr[class=' selected']"
        effective_policy_css="#opsList table tbody tr td b"
        
        """
        Step 1:Sign into WebFOCUS Home Page as Admin User.
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2:Click Content View from the side bar.
        """
        main_page_obj.select_content_from_sidebar()
        utill_obj.wait_for_page_loads(main_page_obj.home_page_medium_timesleep)
        utill_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3:Right click on Web Content folder in resource tree.
        """
        """
        Verify that you see Expand/Collapse, Refresh and Security.
        """
        main_page_obj.verify_repository_folder_context_menu(folder_name,verify_list,msg='Step 03.01', verification_state='collapse')
        
        """
        Step 4:Right click on Web Content folder and select Expand.
        """
        main_page_obj.select_repository_folder_context_menu('Web Content','Expand',verification_state='collaspe')
        utill_obj.wait_for_page_loads(main_page_obj.home_page_medium_timesleep)
        
        """
        Verify that the folder is now expanded and app folders are appearing (e.g: baseapp, ibisamp)
        """
        main_page_object.verify_repository_folders(folder_name, folder_name_list, msg="Step 04.01: Verify that the folder is now expanded and app folders are appearing ",verification_state='test')
        
        """
        Step 5:Right click on Web Content folder and select Collapse.
        """
        main_page_obj.select_repository_folder_context_menu('Web Content','Collapse')
        utill_obj.wait_for_page_loads(main_page_obj.home_page_medium_timesleep)
        
        """
        Verify that the Web Content folder is collapsed now.
        """
        main_page_object.verify_repository_folders(folder_name, folder_name_list, msg="Step 05.01: Verify that the Web Content folder is collapsed now.",verification_state='test',comparion_type='asnotin')
        
        """
        Step 6:Right click on Web Content folder and select Refresh.
        """
        main_page_obj.select_repository_folder_context_menu(folder_name,'Refresh')
        utill_obj.wait_for_page_loads(main_page_obj.home_page_medium_timesleep)
        
        """
        Verify that the page is refreshed now.
        """
        utill_obj.synchronize_until_element_is_visible(locator_obj.files_item_css, main_page_obj.home_page_medium_timesleep)
        main_page_object.verify_repository_folders(folder_name, folder_name_list, msg="Step 06.01: Verify that the page is refreshed now. ",verification_state='test')
        
        """
        Step 7:Right click on Web Content node and select Security.
        """
        """
        Verify Security have the below three options.
        Rules
        Rules on this resource
        Effective policy
        """
        main_page_obj.verify_repository_folder_context_submenu(folder_name,'Security',['Rules...','Rules on this resource...', 'Effective policy...'], msg="Step 07.01: Verify that context menu options Security ")
        utill_obj.wait_for_page_loads(main_page_obj.home_page_medium_timesleep)
        
        """
        Step 8:Right click on Web Content folder and select Security > Rules.
        """
        main_page_obj.select_repository_folder_item_context_submenu(folder_name,'Security->Rules...', verification_state='Collapse')
                
        """
        Verify Rules dialog opens with tile 'Access Rules' with Groups tab open.
        """
        core_utill_obj.switch_to_new_window()
        window_title=self.driver.title
        utill_obj.asequal(access_rules_window_title,window_title,"Step 08.01: Verify Rules dialog opens with tile 'Access Rules' with Groups tab open.")
        group_tab_elem=utill_obj.validate_and_get_webdriver_object(group_tab_css,'group_tab_css')
        utill_obj.verify_object_highlighted(group_tab_elem, highlight_color='none', step_num =' 08.02')
        
        """
        Step 9:Click Cancel
        """
        access_rules_cancel_button_elem=utill_obj.validate_and_get_webdriver_object(access_rules_cancel_button,"Access_rule_cancel_button")
        core_utill_obj.python_left_click(access_rules_cancel_button_elem)
        core_utill_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 10:Right click on Web Content folder and select Security > Rules on this resource.
        """
        main_page_obj.select_repository_folder_item_context_submenu(folder_name,'Security->Rules on this resource...')
                
        """
        Verify 'Rules' dialog opens with role applied as below
        """
        core_utill_obj.switch_to_new_window()
        window_rules_title=self.driver.title
        utill_obj.asequal(rules_window_title,window_rules_title,"Step 10.01: Verify Rules dialog opens with tile 'Access Rules' with Groups tab open.")
        rules_elem=utill_obj.validate_and_get_webdriver_object(rules_css,'rules_text_css')
        rules_roles=rules_elem.text.replace('\n',' ').strip('')
        utill_obj.asequal(roles_applied_text,rules_roles,"Step 10.02: Verify 'Rules' dialog role applied ")
        
        """
        Step 11:Click Cancel
        """
        close_button_elem=utill_obj.validate_and_get_webdriver_object(close_button_css,'close')
        core_utill_obj.python_left_click(close_button_elem)
        core_utill_obj.switch_to_previous_window(window_close=False)
        utill_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Items', main_page_obj.home_page_medium_timesleep)
        """
        Step 12:Right click on Web Content folder and select Security > Effective Policy
        """
        main_page_obj.select_repository_folder_item_context_submenu(folder_name,'Security->Effective policy...')
        
        """
        Verify 'Effective Policy' dialog opens as below;
        Verify the username under users tab has been selected;
        Verify privileges permitted as below
        """
        core_utill_obj.switch_to_new_window()
        policy_window_title=self.driver.title
        utill_obj.asequal(policy_window_title,policy_title,'Step 12.01: Verify Effective Policy dialog opens as below')
        user_name_text=utill_obj.validate_and_get_webdriver_object(username_css,'username_css').text
        utill_obj.asequal(user_name_text,selcted_user,"Step 12.02: Verify the username under users tab has been selected")
        a=utill_obj.validate_and_get_webdriver_objects(effective_policy_css,"privileges")
        for i in range(0,len(a),2):
            if exp_dict[a[i].text.strip()]:
                utill_obj.asequal(exp_dict[a[i].text.strip()],'Permitted', "Step 12.03: Verify the {0} is prenet".format(a[i].text.strip()))
    
        """
        Step 13:Click Cancel
        """
        close_button_elem=utill_obj.validate_and_get_webdriver_object(close_button_css,'close')
        core_utill_obj.python_left_click(close_button_elem)
        core_utill_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 14:In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        