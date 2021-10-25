'''
Created on June 24,2019

@author: Vpriya

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/11397&group_by=cases:section_id&group_id=490184&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6459326
TestCase Name = Verify that Collapsed Resource Tree is remembered
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.wftools import page_designer
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C6459326_TestClass(BaseTestCase):

    def test_C6459326(self):
        
        """
        TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        content_css=wf_mainpage_locators.WfMainPageLocators.CONTENT_CSS
        page_designer_obj=page_designer.Design(self.driver)
        wfmain_obj_run=wf_mainpage.Run(self.driver)
        
        """ Step 1: Login WF as domain developer
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_visble_text(content_css, "Content", 60)
        
        """Step 2: Click on Content tree from side bar
        """
        wfmain_obj.select_content_from_sidebar()
        
        """
        Step 3:Expand 'P292_S11397' domain -> 'G490184' folder;
        Double click on 'Explorer Widget page'
        """
        wfmain_obj.expand_repository_folder("P292_S11397->G490183")
        page_designer_obj.run_page_designer_by_double_click("Explorer Widget page")
        wfmain_obj_run.switch_to_frame()
        page_designer_obj.switch_to_container_frame("Panel 1")
        
        
        
        """ Step 4: Click on Collapse resources tree icon.
                    Verify Tree is collapsed as below.
        """
        wfmain_obj.collapse_resource_tree()
        wfmain_obj.verify_expand_resource_tree(True, 'Step 2: Verify that the Resource Tree is collapsed.')
        page_designer_obj.switch_to_default_page()
        
        """
        Step 5:Close the 'Explorer widget page' run window.
        """
        wfmain_obj_run.close()
        
        """
        Step 6:Refresh browser.
        """
        self.driver.refresh()
        
        """
        Verify Tree is collapsed in home page too
        """
        
        utillobj.synchronize_until_element_is_visible(".right-main-panel .explore-box .tree-showcollapse-button .ibx-label-icon",wfmain_obj.chart_long_timesleep)
        wfmain_obj.verify_expand_resource_tree(True, 'Step 6: Verify that the Resource Tree is collapsed.')
        
        """
        Step 7:Double click on 'Explorer Widget page'
        Verify still the Tree is collapsed.
        """
        wfmain_obj.double_click_on_content_area_items("Explorer Widget page")
        wfmain_obj_run.switch_to_frame()
        page_designer_obj.switch_to_container_frame("Panel 1")
        
        """
        Step 8:Click the Expand Resource Tree icon.
        Verify that the Tree is expanded.
        """
        
        wfmain_obj.expand_resource_tree()
        wfmain_obj.verify_collapse_resource_tree(True, 'Step 8: Verify that the Resource Tree is collapsed.')
        page_designer_obj.switch_to_default_page()
        
        """
        Step 9:Close the 'Explorer widget page' run window..
        """
        wfmain_obj_run.close()

 
        """
        Step 10:Refresh the browser.
        Verify the Tree is expanded in home page
        """
        
        self.driver.refresh()
        utillobj.synchronize_until_element_is_visible(".right-main-panel .explore-box .tree-collapse-button .ibx-label-icon",wfmain_obj.chart_long_timesleep)
        wfmain_obj.verify_collapse_resource_tree(True, 'Step 10: Verify that the Resource Tree is collapsed.')
        
        """
        Step 11:In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        