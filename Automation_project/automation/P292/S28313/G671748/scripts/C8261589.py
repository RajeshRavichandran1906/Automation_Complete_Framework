'''
Created on December 13, 2018

@author: Vpriya
Testcase Name : Verify Action Bar is organized by type
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261589
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C8261589_TestClass(BaseTestCase):
    
    def test_C8261589(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        
        """
        Test case variables
        """
        domains_repository = 'Domains'
        expected_tabs_list_common=['Folder', 'Upload Data', 'Connect', 'Workbook', 'Chart', 'Report', 'Page']
        expected_tabs_list_Data=['Upload Data', 'Connect', 'Metadata', 'Reporting Object']
        expected_tabs_list_Designer=['Workbook', 'Chart', 'Page', 'Portal']
        expected_tabs_list_IA=['Chart', 'Visualization', 'Report', 'Document', 'Sample Content', 'Alert']
        expected_tabs_list_Sch=['Access List', 'Distribution List', 'Schedule']
        expected_tabs_list_other=['Folder', 'Upload File', 'URL', 'Shortcut', 'Text Editor', 'Blog', 'Portal Page', 'Collaborative Portal']
        
        
        """
        Step 1: Sign into WebFOCUS as Administrator.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on the Content View from the sidebar 
        """
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        
        
        """
        Step 3: Click on Domains from the resource tree.
        """
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(domains_repository)
        
        """
        Step 4: Click on the 'Retail Samples' domain > 'Common' category button.
        Verify that Action bar associated with 'Domains' tools (Folder) is in yellow color, 
        the tools associated with 'Data' (Upload Data and Connect) are in green color, 
        then the tools associated with 'Content Designer' (Workbook and Chart) are in purple color, 
        the tools associated with 'IA' (Report) also in purple color and the tools associated with 'Designer' (Page only) is in purple color..
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        main_page_obj.select_action_bar_tab('Common')
        main_page_obj.verify_action_bar_tab_all_options(expected_tabs_list_common,"Step 4.1")
        main_page_obj.verify_action_bar_tab_option_color('Folder','Gorse', "Step 4.2")
        main_page_obj.verify_action_bar_tab_option_color('Upload Data','Pastel_Green', "Step 4.3")
        main_page_obj.verify_action_bar_tab_option_color('Connect','Pastel_Green', "Step 4.4")
        main_page_obj.verify_action_bar_tab_option_color('Workbook','blue_marguerite', "Step 4.5")
        main_page_obj.verify_action_bar_tab_option_color('Chart','blue_marguerite', "Step 4.6")
        main_page_obj.verify_action_bar_tab_option_color('Report','blue_marguerite', "Step 4.7")
        main_page_obj.verify_action_bar_tab_option_color('Page','blue_marguerite', "Step 4.8")
        
        
        """
        Step 5: Click on 'Data' category button.
        Verify that the tools associated with the 'Data' tools (Upload Data, Connect and Metadata) are in green color 
        and the tools associated with the IA tools (Reporting Object) is in purple color.
        """
        main_page_obj.select_action_bar_tab('Data')
        main_page_obj.verify_action_bar_tab_all_options(expected_tabs_list_Data,"Step 5")
        main_page_obj.verify_action_bar_tab_option_color('Upload Data','Pastel_Green', "Step 5.1")
        main_page_obj.verify_action_bar_tab_option_color('Connect','Pastel_Green', "Step 5.2")
        main_page_obj.verify_action_bar_tab_option_color('Metadata','Pastel_Green', "Step 5.3")
        main_page_obj.verify_action_bar_tab_option_color('Reporting Object','blue_marguerite', "Step 5.4")
        
        """
        Step 6:Click on 'Designer' category button.
        Verify that the tools associated with the content designer (Workbook, Chart, and Page) are in purple color 
        and the tools associated with 'BIP' (Portal) is in blue color.
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.verify_action_bar_tab_all_options(expected_tabs_list_Designer,"Step 6")
        main_page_obj.verify_action_bar_tab_option_color('Workbook','blue_marguerite', "Step 6.1")
        main_page_obj.verify_action_bar_tab_option_color('Chart','blue_marguerite', "Step 6.2")
        main_page_obj.verify_action_bar_tab_option_color('Page','blue_marguerite', "Step 6.3")
        main_page_obj.verify_action_bar_tab_option_color('Portal','iris_blue', "Step 6.4")
        
        """
        Step 7:Click on 'Info Assist' category button.
        Verify that the tools associated with 'IA' (Chart, Visualization, Report, Document, Sample Content, and Alert) are in purple color.
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        main_page_obj.verify_action_bar_tab_all_options(expected_tabs_list_IA,"Step 7")
        main_page_obj.verify_action_bar_tab_option_color('Chart','blue_marguerite', "Step 7.1")
        main_page_obj.verify_action_bar_tab_option_color('Visualization','blue_marguerite', "Step 7.2")
        main_page_obj.verify_action_bar_tab_option_color('Report','blue_marguerite', "Step 7.3")
        main_page_obj.verify_action_bar_tab_option_color('Document','blue_marguerite', "Step 7.4")
        main_page_obj.verify_action_bar_tab_option_color('Sample Content','blue_marguerite', "Step 7.5")
        main_page_obj.verify_action_bar_tab_option_color('Alert','blue_marguerite', "Step 7.6")
        
        """
        Step 8:Click on 'Schedule' category button..
        Verify that the tools associated with 'Report Caster' (Access List, Distribution List, and Schedule) are in red color.
        """
        main_page_obj.select_action_bar_tab('Schedule')
        main_page_obj.verify_action_bar_tab_all_options(expected_tabs_list_Sch,"Step 8")
        main_page_obj.verify_action_bar_tab_option_color('Access List','Cinnabar', "Step 8.1")
        main_page_obj.verify_action_bar_tab_option_color('Distribution List','Cinnabar', "Step 8.2")
        main_page_obj.verify_action_bar_tab_option_color('Schedule','Cinnabar', "Step 8.3")
        
        """
        Step 9:Click on the 'Other' category button.
        Verify that the tools associated with 'Domains' (Folder) in yellow color, 
        the tools associated with 'Other' (Upload File, URL, Shortcut, Text Editor) are in cyan color 
        and the tools associated with 'BIP' (Blogs, Portal Page and Collaborative Portal) are in blue color.
        """
        main_page_obj.select_action_bar_tab('Other')
        main_page_obj.verify_action_bar_tab_all_options(expected_tabs_list_other,"Step 9")
        main_page_obj.verify_action_bar_tab_option_color('Folder','Gorse', "Step 9.1")
        main_page_obj.verify_action_bar_tab_option_color('Upload File','Medium_Turquoise', "Step 9.2")
        main_page_obj.verify_action_bar_tab_option_color('URL','Medium_Turquoise', "Step 9.3")
        main_page_obj.verify_action_bar_tab_option_color('Shortcut','Medium_Turquoise', "Step 9.4")
        main_page_obj.verify_action_bar_tab_option_color('Text Editor','Medium_Turquoise', "Step 9.5")
        main_page_obj.verify_action_bar_tab_option_color('Blog','iris_blue', "Step 9.6")
        main_page_obj.verify_action_bar_tab_option_color('Portal Page','iris_blue', "Step 9.7")
        main_page_obj.verify_action_bar_tab_option_color('Collaborative Portal','iris_blue', "Step 9.8")
        
        
        """
        Step 10: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()