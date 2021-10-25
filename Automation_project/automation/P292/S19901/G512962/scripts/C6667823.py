'''
Created on DECEMBER 10, 2018

@author: KK14897
Testcase Name : Verify the Category Buttons and Action Tiles for Dev User
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6667823
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables

class C6667823_TestClass(BaseTestCase):
    
    def test_C6667823(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        content_css='div[class="ibx-label-glyph ibx-label-icon fa fa-bar-chart"]'
        crumb_css='div[class*="crumb-box ibx-widget ibx-flexbox"]'
        folder_name_path="Domains->Retail Samples"
        """
        Step 01: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(content_css, '1', Global_variables.longwait)
        
        """
        Step 02: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        """
        Step 03: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder(folder_name_path) 
        util_obj.synchronize_with_number_of_element(crumb_css, '1', Global_variables.longwait)
        main_page_obj.verify_action_bar_tab_buttons(['Common', 'Data', 'Designer', 'InfoAssist', 'Schedule', 'Other'], 'Step 03 : Verify action bar tab buttons')
        main_page_obj.verify_ribbon_button(["Folder","Upload Data","Connect","Workbook","Chart","Report","Page"],msg="Step 04 click data category button")
        """
        Step 04: Click on 'Data' category buttons
        """
        main_page_obj.select_action_bar_button("Data")
        main_page_obj.verify_ribbon_button(["Upload Data","Connect","Metadata","Reporting Object"],msg="Step 04 click data category button")
        
        """
        Step 05: Click on 'Designer' category buttons
        """
        main_page_obj.select_action_bar_button("Designer")
        main_page_obj.verify_ribbon_button(["Workbook","Chart","Page","Portal"],msg="Step 05: Click on 'Designer' category buttons")
        
        """
        Step 06: Click on 'InfoAssist' category buttons
        """
        main_page_obj.select_action_bar_button("InfoAssist")
        main_page_obj.verify_ribbon_button(["Chart","Visualization","Report","Document","Sample Content","Alert"],msg="Step: 07 Click on 'Schedule' category buttons")
        
        """
        Step 07: Click on 'Schedule' category buttons
        """
        main_page_obj.select_action_bar_button("Schedule")
        main_page_obj.verify_ribbon_button(['Access List', 'Distribution List', 'Schedule'],msg="Step 06: Click on 'Designer' category buttons")
        
        """
        Step 08: Click on 'Other' category buttons
        """
        main_page_obj.select_action_bar_button("Other")
        main_page_obj.verify_ribbon_button(['Folder', 'Upload File', 'URL', 'Shortcut', 'Text Editor', 'Blog', 'Portal Page', 'Collaborative Portal'],msg="Step 08: Click on 'Other' category buttons")
        
        """
        Step 09: Double Click on My Content folder in content area > select Designer category buttons
        """
        main_page_obj.double_click_folder_item_and_select_menu("My Content")
        main_page_obj.select_action_bar_button("Designer")
        main_page_obj.verify_ribbon_button(["Workbook","Chart","Page"],msg="Step 05: Click on 'Designer' category buttons")
        """
        Step 10: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        