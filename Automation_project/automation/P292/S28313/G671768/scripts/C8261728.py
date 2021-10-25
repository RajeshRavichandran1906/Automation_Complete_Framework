'''
Created on November 2, 2018

@author: varun
Testcase Name : Publish/Unpublish portal
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261728
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
import time

class C8261728_TestClass(BaseTestCase):
    
    def test_C8261728(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        workspaces = "Workspaces"
        
        """
        Step 1: Login WF as domain advanced user
        """
        login_obj.invoke_home_page('mridadv', 'mrpassadv')
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Verify user can see only 'v5-mypages-test1-title-changed-contenttree' and 'v5-alias-test2' portals as only those portals are published.
        """
        main_page_obj.select_option_from_crumb_box("Workspaces")
        main_page_obj.expand_repository_folder(workspaces+'->P292_S19901')
        main_page_obj.click_repository_folder('G520448')
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'v5-mypages-test1-title-changed-contenttree', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_content_area_item_publish_or_unpublish('v5-mypages-test1-title-changed-contenttree', 'publish', 'Step 3.1: Verify v5-mypages-test1-title-changed-contenttree published')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'v5-alias-test2', main_page_obj.home_page_short_timesleep)
        main_page_obj.verify_content_area_item_publish_or_unpublish('v5-alias-test2', 'publish', 'Step 3.2: Verify v5-mypages-test1-title-changed-contenttree published')
        time.sleep(5)
        
        """
        Step 4: Right click on 'v5-mypages-test1-title-changed-contenttree' portal
        Verify user can see Run option, edit doesn't appear.
        """
        main_page_obj.verify_repository_folder_item_context_menu('v5-mypages-test1-title-changed-contenttree', ['edit'],msg="Step 4.1:Verify edit doesnt appear", comparision_type='asnotin')
        main_page_obj.verify_repository_folder_item_context_menu('v5-mypages-test1-title-changed-contenttree', ['Run'],msg="Step 4.2: Verify Run appears", comparision_type='asin')
        
        """
        Step 5: Right click on 'v5-alias-test2' portal
        Verify user can see Run option, edit doesn't appear
        """
        main_page_obj.verify_repository_folder_item_context_menu('v5-alias-test2', ['edit'],msg="Step 5.1:Verify edit doesnt appear", comparision_type='asnotin')
        main_page_obj.verify_repository_folder_item_context_menu('v5-alias-test2', ['Run'],msg="Step 5.2: Verify Run appears", comparision_type='asin')
        
        """
        Step 6: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        """
        Step 7: Login WF as domain basic user
        """
        login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """
        Step 8: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 9: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Verify user can see only 'v5-mypages-test1-title-changed-contenttree' and 'v5-alias-test2' portals as only those portals are published.
        """
        main_page_obj.select_option_from_crumb_box("Workspaces")
        main_page_obj.expand_repository_folder(workspaces+'->P292_S19901')
        main_page_obj.click_repository_folder('G520448')
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'v5-mypages-test1-title-changed-contenttree', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_content_area_item_publish_or_unpublish('v5-mypages-test1-title-changed-contenttree', 'publish', 'Step 9.1: Verify v5-mypages-test1-title-changed-contenttree published in basic user')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'v5-alias-test2', main_page_obj.home_page_short_timesleep)
        main_page_obj.verify_content_area_item_publish_or_unpublish('v5-alias-test2', 'publish', 'Step 9.2: Verify v5-mypages-test1-title-changed-contenttree published in basic user')
        
        """
        Step 10: Right click on 'v5-mypages-test1-title-changed-contenttree' portal
        Verify user can see Run option, edit doesn't appear.
        """
        main_page_obj.verify_repository_folder_item_context_menu('v5-mypages-test1-title-changed-contenttree', ['edit'],msg="Step 10.1:Verify edit doesnt appear in basic user", comparision_type='asnotin')
        main_page_obj.verify_repository_folder_item_context_menu('v5-mypages-test1-title-changed-contenttree', ['Run'],msg="Step 10.2: Verify Run appears in basic user", comparision_type='asin')
        
        """
        Step 11: Right click on 'v5-alias-test2' portal
        Verify user can see Run option, edit doesn't appear.
        """
        main_page_obj.verify_repository_folder_item_context_menu('v5-alias-test2', ['edit'],msg="Step 11.1:Verify edit doesnt appear", comparision_type='asnotin')
        main_page_obj.verify_repository_folder_item_context_menu('v5-alias-test2', ['Run'],msg="Step 11.2: Verify Run appears", comparision_type='asin')
        
        """
        Step 12: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()       
        
        