"""-------------------------------------------------------------------------------------------
Author Name  : AH14645
Automated On : 22-December-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9948691_TestClass(BaseTestCase):
    
    def test_C9948691(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        
        """
        TEST CASE VAIABLES
        """
        
        container_options = ['Edit Title', 'Duplicate content']
        
        STEP_01 = """
            STEP 01 : Launch new Assemble Visualizations as developer user.
    
            https://machine.ibi.com:port/alias/designer?is508=false&item=IBFS:/WFC/Repository/P452_S31923/G878240&tool=framework&startlocation=IBFS:/WFC/Repository/P452_S31923/G878240&startUpConditions=%7B%27mode%27%3A%27assemble%27%7D
        """
        Designer.API.invoke_assemble_visualizations(('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Choose the Blank template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Blank')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Drag and drop Category Sales report onto the page canvas from Retail Samples > Portal > Small Widgets folder.
        """
        Designer.ResourcesPanel.Content.drag_to_page_section("G878240->P452_S31923->Retail Samples->Portal->Small Widgets->Category Sales")
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on Container side tab.
        """
        Designer.SideBar.Container.click()
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Double click on Tab, Carousel, Accordion and Panel group.
        """
        Designer.ResourcesPanel.Containers.double_click('Tab')
        Designer.ResourcesPanel.Containers.double_click('Carousel')
        Designer.ResourcesPanel.Containers.double_click('Accordion')
        Designer.ResourcesPanel.Containers.double_click('Panel group')
        Designer._utils.wait_for_page_loads(20, pause_time=2)
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Drag and drop Panel and Tab onto the Panel group.
        """
        Designer.ResourcesPanel.Containers.drag_to_container('Basic', container_index=5, container_location='middle_left', x=10, y=5)
        Designer._utils.wait_for_page_loads(10, pause_time=2)
        Designer.ResourcesPanel.Containers.drag_to_container('Tab', container_index=5, container_location='middle_right', x=-20, y=-20)
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Click on Outline side tab.
        """
        Designer.SideBar.Outline.click()
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Right click on Category Sales content in outline tree.
        """
        Designer.ResourcesPanel.Outline.right_click_on_item('Category Sales->Category Sales')
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify following context menus are visible:
            1) Edit title
            2) Duplicate Content
        """
        Designer.ContextMenu.verify_options(container_options, '08.01')
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Right click on Tab 1 in outline tree.
        """
        Designer.PageCanvas.Containers.Basic('Category Sales').select() #Click on Category Sales container to close current context menu
        Designer.ResourcesPanel.Outline.right_click_on_item('Container 2->Tab 1')
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify following context menus are visible:
            1) Edit title
            2) Duplicate content
        """
        Designer.ContextMenu.verify_options(container_options, '09.01')
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click on (+) New tab in Panel 2 container.
        """
        Designer.PageCanvas.Containers.Tab("Container 2").add_new_tab()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Right click on Tab 2 in outline tree.
        """
        Designer.ResourcesPanel.Outline.right_click_on_item('Container 2->Tab 2')
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify following context menus are visible:
            1) Edit title
            2) Duplicate content
            3) Delete tab
        """
        Designer.ContextMenu.verify_options([container_options[0], container_options[1], "Delete Tab"], '11.01')
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Right click on Slide 1 in outline tree.
        """
        Designer.PageCanvas.Containers.Basic('Category Sales').select() #Click on Category Sales container to close current context menu
        Designer.ResourcesPanel.Outline.right_click_on_item('Container 3->Slide 1')
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify following context menus are visible:
            1) Edit title
            2) Duplicate content
        """
        Designer.ContextMenu.verify_options(container_options, '12.01')
        Designer._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Select Duplicate content context menu.
        """
        Designer.ContextMenu.select("Duplicate content")
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Right click on Slide 1 (Copy) in outline tree.
        """
        Designer.ResourcesPanel.Outline.right_click_on_item('Container 3->Slide 1 (Copy)')
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify following context menus are visible:
            1) Edit title
            2) Duplicate content
            3) Delete slide
        """
        Designer.ContextMenu.verify_options([container_options[0], container_options[1], "Delete slide"], '14.01')
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Right click on Area 1 in outline tree.
        """
        Designer.PageCanvas.Containers.Basic('Category Sales').select() #Click on Category Sales container to close current context menu
        Designer.ResourcesPanel.Outline.right_click_on_item('Container 4->Area 1')
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify following context menus are visible:
            1) Edit title
            2) Duplicate content
        """
        Designer.ContextMenu.verify_options(container_options, '15.01')
        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Click on (+) New area in Panel 4 container.
        """
        Designer.PageCanvas.Containers.Accordion("Container 4").add_new_area()
        Designer._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Right click on Area 2 in outline tree.
        """
        Designer.ResourcesPanel.Outline.right_click_on_item('Container 4->Area 2')
        Designer._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify following context menus are visible:
            1) Edit title
            2) Duplicate content
            3) Delete area
        """
        Designer.ContextMenu.verify_options([container_options[0], container_options[1], "Delete Area"], '17.01')
        Designer._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Right click on Content under Panel 6 in Outline tree.
        """
        Designer.PageCanvas.Containers.Basic('Container 3').select() #Click on Category Sales container to close current context menu
        Designer.ResourcesPanel.Outline.right_click_on_item('Container 5->Container 6->Content')
        Designer._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify following context menus are visible:
            1) Edit title
            2) Duplicate content
        """
        Designer.ContextMenu.verify_options(container_options, '18.01')
        Designer._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Click on (+) New tab in Panel 7 container.
        """
        Designer.PageCanvas.Containers.Tab("Container 7").add_new_tab()
        Designer._utils.capture_screenshot("19", STEP_19)

        STEP_20 = """
            STEP 20 : Right click on Tab 1 under Panel 7.
        """
        Designer.ResourcesPanel.Outline.right_click_on_item('Container 5->Container 7->Tab 1')
        Designer._utils.capture_screenshot("20", STEP_20)

        STEP_20_EXPECTED = """
            STEP 20 - Expected : Verify following context menus are visible:
            1) Edit title
            2) Duplicate content
            3) Delete tab
        """
        Designer.ContextMenu.verify_options([container_options[0], container_options[1], "Delete Tab"], '20.01')
        Designer._utils.capture_screenshot("20 - Expected", STEP_20_EXPECTED, True)

        STEP_21 = """
            STEP 21 : Logout WF using API without saving:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("21", STEP_21)