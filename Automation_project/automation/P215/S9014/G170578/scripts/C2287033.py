'''
Created on Oct 29, 2018

@author: Magesh

Testcase Name : Verify to Run and Interact with 'Prompt Chart'
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287033
'''

import unittest, time
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity

class C2287033_TestClass(BaseTestCase):

    def test_C2287033(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        utillobj = utillity.UtillityMethods(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        USER_NAME='mrdevid'
        PASSWORD= 'mrdevpass'
        FEX_NAME='PromptChart'
        FOLDER_NAME='Retail_Samples/InfoApps/Customizable_Chart'
        expected_x_axis_labels=['EMEA']
        expected_y_axis_labels=['0', '20M', '40M', '60M', '80M', '100M']
        expected_x_axis_title_list=['Store Business Region']
        expected_y_axis_title_list=['Revenue']
        expected_legends=['Gender', 'F', 'M']
        medium_wait=140
        sleep_time=10
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css="jschart_HOLD_0"
        PROMPT_SEGMENT_CSS="#promptPanel [class='autop-pane']"
        iframe_css="#mainPage [name='wfOutput']"
        parent_css_with_tag_name= "#"+chart_parent_run_css+" rect"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to WebFocus using "rsdev" user
        http://machine:port/ibi_apps
        Step 02: Run the Chart using the below API link
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/InfoApps/Customizable_Chart&BIP_item=PromptChart.fex
        """
        chart_obj.run_fex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=PROMPT_SEGMENT_CSS, no_of_element=1)
        chart_obj.wait_for_number_of_element(PROMPT_SEGMENT_CSS, 1, medium_wait)
        
        """
        Verify the following Auto Prompt window
        """
        actual_css1="div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='Measures'] span"
        actual_value1=utillobj.validate_and_get_webdriver_object(actual_css1, 'Measures parameter')
        actual_field1=actual_value1.text.strip()
        
        actual_css2="div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='ColorBy'] span"
        actual_value2=utillobj.validate_and_get_webdriver_object(actual_css2, 'ColorBy parameter')
        actual_field2=actual_value2.text.strip()
        
        
        actual_css3="div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='XAxis'] span"
        actual_value3=utillobj.validate_and_get_webdriver_object(actual_css3, 'XAxis parameter')
        actual_field3=actual_value3.text.strip()
        
        actual_css4="div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='Business Region:'] span"
        actual_value4=utillobj.validate_and_get_webdriver_object(actual_css4, 'Business Region parameter')
        actual_field4=actual_value4.text.strip()
        
        expected_field1="Gross Profit"
        expected_field2="Product Category"
        expected_field3="Sale Year"
        expected_field4="All Values"
        
        utillobj.asequal(actual_field1,expected_field1,'Step 2.1 : Verify default amper value for Measures')
        utillobj.asequal(actual_field2,expected_field2,'Step 2.2 : Verify default amper value for ColorBy')
        utillobj.asequal(actual_field3,expected_field3,'Step 2.3 : Verify default amper value for XAxis')
        utillobj.asequal(actual_field4,expected_field4,'Step 2.4 : Verify default amper value for Business Region')
        
        """
        Step 03: Click 'Gross Profit' dropdown under Measure > Select "Revenue"
        """
        chart_obj.select_amper_small_value_list_in_run_window('Measures', select_value_list=['Revenue'])
        
        """
        Step 04: Click 'Product Category' dropdown under Color BY > Select "Gender"
        """
        chart_obj.select_amper_small_value_list_in_run_window('ColorBy', select_value_list=['Gender'])
        
        """
        Step 05: Click 'Sale Year' dropdown under X-axis > Select "Store Business Region"
        """
        chart_obj.select_amper_small_value_list_in_run_window('XAxis', select_value_list=['Store Business Region'])
        
        """
        Step 06: Click 'Business Region' dropdown Select "EMEA" > Click Close(X)
        """
        chart_obj.select_amper_small_value_list_in_run_window('Business Region:', select_value_list=['EMEA'])
        
        """
        Step 07: Choose the following date "March 14, 2012"
                 Choose the following date "March 11, 2015"
        """
        date_css1="div[class$='autop-amper-TIME_DATE'] div[class*='ui-input-text'] input[class*='hasDatepicker']"
        Date_picker_css="div.ui-datepicker"
        date_value=utillobj.validate_and_get_webdriver_object(date_css1, 'Date element1')
        date_value.click()
        chart_obj.wait_for_number_of_element(Date_picker_css, 1, medium_wait)
        
        chart_obj.select_month_in_calendardatepicker_dialog_in_run_window('Mar')
        chart_obj.select_year_in_calendardatepicker_dialog_in_run_window('2012')
        chart_obj.select_date_in_calendardatepicker_dialog_in_run_window('14')
        
        time.sleep(sleep_time)
        date_css1="div[class$='autop-amper-TIME_DATE2'] div[class*='ui-input-text'] input[class*='hasDatepicker']"
        Date_picker_css="div.ui-datepicker"
        date_value=utillobj.validate_and_get_webdriver_object(date_css1, 'Date element2')
        date_value.click()
        chart_obj.wait_for_number_of_element(Date_picker_css, 1, medium_wait)
        
        chart_obj.select_month_in_calendardatepicker_dialog_in_run_window('Mar')
        chart_obj.select_year_in_calendardatepicker_dialog_in_run_window('2015')
        chart_obj.select_date_in_calendardatepicker_dialog_in_run_window('11')
        
        """
        Verify the following selections
        """
        actual_css1="div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='Measures'] span"
        actual_value1=utillobj.validate_and_get_webdriver_object(actual_css1, 'Measures parameter')
        actual_field1=actual_value1.text.strip()
        
        actual_css2="div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='ColorBy'] span"
        actual_value2=utillobj.validate_and_get_webdriver_object(actual_css2, 'ColorBy parameter')
        actual_field2=actual_value2.text.strip()
        
        
        actual_css3="div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='XAxis'] span"
        actual_value3=utillobj.validate_and_get_webdriver_object(actual_css3, 'XAxis parameter')
        actual_field3=actual_value3.text.strip()
        
        actual_css4="div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='Business Region:'] span"
        actual_value4=utillobj.validate_and_get_webdriver_object(actual_css4, 'Business Region parameter')
        actual_field4=actual_value4.text.strip()
        
        expected_field1="Revenue"
        expected_field2="Gender"
        expected_field3="Store Business Region"
        expected_field4="EMEA"
        
        utillobj.asequal(actual_field1,expected_field1,'Step 7.1 : Verify default amper value for Measures')
        utillobj.asequal(actual_field2,expected_field2,'Step 7.2 : Verify default amper value for ColorBy')
        utillobj.asequal(actual_field3,expected_field3,'Step 7.3 : Verify default amper value for XAxis')
        utillobj.asequal(actual_field4,expected_field4,'Step 7.4 : Verify default amper value for Business Region')
        
        """
        Step 08: Click 'Run'
        """
        chart_obj.select_amper_menu_in_run_window('Run')
        time.sleep(sleep_time)
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame(iframe_css)
        total_riser_css_with_tagname=" rect[class^='riser!']"
        total_riser_css= "#"+chart_parent_run_css+total_riser_css_with_tagname
        chart_obj.wait_for_number_of_element(total_riser_css, 2, medium_wait)
        
        """
        Verify the following output
        """
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, msg="Step 08:01: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, msg="Step 08:02: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, msg="Step 08:03: Verify x_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 08:04: Verify y_axis title at runtime")
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 2, 1, msg="Step 08:05: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mbar!', 'bar_blue', "Step 08:06: Verify chart color")
        chart_obj.verify_legends_in_run_window(expected_legends, msg="Step 08:07: Verify legends")
        chart_obj.switch_to_default_content()
        
        """ 
        Step 09: Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()