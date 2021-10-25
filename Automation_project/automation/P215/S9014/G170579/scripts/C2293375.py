'''
Created on Nov 05, 2018

@author: Magesh

Testcase Name : Verify to Run and Interact with 'Product Gross Profit Ring Chart'
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2293375
'''

import unittest, time
from common.lib import utillity
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C2293375_TestClass(BaseTestCase):

    def test_C2293375(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        utillobj = utillity.UtillityMethods(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        USER_NAME='mrdevuser'
        PASSWORD= 'mrdevpass'
        FEX_NAME='Product_Grossprofit_Ringchart'
        FOLDER_NAME='Retail_Samples/InfoApps/Maps'
        expected_label_list1=["11.1M"]
        expected_label_list2=['Gross Profit']
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions']
        medium_wait=90
        sleep_time=10
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css="jschart_HOLD_0"
        PROMPT_SEGMENT_CSS="div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='Business Sub Region:'] span.autop-control"
        iframe_css="#mainPage [name='wfOutput']"
        parent_css_with_tag_name= "#"+chart_parent_run_css
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to WebFocus using "rsdev" user
        http://machine:port/ibi_apps
        Step 02: Run the "Product Gross Profit Ring Chart" using the below API link
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/InfoApps/Maps&BIP_item=Product_Grossprofit_Ringchart.fex
        """
        chart_obj.run_fex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=PROMPT_SEGMENT_CSS, no_of_element=1)
        chart_obj.wait_for_number_of_element(PROMPT_SEGMENT_CSS, 1, medium_wait)
        
        """
        Verify the Auto Prompt window is displayed
        """
        actual_value1=utillobj.validate_and_get_webdriver_object(PROMPT_SEGMENT_CSS, 'Business Region parameter')
        actual_field1=actual_value1.text.strip()
        expected_field1="All Values"
        utillobj.asequal(actual_field1,expected_field1,'Step 2.1 : Verify default amper value for Measures')
        
        """
        Step 03: Click All Values dropdown
        Step 04: Click "Select Values" > Check Canada,East,Europe then click back
        """
        chart_obj.search_and_select_amper_large_value_list_in_run_window('Business Sub Region:', select_value_list=['Canada','East','Europe'])
        
        """
        Step 05: Click Run in autoprompt window
        """
        chart_obj.select_amper_menu_in_run_window('Run')
        time.sleep(sleep_time)
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame(iframe_css)
        total_riser_css_with_tagname=" path[class^='riser!']"
        total_riser_css= "#"+chart_parent_run_css+total_riser_css_with_tagname
        chart_obj.wait_for_number_of_element(total_riser_css, 7, medium_wait)
        
        """
        Verify the following output
        """
        chart_obj.verify_pie_label_in_single_group_in_run_window(expected_label_list1, parent_css=parent_css_with_tag_name, label_css="text[class^='totalLabel']", msg="Step 05:01:Verify pie total label in runtime")
        chart_obj.verify_pie_label_in_single_group_in_run_window(expected_label_list2, parent_css=parent_css_with_tag_name, label_css="text[class^='pieLabel!g']", msg="Step 05:02:Verify pie label in runtime")
        riser =self.driver.find_elements_by_css_selector("path[class^='riser']")
        utillobj.asequal(self, len(riser), 7, msg="Step 05.03:Verify pie chart riser")
#         chart_obj.verify_number_of_pie_segments(parent_css_with_tag_name, 1, 7, msg="Step 05.03:Verify x_axis label in runtime")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class^='riser!s0!g0!mwedge!']", 'bar_blue', parent_css=parent_css_with_tag_name, msg="Step 05.04:Verify chart color")
        chart_obj.verify_legends_in_run_window(expected_legends, parent_css=parent_css_with_tag_name, msg="Step 05.05: Verify legends")
        chart_obj.switch_to_default_content()
        
        """ 
        Step 06: Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()