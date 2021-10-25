'''
Created on Aug 13, 2019

@author: Nirajan

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2509730
Test case Name =  Add Metadata option as a new action bar button
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.locators import wf_mainpage_locators

class C2509730_TestClass(BaseTestCase):

    def test_C2509730(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
            COMMON TEST CASE VARIABLES 
        """
        folder    = core_utils.parseinitfile('folder')
        
        repository_folder = 'Domains->{0}'.format(folder)
                                                           
        '''
        Step 1 : Log into WebFOCUS as WF_Administrator.
        '''
        login.invoke_home_page('mridadm', 'mrpassadm')
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        '''
        Step 2 : Select any folder/domain >> Select 'Data' Tile >> Click on 'Metadata' action bar.
        '''
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Data", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tab("Data")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Metadata", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option("Metadata")
        core_utils.switch_to_new_window()
        
        '''
        Step 2.00 : Verify RS console page is displayed.
        '''
        utils.synchronize_with_visble_text('#WcMultiframesMFObject-1 #WcMultiframesContentView-2', 'Left', main_page.home_page_medium_timesleep)
        utils.verify_object_visible('#WcMultiframesMFObject-1 #WcMultiframesContentView-2 div[id*="ibxGrid"]', True, 'Step 2.00 : Verify RS console page is displayed')
        core_utils.switch_to_previous_window()
        
        '''
        Step 3 : In the banner link, click on the top right username > Click Sign Out.
        '''
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()