from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9946913_TestClass(BaseTestCase):
    
    def test_C9946913(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        
        STEP_01 = """
            STEP 01 : Launch new Assemble Visualizations as developer user.
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
            STEP 04 : Drag and drop Container, Tab, Accordion and Carousel containers onto the page canvas.
        """
        Designer.ResourcesPanel.Containers.drag_to_page_section('Basic')
        Designer.ResourcesPanel.Containers.drag_to_container('Tab', 'Container 1', container_location='top_right', x=80, y=10)
        Designer.ResourcesPanel.Containers.drag_to_container('Accordion', 'Container 1', container_location='bottom_left')
        Designer.ResourcesPanel.Containers.drag_to_container('Carousel', 'Container 2', container_location='bottom_middle')
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
                STEP 05 : Right click on Container container and select Convert to.
        """
        Designer.PageCanvas.Containers.Basic('Container 1').right_click()
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify following options are available.
        """
        Designer.ContextMenu.verify_options(['Tab', 'Accordion', 'Carousel'], '05.01', menu_path='Convert to')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right click on Tab container and select Convert to.
        """
        Designer.PageCanvas.Containers.Basic('Container 2').right_click()
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Container, Accordion and Carousel options are available.
        """
        Designer.ContextMenu.verify_options(['Basic', 'Accordion', 'Carousel'], '06.01', menu_path='Convert to')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Right click on Carousel container and select Convert to.
        """
        Designer.PageCanvas.Containers.Basic('Container 3').right_click()
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify Container, Tab and Accordion options are available.
        """
        Designer.ContextMenu.verify_options(['Basic', 'Tab', 'Carousel'], '07.01', menu_path='Convert to')
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Right click on Accordion container and select Convert to.
        """
        Designer.PageCanvas.Containers.Basic('Container 4').right_click()
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify Container, Tab and Carousel options are available.
        """
        Designer.ContextMenu.verify_options(['Basic', 'Tab', 'Accordion'], '08.01', menu_path='Convert to')
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Drag and drop Grid, Panel group, Link tile and Explorer containers onto the page canvas.
        """
        Designer.ResourcesPanel.Containers.drag_to_container('Grid', 'Container 3', container_location='bottom_left', y=-5)
        Designer.ResourcesPanel.Containers.drag_to_container('Panel group', 'Container 4', container_location='bottom_middle')
        Designer.ResourcesPanel.Containers.drag_to_container('Link tile', 'Container 5', container_location='bottom_left', y=-15)
        Designer.ResourcesPanel.Containers.drag_to_container('Explorer', 'Container 7', container_location='bottom_middle')
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Right click on Grid container.
        """
        Designer.PageCanvas.Containers.Basic('Container 5').ToolBar.right_click()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify Convert to option is not available.
        """
        Designer.ContextMenu.verify_options(['Convert to'], '10.01', assert_type='notin')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Right click on Panel group.
        """
        Designer.PageCanvas.Containers.Basic(index=6).right_click()
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify Convert to option is not available.
        """
        Designer.ContextMenu.verify_options(['Convert to'], '11.01', assert_type='notin')
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Right click on Link tile.
        """
        Designer.PageCanvas.Containers.Basic(index=7).right_click()
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify Convert to option is not available.
        """
        Designer.ContextMenu.verify_options(['Convert to'], '12.01', assert_type='notin')
        Designer._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Right click on Explorer.
        """
        Designer.PageCanvas.Containers.Basic('Container 8').ToolBar.right_click()
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify Convert to option is not available.
        """
        Designer.ContextMenu.verify_options(['Convert to'], '13.01', assert_type='notin')
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("14", STEP_14)