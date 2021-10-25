'''
Created on sept 11, 2018

@author: vishnu priya
Testcase ID :http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2275859
Testcase Name :Verify to Run and Edit 'Scatter - Profit vs COGs for Products(Animation)'
'''
import unittest
from common.lib import utillity 
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C2275859_TestClass(BaseTestCase):

    def test_C2275859(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        utillobj=utillity.UtillityMethods(self.driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        medium_wait= 50
        long_wait= 240
        username= 'mrid'
        password= 'mrpass'
        fex_name='Scatter_Profit_vs_COGs_for_Products_Monthly'
        new_fex_name='Scatter_Profit_vs_COGs_for_Products_Monthly1'
        reopen_fex_name='Scatter_Profit_vs_COGs_for_Products_Monthly1'
        folder_name="Retail_Samples/Charts"
        fex_folder_after_save='SmokeTest/~rsadv'
        
        chart_xaxis_title=['Cost of Goods']
        chart_yaxis_title=['Gross Profit']
        runtime_chart_x_axis_label=['0', '30K', '60K', '90K', '120K', '150K']
        runtime_chart_y_axis_label=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        expected_title_chart="Gross Profit vs Cost Of Goods for Product Models - Size By Quantity"
        
        preview_chart_y_axis_label=['0','20','40', '60','80', '100','120']
        preview_chart_x_axis_label=['0','40', '80', '120', '160']
        
        legend_list= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Quantity Sold', '540', '274.5', '9']
        query_field_list=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Gross Profit', 'Horizontal Axis', 'Cost of Goods', 'Marker', 'Size', 'Quantity,Sold', 'Detail', 'Model', 'Color BY', 'Product,Category', 'Tooltip', 'Multi-graph', 'Animate', 'Sale,Month']
        preview_legend_list=['Quantity Sold','1'] 
        expected_tooltip_list=['Sale Month:1', 'Cost of Goods:$24,780.00', 'Gross Profit:$43,020.43', 'Quantity Sold:413', 'Product Category:Camcorder', 'Model:Sanyo VPCPD2BK']
        expected_label_list=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
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
        computers_risier="circle[class='riser!s2!g2!mmarker!']"
        media_risier="circle[class='riser!s3!g14!mmarker!']"
        Stereo_risier="circle[class='riser!s4!g0!mmarker!']"
        television_risier="circle[class='riser!s5!g5!mmarker!']"
        video_risier="circle[class='riser!s6!g5!mmarker!']"
        slider_css="rect[class='sliderBody']"
        Handle_css="rect[class='sliderHandle']"
        riser_css1="circle[class*='riser!s4!g10!mmarker!']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02:Run the Chart using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Scatter_Profit_vs_COGs_for_Products.fex 
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=no_of_circles, no_of_element=98)
        """ verify the following"""
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step 02:00: Verify x-axis title')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 02:01: Verify y-axis title")
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step 02:02: Verify pie Legend List in run window', legend_length=10)
        chart_obj.verify_x_axis_label_in_run_window(runtime_chart_x_axis_label, msg="Step 02:03: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(runtime_chart_y_axis_label, msg="Step 02:04: Verify x-axis label")
        chart_obj.verify_chart_title(expected_title_chart, 'run', msg="Step 02:05: Verify chart title")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 98, "Step 02:06: Verify number of chart segments in run window")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(Accessories_riser, "bar_blue", attribute='fill', msg="Step 02.07: Verify accessories color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(camcorder_risier, "pale_green", attribute='fill', msg="Step 02.08: Verify camcorder color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(computers_risier, "dark_green", attribute='fill', msg="Step 02.09: Verify computers color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(media_risier, "pale_yellow_2", attribute='fill', msg="Step 02.10: Verify Media Players color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(Stereo_risier, "brick_red", attribute='fill', msg="Step 02.11: Verify Stereo Systems color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(television_risier, "orange", attribute='fill', msg="Step 02.12: Verify Televisions color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(video_risier, "periwinkle_gray", attribute='fill', msg="Step 02.13: Verify video productions color")
         
        """ Step 03: verify the following bubble chart with animation slider """
         
        chart_obj.verify_animate_slider(slider_css, Handle_css,"Step03:verify animate slider button")
         
        """Step04:Hover over on bubble chart, Verify the tooltip"""
         
        chart_obj.verify_tooltip_in_run_window(riser_css, expected_tooltip_list, "Step04.1", "#"+chart_parent_run_css)
             
        """
        Step 05:click play button in animate slider
        """
        chart_obj.verify_animate_start_position()
        risier=self.driver.find_element_by_css_selector(riser_css1)
        actual_loc=risier.location
        chart_obj.click_chart_animate_button()
        utillobj.synchronize_with_number_of_element("rect[class='animateButton']", 1, 60)
        risier=self.driver.find_element_by_css_selector(riser_css1)
        current_loc=risier.location
        utillobj.as_not_equal(current_loc,actual_loc,"Step 05:verify animate button is working")
        chart_obj.verfiy_animate_end_position()
        chart_obj.verify_slider_labels_in_run_window(expected_label_list,"Step 05.01:verify slider labels value")
         
        """
        Step 06 :Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(no_of_circles, 99, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 99, "Step 06:01: Verify number of pie segments after browser resize in run window")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(no_of_circles, 99, medium_wait)
                        
        """
        Step 07: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
          
        """
        Step 08: Edit the Chart using the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Scatter_Profit_vs_COGs_for_Products.fex
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(chart_color_preview_css, 1, long_wait)
        
        """
        Step 09: Verify the following Query panel and Chart Live Preview
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 09:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css="#"+chart_parent_preview_css,msg="Step 09:02: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css="#"+chart_parent_preview_css,msg="Step 09:03: Verify yaxis label")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_preview_css, "bar_blue", parent_css="#"+chart_parent_preview_css,msg="Step 09:04: Verify chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 1, "Step 09:05: Verify number of scatter segments in preview", custom_css=riser_preview_css)
        chart_obj.verify_legends_in_preview(preview_legend_list, parent_css="#"+chart_parent_preview_css, msg="Step 09:06:Verify legends in preview") 
        chart_obj.verify_number_of_circles_in_preview(riser_preview_css, 0, 1, "Step 09:07:Verify number of circles in preview window")  
            
        """
        Step 10: Click Run inside IA tool
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text(x_axis_title_css, 'Cost of Goods', medium_wait)
        
        """ Verify the output: """
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step 10:00: Verify x-axis title')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 10:01: Verify y-axis title")
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step 10:02: Verify pie Legend List in run window', legend_length=10)
        chart_obj.verify_x_axis_label_in_run_window(runtime_chart_x_axis_label, msg="Step 10:03: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(runtime_chart_y_axis_label, msg="Step 10:04: Verify x-axis label")
        chart_obj.verify_chart_title(expected_title_chart, "run", msg="Step 10:05: Verify chart title")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 98, "Step 10:06: Verify number of chart segments in run window")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(Accessories_riser, "bar_blue", attribute='fill', msg="Step 10:07: Verify accessories color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(camcorder_risier, "pale_green", attribute='fill', msg="Step 10:08: Verify camcorder color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(computers_risier, "dark_green", attribute='fill', msg="Step 10:09: Verify computers color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(media_risier, "pale_yellow_2", attribute='fill', msg="Step 10:10: Verify Media Players color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(Stereo_risier, "brick_red", attribute='fill', msg="Step 10:11: Verify Stereo Systems color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(television_risier, "orange", attribute='fill', msg="Step 10:12: Verify Televisions color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(video_risier, "periwinkle_gray", attribute='fill', msg="Step 10:13: Verify video productions color")
    
        """
        Step 11:click on play button on slider
        """
        chart_obj.verify_animate_start_position()
        risier=self.driver.find_element_by_css_selector(riser_css1)
        actual_loc=risier.location
        chart_obj.click_chart_animate_button()
        utillobj.synchronize_with_number_of_element("rect[class='animateButton']", 1, 60)
        risier=self.driver.find_element_by_css_selector(riser_css1)
        current_loc=risier.location
        utillobj.as_not_equal(current_loc,actual_loc,"Step 11:verify animate button is working")
        chart_obj.verify_slider_labels_in_run_window(expected_label_list,"Step 11.01:verify slider labels value")
        
        """
        Step 12: Click IA > Save as> Select "SmokeTest" > MyContent folder > Enter title as "Scatter_Profit_vs_COGs_for_Products.fex" > Click Save
        Verify the Chart is saving under Mycontent folder
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, medium_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
        Step 13: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 14: Edit the saved chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Retail_Samples/Charts&BIP_item=Scatter_Profit_vs_COGs_for_Products.fex=chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(riser_preview_css, 1, long_wait)
        
        """
        Verify it restored successfully without any error
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 14:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css="#"+chart_parent_preview_css,msg="Step 14:02: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css="#"+chart_parent_preview_css,msg="Step 14:03: Verify yaxis label")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_preview_css, "bar_blue", parent_css="#"+chart_parent_preview_css,msg="Step 14:04: Verify chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 1, "Step 14:05: Verify number of scatter segments in preview", custom_css=riser_preview_css)
        chart_obj.verify_legends_in_preview(preview_legend_list, parent_css="#"+chart_parent_preview_css, msg="Step 14:06:Verify legends in preview") 
        chart_obj.verify_number_of_circles_in_preview(riser_preview_css, 0, 1, "Step 14:07:Verify number of circles in preview window")
        
        """
        Step 15 :Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()