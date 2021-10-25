'''
Created on April 5, 2019

@author: varun
Testcase Name : Create Populated Unlocked Base Page 
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261634
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C8261634_TestClass(BaseTestCase):
    
    def test_C8261634(self):
        """
        Test_case objects
        """
        page_designer_obj = Design(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        Test case CSS
        """
        action_bar_css = "div[data-ibxp-text=\"Action Bar\"]"
        new_page_css = ".ibx-title-bar-caption"
        content_area_css = ".content-box .files-box-files"
        
        """
        Test case variables
        """
        action_bar_text = "Action Bar"
        new_page_name = 'New Page'
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        folder_name_path=folder_name+'->'+group_id
        
        """
        Step 1: Login WF as developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content view from side bar
        """
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G671753' folder -> 'v5portal1dev' portal;
        click on Page
        """
        main_page_obj.expand_repository_folder('Domains->'+folder_name_path+'->v5portal1dev')
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_short_timesleep)
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(new_page_css, new_page_name, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Choose Grid 2-1 template
        """
        page_designer_obj.select_page_designer_template('Grid 2-1')
        
        """
        Step 5: Expand Retail samples --> Portal --> Test widget;
        Add Red, Silver and Yellow to Panel 1,2 and 3 respectively
        """
        pass