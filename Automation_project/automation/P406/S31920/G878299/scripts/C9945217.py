"""-------------------------------------------------------------------------------------------
Author Name : Vishnu priya 
Automated On : 29 April 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools import designer_portal, wf_mainpage
import time

class C9945217_TestClass(BaseTestCase):
    
    def test_C9945217(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        portal_obj = designer_portal.Portal(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        edit_portal_css = ".ibx-title-bar-caption .ibx-label-text"
        
        """
        TEST CASE VARIABLES
        """
        shortcut_report = 'V5_Portal_Context - Shortcut'
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login('mriddev','mrpassdev')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' > 'P406_S31920' Workspace > Click on 'G878309' folder from the resource tree > Click on 'Shortcut Testing'
        """
        HomePage.Workspaces.ResourcesTree.select('P406_S31920->G878309->Shortcut Testing')
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04 = """
            STEP 04 : Click on 'Other' category button > Click on 'Shortcut' action tile
        """
        HomePage.Workspaces.ActionBar.select_tab('OTHER')
        HomePage.Workspaces.ContentArea.delete_file_if_exists(shortcut_report)
        HomePage.Workspaces.ActionBar.select_tab_option('Shortcut')
        HomePage.ModalDailogs.Shortcut.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_05 = """
            STEP 05 : Click the 'Browse' button
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.BrowseButton.click()
        HomePage.ModalDailogs.Resources.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_06 = """
            STEP 06 : Click on > (carot symbol) next to 'P406_S31920' > Click on 'G784912' folder > 
            Double click on 'Portal/Pages' folder
        """
        HomePage.ModalDailogs.Resources.NavigationBar.BreadCrumb.click_arrow('P406_S31920')
        HomePage.ContextMenu.select('G784912')
        time.sleep(3)
        HomePage.ModalDailogs.Resources.GridView.Folders.double_click('Portal/Pages')
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_07 = """
            STEP 07 : 'Click on 'V5_portal_Context''
        """
        HomePage.ModalDailogs.Resources.GridView.Folders.click('V5_Portal_Context')
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_07_01 = """
        Verify the 'Title' = 'V5portal_Context' and 'Name' = 'V5_portal_Context'
        """
        HomePage.ModalDailogs.Resources.Title.verify_text('V5_Portal_Context','07.01')
        HomePage.ModalDailogs.Resources.Name.verify_text('V5_Portal_Context', '07.02')
        HomePage.Home._utils.capture_screenshot('07.01', STEP_07_01,expected_image_verify=True)
        
        STEP_08 = """
        Click on the 'Select' button
        """
        HomePage.ModalDailogs.Resources.SelectButton.click()
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """
        Target path = 'IBFS:/WFC/Repository/P406_S31920/G784912/Portal/Pages/V5_Portal_Context'
        Title = V5_Portal_Context - Shortcut
        Summary should be empty
        Both 'Cancel' and 'OK' buttons get enabled
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.verify_text('IBFS:/WFC/Repository/P406_S31920/G784912/Portal_Pages/V5_Portal_Context','08.01')
        HomePage.ModalDailogs.Shortcut.Title.verify_text('V5_Portal_Context - Shortcut','08.02')
        HomePage.ModalDailogs.Shortcut.Summary.verify_text('','08.03')
        HomePage.ModalDailogs.Shortcut.CancelButton.verify_enabled('08.04')
        HomePage.ModalDailogs.Shortcut.OKButton.verify_enabled('08.05')
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01,expected_image_verify=True)
        
        STEP_09 ="""
        Click OK button
        """
        HomePage.ModalDailogs.Shortcut.OKButton.click()
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_09_01 = """
        Verify that shortcut for an item (V5_Portal_Context - Shortcut) is being created properly
        and showing in the content area and the correct shortcut icon is showing as expected
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_files(['V5_Portal_Context - Shortcut'],'09.01')
        HomePage.Home._utils.capture_screenshot('09.01', STEP_09_01,expected_image_verify=True)
        
        STEP_10 = """
        Edit 'V5_Portal_Context - Shortcut'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('V5_Portal_Context - Shortcut')
        HomePage.ContextMenu.select('Edit')
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        
        STEP_10_01 = """
        Verify that 'V5_Portal_Context - Shortcut' restore without any error
        """
        HomePage.Home._utils.synchronize_with_visble_text(edit_portal_css, 'Edit Portal', main_page_obj.home_page_short_timesleep)
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value='V5_Portal_Context', step_number='10.01')
        portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value='V5_Portal_Context', step_number='10.02')
        portal_obj.alias_textbox_in_new_or_edit_portal_dialog(verify_value='', step_number='10.03')
        portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle='check', step_number='10.04')
        portal_obj.show_portal_title_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='check', step_number='10.05')
        #portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_value='', verify_placeholder_value='Not Selected', current_mode='disable', step_number='10.06')
        portal_obj.logo_browse_button_in_new_or_edit_portal_dialog(button_location=True, step_number='10.07')
        portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', step_number='10.08')
        portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='10.09')
        portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='10.10')
        portal_obj.show_top_navigation_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='uncheck', current_mode='disable', step_number='10.11')
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_value='',step_number='10.12')
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog( verify_placeholder_value="100%",step_number='10.13')
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(current_mode='enable',step_number='10.14')
        portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Designer 2018', step_number='10.15')
        portal_obj.save_button_inside_new_or_edit_portal_dialog(verify_button='Save', current_mode='disable', step_number='10.17')
        portal_obj.cancel_button_inside_new_or_edit_portal_dialog(verify_button='Cancel', current_mode='enable', step_number='10.18')
        
        HomePage.Home._utils.capture_screenshot('10.01', STEP_10_01,expected_image_verify=True)
        
        STEP_11 = """
        Click X to close Edit Portal dialog
        """
        portal_obj.cancel_button_inside_new_or_edit_portal_dialog(select_button=True)
        HomePage.Home._utils.capture_screenshot('11.00', STEP_11)
        
        STEP_12 = """
        Right-click on 'V5_Portal_Context - Shortcut' item > Click on 'Run'
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file('V5_Portal_Context - Shortcut')
        HomePage.ContextMenu.select('Run')
        HomePage.Home._utils.capture_screenshot('12.00', STEP_12)
        
        STEP_12_01 = """
        Verify that 'V5_Portal_Context - Shortcut' run successfully without any error
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.verify_current_tab_name("V5_Portal_Context",'Step 12.01  Verify that "V5_Portal_Context - Shortcut" run successfully without any error')
        HomePage.Home._utils.capture_screenshot('12.01', STEP_12_01)
        
        STEP_13 = """
        Right-click on 'V5_Portal_Context - Shortcut' item > Click on 'Delete'
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.delete_file('V5_Portal_Context - Shortcut')
        HomePage.Home._utils.capture_screenshot('13.00', STEP_13)
        
        STEP_13_01 = """
        Verify that 'V5_Portal_Context - Shortcut'' item gets deleted
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_files('V5_Portal_Context - Shortcut','13.01','asnotin')
        HomePage.Home._utils.capture_screenshot('13.01', STEP_13_01 ,expected_image_verify=True)
        
        STEP_14 = """
            STEP 14 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('14.00', STEP_14)
        
        