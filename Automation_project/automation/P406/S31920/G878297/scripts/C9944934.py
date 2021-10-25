"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 2nd March 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944934_TestClass(BaseTestCase):
    
    def test_C9944934(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
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
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
        Expand the 'Workspaces' > 'P406_S31920' Workspace > Click on 'G878309' folder from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Workspaces->P406_S31920->G878309")
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04="""Click on 'Other' category button > Click on 'URL' action tile
        """
        HomePage.Workspaces.ContentArea.delete_file_if_exists('Testing URL Action Tile')
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("URL")
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
 
        Step_04_01 = """Verify the following in the 'New URL' dialog box
        Cursor should be in the Title area by default.
        Title text box gets highlighted with the blue border
        Name, Summary and URL text boxes are not highlighted
        Cancel button gets enabled and the OK button gets disabled
        """
        HomePage.ModalDailogs.URL.Title.verify_border_color('malibu', '04.01')
        HomePage.ModalDailogs.URL.Name.verify_border_color('gray80', '04.02')
        HomePage.ModalDailogs.URL.Summary.verify_border_color('gray80', '04.02')
        HomePage.ModalDailogs.URL.URL.verify_border_color('gray80', '04.02')
        HomePage.ModalDailogs.URL.CancelButton.verify_enabled("04.04")
        HomePage.ModalDailogs.URL.OKButton.verify_disabled("04.05")
        HomePage.Home._utils.capture_screenshot('04.01', Step_04_01)

        Step_05 = """Enter 'Testing URL Action Tile' in the Title entry box
        """
        HomePage.ModalDailogs.URL.Title.enter_text('Testing URL Action Tile')
        HomePage.Home._utils.capture_screenshot('05.00', Step_05)

        Step_05_01="""Verify that entering text in the 'Title' entry box gets reflected in the 'Name' entry box as 'Testing_URL_Action_Tile'
        """
        HomePage.ModalDailogs.URL.Name.verify_text("Testing_URL_Action_Tile",'05.01')
        HomePage.Home._utils.capture_screenshot('05.01', Step_05_01)
        
        Step_06 = """Click in the 'URL' entry box
        """
        HomePage.ModalDailogs.URL.URL.click()
        HomePage.Home._utils.capture_screenshot('06.00', Step_06)
        
        Step_07 = """Enter URL as 'http://www.informationbuilders.com'
        """
        HomePage.ModalDailogs.URL.URL.enter_text('http://www.informationbuilders.com')
        HomePage.Home._utils.capture_screenshot('07.00', Step_07)
        
        Step_08 = """Click the 'Cancel' button
        """
        HomePage.ModalDailogs.URL.CancelButton.click()
        HomePage.Home._utils.capture_screenshot('08.00', Step_08)
        
        Step_08_01 = """
        Verify that the 'Testing URL Action Tile' URL is not displayed in the content area
        """
        HomePage.Workspaces.ContentArea.verify_files('Testing URL Action Tile', step_num="08.01", assert_type='asnotin')
        HomePage.Home._utils.capture_screenshot('08.01', Step_08_01)
        
        Step_09 = """Again Click on 'URL' action bar > Enter 'Testing URL Action Tile' in the Title entry box >Click in the 'URL' entry box > Enter URL as 'http://www.informationbuilders.com'
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("URL")
        HomePage.ModalDailogs.URL.wait_for_appear()
        HomePage.ModalDailogs.URL.Title.enter_text('Testing URL Action Tile')
        HomePage.ModalDailogs.URL.URL.click()
        HomePage.ModalDailogs.URL.URL.enter_text("http://www.informationbuilders.com")
        HomePage.Home._utils.capture_screenshot('09.00', Step_09)
        
        Step_10 = """Click the 'OK' button
        Verify that the 'Testing URL Action Tile' URL is displayed in the content area
        """
        HomePage.ModalDailogs.URL.OKButton.click()
        HomePage.ModalDailogs.URL.wait_for_diappear()
        HomePage.Workspaces.ContentArea.verify_files(['Testing URL Action Tile'], step_num="10.01")
        HomePage.Home._utils.capture_screenshot('10.00', Step_10)
        
        Step_11 = """Right Click on 'Testing URL Action Tile' URL > Select 'View'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Testing URL Action Tile')
        HomePage.ContextMenu.select("View")
        HomePage.Home._utils.capture_screenshot('11.00', Step_11)
        
        
        Step_11_01 = """Verify 'Testing URL Action Tile' URL opens in a preview window and it displayed 'www.informationbuilders.com refused to connect'
        Note: Some URLs may not be able to run in an iFrame
        """
        HomePage.Home._utils.verify_element_text(".output-area-titlebar .output-area-label",'Testing URL Action Tile',msg = "Step:11.01")
        HomePage.Home._utils.capture_screenshot('11.01', Step_11_01)
        
        Step_12 = """Click 'X' to close 'Testing URL Action Tile' URL preview window
        """
        output_area_close_button = HomePage.Home._utils.validate_and_get_webdriver_object("div.output-area-close-button",'CLose_button')
        output_area_close_button.click()
        HomePage.Home._utils.capture_screenshot('12.01', Step_12)

        Step_13 = """Right Click on 'Testing URL Action Tile' URL > Select 'View'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Testing URL Action Tile')
        HomePage.ContextMenu.select("View")
        HomePage.Home._utils.capture_screenshot('13.00', Step_13)

        Step_14 = """Click on 'Open in new window' button
        """
        open_new_window = HomePage.Home._utils.validate_and_get_webdriver_object('div.output-area-popout-button',"open in new window")
        open_new_window.click()
        HomePage.Home._utils.capture_screenshot('14.00', Step_14)
        
        Step_14_01 = """
        Verify 'Information Builders' site opens in a new window without any issues
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.verify_current_tab_name("Data and Analytics Company | ibi","Step:14.01")
        HomePage.Home._utils.capture_screenshot('14.01', Step_14_01)

        Step_15 = """Close the 'Testing URL Action Tile' URL window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot('15.00', Step_15)

        Step_16 = """Right Click on 'Testing URL Action Tile' URL > Select 'View in new window'
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file('Testing URL Action Tile')
        HomePage.ContextMenu.select("View in new window")
        HomePage.Home._utils.capture_screenshot('16.00', Step_16)
        
        Step_16_01 = """ Verify 'Information Builders' site opens in a new window without any issues
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.verify_current_tab_name("Data and Analytics Company | ibi","Step:14.01")
        HomePage.Home._utils.capture_screenshot('16.01', Step_16_01)
        
        Step_17 = """Close the 'Testing URL Action Tile' URL window
        """
        
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot('17.00', Step_17)
        
        Step_18= """Right click on 'Testing URL Action Tile' > Delete > Ok
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.delete_file('Testing URL Action Tile')
        HomePage.Home._utils.capture_screenshot('18.00', Step_18)
        
        STEP_19 = """
            STEP 19 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('19.00', STEP_19)