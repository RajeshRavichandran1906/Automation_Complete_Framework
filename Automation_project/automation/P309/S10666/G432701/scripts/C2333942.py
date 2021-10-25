"""-------------------------------------------------------------------------------------------
Created on June 26, 2019
@author: Niranjan/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2333942
Test Case Title =  Verify on Hovering x (delete) icon in the bucket should display a hand symbol 
-----------------------------------------------------------------------------------------------"""

import unittest
from common.pages.metadata import MetaData
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.designer_chart import Designer_Insight
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage

class C2333942_TestClass(BaseTestCase):

    def test_C2333942(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        insight = Designer_Insight(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        login = Login(self.driver)
        metadata = MetaData(self.driver)
        main_page = Wf_Mainpage(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        qwerty_tree_css = "#queryTreeWindow"
        chart_css = "#pfjTableChart_1"
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        

        """
            STEP 1 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=baseapp/wf_retail_lite
        """
        chart.invoke_chart_tool_using_api("baseapp/wf_retail_lite")
        chart.wait_for_visible_text(chart_css, "Group 0")
 
        """
            STEP 2 : Double click "Cost of Goods", "Revenue" and "Product, Category"
        """
        metadata.collapse_data_field_section("Filters and Variables")
        chart.double_click_on_datetree_item("Cost of Goods", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Cost of Goods")
        
        chart.double_click_on_datetree_item("Revenue", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Revenue")
        
        chart.double_click_on_datetree_item("Product,Category", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Product,Category")
 
        """
            STEP 3 : Verify following preview displayed
        """
        chart.verify_x_axis_title_in_preview(['Product Category'], msg="step 03.01")
        chart.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="step 03.02")
        chart.verify_y_axis_label_in_preview(['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M'], msg="step 03.03")
        chart.verify_legends_in_preview(['Cost of Goods', 'Revenue'], msg="step 03.04")
        chart.verify_number_of_risers("#pfjTableChart_1 rect", 1, 14, msg="step 03.05")
        chart.verify_chart_color("pfjTableChart_1", "riser!s0!g0!mbar!", "bar_blue", msg="step 03.06 : Verify following preview displayed")
        chart.verify_chart_color("pfjTableChart_1", "riser!s1!g0!mbar!", "pale_green", msg="step 03.07 : Verify following preview displayed")
        
        """
            STEP 4 : Click Format tab > Run with
        """
        chart.select_ia_ribbon_item("Format", "run_with")

        """
            STEP 5 : Click Insight
        """
        chart.select_ia_ribbon_item("Format", "insight")
        
        """
            STEP 6 : Verify preview updated as following
            Expected to see splitting two Y axis in preview
        """
        chart.verify_x_axis_title_in_preview(['Product Category'], msg="step 06.01")
        chart.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="step 06.02")
        chart.verify_y_axis_title_in_preview(['Cost of Goods'], msg="step 06.03")
        chart.verify_y_axis_label_in_preview(['0', '60M', '120M', '180M', '240M'], msg="step 06.04")
        chart.verify_number_of_risers("#pfjTableChart_1 rect", 1, 14, msg="step 06.05")
        chart.verify_y_axis_title_in_preview(['Revenue'], msg="step 06.06", x_or_y_axis_title_css="text[class='y2axis-title']" )
        chart.verify_y_axis_label_in_preview(['0', '87.5M', '175M', '262.5M', '350M'], msg="step 06.07", xyz_axis_label_css="svg > g text[class^='y2axis-labels']")
        chart.verify_chart_color("pfjTableChart_1", "riser!s0!g0!ay1!mbar!", "bar_blue", msg="step 06.08 : Verify preview updated as following")

        """
            STEP 7 : Click on the 'Create Thumbnail' button in the toolbar
        """
        chart.select_ia_toolbar_item("toolbar_thumbnail")
        chart.wait_for_visible_text("#qbThumbNailDlgOkBtn", "OK")

        """
            STEP 8 : Verify Thumbnail > Click OK
        """
        utils.verify_picture_using_sikuli("C2333942_step8.png", msg="STEP 8 : Verify Thumbnail")
        
        button_obj = utils.validate_and_get_webdriver_object("#qbThumbNailDlgOkBtn", "OK button")
        core_utils.python_left_click(button_obj)
        
        """
            STEP 9 : Click "Save" > Save As "C2333942" > Click Save
        """
        chart.save_as_from_application_menu_item("C2333942", target_table_path="P309_S10666->G169735")
 
        """
            STEP 10 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()
 
        """
            STEP 11 : Right-click the saved "C2333942" fex in the Domains tree > Publish
        """        
        login.invoke_home_page('mrid', 'mrpass')
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        
        main_page.right_click_folder_item_and_select_menu("C2333942", "Publish")
        chart.wait_for_visible_text(".file-item-published div[title*='C2333942']", "C2333942")
        
        """
            STEP 12 : Right-click the saved "C2333942" fex in the Domains tree > Select "Properties"
        """
        main_page.right_click_folder_item_and_select_menu("C2333942", "Properties")
        chart.wait_for_visible_text("div[class^='propPage ibx-widget ibx-flexbox']", "Cancel")
 
        """
            STEP 13 : Click "Advanced" Tab
        """
        main_page.select_property_tab_value("Advanced")
        
        """
            STEP 14 : Verify thumbnail saved
            (should match image displayed from IA when thumbnail created)
        """
        utils.verify_picture_using_sikuli("C2333942_step14.png", msg="STEP 14 : Verify thumbnail saved")
        
        """
            STEP 15 : Click cancel
        """
        main_page.select_property_dialog_save_cancel_button("Cancel")
        
        """
            STEP 16 : Right-click the saved "C2333942" fex > Run
        """
        main_page.right_click_folder_item_and_select_menu("C2333942", "Run")
        chart.switch_to_frame(frame_css="iframe[class='ibx-iframe-frame']")
        chart.wait_for_visible_text("#runbox_id", "Cost")
        
        """
            STEP 17 : Verify run time chart displayed as preview and thumbnail
        """
        chart.verify_x_axis_title_in_run_window(['Product Category'], msg="Step 17.01", parent_css="#runbox_id")
        chart.verify_x_axis_label_in_run_window(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="step 17.02",parent_css="#runbox_id")
        chart.verify_y_axis_title_in_run_window(['Cost of Goods'], msg="step 17.03", parent_css="#runbox_id")
        chart.verify_y_axis_label_in_run_window(['0', '60M', '120M', '180M', '240M'], msg="step 17.04", parent_css="#runbox_id")
        chart.verify_number_of_risers("#runbox_id rect", 1, 14, msg="step 17.05")
        chart.verify_y_axis_title_in_run_window(['Revenue'], msg="step 17.06", x_or_y_axis_title_css="text[class='y2axis-title']", parent_css="#runbox_id" )
        chart.verify_y_axis_label_in_run_window(['0', '87.5M', '175M', '262.5M', '350M'], msg="step 17.07", xyz_axis_label_css="svg > g text[class^='y2axis-labels']", parent_css="#runbox_id")
        chart.verify_chart_color("runbox_id", "riser!s0!g0!ay1!mbar!", "bar_blue", msg="step 17.08 : Verify preview updated as following")
        insight.verify_insight_querybox_text_options(['Vertical Axis', 'Group', 'Color'], msg="step 17.09")
        chart.switch_to_default_content()

        """
            STEP 18 :Logout:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()
        
if __name__ == '__main__':
    unittest.main() 