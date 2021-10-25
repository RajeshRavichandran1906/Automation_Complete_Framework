'''
Created on Oct 26, 2018

@author: Nasir

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/19901&group_by=cases:section_id&group_id=513448&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8261564
TestCase Name = Portal Menu Defaults using Developers
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity, core_utility

class C8261564_TestClass(BaseTestCase):

    def test_C8261564(self):
        
        """
        TESTCASE VARIABLES
        """
        long_wait = 190
        crumb_box_css = ".crumb-box .ibx-label-text"
        ITEM_NAME = 'Portal for Context Menu Testing'
        EXPECTED_CONTEXT_MENU = ['Run', 'Remove from Favorites', 'Properties']
        workspace = "Workspaces"
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        coreutil_obj = core_utility.CoreUtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)

        """    1. Sign into WebFOCUS Home Page as Developers User.    """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """    2. Click Content View from the sidebar > Click on Domains from the resource tree    """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, workspace, 30, 1)
        wfmain_obj.select_option_from_crumb_box(workspace)
        
        """    3. If not expand Domains > 'P292_S19901' > 'G513445' folder from the resource tree    """
        """    4. Right click on 'Portal for Context Menu Testing' > Click Add to Favorites    """
        wfmain_obj.right_click_folder_item_and_select_menu(ITEM_NAME, 'Add to Favorites', 'P292_S19901->G513445')
        
        """    Verify that Favorite added popup opens with a background transparent green layer over the popup.    """
        utillobj.verify_notify_popup(notify_text="Favorite added", msg='Step 04a')
        
        """    5. Click on Favorites View from the sidebar    """
        wfmain_obj.select_favorites_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", long_wait)
        """    Verify that 'Portal for Context Menu T...' appears    """
        wfmain_obj.verify_items_in_grid_view(['Portal for Context Menu Testing'], 'asin', "Step 05b: Verify Portal for Context Menu Testing item listed under Favorites")
        
        """    6. Right click on 'Portal for Context Menu T...'    """
        """    Verify that 'Run', 'Remove from Favorites', and 'Properties' context menus are displayed    """
        wfmain_obj.verify_repository_folder_item_context_menu(ITEM_NAME, EXPECTED_CONTEXT_MENU, msg = 'Step 06a')
        
        """    7. In the banner link, click on the top right username > Click Sign Out.    """
        wfmain_obj.select_content_from_sidebar()
        crumb_elems=driver.find_elements_by_css_selector(crumb_box_css)
        domain_obj=[elem for elem in crumb_elems if elem.text.strip()==workspace][0]
        coreutil_obj.left_click(domain_obj)
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        