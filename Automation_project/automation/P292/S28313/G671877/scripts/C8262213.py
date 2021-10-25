'''
Created on September 25, 2019

@author: Niranjan

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262213
TestCase Name = Create a workbook, edit the Chart, add Page
'''

import unittest
from common.wftools.designer_chart import Designer_Chart
from common.wftools.page_designer import Design
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.lib.global_variables import Global_variables
import time

class C8262213_TestClass(BaseTestCase):
    
    def test_C8262213(self):
        
        """
            Class Objects
        """
        designer_chart = Designer_Chart(self.driver)
        pd_design = Design(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        gv = Global_variables()
        
        """
            Common Variables
        """
        preview_chart_css = ".wfc-bc-output-div svg"
        run_chart_css = "#jschart_HOLD_0"
        riser_css = "[class='riser!s0!g0!mbar!']"
        
        """
            STEP 01 : Launch the API to create new Workbook with WF_RETAIL_LITE
            http://machine:port/{alias}/designer?&tool=workbook&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/P292_S28313/G671877
            Check the Loading cursor is displayed.
            Check default menu in the Component Tab Shelf.
        """
        designer_chart.invoke_designer_chart_using_api('baseapp/wf_retail_lite', 'workbook')
        designer_chart.wait_for_visible_text(preview_chart_css, "Group", designer_chart.chart_long_timesleep)
        
        utils.verify_picture_using_sikuli("C8262213_step1.png", msg = "Step 01.01 : Check default menu in the Component Tab Shelf.")
        
        """
            STEP 02 : Double click "Product,Category" in Data pane.
            Check the Query pane and Chart Canvas.
        """
        designer_chart.double_click_on_dimension_field("Product->Product->Product,Category")
        designer_chart.wait_for_visible_text(preview_chart_css, "Product Category", designer_chart.chart_short_timesleep)
        
        designer_chart.verify_values_in_querybucket("Horizontal", ['Product,Category'], "Step 02.01 : Check the Query pane and Chart Canvas")
        designer_chart.verify_number_of_risers(preview_chart_css + ' rect', 1, 7, msg = "Step 02.02 : Check the Query pane and Chart Canvas")
        designer_chart.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg = "Step 02.03 : Check the Query pane and Chart Canvas")
        designer_chart.verify_x_axis_title_in_preview(['Product Category'], msg = "Step 02.04 : Check the Query pane and Chart Canvas")
        designer_chart.verify_chart_color_using_get_css_property_in_preview(riser_css, "bar_blue", msg = "Step 02.05 : Check the Query pane and Chart Canvas")

        """
            STEP 03 : Click "Save" in toolbar Enter "C8262213" and Click "Save" button.
        """ 
        designer_chart.save_designer_chart_from_toolbar("C8262213")
        
        """
            STEP 04 : Logout.
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        designer_chart.api_logout()
        
        """
            STEP 05 : Reopen the saved fex using API link
            http://machine:port/{alias}/designer?item=IBFS:/WFC/Repository/P292_S28313/G671877/c8262213
            Check the Query pane and Chart Canvas.
        """
        designer_chart.invoke_designer_chart_in_edit_mode_using_api("c8262213", tool = "workbook", mrid = "mrid", mrpass = "mrpass")
        designer_chart.wait_for_visible_text(preview_chart_css, "Product Category", designer_chart.chart_long_timesleep)
        
        designer_chart.verify_values_in_querybucket("Horizontal", ['Product,Category'], "Step 05.01 : Check the Query pane and Chart Canvas")
        designer_chart.verify_number_of_risers(preview_chart_css + ' rect', 1, 7, msg = "Step 05.02 : Check the Query pane and Chart Canvas")
        designer_chart.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg = "Step 05.03 : Check the Query pane and Chart Canvas")
        designer_chart.verify_x_axis_title_in_preview(['Product Category'], msg = "Step 05.04 : Check the Query pane and Chart Canvas")
        designer_chart.verify_chart_color_using_get_css_property_in_preview(riser_css, "bar_blue", msg = "Step 05.05 : Check the Query pane and Chart Canvas")
        """
            STEP 06 : Double click "Cost of Goods" and "Revenue" in Data pane.
            Check the Query pane and Chart Canvas.
        """
        designer_chart.double_click_on_measures_field("Sales->Cost of Goods")
        designer_chart.wait_for_visible_text(preview_chart_css, "Cost of Goods", designer_chart.chart_short_timesleep)
        
        designer_chart.double_click_on_measures_field("Revenue")
        designer_chart.wait_for_visible_text(preview_chart_css, "Revenue", designer_chart.chart_short_timesleep)
        
        designer_chart.verify_values_in_querybucket("Horizontal", ['Product,Category'], "Step 06.01 : Check the Query pane and Chart Canvas")
        designer_chart.verify_values_in_querybucket("Vertical", ['Cost of Goods', 'Revenue'], "Step 06.02 : Check the Query pane and Chart Canvas")
        
        designer_chart.verify_number_of_risers(preview_chart_css + ' rect', 2, 7, msg = "Step 06.03 : Check the Query pane and Chart Canvas")
        designer_chart.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg = "Step 06.04 : Check the Query pane and Chart Canvas")
        designer_chart.verify_x_axis_title_in_preview(['Product Category'], msg = 'Step 06.05 : Check the Query pane and Chart Canvas')
        designer_chart.verify_y_axis_label_in_preview(['0', '100M', '200M', '300M', '400M', '500M', '600M'], msg = "Step 06.06 : Check the Query pane and Chart Canvas")
        designer_chart.verify_legends_in_preview(['Cost of Goods', 'Revenue'], msg = "Step 06.07 : Check the Query pane and Chart Canvas")
        designer_chart.verify_chart_color_using_get_css_property_in_preview("[class='riser!s0!g4!mbar!']", "bar_blue", msg = 'Step 06.08 : Check the Query pane and Chart Canvas')
        designer_chart.verify_chart_color_using_get_css_property_in_preview('[class="riser!s1!g3!mbar!"]', "pale_green", msg = "Step 06.09 : Check the Query pane and Chart Canvas")
        
        """
            STEP 07 : Click "Save" icon in toolbar.
        """
        designer_chart.click_toolbar_item("save")
        time.sleep(7)
        
        """
            STEP 08 : Logout.
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        designer_chart.api_logout()
        
        """
            STEP 09 : Run the saved fex from BIP using API.
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS:/WFC/Repository/P292_S28313/G671877&BIP_item=c8262213
            Check the following Output.
        """
        designer_chart.run_designer_workbook_using_api("c8262213", mrid = "mrid", mrpass = "mrpass")
        core_utils.switch_to_frame(frame_css = "iframe[class='ibx-iframe-frame']")
        designer_chart.wait_for_visible_text("#jschart_HOLD_0", "Product Category")
        
        designer_chart.verify_number_of_risers(run_chart_css + ' rect', 2, 7, msg = "Step 09.01 : Check the following Output.")
        designer_chart.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css = run_chart_css, msg = "Step 09.02 : Check the following Output.")
        designer_chart.verify_x_axis_title_in_preview(['Product Category'], parent_css = run_chart_css, msg = 'Step 09.03 : Check the following Output.')
        designer_chart.verify_y_axis_label_in_preview(['0', '100M', '200M', '300M', '400M', '500M', '600M'], parent_css = run_chart_css, msg = "Step 09.04 : Check the following Output.")
        designer_chart.verify_legends_in_preview(['Cost of Goods', 'Revenue'], parent_css = run_chart_css, msg = "Step 09.05 : Check the following Output.")
        designer_chart.verify_chart_color_using_get_css_property_in_preview("[class='riser!s0!g4!mbar!']", "bar_blue", parent_css = run_chart_css, msg = 'Step 09.06 : Check the following Output.')
        designer_chart.verify_chart_color_using_get_css_property_in_preview('[class="riser!s1!g3!mbar!"]', "pale_green", parent_css = run_chart_css, msg = "Step 09.07 : Check the following Output.")
        core_utils.switch_to_default_content()
        
        """
            STEP 10 : Logout.
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        designer_chart.api_logout()
        
        """
            STEP 11 : Reopen the saved fex using API link.
            http://machine:port/{alias}/designer?item=IBFS:/WFC/Repository/P292_S28313/G671877/c8262213
            Check the Query pane and Chart Canvas.
        """
        designer_chart.invoke_designer_chart_in_edit_mode_using_api("c8262213", tool = "workbook", mrid = "mrid", mrpass = "mrpass")
        designer_chart.wait_for_visible_text(preview_chart_css, "Product Category", designer_chart.chart_long_timesleep)
        
        designer_chart.verify_values_in_querybucket("Horizontal", ['Product,Category'], "Step 11.01 : Check the Query pane and Chart Canvas")
        designer_chart.verify_values_in_querybucket("Vertical", ['Cost of Goods', 'Revenue'], "Step 11.02 : Check the Query pane and Chart Canvas")
        
        designer_chart.verify_number_of_risers(preview_chart_css + ' rect', 2, 7, msg = "Step 11.03 : Check the Query pane and Chart Canvas")
        designer_chart.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg = "Step 11.04 : Check the Query pane and Chart Canvas")
        designer_chart.verify_x_axis_title_in_preview(['Product Category'], msg = 'Step 11.05 : Check the Query pane and Chart Canvas')
        designer_chart.verify_y_axis_label_in_preview(['0', '100M', '200M', '300M', '400M', '500M', '600M'], msg = "Step 11.06 : Check the Query pane and Chart Canvas")
        designer_chart.verify_legends_in_preview(['Cost of Goods', 'Revenue'], msg = "Step 11.07 : Check the Query pane and Chart Canvas")
        designer_chart.verify_chart_color_using_get_css_property_in_preview("[class='riser!s0!g4!mbar!']", "bar_blue", msg = 'Step 11.08 : Check the Query pane and Chart Canvas')
        designer_chart.verify_chart_color_using_get_css_property_in_preview('[class="riser!s1!g3!mbar!"]', "pale_green", msg = "Step 11.09 : Check the Query pane and Chart Canvas")
        
        """
            STEP 12 : Click "New embedded page" in the Component tab shelf.
        """
        designer_chart.click_new_embedded_page()
        
        """
            STEP 13 : Select "Blank template".
        """
        pd_design.select_page_designer_template("Blank")
        
        """
            STEP 14 : Drag and drop "Chart 1" into the Page canvas.
            Check the following Page Canvas.
        """
        pd_design.drag_embedded_content_to_canvas_section("Chart 1", 1)
        
        pd_design.verify_containers_title(['Chart 1'], "Step 14.01 : Check the following Page Canvas")
        pd_design.switch_to_container_frame('Chart 1')
        designer_chart.verify_number_of_risers(run_chart_css + ' rect', 2, 7, msg = "Step 14.02 : Check the following Page Canvas")
        if gv.browser_name == "chrome" or "cr":
            designer_chart.verify_x_axis_label_in_preview(['Accesso...', 'Camcor...', 'Computers', 'Media Pl...', 'Stereo...', 'Televisions', 'Video Pr...'], parent_css = run_chart_css, msg = "Step 14.03 : Check the following Page Canvas")
        else:
            designer_chart.verify_x_axis_label_in_preview(['Access...', 'Camco...', 'Compu...', 'Media...', 'Stereo...', 'Televis...', 'Video P...'], parent_css = run_chart_css, msg = "Step 14.03 : Check the following Page Canvas")
        designer_chart.verify_x_axis_title_in_preview(['Product Category'], parent_css = run_chart_css, msg = 'Step 14.04 : Check the following Page Canvas')
        designer_chart.verify_y_axis_label_in_preview(['0', '100M', '200M', '300M', '400M', '500M', '600M'], parent_css = run_chart_css, msg = "Step 14.05 : Check the following Page Canvas")
        designer_chart.verify_legends_in_preview(['Cost of Goods', 'Revenue'], parent_css = run_chart_css, msg = "Step 14.06 : Check the following Page Canvas")
        designer_chart.verify_chart_color_using_get_css_property_in_preview("[class='riser!s0!g4!mbar!']", "bar_blue", parent_css = run_chart_css, msg = 'Step 14.07 : Check the following Page Canvas')
        designer_chart.verify_chart_color_using_get_css_property_in_preview('[class="riser!s1!g3!mbar!"]', "pale_green", parent_css = run_chart_css, msg = "Step 14.08 : Check the following Page Canvas")
        pd_design.switch_to_default_page()
        
        """
            STEP 15 : Click"Save" icon in toolbar.
        """
        pd_design.click_toolbar_save()
        time.sleep(7)
        
        """
            STEP 16 : Logout.
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        designer_chart.api_logout()
        
        """
            STEP 17 : Reopen the saved fex using API link.
            http://machine:port/{alias}/designer?item=IBFS:/WFC/Repository/P292_S28313/G671877/c8262213
        """
        designer_chart.invoke_designer_chart_in_edit_mode_using_api("c8262213", tool = "workbook", mrid = "mrid", mrpass = "mrpass")
        designer_chart.wait_for_visible_text(preview_chart_css, "Product Category", designer_chart.chart_long_timesleep)
        
        """
            STEP 18 : Click the "Page tab" in the Component tab shelf.
            Check the following Page Canvas.
        """
        designer_chart.select_tab_button("Page")
        designer_chart.wait_for_visible_text("div[class*='pd-page-header']", "Page Heading")
        
        pd_design.verify_containers_title(['Chart 1'], "Step 18.01 : Check the following Page Canvas")
        pd_design.switch_to_container_frame('Chart 1')
        designer_chart.verify_number_of_risers(run_chart_css + ' rect', 2, 7, msg = "Step 18.02 : Check the following Page Canvas")
        if gv.browser_name == "chrome" or "cr":
            designer_chart.verify_x_axis_label_in_preview(['Accesso...', 'Camcor...', 'Computers', 'Media Pl...', 'Stereo...', 'Televisions', 'Video Pr...'], parent_css = run_chart_css, msg = "Step 18.03 : Check the following Page Canvas")
        else:
            designer_chart.verify_x_axis_label_in_preview(['Access...', 'Camco...', 'Compu...', 'Media...', 'Stereo...', 'Televis...', 'Video P...'], parent_css = run_chart_css, msg = "Step 18.03 : Check the following Page Canvas")
        designer_chart.verify_x_axis_title_in_preview(['Product Category'], parent_css = run_chart_css, msg = 'Step 18.04 : Check the following Page Canvas')
        designer_chart.verify_y_axis_label_in_preview(['0', '100M', '200M', '300M', '400M', '500M', '600M'], parent_css = run_chart_css, msg = "Step 18.05 : Check the following Page Canvas")
        designer_chart.verify_legends_in_preview(['Cost of Goods', 'Revenue'], parent_css = run_chart_css, msg = "Step 18.06 : Check the following Page Canvas")
        designer_chart.verify_chart_color_using_get_css_property_in_preview("[class='riser!s0!g4!mbar!']", "bar_blue", parent_css = run_chart_css, msg = 'Step 18.07 : Check the following Page Canvas')
        designer_chart.verify_chart_color_using_get_css_property_in_preview('[class="riser!s1!g3!mbar!"]', "pale_green", parent_css = run_chart_css, msg = "Step 18.08 : Check the following Page Canvas")
        pd_design.switch_to_default_page()
        
        """
            STEP 19 : Logout.
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        designer_chart.api_logout()

if __name__ == '__main__':
    unittest.main()