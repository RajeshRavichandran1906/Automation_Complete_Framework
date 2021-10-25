"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 30th March 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944936_TestClass(BaseTestCase):
    
    def test_C9944936(self):
        
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
        Expand the 'Workspaces' > 'P406_S31920' Workspace
        """
        HomePage.Workspaces.ResourcesTree.select("Workspaces->P406_S31920->G878309")
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04 = """
        Click on 'G878309' folder from the resource tree > Double click on 'URL Testing' folder from the content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder('URL Testing')
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_05 = """
        Right-click on 'Testing Summary' > Click on 'Edit'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Testing Summary')
        HomePage.ContextMenu.select('Edit')
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_05_01 = """
        Verify the following in the 'Edit URL' dialog box:
        Title entry box gets highlighted
        Inside the 'Name' entry box 'Testing_Summary' is available
        Name entry box should be in read-only format
        Inside the 'Name' entry box 'Edit_Testing_URL_Action_tile' is available
        Summary entry box should be empty and URL should be 'http://www.informationbuilders.com/'
        'Update' button is disabled (until user make a change) and the 'Cancel' button is enabled by default
        """
        HomePage.ModalDailogs.URL.Title.verify_border_color('malibu','05.01')
        HomePage.ModalDailogs.URL.Title.verify_text("Testing Summary",'05.02')
        HomePage.ModalDailogs.URL.Name.verify_disabled('05.03')
        HomePage.ModalDailogs.URL.Name.verify_text('Testing_Summary','05.04')
        HomePage.ModalDailogs.URL.Summary.verify_text('','05.05')
        HomePage.ModalDailogs.URL.URL.verify_text('http://www.informationbuilders.com','05.06')
        HomePage.ModalDailogs.URL.UpdateButton.verify_disabled('05.07')
        HomePage.ModalDailogs.URL.CancelButton.verify_enabled('05.08')
        HomePage.Home._utils.capture_screenshot('05.01', STEP_05_01)
        
        STEP_06 = """
        Add 'Testing HOME-409 as there were issues with Edit and adding a summary to a URL item' to the Summary entry box > Click Update
        """
        HomePage.ModalDailogs.URL.Summary.enter_text("Testing HOME-409 as there were issues with Edit and adding a summary to a URL item",)
        HomePage.ModalDailogs.URL.UpdateButton.click()
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_07 = """
        Hover over the mouse to 'Testing Summary' URL
        """
        Expected_summary = 'Testing HOME-409 as there were issues with Edit and adding a summary to a URL item'
        HomePage.Workspaces.ContentArea.verify_file_summary('Testing Summary',Expected_summary,07.00)
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_07_01 = """
        Verify that 'Testing HOME-409 as there were issues with Edit and adding a summary to a URL item' summary appears
        """
        HomePage.Home._utils.capture_screenshot('07.01', STEP_07_01,expected_image_verify=True)
        
        STEP_08 = """
        Right-click on 'Testing Summary' > Click on 'View in new window'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Testing Summary')
        HomePage.ContextMenu.select('View in new window')
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """
        Verify 'Business Intelligence and Data Management Software' site opens in a new window without any issues and it's URL as 'https://www.informationbuilders.com/'
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.verify_current_tab_name("Data and Analytics Company | ibi","Step:08.01 verify the new window")
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01,expected_image_verify=True)
        
        STEP_09 = """
        Close the 'Business Intelligence and Data Management Software' URL window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_10 = """
        Right-click on 'Testing Summary' > Click on 'Edit'
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file('Testing Summary')
        HomePage.ContextMenu.select('Edit')
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        
        STEP_11 = """
        Click on 'Summary' text box > Make it as empty > Click Update
        """
        HomePage.ModalDailogs.URL.Summary.enter_text("")
        HomePage.ModalDailogs.URL.UpdateButton.click()
        HomePage.Home._utils.capture_screenshot('11.00', STEP_11)
        
        STEP_12 = """
        Hover over the mouse to 'Testing Summary' URL
        """
        HomePage.Workspaces.ContentArea.verify_file_summary('Testing Summary',"",07.00)
        HomePage.Home._utils.capture_screenshot('12.00', STEP_12)
        
        STEP_13 = """
            STEP 13 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('13.00', STEP_13)