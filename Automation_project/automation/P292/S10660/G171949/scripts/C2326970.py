'''
Created on Sep 3, 2019

@author: Niranjan
Test rail link : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2326970
Testcase title : Content Menu:Verify MyContent folder and Hidden folder.
'''
import unittest
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login

class C2326970_TestClass(BaseTestCase):
   
    def test_C2326970(self):
       
        """ CLASS  OBJECTS """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
       
        step1 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        loginpage.invoke_home_page('mradmid', 'mradmpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.main-panel .toolbar', 'Domains', homepage.home_page_long_timesleep)
        utils.capture_screenshot('01.01', step1)
        
        step2 = """
            STEP 02 : Under Domain tree >> Select domain P292_S10660.
            
            Verify 'My Content' and 'Hidden Content' folders are available for P292_S10660.

        'My Content' folder is Published.
        'Hidden Content' folder is Hidden.
        """
        homepage.expand_repository_folder('Domains->P292_S10660')
        utils.synchronize_with_visble_text('.sd-content-title-label-folders', 'Folders', homepage.home_page_short_timesleep)
        utils.capture_screenshot('02.01', step2)
        
        homepage.verify_repository_folder_publish_or_unpublish('My Content', 'publish', 'Step 02.00 : Verify My Content folder is Published')
        utils.capture_screenshot('02.00', step2, expected_image_verify=True)
        homepage.verify_hidden_repository_folder('Hidden Content', 'Step 02.01 : Verify Hidden Content folder is Hidden')
        utils.capture_screenshot('02.01', step2, expected_image_verify=True)
        
        """
            STEP 03 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()