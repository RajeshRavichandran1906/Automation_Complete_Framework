'''
Created on Aug 13, 2019

@author: Vpriya

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6668383&group_by=cases:section_id&group_id=192834&group_order=asc
Test case Name =  Replace IBI Action-O logo with the new square logo
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.locators import wf_mainpage_locators

class C6668383_TestClass(BaseTestCase):

    def test_C6668383(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
            COMMON TEST CASE VARIABLES 
        """
        
                                                           
        '''
        Step 1 : Sign in to WebFOCUS as Developer user..
        Verify the Information Builders Logo,
        '''
        login.invoke_home_page('mrid', 'mrpass')
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        utils.verify_picture_using_sikuli('C6668383_step_1',"step 01:Verify the Information Builders Logo")
        
        '''
        Step 2 : Click on the "Collapse side bar" button in the banner area
        Verify the IBI Action-O logo is replaced with the new square logo,.
        '''
        main_page.collapse_side_bar()
        utils.verify_picture_using_sikuli('C6668383_step_2',"step 02:Verify the IBI Action-O logo is replaced with the new square logo,.")
        main_page.expand_side_bar()
        
        '''
        Step 3 : In the banner link, click on the top right username > Click Sign Out.
        '''
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()