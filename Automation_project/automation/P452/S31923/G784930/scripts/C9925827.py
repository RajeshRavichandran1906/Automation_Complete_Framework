"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 22-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.designer_chart import Designer_Chart
from common.wftools.paris_home_page import ParisHomePage

class C9925827_TestClass(BaseTestCase):
    
    def test_C9925827(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Designer = Designer_Chart(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        file_name = "C9925827"
        riser_css = "rect[class^='riser!s{0}!g0']"
        run_chart_css = "#jschart_HOLD_0"
        preview_chart_css = "#arpreview_fdmId_11_f"
        riser_rect_css = preview_chart_css + " rect"
        run_riser_rect_css = run_chart_css + " rect"
        xaxis_title = ["Product Category"]
        xaxis_labels = ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        yaxis_labels = ['0', '100M', '200M', '300M', '400M', '500M', '600M', '700M']
        legends = ['Cost of Goods', 'Gross Profit', 'Revenue']
        
        STEP_01 = """
            STEP 01 : Create a new visualization:
            http://machine.ibi.com:port/alias/designer?&master=retail_samples/wf_retail_lite&item=IBFS:/WFC/Repository/P452_S31923/G784930&tool=framework&startlocation=IBFS:/WFC/Repository
        """
        Designer.invoke_designer_using_api("retail_samples/wf_retail_lite", "mriddev", "mrpassdev")
        HomePage.Home._utils.synchronize_with_visble_text("div.messageTextWrapper", "Drop", 10)
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_01_EXPECTED = """
            STEP 01 - Expected : Verify default chart displayed
        """
        totla_risers = [riser for riser in self.driver.find_elements_by_css_selector("div.output-sample rect[class^='riser']") if riser.is_displayed()]
        HomePage.Home._utils.asequal(25, len(totla_risers), "Step 01.01 : Verify default chart displayed")
        HomePage.Home._utils.capture_screenshot("01 - Expected", STEP_01_EXPECTED, True)

        STEP_02 = """
            STEP 02 : Double click Product Category, Cost of Goods, Gross Profit & Revenue
        """
        Designer.double_click_on_dimension_field("Product->Product,Category")
        HomePage.Home._utils.synchronize_with_visble_text(preview_chart_css, "Product", 45)
        Designer.double_click_on_measures_field("Sales->Cost of Goods")
        HomePage.Home._utils.synchronize_with_visble_text(preview_chart_css, "Cost of Goods", 45)
        Designer.double_click_on_measures_field("Sales->Gross Profit")
        HomePage.Home._utils.synchronize_with_visble_text(preview_chart_css, "Gross Profit", 45)
        Designer.double_click_on_measures_field("Sales->Revenue")
        HomePage.Home._utils.synchronize_with_visble_text(preview_chart_css, "Revenue", 45)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify chart output
        """
        Designer.verify_number_of_risers(riser_rect_css, 3, 7, "Step 02.01")
        Designer.verify_x_axis_title_in_preview(xaxis_title, msg="Step 02.02")
        Designer.verify_x_axis_label_in_preview(xaxis_labels, msg="Step 02.03")
        Designer.verify_y_axis_label_in_preview(yaxis_labels, msg="Step 02.04")
        Designer.verify_legends_in_preview(legends, msg="Step 02.05")
        Designer.verify_chart_color_using_get_css_property_in_preview(riser_css.format(0), "bar_blue1", msg="Step 02.06 ")
        Designer.verify_chart_color_using_get_css_property_in_preview(riser_css.format(1), "pale_green", msg="Step 02.07 ")
        Designer.verify_chart_color_using_get_css_property_in_preview(riser_css.format(2), "dark_green", msg="Step 02.08 ")
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click the Save button, save with name C9925827
        """
        save_btn = self.driver.find_element_by_css_selector("div.btn-save")
        HomePage.Home._core_utils.left_click(save_btn)
        HomePage.ModalDailogs.Resources.wait_for_appear()
        HomePage.ModalDailogs.Resources.Title.enter_text(file_name)
        HomePage.ModalDailogs.Resources.SaveButton.click()
        HomePage.Home._utils.wait_for_page_loads(10, pause_time=3)
        ok_btn = self.driver.find_elements_by_css_selector(".pop-top .ibx-dialog-ok-button")
        (len(ok_btn)>0) and HomePage.Home._core_utils.left_click(ok_btn[0])
        HomePage.ModalDailogs.Resources.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Double click C9925827 in home page
        """
        Designer.api_logout()
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select("P452_S31923->G784930")
        HomePage.Workspaces.ContentArea.double_click_on_file(file_name)
        HomePage.RunWindow.wait_for_visible()
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify Chart
        """
        Designer.verify_number_of_risers(run_riser_rect_css, 3, 7, "Step 04.01")
        Designer.verify_x_axis_title_in_preview(xaxis_title, parent_css=run_chart_css, msg="Step 04.02")
        Designer.verify_x_axis_label_in_preview(xaxis_labels, parent_css=run_chart_css, msg="Step 04.03")
        Designer.verify_y_axis_label_in_preview(yaxis_labels, parent_css=run_chart_css, msg="Step 04.04")
        Designer.verify_legends_in_preview(legends, parent_css=run_chart_css, msg="Step 04.05")
        Designer.verify_chart_color_using_get_css_property_in_preview(riser_css.format(0), "bar_blue1", msg="Step 04.06 ", parent_css=run_chart_css)
        Designer.verify_chart_color_using_get_css_property_in_preview(riser_css.format(1), "pale_green", msg="Step 04.07 ", parent_css=run_chart_css)
        Designer.verify_chart_color_using_get_css_property_in_preview(riser_css.format(2), "dark_green", msg="Step 04.08 ", parent_css=run_chart_css)
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Close Designer
        """
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        Designer.api_logout()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Edit the saved FEX:
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P452_S31923/G784930/c9925827.fex&startlocation=IBFS:/WFC/Repository
        """
        Designer.edit_chart_with_designer_using_api(file_name, "mriddev", "mrpassdev")
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.synchronize_with_visble_text(preview_chart_css, "Revenue", 80)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify chart canvas
        """
        Designer.verify_number_of_risers(riser_rect_css, 3, 7, "Step 06.01")
        Designer.verify_x_axis_title_in_preview(xaxis_title, msg="Step 06.02")
        Designer.verify_x_axis_label_in_preview(xaxis_labels, msg="Step 06.03")
        Designer.verify_y_axis_label_in_preview(yaxis_labels, msg="Step 06.04")
        Designer.verify_legends_in_preview(legends, msg="Step 06.05")
        Designer.verify_chart_color_using_get_css_property_in_preview(riser_css.format(0), "bar_blue1", msg="Step 06.06 ")
        Designer.verify_chart_color_using_get_css_property_in_preview(riser_css.format(1), "pale_green", msg="Step 06.07 ")
        Designer.verify_chart_color_using_get_css_property_in_preview(riser_css.format(2), "dark_green", msg="Step 06.08 ")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Logout - http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.api_logout()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)