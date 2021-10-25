'''
Created on Jun 26, 2019

@author: Magesh

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6459303
TestCase Name = Verify lists of Action bars
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.wftools import page_designer
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C6459303_TestClass(BaseTestCase):

    def test_C6459303(self):
        
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
        
        """ 
        Step 1: Login WF as domain developer
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_visble_text(content_css, "Content", 60)
        
        """
        Step 2: Click on Content tree from side bar
        """
        wfmain_obj.select_content_from_sidebar()
        
        """
        Step 3: Expand 'P292_S11397' domain -> 'G490183' folder;
        Double click on 'Explorer Widget page'
        """
        wfmain_obj.expand_repository_folder("P292_S11397->G490183")
        page_designer_obj.run_page_designer_by_double_click("Explorer Widget page")
        time.sleep(15)
        wfmain_obj_run.switch_to_frame()
        page_designer_obj.switch_to_container_frame("Panel 1")
        
        """
        Step 3.1: Verify Home Page is displayed inside the panel as below;
        """
        wfmain_obj.verify_action_bar_tab_specific_options(["Folder","Upload Data","Connect","Workbook","Chart","Report","Page"], "Step 03.1: Verify action tiles under common category are arranged as below")
        
        """
        Step 4: Click on Data tag
        """
        wfmain_obj.select_action_bar_tab('Data')
        
        """
        Step 04.1: Verify the below list of action bars appears in the exact order
        """
        wfmain_obj.verify_action_bar_tab_specific_options(["Upload Data","Connect","Metadata","Reporting Object"], "Step 04.1 Verify the below list of action bars appears in the exact order")
        
        """
        Step 05: Click on 'Designer' category buttons
        """
        wfmain_obj.select_action_bar_tab('Designer')
        
        """
        Step 05.1: Verify the below list of action bars appears in the exact order
        """
        wfmain_obj.verify_action_bar_tab_specific_options(["Workbook","Chart","Page","Portal"], "Step 05.1: Verify the below list of action bars appears in the exact order")
        
        """
        Step 06: Click on 'InfoAssist' category buttons
        """
        wfmain_obj.select_action_bar_tab('InfoAssist')
        
        """
        Step 06.1: Verify the below list of action bars appears in the exact order
        """
        wfmain_obj.verify_action_bar_tab_specific_options(["Chart","Visualization","Report","Document","Sample Content","Alert"], "Step: 06.1 Verify the below list of action bars appears in the exact order")
        
        """
        Step 07: Click on 'Schedule' category buttons
        """
        wfmain_obj.select_action_bar_tab('Schedule')
        
        """
        Step 07.1: Verify the below list of action bars appears in the exact order
        """
        wfmain_obj.verify_action_bar_tab_specific_options(['Access List', 'Distribution List', 'Schedule'], "Step 07.1: Verify the below list of action bars appears in the exact order")
        
        """
        Step 08: Click on 'Other' category buttons
        """
        wfmain_obj.select_action_bar_tab('Other')
        
        """
        Step 08.1: Verify the below list of action bars appears in the exact order
        """
        wfmain_obj.verify_action_bar_tab_specific_options(['Folder', 'Upload File', 'URL', 'Shortcut', 'Text Editor', 'Blog', 'Portal Page', 'Collaborative Portal'], "Step 08.1: Verify the below list of action bars appears in the exact order")
        page_designer_obj.switch_to_default_page()
        
        """
        Step 09: Close page
        """
        wfmain_obj_run.close()

        """
        Step 10: Sign Out WF
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()