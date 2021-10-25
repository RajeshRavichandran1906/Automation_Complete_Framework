'''
Created on sept 1, 2018

@author: vpriya
Testcase ID :http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2275858
Testcase Name :Verify to Run and Edit 'Scatter - Profit vs COGs for Products'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C2275858_TestClass(BaseTestCase):

    def test_C2275858(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        medium_wait= 50
        long_wait= 240
        username= 'mrid'
        password= 'mrpass'
        fex_name='Scatter_Profit_vs_COGs_for_Products'
        new_fex_name='Scatter Profit vs COGs for Products1'
        reopen_fex_name='Scatter_Profit_vs_COGs_for_Products1'
        folder_name="Retail_Samples/Charts"
        fex_folder_after_save='SmokeTest/~rsadv'
        
        chart_xaxis_title=['Cost of Goods']
        chart_yaxis_title=['Gross Profit']
        runtime_chart_x_axis_label=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        runtime_chart_y_axis_label=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        expected_title_chart="Gross Profit vs Cost Of Goods for Product Models - Size By Quantity"
        
        preview_chart_y_axis_label=['0','20','40', '60','80', '100','120']
        preview_chart_x_axis_label=['0','40', '80', '120', '160']
        
        legend_list= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Quantity Sold', '5,001', '2,631.5', '262']
        query_field_list=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Gross Profit', 'Horizontal Axis', 'Cost of Goods', 'Marker', 'Size', 'Quantity,Sold', 'Detail', 'Model', 'Color BY', 'Product,Category', 'Tooltip', 'Multi-graph', 'Animate']
        preview_legend_list=['Quantity Sold','1'] 
        expected_tooltip_list=['Cost of Goods:$268,320.00', 'Gross Profit:$458,241.53', 'Quantity Sold:4,472', 'Product Category:Camcorder', 'Model:Sanyo VPCPD2BK']
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css= 'jschart_HOLD_0'
        chart_parent_preview_css= 'pfjTableChart_1'
        chart_color_preview_css="[class='riser!s0!g0!mmarker!']"
        x_axis_title_css="#"+chart_parent_run_css+" text[class^='xaxis'][class$='title']"
        iframe_css= '#resultArea [id^=ReportIframe-]'
        riser_preview_css = "[class*='riser!s']"
        application_css= '#applicationButton'
        no_of_circles="#"+chart_parent_run_css+" svg g circle[class^='riser']"
        riser_css='riser!s1!g8!mmarker!'
        Accessories_riser="circle[class='riser!s0!g2!mmarker!']"
        camcorder_risier="circle[class='riser!s1!g8!mmarker!']"
        computers_risier="circle[class='riser!s2!g4!mmarker!']"
        media_risier="circle[class='riser!s3!g14!mmarker!']"
        Stereo_risier="circle[class='riser!s4!g0!mmarker!']"
        television_risier="circle[class='riser!s5!g5!mmarker!']"
        video_risier="circle[class='riser!s6!g5!mmarker!']"
                
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02:Run the Chart using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Scatter_Profit_vs_COGs_for_Products.fex 
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=no_of_circles, no_of_element=100)
              
        """
        Step 03:Verify the Buuble chart output:
        """
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step 02:00: Verify x-axis title')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 02:01: Verify y-axis title")
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step 02:02: Verify pie Legend List in run window')
        chart_obj.verify_x_axis_label_in_run_window(runtime_chart_x_axis_label, msg="Step 02:03: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(runtime_chart_y_axis_label, msg="Step 02:04: Verify x-axis label")
        chart_obj.verify_chart_title(expected_title_chart, 'run', msg="Step 02:05: Verify chart title")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 100, "Step 02:06: Verify number of chart segments in run window")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(Accessories_riser, "bar_blue", attribute='fill', msg="Step 02:07: Verify accessories color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(camcorder_risier, "pale_green", attribute='fill', msg="Step 02:07: Verify camcorder color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(computers_risier, "dark_green", attribute='fill', msg="Step 02:07: Verify computers color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(media_risier, "pale_yellow_2", attribute='fill', msg="Step 02:07: Verify Media Players color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(Stereo_risier, "brick_red", attribute='fill', msg="Step 02:07: Verify Stereo Systems color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(television_risier, "orange", attribute='fill', msg="Step 02:07: Verify Televisions color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(video_risier, "periwinkle_gray", attribute='fill', msg="Step 02:07: Verify video productions color")
        
        """Step04:Hover over on bubble chart, Verify the tooltip"""
        
        chart_obj.verify_tooltip_in_run_window(riser_css, expected_tooltip_list, "Step04.5", "#"+chart_parent_run_css)
            
        """
        Step 05 :Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(no_of_circles, 100, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 100, "Step 05:01: Verify number of pie segments after browser resize in run window")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(no_of_circles, 100, medium_wait)
                       
        """
        Step 06: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
         
        """
        Step 07: Edit the Chart using the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Scatter_Profit_vs_COGs_for_Products.fex
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(chart_color_preview_css, 1, long_wait)
        
        """
        Step 08: Verify the Chart launched in IA tool
        Verify the following Query panel and Chart Live Preview
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 08:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css="#"+chart_parent_preview_css,msg="Step 08:02: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css="#"+chart_parent_preview_css,msg="Step 08:03: Verify yaxis label")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_preview_css, "bar_blue", parent_css="#"+chart_parent_preview_css,msg="Step 06:04: Verify chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 1, "Step 06:05: Verify number of scatter segments in preview", custom_css=riser_preview_css)
        chart_obj.verify_legends_in_preview(preview_legend_list, parent_css="#"+chart_parent_preview_css, msg="Step 06:06:Verify legends in preview") 
        chart_obj.verify_number_of_circles_in_preview(riser_preview_css, 0, 1, "Step 06:07:Verify number of circles in preview window")  
            
        """
        Step 09: Click Run inside IA tool
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text(x_axis_title_css, 'Cost of Goods', medium_wait)
        
        """ Verify the output: """
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step 09:00: Verify x-axis title')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 09:01: Verify y-axis title")
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step 09:02: Verify pie Legend List in run window')
        chart_obj.verify_x_axis_label_in_run_window(runtime_chart_x_axis_label, msg="Step 09:03: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(runtime_chart_y_axis_label, msg="Step 09:04: Verify x-axis label")
        chart_obj.verify_chart_title(expected_title_chart, "run", msg="Step 09:05: Verify chart title")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 100, "Step 09:06: Verify number of chart segments in run window")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(Accessories_riser, "bar_blue", attribute='fill', msg="Step 09:07: Verify accessories color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(camcorder_risier, "pale_green", attribute='fill', msg="Step 09:08: Verify camcorder color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(computers_risier, "dark_green", attribute='fill', msg="Step 09:09: Verify computers color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(media_risier, "pale_yellow_2", attribute='fill', msg="Step 09:10: Verify Media Players color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(Stereo_risier, "brick_red", attribute='fill', msg="Step 09:11: Verify Stereo Systems color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(television_risier, "orange", attribute='fill', msg="Step 09:12: Verify Televisions color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(video_risier, "periwinkle_gray", attribute='fill', msg="Step 02:07: Verify video productions color")
                
        """
        Step 10: Click IA > Save as> Select "SmokeTest" > MyContent folder > Enter title as "Scatter_Profit_vs_COGs_for_Products.fex" > Click Save
        Verify the Chart is saving under Mycontent folder
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, medium_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
        Step 09: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 10: Edit the saved chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Retail_Samples/Charts&BIP_item=Scatter_Profit_vs_COGs_for_Products.fex=chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(riser_preview_css, 1, long_wait)
        
        """
        Verify it restored successfully without any error
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 06:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css="#"+chart_parent_preview_css,msg="Step 08:02: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css="#"+chart_parent_preview_css,msg="Step 08:03: Verify yaxis label")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_preview_css, "bar_blue", parent_css="#"+chart_parent_preview_css,msg="Step 06:04: Verify chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 1, "Step 06:05: Verify number of scatter segments in preview", custom_css=riser_preview_css)
        chart_obj.verify_legends_in_preview(preview_legend_list, parent_css="#"+chart_parent_preview_css, msg="Step 06:06:Verify legends in preview") 
        chart_obj.verify_number_of_circles_in_preview(riser_preview_css, 0, 1, "Step 06:07:Verify number of circles in preview window")
        
        """
        Step 11 :Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()