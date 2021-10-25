'''
Created on August 16, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=170114&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2362380
TestCase Name = Verify Publish/Unpublish and Hide/Show content in Portals view does not jump to content view.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C2362380_TestClass(BaseTestCase):

    def test_C2362380(self):
        
        """
        TESTCASE VARIABLES
        """
        context_box_Item_title_css=".content-box .file-item [title*='V4 Portal'] .ibx-label-text, .content-box .file-item [title*='V4_Portal'] .ibx-label-text"
        crumb_box_css = ".crumb-box .ibx-label-text"
        files_box_css = ".content-box.ibx-widget .files-box .ibx-label-text"
        content_list=['Content', 'Portals', 'Favorites', 'Ask WebFOCUS']
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        long_wait = wfmain_obj.home_page_long_timesleep
        medium_wait = wfmain_obj.home_page_medium_timesleep
        
        
        """ Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step02: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        wfmain_obj.select_content_from_sidebar()
        
        """ Step 2: Click Portals from the sidebar.
        """
        wfmain_obj.select_portals_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Portals", medium_wait)
        utillobj.synchronize_with_visble_text(context_box_Item_title_css, 'V4 Portal', long_wait)
        
        """ Step 3: Right click on V4 Portal > Click UnPublish.
                    Verify that V4 Portal is Unpublished and Portal view does not shift to the Content View.
        """
        wfmain_obj.right_click_folder_item_and_select_menu('V4 Portal', context_menu_item_path='Unpublish')
        wfmain_obj.verify_content_area_item_publish_or_unpublish('V4 Portal', 'unpublish', 'Step 3: Verify that V4 Portal is Unpublished')
        wfmain_obj.verify_left_panel(content_list, "Step 3.1: Verify Portal view does not shift to the Content View.", default_selected='Portals')
        
        """ Step 4: Right click on V4 Portal > Click Publish.
                    Verify that V4 Portal is Published and Portal view does not shift to the Content View.
        """
        wfmain_obj.right_click_folder_item_and_select_menu('V4 Portal', context_menu_item_path='Publish')
        wfmain_obj.verify_content_area_item_publish_or_unpublish('V4 Portal', 'publish', 'Step 4: Verify that V4 Portal is Published.')
        wfmain_obj.verify_left_panel(content_list, "Step 4.1: Verify Portal view does not shift to the Content View.", default_selected='Portals')
        
        """ Step 5: Right click on V4 Portal > Click Hide.
                    Verify that V4 Portal is Hided and Portal view does not shift to the Content View.
        """
        wfmain_obj.right_click_folder_item_and_select_menu('V4 Portal', context_menu_item_path='Hide')
        wfmain_obj.verify_content_area_item_shown_or_hide('V4 Portal', 'hide', 'Step 5: Verify that V4 Portal is Hidden.')
        wfmain_obj.verify_left_panel(content_list, "Step 5.1: Verify Portal view does not shift to the Content View.", default_selected='Portals')
        
        """ Step 6: Right click on V4 Portal > Click Show.
                    Verify that V4 Portal is shown and Portal view does not shift to the Content View.
        """
        wfmain_obj.right_click_folder_item_and_select_menu('V4 Portal', context_menu_item_path='Show')
        wfmain_obj.verify_content_area_item_shown_or_hide('V4 Portal', 'shown', 'Step 6: Verify that V4 Portal is Shown.')
        wfmain_obj.verify_left_panel(content_list, "Step 6.1: Verify Portal view does not shift to the Content View.", default_selected='Portals')
        
        """ Step 7: Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        wfmain_obj.expand_repository_folder('Workspaces')
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", 90)
        wfmain_obj.select_option_from_crumb_box('Workspaces')
        
        """ Step 8: In the banner link, click on the top right username > Click Sign Out.
        """       
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        