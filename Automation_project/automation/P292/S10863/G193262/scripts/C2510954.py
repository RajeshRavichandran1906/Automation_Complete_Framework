"""-------------------------------------------------------------------------------------------
Created on September 23, 2019
@author: Niranjan

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/2510954
Test Case Title =  Verify Insight icon appears in Grid and List Views
-----------------------------------------------------------------------------------------------"""

import unittest
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
import time

class C2510954_TestClass(BaseTestCase):

    def test_C2510954(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        locator = WfMainPageLocators()
        core_utils = CoreUtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        chart_css = "#pfjTableChart_1"
        querytree_css = "#queryTreeColumn"
        
        Step1 = """
            STEP 01 : Sign in to WebFOCUS as Developer user.
        """
        login.invoke_home_page("mrid", "mrpass")
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", main_page.home_page_long_timesleep)
        utils.capture_screenshot("01.01", Step1)
        
        Step2 = """
            STEP 02 : Click on Content tree from side bar.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        utils.capture_screenshot("02.01", Step2)
        
        Step3 = """
            STEP 03 : Launch the IA API with chart in edit mode under P292_S10863 >> G193260 (edit the domain, port and alias of the URL - do not use the URL as is)
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10863%2FG193260&tool=chart&master=ibisamp/car
        """
        node = core_utils.parseinitfile('nodeid')
        port = core_utils.parseinitfile('httpport')
        context = core_utils.parseinitfile('wfcontext')
        setup_url = 'http://' + node + ':' + port + context
        project = utils.parseinitfile('project_id')
        suite = utils.parseinitfile('suite_id')
        group_id=utils.parseinitfile('group_id')
        folder = project + '_' + suite + '/' + group_id
        tool = "chart"
        master = "ibisamp/car"
        api_url = setup_url + '/ia?tool=' + tool + '&master=' + master + '&item=IBFS%3A%2FWFC%2FRepository%2F' + folder
        self.driver.get(api_url)
        chart.wait_for_visible_text(chart_css, "Group 0")
        utils.capture_screenshot("03.01", Step3, expected_image_verify = True)
        
        Step4 = """
            STEP 04 : Double click "SALES" under Measures and double click "COUNTRY" under Dimensions.
            Verify "SALES" added to Vertical Axis and "COUNTRY" added to Horizontal axis
        """
        chart.double_click_on_datetree_item("SALES", 1)
        chart.wait_for_visible_text(querytree_css, "SALES")
        
        chart.double_click_on_datetree_item("COUNTRY", 1)
        chart.wait_for_visible_text(querytree_css, "COUNTRY")
        
        chart.verify_all_fields_in_query_pane(['Chart (car)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'SALES', 'Horizontal Axis', 'COUNTRY', 'Marker', 'Color', 'Size', 'Tooltip', 'Multi-graph', 'Animate'], "Step 04.01 : Verify 'SALES' added to Vertical Axis and 'COUNTRY' added to Horizontal axis")
        utils.capture_screenshot("04.01", Step4, expected_image_verify = True)
        
        Step5 = """
            STEP 05 : Click Format tab -> Click on "Run with" option -> Click on Insight in ribbon.
        """
        chart.select_ia_ribbon_item("Format", "run_with")
        chart.select_ia_ribbon_item("Format", "insight")
        utils.capture_screenshot("05.01", Step5)
        
        Step6 = """
            STEP 06 : Click "Create Thumbnail" option in toolbar and click OK.
        """
        chart.select_item_in_top_toolbar("thumbnail")
        chart.wait_for_visible_text("#qbThumbNailDlgCancelBtn", "Cancel")
        
        ok_button_obj = utils.validate_and_get_webdriver_object("#qbThumbNailDlgOkBtn", "OK button css")
        core_utils.python_left_click(ok_button_obj)
        time.sleep(15)
        utils.capture_screenshot("06.01", Step6)
        
        Step7 = """
            STEP 07 : Click Save in toolbar and enter 'Insight1' and click Save.
        """
        chart.select_item_in_top_toolbar('save')
        chart.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")
        
        chart.save_file_in_save_dialog("Insight1")
        utils.synchronize_until_element_disappear("#IbfsOpenFileDialog7_btnCancel", 15)
        utils.capture_screenshot("07.01", Step7)
        
        Step8 = """
            STEP 08 : Click the Application menu and click Exit.
        """
        chart.api_logout()
        login.invoke_home_page("mrid", "mrpass")
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", main_page.home_page_long_timesleep)
        
        main_page.expand_repository_folder("P292_S10863->G193260")
        chart.wait_for_visible_text("div.files-box-files", "Insight1")
        utils.capture_screenshot("08.01", Step8)
        
        Step9 = """
            STEP 09 : Right click on 'Insight1' and select Publish.
            Verify Insight icon (hand) and Insight chart thumbnail appear in Grid View:
        """
        main_page.right_click_folder_item_and_select_menu("Insight1", "Publish")
        time.sleep(15)
        utils.verify_picture_using_sikuli("C2510954_step9.png", "Step 09.01 : Verify Insight icon (hand) and Insight chart thumbnail appear in Grid View:")
        utils.capture_screenshot("09.01", Step9)
        
        Step10 = """
            STEP 10 : Click toggle button to switch to List View.
            Verify Insight icon (hand) appears in List View:
        """
        main_page.select_list_view()
        chart.wait_for_visible_text("div.files-listing", "Insight1")
        utils.verify_picture_using_sikuli("C2510954_step10.png", "Step 10.01 : Verify Insight icon (hand) appears in List View:")
        utils.capture_screenshot("10.01", Step10, expected_image_verify = True)
        
        Step11 = """
            STEP 11 : Click toggle button to switch to Grid View
        """
        main_page.select_grid_view()
        chart.wait_for_visible_text("div.files-box-files ", "Insight1")
        utils.capture_screenshot("11.01", Step11)
        
        Step12 = """
            STEP 12 : In the banner link, click on the top right username > Click Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
        utils.capture_screenshot("12.01", Step12)
        
        
if __name__ == '__main__':
    unittest.main()