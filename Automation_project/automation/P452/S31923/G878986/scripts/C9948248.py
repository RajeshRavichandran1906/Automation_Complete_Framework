"""-------------------------------------------------------------------------------------------
Author Name  : Rajesh
Automated On : 11-January-2021
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer as DesignerPage
from common.locators.charts.common import Legend
from common.pages.charts.pie import Pie as pie_chart

class C9948248_TestClass(BaseTestCase):
    
    def test_C9948248(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Designer = DesignerPage()
        Pie = pie_chart()
        
        """
        TEST CASE VAIABLES
        """
        content_name = 'G878986->P452_S31923->Retail Samples->Portal->Small Widgets->Category Sales'
        
        STEP_01 = """
            STEP 01 : Launch new Assemble Visualizations as developer user.
    
            https://machine.ibi.com:port/alias/designer?is508=false&item=IBFS:/WFC/Repository/P452_S31923/G878986&tool=framework&startlocation=IBFS:/WFC/Repository/P452_S31923/G878986&startUpConditions=%7B%27mode%27%3A%27assemble%27%7D
        """
        Designer.API.invoke_assemble_visualizations(credential_keys=('mriddev', 'mrpassdev'), workspace_folder="P452_S31923/G878986")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Blank template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Blank')
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Navigate to Retail Samples > Portal > Small Widgets folder;
            Drag and drop Category Sales onto the page canvas.
        """
        Designer.ResourcesPanel.Content.drag_to_page_section(content_name)
        Designer.PageCanvas.Containers.Basic('Category Sales').wait_until_loading_complete(30)
        Designer.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        Designer._webelement.wait_for_element_text(Legend.title, 'Product Category', 60)
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify the content added to the page canvas.
        """
        
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Right click on section and select Format.
        """

        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify Number of Columns section available in the Format.
            12 Column is selected by default and applied in the section grid canvas.
        """

        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on 28 Column.
        """

        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify 28 column applied in section grid canvas.
        """

        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on 45 Column.
        """

        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify 45 column applied in section grid canvas.
        """

        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on 80 Column.
        """

        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify 80 column applied in section grid canvas.
        """

        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Save the page as 'C9948248'
        """

        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Restore C9948248 designer using API:
            https://machine.ibi.com:port/alias/designer?item=IBFS:/WFC/Repository/P452_S31923/G878986/c9948248&startlocation=IBFS:/WFC/Repository/P452_S31923/G878986
        """

        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify 80 columns visible in section grid canvas.
        """

        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click on Section;
            Select Format tab.
        """

        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify 80 Column icon is selected in the Number of Columns.
        """

        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

        HomePage.Home._utils.capture_screenshot("12", STEP_12)

