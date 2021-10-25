"""-------------------------------------------------------------------------------------------
Author Name  : AH14645
Automated On : 06-January-2021
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage
from common.pages.charts import Pie, Scatter, Bar, TreeMap

class C9947034_TestClass(BaseTestCase):
    
    def test_C9947034(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        PieChart = Pie()
        ScatterChart = Scatter()
        BarChart = Bar()
        TreeMapChart = TreeMap()
        """
        TEST CASE VAIABLES
        """
        
        STEP_01 = """
            STEP 01 : Launch new Assemble Visualizations as developer user.
    
            https://machine.ibi.com:port/alias/designer?is508=false&item=IBFS:/WFC/Repository/P452_S31923/G875086&tool=framework&startlocation=IBFS:/WFC/Repository/P452_S31923/G875086&startUpConditions=%7B%27mode%27%3A%27assemble%27%7D
        """
        Designer.API.invoke_assemble_visualizations(('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Blank template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Blank')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on Container side tab.
        """
        Designer.SideBar.Container.click()
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Double click on Panel container.
        """
        Designer.ResourcesPanel.Containers.double_click("Basic")
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Select Content side tab;
            Drag and drop Category Sales onto the Panel 1 from Retail Samples > Portal > Small widgets folder.
        """
        Designer.SideBar.Content.click()
        Designer.ResourcesPanel.Content.drag_to_container("G875086->P452_S31923->Retail Samples->Portal->Small Widgets->Category Sales", "Container 1")
        Designer._utils.wait_for_page_loads(20)
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify content added in container.
        """
        Designer.PageCanvas.Containers.Basic("Category Sales").switch_to_frame()
        PieChart.verify_number_of_risers(7, "05.01")
        PieChart.verify_legend_title(["Product Category"], "05.02")
        PieChart.verify_legend_labels(["Accessories", "Camcorder", "Computers", "Media Player", "Stereo Systems", "Televisions", "Video Production"], "05.03")
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right click on Panel container;
            Select Convert to > Tab.
        """
        Designer.PageCanvas.Containers.Basic("Category Sales").right_click()
        Designer.ContextMenu.select("Convert to->Tab")
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Panel container converted to Tab.
        """
        Designer._utils.wait_for_page_loads(20)
        Designer.PageCanvas.Containers.Tab("Category Sales").verify_tabs_title(["Category Sales"], "06.01")
        Designer.PageCanvas.Containers.Tab("Category Sales").verify_plus_icon("06.02")
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Drag and drop Discount by Region onto the tab container from Retail Samples > Portal > Small widgets folder;
            Select Add content.
        """
        Designer.ResourcesPanel.Content.drag_to_container("Discount by Region", "Category Sales")
        Designer.Dialog.AddContent.wait_until_visible()
        Designer.Dialog.AddContent.select("Add content")
        Designer.Dialog.AddContent.wait_until_invisible()
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Right click on Tab container;
            Select Convert to > Accordion.
        """
        Designer._utils.wait_for_page_loads(20)
        Designer.PageCanvas.Containers.Tab("Category Sales").right_click()
        Designer.ContextMenu.select("Convert to->Accordion")
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify Tab container converted to Accordion.
        """
        Designer._utils.wait_for_page_loads(20)
        Designer.PageCanvas.Containers.Accordion("Category Sales").verify_areas_title(["Category Sales", "Discount by Region"], "08.01")
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Drag and drop Average Cost V Sales onto the accordion container from Retail Samples > Portal > Small widgets folder;
            Select Replace content.
        """
        Designer.ResourcesPanel.Content.drag_to_container("Average Cost v Sales", "Category Sales")
        Designer.Dialog.AddContent.wait_until_visible()
        Designer.Dialog.AddContent.select("Replace content")
        Designer.Dialog.AddContent.wait_until_invisible()
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify content in converted container is replaced.
        """
        Designer._utils.wait_for_page_loads(20)
        Designer.PageCanvas.Containers.Accordion("Category Sales").verify_areas_title(['Average Cost v Sales', 'Discount by Region'], "09.01")
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)
        
        STEP_10 = """
            STEP 10 : Right click on Accordion container;
            Select Convert to > Carousel.
        """
        Designer.PageCanvas.Containers.Accordion("Category Sales").right_click()
        Designer.ContextMenu.select("Convert to->Carousel")
        Designer._utils.capture_screenshot("10", STEP_10)
        
        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify Accordion container converted to Carousel. Verify Autoplay interval option visible in Settings.
        """
        Designer._utils.wait_for_page_loads(20)
        Designer.PageCanvas.Containers.Carousel("Category Sales").verify_no_of_sliders(2, "10.01")
        Designer.PropertiesPanel.Settings.ContainerSettings.AutoplayInterval.verify_text('0', "10.02")
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)
        
        STEP_11 = """
            STEP 11 : Select Slide 2.
        """
        Designer.PageCanvas.Containers.Carousel("Category Sales").click_on_slide_pin(2)
        Designer._utils.capture_screenshot("11", STEP_11)
        
        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify content is visible without error.
        """
        Designer._utils.wait_for_page_loads(10)
        Designer.PageCanvas.Containers.Carousel("Category Sales").switch_to_frame(2)
        TreeMapChart.verify_xaxis_labels(["1", "2", "3", "4"], "13.04")
        TreeMapChart.verify_number_of_risers(16, "11.03")
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)
        
        STEP_12 = """
            STEP 12 : Drag and drop Revenue Product Bar onto the Carousel container from Retail Samples > Portal > Small widgets folder;
            Select Add content.
        """
        Designer.ResourcesPanel.Content.drag_to_container("Revenue Product Bar", "Category Sales")
        Designer.Dialog.AddContent.wait_until_visible()
        Designer.Dialog.AddContent.select("Add content")
        Designer.Dialog.AddContent.wait_until_invisible()
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Click Run in new window icon in the toolbar.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Switch slide and verify contents are visible.
        """
        Designer._utils.wait_for_page_loads(20)
        Designer.RunMode.PageCanvas.Containers.Carousel("Category Sales").switch_to_frame(1)
        ScatterChart.verify_xaxis_title(["Revenue"], "13.01")
        ScatterChart.verify_yaxis_title(["Gross Profit"], "13.02")
        ScatterChart.verify_number_of_risers(21, "13.03")
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Carousel("Category Sales").click_on_slide_pin(2)
        Designer._utils.wait_for_page_loads(15)
        Designer.RunMode.PageCanvas.Containers.Carousel("Category Sales").switch_to_frame(2)
        TreeMapChart.verify_xaxis_labels(["1", "2", "3", "4"], "13.04")
        TreeMapChart.verify_number_of_risers(16, "13.05")
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Carousel("Category Sales").click_on_slide_pin(3)
        Designer._utils.wait_for_page_loads(15)
        Designer.RunMode.PageCanvas.Containers.Carousel("Category Sales").switch_to_frame(3)
        BarChart.verify_xaxis_title(["Product Category"], "13.06")
        BarChart.verify_yaxis_title(["Revenue"], "13.07")
        BarChart.verify_number_of_risers(28, "13.08")
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)
        
        STEP_14 = """
            STEP 14 : Close the run window.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("14", STEP_14)
        
        STEP_15 = """
            STEP 15 : Click Save icon in the toolbar.
            Enter 'C9947034' in Title and click Save.
        """
        Designer.ToolBar.save("C9947034")
        Designer._utils.capture_screenshot("15", STEP_15)
        
        STEP_16 = """
            STEP 16 : Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.wait_for_page_loads(10)
        Designer._utils.capture_screenshot("16", STEP_16)
        
        STEP_17 = """
            STEP 17 : Edit the saved designer:
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P452_S31923/G875086/c9947034&startlocation=IBFS:/WFC/Repository/P452_S31923/G875086
        """
        Designer.API.edit_page("C9947034", ("mriddev", "mrpassdev"), 'P452_S31923/G875086')
        Designer._utils.wait_for_page_loads(30)
        Designer._utils.capture_screenshot("17", STEP_17)
        
        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify Carousel container visible in the page.
        """
        Designer.PageCanvas.Containers.Carousel("Category Sales").verify_no_of_sliders(3, "17.01")
        Designer._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)
        
        STEP_18 = """
            STEP 18 : Right click on Carousel container;
            Select Convert to > Panel.
        """
        Designer.PageCanvas.Containers.Carousel("Category Sales").right_click()
        Designer.ContextMenu.select("Convert to->Basic")
        Designer._utils.capture_screenshot("18", STEP_18)
        
        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify Carousel container converted to Panel.
        """
        Designer._utils.wait_for_page_loads(15)
        Designer.PageCanvas.Containers.verify_number_of_containers(3, "18.01")
        Designer._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)
        
        STEP_19 = """
            STEP 19 : Click Undo.
        """
        Designer.ToolBar.Undo.click()
        Designer._utils.capture_screenshot("19", STEP_19)
        
        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify Panel containers are converted back to Carousel.
        """
        Designer._utils.wait_for_page_loads(15)
        Designer.PageCanvas.Containers.Carousel("Category Sales").verify_no_of_sliders(3, "19.01")
        Designer._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)
        
        STEP_20 = """
            STEP 20 : Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("20", STEP_20)
        
        
        