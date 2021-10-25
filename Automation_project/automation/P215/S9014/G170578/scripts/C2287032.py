'''
Created on Oct 31, 2018

@author: Magesh

Testcase Name : Verify to Run and Interact with 'Product Sales Analysis' html file
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287032
'''

import unittest, time
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity, javascript

class C2287032_TestClass(BaseTestCase):
    
    def test_C2287032(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        utillobj = utillity.UtillityMethods(driver)
        javascript_obj = javascript.JavaScript(driver)
        
        def verify_text(expected_text_list_1):
            text_elems=self.driver.find_elements_by_css_selector("td")
            text= javascript_obj.get_elements_text(text_elems)        
            actual_text_items=[e.strip().replace(' ','').replace('\n','') for e in text if e!='']
            for i in expected_text_list_1:
                for j in actual_text_items:
                    if i in j:
                        status = True
                        break
                    else:
                        status=False
                if status == False:
                    break
            utillobj.asequal(True, status, "Step13.5: Verify text present in DeferredReportStatus window")
            
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        USER_NAME='mrdevid'
        PASSWORD= 'mrdevpass'
        FEX_NAME='Product_Sales_Analysis'
        FOLDER_NAME='Retail_Samples/InfoApps/Customizable_Chart'
        expected_x_axis_labels=['2013', '2014', '2015', '2016', '2017', '2018']
        expected_y_axis_labels=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        expected_x_axis_title_list=['Sale Year']
        expected_y_axis_title_list=['Gross Profit']
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions']
        medium_wait=90
        sleep_time=10
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css="jschart_HOLD_0"
        RISER_CSS="#jschart_HOLD_0 rect[class^='riser']"
        PROMPT_SEGMENT_CSS='form.IBI_ReportControlPanel'
        iframe_css="[id^='chart1']"
        parent_css_with_tag_name= "#"+chart_parent_run_css+" rect"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to WebFocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02: Run html file using below API link:
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/InfoApps/Customizable_Chart&BIP_item=Product_Sales_Analysis.htm
        """
        chart_obj.run_htmlfex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=PROMPT_SEGMENT_CSS, no_of_element=1)
        time.sleep(sleep_time)
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame(iframe_css)
        chart_obj.wait_for_number_of_element(RISER_CSS, 42, medium_wait)
        
        """
        Verify the following output
        """
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, msg="Step 02:01: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, msg="Step 02:02: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, msg="Step 02:03: Verify x_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 02:04: Verify y_axis title at runtime")
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 7, 6, msg="Step 02:05: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mbar!', 'bar_blue', "Step 02:06: Verify chart color")
        chart_obj.verify_legends_in_run_window(expected_legends, msg="Step 02:07: Verify legends")
        chart_obj.switch_to_default_content()
        
        """
        Step 03: Click 'Gross Profit' dropdown under Measure > Select "Cost of Goods"
        """
        chart_obj.select_combo_item_in_infoapps_left_panel('Measures', "Cost of Goods")
        
        """
        Step 04: Click 'Product Category' dropdown under Color BY > Select "Sale Quarter"
        """
        chart_obj.select_combo_item_in_infoapps_left_panel('ColorBY', "Sale Quarter")
        
        """
        Step 05: Click 'Sale Year' dropdown under X-axis > Select "Store Business Region"
        """
        chart_obj.select_combo_item_in_infoapps_left_panel('XAxis', "Store Business Region")
        
        """
        Step 06: Select 'North America' Region under Filters
        """
        chart_obj.select_listbox_item_in_infoapps_left_panel(1, item_list=['North America'])
        
        """
        Step 07: Click From date calendar icon choose the following date "2013/01/10"
        """
        time.sleep(sleep_time)
        calendar_icon_css="#form1 #calendar1 [class*='IBI_btn-calendar']"
        Date_picker_css="div.ui-datepicker"
        calendar_icon_obj=utillobj.validate_and_get_webdriver_object(calendar_icon_css, 'From date calendar icon')
        calendar_icon_obj.click()
        chart_obj.wait_for_number_of_element(Date_picker_css, 1, medium_wait)
        chart_obj.select_month_in_calendardatepicker_dialog_in_run_window('January')
        chart_obj.select_year_in_calendardatepicker_dialog_in_run_window('2013')
        chart_obj.select_date_in_calendardatepicker_dialog_in_run_window('10')
        
        """
        Step 08: Click To date calendar icon choose the following date "2017/07/13"
        """
        time.sleep(sleep_time)
        calendar_icon_css="#form1 #calendar2 [class*='IBI_btn-calendar']"
        Date_picker_css="div.ui-datepicker"
        calendar_icon_obj=utillobj.validate_and_get_webdriver_object(calendar_icon_css, 'To date calendar icon')
        calendar_icon_obj.click()
        chart_obj.wait_for_number_of_element(Date_picker_css, 1, medium_wait)
        chart_obj.select_month_in_calendardatepicker_dialog_in_run_window('July')
        chart_obj.select_year_in_calendardatepicker_dialog_in_run_window('2017')
        chart_obj.select_date_in_calendardatepicker_dialog_in_run_window('13')
        
        """Verify the following selections"""
        time.sleep(sleep_time)
        measures_combobox_css='form.IBI_ReportControlPanel > select#combobox1'
        utillobj.verify_dropdown_value(measures_combobox_css, expected_default_selected_value="Cost of Goods", default_selection_msg="Step 08.1: Verify Cost of Goods is selected under Measure")
        
        ColorBY_combobox_css='form.IBI_ReportControlPanel > select#combobox2'
        utillobj.verify_dropdown_value(ColorBY_combobox_css, expected_default_selected_value="Sale Quarter", default_selection_msg="Step 08.2: Verify Sale Quarter is selected under ColorBY")
        
        XAxis_combobox_css='form.IBI_ReportControlPanel > select#combobox3'
        utillobj.verify_dropdown_value(XAxis_combobox_css, expected_default_selected_value="Store Business Region", default_selection_msg="Step 08.3: Verify Store Business Region is selected under XAxis")
        
        Business_Region_listbox_css='form.IBI_ReportControlPanel > select#listbox1'
        utillobj.verify_dropdown_value(Business_Region_listbox_css, expected_default_selected_value="North America", default_selection_msg="Step 08.4: Verify North America Region is selected under Business Region")
        
        from_date_css="#form1 #calendar1 input"
        from_date_obj=utillobj.validate_and_get_webdriver_object(from_date_css, 'From date in Calender1')
        actual_from_date=from_date_obj.get_attribute('value')
        expected_from_date="2013/01/10"
        utillobj.asequal(actual_from_date,expected_from_date,'Step 8.5: Verify From date in Calender1')
        
        to_date_css="#form1 #calendar2 input"
        to_date_obj=utillobj.validate_and_get_webdriver_object(to_date_css, 'To date in Calender2')
        actual_to_date=to_date_obj.get_attribute('value')
        expected_to_date="2017/07/13"
        utillobj.asequal(actual_to_date,expected_to_date,'Step 8.6: Verify To date in Calender2')
        
        """
        Step 09: Click 'Run' under Run Options
        """
        chart_obj.click_run_option_button('run')
        time.sleep(sleep_time)
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame(iframe_css)
        chart_obj.wait_for_number_of_element(RISER_CSS, 4, medium_wait)
        
        """
        Verify the following output
        """
        expected_x_axis_labels1=['North America']
        expected_y_axis_labels1=['0', '40M', '80M', '120M', '160M', '200M']
        expected_x_axis_title_list1=['Store Business Region']
        expected_y_axis_title_list1=['Cost of Goods']
        expected_legends1=['Sale Quarter', '1', '2', '3', '4']
        
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels1, msg="Step 09:01: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels1, msg="Step 09:02: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list1, msg="Step 09:03: Verify x_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list1, msg="Step 09:04: Verify y_axis title at runtime")
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 4, 1, msg="Step 09:05: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mbar!', 'bar_blue', "Step 09:06: Verify chart color")
        chart_obj.verify_legends_in_run_window(expected_legends1, msg="Step 09:07: Verify legends")
        chart_obj.switch_to_default_content()
        
        """
        Step 10: Click 'Reset' button under Run Options
        """
        chart_obj.click_run_option_button('reset')
        time.sleep(sleep_time)
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame(iframe_css)
        chart_obj.wait_for_number_of_element(RISER_CSS, 42, medium_wait)
        
        """
        Verify the html file is restored back to original
        """
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, msg="Step 10:01: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, msg="Step 10:02: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, msg="Step 10:03: Verify x_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 10:04: Verify y_axis title at runtime")
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 7, 6, msg="Step 10:05: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mbar!', 'bar_blue', "Step 10:06: Verify chart color")
        chart_obj.verify_legends_in_run_window(expected_legends, msg="Step 10:07: Verify legends")
        chart_obj.switch_to_default_content()
        
        """
        Step 11: Click "Run Deferred" button under Run Options
        """
        chart_obj.click_run_option_button('defer')
        
        """
        Verify the Deferred Report Description window is displayed
        """
        chart_obj.switch_to_new_window()
        OK_BTN_CSS="#deferMsg input[id='okButton']"
        chart_obj.wait_for_number_of_element(OK_BTN_CSS, 1, medium_wait)
        defer_msg_css="#deferMsg div[style*='bottom']"
        actual_defer_obj=utillobj.validate_and_get_webdriver_object(defer_msg_css, 'Deferred Report Description')
        actual_defer_msg=actual_defer_obj.text.strip()
        expected_defer_msg='Deferred Report Description'
        utillobj.asequal(actual_defer_msg,expected_defer_msg,'Step 11: Verify the Deferred Report Description window is displayed')
        
        """
        Step 12: Click OK
        """
        OK_BTN_obj=utillobj.validate_and_get_webdriver_object(OK_BTN_CSS, 'OK button object')
        OK_BTN_obj.click()
        time.sleep(sleep_time)
        
        """
        Verify the Deferred Report Notification window is displayed
        """
        href_css = "html a[href]"
        chart_obj.wait_for_number_of_element(href_css, 1, medium_wait)
        wnd_title=driver.title
        utillobj.asin(wnd_title,'Deferred Report Notification','Step 12.1: Verify the Deferred Report Notification window is displayed')
        
        href_obj=utillobj.validate_and_get_webdriver_object(href_css, 'Deferred Report Status link')
        actual_href_text = href_obj.text.strip()
        utillobj.asequal(actual_href_text, 'Deferred Report Status', "Step 12.2: Verify hyperlink in Deferred Status Report page")
        
        """
        Step 13: Click Deferred Report Status link
        """
        href_obj.click()
        time.sleep(sleep_time)
        
        """
        Verify the following window is displayed
        """
        deferred_css = "table[id]"
        chart_obj.wait_for_number_of_element(deferred_css, 1, medium_wait)
        wnd_title=driver.title
        utillobj.asin(wnd_title,'Deferred Report Status','Step 13.1: Verify the Deferred Report Status window is displayed')
        
        refresh_image_css = "img[src*='defresh1.gif']"
        sort_image_css = "img[src*='def_sort_az.gif']"
        delete_image_css = "#DeleteMenu img[src*='Delete16.gif']"
        utillobj.verify_object_visible(refresh_image_css, True, "Step13.2: Verify Refresh image object is displaying")
        utillobj.verify_object_visible(sort_image_css, True, "Step13.3: Verify sort image object is displaying")
        utillobj.verify_object_visible(delete_image_css, True, "Step13.4: Verify delete image object is displaying")
        
        
        expected_text_list_1 = ['DeferredReportStatusasof', 'Refresheveryseconds.(min.5seconds)EnableRefresh:']
        verify_text(expected_text_list_1)        
                  
        text = self.driver.find_elements_by_css_selector("td img[title]")
        actual_text_list_2 = [e.get_attribute('title') for e in text]        
        expected_text_list_2 = ['Refresh', 'Refresh', 'Sort By', 'Reverse Sort Order', 'Delete All', 'All']
        for expected_text, actual_text in zip(expected_text_list_2, actual_text_list_2):
            if expected_text == actual_text:
                status= True
            else:
                status=False
                break
        utillobj.asequal(status, True, "Step13.6: Verify text Refresh, Sort By, Delete, Help")
                  
        href = self.driver.find_elements_by_css_selector("td a[href]")
        actual_href_count = len(href)
        utillobj.as_GE(actual_href_count, 13, "Step13.7: Verify hyperlink count in Deferred Status Report page")       
                  
        dropdown_css ="[name='IBIMR_def_sortoption'] [selected]"
        actual_css = self.driver.find_element_by_css_selector(dropdown_css).get_attribute('value')
        utillobj.asequal("Date", actual_css, "Step13.8: Verify Date selected in Sort By dropdown")
        
        """
        Step 14: Click View
        """
        view_css="td a[href] img[title='View']"
        view_elem=utillobj.validate_and_get_webdriver_object(view_css, 'view link')
        view_elem.click()
        
        """
        Verify the output
        """
        chart_obj.switch_to_new_window()
        chart_obj.wait_for_number_of_element(RISER_CSS, 42, medium_wait)
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, msg="Step 14:01: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, msg="Step 14:02: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, msg="Step 14:03: Verify x_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 14:04: Verify y_axis title at runtime")
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 7, 6, msg="Step 14:05: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mbar!', 'bar_blue', "Step 14:06: Verify chart color")
        chart_obj.verify_legends_in_run_window(expected_legends, msg="Step 14:07: Verify legends")
        
        """
        Step 15: Close the output and Deferred window
        """
        chart_obj.switch_to_previous_window()
        chart_obj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            print("window not switched to main window")
            chart_obj.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element(PROMPT_SEGMENT_CSS, 1, medium_wait)
        
        """
        Step 16: Click 'Schedule' button under Run Options
        """
        chart_obj.click_run_option_button('schedule')
        
        """
        Verify the following schedule window is dispalyed
        """
        chart_obj.switch_to_new_window()
        time.sleep(sleep_time)
        RC_css="#ReportCasterDistribution"
        chart_obj.wait_for_number_of_element(RC_css, 1, medium_wait)
        wnd_title=driver.title
        utillobj.asin(wnd_title,'Distribution Method Selection','Step 16.1: Verify the schedule window is dispalyed')
        
        RC_label_css="#ReportCasterDistribution [class='bi-label']"
        RC_label_obj=utillobj.validate_and_get_webdriver_object(RC_label_css, 'view link')
        actual_rc_label=RC_label_obj.text.strip()
        utillobj.asequal(actual_rc_label, 'Please choose distribution method:','Step 16.2: Verify the ReportCasterDistribution label')
        
        RC_dist_css = "#ReportCasterDistribution [class*='tool-bar-button'] img"
        RC_dist_obj=utillobj.validate_and_get_webdriver_objects(RC_dist_css, 'Email and Report Library')
        actual_dist_count = len(RC_dist_obj)
        utillobj.as_GE(actual_dist_count, 2, "Step16.3: Verify Email and Report Library")
        
        """
        Step 17: Close the schedule window
        """
        chart_obj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            print("window not switched to main window")
            chart_obj.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element(PROMPT_SEGMENT_CSS, 1, medium_wait)
        
        """ 
        Step 18: Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == "__main__":
    unittest.main()