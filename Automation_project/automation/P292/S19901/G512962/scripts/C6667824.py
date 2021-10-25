'''
Created on Dec 11, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6667824
Testcase Name : Verify the Category Buttons and Action Tiles for Adv User
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables

class C6667824_TestClass(BaseTestCase):

    def test_C6667824(self):
        
        """
        TESTCASE_OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        my_content_folder='My Content'
        domain_folder='Retail Samples'
        folder_path='{0}->{1}'.format(domain_folder,my_content_folder)
        
        """
        Step 1:Sign into WebFOCUS Home Page as Adv User
        """
        login_obj.invoke_home_page('mridadv', 'mrpassadv')
 
        """
        Step 2:Click Content View from the side bar
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3:Click on Retail Samples from the resource tree
        Verify NO action bar is displayed
        """
        main_page_obj.click_repository_folder(domain_folder)
        util_obj.synchronize_until_element_disappear(WfMainPageLocators.ACTION_BAR_CSS, 5)
        main_page_obj.verify_action_bar_is_not_visible("Step 3:1: Verify NO action bar is displayed")
        
        """
        Step 4:Click on 'My Content' folder
        Verify that 5 category buttons (Common, Designer, InfoAssist, Schedule and Other) are displayed, by default 'Common category button is selected.
        Also, verify that 5 action bars (Folder, Workbook, Chart, Report , Page) is displayed under common category
        """
        common_action_bar_items=['Folder','Workbook','Chart','Report','Page']
        action_bar_tab_buttons=['Common','Designer','InfoAssist','Schedule','Other']
        main_page_obj.expand_repository_folder(folder_path)
        main_page_obj.verify_action_bar_all_tabs(action_bar_tab_buttons, 'Step 4:1: Verify Mycontent bar buttons'.format(action_bar_tab_buttons))
        main_page_obj.verify_selected_action_bar_tab(['Common'], "Step 4:2:Verify Common action bar is selected")
        main_page_obj.verify_action_bar_tab_all_options(common_action_bar_items, 'Step 4:3:Verify Common action bar items'.format(common_action_bar_items))
        
        """
        Step 5:Click on 'Designer' category buttons
        Verify 3 Action Bar ( Workbook, Chart, Page) is displayed
        """
        action_bar_items=['Workbook','Chart','Page']
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.verify_action_bar_tab_all_options(action_bar_items, 'Step 5:1: Verify Desginer category action bar items'.format(action_bar_items))
        
        """
        Step 6:Click on 'InfoAssist' category buttons
        Verify 6 Action Bar (Chart, Visualization, Report, Document, Sample content, Alert) is displayed
        """
        infoassist_category_buttons=['Chart', 'Visualization', 'Report', 'Document', 'Sample Content', 'Alert']
        main_page_obj.select_action_bar_tab('InfoAssist')
        main_page_obj.verify_action_bar_tab_all_options(infoassist_category_buttons, 'Step 6:1: Verify Infoassist category action bar items'.format(infoassist_category_buttons))

        """
        Step 7:Click on 'Schedule' category buttons
        Verify 2 Action Bar ( Access List, Distribution List) is displayed
        """
        schedule_category_action_bar_items=['Access List', 'Distribution List']
        main_page_obj.select_action_bar_tab('Schedule')
        main_page_obj.verify_action_bar_tab_all_options(schedule_category_action_bar_items,'Step 7:1: Verify Schedule action bar ribbon items'.format(schedule_category_action_bar_items))
        
        """
        Step 8:Click on 'Other' category buttons
        Verify 4 Action Bar (Folder, Upload File, URL, Shortcut) is displayed
        """
        other_action_bar_items=['Folder','Upload File','URL','Shortcut']
        main_page_obj.select_action_bar_tab('Other')
        main_page_obj.verify_action_bar_tab_all_options(other_action_bar_items,'Step 8:1: Verify Other action bar ribbon items'.format(other_action_bar_items))

        """
        Step 9:In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()