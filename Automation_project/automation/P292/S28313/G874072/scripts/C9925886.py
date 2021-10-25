'''
Created on Aug 30, 2019

@author: Niranjan

Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9925886
Test case name: Context Menu:Verify Homepage Context menu for Schedule items as Developer
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C9925886_TestClass(BaseTestCase):

    def test_C9925886(self):
        
        """
        CLASS OBJECTS
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        locator = WfMainPageLocators()
        
        """
        COMMON VARIABLES 
        """
        folder_path = "P292_S10660->G671733->Schedule"
        accesslist_context = "AccessList_Context"
        distributionlist_context = "DistributionList_Context"
        schedule_context = "Schedule_Context"
        
        """
            STEP 1 : Sign into WebFOCUS Home Page as Developer User.
        """
        login.invoke_home_page("mrid", "mrpass")
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", main_page.home_page_long_timesleep)
        
        """
            STEP 2 : Under Domain tree >> Navigate to 'P292_S10660' domain >> G671733 >> Click on folder Schedule.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        main_page.expand_repository_folder(folder_path)
        utils.synchronize_with_visble_text("#files-box-area", "AccessList_Context", main_page.home_page_long_timesleep)
        
        """
            STEP 3 : Right click on Schedule_Context.
            Verify context menu,
            Edit.
            Run.
            View log.
            Disable.
            Duplicate.
            Cut.
            Copy.
            Create shortcut.
            Delete.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource/Effective policy/Owner).
            Properties.
        """
        expected_context_menu = ['Edit', 'Run', 'View log', 'Disable', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        main_page.verify_repository_folder_item_context_menu(schedule_context, expected_context_menu, msg="Step 03.01")
        main_page.verify_repository_folder_item_context_submenu(schedule_context, "Security", expected_security_submenu, msg="Step 03.02", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 4 : Right click on AccessList_Context.
            Verify context menu,
            Edit.
            Duplicate.
            Cut.
            Copy.
            Create shortcut.
            Delete.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource/Effective policy/Owner).
            Properties.
        """
        expected_context_menu = ['Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        main_page.verify_repository_folder_item_context_menu(accesslist_context, expected_context_menu, msg="Step 04.01")
        main_page.verify_repository_folder_item_context_submenu(accesslist_context, "Security", expected_security_submenu, msg="Step 04.02", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 5 : Right click on DistributionList_Context    
            Verify context menu,
            Edit.
            Duplicate.
            Cut.
            Copy.
            Create shortcut.
            Delete.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource/Effective policy/Owner).
            Properties.
        """
        expected_context_menu = ['Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        main_page.verify_repository_folder_item_context_menu(distributionlist_context, expected_context_menu, msg="Step 05.01")
        main_page.verify_repository_folder_item_context_submenu(distributionlist_context, "Security", expected_security_submenu, msg="Step 05.02", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 6 : In the banner link, click on the top right username > Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()  