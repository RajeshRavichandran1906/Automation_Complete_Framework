'''
Created on December 11,2018

@author: Magesh

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/19901&group_by=cases:section_id&group_id=512962&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261587
TestCase Name = Verify the Category Buttons and Action Tiles for basic users
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib import utillity
from common.lib.global_variables import Global_variables

class C8261587_TestClass(BaseTestCase):

    def test_C8261587(self):
        
        """
        TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        long_wait = 190
        
        """ 
        Step 1: Sign into WebFOCUS Home Page as bas User.
        """
        wftools_login_obj.invoke_home_page('mridbas', 'mrpassbas')
        utillobj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, long_wait)
                
        """
        Step 2: Click Content View from the side bar
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait*5)
        
        """ 
        Step 3: Click on Retail Samples from the resource tree
        """
        wfmain_obj.click_repository_folder('Retail Samples')
        
        """ 
        Step 3.1: Verify NO action bar is displayed
        """
        actionbar_folder_css='.create-new-box .domains-new-items-box div[data-ibxp-text^="Folder"]'
        utillobj.verify_object_visible(actionbar_folder_css, False, "Step 3.1: Verify NO action bar is displayed")
        
        """ 
        Step 4: Click on 'My Content' folder
        """
        wfmain_obj.click_repository_folder('My Content')
        
        """ 
        Step 4.1: Verify that 2 action bars (Folder, Shortcut) is displayed
        """
        labels_list=['Folder','Shortcut']
        wfmain_obj.verify_action_bar_tab_specific_options(labels_list, 'Step 4.1: Verify that 2 action bars (Folder, Shortcut) is displayed')
        
        """ 
        Step 5: Click on toggle to hide the action bar
        """
        wfmain_obj.collapse_action_bar()
        
        """ 
        Step 5.1: Verify that action bar is Collapsed
        """
        time.sleep(Global_variables.longwait)
        action_bar_css = ".create-new-box .domains-new-items-box[style='']"
        utillobj.verify_object_visible(action_bar_css, False, "Step 5.1: Verify that action bar is Collapsed")
        
        labels_list=[]
        wfmain_obj.verify_action_bar_tab_specific_options(labels_list, 'Step 5.2: Verify that action bar is Collapsed')
        
        """ 
        Step 6: Again Click on toggle
        """
        wfmain_obj.expand_action_bar()
        
        """ 
        Step 6.1: Verify that action bar is Expanded
        """
        labels_list=['Folder','Shortcut']
        wfmain_obj.verify_action_bar_tab_specific_options(labels_list, 'Step 6.1: Verify that action bar is Expanded')
        
        """ 
        Step 7: In the banner link, click on the top right username > Click Sign Out
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        