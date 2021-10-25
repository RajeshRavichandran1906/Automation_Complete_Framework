'''
Created on Aug 30, 2019

@author: Niranjan
Test rail link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9925908
Test case title: Context Menu:Verify Homepage Context menu for Schedule items as Basic User.
'''
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.login import Login

class C9925908_TestClass(BaseTestCase):
    
    def test_C9925908(self):
        
        """ CLASS  OBJECTS """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        folder_path = "P292_S10660->G671733->Schedule"
        schedule_context = "Schedule_Context"
        accessList_context = "AccessList_Context"
        distribution_list_Context = "DistributionList_Context"
        workspace = "Workspaces"
       
        """
            STEP 01 : Sign into WebFOCUS Home Page as basic User.
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.toolbar', workspace, homepage.home_page_long_timesleep)
        
        """
            STEP 02 : Under Domain tree >> Navigate to 'P292_S10660' domain >> G671733 >> Click on folder Schedule
        """
        homepage.expand_repository_folder(folder_path)
        utils.synchronize_with_visble_text('.files-box', schedule_context, homepage.home_page_short_timesleep)
        left_panel_elem = utils.validate_and_get_webdriver_object(".left-main-panel","left_area_panel")
        core_utils.python_left_click(left_panel_elem)
        
        """
            STEP 03 : Right click on Schedule_Context
            Verify context menu
            Run.
            Properties.
        """
        expected_context_menu = ['Run', 'Properties']
        homepage.verify_repository_folder_item_context_menu(schedule_context, expected_context_menu, msg="Step 03.01")
        left_panel_elem = utils.validate_and_get_webdriver_object(".left-main-panel","left_area_panel")
        core_utils.python_left_click(left_panel_elem)
        
        """
            STEP 04 : Right click on AccessList_Context
            Verify context menu
            View Only 
            Properties
        """
        expected_context_menu = ['View Only', 'Properties']
        homepage.verify_repository_folder_item_context_menu(accessList_context, expected_context_menu, msg="Step 04.01")
        left_panel_elem = utils.validate_and_get_webdriver_object(".left-main-panel","left_area_panel")
        core_utils.python_left_click(left_panel_elem)
        
        """
            STEP 05 : Right click on DistributionList_Context
            Verify context menu
            View Only 
            Properties
        """
        expected_context_menu = ['View Only', 'Properties']
        homepage.verify_repository_folder_item_context_menu(distribution_list_Context, expected_context_menu, msg="Step 05.01")
        left_panel_elem = utils.validate_and_get_webdriver_object(".left-main-panel","left_area_panel")
        core_utils.python_left_click(left_panel_elem)
        
        """
            STEP 06 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()