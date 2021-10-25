"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 31th March 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944937_TestClass(BaseTestCase):
    
    def test_C9944937(self):
        
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
        HomePage.Workspaces.ResourcesTree.select("Workspaces->P406_S31920")
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04 = """
        Click on 'G878309' folder from the resource tree > Double click on 'URL Testing' folder from the content area
        """
        HomePage.Workspaces.ResourcesTree.select('G878309')
        HomePage.Workspaces.ContentArea.double_click_on_folder('URL Testing')
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_05 = """
        Click on 'Other' category button > Click on 'URL' action tile
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("URL")
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_06 = """
        Enter 'A234567890B234567890C23456789D23456789E234567890F234567890G234567890H234567890I234567890J' in the Title entry box > Enter URL as 'http://www.informationbuilders.com'
        """
        Title_to_enter = "A234567890B234567890C23456789D23456789E234567890F234567890G234567890H234567890I234567890J"
        HomePage.ModalDailogs.URL.Title.enter_text(Title_to_enter)
        url_addr = "http://www.informationbuilders.com"
        HomePage.ModalDailogs.URL.URL.enter_text(url_addr)
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_06_01 = """
        Verify the following in the 'Create URL' dialog box:
        URL entry box gets highlighted
        Inside the 'Title' entry box 'A234567890B234567890C23456789D23456789E234567890F23456' is available
        Inside the 'Name' entry box 'A234567890B234567890C23456789D23456789E234567890F234...' is available
        Summary entry box should be empty and URL should be 'http://www.informationbuilders.com/'
        'OK' button and the 'Cancel' button gets enabled by default
        """
        HomePage.ModalDailogs.URL.URL.verify_border_color('malibu','06.01')
        HomePage.ModalDailogs.URL.Title.verify_text(Title_to_enter,'05.02')
        Name_entry_box = "A234567890B234567890C23456789D23456789E234567890F234567890G2"
        HomePage.ModalDailogs.URL.Name.verify_text(Name_entry_box,'05.04')
        HomePage.ModalDailogs.URL.Summary.verify_text('','05.05')
        HomePage.ModalDailogs.URL.URL.verify_text('http://www.informationbuilders.com','05.06')
        HomePage.ModalDailogs.URL.OKButton.verify_enabled('05.07')
        HomePage.ModalDailogs.URL.CancelButton.verify_enabled('05.08')
        HomePage.Home._utils.capture_screenshot('06.01', STEP_06_01,expected_image_verify=True)
        
        STEP_07 = """
        Click OK > Right-click on 'A234567890B234567890C23456789D23456789E234567890F234567890G234567890H234567890I234567890J' URL > Click 'View in a new window'
        """
        HomePage.ModalDailogs.URL.OKButton.click()
        HomePage.Workspaces.ContentArea.right_click_on_file(Title_to_enter)
        HomePage.ContextMenu.select('View in new window')
        HomePage.Home._utils.capture_screenshot('07.00',STEP_07)
        
        STEP_07_01 = """
        Verify 'Information Builders' site opens in a new window without any issues and it's URL as 'https://www.informationbuilders.com/'
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.verify_current_tab_name("Data and Analytics Company | ibi","Step:08.01 verify the new window")
        HomePage.Home._utils.capture_screenshot('07.01',STEP_07_01,expected_image_verify=True)
        
        STEP_08 = """
        Right-click on 'A234567890B234567890C23456789D23456789E234567890F234567890G234567890H234567890I234567890J' URL > Click on 'Edit'
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file(Title_to_enter)
        HomePage.ContextMenu.select('Edit')
        HomePage.Home._utils.capture_screenshot('08.00',STEP_08)
        
        STEP_08_01 = """
        Verify the following in the 'Edit URL' dialog box:
        Title entry box gets highlighted
        Inside the 'Title' entry box 'A234567890B234567890C23456789D23456789E234567890F23456' is available
        Name entry box should be in read-only format
        Inside the 'Name' entry box 'A234567890B234567890C23456789D23456789E234567890F234...' is available
        Summary entry box should be empty and URL should be 'http://www.informationbuilders.com/'
        'Update' button is disabled (until user make a change) and the 'Cancel' button is enabled by default
        """
        HomePage.ModalDailogs.URL.Title.verify_border_color('malibu','08.01')
        HomePage.ModalDailogs.URL.Title.verify_text(Title_to_enter,'08.02')
        HomePage.ModalDailogs.URL.Name.verify_disabled('08.03')
        HomePage.ModalDailogs.URL.Name.verify_text(Name_entry_box,'08.04')
        HomePage.ModalDailogs.URL.Summary.verify_text('','08.05')
        HomePage.ModalDailogs.URL.URL.verify_text('http://www.informationbuilders.com','08.06')
        HomePage.ModalDailogs.URL.UpdateButton.verify_disabled('08.07')
        HomePage.ModalDailogs.URL.CancelButton.verify_enabled('08.08')
        HomePage.Home._utils.capture_screenshot('08.01',STEP_08_01,expected_image_verify=True)
        
        STEP_09 = """
        Change URL into 'https://www.google.com/maps/embed?pb&#61;!1m18!1m12!1m3!1d3022.547936322724!2d-73.99435628416859!3d40.74997177932779!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c259ae5c063d57%3A0x6373e9d375b9dd35!2s2+Pennsylvania+Plaza%2C+New+York%2C+NY+10121!5e0!3m2!1sen!2sus!4v1505502221168&quot;width&#61;&quot;600&quot;height&#61;&quot;450&quot;frameborder&#61;&quot;0&quot;style&#61;&quot;border:0&quot;allowfullscreen' > Click 'Update'
        """
        map_link_addr = "https://www.google.com/maps/embed?pb&#61;!1m18!1m12!1m3!1d3022.547936322724!2d-73.99435628416859!3d40.74997177932779!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c259ae5c063d57%3A0x6373e9d375b9dd35!2s2+Pennsylvania+Plaza%2C+New+York%2C+NY+10121!5e0!3m2!1sen!2sus!4v1505502221168&quot;width&#61;&quot;600&quot;height&#61;&quot;450&quot;frameborder&#61;&quot;0&quot;style&#61;&quot;border:0&quot;allowfullscreen"
        HomePage.ModalDailogs.URL.URL.enter_text(map_link_addr)
        HomePage.ModalDailogs.URL.UpdateButton.click()
        HomePage.Home._utils.capture_screenshot('09.00',STEP_09)
        
        STEP_10 = """
        Right-click on 'A234567890B234567890C23456789D23456789E234567890F234567890G234567890H234567890I234567890J' URL > Click on 'View in new window'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(Title_to_enter)
        HomePage.ContextMenu.select('View in new window')
        HomePage.Home._utils.capture_screenshot('10.00',STEP_10)
        
        STEP_10_01 = """
        Verify 'https://www.google.com/maps/embed?pb&#61;!1m18!1m12!1m3!1d3022.547936322724!2d-73.99435628416859!3d40.74997177932779!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c259ae5c063d57%3A0x6373e9d375b9dd35!2s2+Pennsylvania+Plaza%2C+New+York%2C+NY+10121!5e0!3m2!1sen!2sus!4v1505502221168&quot;%20width&#61;&quot;600&quot;%20height&#61;&quot;450&quot;%20frameborder&#61;&quot;0&quot;%20style&#61;&quot;border:0&quot;%20allowfullscreen' URL opens in a new window without any issue
        """
        HomePage.Home._core_utils.switch_to_new_window()
        current_url = self.driver.current_url
        HomePage.Home._utils.asequal(map_link_addr,current_url,"Step :10.01 verify the map opens in new window")
        HomePage.Home._utils.capture_screenshot('10.01',STEP_10_01,expected_image_verify=True)
        
        STEP_11 = """
        Close the URL window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('11.00',STEP_11)
        
        STEP_11_01 = """
        Verify 'A234567890B234567890...' gets displayed in the content area
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.verify_files([Title_to_enter],'11.01')
        HomePage.Home._utils.capture_screenshot('11.01',STEP_11_01,expected_image_verify=True)
        
        STEP_12 = """
        Double-click on 'A234567890B234567890...' URL in the content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(Title_to_enter)
        HomePage.Home._utils.capture_screenshot('12.00',STEP_12)
        
        STEP_12_01 = """
        Verify that 'A234567890B234567890C23456789D23456789E234567890F234567890G234567890H234567890I234567890J' opens without any issue
        """
        output_text = HomePage.Home._utils.validate_and_get_webdriver_object(".output-area-label .ibx-label-text","output_label_text").text
        HomePage.Home._utils.asequal(Title_to_enter,output_text,"Step :12.01 verify the title ")
        HomePage.Home._utils.capture_screenshot('12.01',STEP_12_01,expected_image_verify=True)
        
        STEP_13 = """
        Click 'X' to close the URL window
        """
        close_button = HomePage.Home._utils.validate_and_get_webdriver_object(".output-area-close-button","close_button")
        HomePage.Home._core_utils.python_left_click(close_button)
        HomePage.Home._utils.capture_screenshot('13.00',STEP_13)
        
        STEP_14 = """
        Right-click on 'A234567890B234567890...' URL in the content area > Click 'Delete'
        """
        HomePage.Workspaces.ContentArea.delete_file(Title_to_enter)
        HomePage.Home._utils.capture_screenshot('14.00',STEP_14)
        
        STEP_14_01 = """
        Verify that 'A234567890B234567890...' URL is not available in the content area under 'P406_S31920 > G878309 > URL Testing'
        """
        HomePage.Workspaces.ContentArea.verify_files(Title_to_enter,'14.01',assert_type = 'asnotin')
        HomePage.Home._utils.capture_screenshot('14.01',STEP_14_01,expected_image_verify=True)
        
        STEP_15 = """
            STEP 15 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('15.00', STEP_15)
        