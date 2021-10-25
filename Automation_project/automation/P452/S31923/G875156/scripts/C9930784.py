"""-------------------------------------------------------------------------------------------
Author Name  : RAJESH
Automated On : 30-December-2020
-------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer as DesignerPage
from common.pages.charts.map import Map as maps
from common.locators.charts.common import Legend

class C9930784_TestClass(BaseTestCase):
    
    def test_C9930784(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Designer = DesignerPage()
        Map = maps()
        
        """
        TEST CASE VAIABLES
        """
        content_name = 'G866552->P452_S31923->Retail Samples->Portal->Small Widgets->Category Sales'

        STEP_01 = """
            STEP 01 : Open the Tool as Dev and/or author users
        """
        HomePage.invoke_with_login('mriddev', 'mrpassdev')
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Choose Grid 2-1 template
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.select('P452_S31923->G866552')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Assemble Visualizations')
        Designer._core_utils.switch_to_new_window()
        Designer.Dialog.ChooseTemplate.Common.select('Grid 2-1')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click Content on the sidebar and choose Retail samples domain --> Portals --> Small Widgets
        """
        Designer.SideBar.Content.click()
        Designer._utils.capture_screenshot("03", STEP_03)
        
        STEP_04 = """
            STEP 04 : Drag Category Sales to Panel 1
        """
        Designer.ResourcesPanel.Content.drag_to_container(content_name, 'Container 1')
        Designer.PageCanvas.Containers.Basic('Category Sales').wait_until_loading_complete(30)
        Designer.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        Designer._webelement.wait_for_element_text(Legend.title, 'Product Category', 60)
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Right-click on that panel
        """
        Designer.PageCanvas.Containers.Basic('Category Sales').right_click()
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify Duplicate container is there and above Delete container and below Format
        """
        Designer.ContextMenu.verify_options(['Refresh', 'Edit Title', 'Settings', 'Format', 'Duplicate Container', 'Convert to', 'Delete Container'], '05')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click Duplicate Container
        """
        Designer.ContextMenu.select('Duplicate Container')
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Category Sales is duplicated with title category Sales (Copy)
            It appears at the bottom and the same size
        """
        Designer.PageCanvas.Containers.verify_containers_title(['Category Sales', 'Container 2', 'Container 3', 'Category Sales (Copy)'], '06')
        original = Designer.PageCanvas.Containers.Basic('Category Sales')._get_container_object()
        duplicate = Designer.PageCanvas.Containers.Basic('Category Sales (Copy)')._get_container_object()
        if duplicate.rect['width'] == original.rect['width'] and duplicate.rect['height'] == original.rect['height']: result = True
        else: result = False
        msg = 'Step 06: Verify duplicated container is also same size as orginal container'
        Designer._utils.asequal(result, True, msg)
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Drag some reports to Panel 2 and 3
        """
        Designer.ResourcesPanel.Content.drag_to_container('Regional Sales Trend', 'Container 2')
        Designer.PageCanvas.Containers.Basic('Regional Sales Trend').wait_until_loading_complete(30)
        Designer.ResourcesPanel.Content.drag_to_container('Discount by Region', 'Container 3')
        Designer.PageCanvas.Containers.Basic('Discount by Region').wait_until_loading_complete(30)
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Drag the second set of reports to panel 1, panel 2 and 3 to create a tab, carousel and accordion containers respectively
        """
        Designer.ResourcesPanel.Content.drag_to_container('Category Sales', 'Category Sales')
        Designer.Dialog.AddContent.click_dropdown()
        Designer.ContextMenu.select('Add content as new tab')
        Designer.ResourcesPanel.Content.drag_to_container('Regional Sales Trend', 'Regional Sales Trend')
        Designer.Dialog.AddContent.click_dropdown()
        Designer.ContextMenu.select('Add content as new slide')
        Designer.ResourcesPanel.Content.drag_to_container('Discount by Region', 'Discount by Region')
        Designer.Dialog.AddContent.click_dropdown()
        Designer.ContextMenu.select('Add content as new accordion area')
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click the second tab 
            Right-click  and  Click Duplicate content
        """
        Designer.PageCanvas.Containers.Tab('Category Sales').right_click()
        Designer.ContextMenu.select('Duplicate content')
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : verify that the tab is  added and with (Copy) as a suffix
        """
        Designer.PageCanvas.Containers.Tab('Category Sales').verify_tabs_title(['Category Sales (Copy)'], '09', assert_type= 'in')
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click Slide 1 and right-click on the panel and choose Duplicate content
        """
        Designer.PageCanvas.Containers.Carousel('Regional Sales Trend').right_click()
        Designer.ContextMenu.select('Duplicate content')
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify another slide is added
        """
        Designer.PageCanvas.Containers.Carousel('Regional Sales Trend').verify_no_of_sliders(3, '10')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click Area 1 and right-click on the panel and choose Duplicate content
        """
        Designer.PageCanvas.Containers.Accordion('Discount by Region').right_click()
        Designer.ContextMenu.select('Duplicate content')
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify another area is added with (Copy)
        """
        Designer.PageCanvas.Containers.Accordion('Discount by Region').verify_areas_title(['Discount by Region (Copy)'], '10', assert_type= 'in')
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)
        
        STEP_12 = """
            STEP 12 : Click Outline sidebar
        """
        Designer.SideBar.Outline.click()
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify that slide 1 was duplicated and same for area 1
        """
        Designer.ResourcesPanel.Outline.verify_items(['Category Sales (Copy)', 'Regional Sales Trend (Copy)', 'Discount by Region (Copy)'], '12', assert_type='in')
        Designer._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Right-click on the outline side bar on one of the tabs/slides/areas and choose Duplicate content
        """
        Designer.ResourcesPanel.Outline.right_click_on_item('Category Sales->Category Sales')
        Designer.ContextMenu.select('Duplicate content')
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify those are duplicated and they appear after the one that was chosen to be duplicated
        """
        Designer.PageCanvas.Containers.Tab('Category Sales').verify_tabs_title(['Category Sales', 'Category Sales', 'Category Sales (Copy)', 'Category Sales (Copy)'], '13')
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Right-click on the outline side bar on one of the tabs/slides/areas (Copy) and choose Duplicate content
        """
        Designer.ResourcesPanel.Outline.right_click_on_item('Discount by Region->Discount by Region (Copy)')
        Designer.ContextMenu.select('Duplicate content')
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify those are duplicated and they appear after the one that was chosen to be duplicated and (Copy) (Copy) appears as a suffix
        """
        Designer.PageCanvas.Containers.Accordion('Discount by Region').verify_areas_title(['Discount by Region', 'Discount by Region', 'Discount by Region (Copy)', 'Discount by Region (Copy) (Copy)'], '14')
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Drag large widgets -->Stores Sales by Region to the canvas
        """
        Designer.SideBar.Content.click()
        Designer.ResourcesPanel.Content.drag_to_container('Small Widgets->Large Widgets->Store Sales by Region', 'Category Sales (Copy)', container_location='bottom_left')
        Designer.PageCanvas.Containers.Basic('Store Sales by Region').wait_until_loading_complete(120)
        Designer.PageCanvas.Containers.Basic('Store Sales by Region').switch_to_frame()
        Designer._webelement.wait_for_element_text(Legend.title, 'Store Business Region', 120)
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Resize it to be bigger
        """
        Designer.PageCanvas.Containers.Basic('Store Sales by Region').resize('middle_right', xoffset=300)
        Designer.PageCanvas.Containers.Basic('Store Sales by Region').wait_until_loading_complete(120)
        Designer.PageCanvas.Containers.Basic('Store Sales by Region').switch_to_frame()
        Designer._webelement.wait_for_element_text(Legend.title, 'Store Business Region', 120)
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Right-click on duplicate container
        """
        Designer.PageCanvas.Containers.Basic('Store Sales by Region').right_click()
        Designer.ContextMenu.select('Duplicate Container')
        Designer.PageCanvas.Containers.Basic('Store Sales by Region').wait_until_loading_complete(120)
        Designer._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : verify the container size and map
        """
        original = Designer.PageCanvas.Containers.Basic('Store Sales by Region')._get_container_object()
        duplicate = Designer.PageCanvas.Containers.Basic('Store Sales by Region (Copy)')._get_container_object()
        if duplicate.rect['width'] == original.rect['width'] and duplicate.rect['height'] == original.rect['height']: result = True
        else: result = False
        msg = 'Step 17.01: Verify duplicated container is also same size as orginal container'
        Designer._utils.asequal(result, True, msg)
        Designer.PageCanvas.Containers.Basic('Store Sales by Region (Copy)').switch_to_frame()
        Designer._webelement.wait_for_element_text(Legend.title, 'Store Business Region', 120)
        Map.verify_number_of_risers(86, '17.02')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)