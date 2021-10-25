"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 16-September-2021
-------------------------------------------------------------------------------------------"""
from common.pages.charts import Pie
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9953827_TestClass(BaseTestCase):
    
    def test_C9953827(self):
        
        """
        TEST CASE OBJECTS
        """
        PieChart = Pie()
        Designer = DesignerPage()
        
        """
        TEST CASE VAIABLES
        """
        content_path = "G875470->P215_S31921->Retail Samples->Portal->Small Widgets->Category Sales"
        
        STEP_01 = """
            STEP 01 : Launch new Assemble Visualizations as developer user.
    
            https://machine.ibi.com:port/alias/designer?is508=false&item=IBFS:/WFC/Repository/P215_S10741/G879873&tool=framework&startlocation=IBFS:/WFC/Repository/P215_S10741/G879873&startUpConditions=%7B%27mode%27%3A%27assemble%27%7D
        """
        Designer.API.invoke_assemble_visualizations(credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Grid 2-1 template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Grid 2-1')  
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on the back arrow < twice in the Content tree and Navigate to Retail samples > Portal > Small Widgets folder;
            Drag and drop Category Sales report onto the Container 1.
        """
        Designer.ResourcesPanel.Content.drag_to_container(content_path, 'Container 1')
        Designer._utils.wait_for_page_loads(30)
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify content added and visible without error.
        """
        Designer.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        PieChart.wait_for_text('Product Category', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '03.01')
        PieChart.verify_legend_title(['Product Category'], '03.02')
        PieChart.verify_number_of_risers(7, '03.03')
        PieChart.verify_total_lables(['1.1B'], '03.04')
        PieChart.verify_riser_color([(1, 'bar_blue')], '03.05')
        PieChart.verify_pie_labels(['Revenue'], '03.06')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click on Containers side tab.
        """
        Designer.SideBar.Container.click()
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Drag and drop Grid container onto the Container 2.
        """
        Designer.ResourcesPanel.Containers.drag_to_container('Grid', 'Container 2')
        Designer._utils.wait_for_page_loads(10)
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Click on Filters side tab.
        """
        Designer.SideBar.Filters.click()
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Right click on Category: filter control;
            Select Add to page.
        """
        Designer.ResourcesPanel.Filters.right_click('Category:')
        Designer.ContextMenu.select('Add to page')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify Category filter control added to the page.
        """
        Designer.PageCanvas.FilterGrid.wait_for_text('Category:', 30)
        Designer.PageCanvas.FilterGrid.verify_control_labels(['Category:'], '07')
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Drag and drop Product Model: control onto the filter bar.
        """
        Designer.ResourcesPanel.Filters.drag_to_filter_bar('Product Model:', 2)
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify Product Model filter control added to the filter bar.
        """
        Designer.PageCanvas.FilterGrid.wait_for_text('Product Model:', 30)
        Designer.PageCanvas.FilterGrid.verify_control_labels(['Product Model:'], '08', assert_type='in')
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Drag and drop Region: control onto the Grid container.
        """
        Designer.ResourcesPanel.Filters.drag_to_container_grid('Container 2', 'Region:', 1)
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify Region control added to grid container.
        """
        Designer.PageCanvas.Containers.Grid('Container 2').FilterGrid.wait_for_text('Region:', 30)
        Designer.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_control_labels(['Region:'], '09')
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click Add all filters to page button.
        """
        Designer.ResourcesPanel.Filters.click_add_all_filters_to_page_button()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify filter controls are added to the filter bar.
        """
        Designer.PageCanvas.FilterGrid.wait_for_text('Product Model:', 30)
        Designer.PageCanvas.FilterGrid.verify_control_labels(['Category:', 'Product Model:', 'Store Type:', 'From:', 'To:'], '10')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Right click on Category: filter control.
            Select Remove from page.
        """
        Designer.ResourcesPanel.Filters.right_click('Category:')
        Designer.ContextMenu.select('Remove from page')
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify Category: control has been removed from the filter bar.
        """
        Designer.PageCanvas.FilterGrid.verify_control_labels(['Product Model:', 'Store Type:', 'From:', 'To:'], '11')
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Right click on Region: filter control.
            Select Remove from page.
        """
        Designer.ResourcesPanel.Filters.right_click('Region:')
        Designer.ContextMenu.select('Remove from page')
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify Region: control has been removed from the Grid container.
        """
        Designer.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_control_labels([], '12')
        Designer._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Save the page as C9953827.
        """
        Designer.ToolBar.save('C9953827')
        Designer._utils.wait_for_page_loads(30)
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("14", STEP_14)