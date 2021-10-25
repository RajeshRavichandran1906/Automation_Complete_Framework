'''
Created on Aug 16, 2019

@author: Vpriya

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2509407&group_by=cases:section_id&group_id=192834&group_order=asc
Test case Name =  Direct access to Portals node
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators
from common.pages.wf_mainpage import Wf_Mainpage as homepage

class C2509407_TestClass(BaseTestCase):

    def test_C2509407(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        home_page = homepage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
                
        """                                                 
        Step 1: Enter URL http://{machine_name}:{port}/{soft-context}/portals
        Verify you get the Sign in page.
        """
        """
        Step 2:Login as WF_Administrator.
        """
        login.invoke_homepage_with_portal('mridadm','mrpassadm')

        """
        Step 3:Verify,Only the portal contents (V3, V4 & V5) are listed.
        No sidebar is present.Click on the user Link.
        Verify only 'Help', 'Change Password' & 'Signout' options are available.
        """
        utils.synchronize_with_visble_text(locator_obj.content_area_css,'Retail Samples',home_page.chart_long_timesleep)
        utils.verify_object_visible('.main-panel .left-main-panel',False,"Step 03:verify No sidebar is present ")
        Wf_Mainpage.verify_username_dropdown_menu(self,['Help', 'Change Password', 'Sign Out'],msg="step 03:Verify only 'Help', 'Change Password' & 'Signout' options are available.")
        
        """
        Step 4:Right click on Retail Samples Collaborative portal
        Verify under context menu 'Open file location' option should be removed.
        """
        item_obj = home_page.get_domain_folder_item(item_name="Retail Samples",item_name_index=2)
        core_utils.right_click(item_obj)
        home_page.verify_context_menu_item(["Open item location"], msg ="Step 4:Verify under context menu 'Open file location' option should be removed.", comparision_type ='asnotin')
        
        """
        Step 5 : Click signout from the user link.
        """
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()