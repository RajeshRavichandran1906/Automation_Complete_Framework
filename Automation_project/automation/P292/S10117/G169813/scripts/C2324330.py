'''
Created on 07-Feb-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324330
TestCase Name = Portal Designer_Selecting Pages : Select_Linked_Pages
'''
import unittest, time
from common.lib import utillity, core_utility
from common.pages import visualization_resultarea, vfour_portal_canvas, wf_legacymainpage, vfour_portal_run, vfour_portal_ribbon, vfour_miscelaneous, ia_resultarea
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage

class C2324330_TestClass(BaseTestCase):

    def test_C2324330(self):
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
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        wf_mainpage_obj = wf_mainpage.Wf_Mainpage(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        root_path = project_id+'->'+suite_id
        BIP_Portal_Path = root_path+'->BIP_V4_Portal'
        portal_name = 'Select_Linked_Page'
        
        def verify_panel_data(panel_name, expected_panel_text, step_num):
            panel_text = portal_canvas.get_panel_obj(panel_name)
            actual_panel_text = [elem.strip() for elem in panel_text.text.strip().split('\n') if elem != '']
            utillobj.asin(expected_panel_text, actual_panel_text, "Step " + str(step_num) + ": Verify 'Resource Tree' added in '" + str(panel_name) + "'.")
            
        def verify_column_data(column_no, expected_column_text, step_num):
            column_text = portal_canvas.get_column_obj(column_no)
            actual_column_text_list = [elem.strip() for elem in column_text.text.strip().split('\n') if elem != '']
            utillobj.asin(expected_column_text, actual_column_text_list, "Step " + str(step_num) + ": Verify 'column " + str(column_no) + "' panel.")
        
        def verify_panel_frame_data(chart_type, panel_name, expected_legend, step_num, custom_css="svg g>text[class^='riser!s']"):
            portal_misobj.switch_to_frame_in_bip_page(frame_panel_name=panel_name)
            if chart_type == 'legend':
                resultobj.verify_riser_legends("jschart_HOLD_0", expected_legend, "Step "+str(step_num)+": Verify legend Title in '" + str(panel_name) + "'.")
            elif chart_type == 'riser':
                ia_resultobj.verify_number_of_chart_segment("jschart_HOLD_0", expected_legend, "Step "+str(step_num)+": Verify number of risers displayed in '" + str(panel_name) + "'.", custom_css=custom_css)   
            utillobj.switch_to_default_content(pause=3)
        
        
        """ Step 1: Sign into WebFOCUS home page as Developer User if you are not already
                    Navigate URL to http://environment name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        time.sleep(1)
         
        """ Step 2: Expand P292 domain, right Click on the S10117 folder from domains tree and choose New -> Collaborative Portal
        """
        """ Step 3: Enter 'Select_Linked_Page'
        """
        wf_mainpageobj.create_portal(BIP_Portal_Path, portal_name)
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(self.driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        core_utilobj.switch_to_new_window()
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        portal_misobj.verify_page_template("Step 3: Verify when Portal Designer loads you are on the Layout tab", page_template="1 Column")
         
        """ Step 4: Click on the Link to Existing Icon from the page canvas
                    Verify that an explorer window shows up
        """
        """ Step 5: Open the domain where the page folder resides
                    Select 'Pages_Folder'
        """
        """ Step 6: Choose both pages (Page_designer_fluid and Page_designer1) then click the Open button
                    Verify that the pages now appear and the content is correct
        """
        folder_path=BIP_Portal_Path+"->Pages_Folder"
        file_name_list=['Page_designer1', 'Page_designer_fluid']
        portal_canvas.add_page_with_existing_link('page','Link To Existing Page...', folder_path, file_name_list, close_add_page_dialog=None)
         
        portal_canvas.verify_page_in_navigation_bar('Page_designer1', "Step 6: Verify 'Page_designer1' in Navigation bar.", page_order_list=['Page_designer1', 'Page_designer_fluid'])
         
        portal_canvas.select_page_in_navigation_bar('Page_designer1')
        verify_panel_data('Panel 2', suite_id, '6.1')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_1', expected_legend, '6.2')
         
        portal_canvas.select_page_in_navigation_bar('Page_designer_fluid')
        verify_panel_data('Panel 1', 'Retail Samples', '6.3')
        verify_panel_data('Panel 2', 'Area 1', '6.4')
        portal_canvas.verify_panel_image('honda_integra', 'honda_integra', 'Step 6.5: Verify Honda car displayed.')
        verify_panel_data('Panel 4', suite_id, '6.6')
         
        """ Step 7: Click the new page icon and choose link to existing page.
                    Choose a page is already chosen and click create
                    Verify that you get an error message stating that the page is already in the portal 
        """
        folder_path=BIP_Portal_Path+"->Pages_Folder"
        file_name_list=['Page_designer1']
        portal_canvas.add_page_with_existing_link('navigation_bar','Link To Existing Page...', folder_path, file_name_list, close_add_page_dialog=None)
         
        utillobj.verify_js_alert('Page already in portal.', "Step 7: Verify that you get an error message stating that the page is already in the portal")
        time.sleep(2)
        portal_canvas.close_add_page_dialog("div[id='dlgTitleExplorer'] [class*='window'][class*='active']", 'Cancel')
         
        """ Step 8: Click another page layout that is already there and give it the same name and title
                    Click change location. choose the same location as the other pages added.
                    Cancel out of that page template window
                    Verify that you get an error message stating that the page is already in the portal 
        """
        location_text='/Repository/'+project_id+'/'+suite_id+'/BIP_V4_Portal/Pages_Folder'
        path='BIP_V4_Portal->Pages_Folder'
        portal_canvas.add_page('2 Column', Page_title='Page_designer1', Page_name='Page_designer1', change_location=path, close_browser_folder_dialog='ok', verify_location=location_text, msg="Step 8: Verify location after changed.", page_verify=False)
        time.sleep(1)
         
        utillobj.verify_js_alert('Page already in portal.', "Step 8: Verify that you get an error message stating that the page is already in the portal")
        time.sleep(2)
        portal_canvas.close_add_page_dialog("div[id='dlgTitleExplorer'] [class*='window'][class*='active']", 'Cancel')
         
        """ Step 9: Click the new page icon and add another 1 column page with a tree block
        """
        portal_canvas.add_page('1 Column', Page_title='Linked_Page1')
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_ResourceTree')
        time.sleep(2)
        verify_panel_data('Panel 1', project_id, '11')
         
        """ Step 10: Exit and save
        """
        portal_ribbon.bip_save_and_exit('Yes')
        time.sleep(3)
        core_utilobj.switch_to_previous_window(window_close=False)
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 90)
        time.sleep(1)
        
        """ Step 11: Run the portal
                     Verify that the pages were added in the right order and no issues.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        portal_canvas.verify_page_in_navigation_bar('Page_designer1', "Step 11: Verify 'Page_designer1' in Navigation bar.", page_order_list=['Page_designer1', 'Page_designer_fluid', 'Linked_Page1'])
        
        portal_canvas.select_page_in_navigation_bar('Page_designer1')
        verify_panel_data('Panel 2', suite_id, '11.1')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_1', expected_legend, '11.2')
        
        portal_canvas.select_page_in_navigation_bar('Page_designer_fluid')
        verify_panel_data('Panel 1', 'Retail Samples', '11.3')
        verify_panel_data('Panel 2', 'Area 1', '11.4')
        portal_canvas.verify_panel_image('honda_integra', 'honda_integra', 'Step 11.5: Verify Honda car displayed.')
        verify_panel_data('Panel 4', suite_id, '11.6')
        
        portal_canvas.select_page_in_navigation_bar('Linked_Page1')
        verify_panel_data('Panel 1', project_id, '11.7')
        
        """ Step 12: Click the new page icon and select Link to existing option for a page from any resource folder
                     Verify the page was added
        """
        folder_path=BIP_Portal_Path+"->lock column portal Resources"
        file_name_list=['Two_Col_placeholder_easy']
        portal_canvas.add_page_with_existing_link('navigation_bar','Link To Existing Page...', folder_path, file_name_list, close_add_page_dialog=None)
        
        utillobj.synchronize_with_number_of_element("div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton']", 4, 15)
        time.sleep(1)
        expected_list = ['Page_designer1', 'Page_designer_fluid', 'Linked_Page1', 'Two_Col_placeholder_easy']
        portal_canvas.verify_page_in_navigation_bar('Page_designer1', "Step 12: Verify 'Page_designer1' in Navigation bar.", page_order_list=expected_list)
        
        portal_canvas.select_page_in_navigation_bar('Two_Col_placeholder_easy')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_1', expected_legend, '12.1')
        expected_legend= ['EMEA', 'North America', 'Oceania', 'South America']
        verify_panel_frame_data('legend', 'Panel_2', expected_legend, '12.2')
        
        """ Step 13: Click the new page icon and add another page
        """
        portal_canvas.add_page('1 Column', Page_title='Linked_Page2')
        time.sleep(1)
        item_path=root_path
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'column', 1)
        verify_panel_data('Panel 1', suite_id, '13')
         
         
        """ Step 14: Click the Close button
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
         
        """ Step 15: Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.navigate_to_legacyhomepage()
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 90)
        
        """ Step 16: Run the portal again
                     Verify that all changes are still present
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        time.sleep(1)
        expected_list = ['Page_designer1', 'Page_designer_fluid', 'Linked_Page1', 'Two_Col_placeholder_easy', 'Linked_Page2']
        portal_canvas.verify_page_in_navigation_bar('Page_designer1', "Step 16: Verify 'Page_designer1' in Navigation bar.", page_order_list=expected_list)
         
        portal_canvas.select_page_in_navigation_bar('Page_designer1')
        verify_panel_data('Panel 2', suite_id, '16.1')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_1', expected_legend, '16.2')
        
        portal_canvas.select_page_in_navigation_bar('Page_designer_fluid')
        verify_panel_data('Panel 1', 'Retail Samples', '16.3')
        verify_panel_data('Panel 2', 'Area 1', '16.4')
        portal_canvas.verify_panel_image('honda_integra', 'honda_integra', 'Step 16.5: Verify Honda car displayed.')
        verify_panel_data('Panel 4', suite_id, '16.6')
        
        portal_canvas.select_page_in_navigation_bar('Linked_Page1')
        verify_panel_data('Panel 1', project_id, '16.7')
        
        portal_canvas.select_page_in_navigation_bar('Two_Col_placeholder_easy')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_1', expected_legend, '16.8')
        expected_legend= ['EMEA', 'North America', 'Oceania', 'South America']
        verify_panel_frame_data('legend', 'Panel_2', expected_legend, '16.9')
        
        portal_canvas.select_page_in_navigation_bar('Linked_Page2')
        verify_panel_data('Panel 1', suite_id, '16.10')
        
        
        """ Step 17: Click the Close button
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value=workspace, with_regular_exprestion=True)
        
        """ Step 18: In the banner link, click on the top right username > Click Sign Out.
        """
        wf_mainpage_obj.signout_from_username_dropdown_menu()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()