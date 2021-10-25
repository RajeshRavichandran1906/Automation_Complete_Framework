"""---------------------------------------------------------------
Author Name : Prabhakaran.
Automated On : 19-September-2019
---------------------------------------------------------------"""
from common.wftools.designer_chart import Designer_Chart
from common.wftools.page_designer import Design, Run
from common.lib.basetestcase import BaseTestCase

class C8262223_TestClass(BaseTestCase):
    
    def test_C8262223(self):
        
        """
            Class Objects
        """
        designer_chart = Designer_Chart(self.driver)
        pd_design = Design(self.driver)
        pd_run = Run(self.driver)
        
        """
            Common Variables
        """
        case_id = "C8262223"
        preview_chart_css = ".wfc-bc-output-div svg"
        run_chart_css = "#jschart_HOLD_0"
        x_axis_labels = ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        y_axis_labels = ['0', '20K', '40K', '60K', '80K', '100K']
        riser_css = "[class='riser!s0!g3!mbar!']"
        
        """
            STEP 01 : Launch the API to create new Workbook with CAR
            http://machine:port/{alias}/designer?&tool=workbook&master=ibisamp/car&item=IBFS:/WFC/Repository/P292_S28313/G671877
        """
        designer_chart.invoke_designer_chart_using_api('ibisamp/car', 'workbook')
        designer_chart.wait_for_visible_text(preview_chart_css, "Group", designer_chart.chart_long_timesleep)
        
        """
            STEP 02 : Double click "COUNTRY" and "SALES" in Data pane.
        """
        designer_chart.double_click_on_dimension_field("COUNTRY")
        designer_chart.wait_for_visible_text(preview_chart_css, "COUNTRY", designer_chart.chart_short_timesleep)
        
        designer_chart.double_click_on_measures_field("COMP->CARREC->BODY->SALES")
        designer_chart.wait_for_visible_text(preview_chart_css, "SALES", designer_chart.chart_short_timesleep)
        
        """
            STEP 02 - Expected : Check the Query pane and Chart Canvas.
        """
        designer_chart.verify_number_of_risers(preview_chart_css+ " rect", 1, 5, "Step 02.01")
        designer_chart.verify_x_axis_title_in_preview(['COUNTRY'], msg="Step 02.02")
        designer_chart.verify_y_axis_title_in_preview(['SALES'], msg="Step 02.03")
        designer_chart.verify_x_axis_label_in_preview(x_axis_labels, msg="Step 02.04")
        designer_chart.verify_y_axis_label_in_preview(y_axis_labels, msg="Step 02.05")
        designer_chart.verify_chart_color_using_get_css_property_in_preview(riser_css, "bar_blue", msg="Step 02.06")
        
        """
            STEP 03 : Click "New embedded Page" in the Component tab shelf.
        """
        designer_chart.click_new_embedded_page()
        
        """
            STEP 04 : Select "Blank" template.
        """
        pd_design.select_page_designer_template("Blank")
        
        """
            STEP 05 : Drag and drop "Chart 1" from Embedded content into the Page canvas.
        """
        pd_design.drag_embedded_content_to_canvas_section("Chart 1", 1)
        
        """
            STEP 05 - Expected - Check you didn't get asked for EDA credentials and Check the following Page canvas.
        """
        pd_design.verify_containers_title(['Chart 1'], "Step 05.01 : Verify containers")
        pd_design.switch_to_container_frame('Chart 1')
        designer_chart.verify_number_of_risers(run_chart_css + " rect", 1, 5, "Step 05.02")
        designer_chart.verify_x_axis_title_in_preview(['COUNTRY'], msg="Step 05.03", parent_css=run_chart_css)
        designer_chart.verify_y_axis_title_in_preview(['SALES'], msg="Step 05.04", parent_css=run_chart_css)
        designer_chart.verify_x_axis_label_in_preview(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GER...'], msg="Step 05.05", parent_css=run_chart_css)
        designer_chart.verify_y_axis_label_in_preview(y_axis_labels, msg="Step 05.06", parent_css=run_chart_css)
        designer_chart.verify_chart_color_using_get_css_property_in_preview(riser_css, "bar_blue", msg="Step 05.07 ", parent_css=run_chart_css)
        pd_design.switch_to_default_page()
        
        """
            STEP 06 : Click "Save" in toolbar Enter "C8262223" and Click "Save" button.
        """
        pd_design.save_page_from_toolbar(case_id)
        
        """
            STEP 07 : Logout - http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        designer_chart.api_logout()
        
        """
            STEP 08 : Run the saved fex from BIP using API.
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS:/WFC/Repository/P292_S28313/G671877&BIP_item=c8262223
        """
        pd_run.run_page_using_api(case_id)
        designer_chart.wait_for_visible_text(".runner", "Chart", designer_chart.chart_long_timesleep)
        
        """
            STEP 08 - Expected : Check the following Output.
        """
        pd_run.verify_containers_title(['Chart 1'], "Step 08.01 : Verify containers")
        pd_run.switch_to_container_frame('Chart 1')
        designer_chart.verify_number_of_risers(run_chart_css + " rect", 1, 5, "Step 08.02")
        designer_chart.verify_x_axis_title_in_preview(['COUNTRY'], msg="Step 08.03", parent_css=run_chart_css)
        designer_chart.verify_y_axis_title_in_preview(['SALES'], msg="Step 08.04", parent_css=run_chart_css)
        designer_chart.verify_x_axis_label_in_preview(x_axis_labels, msg="Step 08.05", parent_css=run_chart_css)
        designer_chart.verify_y_axis_label_in_preview(y_axis_labels, msg="Step 08.06", parent_css=run_chart_css)
        designer_chart.verify_chart_color_using_get_css_property_in_preview(riser_css, "bar_blue", msg="Step 08.07 ", parent_css=run_chart_css)
        pd_run.switch_to_default_page()
        
        """
            STEP 09 : Logout
        """