'''
Created on May 8, 2019

@author: varun
Testcase Name : Verify Action Bar is organized by type
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9318101
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C9318101_TestClass(BaseTestCase):
    
    def test_C9318101(self):
        
        """
        Test case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        domains_css = ".toolbar"
        workspace = "Workspaces"
        
        """
        Step 1: Sign into WebFOCUS as Administrator.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on the Content View from the sidebar.
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Click on Domains from the resource tree.
        """
        util_obj.synchronize_with_visble_text(domains_css, workspace, main_page_obj.home_page_short_timesleep)
        main_page_obj.expand_repository_folder(workspace)
        
        """
        Step 4: Click on the 'Retail Samples' domain > 'Common' category button
        Verify that Action bar associated with workspace tools (Folder) is in yellow color, 
        the tools associated with 'Data' (Upload Data and Connect) are in green color, 
        then the tools associated with 'Content Designer' (Workbook and Chart) are in purple color, 
        the tools associated with 'IA' (Report) also in purple color and the tools associated 
        with 'Designer' (Page only) is in purple color.
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Common', main_page_obj.home_page_long_timesleep)
        main_page_obj.select_action_bar_tab('Common')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Folder', main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_action_bar_tab_option_color('Folder', 'Gorse', 'Step 4.1: Verify the folder color')
        main_page_obj.verify_action_bar_tab_option_color('Upload Data', 'Pastel_Green', 'Step 4.2: Verify upload data color')
        main_page_obj.verify_action_bar_tab_option_color('Connect', 'Pastel_Green', 'Step 4.3: Verify the connect color')
        main_page_obj.verify_action_bar_tab_option_color('Workbook', 'blue_marguerite', 'Step 4.4: Verify the workbook color')
        main_page_obj.verify_action_bar_tab_option_color('Chart', 'blue_marguerite', 'Step 4.5: Verify the chart color')
        main_page_obj.verify_action_bar_tab_option_color('Report', 'blue_marguerite', 'Step 4.6: Verify the report color')
        main_page_obj.verify_action_bar_tab_option_color('Page', 'blue_marguerite', 'Step 4.7: Verify the page color')
        
        """
        Step 5: Click on 'Data' category button.
        Verify that the tools associated with the 'Data' tools (Upload Data, Connect and Metadata) are in green color 
        and the tools associated with the IA tools (Reporting Object) is in purple color.
        """
        main_page_obj.select_action_bar_tab('Data')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Upload Data', main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_action_bar_tab_option_color('Upload Data', 'Pastel_Green', 'Step 5.1: Verify the upload data color')
        main_page_obj.verify_action_bar_tab_option_color('Connect', 'Pastel_Green', 'Step 5.2: Verify the connect color')
        main_page_obj.verify_action_bar_tab_option_color('Metadata', 'Pastel_Green', 'Step 5.3: Verify the metadata color')
        main_page_obj.verify_action_bar_tab_option_color('Reporting Object', 'blue_marguerite', 'Step 5.4: Verify the RO color')
        
        """
        Step 6: Click on 'Designer' category button.        
        Verify that the tools associated with the content designer (Workbook, Chart,Report and Page) are in purple color 
        and the tools associated with 'BIP' (Portal) is in blue color.
        """
        main_page_obj.select_action_bar_tab('Designer')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Workbook', main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_action_bar_tab_option_color('Workbook', 'blue_marguerite', 'Step 6.1: Verify the workbook color')
        main_page_obj.verify_action_bar_tab_option_color('Chart', 'blue_marguerite', 'Step 6.2: Verify the Chart color')
        main_page_obj.verify_action_bar_tab_option_color('Report', 'blue_marguerite', 'Step 6.3: Verify the Report color')
        main_page_obj.verify_action_bar_tab_option_color('Page', 'blue_marguerite', 'Step 6.4: Verify the Page color')
        main_page_obj.verify_action_bar_tab_option_color('Portal', 'iris_blue', 'Step 6.5: Verify the portal color')
        
        """
        Step 7: Click on 'Info Assist' category button.
        Verify that the tools associated with 'IA' (Chart, Visualization, Report, Document, Sample Content, and Alert) are in purple color.
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Chart', main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_action_bar_tab_option_color('Chart', 'blue_marguerite', 'Step 7.1: Verify the chart color')
        main_page_obj.verify_action_bar_tab_option_color('Visualization', 'blue_marguerite', 'Step 7.2: Verify the visualization color')
        main_page_obj.verify_action_bar_tab_option_color('Report', 'blue_marguerite', 'Step 7.3: Verify the report color')
        main_page_obj.verify_action_bar_tab_option_color('Document', 'blue_marguerite', 'Step 7.4: Verify the document color')
        main_page_obj.verify_action_bar_tab_option_color('Sample Content', 'blue_marguerite', 'Step 7.5: Verify the sample content color')
        main_page_obj.verify_action_bar_tab_option_color('Alert', 'blue_marguerite', 'Step 7.6: Verify the Alert color')
        
        """
        Step 8: Click on 'Schedule' category button.
        Verify that the tools associated with 'Report Caster' (Access List, Distribution List, and Schedule) are in red color.
        """
        main_page_obj.select_action_bar_tab('Schedule')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Access List', main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_action_bar_tab_option_color('Access List', 'Cinnabar', 'Step 8.1: Verify the access list color')
        main_page_obj.verify_action_bar_tab_option_color('Distribution List', 'Cinnabar', 'Step 8.2: Verify the distribution list color')
        main_page_obj.verify_action_bar_tab_option_color('Schedule', 'Cinnabar', 'Step 8.3: Verify the schedule color')
        
        """
        Step 9: Click on the 'Other' category button.
        Verify that the tools associated with workspace (Folder) in yellow color, the tools associated with 'Other' 
        (Upload File, URL, Shortcut, Text Editor) are in cyan color and the tools associated with 'BIP' (Blogs, Portal Page 
        and Collaborative Portal) are in blue color.
        """
        main_page_obj.select_action_bar_tab('Other')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Folder', main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_action_bar_tab_option_color('Folder', 'Gorse', 'Step 9.1: Verify the folder color')
        main_page_obj.verify_action_bar_tab_option_color('Upload File', 'Medium_Turquoise', 'Step 9.2: Verify the upload file color')
        main_page_obj.verify_action_bar_tab_option_color('URL', 'Medium_Turquoise', 'Step 9.3: Verify the URL color')
        main_page_obj.verify_action_bar_tab_option_color('Shortcut', 'Medium_Turquoise', 'Step 9.4: Verify the shortcut color')
        main_page_obj.verify_action_bar_tab_option_color('Text Editor', 'Medium_Turquoise', 'Step 9.5: Verify the text editor color')
        main_page_obj.verify_action_bar_tab_option_color('Upload File', 'Medium_Turquoise', 'Step 9.6: Verify the upload file color')
        main_page_obj.verify_action_bar_tab_option_color('Blog', 'iris_blue', 'Step 9.7: Verify the upload file color')
        main_page_obj.verify_action_bar_tab_option_color('Portal Page', 'iris_blue', 'Step 9.8: Verify the portal page color')
        main_page_obj.verify_action_bar_tab_option_color('Collaborative Portal', 'iris_blue', 'Step 9.9: Verify the collab portal color')
        
        """
        Step 10: From the banner link, click on the top right username > Click Signout.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()