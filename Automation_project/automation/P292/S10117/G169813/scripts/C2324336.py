'''
Created on 02-May-2018

@author: AAkhan(AA14564)

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324336
TestCase Name = Customizations : Tree own/all customizations
'''
import unittest, time
from common.lib import utillity
from common.pages import vfour_portal_canvas, wf_legacymainpage, vfour_portal_run, vfour_miscelaneous
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage

class C2324336_TestClass(BaseTestCase):

    def test_C2324336(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
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

        """ Step 2: Open 'P292_S10117_G169813' domain->S10117 from domains tree and right Click on 'BIP_Customization_Portal', 
                    Choose Customizations --> Remove My Customizations
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Customizations->Remove My Customizations')
        dialog_css = "[id*='BiDialog'] [class*='active']"
        utillobj.synchronize_with_number_of_element(dialog_css, 1, 90)
        
        """ Step 3: Click No on the confirmation popup
        """
        utillobj.click_dialog_button(dialog_css, 'No')
        portal_misobj.synchronize_until_element_disappear(dialog_css, 0, 27)
        
        """ Step 4: Run the portal
                    Verify that the run time added page is still there.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('1 Column', "Step 4: Verify '1 Column' page in navigation bar and pages are ordered.", page_order_list=['2 Column', '3 Column', '1 Column'])
        
        """ Step 5: Close the portal and Navigate URL to http://environment_name:port/alias/legacyhome
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.navigate_to_legacyhomepage()
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 45)
        time.sleep(2)
        
        """ Step 6: Right Click on 'BIP_Customization_Portal'
                    Choose Customizations --> Remove My Customizations
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Customizations->Remove My Customizations')
        dialog_css = "[id*='BiDialog'] [class*='active']"
        utillobj.synchronize_with_number_of_element(dialog_css, 1, 90)
        
        """ Step 7: Click Yes on the confirmation popup
        """
        utillobj.click_dialog_button(dialog_css, 'Yes')
        portal_misobj.synchronize_until_element_disappear(dialog_css, 0, 27)
        
        """ Step 8: Run the portal
                    Verify that the portal is back to its original state
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('2 Column', "Step 8: Verify '2 Column' page in navigation bar and pages are ordered.", page_order_list=['2 Column', '3 Column'])
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        verify_column_data(1, ['Panel 1'], '8.1')
        verify_panel_data('Panel 1', portal_name, '8.2')
        verify_column_data(2, ['Panel 2'], '8.3')
        verify_panel_data('Panel 2', project_id, '8.4')
        verify_column_data(3, ['Category Sales'], '8.5')
        time.sleep(2)
        
        """ Step 9: Click Sign Out
                    Sign in as Domain Advanced user
                    Verify that this portal was not affected.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid02', 'mrpass02')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('1 Column', "Step 9: Verify '1 Column' page in navigation bar and pages are ordered.", page_order_list=['2 Column', '3 Column', '1 Column'])
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        verify_column_data(1, ['Panel 1', 'Panel 4'], '9.1')
        time.sleep(2)
        portal_canvas.select_page_in_navigation_bar('1 Column')
        time.sleep(2)
        verify_column_data(1, ['Panel 1'], '9.2')
        verify_panel_data('Panel 1', 'Portal', '9.3')
        
        """ Step 10: Click Sign Out
                     Sign in as Domain Basic user
                     Verify that this portal was not affected.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid01', 'mrpass01')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('2 Column', "Step 10: Verify '2 Column' page in navigation bar and pages are ordered.", page_order_list=['2 Column', '3 Column'])
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        verify_column_data(1, ['Panel 1', 'babydeer'], '10.1')
        
        """ Step 11: Click Sign Out and sign back in as WF Developer
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid03', 'mrpass03')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(1)
        
        """ Step 12: Click Close and Navigate URL to http://environment_name:port/alias/legacyhome
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.navigate_to_legacyhomepage()
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 45)
        
        """ Step 13: Right Click on 'BIP_Customization_Portal'
                     Choose Customizations --> Remove Customizations for all users
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Customizations->Remove Customizations for All Users')
        dialog_css = "[id*='BiDialog'] [class*='active']"
        utillobj.synchronize_with_number_of_element(dialog_css, 1, 90)
        
        """ Step 14: Click Yes on the confirmation popup
        """
        utillobj.click_dialog_button(dialog_css, 'Yes')
        portal_misobj.synchronize_until_element_disappear(dialog_css, 0, 27)
        
        """ Step 15: Run the portal
                     Click signout
                     Sign in as Domain Advanced user
                     Verify that the portal is back to its original state
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid02', 'mrpass02')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        portal_canvas.verify_page_in_navigation_bar('2 Column', "Step 15: Verify '2 Column' page in navigation bar and pages are ordered.", page_order_list=['2 Column', '3 Column'])
        
        '''2 Column page verification'''
        portal_canvas.select_page_in_navigation_bar('2 Column')
        time.sleep(2)
        verify_total_column_panel_name(['Panel 1', 'Panel 2'], 'Step 15.1: Verify 2 Column page.')
        time.sleep(1)
           
        '''3 Column page verification'''
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        verify_total_column_panel_name(['Panel 1', 'Panel 2', 'Category Sales'], 'Step 15.2: Verify 3 Column page.')
        time.sleep(1)

        """ Step 16: Click Sign Out
                     Sign in as Domain Basic user
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Sign Out')
        utillobj.login_wf('mrid01', 'mrpass01')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        portal_canvas.verify_page_in_navigation_bar('2 Column', "Step 16: Verify '2 Column' page in navigation bar and pages are ordered.", page_order_list=['2 Column', '3 Column'])
        
        '''2 Column page verification'''
        portal_canvas.select_page_in_navigation_bar('2 Column')
        time.sleep(2)
        verify_total_column_panel_name(['Panel 1', 'Panel 2'], 'Step 16.1: Verify 2 Column page.')
        time.sleep(1)
           
        '''3 Column page verification'''
        portal_canvas.select_page_in_navigation_bar('3 Column')
        time.sleep(2)
        verify_total_column_panel_name(['Panel 1', 'Panel 2', 'Category Sales'], 'Step 16.2: Verify 3 Column page.')
        time.sleep(1)
        
        """ Step 17: Close and Sign Out.
                     Sign back in as WF Developer
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 45)
        utillobj.infoassist_api_logout()
        utillobj.login_wf('mrid03', 'mrpass03')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 45)
        
        """ Step 18: In the banner link, click on the top right username > Click Sign Out.
        """
        wf_mainpage_obj.signout_from_username_dropdown_menu()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()