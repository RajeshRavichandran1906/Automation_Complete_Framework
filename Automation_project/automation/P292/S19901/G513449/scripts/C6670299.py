"""-------------------------------------------------------------------------------------------
Created on October 25, 2018
@author: Nasir
Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/6670299
Test Case Title =  Test Open item location menu  
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib.utillity import UtillityMethods
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6670299_TestClass(BaseTestCase):
    
    def test_C6670299(self):
        """    CLASS OBJECTS    """
        wf_login = login.Login(self.driver)
        wf_home = wf_mainpage.Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        
        """    COMMON TEST CASE VARIABLES    """
        project_id = utils.parseinitfile('project_id')
        suite_id = utils.parseinitfile('suite_id')
        group_id = utils.parseinitfile('group_id')
        ITEM_NAME = 'Portal for Context Menu Testing'
        EXPECTED_CONTEXTMENU_LIST=['Open', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        grid_list=['Portal for Context Menu Testing']
        FOLDER_PATH="{0}_{1}->{2}".format(project_id, suite_id, group_id)
        crumbbox_css = ".crumb-box .ibx-label-text"
        
        """    1. Sign into WebFOCUS Home Page as Admin User    """
        wf_login.invoke_home_page('mrid', 'mrpass')
        
        """    2. Click Content View from the sidebar > Click on Domains from the resource tree    """
        utils.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        wf_home.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        wf_home.select_option_from_crumb_box('Domains')
        
        """    3. Click on Portal View from the sidebar    """
        wf_home.select_portals_from_sidebar()
        utils.synchronize_with_visble_text(crumbbox_css, 'Portals', 90)
        
        """    4. Right click on the 'Portal for Context Menu T...' > Click Open item location    """
        wf_home.right_click_folder_item_and_select_menu(ITEM_NAME, 'Open item location')
        element_css="div[class^='folder-item folder-item-selected']"
        utils.synchronize_with_visble_text(element_css, ITEM_NAME, 30)
        
        """    Verify that user now in the content area under the place where the portal was created (Domains > P292_S19901 > G513445) and it is highlighted in blue and the domain/folders is in grey    """
        wf_home.verify_folders_in_grid_view(grid_list, 'asin', 'Step 04.01. Verify the portal in grid view')
        wf_home.verify_crumb_box('Domains->{0}'.format(FOLDER_PATH), "Step 04.02 : Verify that place where the portal was created (Domains > P292_S19901 > G513445)")
        
        """    5. Right click on 'Portal for Context Menu T...'
        Verify that following Context Menu appears as same in the below screenshot    """
        wf_home.verify_repository_folder_item_context_menu(ITEM_NAME, EXPECTED_CONTEXTMENU_LIST, FOLDER_PATH,'Step 05.01 Verify the context menu options')
         
        """    6. In the banner link, click on the top right username > Click Sign Out    """
        wf_home.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        