"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 18-October-2021
-------------------------------------------------------------------------------------------"""
import time
from common.pages.charts import Pie
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9953828_TestClass(BaseTestCase):
    
    def test_C9953828(self):
        
        """
        TEST CASE OBJECTS
        """
        PieChart = Pie()
        Designer = DesignerPage()
        
        """
        TEST CASE VAIABLES
        """
        content_path = "G875470->P215_S31921->Retail Samples->Portal->Small Widgets->Category Sales"
        page_header_css = "div.pd-page-header"
        
        STEP_01 = """
            STEP 01 : Launch new Assemble Visualizations as developer user
            https://machine.ibi.com:port/alias/designer?is508=false&item=IBFS:/WFC/Repository/P215_S10741/G879873&tool=framework&startlocation=IBFS:/WFC/Repository/P215_S10741/G879873&startUpConditions=%7B%27mode%27%3A%27assemble%27%7D
        """
        Designer.API.invoke_assemble_visualizations(credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Choose the Blank template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Blank')  
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on the back arrow '<' twice in the Content tree and Navigate to Retail samples > Portal > Small Widgets folder;
            Drag and drop Category Sales report onto the page canvas.
        """
        Designer.ResourcesPanel.Content.drag_to_page_section(content_path)
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Select Filters side tab.
        """
        Designer.SideBar.Filters.click()
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click Add filter controls button.
        """
        Designer.ResourcesPanel.Filters.click_add_all_filters_to_page_button()
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify controls are added to the page.
        """
        Designer.PageCanvas.FilterGrid.wait_for_text("Category:", time_out=60)
        Designer.PageCanvas.FilterGrid.verify_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], '05')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right click on Category: control and select Convert.
        """
        Designer.PageCanvas.FilterGrid.Control("Category:").click()
        Designer.PageCanvas.FilterGrid.right_click_on_cell(1)
        Designer.ContextMenu.select("Convert")
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Toggle and Double list is available in Convert Control To model dialog.
        """
        Designer.Dialog.ConvertControlTo.wait_for_text("Convert")
        Designer.Dialog.ConvertControlTo.verify_options(['Checkbox', 'Button set', 'Toggle', 'Double list'], '06')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Select Toggle in Convert Control To model dialog.
        """
        Designer.Dialog.ConvertControlTo.select_options("Toggle")
        Designer.Dialog.ConvertControlTo.wait_until_invisible()
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify dropdown control converted to Toggle.
        """
        Designer.PageCanvas.FilterGrid.Control('Category:').Toggle.verify_converted('07.01')
        Designer.PageCanvas.FilterGrid.Control('Category:').Toggle.verify_lables(['Accessories', 'Camcorder'], '07.02')
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Right click on Product Model: control and select Convert.
            Select Double list in Convert Control To model dialog.
        """
        Designer.PageCanvas.FilterGrid.Control('Product Model:').click()
        Designer.PageCanvas.FilterGrid.right_click_on_cell(2)
        Designer.ContextMenu.select('Convert')
        Designer.Dialog.ConvertControlTo.wait_for_text("Convert")
        Designer.Dialog.ConvertControlTo.select_options('Double list')
        Designer.Dialog.ConvertControlTo.wait_until_invisible()
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify dropdown control converted to Double list.
        """
        Designer.PageCanvas.FilterGrid.Control('Product Model:').DoubleList.verify_converted('08')
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click Run in new window icon in the toolbar.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify page runs successfully with controls.
        """
        Designer.RunMode.PageCanvas.FilterGrid.wait_for_text("Category:", time_out=120)
        Designer.RunMode.PageCanvas.FilterGrid.verify_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], '09')
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Select 'Camcorder' in 'Category' filter control.
            Select first three values in Double list control.
        """
        time.sleep(5)
        Designer.RunMode.PageCanvas.FilterGrid.Control('Category:').Toggle.check()
        time.sleep(20)
        Designer.RunMode.PageCanvas.FilterGrid.Control('Product Model:').click(location='middle')
        Designer.RunMode.PageCanvas.FilterGrid.Control('Product Model:').DoubleList.wait_for_text('Values', 15)
        Designer.RunMode.PageCanvas.FilterGrid.Control('Product Model:').DoubleList.DualListBox.select_options_in_all_options_area(['Canon FS300', 'Canon HFR11', 'Canon XHA1S'])
        Designer.RunMode.PageCanvas.FilterGrid.Control('Product Model:').DoubleList.DualListBox.AddSelections.click()
        Designer._core_utils.left_click(Designer._utils.validate_and_get_webdriver_object(page_header_css, "Page Header"))
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify filter condition applied in the page.
        """
        Designer.RunMode.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        PieChart.wait_for_text('Revenue', time_out=30)
        PieChart.verify_number_of_risers(1, '10.01')
        PieChart.verify_pie_labels(['Revenue'], '10.02')
        PieChart.verify_total_lables(['34.4M'], '10.03')
        PieChart.verify_riser_color([(1, 'bar_blue')], '10.04')
        PieChart.verify_legend_title(['Product Category'], '10.05')
        PieChart.verify_legend_labels(['Camcorder'], '10.06')
        PieChart.verify_data_lables(['100%'], '10.07')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Close the run window.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Click Save;
            Enter C9953828 in Title and click Save.
        """
        Designer.ToolBar.save('C9953828')
        Designer._utils.wait_for_page_loads(30)
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Run designer using API:
            https://machine.ibi.com:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P215_S10741/G879873&BIP_item=c9953828
        """
        Designer.API.run_page('C9953828', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify filter controls are available in the page.
        """
        Designer.RunMode.PageCanvas.FilterGrid.wait_for_text('Category:', time_out=180)
        Designer.RunMode.PageCanvas.FilterGrid.verify_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], '14')
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Select 'Camcorder' in 'Category' filter control.
            Select first three values in Double list control.
        """
        time.sleep(5)
        Designer.RunMode.PageCanvas.FilterGrid.Control('Category:').Toggle.check()
        time.sleep(20)
        Designer.RunMode.PageCanvas.FilterGrid.Control('Product Model:').click(location='middle')
        Designer.RunMode.PageCanvas.FilterGrid.Control('Product Model:').DoubleList.wait_for_text('Values', 15)
        Designer.RunMode.PageCanvas.FilterGrid.Control('Product Model:').DoubleList.DualListBox.select_options_in_all_options_area(['Canon FS300', 'Canon HFR11', 'Canon XHA1S'])
        Designer.RunMode.PageCanvas.FilterGrid.Control('Product Model:').DoubleList.DualListBox.AddSelections.click()
        Designer._core_utils.left_click(Designer._utils.validate_and_get_webdriver_object(page_header_css, "Page Header"))
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify filter condition applied in the page.
        """
        Designer.RunMode.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        PieChart.wait_for_text('Revenue', time_out=30)
        PieChart.verify_number_of_risers(1, '15.01')
        PieChart.verify_pie_labels(['Revenue'], '15.02')
        PieChart.verify_total_lables(['34.4M'], '15.03')
        PieChart.verify_riser_color([(1, 'bar_blue')], '15.04')
        PieChart.verify_legend_title(['Product Category'], '15.05')
        PieChart.verify_legend_labels(['Camcorder'], '15.06')
        PieChart.verify_data_lables(['100%'], '15.07')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Restore C9953828 designer using API:
            https://machine.ibi.com:port/alias/designer?item=IBFS:/WFC/Repository/P215_S10741/G879873/c9953828&startlocation=IBFS:/WFC/Repository/P215_S10741/G879873
        """
        Designer.API.edit_page('C9953828', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify filter controls are available in the page.
        """
        Designer.PageCanvas.FilterGrid.wait_for_text('Category:', time_out=180)
        Designer.PageCanvas.FilterGrid.verify_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], '17')
        Designer._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Select 'Camcorder' in 'Category' filter control.
            Select first three values in Double list control.
        """
        time.sleep(5)
        Designer.PageCanvas.FilterGrid.Control('Category:').Toggle.check()
        time.sleep(20)
        Designer.PageCanvas.FilterGrid.Control('Product Model:').click(location='middle')
        Designer.PageCanvas.FilterGrid.Control('Product Model:').DoubleList.wait_for_text('Values', 15)
        Designer.PageCanvas.FilterGrid.Control('Product Model:').DoubleList.DualListBox.select_options_in_all_options_area(['Canon FS300', 'Canon HFR11', 'Canon XHA1S'])
        Designer.PageCanvas.FilterGrid.Control('Product Model:').DoubleList.DualListBox.AddSelections.click()
        Designer._core_utils.left_click(Designer._utils.validate_and_get_webdriver_object(page_header_css, "Page Header"))
        Designer._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify filter condition applied in the page.
        """
        Designer.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        PieChart.wait_for_text('Revenue', time_out=30)
        PieChart.verify_number_of_risers(1, '18.01')
        PieChart.verify_pie_labels(['Revenue'], '18.02')
        PieChart.verify_total_lables(['34.4M'], '18.03')
        PieChart.verify_riser_color([(1, 'bar_blue')], '18.04')
        PieChart.verify_legend_title(['Product Category'], '18.05')
        PieChart.verify_legend_labels(['Camcorder'], '18.06')
        PieChart.verify_data_lables(['100%'], '18.07')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("19", STEP_19)
