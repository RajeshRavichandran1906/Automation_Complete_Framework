'''
Created on 30-April-2018

@author: AAkhan(AA14564)

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324334
TestCase Name = Customizations : Tools Customizations
'''
import unittest, time
from common.lib import utillity, core_utility
from common.pages import visualization_resultarea, vfour_portal_canvas, wf_legacymainpage, ia_resultarea, vfour_portal_properties, vfour_portal_run, vfour_portal_ribbon, vfour_miscelaneous
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage

class C2324334_TestClass(BaseTestCase):

    def test_C2324334(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        wf_mainpage_obj = wf_mainpage.Wf_Mainpage(self.driver)
        user_name = utillobj.parseinitfile('mrid03')
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        BIP_Portal_Path = str(project_id)+'->'+str(suite_id)+'->BIP_V4_Portal'
        portal_name = 'BIP_Customization_Portal'
        welcome_page_parent_css = "#PortalResourcevBOX table tr td"
        edit_page_parent_css = "#applicationButtonBox img[src*='bip_button']"
        run_page_parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        
        def verify_panel_data(panel_name, expected_panel_text, step_num):
            panel_text = portal_canvas.get_panel_obj(panel_name)
            actual_panel_text = [elem.strip() for elem in panel_text.text.strip().split('\n') if elem != '']
            utillobj.asin(expected_panel_text, actual_panel_text, "Step " + str(step_num) + ": Verify 'Resource Tree' added in '" + str(panel_name) + "'.")
            
        def verify_column_data(column_no, expected_panel_in_column_text_list, step_num):
            columns_obj = portal_canvas.get_column_obj(column_no)
            actual_panel_in_column_text_list = [elem.text.strip() for elem in columns_obj.find_elements_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']") if elem != '']
            utillobj.asequal(expected_panel_in_column_text_list, actual_panel_in_column_text_list, "Step " + str(step_num) + ": Verify 'column " + str(column_no) + "' panel.")
        
        def verify_panel_frame_data(chart_type, panel_name, expected_value, step_num, custom_css="svg g>text[class^='riser!s']"):
            portal_misobj.switch_to_frame_in_bip_page(frame_panel_name=panel_name)
            if chart_type == 'legend':
                resultobj.verify_riser_legends("jschart_HOLD_0", expected_value, "Step "+str(step_num)+": Verify legend Title in '" + str(panel_name) + "'.")
            elif chart_type == 'riser':
                ia_resultobj.verify_number_of_chart_segment("jschart_HOLD_0", expected_value, "Step "+str(step_num)+": Verify number of risers displayed in '" + str(panel_name) + "'.")   
            elif chart_type == 'text':
                actual_text = self.driver.find_element_by_css_selector(custom_css).text.strip()
                utillobj.asequal(actual_text, expected_value, "Step "+str(step_num)+": Verify table data displayed in '" + str(panel_name) + "'.")
            utillobj.switch_to_default_content(pause=3)
        
        """ Step 1: Sign into WebFOCUS home page as Developer User
                    Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """ Step 2: Expand P292 domain, right click on S10117 folder and choose New -> Collaborative Portal
        """
        """ Step 3: Enter 'BIP_Customization_Portal'
                    Maximize the portal designer window
        """
        wf_mainpageobj.create_portal(BIP_Portal_Path, portal_name)
        core_utilobj.switch_to_new_window()
        utillobj.synchronize_with_number_of_element(edit_page_parent_css, 1, 50)
        portal_misobj.verify_page_template("Step 3: Verify when Portal Designer loads you are on the Layout tab", page_template="1 Column")
        
        """ Step 4: Click 2 Column template
                    Click create
        """
        portal_misobj.select_page_template(page_template="2 Column", btn_name='Create')
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('2 Column', "Step 4: Verify '2 Column' in Navigation bar.")
        
        """ Step 5: Add a tabbed container with a tree block and portal list tabs.
                    Add an accordion container in column2 with the domain and Accordion report in the other area.
        """
        portal_canvas.select_column(1)
        time.sleep(1)
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Tabbed')
        portal_canvas.select_panel('Panel 1')
        portal_ribbon.select_ribbon_item("Insert", 'Insert_ResourceTree')
        time.sleep(2)
        portal_canvas.select_tabbed_panel('Panel 1', 'New Tab')
        time.sleep(2)
        portal_ribbon.select_ribbon_item("Insert", 'Insert_PortalList')
        time.sleep(2)
        portal_canvas.select_column(2)
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Accordion')
        time.sleep(2)
        portal_ribbon.invoke_and_verify_wf_resource_tree()
        time.sleep(2)
        item_path=str(project_id)
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'panel', 'Panel 2')
        utillobj.select_or_verify_bipop_menu('Replace Area Content', custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item ']:not([style*='hidden'])")
        item_path=BIP_Portal_Path+'->Accordion_change_title'
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'panel', 'Panel 2')
        utillobj.select_or_verify_bipop_menu('Add As Area', custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item ']:not([style*='hidden'])")
        time.sleep(2)
        verify_panel_frame_data('text', 'Panel_2', 'Budget Units', '5', custom_css="table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)")
        verify_panel_data('Panel 1', portal_name, '5.1')
        
        """ Step 6: Add another 3 column page by double clicking on 3 Column option
                    Add portal list, tree block and Category sales in each column respectively
                    Unlock the page
        """
        portal_canvas.add_page('3 Column')
        time.sleep(1)
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        portal_canvas.select_column(1)
        time.sleep(1)
        portal_ribbon.select_ribbon_item("Insert", 'Insert_PortalList')
        time.sleep(2)
        portal_canvas.select_column(2)
        time.sleep(1)
        portal_ribbon.select_ribbon_item("Insert", 'Insert_ResourceTree')
        time.sleep(2)
        item_path="Retail Samples->Portal->Small Widgets->Category Sales"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'column', 3)
        time.sleep(2)
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_3', expected_legend, '6')
        time.sleep(2)
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        portal_properties.edit_input_control('page', 'Lock Page', 'checkbox', checkbox_input='uncheck', msg="Step 6.1: ")
        time.sleep(2)
        
        
        """ Step 7: Save the portal
                    Right click and Publish the portal
        """
        portal_ribbon.select_save_from_toolbar()
        time.sleep(1)
        portal_ribbon.select_tool_menu_item('menu_Exit')
        core_utilobj.switch_to_previous_window(window_close=False)
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        time.sleep(1)
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Publish')
        time.sleep(1)
        
        """ Step 8: Run the portal
                    Verify that all reports and panels are present
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        '''2 Column page verification'''
        portal_canvas.select_page_in_navigation_bar('2 Column')
        time.sleep(2)
        verify_column_data(1, ['Panel 1'], '8')
        verify_panel_data('Panel 1', 'Tab 1', '8.1')
        verify_panel_data('Panel 1', 'Tab 2', '8.2')
        verify_panel_data('Panel 1', project_id, '8.3')
        portal_canvas.select_tabbed_panel('Panel 1', 'Tab 2')
        time.sleep(2)
        verify_panel_data('Panel 1', portal_name, '8.4')
        verify_column_data(2, ['Panel 2'], '8.5')
        verify_panel_data('Panel 2', 'Area 1', '8.6')
        verify_panel_data('Panel 2', 'Accordion_change_title', '8.7')
        verify_panel_data('Panel 2', project_id, '8.8')
        portal_canvas.select_accordian_panel_title('Panel 2', 'Accordion_change_title')
        time.sleep(2)
        verify_panel_frame_data('text', 'Panel_2', 'Budget Units', '8.9', custom_css="table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)")
           
        '''3 Column page verification'''
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        verify_column_data(1, ['Panel 1'], '8.10')
        verify_panel_data('Panel 1', portal_name, '8.11')
        verify_column_data(2, ['Panel 2'], '8.12')
        verify_panel_data('Panel 2', project_id, '8.13')
        verify_column_data(3, ['Category Sales'], '8.14')
        time.sleep(2)
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_3', expected_legend, '8.15')
        time.sleep(2)
           
        """ Step 9: Add a 1 column page and drag a folder onto it.
                    Verify the page is created and Resource tree opens as well
        """
        portal_canvas.add_page('1 Column')
        time.sleep(1)
        item_path=str(project_id)
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'column', 1)
        time.sleep(1)
        verify_panel_data('Panel 1', suite_id, '9')
          
        """ Step 10: Add another page using Link to existing option. Browse to any page
                     Verify the page is created and Resource tree opens as well
        """
        folder_path=BIP_Portal_Path+"->Pages_Folder"
        file_name_list=['Page_designer1']
        portal_canvas.add_page_with_existing_link('navigation_bar','Link To Existing Page...', folder_path, file_name_list, close_add_page_dialog=None)
        portal_canvas.verify_page_in_navigation_bar('Page_designer1', "Step 10: Verify 'Page_designer1' in Navigation bar.")
        verify_column_data(1, ['Category Sales'], '10.1')
        verify_column_data(2, ['Panel 2'], '10.2')
        verify_panel_data('Panel 2', 'BIP_V4_Portal', '10.3')
          
        """ Step 11: Add another page using Copy existing Page option. Browse to any page
                     Verify the page is created and Resource tree opens as well
        """
        file_name_list=['Page_designer_fluid']
        portal_canvas.add_page_with_existing_link('navigation_bar','Copy Existing Page...', folder_path, file_name_list)
        portal_canvas.verify_page_in_navigation_bar('Page_designer_fluid', "Step 11: Verify 'Page_designer_fluid' in Navigation bar.")
        verify_panel_data('Panel 4', 'BIP_V4_Portal', '11.1')
          
        """ Step 12: Click on 3 Column page
                     Drag a report to that page.
                     Verify that the report shows.
        """
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        item_path=BIP_Portal_Path+'->Accordion_change_title'
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'panel', 'Panel 1', drop_point='bottom_middle')
        portal_misobj.switch_to_frame_in_bip_page('Panel_4')
        utillobj.synchronize_with_visble_text("table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)", 'Budget Units', 90)
        utillobj.switch_to_default_content()
        verify_panel_frame_data('text', 'Panel_4', 'Budget Units', '12', custom_css="table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)")
         
        """ Step 13: Close the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """ Step 14: Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.navigate_to_legacyhomepage()
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """ Step 15: Rerun the portal
                     Verify that all the changes are still there.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(3)
        portal_canvas.verify_page_in_navigation_bar('3 Column', "Step 15: Verify '3 Column' page in navigation bar and pages are ordered.", page_order_list=['2 Column', '3 Column', '1 Column', 'Page_designer1', 'Page_designer_fluid'])
        verify_column_data(1, ['Panel 1', 'Accordion_change_title'], '15.1')
        portal_misobj.switch_to_frame_in_bip_page('Panel_4')
        utillobj.synchronize_with_visble_text("table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)", 'Budget Units', 90)
        utillobj.switch_to_default_content()
        verify_panel_frame_data('text', 'Panel_4', 'Budget Units', '15.2', custom_css="table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)")
        
        """ Step 16: Click Sign Out
                     Sign in as Domain Advanced user
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid02', 'mrpass02')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(3)
        
        """ Step 17: Add some content on 3 Column page
                     Add another page with some content
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(1)
        item_path=str(project_id)
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'panel', 'Panel 1', drop_point='bottom_middle')
        time.sleep(3)
        verify_column_data(1, ['Panel 1', 'Panel 4'], '17')
        verify_panel_data('Panel 4', suite_id, '17.1')
        portal_canvas.add_page('1 Column')
        time.sleep(1)
        item_path='Retail Samples'
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'column', 1)
        time.sleep(1)
        verify_panel_data('Panel 1', 'Portal', '17.2')
        
        """ Step 18: Click Sign Out and sign back in as WF Developer
                     Verify that all the changes are still there.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid03', 'mrpass03')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(3)
        portal_canvas.verify_page_in_navigation_bar('3 Column', "Step 18: Verify '3 Column' page in navigation bar and pages are ordered.", page_order_list=['2 Column', '3 Column', '1 Column', 'Page_designer1', 'Page_designer_fluid'])
        verify_column_data(1, ['Panel 1', 'Accordion_change_title'], '18.1')
        portal_misobj.switch_to_frame_in_bip_page('Panel_4')
        utillobj.synchronize_with_visble_text("table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)", 'Budget Units', 90)
        utillobj.switch_to_default_content()
        verify_panel_frame_data('text', 'Panel_4', 'Budget Units', '18.2', custom_css="table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)")
        
        """ Step 19: Click on the user link then choose Remove My Customizations
                     Click Yes
                     Verify that the portal refreshes and the changes are not there anymore
        """
        panel1_obj = portal_canvas.get_panel_obj('Panel 1')
        portal_run.select_or_verify_portal_menu_bar_item(select=user_name, option='Remove My Customizations')
        dialog_css = "[id*='BiDialog'] [class*='active']"
        utillobj.synchronize_with_number_of_element(dialog_css, 1, 90)
        utillobj.click_dialog_button(dialog_css, 'Yes')
        portal_misobj.synchronize_until_element_disappear(dialog_css, 0, 27)
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 90)
        try:
            panel1_obj.text
        except:
            ready_state = self.driver.execute_script("return document.readyState")
            utillobj.asequal('complete', ready_state, 'Step 19: Verify page is Refreshed and Portal is reloaded.')
        portal_canvas.verify_page_in_navigation_bar('3 Column', "Step 19.1: Verify '3 Column' page in navigation bar and pages are ordered.", page_order_list=['2 Column', '3 Column'])
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        verify_column_data(1, ['Panel 1'], '17.2')
        
        """ Step 20: Click Sign Out
                     Sign in as Domain advanced user
                     Verify that the changes this user made are still there.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid02', 'mrpass02')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(3)
        verify_column_data(1, ['Panel 1', 'Panel 4'], '20')
        verify_panel_data('Panel 4', suite_id, '18.1')
        portal_canvas.verify_page_in_navigation_bar('3 Column', "Step 20.1: Verify '3 Column' page in navigation bar and pages are ordered.", page_order_list=['2 Column', '3 Column', '1 Column'])
        
        """ Step 21: Click Sign Out and sign back in as WF developer
                     Close the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid03', 'mrpass03')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """ Step 22: In the banner link, click on the top right username > Click Sign Out.
        """
        wf_mainpage_obj.signout_from_username_dropdown_menu()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()