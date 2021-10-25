"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 08-October-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928099_TestClass(BaseTestCase):
    
    def test_C9928099(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        folder_path = "P406_S31920->G875202"
        portal_name = "v5-alias-test1"
        base_url = HomePage.Home._utils.get_setup_url().replace("home8206", "")
        portal_url = base_url + "portal/P406_S31920/G875202/" + portal_name
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' tab and Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' > 'P406_S31920' Workspace > Click on 'G875202' folder from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select(folder_path)
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click the 'Application' category button and click on 'Portal' action tile
        """
        HomePage.Workspaces.ActionBar.select_tab("APPLICATION")
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(portal_name) #Delete portal if already exits.
        HomePage.Workspaces.ActionBar.select_tab_option("Portal")
        HomePage.ModalDailogs.V5Portal.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Enter 'v5-alias-test1' in Title text box.
        """
        HomePage.ModalDailogs.V5Portal.Title.enter_text(portal_name)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Check the 'Title, Name' text box and Check the 'URL' text box.
        """
        HomePage.ModalDailogs.V5Portal.Title.verify_text(portal_name, "05.01")
        HomePage.ModalDailogs.V5Portal.Name.verify_text(portal_name, "05.02")
        HomePage.ModalDailogs.V5Portal.URL.verify_text(portal_url, "05.03")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on 'Theme' dropdown and Select 'Midnight' theme.
        """
        HomePage.ModalDailogs.V5Portal.Theme.click()
        HomePage.ContextMenu.select("Midnight")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Click 'Create' button.
        """
        HomePage.ModalDailogs.V5Portal.CreateButton.click()
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, portal_name, 60)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : 'v5-alias-test1' portal folder is created under 'P292_S19901' Workspaces> 'G520448' folder in content tree;
            Portal is unpublished, title appears in Italic in content tree.
        """
        HomePage.Workspaces.ResourcesTree.verify_unpublished_items([portal_name], "07.01", assert_type="asin", parent_folder=folder_path)
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Double click 'v5-alias-test1' from Repository tree.
        """
        HomePage.Workspaces.ResourcesTree.double_click(folder_path + "->" + portal_name)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Check the 'My Content' folder does not appear.
        """
        HomePage.Workspaces.ResourcesTree.verify_items([], "08.01", assert_type="asequal", parent_folder=folder_path + "->" + portal_name)
        HomePage.Workspaces.ContentArea.verify_folders([], "08.02", assert_type="asequal")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)