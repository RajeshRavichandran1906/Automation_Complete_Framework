"""-------------------------------------------------------------------------------------------
Author Name  : AH14645
Automated On : 21-October-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928113_TestClass(BaseTestCase):
    
    def test_C9928113(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        
        portal_name_1 = "v5-mypages-test1"
        portal_name_2 = "v5-alias-test2"
        User_CSS = "div.hpreboot-top-bar [title ='User']"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Advanced User
        """
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view and Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' > 'P406_S31920' Workspace > Click on 'G875202' folder from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G875202")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify 'v5-mypages-test1' and 'v5-alias-test2' portals are published.
        """
        published_file_object_1 = HomePage.Workspaces.ContentArea._get_file_object_(portal_name_1).value_of_css_property('border-top-style')
        published_file_object_2 = HomePage.Workspaces.ContentArea._get_file_object_(portal_name_2).value_of_css_property('border-top-style')
        published_files = all([published_file_object_1=='solid', published_file_object_2=='solid'])
        HomePage.Home._utils.asequal(True, published_files, "Step03.01: Verify 'v5-mypages-test1' and 'v5-alias-test2' portals are published.")
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Right click on 'v5-mypages-test1' portal
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(portal_name_1)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify user can see Run option, edit doesn't appear.
        """
        HomePage.Home._utils.synchronize_until_element_is_visible(HomePage.ContextMenu._root_css_, 5)
        HomePage.ContextMenu.verify(['Run'], "04.01", assert_type='asin')
        HomePage.ContextMenu.verify(['Edit'], "04.02", assert_type='asnotin')
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Right click on 'v5-alias-test2' portal
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(portal_name_2)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify user can see Run option, edit doesn't appear.
        """
        HomePage.Home._utils.synchronize_until_element_is_visible(HomePage.ContextMenu._root_css_, 5)
        HomePage.ContextMenu.verify(['Run'], "05.01", assert_type='asin')
        HomePage.ContextMenu.verify(['Edit'], "05.02", assert_type='asnotin')
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.synchronize_until_element_is_visible(User_CSS, 30)
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Sign into WebFOCUS Home Page as Basic User
        """
        HomePage.invoke_with_login("mridbas", "mrpassbas")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click on 'Workspaces' view and Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Expand the 'Workspaces' > 'P406_S31920' Workspace > Click on 'G875202' folder from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G875202")
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify 'v5-mypages-test1' and 'v5-alias-test2' portals are published.
        """
        published_file_object_1 = HomePage.Workspaces.ContentArea._get_file_object_(portal_name_1).value_of_css_property('border-top-style')
        published_file_object_2 = HomePage.Workspaces.ContentArea._get_file_object_(portal_name_2).value_of_css_property('border-top-style')
        published_files = all([published_file_object_1=='solid', published_file_object_2=='solid'])
        HomePage.Home._utils.asequal(True, published_files, "Step09.01: Verify 'v5-mypages-test1' and 'v5-alias-test2' portals are published.")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Right click on 'v5-mypages-test1' portal
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(portal_name_1)
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify user can see Run option, edit doesn't appear.
        """
        HomePage.Home._utils.synchronize_until_element_is_visible(HomePage.ContextMenu._root_css_, 5)
        HomePage.ContextMenu.verify(['Run'], "10.01", assert_type='asin')
        HomePage.ContextMenu.verify(['Edit'], "10.02", assert_type='asnotin')
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Right click on 'v5-alias-test2' portal
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(portal_name_2)
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify user can see Run option, edit doesn't appear.
        """
        HomePage.Home._utils.synchronize_until_element_is_visible(HomePage.ContextMenu._root_css_, 5)
        HomePage.ContextMenu.verify(['Run'], "11.01", assert_type='asin')
        HomePage.ContextMenu.verify(['Edit'], "11.02", assert_type='asnotin')
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.synchronize_until_element_is_visible(User_CSS, 30)
        HomePage.Home._utils.capture_screenshot("12", STEP_12)