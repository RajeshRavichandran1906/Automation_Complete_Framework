"""----------------------------------------------------
Author Name : Bhagavathi/Joyal
Automated on : 12 Dec 2019
----------------------------------------------------"""
import unittest
from common.wftools.report import Report
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.paris_home_page import ParisHomePage

class C9928161_TestClass(BaseTestCase):
    
    def test_C9928161(self):
        
        """TESTCASE OBJECTS"""
        
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        reporting_object = Report(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """TESTCASE VARIABLES"""
        
        master_dialog_css = "#paneIbfsExplorer_exTree"
        reporting_object_popup_css = "div.window-active"
        reporting_object_css = "#editorViewPane table>tbody>tr"
        
        Step1 = """
        Step 01.Sign into WebFOCUS Home Page as dev User
        """
        HomePage.invoke_with_login('mrdevid', 'mrdevpass')
        utils.capture_screenshot('01.00', Step1)
        
        Step2 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        utils.capture_screenshot('02.00', Step2)
        
        Step3 = """
        Step 03.Expand the 'Workspaces' from the tree and Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.expand("Workspaces")
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        utils.capture_screenshot('03.00', Step3)
        
        Step4 = """
        Step 04.Click on 'Data' category button
        """
        HomePage.Workspaces.ActionBar.select_tab("DATA")
        utils.capture_screenshot('04.00', Step4)
        
        Step5 = """
        Step 05.Click on 'Reporting Object' action bar under 'Data' category
        Verify the Master File Dialog is displayed
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Reporting Object")
        reporting_object.switch_to_new_window()
        reporting_object.wait_for_visible_text(master_dialog_css, 'baseapp', reporting_object.home_page_long_timesleep)
        utils.verify_object_visible(master_dialog_css, True, "Step 05.00: Verify the Master File Dialog is displayed")
        utils.capture_screenshot('05.00', Step5, expected_image_verify= True)
        
        Step6 = """
        Step 06.Select 'wf_retail_lite.mas' > open
        Verify Reporting Object tool opens
        """
        reporting_object.select_masterfile_in_open_dialog('baseapp', 'wf_retail_lite')
        reporting_object.wait_for_visible_text(reporting_object_css, 'Reporting Object')
        reporting_object_element = utils.validate_and_get_webdriver_objects(reporting_object_css, 'Reporting Object')
        reporting_object_items = [x.text for x in reporting_object_element]
        del(reporting_object_items[-1])
        actual_reporting_object_list = reporting_object_items
        expected_reporting_object_list = ['Reporting Object', 'Preprocessing Other', 'Joins', 'Defines', 'Filters', 'Where Statements', 'Report', 'Chart', 'Postprocessing Other']
        utils.asequal(expected_reporting_object_list, actual_reporting_object_list, 'Step 06.00: Verify the Reporting Object is open')
        utils.capture_screenshot('06.00', Step6, expected_image_verify= True)
        
        Step7 = """
        Step 07.Click on RO Globe > Exit > No
        """
        reporting_object.select_visualization_application_menu_item('exit')
        reporting_object.wait_for_visible_text(reporting_object_popup_css, 'No')
        reporting_object.click_any_bibutton_in_dialog(reporting_object_popup_css, 'No')
        core_utils.switch_to_previous_window('False')
        utils.capture_screenshot('07.00', Step7)
        
        Step8 = """
        Step 08.In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('08.00', Step8)
        
if __name__ == '__main__':
    unittest.main()