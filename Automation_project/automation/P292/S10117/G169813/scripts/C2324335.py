'''
Created on 02-May-2018

@author: AAkhan(AA14564)

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324335
TestCase Name = Customizations : Run Page customizations
'''
import unittest, time
from common.lib import utillity
from common.pages import vfour_portal_canvas, wf_legacymainpage, vfour_portal_run, vfour_portal_ribbon, vfour_miscelaneous
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage

class C2324335_TestClass(BaseTestCase):

    def test_C2324335(self):
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
        wf_mainpage_obj = wf_mainpage.Wf_Mainpage(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        BIP_Portal_Path = str(project_id)+'->'+str(suite_id)+'->BIP_V4_Portal'
        portal_name = 'BIP_Customization_Portal'
        welcome_page_parent_css = "#PortalResourcevBOX table tr td"
        run_page_parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        
        def verify_panel_data(panel_name, expected_panel_text, step_num):
            panel_text = portal_canvas.get_panel_obj(panel_name)
            actual_panel_text = [elem.strip() for elem in panel_text.text.strip().split('\n') if elem != '']
            utillobj.asin(expected_panel_text, actual_panel_text, "Step " + str(step_num) + ": Verify 'Resource Tree' added in '" + str(panel_name) + "'.")
            
        def verify_column_data(column_no, expected_panel_in_column_text_list, step_num):
            columns_obj = portal_canvas.get_column_obj(column_no)
            actual_panel_in_column_text_list = [elem.text.strip() for elem in columns_obj.find_elements_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']") if elem != '']
            utillobj.asequal(expected_panel_in_column_text_list, actual_panel_in_column_text_list, "Step " + str(step_num) + ": Verify 'column " + str(column_no) + "' panel.")
        
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
        
        """ Step 2: Open 'P292_S10117_G169813' domain->S10117 from domains tree,
                    Run the 'BIP_Customization_Portal'
                    Verify that you have 2 pages (2 Column and 3 Column)
                    3 Column has 3 panels and 3 columns.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('2 Column', "Step 2: Verify '2 Column' page in navigation bar and pages are ordered.", page_order_list=['2 Column', '3 Column'])
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        verify_column_data(1, ['Panel 1'], '2.1')
        verify_panel_data('Panel 1', portal_name, '2.2')
        verify_column_data(2, ['Panel 2'], '2.3')
        verify_panel_data('Panel 2', project_id, '2.4')
        verify_column_data(3, ['Category Sales'], '2.5')
        time.sleep(2)
        
        """ Step 3: Right Click on the 3 column page tab and choose page layout.
                    Change it to 4 columns
        """
        portal_canvas.manage_page_menu('3 Column', 'Page Layout', page_layout='Four Column')
        
        """ Step 4: Drag retail samples domain to column 4
                    Verify that the folder is now in column 4
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(2)
        item_path='Retail Samples'
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'column', 4)
        time.sleep(1)
        verify_column_data(4, ['Panel 4'], '4')
        verify_panel_data('Panel 4', 'Portal', '2.4')
        
        """ Step 5: Click sign Out
                    Sign in as Domain Basic user
                    Verify that the 4th column is not there.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid01', 'mrpass01')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        verify_total_column_panel_name(['Panel 1', 'Panel 2', 'Category Sales'], 'Step 5: Verify that the 4th column is not there.')
        time.sleep(2)
                
        """ Step 6: Add another image in column 1 of this page.
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(2)
        item_path=BIP_Portal_Path+'->babydeer'
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'panel', 'Panel 1', drop_point='bottom_middle')
        time.sleep(2)
        verify_column_data(1, ['Panel 1','babydeer'], '6')
        time.sleep(2)
        
        """ Step 7: Click Sign Out and sign back in as WF Developer
                    Verify that this image added is not there.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid03', 'mrpass03')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        verify_total_column_panel_name(['Panel 1', 'Panel 2', 'Category Sales', 'Panel 4'], 'Step 7: Verify that this image added is not there.')
        time.sleep(2)
        
        """ Step 8: Add another page. does not matter which layout or if there is content added.
        """
        portal_canvas.add_page('1 Column')
        time.sleep(1)
        item_path=str(project_id)
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'column', 1)
        time.sleep(1)
        verify_panel_data('Panel 1', suite_id, '8')
        
        """ Step 9: Right click on the 3 Column page tab and choose Remove My Customizations
                    Verify that the page refreshes and the 4th column is no longer there or any other content added. The page should be back to its original state.
                    Verify that the new page added is also there.
        """
        portal_canvas.manage_page_menu('3 Column', 'Remove My Customizations')
        time.sleep(2)
        portal_canvas.select_page_in_navigation_bar('3 Column')
        portal_misobj.switch_to_frame_in_bip_page(frame_panel_name='Panel_3')
        utillobj.synchronize_with_number_of_element("#jschart_HOLD_0 .legend text", 8, 27)
        utillobj.switch_to_default_content()
        time.sleep(1)
        verify_total_column_panel_name(['Panel 1', 'Panel 2', 'Category Sales'], 'Step 9: Verify that this image added is not there.')
        portal_canvas.verify_page_in_navigation_bar('1 Column', "Step 9.1: Verify '1 Column' page in navigation bar and pages are ordered.", page_order_list=['2 Column', '3 Column', '1 Column'])
        
        """ Step 10: Click Sign Out
                     Sign in as Domain Basic user
                     Verify that this user's changes are still there
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid01', 'mrpass01')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        portal_canvas.verify_page_in_navigation_bar('3 Column', "Step 9.1: Verify '3 Column' page in navigation bar and pages are ordered.", page_order_list=['2 Column', '3 Column'])
        portal_canvas.select_page_in_navigation_bar('3 Column')
        verify_column_data(1, ['Panel 1','babydeer'], '10')
        
        """ Step 11: Click Sign Out and sign back in as WF Developer
                     Close the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid03', 'mrpass03')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 45)
        
        """ Step 12: In the banner link, click on the top right username > Click Sign Out.
        """
        wf_mainpage_obj.signout_from_username_dropdown_menu()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()