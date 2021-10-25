'''
Created on Oct 26, 2018

@author: Nasir

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/19901&group_by=cases:section_id&group_id=513448&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8261560
TestCase Name = Test Add to/Remove from Favorites using Administrator
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C8261560_TestClass(BaseTestCase):

    def test_C8261560(self):
        
        """
        TESTCASE VARIABLES
        """
        content_list=['Content', 'Portals', 'Favorites', 'Ask WebFOCUS']
        crumb_box_css = ".crumb-box .ibx-label-text"
        workspace = "Workspaces"
        wait = 15
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        loc_obj=wf_mainpage_locators.WfMainPageLocators()

        """    1. Sign into WebFOCUS Home Page as Admin/Developers User.    """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        time.sleep(wait) # this is required in firefox before loading take place 
        utillobj.wait_for_page_loads(wfmain_obj.home_page_long_timesleep)
               
        """    2. Click Content View from the sidebar > Click on Domains from the resource tree    """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, workspace, wfmain_obj.home_page_long_timesleep)
        wfmain_obj.select_option_from_crumb_box(workspace)
        
        """    3. If not expand Domains > 'P292_S19901' > 'G513445' folder from the resource tree    """
        """    4. Right click on 'Portal for Context Menu Testing2' > Click Add to Favorites    """
        utillobj.wait_for_page_loads(wfmain_obj.home_page_long_timesleep)
        wfmain_obj.right_click_folder_item_and_select_menu("Portal for Context Menu Testing2", 'Add to Favorites', 'P292_S19901->G513445')
        
        """    Verify that Favorite added popup opens with a background transparent green layer over the popup.    """
        utillobj.verify_notify_popup(notify_text="Favorite added", msg='Step 04.01')
        
        """    5. Click on Favorites View from the sidebar    """
        wfmain_obj.select_favorites_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", wfmain_obj.home_page_long_timesleep)
        utillobj.wait_for_page_loads(wfmain_obj.home_page_long_timesleep)
        
        """    Verify that 'Portal for Context Menu T...' appears    """
        wfmain_obj.verify_left_panel(content_list, "Step 05.01: Verify Favorites View is selected.", default_selected='Favorites')
        wfmain_obj.verify_items_in_grid_view(['Portal for Context Menu Testing2'], 'asin', "Step 05.02: Verify Portal for Context Menu Testing item listed under Favorites")
        
        """    6. Right click on 'Portal for Context Menu Testing' > Click Remove from Favorites    """
        wfmain_obj.right_click_folder_item_and_select_menu('Portal for Context Menu Testing2', 'Remove from Favorites')
        
        """    Verify that 'Portal for Context Menu T...' favorite has been removed    """
        utillobj.synchronize_with_visble_text(loc_obj.content_area_css, 'Portal for Context Menu Testing2', wfmain_obj.home_page_long_timesleep,condition_type='asnotin')
        utillobj.synchronize_with_number_of_element(loc_obj.FAVORITE_ICON_CSS, 1,wfmain_obj.home_page_long_timesleep)
        wfmain_obj.verify_items_in_grid_view(['Portal for Context Menu Testing2'], 'asnotin', "Step 06.01: Portal for Context Menu Testing item removed under Favorites")
        
        """    7. In the banner link, click on the top right username > Click Sign Out.    """
        wfmain_obj.select_content_from_sidebar()
        wfmain_obj.select_option_from_crumb_box(workspace)
        utillobj.wait_for_page_loads(wfmain_obj.home_page_long_timesleep)
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        