"""---------------------------------------------------------------
Author Name : Prabhakaran.
Automated On : 22-August-2019
---------------------------------------------------------------"""

from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login

class C9925814_TestClass(BaseTestCase):
    
    def test_C9925814(self):
        
        """ CLASS  OBJECTS """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        folder_path = "P292_S10660->G671733->Schedule"
        schedule_context = "Schedule_Context"
        accessList_context = "AccessList_Context"
        distribution_list_Context = "DistributionList_Context"
       
        """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.toolbar', 'Workspaces', homepage.home_page_long_timesleep)
        
        """
            STEP 02 : Under Domain tree >> Navigate to 'P292_S10660' domain >> G671733 >> Click on folder Schedule
        """
        homepage.expand_repository_folder(folder_path)
        utils.synchronize_with_visble_text('.files-box', schedule_context, homepage.home_page_short_timesleep)
        
        """
            STEP 03 : Right click on Schedule_Context
            Verify context menu
        """
        expected_context_menu = ['Edit', 'Run', 'View log', 'Disable', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(schedule_context, expected_context_menu, msg="Step 03.01")
        homepage.verify_repository_folder_item_context_submenu(schedule_context, "Security", expected_security_submenu, msg="Step 03.02")
        
        """
            STEP 04 : Right click on AccessList_Context
            Verify context menu
        """
        expected_context_menu = ['Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(accessList_context, expected_context_menu, msg="Step 04.01")
        homepage.verify_repository_folder_item_context_submenu(accessList_context, "Security", expected_security_submenu, msg="Step 04.02")
        
        """
            STEP 05 : Right click on DistributionList_Context
            Verify context menu
        """
        expected_context_menu = ['Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(distribution_list_Context, expected_context_menu, msg="Step 05.01")
        homepage.verify_repository_folder_item_context_submenu(distribution_list_Context, "Security", expected_security_submenu, msg="Step 05.02")
        
        """
            STEP 06 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()