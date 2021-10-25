'''
Created on 14-Feb-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324331
TestCase Name = Portal Designer_Selecting Pages : Select_Copied_Pages
'''
import unittest, time
from common.lib import utillity, core_utility
from common.pages import visualization_resultarea, vfour_portal_canvas, wf_legacymainpage, vfour_portal_run, vfour_portal_ribbon, vfour_miscelaneous
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage

class C2324331_TestClass(BaseTestCase):

    def test_C2324331(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        wf_mainpage_obj = wf_mainpage.Wf_Mainpage(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        root_path = project_id+'->'+suite_id
        BIP_Portal_Path = root_path+'->BIP_V4_Portal'
        portal_name = 'Select_Copied_Page'
        welcome_page_parent_css = "#PortalResourcevBOX table tr td"
        edit_page_parent_css = "#applicationButtonBox img[src*='bip_button']"
        run_page_parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        
        def verify_panel_data(panel_name, expected_panel_text, step_num):
            panel_text = portal_canvas.get_panel_obj(panel_name)
            actual_panel_text = [elem.strip() for elem in panel_text.text.strip().split('\n') if elem != '']
            utillobj.asin(expected_panel_text, actual_panel_text, "Step " + str(step_num) + ": Verify 'Resource Tree' added in '" + str(panel_name) + "'.")
            
        def verify_column_data(column_no, expected_column_text, step_num):
            column_text = portal_canvas.get_column_obj(column_no)
            actual_column_text_list = [elem.strip() for elem in column_text.text.strip().split('\n') if elem != '']
            utillobj.asin(expected_column_text, actual_column_text_list, "Step " + str(step_num) + ": Verify 'column " + str(column_no) + "' panel.")
        
        def verify_panel_frame_data(chart_type, panel_name, expected_value, step_num, custom_css="svg g>text[class^='riser!s']"):
            portal_misobj.switch_to_frame_in_bip_page(frame_panel_name=panel_name)
            if chart_type == 'legend':
                resultobj.verify_riser_legends("jschart_HOLD_0", expected_value, "Step "+str(step_num)+": Verify legend Title in '" + str(panel_name) + "'.")
            elif chart_type == 'text':
                actual_text = self.driver.find_element_by_css_selector(custom_css).text.strip()
                utillobj.asequal(actual_text, expected_value, "Step "+str(step_num)+": Verify table data displayed in '" + str(panel_name) + "'.")
            utillobj.switch_to_default_content(pause=3)
        
        
        """ Step 1: Sign into WebFOCUS home page as Developer User
                    Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        time.sleep(1)
         
        """ Step 2: Expand P292 project, right Click on the S10117 folder from domains tree and choose New -> Collaborative Portal
        """
        """ Step 3: Enter 'Select_Copied_Page'
        """
        wf_mainpageobj.create_portal(BIP_Portal_Path, portal_name)
        core_utilobj.switch_to_new_window()
        utillobj.synchronize_with_number_of_element(edit_page_parent_css, 1, 90)
        portal_misobj.verify_page_template("Step 3: Verify when Portal Designer loads you are on the Layout tab", page_template="1 Column")
         
        """ Step 4: Click on the Copy Existing Page Icon from the page canvas
                    Verify that an explorer window shows up
        """
        """ Step 5: Open 'Pages_Folder'
        """
        """ Step 6: Choose both pages then click the Open button
                    Verify that you cant multi select the pages.
        """
        folder_path=BIP_Portal_Path+"->Pages_Folder"
        file_name_list=['Page_designer1', 'Page_designer_fluid']
        verify_repository_file_selected=['Page_designer_fluid']
        portal_canvas.add_page_with_existing_link('page','Copy Existing Page...', folder_path, file_name_list, 
                                                  verify_repository_file_selected=verify_repository_file_selected, msg="Step 6", close_add_page_dialog='Cancel')
         
        """ Step 7: Add the first page
                    Verify it shows on the portal
        """
        folder_path=BIP_Portal_Path+"->Pages_Folder"
        file_name_list=['Page_designer1']
        portal_canvas.add_page_with_existing_link('navigation_bar','Copy Existing Page...', folder_path, file_name_list)
         
        portal_canvas.verify_page_in_navigation_bar('Page_designer1', "Step 7: Verify 'Page_designer1' in Navigation bar.", page_order_list=['Page_designer1'])
         
        portal_canvas.select_page_in_navigation_bar('Page_designer1')
        verify_panel_data('Panel 2', suite_id, '7.1')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_1', expected_legend, '7.2')
          
        """ Step 8: Try to add the same page again
                    Click Ok button
                    Verify you get a message stating that the "page already in portal"
        """
        folder_path=BIP_Portal_Path+"->Pages_Folder"
        file_name_list=['Page_designer1']
        portal_canvas.add_page_with_existing_link('navigation_bar','Copy Existing Page...', folder_path, file_name_list)
        time.sleep(1)
        utillobj.verify_js_alert('Page already in portal.', "Step 8: Verify that you get an error message stating that the page is already in the portal")
        time.sleep(2)
        portal_canvas.close_add_page_dialog("div[id='dlgTitleExplorer'] [class*='window'][class*='active']", 'Cancel')
         
        """ Step 9: Add the other page
        """
        folder_path=BIP_Portal_Path+"->Pages_Folder"
        file_name_list=['Page_designer_fluid']
        portal_canvas.add_page_with_existing_link('navigation_bar','Copy Existing Page...', folder_path, file_name_list)
         
        portal_canvas.verify_page_in_navigation_bar('Page_designer_fluid', "Step 9: Verify 'Page_designer1' in Navigation bar.", page_order_list=['Page_designer1', 'Page_designer_fluid'])
         
        portal_canvas.select_page_in_navigation_bar('Page_designer_fluid')
        verify_panel_data('Panel 1', 'Retail Samples', '9.1')
        verify_panel_data('Panel 2', 'Area 1', '9.2')
        portal_canvas.verify_panel_image('honda_integra', 'honda_integra', 'Step 9.3: Verify Honda car displayed.')
        verify_panel_data('Panel 4', suite_id, '9.4')
         
        """ Step 10: Click the new page icon and add another 1 column page with a tree block
        """
        portal_canvas.add_page('1 Column', Page_title='Copy_Page1')
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_ResourceTree')
        time.sleep(2)
        verify_panel_data('Panel 1', project_id, '11')
         
        """ Step 11: Exit and save
        """
        portal_ribbon.bip_save_and_exit('Yes')
        core_utilobj.switch_to_previous_window(window_close=False)
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        time.sleep(1)
        
        """ Step 12: Run the portal
                     Verify that the pages were added in the right order and no issues.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 50)
        portal_canvas.verify_page_in_navigation_bar('Page_designer1', "Step 11: Verify 'Page_designer1' in Navigation bar.", page_order_list=['Page_designer1', 'Page_designer_fluid', 'Copy_Page1'])
        
        portal_canvas.select_page_in_navigation_bar('Page_designer1')
        verify_panel_data('Panel 2', suite_id, '11.1')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_1', expected_legend, '11.2')
        
        portal_canvas.select_page_in_navigation_bar('Page_designer_fluid')
        verify_panel_data('Panel 1', 'Retail Samples', '11.3')
        verify_panel_data('Panel 2', 'Area 1', '11.4')
        portal_canvas.verify_panel_image('honda_integra', 'honda_integra', 'Step 11.5: Verify Honda car displayed.')
        verify_panel_data('Panel 4', suite_id, '11.6')
        
        portal_canvas.select_page_in_navigation_bar('Copy_Page1')
        verify_panel_data('Panel 1', project_id, '11.7')
        
        """ Step 13: Click the new page icon and select Copy existing Page option for a page from any resource folder
                     Verify the page was added
        """
        folder_path=BIP_Portal_Path+"->lock column portal Resources"
        file_name_list=['Two_Col_placeholder_easy']
        portal_canvas.add_page_with_existing_link('navigation_bar','Copy Existing Page...', folder_path, file_name_list)
        
        utillobj.synchronize_with_number_of_element("div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton']", 4, 15)
        time.sleep(1)
        expected_list = ['Page_designer1', 'Page_designer_fluid', 'Copy_Page1', 'Two_Col_placeholder_easy']
        portal_canvas.verify_page_in_navigation_bar('Page_designer1', "Step 13: Verify 'Page_designer1' in Navigation bar.", page_order_list=expected_list)
        
        portal_canvas.select_page_in_navigation_bar('Two_Col_placeholder_easy')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_1', expected_legend, '13.1')
        expected_legend= ['EMEA', 'North America', 'Oceania', 'South America']
        verify_panel_frame_data('legend', 'Panel_2', expected_legend, '13.2')
        
        """ Step 14: Click the new page icon and add another page from the same folder
                     Verify that you don't get any messages stating the page already exists.
        """
        folder_path=BIP_Portal_Path+"->lock column portal Resources"
        file_name_list=['two_column_page']
        portal_canvas.add_page_with_existing_link('navigation_bar','Copy Existing Page...', folder_path, file_name_list)
        
        utillobj.synchronize_with_number_of_element("div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton']", 5, 15)
        time.sleep(1)
        expected_list = ['Page_designer1', 'Page_designer_fluid', 'Copy_Page1', 'Two_Col_placeholder_easy', 'two_column_page']
        portal_canvas.verify_page_in_navigation_bar('two_column_page', "Step 14.1: Verify 'two_column_page' in Navigation bar.", page_order_list=expected_list)
        
        portal_canvas.select_page_in_navigation_bar('two_column_page')
        verify_panel_data('Panel 1', 'Tab 1', '14.2')
        verify_panel_frame_data('text', 'Panel_2_1', 'Budget Units', '14.3', custom_css="table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)")
        verify_panel_data('Panel 3', 'Area 1', '14.4')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_4', expected_legend, '14.5')
        
        """ Step 15: Click the Close button
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """ Step 16: Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.navigate_to_legacyhomepage()
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """Step 17: Run the portal again
                     Verify that all changes are still present
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 50)
        expected_list = ['Page_designer1', 'Page_designer_fluid', 'Copy_Page1', 'Two_Col_placeholder_easy', 'two_column_page']
        portal_canvas.verify_page_in_navigation_bar('Page_designer1', "Step 17.1: Verify 'Page_designer1' in Navigation bar.", page_order_list=expected_list)
        
        portal_canvas.select_page_in_navigation_bar('Page_designer1')
        verify_panel_data('Panel 2', suite_id, '11.1')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_1', expected_legend, '17.2')
        
        portal_canvas.select_page_in_navigation_bar('Page_designer_fluid')
        verify_panel_data('Panel 1', 'Retail Samples', '17.3')
        verify_panel_data('Panel 2', 'Area 1', '17.4')
        portal_canvas.verify_panel_image('honda_integra', 'honda_integra', 'Step 17.5: Verify Honda car displayed.')
        verify_panel_data('Panel 4', suite_id, '17.6')
        
        portal_canvas.select_page_in_navigation_bar('Copy_Page1')
        verify_panel_data('Panel 1', project_id, '17.7')
        
        portal_canvas.select_page_in_navigation_bar('Two_Col_placeholder_easy')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_1', expected_legend, '17.8')
        expected_legend= ['EMEA', 'North America', 'Oceania', 'South America']
        verify_panel_frame_data('legend', 'Panel_2', expected_legend, '17.9')
        
        portal_canvas.select_page_in_navigation_bar('two_column_page')
        verify_panel_data('Panel 1', 'Tab 1', '17.10')
        verify_panel_frame_data('text', 'Panel_2', 'Budget Units', '17.11', custom_css="table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)")
        verify_panel_data('Panel 3', 'Area 1', '17.12')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_4', expected_legend, '17.13')
        
        """ Step 18: Click the Close button
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """ Step 19: In the banner link, click on the top right username > Click Sign Out.
        """
        wf_mainpage_obj.signout_from_username_dropdown_menu()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()