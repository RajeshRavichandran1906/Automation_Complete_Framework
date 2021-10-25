"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 21-December-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9948690_TestClass(BaseTestCase):
    
    def test_C9948690(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        
        """
        TEST CASE VAIABLES
        """
        container_options = ['Edit Title', 'Delete Container']
        
        STEP_01 = """
            STEP 01 : Launch new Assemble Visualizations as developer user.
        """
        Designer.API.invoke_assemble_visualizations(('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Choose the Grid 2-1 template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Grid 2-1')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on Outline side tab.
        """
        Designer.SideBar.Outline.click()
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Right click on Panel 1 in outline tree.
        """
        Designer.ResourcesPanel.Outline.right_click_on_item('Container 1')
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify following context menus are visible:
            1.Edit title
            2.Delete container
        """
        Designer.ContextMenu.verify_options(container_options, '04.01')
        Designer._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Right click on Panel 1 in page.
        """
        Designer.PageCanvas.Containers.Basic('Container 1').right_click()
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Edit title and Delete container icons are same as Outline tree.
        """
        Designer.ContextMenu.verify_options(container_options, '05.01', assert_type='in')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on Container side tab.
        """
        Designer.SideBar.Container.click()
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Double click on Grid, Panel group, Link tile and Explorer.
        """
        Designer.ResourcesPanel.Containers.double_click('Grid')
        Designer.ResourcesPanel.Containers.double_click('Panel group')
        Designer.ResourcesPanel.Containers.double_click('Link tile')
        Designer.ResourcesPanel.Containers.double_click('Explorer')
        Designer._utils.wait_for_page_loads(20, pause_time=2)
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Drag and drop Tab onto the Panel group.
        """
        Designer.ResourcesPanel.Containers.drag_to_container('Tab', container_index=5)
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click on Outline side tab.
        """
        Designer.SideBar.Outline.click()
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Right click on Panel 4 (Grid)
        """
        Designer.ResourcesPanel.Outline.right_click_on_item('Container 4')
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify following context menus are visible:
            1) Edit title
            2) Delete container
        """
        Designer.ContextMenu.verify_options(container_options, '10.01')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Right click on Panel 5 (Panel group)
        """
        Designer.ResourcesPanel.Outline.right_click_on_item('Container 5')
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify following context menus are visible:
            1) Edit title
            2) Delete container
        """
        Designer.ContextMenu.verify_options(container_options, '11.01')
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Right click on Panel 6 (Link tile)
        """
        Designer.PageCanvas.Containers.Basic('Container 5').select() #Click on Container 5 to close current context menu
        Designer.ResourcesPanel.Outline.right_click_on_item('Container 6')
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify following context menus are visible:
            1) Edit title
            2) Delete container
        """
        Designer.ContextMenu.verify_options(container_options, '12.01')
        Designer._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Right click on Panel 7 (Explorer)
        """
        Designer.PageCanvas.Containers.Basic('Container 6').select() #Click on Container 5 to close current context menu
        Designer.ResourcesPanel.Outline.right_click_on_item('Container 7')
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify following context menus are visible:
            1) Edit title
            2) Delete container
        """
        Designer.ContextMenu.verify_options(container_options, '13.01')
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Right click on Panel 8 (Tab)
        """
        Designer.ResourcesPanel.Outline.right_click_on_item('Container 8')
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify following context menus are visible:
            1) Edit title
            2) Delete container
        """
        Designer.ContextMenu.verify_options(container_options, '14.01')
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Logout WF using API without saving:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("15", STEP_15)