'''
Created on June 26,2019

@author: Vpriya

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/11397&group_by=cases:section_id&group_id=490184&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6459329
TestCase Name = Verify that chosen and expanded is remembered
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.wftools import page_designer
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C6459329_TestClass(BaseTestCase):

    def test_C6459329(self):
        
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
        crumb_css="[class^='main-box'] [class^='main-panel'] [class^='right-main-panel'] [class^='crumb-box'] [class^='sd-right-carat']"
        
        """ Step 1: Login WF as domain developer
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_visble_text(content_css, "Content", 60)
        
        """Step 2: Click on Content view from side bar
        """
        wfmain_obj.select_content_from_sidebar()
        
        """
        Step 3:Expand 'P292_S11397' domain -> 'G490183' folder;
        Double click on 'Explorer Widget page''
        """
        wfmain_obj.expand_repository_folder("P292_S11397->G490183")
        page_designer_obj.run_page_designer_by_double_click("Explorer Widget page")
        wfmain_obj_run.switch_to_frame()
        page_designer_obj.switch_to_container_frame("Panel 1")

        
        """ Step 4: Double click on 'Retail Samples' domain -> 'Charts' folder
        Verify 'Retail Samples' domain is expanded and 'Chart' folder is highlighted.
        """
        wfmain_obj.expand_repository_folder("Retail Samples->Charts")
        time.sleep(5)
        wfmain_obj.verify_crumb_box("Workspaces->Retail Samples->Charts","Step 4.1")
        wfmain_obj.verify_selected_resource_tree_item(["Charts"],"4.2")
        page_designer_obj.switch_to_default_page()
        
        """
        Step 5:Close the 'Explorer widget' page run window.
        Verify still 'P292_S11397' domain -> 'G490183' folder is selected and expanded.
        """
        wfmain_obj_run.close()
        wfmain_obj_run.switch_to_default_content()
        time.sleep(2)
        utillobj.synchronize_until_element_is_visible(crumb_css,wfmain_obj.home_page_long_timesleep)
        wfmain_obj.verify_crumb_box("Workspaces->P292_S11397->G490183","Step 5.1")
        
        """
        Step 6:Refresh the browser.
        Verify 'Retail Samples' domain is expanded and 'Charts' folder is highlighted.
        """
        self.driver.refresh()
        utillobj.synchronize_until_element_is_visible(crumb_css,wfmain_obj.home_page_long_timesleep)
        wfmain_obj.verify_crumb_box("Workspaces->Retail Samples->Charts","Step 4.1")
        wfmain_obj.verify_selected_resource_tree_item(["Charts"],"4.2")
        
        """
        Step 7:Click on 'G490183' folder;
        Double click on 'Explorer Widget page'
        Verify 'P292_S11397' domain -> 'G490183' folder is selected and expanded.
        """
        wfmain_obj.expand_repository_folder("P292_S11397->G490183")
        page_designer_obj.run_page_designer_by_double_click("Explorer Widget page")
        wfmain_obj_run.switch_to_frame()
        page_designer_obj.switch_to_container_frame("Panel 1")
        utillobj.synchronize_until_element_is_visible(crumb_css,wfmain_obj.home_page_long_timesleep)
        wfmain_obj.verify_crumb_box("Workspaces->P292_S11397->G490183","Step 7.1")
        
        """
        Step 8:Close the 'Explorer widget page' run window.
        Verify still 'P292_S11397' domain -> 'G490183' folder is selected and expanded.
        """
        page_designer_obj.switch_to_default_page()
        wfmain_obj_run.close()
        wfmain_obj_run.switch_to_default_content()
        utillobj.synchronize_until_element_is_visible(crumb_css,wfmain_obj.home_page_long_timesleep)
        wfmain_obj.verify_crumb_box("Workspaces->P292_S11397->G490183","Step 8.1")
        
        """
        Step 9:Refresh the browser.
        Verify 'P292_S11397' domain -> 'G490183' folder is selected and expanded.
        """
        self.driver.refresh()
        utillobj.synchronize_until_element_is_visible(crumb_css,wfmain_obj.home_page_long_timesleep)
        wfmain_obj.verify_crumb_box("Workspaces->P292_S11397->G490183","Step 9.1")

        """
        Step 10:In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        