"""---------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 21-August-2019
Testcase title: Context Menu:Verify Homepage Context menu for Domain/Folders as Admin.
---------------------------------------------------------------"""

from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.login import Login

class C9917338_TestClass(BaseTestCase):
    
    def test_C9917338(self):
        
        """ CLASS  OBJECTS """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        project_id = core_utils.parseinitfile('project_id')
        suite_id = core_utils.parseinitfile('suite_id')
        folder_path = project_id+'_'+suite_id
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.toolbar', 'Workspaces', homepage.home_page_long_timesleep)
        
        """
            STEP 02 : Under Domain tree >> Navigate to 'P292_S10660' domain
        """
        homepage.expand_repository_folder(folder_path)
        utils.synchronize_with_visble_text('.content-box', 'Folders', homepage.home_page_short_timesleep)
        
        """
        STEP 02 : Verify Context Menu,
        Expand/Collapse.
        Paste (Grayed out).
        Delete.
        Refresh.
        General Access (All Users/Domain Groups[Default Selection]).
        Publish/Unpublish.
        Show/Hide.
        Security (Rules/Rules on this resource/Effective Policy/Owner).
        Properties.
        """
        homepage.verify_repository_folder_context_menu(folder_path,['Collapse', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'General access', 'Unpublish', 'Hide', 'Security', 'Properties'], msg ="Step 02:01")
        paste_element = utils.validate_and_get_webdriver_object('[data-ibx-type="ibxMenuItem"][action="paste"]',"Paste_element")
        paste_grey_out_value =utils.get_element_css_propery(paste_element,'opacity')
        utils.asequal(paste_grey_out_value,'0.5',"Step:03 Paste (Grayed out).")
        banner_elem = utils.validate_and_get_webdriver_object(".banner-group-spacer","banner_area")
        core_utils.python_left_click(banner_elem)
        homepage.verify_repository_folder_context_submenu(folder_path, 'General access', ['All users', 'Workspace groups'], msg="Step 02:02")
        homepage.verify_repository_folder_context_submenu(folder_path, 'Security', ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'], msg="Step 02:03")
        
        
        """
        Step 03:Under Domain Tree >> Right-click on My Content folder underneath 'P292_S10660' domain.
        Verify Context Menu,
        Expand/Collapse.
        Paste (Grayed out).
        Delete.
        Refresh.
        Security (Rules/Rules on this resource/Effective Policy/Owner).
        Share/Unshare.
        Share with.
        Properties.
        """
        homepage.verify_repository_folder_context_menu(folder_path+'->My Content',['Collapse', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Security', 'Share', 'Share with...', 'Properties'],msg ="Step 03:01")
        paste_element = utils.validate_and_get_webdriver_object('[data-ibx-type="ibxMenuItem"][action="paste"]',"Paste_element")
        paste_grey_out_value =utils.get_element_css_propery(paste_element,'opacity')
        utils.asequal(paste_grey_out_value,'0.5',"Step:03.02 Paste (Grayed out).")
        banner_elem = utils.validate_and_get_webdriver_object(".banner-group-spacer","banner_area")
        core_utils.python_left_click(banner_elem)
        homepage.verify_repository_folder_context_submenu(folder_path, 'Security', ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'], msg="Step 03:03")
        
        """
        Step 04:Under Domain Tree >> Right-click on Hidden Content folder underneath 'P292_S10660' domain.
        Verify Context Menu,
        Expand/Collapse.
        Duplicate.
        Cut.
        Copy.
        Paste (Grayed out).
        Delete.
        Refresh.
        Unpublish/Publish.
        Show/Hide.
        Security (Rules/Rules on this resource/Effective Policy/Owner).
        Properties.
        """
        homepage.verify_repository_folder_context_menu(folder_path+'->Hidden Content',['Collapse', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Unpublish', 'Show', 'Security', 'Properties'],msg ="Step 04:01")
        paste_element = utils.validate_and_get_webdriver_object('[data-ibx-type="ibxMenuItem"][action="paste"]',"Paste_element")
        paste_grey_out_value =utils.get_element_css_propery(paste_element,'opacity')
        utils.asequal(paste_grey_out_value,'0.5',"Step:03.02 Paste (Grayed out).")
        banner_elem = utils.validate_and_get_webdriver_object(".banner-group-spacer","banner_area")
        core_utils.python_left_click(banner_elem)
        homepage.verify_repository_folder_context_submenu(folder_path, 'Security', ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'], msg="Step 04:02")

        """
        Step 05:Under Domain Tree >> Right-click on G671733 folder underneath 'P292_S10660' domain.
        Verify Context Menu,

        Expand/Collapse.
        Duplicate.
        Cut.
        Copy.
        Paste (Grayed out).
        Delete.
        Refresh.
        Unpublish/Publish.
        Hide/Show.
        Security (Rules/Rules on this resource/Effective Policy/Owner).
        Properties.
        """
        homepage.verify_repository_folder_context_menu(folder_path+'->G671733',['Collapse', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Unpublish', 'Hide', 'Security', 'Properties'],msg="Step 05:01")
        paste_element = utils.validate_and_get_webdriver_object('[data-ibx-type="ibxMenuItem"][action="paste"]',"Paste_element")
        paste_grey_out_value =utils.get_element_css_propery(paste_element,'opacity')
        utils.asequal(paste_grey_out_value,'0.5',"Step:05.03 Paste (Grayed out).")
        banner_elem = utils.validate_and_get_webdriver_object(".banner-group-spacer","banner_area")
        core_utils.python_left_click(banner_elem)
        homepage.verify_repository_folder_context_submenu(folder_path, 'Security', ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'], msg="Step 05:02")
        
        
        
        """
            STEP 06 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()