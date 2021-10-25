"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 17-September-2021
-------------------------------------------------------------------------------------------"""
from common.pages.charts import Pie
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9953848_TestClass(BaseTestCase):
    
    def test_C9953848(self):
        
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
            STEP 04 : Right click on Category Sales container and select Duplicate content (select Duplicate container if release is 8207.29 or higher)
        """
        Designer.PageCanvas.Containers.Basic('Category Sales').right_click()
        Designer.ContextMenu.select('Duplicate Container')
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify duplicated container Category Sales (Copy) is available in the page canvas.
        """
        Designer.PageCanvas.Containers.verify_containers_title(['Category Sales', 'Container 2', 'Container 3', 'Category Sales (Copy)'], '04')
        Designer.PageCanvas.Containers.Basic('Category Sales (Copy)').switch_to_frame()
        PieChart.wait_for_text('Product Category', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '04.01')
        PieChart.verify_legend_title(['Product Category'], '04.02')
        PieChart.verify_number_of_risers(7, '04.03')
        PieChart.verify_total_lables(['1.1B'], '04.04')
        PieChart.verify_riser_color([(1, 'bar_blue')], '04.05')
        PieChart.verify_pie_labels(['Revenue'], '04.06')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Right click on Category Sales container and select Convert to > Tab.
        """
        Designer.PageCanvas.Containers.Basic('Category Sales').right_click()
        Designer.ContextMenu.select('Convert to->Tab')
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify category sales container converted to Tab.
        """
        Designer.PageCanvas.Containers.Tab('Category Sales').verify_tabs_title(['Category Sales'], '05')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right click on Category Sales (Copy) container and select Convert to > Carousel.
        """
        Designer.PageCanvas.Containers.Basic('Category Sales (Copy)').right_click()
        Designer.ContextMenu.select('Convert to->Carousel')
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify category sales container converted to Carousel.
        """
        Designer.PageCanvas.Containers.Carousel('Category Sales (Copy)').verify_no_of_sliders(1)
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)
        
        STEP_07 = """
            STEP 07 : Multi select Category Sales and Category Sales (Copy) containers.
            Right click and select Combine > Accordion.
        """
        Designer.PageCanvas.Containers.multi_select_containers(['Category Sales'])
        Designer.PageCanvas.Containers.Tab('Category Sales').right_click()
        Designer.ContextMenu.select('Combine->Accordion')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify accordion container is created.
        """
        Designer.PageCanvas.Containers.Accordion('Container 4').verify_areas_title(['Category Sales', 'Category Sales (Copy)'], '07')
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click on Category Sales (Copy) area.
        """
        Designer.PageCanvas.Containers.Accordion('Container 4').expand_area('Category Sales (Copy)')
        Designer.PageCanvas.Containers.Accordion('Container 4').switch_to_frame('Category Sales (Copy)')
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify Category Sales (Copy) content is visible without error.
        """
        PieChart.wait_for_text('Product Category', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '08.01')
        PieChart.verify_legend_title(['Product Category'], '08.02')
        PieChart.verify_number_of_risers(7, '08.03')
        PieChart.verify_total_lables(['1.1B'], '08.04')
        PieChart.verify_riser_color([(1, 'bar_blue')], '08.05')
        PieChart.verify_pie_labels(['Revenue'], '08.06')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Right click on Container 4 and select Duplicate content.
        """
        Designer.PageCanvas.Containers.Accordion('Container 4').right_click()
        Designer.ContextMenu.select('Duplicate content')
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify Category Sales (Copy) (Copy) area is created.
        """
        Designer.PageCanvas.Containers.Accordion('Container 4').verify_areas_title(['Category Sales', 'Category Sales (Copy)', 'Category Sales (Copy) (Copy)'], '09')
        Designer.PageCanvas.Containers.Accordion('Container 4').switch_to_frame('Category Sales (Copy) (Copy)')
        PieChart.wait_for_text('Product Category', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '09.01')
        PieChart.verify_legend_title(['Product Category'], '09.02')
        PieChart.verify_number_of_risers(7, '09.03')
        PieChart.verify_total_lables(['1.1B'], '09.04')
        PieChart.verify_riser_color([(1, 'bar_blue')], '09.05')
        PieChart.verify_pie_labels(['Revenue'], '09.06')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Save the page as C9953848.
        """
        Designer.ToolBar.save('C9953848')
        Designer._utils.wait_for_page_loads(30)
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("11", STEP_11)