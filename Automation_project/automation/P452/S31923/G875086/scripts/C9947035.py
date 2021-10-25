"""-------------------------------------------------------------------------------------------
Author Name  : BM13368
Automated On : 21-December-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage
from common.wftools.paris_home_page import ParisHomePage

class C9947035_TestClass(BaseTestCase):
    
    def test_C9947035(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Designer = DesignerPage()
        
        """
        TEST CASE VAIABLES
        """
        
        STEP_01 = """
            STEP 01 : Launch WF Designer to create a new visualization as domain developer:
    
            http://machine.ibi.com:port/alias/designer?&master=ibisamp/car&item=IBFS:/WFC/Repository/P452_S31923/G875086&tool=framework&startlocation=IBFS:/WFC/Repository
        """
        Designer.API.invoke_new_visualization(credential_keys=('mriddev', 'mrpassdev'), workspace_folder="P452_S31923/G875086",master_file='ibisamp/car'), 
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Double click COUNTRY and DEALER_COST.
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click("COUNTRY")
        Designer.ResourcesPanel.Fields.Measures.double_click("DEALER_COST")
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on Convert to page icon in the toolbar.
        """
        Designer.VisualizationToolBar.ConvertToPage.click()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Right click on Visualization 1 container.
        """
        Designer.PageCanvas.Containers.Basic("Container 1").ToolBar.right_click()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)
        
        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify Convert to option is available.
        """
        Designer.ContextMenu.verify_options(['Convert to'], '04', assert_type='in')
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on Convert to option.
        """
        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify Tab, Accordion and Carousel options are available.
        """
        Designer.ContextMenu.verify_options(['Tab', 'Accordion', 'Carousel'], "05.01", "Convert to")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)       
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right click on Visualization 1 container.
            Select Convert to > Tab.
        """
        Designer.PageCanvas.Containers.Basic("Container 1").ToolBar.right_click()
        Designer.ContextMenu.select("Convert to->Tab")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Panel container converted to Tab.
        """
        Designer.PageCanvas.Containers.Tab("Container 1").verify_plus_icon("06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on Fields tab.
            Drag and drop COUNTRY field onto the tab container;
            Select Add content.
        """
        Designer.SideBar.Fields.click()
        Designer.ResourcesPanel.Fields.Dimensions.drag_to_container("COUNTRY", "Container 1")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify content added.
        """
        
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Double click on RETAIL_COST.
        """
        Designer.ResourcesPanel.Fields.Measures.double_click("DEALER_COST")
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify chart updated.
        """

        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Right click on Tab container;
            Select Convert to > Accordion.
        """
        Designer.PageCanvas.Containers.Basic("Container 1").ToolBar.right_click()
        Designer.ContextMenu.select("Convert to->Accordion")
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify Tab container converted to Accordion.
        """

        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click Run in new window icon in the toolbar.
        """
        
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify contents are visible.
        """

        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Close the run window.
        """

        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Drag and drop CAR field onto the accordion container;
            Select Add content.
            Double click on SEATS.
        """
        Designer.ResourcesPanel.Fields.Dimensions.drag_to_container("CAR", "Container 1")
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify content is added.
        """

        HomePage.Home._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Right click on Accordion container;
            Select Convert to > Carousel.
        """

        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify Accordion container converted to Carousel.
        """

        HomePage.Home._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Drag and drop COUNTRY field onto the Carousel container;
            Select Replace content.
        """
        Designer.ResourcesPanel.Fields.Dimensions.drag_to_container("CAR", "Container 1")
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify content is added.
        """

        HomePage.Home._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click Save icon in the toolbar.
            Enter 'C9947035' in Title and click Save.
        """

        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

        HomePage.Home._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Edit the saved designer:
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P452_S31923/G875086/c9947035&startlocation=IBFS:/WFC/Repository/P452_S31923/G875086
        """

        HomePage.Home._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify Carousel container visible in the page.
        """

        HomePage.Home._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Right click on Carousel container;
            Select Convert to > Panel.
        """

        HomePage.Home._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify Carousel container converted to Panel containers.
        """

        HomePage.Home._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Click Undo.
        """

        HomePage.Home._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify Panel containers converted back to Carousel.
        """

        HomePage.Home._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)

        STEP_20 = """
            STEP 20 : Logout WF using API without saving:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

        HomePage.Home._utils.capture_screenshot("20", STEP_20)

