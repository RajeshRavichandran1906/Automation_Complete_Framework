'''
Created on Nov 2, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2293377
Testcase Name : Verify to Run 'Top 5 Stores Chart'

'''
import unittest
from common.wftools import report
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity

class C2293377_TestClass(BaseTestCase):

    def test_C2293377(self):
        
        driver = self.driver
        
        report_obj=report.Report(driver)
        chart_obj=chart.Chart(driver)
        utillobj=utillity.UtillityMethods(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        LONG_WAIT=180
        
        USERNAME= 'mrdevuser'
        PASSWORD= 'mrdevpass'
        FEX_NAME='Top_5_Stores_Chart'
        FOLDER_NAME='Retail_Samples/InfoApps/Maps'
         
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        
        RUN_BUTTON_CSS=".autop-pane div[class^='autop-navbar'] a[title^='Run']"
        chart_parent_run_css="jschart_HOLD_0"
        total_riser_css= "[class^='riser!s']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
            Step 1: Sign to WebFocus using "rsdev" user
            http://machine:port/ibi_apps
            Run the report using the below API link
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/InfoApps/Maps&BIP_item=Top_5_Store_Chart.fex
        """
        chart_obj.run_fex_using_api_url(FOLDER_NAME, fex_name=FEX_NAME, mrid=USERNAME, mrpass=PASSWORD, run_chart_css=RUN_BUTTON_CSS)
        
        """
            Verify the Auto Prompt window is displayed
        """
        css="#promptPanel .autop-title"
        utillobj.verify_object_visible(css, True, "Step 1: Verify Autoprompt is displayed.")
        
        """
            Step 3: Click Run in autoprompt window
        """
        
        report_obj.run_auto_prompt_report()
        iframe_css="[name='wfOutput']"
        report_obj.wait_for_number_of_element(iframe_css, 1, LONG_WAIT)
        report_obj.switch_to_frame(frame_css=iframe_css)
        
        """
            Verify the following output
        """
        y_axis_title_list= ['Revenue']
        expected_xaxis_list= ['New York', 'Houston', 'Chicago', 'Detroit', 'Atlanta']
        expected_yaxis_list= ['0', '4M', '8M', '12M', '16M', '20M', '24M', '28M']
        legend_list= ['Gross Profit', '2.3M', '3.6M', '4.8M', '6M', '7.3M']
        riser_css= "riser!s0!g4!mbar"
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0", "Revenue", LONG_WAIT)
        chart_obj.verify_y_axis_title_in_run_window(y_axis_title_list, "#"+chart_parent_run_css, msg='Step 03:1')
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 5, "Step 03:2: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_run_window(expected_xaxis_list, "#"+chart_parent_run_css, msg='Step 03:3')
        chart_obj.verify_y_axis_label_in_run_window(expected_yaxis_list, "#"+chart_parent_run_css, msg='Step 03:4')
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step 03:5: Verify pie Legend List in run window')
        chart_obj.verify_chart_color(chart_parent_run_css, riser_css, 'persian_red', "Step 03:6: Verify chart color")
        
        """
            Step 4: Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """



if __name__ == "__main__":
    unittest.main()
    