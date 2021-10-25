'''
Created on Aug 30, 2018

@author: vishnu priya
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/6670257
TestCase_Name : Verify to Run and Edit 'Heatmap - Average Margin Product By Country (Animation)'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity 

class C6670257_TestClass(BaseTestCase):

    def test_C6670257(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        utillobj=utillity.UtillityMethods(self.driver)
        
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        medium_wait= 60
        long_wait= 240
        username= 'mrid'
        password= 'mrpass'
        fex_name='Heatmap_Average_Margin_Product_By_Country_Month'
        new_fex_name='Heatmap Average Margin Product By Country (Animation)1'
        reopen_fex_name= 'Heatmap_Average_Margin_Product_By_Country_Animation_1'
        folder_name="Retail_Samples/Charts"
        fex_folder_after_save='SmokeTest/~rsadv'
        query_field_list= ['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Product,Subcategory', 'Horizontal Axis', 'Store,Country', 'Marker', 'Color', 'AVE.Margin', 'Multi-graph', 'Animate','Sale,Month']
        chart_title_list= ['Store Country', 'Product Subcategory']
        expected_xval_list= ['Belgium', 'Brazil', 'Canada', 'Czech Republic', 'Denmark', 'Germany', 'Hungary', 'Ireland',  'Italy', 'Mexico', 'Netherlands', 'Poland', 'Singapore', 'Spain', 'Sweden', 'Switzerland', 'United Kingdom', 'United States']
        expected_tooltip_list=['Sale Month:1', 'AVE Margin:15.70', 'Product Subcategory:Professional', 'Store Country:Italy']
        expected_yval_list=['Blu Ray', 'Charger', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_preview_xval_list=['Singapore']
        expected_preview_yval_list=['Receivers']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css= 'jschart_HOLD_0'
        chart_parent_preview_css= 'pfjTableChart_1'
        total_riser_css= "svg g.chartPanel rect[class^='riser!s']"
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
        riser_css="riser!s6!g10!mbar!"
        button_css="rect[class='animateButton']"
        first_riser_css="riser!s0!g0!mbar!"
                
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step02:Run the Chart using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Heatmap_Average_Margin_Product_By_Country_Month.fex
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password)
        
        """
        Step03: Hover over anywhere on Heatmap, Verify the tooltip
        """
        
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list,"#"+chart_parent_run_css,msg='Step 03.01')
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 270, "Step 03.02: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, "#"+chart_parent_run_css, msg='Step 03.03')
        chart_obj.verify_z_axis_label_in_run_window(expected_yval_list, "#"+chart_parent_run_css, msg='Step 03.04')
        chart_obj.verify_chart_color(chart_parent_run_css, riser_css, 'salomie1',"Step 03.05: Verify chart color")
        
        """
        Step04:Hover over on Italy(Country), Verify the tooltip
        """
        chart_obj.verify_tooltip_values(chart_parent_run_css,riser_css, expected_tooltip_list, "Step 04.01: verify tooltip value of Italy")
        
        """Step05:Click the "play" button (on the slider),Verify Animate is working"""
        """Step06:Verify animate button is working"""
        chart_obj.verify_animate_start_position(msg="Step 05.01: Verify animate button is in Start position.")
        chart_obj.click_chart_animate_button(button_css)
        utillobj.synchronize_with_visble_text(element_css="rect[class='riser!s6!g4!mbar!']",visble_element_text='rgb(251,253,187)',expire_time=180,text_option='fill')
        actual_color = utillobj.validate_and_get_webdriver_object('#jschart_HOLD_0 rect[class="riser!s6!g4!mbar!"]' , 'chartcolor').value_of_css_property('fill')
        expected_color = 'rgb(251, 253, 187)'
        utillobj.asequal(actual_color, expected_color, "Step 06.01: Verify chart color")
        chart_obj.verfiy_animate_end_position(msg="Step 06.02: Verify animate button is in End position.")

        """
        Step07: Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        utillobj.synchronize_with_number_of_element(total_riser_css, 318, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 318, "Step 07.01: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.maximize_browser()
        utillobj.synchronize_with_number_of_element(total_riser_css, 318, medium_wait)
                
        """
        Step08: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        chart_obj.api_logout()
        
        """
        Step09: Edit the Chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Discount_by_Region.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(total_riser_css, 1, long_wait)
        
        """
        Step10: Verify the Chart launched in IA tool
        Verify the following Query panel and Chart in Live Preview
        """        
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 10.01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list, "#"+chart_parent_preview_css, msg='Step 10.02')
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 1, "Step 10.03: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_run_window(expected_preview_xval_list, "#"+chart_parent_preview_css, msg='Step 10.04')
        chart_obj.verify_z_axis_label_in_run_window(expected_preview_yval_list, "#"+chart_parent_preview_css, msg='Step 10.05')
        chart_obj.verify_chart_color(chart_parent_preview_css, first_riser_css, 'chardonnay_1', "Step 10.06: Verify chart color")
        
        """
        Step11: Click Run inside IA tool
        Verify the output:
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, long_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(total_riser_css, 270, medium_wait)
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list, "#"+chart_parent_run_css, msg='Step 11.01')
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 270, "Step 11.02: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, "#"+chart_parent_run_css, msg='Step 11.03')
        chart_obj.verify_z_axis_label_in_run_window(expected_yval_list, "#"+chart_parent_run_css, msg='Step 11.04')
        chart_obj.verify_chart_color(chart_parent_run_css, riser_css, 'salomie1',"Step 11.05: Verify chart color")
        
        """
        Step12: Click IA > Save> Select "SmokeTest" > Mycontent folder > Enter title as "Heatmap Average Margin Product By Country (Animation)1" > Click Save
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, long_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
        Step13: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 14:Edit the saved chart using "rsadv" with the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/~rsadv/Heatmap_Average_Margin_Product_By_Country_Animation_1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(total_riser_css, 1, long_wait)
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 14.01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list, "#"+chart_parent_preview_css, msg='Step 14.02')
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 1, "Step 14.03: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_run_window(expected_preview_xval_list, "#"+chart_parent_preview_css, msg='Step 14.04')
        chart_obj.verify_z_axis_label_in_run_window(expected_preview_yval_list, "#"+chart_parent_preview_css, msg='Step 14.05')
        chart_obj.verify_chart_color(chart_parent_preview_css, first_riser_css, 'chardonnay_1', "Step 14.06: Verify chart color")
        
        """
        Step15: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        '''Will be acheived in teardown'''
#         report_obj.api_logout()

if __name__ == "__main__":
    unittest.main()