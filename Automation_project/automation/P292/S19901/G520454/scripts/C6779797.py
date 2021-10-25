'''
Created on November 14, 2018

@author: Nasir
Testcase Name : Check Share Tooltip after sharing personal pages
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779797
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.lib import utillity,core_utility

class C6779797_TestClass(BaseTestCase):
    
    def test_C6779797(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj=designer_portal.Canvas(self.driver)
        
        """    1. Sign in to WebFOCUS as Developer user    """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """    2. Expand the domain from the tree and click on 'P292_S19901_G520454'    """
        """    3. Right click on 'V5 Portal Share' from the content area > Run    """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share', context_menu_item_path='Run', folder_path='Domains->P292_S19901_G520454')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(".pd-container-title", 'Panel 1', main_page_obj.home_page_medium_timesleep)
        
         
        """    4. Hover the mouse to the Share button in the personal page toolbar.    """
        """    Verify the tooltip shows 'Stop Sharing'    """
        portal_obj.verify_page_header_button_tooltip('Stop sharing', "Step 04a: Verify the tooltip shows 'Stop Sharing'")
        
        """    5. Close the portal run window.    """
        core_util_obj.switch_to_previous_window()
        
        """    6. In the banner link, click on the top right username > Click Sign Out.    """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
        
if __name__ == '__main__':
    unittest.main()
    
        