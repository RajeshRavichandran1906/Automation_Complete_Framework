'''
Created on December 11, 2018

@author: varun
Testcase Name : Verify the Category Buttons and Action Tiles for Admin User
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261582
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators

class C8261582_TestClass(BaseTestCase):
    
    def test_C8261582(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        action_bar_css = "div[data-ibxp-text=\"Action Bar\"]"
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        domain_action_button_css = ".tpg-selected .create-new-item[role='button']"
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        repository_folder = project_id + '_' + suite_id
        action_bar_text = 'Action Bar'
        domains_repository = 'Domains'
        domains_actionbar_list = ['Domain','Folder']
        folders_title = 'Folders'
        action_bar_tabs = ['Common','Data','Designer','InfoAssist','Schedule','Other']
        action_button_list = ['Folder','Upload Data','Connect','Workbook','Chart','Report','Page']
        data_action_button = ['Upload Data','Connect','Metadata','Reporting Object']
        designer_action_button = ['Workbook','Chart','Page','Portal']
        infoassist_action_button = ['Chart', 'Visualization', 'Report', 'Document', 'Sample Content', 'Alert']
        schedule_action_button = ['Access List','Distribution List','Schedule']
        other_action_button = ['Folder', 'Upload File', 'URL', 'Shortcut', 'Text Editor', 'Blog', 'Portal Page', 'Collaborative Portal']
        
        """
        Step 1: Sign into WebFOCUS Home Page as Basic User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar
        """
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on Domains from the resource tree.
        Verify the Action bar shows 'Domain' and 'Folder' action tiles only.
        """
        main_page_obj.expand_repository_folder(domains_repository)
        util_obj.synchronize_with_visble_text(action_bar_css, action_bar_text, base_obj.home_page_medium_timesleep)
        main_page_obj.verify_action_bar_tab_all_options(domains_actionbar_list, "Step 3.1: verify Domain and Folders are present")
        
        """
        Step 4: Click on domain 'P292_S19901_G512418' from the resource tree.
        Verify Action Bar shows the following 6 category buttons (Common category button selected by default).
        (Common, Data, Designer, InfoAssist, Schedule, Other)
        Verify the following 7 action tiles under the common Category.
        (Folder, Upload Data, Connect, Workbook, Chart, Report, Page)
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(folders_text_css, folders_title, base_obj.home_page_medium_timesleep)
        main_page_obj.verify_selected_action_bar_tab(['Common'], 'Step 4.1: Verify Common is selected')
        main_page_obj.verify_action_bar_all_tabs(action_bar_tabs, "Step 4.2: Verify 6 tabs are present")
        main_page_obj.verify_action_bar_tab_all_options(action_button_list,'Step 4.3: Verify all Action buttons are present' )
        
        """
        Step 5: Click on 'Data' category button.
        Verify the following 4 action tiles under the Data category.
        (Upload Data, Connect, Metadata, Reporting Object)
        """
        main_page_obj.select_action_bar_tab('Data')
        util_obj.synchronize_with_number_of_element(domain_action_button_css, 4, base_obj.home_page_medium_timesleep)
        main_page_obj.verify_action_bar_tab_all_options(data_action_button,'Step 5.1: Verify 4 action buttons under data' )
        
        """
        Step 6: Click on 'Designer' category button.
        Verify the following 4 action tiles under the Designer category.
        (Workbook, Chart, Page, Portal)
        """ 
        main_page_obj.select_action_bar_tab('Designer')
        util_obj.synchronize_with_number_of_element(domain_action_button_css, 4, base_obj.home_page_medium_timesleep)
        main_page_obj.verify_action_bar_tab_all_options(designer_action_button,'Step 6.1: Verify 4 action buttons under designer')
        
        """
        Step 7: Click on 'InfoAssist' category button.
        Verify the following 6 action tiles under the InfoAssist category.
        (Chart, Visualization, Report, Document, Sample Content, Alert)
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        util_obj.synchronize_with_number_of_element(domain_action_button_css, 6, base_obj.home_page_medium_timesleep)
        main_page_obj.verify_action_bar_tab_all_options(infoassist_action_button,'Step 7.1: Verify 6 action buttons under Infoassist')
        
        """
        Step 8: Click on 'Schedule' category button.
        Verify the following 3 action tiles under the Schedule category.
        (Access List, Distribution List, Schedule)
        """
        main_page_obj.select_action_bar_tab('Schedule')
        util_obj.synchronize_with_number_of_element(domain_action_button_css, 3, base_obj.home_page_medium_timesleep)
        main_page_obj.verify_action_bar_tab_all_options(schedule_action_button,'Step 8.1: Verify 3 action buttons under Schedule')
        
        """
        Step 9: Click on 'Other' category button. 
        Verify the following 8 action tiles under the Other category.
        (Folder, Upload File, URL, Shortcut, Text Editor, Blog, Portal Page, Collaborative Portal)
        """
        main_page_obj.select_action_bar_tab('Other')
        util_obj.synchronize_with_number_of_element(domain_action_button_css, 8, base_obj.home_page_medium_timesleep)
        main_page_obj.verify_action_bar_tab_all_options(other_action_button,'Step 9.1: Verify 8 action buttons under Other')
        
        """
        Step 10: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()