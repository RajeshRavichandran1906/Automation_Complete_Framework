'''
Created on Aug 28, 2018

@author: vpriya
Testcase Name : Verify to Run and Edit 'Arc - Sales by Region'
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2275851
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity, core_utility


class C2275851_TestClass(BaseTestCase):
    
    def test_C2275851(self):

        driver = self.driver
        chart_obj=chart.Chart(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        coreutillobj=core_utility.CoreUtillityMethods(driver)
        
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        medium_wait= 50
        long_wait= 120
        username= 'mrid'
        password= 'mrpass'
        fex_name="Sales_by_Region_Arc"
        new_fex_name="Arc - Sales by Region1"
        reopen_fex_name= "Arc_-_Sales_by_Region1"
        folder_name="Retail_Samples/Charts"
        fex_folder_after_save='SmokeTest/~rsadv'
        
        expected_tooltip_list=["South America: 27.3M"]
        expected_tooltip_list1=["North America:610M"]
        expected_datalabel_y=['0','50M','100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M', '500M', '550M','600M']
        expected_datalabel_x=['Oceania','South America','EMEA','North America']
        preview_chart_y_axis_label=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K','40K','45K','50K','55K','60K','65K']
        preview_chart_x_axis_label=['North America']
        query_field_list=['Chart (wf_retail_lite)','Extension specific buckets','Label (DIM)','Store,Business,Region','Value (MES)','Revenue','Multi-graph']
        expected_group_label='27.3M'
        expected_group_label1='610M'
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        run_parent_css= 'jschart_HOLD_0'
        #parent_preview_css= '#TableChart_2'
        Chart_color_custom_css=".chartPanel .group-main path[class*='riser!s0!g0!mbar!']"
        custom_css_y_label=" g text.label"
        custom_css_x_labels=" g.group-labels text"
        #riser_preview_css = "[class*='riser!s']"
        color_css=" .chartPanel .group-main path[class*='riser!s0!g0!mbar!']"
        run_chart_css="#jschart_HOLD_0 .chartPanel .group-main path[class*='riser!s0!g0!mbar!']"
        application_css= '#applicationButton'
        iframe_css= '#resultArea [id^=ReportIframe-]'
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
            Step 01 : Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 02 : Run the Chart using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Sales_by_Region_Arc.fex
        """
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password,run_chart_css=run_chart_css,no_of_element=1)
  
        """
        Step3 :Verify the output:
        """
        utillobj.synchronize_with_number_of_element(custom_css_x_labels,4,long_wait)
        chart_obj.verify_x_axis_label_in_run_window(expected_datalabel_x, xyz_axis_label_css=custom_css_x_labels, msg="Step 03:01: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(expected_datalabel_y, xyz_axis_label_css=custom_css_y_label, msg="Step 03:02: Verify y-axis label")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(color_css, "dark_green2", attribute='fill', msg="Step 03:03: Verify chart colour")
        chart_obj.verify_number_of_chart_segment(run_parent_css, 4, "Step 02:06: Verify number of chart segments in run window")
          
        """
            Step 04 : Hover over anywhere on line chart, Verify the Tooltip
        """
        chart_obj.verify_active_chart_tooltip(run_parent_css,"riser!s0!g3!mbar!",expected_tooltip_list,"Step04.01: Verify tooltip values")
        chart_obj.verify_arc_chart_group_label(run_parent_css,"riser!s0!g3!mbar!","g.group-value>text",expected_group_label,"middle","Step04.01: Verify arc chart group label values", default_move='true')
          
        """
            Step 05 : Resize the browser window and verify it does not throws any error message
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(custom_css_y_label, 13, medium_wait)
        chart_obj.verify_x_axis_label_in_run_window(expected_datalabel_x, parent_css="#" +run_parent_css, xyz_axis_label_css=custom_css_x_labels, msg="Step 05:01: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(expected_datalabel_y, parent_css="#" +run_parent_css, xyz_axis_label_css=custom_css_y_label, msg="Step 05:02: Verify y-axis label")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(custom_css_y_label, 13, medium_wait)
        
        
        """ Step 06: Logout from WebFOCUS BI Portal using the below API Link.

        http://machine:port/ibi_apps/service/wf_security_logout.jsp"""
        
        chart_obj.api_logout()
        
        
        """
            Step 07 : Edit the Chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts/Sales_by_Region_Arc.fex&tool=Chart
             
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(custom_css_y_label, 14, long_wait)
         
        """
            Step 08 :Verify the following Query Pane,Filter Pane and Live Preview
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 07:01 : Verify the Query panel")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, xyz_axis_label_css=custom_css_x_labels,msg="step 8:verify x axis label in live preview")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_y_axis_label, xyz_axis_label_css=custom_css_y_label,msg="step 8.1:verify y axis label in live preview")
         
        """ Step 09:click Run """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(custom_css_y_label, 13,long_wait)
         
        chart_obj.verify_x_axis_label_in_run_window(expected_datalabel_x, parent_css="#" +run_parent_css, xyz_axis_label_css=custom_css_x_labels, msg="Step 09:01: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(expected_datalabel_y, parent_css="#" +run_parent_css, xyz_axis_label_css=custom_css_y_label, msg="Step 09:02: Verify y-axis label")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(Chart_color_custom_css, "dark_green2", attribute='fill', msg="Step 09:03: Verify chart colour")
         
        """ Step 10:Hover on arc verify the values of North America"""
         
        tooltip_css=driver.find_element_by_css_selector("#" +run_parent_css+" [class*='riser!s0!g1!mbar!']")
        utillobj.click_on_screen(tooltip_css,"bottom_middle", y_offset=-10)
        coreutillobj.python_move_to_element(tooltip_css, 'bottom_middle', yoffset=-10, mouse_move_duration=2)
        chart_obj.verify_tooltip_values(run_parent_css,"riser!s0!g1!mbar!",expected_tooltip_list1,"Step 10:01: Verify tooltip values", default_move=True)
        chart_obj.verify_arc_chart_group_label(run_parent_css,"riser!s0!g1!mbar!","g.group-value>text",expected_group_label1,"middle","step 04:01:verify arc chart group label values",default_move=True)
         
        """
            Step 11: Click IA > Save> Select "SmokeTest" folder > Enter title as "Arc - Sales by Region1" > Click Save
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, medium_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
         
        """
            Step 12 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
           
        """
            Step 13 : Edit the saved chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/~rsadv/Sales_by_Region_Arc.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save,fex_name=reopen_fex_name,mrid=username,mrpass=password)
        chart_obj.wait_for_number_of_element(custom_css_y_label, 14, long_wait)
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 07:01 : Verify the Query panel")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, xyz_axis_label_css=custom_css_x_labels,msg="step 13:verify x axis label in live preview")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_y_axis_label, xyz_axis_label_css=custom_css_y_label,msg="step 13.1:verify y axis label in live preview")
         
       
if __name__ == "__main__":
    unittest.main()
        
        
        
        