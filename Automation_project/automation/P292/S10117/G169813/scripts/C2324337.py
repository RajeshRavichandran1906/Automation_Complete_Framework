'''
Created on 03-May-2018

@author: AAkhan(AA14564)

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324337
TestCase Name = Page Testing : Unlink_Pages
'''
import unittest, time
from common.lib import utillity
from common.pages import vfour_portal_canvas, wf_legacymainpage, vfour_portal_run, vfour_portal_ribbon, vfour_miscelaneous, visualization_resultarea, ia_resultarea, vfour_portal_properties
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage

class C2324337_TestClass(BaseTestCase):

    def test_C2324337(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        wf_mainpage_obj = wf_mainpage.Wf_Mainpage(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        BIP_Portal_Path = str(project_id)+'->'+str(suite_id)+'->BIP_V4_Portal'
        portal_name = 'BIP_Unlink_Portal'
        welcome_page_parent_css = "#PortalResourcevBOX table tr td"
        edit_page_parent_css = "#applicationButtonBox img[src*='bip_button']"
        run_page_parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        welcome_page_css="img[src*='Welcome']"
        
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
        
        def verify_total_column_panel_name(expected_panel_names, msg):
            current_page = portal_canvas.get_current_page()
            columns=current_page.find_elements_by_css_selector("[class*='bip-column']")
            panel_names = []
            for column_elem in columns:
                panels = column_elem.find_elements_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
                for panel_elem in panels:
                    panel_names.append(panel_elem.text.strip())
            utillobj.as_List_equal(panel_names, expected_panel_names, msg)
                    
        
        """ Step 1: Sign into WebFOCUS home page as Developer User
                    Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
         
        """ Step 2: Expand 'P292_S10117_G169813' domain , right click on S10117 folder and choose New > Collaborative Portal.
        """
        """ Step 3: Enter 'BIP_Unlink_Portal'
                    Maximize the portal designer window
        """
        wf_mainpageobj.create_portal(BIP_Portal_Path, portal_name)
        utillobj.switch_to_window(1)
        utillobj.synchronize_with_number_of_element(edit_page_parent_css, 1, 50)
        portal_misobj.verify_page_template("Step 3: Verify when Portal Designer loads you are on the Layout tab", page_template="1 Column")
          
        """ Step 4: Click 2 Column template
                    Click Create button
        """
        portal_misobj.select_page_template(page_template="2 Column", btn_name='Create')
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('2 Column', "Step 4: Verify '2 Column' in Navigation bar.")
          
        """ Step 5: Add a tabbed container with a tree block and portal list tabs.
                    Add an accordion container in column2 with retail samples and Accordion report in the other area.
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
        item_path='Retail Samples'
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'panel', 'Panel 2')
        utillobj.select_or_verify_bipop_menu('Replace Area Content', custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item ']:not([style*='hidden'])")
        item_path=BIP_Portal_Path+'->Accordion_change_title'
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'panel', 'Panel 2')
        utillobj.select_or_verify_bipop_menu('Add As Area', custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item ']:not([style*='hidden'])")
        time.sleep(2)
        verify_panel_frame_data('text', 'Panel_2', 'Budget Units', '5', custom_css="table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)")
        verify_panel_data('Panel 1', portal_name, '5.1')
          
          
        """ Step 6: Add another 3 column page by double clicking on 3 Column option
                    add portal list, tree block and category sales in each column respectively
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
          
        """ Step 7: Save and exit the portal 
                    Right click and Publish the portal
        """
        portal_ribbon.select_save_from_toolbar()
        time.sleep(1)
        portal_ribbon.select_tool_menu_item('menu_Exit')
        utillobj.switch_to_window(0, pause=9)
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
        verify_panel_data('Panel 2', 'Portal', '8.8')
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
          
        """ Step 9: Add another page with some content.
        """
        portal_canvas.add_page('1 Column')
        time.sleep(1)
        item_path=str(project_id)
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'column', 1)
        time.sleep(1)
        verify_panel_data('Panel 1', suite_id, '9')
          
        """ Step 10: Click Sign Out
                     Sign in as Domain Advanced user
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid02', 'mrpass02')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
          
        """ Step 11: Add some content on 3 Column page
                     Add another page with some content
        """
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(2)
        item_path=BIP_Portal_Path+'->babydeer'
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'panel', 'Panel 1', drop_point='bottom_middle')
        time.sleep(2)
        verify_column_data(1, ['Panel 1','babydeer'], '11')
        time.sleep(2)
        portal_canvas.add_page('1 Column')
        time.sleep(1)
        item_path='Retail Samples'
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'column', 1)
        time.sleep(1)
        verify_panel_data('Panel 1', 'Portal', '11.1')
          
        """ Step 12: Click Sign Out and sign back in as WF Developer
                     Verify that all the changes are still there.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid03', 'mrpass03')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('2 Column', "Step 12: Verify '2 Column' page in navigation bar and pages are ordered.", page_order_list=['2 Column', '3 Column', '1 Column'])
        '''2 Column page verification'''
        portal_canvas.select_page_in_navigation_bar('2 Column')
        time.sleep(2)
        verify_total_column_panel_name(['Panel 1', 'Panel 2'], 'Step 12.1: Verify 2 Column page.')
        time.sleep(1)
             
        '''3 Column page verification'''
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        verify_total_column_panel_name(['Panel 1', 'Panel 2', 'Category Sales'], 'Step 12.2: Verify 3 Column page.')
        time.sleep(1)
        '''1 Column page verification'''
        portal_canvas.select_page_in_navigation_bar('1 Column')
        time.sleep(2)
        verify_total_column_panel_name(['Panel 1'], 'Step 112.3: Verify 1 Column page.')
        time.sleep(1)
          
        """ Step 13: Close the portal and Navigate URL to http://environment_name:port/alias/legacyhome
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.navigate_to_legacyhomepage()
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 45)
         
        """ Step 14: Open the Resource folder
                     Verify that 2 pages are there (2 Column and 3 Column)
        """
        wf_mainpageobj.verify_repositery_item(BIP_Portal_Path+'->BIP_Unlink_Portal Resources->2 Column', '2 Column', msg='14')
        time.sleep(1)
        welcome_page=self.driver.find_element_by_css_selector(welcome_page_css)
        utillobj.default_click(welcome_page)
        wf_mainpageobj.verify_repositery_item(BIP_Portal_Path+'->BIP_Unlink_Portal Resources->2 Column', '3 Column', msg='14.1')
        welcome_page=self.driver.find_element_by_css_selector(welcome_page_css)
        utillobj.default_click(welcome_page)
        
        """ Step 15: Right click on both pages
                     Verify that the Unlink menu is there.
        """
        wf_mainpageobj.select_menu(BIP_Portal_Path+'->BIP_Unlink_Portal Resources->2 Column', expected_menu_list=['Unlink'], item_exit=True, msg='Step 15:')
        time.sleep(1)
        welcome_page=self.driver.find_element_by_css_selector(welcome_page_css)
        utillobj.default_click(welcome_page)
        wf_mainpageobj.select_menu(BIP_Portal_Path+'->BIP_Unlink_Portal Resources->3 Column', expected_menu_list=['Unlink'], item_exit=True, msg='Step 15.1:')
        welcome_page=self.driver.find_element_by_css_selector(welcome_page_css)
        utillobj.default_click(welcome_page)
        
        """ Step 16: Run the portal
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        
        """ Step 17: In 2 Column page Open the BIP_Unlink_Portal resource folder in the resource tree panel right click on 3 Column page.
                     In 3 Column page Open the BIP_Unlink_Portal resource folder in the resource tree panel right click on 2 Column page.
        """
        '''2 Column page verification'''
        portal_canvas.select_page_in_navigation_bar('2 Column')
        time.sleep(2)
        portal_canvas.select_tabbed_panel('Panel 1', 'Tab 1')
        time.sleep(2)
        panel_obj = portal_canvas.get_panel_obj('Panel 1')
        portal_run.select_menu(BIP_Portal_Path+'->BIP_Unlink_Portal Resources->3 Column', scrollable_elem=panel_obj, expected_menu_list=['Unlink'], item_exit=True, msg='Step 17:')
        time.sleep(1)
             
        '''3 Column page verification'''
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        panel_obj = portal_canvas.get_panel_obj('Panel 2')
        portal_run.select_menu(BIP_Portal_Path+'->BIP_Unlink_Portal Resources->2 Column', scrollable_elem=panel_obj, expected_menu_list=['Unlink'], item_exit=True, msg='Step 17.1:')
        time.sleep(1)
        
        """ Step 18: Press F8 to bring up the resource tree
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        
        """ Step 19: Open the Resource folder
                     Right click on both pages
                     Verify that the Unlink menu is there.
        """
        resource_tree_panel_css="#bipResourcesPanel"
        resource_tree_css=resource_tree_panel_css+" #treeView table>tbody>tr"
        resource_tree_elem = self.driver.find_element_by_css_selector(resource_tree_panel_css)
        portal_run.select_menu(BIP_Portal_Path+'->BIP_Unlink_Portal Resources->2 Column', tree_elem_css=resource_tree_css, scrollable_elem=resource_tree_elem, expected_menu_list=['Unlink'], item_exit=True, msg='Step 19:')
        portal_canvas.select_page_in_navigation_bar('3 Column')
        portal_run.select_menu(BIP_Portal_Path+'->BIP_Unlink_Portal Resources->3 Column', tree_elem_css=resource_tree_css, scrollable_elem=resource_tree_elem, expected_menu_list=['Unlink'], item_exit=True, msg='Step 19.1:')
        portal_canvas.select_page_in_navigation_bar('3 Column')
        
        """ Step 20: Pick 2 Column page and choose Unlink
                     Click Ok in the confirmation popup
        """
        portal_run.select_menu(BIP_Portal_Path+'->BIP_Unlink_Portal Resources->2 Column', menu_item='Unlink', tree_elem_css=resource_tree_css, scrollable_elem=resource_tree_elem)
        dialog_css = "[id*='BiDialog'] [class*='active']"
        utillobj.synchronize_with_number_of_element(dialog_css, 1, 90)
        utillobj.click_dialog_button(dialog_css, 'OK')
        portal_misobj.synchronize_until_element_disappear(dialog_css, 0, 27)
        
        """ Step 21: If the Browser does not refresh please do so.
                     Verify that the page is no longer in the portal
        """
        self.driver.refresh()
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('2 Column', "Step 21: Verify '2 Column' page is no longer in the portal.",  verify=False, page_order_list=['3 Column', '1 Column'])
        
        """ Step 22: Click Sign Out
                     Sign in as Domain Advanced user
                     Verify that the 2 column page is no longer in the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid02', 'mrpass02')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('2 Column', "Step 22: Verify '2 Column' page is no longer in the portal.", verify=False, page_order_list=['3 Column', '1 Column'])
        
        """ Step 23: Click Sign Out and sign back in as WF Developer
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid03', 'mrpass03')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(1)
        
        """ Step 24: Close the portal and Navigate URL to http://environment_name:port/alias/legacyhome
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.navigate_to_legacyhomepage()
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 45)
        
        """ Step 25: In the banner link, click on the top right username > Click Sign Out.
        """
        wf_mainpage_obj.signout_from_username_dropdown_menu()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()