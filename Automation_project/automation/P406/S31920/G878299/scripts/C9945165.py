"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 09 April 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9945165_TestClass(BaseTestCase):
    
    def test_C9945165(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VARIABLES
        """
        chart = 'Arc - Sales by Region'
        shortcut_chart = 'Arc - Sales by Region - Shortcut'
        
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
        HomePage.Workspaces.ContentArea.delete_file_if_exists(shortcut_chart)
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
            STEP 06 : Click on 'Workspaces' from the breadcrumb trail
        """
        HomePage.ModalDailogs.Resources.NavigationBar.BreadCrumb.select_workspaces()
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_07 = """
            STEP 07 : Double click on 'Retail Samples' > 'Charts' > Click on 'Arc - Sales by Region'
        """
        HomePage.ModalDailogs.Resources.GridView.Folders.double_click('Retail Samples->Charts')
        HomePage.ModalDailogs.Resources.GridView.Files.click(chart)
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify that 'Title' should be 'Arc - Sales by Region' and 'Name' should be 'Sales_by_Region_Arc.fex
        """
        HomePage.ModalDailogs.Resources.Title.verify_text(chart, '07.01')
        HomePage.ModalDailogs.Resources.Name.verify_text('Sales_by_Region_Arc.fex', '07.02')
        HomePage.Home._utils.capture_screenshot('07.01', STEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : Click 'Select'
        """
        HomePage.ModalDailogs.Resources.SelectButton.click()
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : Verify the following:
            1.Target path = IBFS:WFC/Repository/Retail_Samples/Char...
            2.Title - Arc -Sales by Region - Shortcut
            3.Summary should be empty
            4.Both 'Cancel' and 'OK' buttons gets enabled
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.verify_text('IBFS:/WFC/Repository/Retail_Samples/Charts/Sales_by_Region_Arc.fex', '08.01')
        HomePage.ModalDailogs.Shortcut.Title.verify_text('Arc - Sales by Region - Shortcut', '08.02')
        HomePage.ModalDailogs.Shortcut.Summary.verify_text('', '08.03')
        HomePage.ModalDailogs.Shortcut.OKButton.verify_enabled('08.04')
        HomePage.ModalDailogs.Shortcut.CancelButton.verify_enabled('08.05')
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01, True)
        
        STEP_09 = """
            STEP 08 : Click on 'Summary' enter the following:
        """
        l1 = "Login to WF admin/admin\n"
        l2 = "Form Retail Sample folder click on shortcut\n"
        l3 = "click on browse and select charts folder then click on select to close the dialog\n"
        l4 = "From Shortcut dialog enter long Summary and click on ok then\n"
        l5 = "Verify short cut with long summary is showing properly in the content area\n"
        l6 = "Verify shortcut icon and summary will display"
        summary = l1 + l2 + l3 + l4 + l5 + l6
        HomePage.ModalDailogs.Shortcut.Summary.enter_text(summary)
        HomePage.Home._utils.wait_for_page_loads(10, pause_time=8)
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_09_01 = """
            STEP 09.01 : Verify that 'Summary' text box filled up with a long title 
            and it shows a vertical bar to scroll up
        """
        summary_object = HomePage.ModalDailogs.Shortcut.Summary._object
        vertical_scrollbar = HomePage.Home._javascript.check_element_has_vertical_scrollbar(summary_object)
        HomePage.Home._utils.asequal(vertical_scrollbar, True, "Step 09.01 : Verify summary textbox has vertical scollbar")
        HomePage.ModalDailogs.Shortcut.Summary.verify_text(summary, '09.02')
        HomePage.Home._utils.capture_screenshot('09.01', STEP_09_01, True)
        
        STEP_10 = """
            STEP 10 : Right-click on 'Reports - Shortcut' folder > Click on 'Delete
        """
        HomePage.ModalDailogs.Shortcut.OKButton.click()
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, shortcut_chart, 60)
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        
        STEP_10_01 = """
            STEP 10.01 : Verify that Arc -Sales by Region - Shortcut created with the shortcut in the thumbnail
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_files([shortcut_chart], '10.01')
        HomePage.Home._utils.capture_screenshot('10.01', STEP_10_01, True)
        
        STEP_11 = """
            STEP 11 : Hover over the mouse on 'Arc -Sales by Region - Shortcut'
            STEP 11.01 : Verify it shows the summary in the thumbnail
        """
        HomePage.Workspaces.ContentArea.verify_file_summary(shortcut_chart, summary, '11.01')
        HomePage.Home._utils.capture_screenshot('11.01', STEP_11, True)
        
        STEP_12 = """
            STEP 12 : Right-click on 'Arc -Sales by Region - Shortcut' > Click 'Delete'
        """
        HomePage.Workspaces.ContentArea.delete_file(shortcut_chart)
        HomePage.Home._utils.capture_screenshot('12.00', STEP_12)
        
        STEP_12_01 = """
            STEP 09.01 : Verify that 'Reports - Shortcut' folder get deleted
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_files([shortcut_chart], '12.01', 'asnotin')
        HomePage.Home._utils.capture_screenshot('12.01', STEP_12_01, True)
        
        STEP_13 = """
            STEP 13 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('13.00', STEP_13)