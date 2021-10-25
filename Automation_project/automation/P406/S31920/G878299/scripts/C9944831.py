"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 6th April 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944831_TestClass(BaseTestCase):
    
    def test_C9944831(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Long_title = "Arc - Sales by Region and Arc - Sales by Region1 and Arc - Sales by Region2 and Arc - Sales by Region3"
        
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
        Expand the 'Workspaces' > 'P406_S31920' Workspace > Click on 'G878309' folder from the resource tree > 
        Click on 'Shortcut Testing'
        """
        HomePage.Workspaces.ResourcesTree.select("Workspaces->P406_S31920->G878309->Shortcut Testing")
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04="""Click on 'Other' category button > Click on 'Shortcut' action tile
        """
        HomePage.Workspaces.ContentArea.delete_file_if_exists(Long_title)
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Shortcut")
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
 
        STEP_05 = """
        Click on the 'Browse' button
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.BrowseButton.click()
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_06 = """
        Click on 'Workspaces' from the breadcrumb trail
        """
        HomePage.ModalDailogs.Resources.NavigationBar.BreadCrumb.select_workspaces()
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_07 = """
        Double click on 'Retail Samples' > 'Charts' > Click on 'Arc - Sales by Region'
        """
        HomePage.ModalDailogs.Resources.GridView.Folders.double_click('Retail Samples')
        HomePage.ModalDailogs.Resources.GridView.Folders.double_click('Charts')
        HomePage.ModalDailogs.Resources.GridView.Files.click('Arc - Sales by Region')
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
    
        STEP_07_01  = """
        Verify that 'Title' should be 'Arc - Sales by Region' and 'Name' should be 'Sales_by_Region_Arc.fex'
        """
        HomePage.ModalDailogs.Resources.Title.verify_text("Arc - Sales by Region",'07.01')
        HomePage.ModalDailogs.Resources.Name.verify_text("Sales_by_Region_Arc.fex",'07.02')
        HomePage.Home._utils.capture_screenshot('07.01', STEP_07_01,expected_image_verify=True)
        
        STEP_08 = """
        Click 'Select'
        """
        HomePage.ModalDailogs.Resources.SelectButton.click()
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
         
        STEP_08_01 ="""
        Verify the following:
        Target path = IBFS:WFC/Repository/Retail_Samples/Char...
        Title - Arc -Sales by Region - Shortcut
        Summary should be empty
        Both 'Cancel' and 'OK' buttons gets enabled
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.verify_text("IBFS:/WFC/Repository/Retail_Samples/Charts/Sales_by_Region_Arc.fex",'08.01')
        HomePage.ModalDailogs.Shortcut.Title.verify_text('Arc - Sales by Region - Shortcut', '08.02')
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08_01,expected_image_verify=True)
        
        STEP_09 = """
        Enter the title as 'Arc - Sales by Region and Arc - Sales by Region1 and Arc - Sales by Region2 and Arc - Sales by Region3'
        """
        HomePage.ModalDailogs.Shortcut.Title.enter_text(Long_title)
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_10 = """
        Click OK
        """
        HomePage.ModalDailogs.Shortcut.OKButton.click()
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        
        STEP_10_01 = """
        Verify that Arc - Sales by Region and Arc - Sales by Region1 and Arc - Sales by Region2 and Arc - Sales by Region3 - Shortcut created with the shortcut in the thumbnail
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_files([Long_title],'10.01')
        HomePage.Home._utils.capture_screenshot('10.01', STEP_10_01,expected_image_verify=True)
        
        STEP_11 = """
        Right-click on 'Arc - Sales by Region and Arc - Sales by Region1 and Arc - Sales by Region2 and Arc - Sales by Region3 - Shortcut' > Click 'Delete'
        """
        HomePage.Workspaces.ContentArea.delete_file(Long_title)
        HomePage.Home._utils.capture_screenshot('11.00', STEP_11)
        
        STEP_11_01 = """
        Verify 'Arc - Sales by Region and Arc - Sales by Region1 and Arc - Sales by Region2 and Arc - Sales by Region3 - Shortcut' gets deleted
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_files([Long_title],'11.01',assert_type='asnotin')
        HomePage.Home._utils.capture_screenshot('11.00', STEP_11_01,expected_image_verify=True)
              
        STEP_12 = """
            STEP 12 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('12.00', STEP_12)