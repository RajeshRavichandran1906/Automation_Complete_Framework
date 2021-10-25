"""---------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 29-August-2019
---------------------------------------------------------------"""

from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login

class C9925894_TestClass(BaseTestCase):
    
    def test_C9925894(self):
        
        """ CLASS  OBJECTS """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        folder_path = "P292_S10660->G671733->Schedule"
        schedule_context = "Schedule_Context"
        accessList_context = "AccessList_Context"
        distribution_list_Context = "DistributionList_Context"
        workspaces = 'Workspaces'
       
        """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.toolbar', workspaces, homepage.home_page_long_timesleep)
        
        """
            STEP 02 : Under Domain tree >> Navigate to 'P292_S10660' domain >> G671733 >> Click on folder Schedule
        """
        homepage.expand_repository_folder(folder_path)
        utils.synchronize_with_visble_text('.files-box', schedule_context, homepage.home_page_short_timesleep)
        
        """
            STEP 03 : Right click on Schedule_Context
            Verify context menu
        """
        expected_context_menu = ['Edit', 'Run', 'View log', 'Copy Ctrl+C','Properties']
        homepage.verify_repository_folder_item_context_menu(schedule_context, expected_context_menu, msg="Step 03.01")
        
        """
            STEP 04 : Right click on AccessList_Context
            Verify context menu
        """
        expected_context_menu = ['Edit','Copy Ctrl+C','Properties']
        homepage.verify_repository_folder_item_context_menu(accessList_context, expected_context_menu, msg="Step 04.01")
        
        """
            STEP 05 : Right click on DistributionList_Context
            Verify context menu
        """
        expected_context_menu = ['Edit','Copy Ctrl+C','Properties']
        homepage.verify_repository_folder_item_context_menu(distribution_list_Context, expected_context_menu, msg="Step 05.01")
        
        """
            STEP 06 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()