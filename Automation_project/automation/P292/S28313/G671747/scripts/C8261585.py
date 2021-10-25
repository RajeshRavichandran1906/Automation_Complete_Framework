'''
Created on DECEMBER 10, 2018

@author: KK14897
Testcase Name : Verify the Category Buttons and Action Tiles for Dev User
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261585
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables

class C8261585_TestClass(BaseTestCase):
    
    def test_C8261585(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        crumb_css='div[class*="crumb-box ibx-widget ibx-flexbox"]'
        folder_name_path="Domains->Retail Samples"
        
        """
        Step 01: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 02: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        """
        Step 03: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder(folder_name_path) 
        util_obj.synchronize_with_number_of_element(crumb_css, '1', Global_variables.longwait)
        main_page_obj.verify_action_bar_all_tabs(['Common', 'Data', 'Designer', 'InfoAssist', 'Schedule', 'Other'], 'Step 03a : Verify action bar tab buttons')
        main_page_obj.verify_action_bar_tab_specific_options(["Folder","Upload Data","Connect","Workbook","Chart","Report","Page"], "Step 03b click data category button")
        
        """
        Step 04: Click on 'Data' category buttons
        """
        main_page_obj.select_action_bar_tab('Data')
        main_page_obj.verify_action_bar_tab_specific_options(["Upload Data","Connect","Metadata","Reporting Object"], "Step 04 click data category button")
        
        """
        Step 05: Click on 'Designer' category buttons
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.verify_action_bar_tab_specific_options(["Workbook","Chart","Page","Portal"], "Step 05: Click on 'Designer' category buttons")
        
        """
        Step 06: Click on 'InfoAssist' category buttons
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        main_page_obj.verify_action_bar_tab_specific_options(["Chart","Visualization","Report","Document","Sample Content","Alert"], "Step: 06 Click on 'Schedule' category buttons")
        
        """
        Step 07: Click on 'Schedule' category buttons
        """
        main_page_obj.select_action_bar_tab('Schedule')
        main_page_obj.verify_action_bar_tab_specific_options(['Access List', 'Distribution List', 'Schedule'], "Step 07: Click on 'Schedule' category buttons")
        
        """
        Step 08: Click on 'Other' category buttons
        """
        main_page_obj.select_action_bar_tab('Other')
        main_page_obj.verify_action_bar_tab_specific_options(['Folder', 'Upload File', 'URL', 'Shortcut', 'Text Editor', 'Blog', 'Portal Page', 'Collaborative Portal'], "Step 08: Click on 'Other' category buttons")
        
        """
        Step 09: Double Click on My Content folder in content area > select Designer category buttons
        """
        main_page_obj.double_click_folder_item_and_select_menu("My Content")
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.verify_action_bar_tab_specific_options(["Workbook","Chart","Page"], "Step 09: Click on 'Designer' category buttons")
        
        """
        Step 10: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        