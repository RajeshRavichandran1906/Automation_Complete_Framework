'''
Created on Nov 8, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261531
Testcase Name :  Test Delete
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261531_TestClass(BaseTestCase):

    def test_C8261531(self):
        """
        TESTCASE VARIABLES
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utillobj=core_utility.CoreUtillityMethods(self.driver)
         
        """
        CSS
        """
        designer_css=".ibx-tab-button:nth-child(3) .ibx-label-text"
        folder_name='P292_S19901'
        group_name='G513445'
        title_name='Portal for Context Menu Testing1'
        css=".pop-top [class*='ok-button']"

        """
            Step 1:Sign into WebFOCUS Home Page as Admin User
            Step 2:Click Content View from the sidebar > Click on Domains from the resource tree
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        time.sleep(5)
        main_page_obj.select_content_from_sidebar()  #Its written when poratl is selected its keep on loading on clicking content so the content is not selected since its written twice
        time.sleep(5)
        
        """
            Step 2:Click Content View from the sidebar > Click on Domains from the resource tree
        """
        util_obj.wait_for_page_loads(main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text('div.crumb-box', 'Workspaces', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Domains')
        
        """
            Step 3:If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder('{0}'.format(folder_name))
        main_page_obj.expand_repository_folder('{0}'.format(group_name))
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, "Portal for Context Menu Testing1", main_page_obj.home_page_medium_timesleep)
 
        """
            Step 4:Click on 'Portal for Context Menu Testing1' from the resource tree
            Step 5:Right click on 'Portal for Context Menu Testing1' from the content area > Click Delete > Click OK
            Verify 'Portal for Context Menu Testing1' portal deleted from the content area.
        """
        main_page_obj.right_click_folder_item_and_select_menu(title_name,'Delete', 'P292_S19901->G513445')
        util_obj.synchronize_with_number_of_element(css, 1, Global_variables.mediumwait)
        elem=util_obj.validate_and_get_webdriver_object(css, "OK Button in Delete item confirmation dialog")
        core_utillobj.left_click(elem)
        util_obj.synchronize_with_number_of_element(designer_css, 1, Global_variables.mediumwait)
        main_page_obj.verify_folders_in_grid_view(['Portal for Context Menu Testing1'], 'asnotin', "Step 5: Verify the deleted folder is not in the folder content area")
        
        """
            Step 6:In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()