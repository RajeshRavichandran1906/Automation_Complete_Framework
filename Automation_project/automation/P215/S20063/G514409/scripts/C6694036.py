'''
Created on Sep 17, 2018

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/6694036&group_by=cases:section_id&group_order=asc&group_id=514409
TestCase Name : Verify to Run and Edit 'Profit Comparison by Gender'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C6694036_TestClass(BaseTestCase):

    def test_C6694036(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        medium_wait= 60
        long_wait= 300
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='M_v_F_Profit_Area'
        new_fex_name='M_v_F_Profit_Area1'
        folder_name='Retail_Samples/Portal/Large_Widgets'
        fex_folder_after_save='SmokeTest/~rsadv'
        
        query_field_list=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Gender', 'Axis', 'Vertical Axis', 'Gross Profit', 'Horizontal Axis', 'Sale,Year/Quarter', 'Marker', 'Color BY', 'Product,Category', 'Tooltip', 'Multi-graph', 'Animate'] 
        expected_x_axis_labels=['2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4', '2017 Q1', '2017 Q2', '2017 Q3', '2017 Q4', '2018 Q1', '2018 Q2', '2018 Q3', '2018 Q4', '2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4', '2017 Q1', '2017 Q2', '2017 Q3', '2017 Q4', '2018 Q1', '2018 Q2', '2018 Q3', '2018 Q4']
        expected_y_axis_labels=['0','4M','8M','12M','16M','20M']
        expected_x_axis_top_level_title=['Gender : Sale Year/Quarter']
        expected_x_axis_top_level_labels=['F', 'M']
        expected_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        
        preview_expected_x_axis_labels=['2014 Q1', '2014 Q1']
        preview_expected_y_axis_labels=['0', '2,000', '4,000', '6,000', '8,000', '10,000']
        
        expected_y_axis_title=['Gross Profit']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css= 'jschart_HOLD_0'
        chart_parent_preview_css= 'TableChart_2'
        total_riser_css= "svg g [class^='riser!s']"
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
        riser_css="[class='riser!s0!g0!marea!r0!c0!']"
        
        no_of_risers="#"+chart_parent_run_css+" "+total_riser_css
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02: Run the Chart using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Large_Widgets&BIP_item=M_v_F_Profit_Area.fex
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=no_of_risers, no_of_element=14)
        
        """
            Verify the output
        """
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title, msg="Step 02:01:Verify y axis title")
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels,xyz_axis_label_length=4, msg="Step 02:02:Verify x_axis labels")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, msg="Step 02:03:Verify x_axis labels")
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_top_level_title, xyz_axis_label_css="[class='colHeader-label!']", msg="Step 02:04:Verify x-axis top level title at runtime")
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_top_level_labels, xyz_axis_label_css="[class^='colLabel!']", msg="Step 02:05: Verify x-axis top level labels at runtime")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 02:06: Verify expected legend list")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(riser_css, "bar_blue", msg="Step 02:07:Verify area chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 350, "Step 02:08:Verify chart segments in the area chart")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" path", 2, 7, msg="Step 02:09:Verify number of risers")
         
        """
        Step 03: Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(total_riser_css, 14, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 14, "Step 03: Verify number of riser segments in run window", custom_css=total_riser_css)
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(total_riser_css, 14, medium_wait)
                 
        """
        Step 04: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 05: Edit the Chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Large_Widgets/M_v_F_Profit_Area.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(total_riser_css, 14, long_wait)
        
        """
        Verify the Chart launched in IA tool
        """
        chart_obj.verify_y_axis_title_in_preview(expected_y_axis_title, parent_css="#"+chart_parent_preview_css,msg="Step 05:01:Verify y-axis title")
        chart_obj.verify_x_axis_label_in_preview(preview_expected_x_axis_labels, parent_css="#"+chart_parent_preview_css, msg='Step 05:03 Verify preview x_axis labels in preview')
        chart_obj.verify_y_axis_label_in_preview(preview_expected_y_axis_labels, parent_css="#"+chart_parent_preview_css, msg='Step 05:04 Verify preview y_axis labels in preview')
        chart_obj.verify_legends_in_preview(expected_legend_list, parent_css="#"+chart_parent_preview_css, msg="Step 05:05:Verify legends in preview")
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 05:06: Verify the Query panel in preview")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 14, "Step 05:07: Verify number of chart segements in preview", custom_css=total_riser_css)
        chart_obj.verify_number_of_risers("#"+chart_parent_preview_css+" path", 2, 7, msg="Step 05:08: Verify number of risers")
        chart_obj.verify_x_axis_label_in_preview(expected_x_axis_top_level_title, parent_css="#"+chart_parent_preview_css, xyz_axis_label_css="[class='colHeader-label!']",msg="Step 05:09:Verify x-axis title in top level")
        chart_obj.verify_x_axis_label_in_preview(expected_x_axis_top_level_labels, parent_css="#"+chart_parent_preview_css, xyz_axis_label_css="[class^='colLabel!']", msg="Step 05:10: Verify x-axis top level labels at preview")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(riser_css, "bar_blue", parent_css="#"+chart_parent_preview_css, msg="Step 05:11: Verify area chart color at preview")
        
        """
        Step 06: Click Run
        """ 
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(total_riser_css, 14, long_wait)
        
        """ Verify the output: """
        
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title, msg="Step 06:01:Verify y axis title")
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, xyz_axis_label_length=4, msg="Step 06:02:Verify x_axis labels")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, msg="Step 06:03:Verify x_axis labels")
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_top_level_title, xyz_axis_label_css="[class='colHeader-label!']", msg="Step 06:04:Verify x-axis top level title at runtime")
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_top_level_labels, xyz_axis_label_css="[class^='colLabel!']", msg="Step 06:05: Verify x-axis top level labels at runtime")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 06:06: Verify expected legend list")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(riser_css, "bar_blue", msg="Step 06:07: Verify area chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 350, "Step 06:08: Verify chart segments in the area chart")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" path", 2, 7, msg="Step 06:09: Verify number of risers")
               
        """
        Step 07: Click IA > Save as> Select "SmokeTest" > My Content folder > Enter title as "M v F Profit Area1" > Click Save
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, medium_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
        Step 08: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 09: Edit the saved chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/M_v_F_Profit_Area1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=new_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(total_riser_css, 14, long_wait)
        
        """
        Verify it restored successfully without any error
        """ 
        chart_obj.verify_y_axis_title_in_preview(expected_y_axis_title, parent_css="#"+chart_parent_preview_css,msg="Step 09:01:Verify y-axis title")
        chart_obj.verify_x_axis_label_in_preview(preview_expected_x_axis_labels, parent_css="#"+chart_parent_preview_css, msg='Step 09:03 Verify preview x_axis labels in preview')
        chart_obj.verify_y_axis_label_in_preview(preview_expected_y_axis_labels, parent_css="#"+chart_parent_preview_css, msg='Step 09:04 Verify preview y_axis labels in preview')
        chart_obj.verify_legends_in_preview(expected_legend_list, parent_css="#"+chart_parent_preview_css, msg="Step 09:05:Verify legends in preview")
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 09:06: Verify the Query panel in preview")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 14, "Step 09:07: Verify number of chart segements in preview", custom_css=total_riser_css)
        chart_obj.verify_number_of_risers("#"+chart_parent_preview_css+" path", 2, 7, msg="Step 09:08: Verify number of risers")
        chart_obj.verify_x_axis_label_in_preview(expected_x_axis_top_level_title, parent_css="#"+chart_parent_preview_css, xyz_axis_label_css="[class='colHeader-label!']",msg="Step 09:09:Verify x-axis title in top level")
        chart_obj.verify_x_axis_label_in_preview(expected_x_axis_top_level_labels, parent_css="#"+chart_parent_preview_css, xyz_axis_label_css="[class^='colLabel!']", msg="Step 09:10: Verify x-axis top level labels at preview")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(riser_css, "bar_blue", parent_css="#"+chart_parent_preview_css, msg="Step 09:11: Verify area chart color at preview")
        
        """
        Step 10: Logout from WebFOCUS BI Portal using the below API Link.
        http:/machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        '''Will be acheived in teardown'''


if __name__ == "__main__":
    unittest.main()