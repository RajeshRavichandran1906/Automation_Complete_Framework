'''
Created on Nov 9, 2018

Testcase Name : Verify to Run and Interact with 'Filtered Dashboard' html file
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2293379
'''

import unittest, time
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity

class C2293379_TestClass(BaseTestCase):
    
    def test_C2293379(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        utillobj = utillity.UtillityMethods(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        USER_NAME='mrbasid'
        PASSWORD= 'mrbaspass'
        FEX_NAME='Filtered_Dashboard'
        FOLDER_NAME='Retail_Samples/InfoApps/Responsive_Dashboards'
        medium_wait=90
        sleep_time=8
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css="jschart_HOLD_0"
        RISER_CSS1="#jschart_HOLD_0 svg g g circle[class^='riser']"
        RISER_CSS2="#jschart_HOLD_0 svg g g g  g g rect[class^='riser']"
        PROMPT_SEGMENT_CSS='form.IBI_ReportControlPanel'
        iframe1_css="[id^='iframe1']"
        iframe2_css="[id^='iframe2']"
        iframe3_css="[id^='iframe3']"
        iframe4_css="[id^='iframe4']"
        iframe5_css="[id^='iframe5']"
        iframe6_css="[id^='iframe6']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to WebFocus using "rsbas"
        http://machine:port/ibi_apps
        Step 02: Run html file using below API link:
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/InfoApps/Responsive_Dashboards&BIP_item=Filtered_Dashboard.htm
        """
        chart_obj.run_htmlfex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=PROMPT_SEGMENT_CSS, no_of_element=1)
        utillobj.wait_for_page_loads(20)
        time.sleep(sleep_time)
        chart_obj.wait_for_number_of_element(iframe1_css, 1, medium_wait)
        
        """
        Verify the following output
        """
        "---1. bubble chart---"
        chart_obj.switch_to_frame(iframe1_css)
        chart_obj.wait_for_number_of_element(RISER_CSS1, 21, medium_wait)
        expected_x_axis_labels=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css='#jschart_HOLD_0', msg="Step 01.1:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css='#jschart_HOLD_0', msg="Step 01.2:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Revenue']
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#jschart_HOLD_0', msg="Step 01.3:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css='#jschart_HOLD_0', msg="Step 01.4:Verify y_axis title at runtime")
        parent_css_with_tag_name="#jschart_HOLD_0 svg g g circle"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 21, msg="Step 01.5:Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g2!mmarker!', 'bar_blue', "Step 01.6: Verify chart color")
        chart_obj.switch_to_default_content()
        
        "---2. Bar chart---"
        chart_obj.switch_to_frame(iframe2_css)
        chart_obj.wait_for_number_of_element(RISER_CSS2, 28, medium_wait)
        expected_x_axis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, msg="Step 01.7: Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '20M', '40M', '60M', '80M', '100M']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, msg="Step 01.8: Verify y-axis label in runtime")
        expected_x_axis_title_list=['Product Category']
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, msg="Step 01.9: Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 01.10: Verify y_axis title at runtime")
        parent_css_with_tag_name="#jschart_HOLD_0 svg g g g g g rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 28, msg="Step 01.11:Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mbar!', 'bar_blue', "Step 01.12: Verify chart color")
        chart_obj.switch_to_default_content()
        
        "---3. Heatmap chart---"
        chart_obj.switch_to_frame(iframe3_css)
        chart_title_list= ['Sale Quarter', 'Store Region']
        expected_xval_list= ['1', '2', '3', '4']
        expected_zval_list=['EMEA', 'North America', 'Oceania', 'South America']
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list,"#"+chart_parent_run_css,msg='Step01.14')
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, "#"+chart_parent_run_css, msg='Step01.15')
        chart_obj.verify_z_axis_label_in_run_window(expected_zval_list, "#"+chart_parent_run_css, msg='Step01.16')
        parent_css_with_tag_name="#jschart_HOLD_0 svg g rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 16, msg="Step 01.17:Verify number of risers at runtime")
        chart_obj.switch_to_default_content()
        
        "---4. Line chart---"
        chart_obj.switch_to_frame(iframe4_css)
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css='#jschart_HOLD_0', msg="Step 01.19:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css='#jschart_HOLD_0', msg="Step 01.20:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Month']
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#jschart_HOLD_0', msg="Step 01.21:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue']
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css='#jschart_HOLD_0', msg="Step 01.22:Verify y_axis title at runtime")
        parent_css_with_tag_name="#jschart_HOLD_0 svg g g g g g path"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 4, msg="Step 01.23:Verify number of risers at runtime")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class^='riser!s0!g0!mline!']", 'bar_blue', parent_css='#jschart_HOLD_0', attribute='stroke', msg="Step 01.24:Verify chart color")
        chart_obj.switch_to_default_content()
        
        "---5. bubble map---"
        chart_obj.switch_to_frame(iframe5_css)
        RISER_CSS="[id*='jschart_HOLD_0_com-esri-map'] circle[class^='riser']"
        chart_obj.wait_for_number_of_element(RISER_CSS, 86, medium_wait)
        parent_css_with_tag_name1="[id*='jschart_HOLD_0_com-esri-map'] circle"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name1, 1, 86, msg="Step 01.26:Verify number of risers at preview")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g2!mregion!', 'bar_blue',"Step01.27: Verify chart color")
        expected_legends=['Store Business Region', 'EMEA', 'North America', 'Oceania', 'South America', 'Revenue', '327.8M', '164M']
        chart_obj.verify_legends_in_run_window(expected_legends, parent_css="#jschart_HOLD_0", msg="Step 01.25: Verify legends")
        chart_obj.switch_to_default_content()
        
        "---6. Treemap chart---"
        chart_obj.switch_to_frame(iframe6_css)
        treemap_parent_css="jschart_HOLD_0"
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 21, "Step 01.29: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        treemap_riser_css="riser!sMedia Player-_-Blu Ray!g0!mnode"
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'elf_green', "Step 01.30: Verify Treemap chart color")
        treemap_x_axis_label1=['Stereo Systems', 'Media Player', 'Accessories', 'Camcorder', 'Computers', 'Video Production', 'Televisions', 'Home Theater Systems', 'iPod Docking Station', 'Speaker Kits', 'Receivers', 'Boom B...', 'Blu Ray', 'Str...', 'DV...', 'DV...', 'Headphones', 'Universal Remot...', 'Charger', 'Handheld', 'Standard', 'Smartphone', 'Tablet', 'Video Editing', 'Flat Panel TV', 'P', 'C', 'Gross Profit']
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 01.31: Verify Treemap labels at runtime")
        chart_obj.switch_to_default_content()
         
        """
        Step 03: Click 'Filters' dropdown arrow on top of the html
        """
        time.sleep(sleep_time)
        filter_dropdown_css="div[title*='Filters'][class*='IBI_btn-down']"
        filter_dropdown_elem=utillobj.validate_and_get_webdriver_objects(filter_dropdown_css, 'Filter dropdown')
        filter_dropdown_elem[6].click()
        run_css="form.IBI_ReportControlPanel div > input[class^='IBI_button IBI_btn-run']"
        chart_obj.wait_for_number_of_element(run_css, 1, medium_wait)
         
        """
        Step 04: Click "Business Region" dropdown > Select 'North America'
        """
        chart_obj.select_combo_item_in_infoapps_top_panel('Business Region:', "North America")
        
        """
        Step 05: Click "Product Category" dropdown > Select 'Camcorder', 'Computers' , Click (X) to close
        """
        time.sleep(sleep_time)
        Prod_cat_dropdown_css="#panel3 #combobox2"
        Prod_cat_dropdown_elem=utillobj.validate_and_get_webdriver_object(Prod_cat_dropdown_css, 'Product Category dropdown')
        Prod_cat_dropdown_elem.click()
        combobox_css="div[class*='ui-dialog'] #combobox2"
        chart_obj.wait_for_number_of_element(combobox_css, 1, medium_wait)
        
        camcorder_css="#combobox2 table tr input[type*='checkbox'][value='Camcorder']"
        camcorder_elem=utillobj.validate_and_get_webdriver_object(camcorder_css, 'Camcorder checkbox in combobox')
        camcorder_elem.click()
        
        computers_css="#combobox2 table tr input[type*='checkbox'][value='Computers']"
        computers_elem=utillobj.validate_and_get_webdriver_object(computers_css, 'Computers checkbox in combobox')
        computers_elem.click()
        
        close_btn_css="div[class*='ui-dialog-titlebar'] button[title='Close']"
        close_btn_elem=utillobj.validate_and_get_webdriver_object(close_btn_css, 'Close button in combobox')
        close_btn_elem.click()
        time.sleep(sleep_time)
         
        """
        Step 06: Click "Store Type Description" dropdown > Select Web
        """
        store_type_css="select#combobox3"
        store_type_elem=utillobj.validate_and_get_webdriver_object(store_type_css, 'Store Type Description dropdown')
        store_type_elem.click()
        time.sleep(sleep_time)
        web_css="select#combobox3 option[value='Web']"
        web_elem=utillobj.validate_and_get_webdriver_object(web_css, 'web value parameter')
        web_elem.click()
        time.sleep(sleep_time)
#         chart_obj.select_combo_item_in_infoapps_left_panel('Store Type Description:', "Web", top_panel=True)
         
        """
        Step 07: Click 'From' calendar button > choose 2013/01/23
        """
        from_calendar_icon_css="#calendar1_but"
        Date_picker_css="div.ui-datepicker"
        from_calendar_icon_obj=utillobj.validate_and_get_webdriver_object(from_calendar_icon_css, 'From date calendar icon')
        from_calendar_icon_obj.click()
        chart_obj.wait_for_number_of_element(Date_picker_css, 1, medium_wait)
        chart_obj.select_month_in_calendardatepicker_dialog_in_run_window('January')
        chart_obj.select_year_in_calendardatepicker_dialog_in_run_window('2013')
        chart_obj.select_date_in_calendardatepicker_dialog_in_run_window('23')
         
        """
        Step 08: Click 'To' calendar button > choose 2016/07/13
        """
        time.sleep(sleep_time)
        to_calendar_icon_css="#calendar2_but"
        Date_picker_css="div.ui-datepicker"
        to_calendar_icon_obj=utillobj.validate_and_get_webdriver_object(to_calendar_icon_css, 'To date calendar icon')
        to_calendar_icon_obj.click()
        chart_obj.wait_for_number_of_element(Date_picker_css, 1, medium_wait)
        chart_obj.select_month_in_calendardatepicker_dialog_in_run_window('July')
        chart_obj.select_year_in_calendardatepicker_dialog_in_run_window('2016')
        chart_obj.select_date_in_calendardatepicker_dialog_in_run_window('13')
        
        """Verify the changes"""
        time.sleep(sleep_time)
        Business_Region_combobox_css='form.IBI_ReportControlPanel div > select#combobox1'
        utillobj.verify_dropdown_value(Business_Region_combobox_css, expected_default_selected_value="North America", default_selection_msg="Step 08.1: Verify North America is selected under Business_Region")
         
        Product_Category_combobox_css="form.IBI_ReportControlPanel div #combobox2"
        actual_value=utillobj.validate_and_get_webdriver_object(Product_Category_combobox_css, 'Product_Category parameter')
        actual_field=actual_value.text.strip()
        expected_field="Camcorder; Computers"
        utillobj.asequal(actual_field,expected_field,'Step 08.2: Verify default amper value for Product Category')
        chart_obj.switch_to_default_content()
         
        Store_Type_Description_combobox_css='form.IBI_ReportControlPanel div > select#combobox3'
        utillobj.verify_dropdown_value(Store_Type_Description_combobox_css, expected_default_selected_value="Web", default_selection_msg="Step 08.3: Verify Web is selected under Store Type Description")
         
        from_date_css="#form1 #calendar1 > input"
        from_date_obj=utillobj.validate_and_get_webdriver_object(from_date_css, 'From date in Calender1')
        actual_from_date=from_date_obj.get_attribute('value')
        expected_from_date="2013/01/23"
        utillobj.asequal(actual_from_date,expected_from_date,'Step 08.4: Verify From date in Calender1')
         
        to_date_css="#form1 #calendar2 > input"
        to_date_obj=utillobj.validate_and_get_webdriver_object(to_date_css, 'To date in Calender2')
        actual_to_date=to_date_obj.get_attribute('value')
        expected_to_date="2016/07/13"
        utillobj.asequal(actual_to_date,expected_to_date,'Step 08.5: Verify To date in Calender2')
         
        """
        Step 09: Click Run, Verify the dashboard gets refreshed
        """
        chart_obj.click_run_option_button_in_infoapps_top_panel('run')
        time.sleep(sleep_time)
        chart_obj.wait_for_number_of_element(iframe1_css, 1, medium_wait)
         
        """
        Verify the following output
        """
        "---1. bubble chart---"
        chart_obj.switch_to_frame(iframe1_css)
        chart_obj.wait_for_number_of_element(RISER_CSS1, 5, medium_wait)
        expected_x_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M', '2.8M']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css='#jschart_HOLD_0', msg="Step 09.1:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '200K', '400K', '600K', '800K', '1,000K']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css='#jschart_HOLD_0', msg="Step 09.2:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Revenue']
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#jschart_HOLD_0', msg="Step 09.3:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css='#jschart_HOLD_0', msg="Step 09.4:Verify y_axis title at runtime")
        parent_css_with_tag_name="#jschart_HOLD_0 svg g g circle"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 5, msg="Step 09.5:Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mmarker!', 'bar_blue', "Step 09.6: Verify chart color")
        chart_obj.switch_to_default_content()
        
        "---2. Bar chart---"
        chart_obj.switch_to_frame(iframe2_css)
        chart_obj.wait_for_number_of_element(RISER_CSS2, 2, medium_wait)
        expected_x_axis_labels=['Camcorder', 'Computers']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, msg="Step 09.7: Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, msg="Step 09.8: Verify y-axis label in runtime")
        expected_x_axis_title_list=['Product Category']
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, msg="Step 09.9: Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 09.10: Verify y_axis title at runtime")
        parent_css_with_tag_name="#jschart_HOLD_0 svg g g g g g rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 09.11:Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mbar!', 'bar_blue', "Step 09.12: Verify chart color")
        chart_obj.switch_to_default_content()
        
        "---3. Heatmap chart---"
        chart_obj.switch_to_frame(iframe3_css)
        chart_title_list= ['Sale Quarter', 'Store Region']
        expected_xval_list= ['1', '2', '3', '4']
        expected_zval_list=['North America']
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list,"#"+chart_parent_run_css,msg='Step09.14')
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, "#"+chart_parent_run_css, msg='Step09.15')
        chart_obj.verify_z_axis_label_in_run_window(expected_zval_list, "#"+chart_parent_run_css, msg='Step09.16')
        parent_css_with_tag_name="#jschart_HOLD_0 svg g rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 4, msg="Step 09.17:Verify number of risers at runtime")
        chart_obj.switch_to_default_content()
        
        "---4. Line chart---"
        chart_obj.switch_to_frame(iframe4_css)
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css='#jschart_HOLD_0', msg="Step 09.19:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '200K', '400K', '600K', '800K', '1,000K']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css='#jschart_HOLD_0', msg="Step 09.20:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Month']
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#jschart_HOLD_0', msg="Step 09.21:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue']
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css='#jschart_HOLD_0', msg="Step 09.22:Verify y_axis title at runtime")
        parent_css_with_tag_name="#jschart_HOLD_0 svg g g g g g path"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 1, msg="Step 09.23:Verify number of risers at runtime")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class^='riser!s0!g0!mline!']", 'bar_blue', parent_css='#jschart_HOLD_0', attribute='stroke', msg="Step 09.24:Verify chart color")
        chart_obj.switch_to_default_content()
        
        "---5. bubble map---"
        chart_obj.switch_to_frame(iframe5_css)
        RISER_CSS="#jschart_HOLD_0 svg circle[class^='riser']"
        chart_obj.wait_for_number_of_element(RISER_CSS, 1, medium_wait)
        parent_css_with_tag_name="[id*='jschart_HOLD_0_com-esri-map'] circle"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 1, msg="Step 09.26:Verify number of risers at preview")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mregion!', 'bar_blue',"Step09.27: Verify chart color")
        chart_obj.switch_to_default_content()
        
        "---6. Treemap chart---"
        chart_obj.switch_to_frame(iframe6_css)
        treemap_parent_css="jschart_HOLD_0"
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 5, "Step 09.29: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        treemap_riser_css="riser!sCamcorder-_-Handheld!g0!mnode"
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'elf_green', "Step 09.30: Verify Treemap chart color")
        treemap_x_axis_label1=['Camcorder', 'Computers', 'Handheld', 'Standard', 'Professional', 'Smartphone', 'Tablet', 'Gross Profit']
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 09.31: Verify Treemap labels at runtime")
        chart_obj.switch_to_default_content()
        
        """
        Step 10: Click arrow again to close the filter dropdown
        Step 11: Resize the runtime browser page as shown in the screen shot and verify Responsive behavior
        """
        driver.set_window_size(945, 1020)
        time.sleep(sleep_time)
        
        "---1. bubble chart---"
        chart_obj.switch_to_frame(iframe1_css)
        chart_obj.wait_for_number_of_element(RISER_CSS1, 5, medium_wait)
        expected_x_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M', '2.8M']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css='#jschart_HOLD_0', msg="Step 011.1:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '200K', '400K', '600K', '800K', '1,000K']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css='#jschart_HOLD_0', msg="Step 011.2:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Revenue']
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#jschart_HOLD_0', msg="Step 011.3:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css='#jschart_HOLD_0', msg="Step 011.4:Verify y_axis title at runtime")
        parent_css_with_tag_name="#jschart_HOLD_0 svg g g circle"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 5, msg="Step 011.5:Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mmarker!', 'bar_blue', "Step 011.6: Verify chart color")
        chart_obj.switch_to_default_content()
        
        "---2. Bar chart---"
        chart_obj.switch_to_frame(iframe2_css)
        chart_obj.wait_for_number_of_element(RISER_CSS2, 2, medium_wait)
        expected_x_axis_labels=['Camcorder', 'Computers']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, msg="Step 011.7: Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, msg="Step 011.8: Verify y-axis label in runtime")
        expected_x_axis_title_list=['Product Category']
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, msg="Step 011.9: Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 011.10: Verify y_axis title at runtime")
        parent_css_with_tag_name="#jschart_HOLD_0 svg g g g g g rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 011.11:Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mbar!', 'bar_blue', "Step 011.12: Verify chart color")
        chart_obj.switch_to_default_content()
        
        "---3. Heatmap chart---"
        chart_obj.switch_to_frame(iframe3_css)
        chart_title_list= ['Sale Quarter', 'Store Region']
        expected_xval_list= ['1', '2', '3', '4']
        expected_zval_list=['North America']
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list,"#"+chart_parent_run_css,msg='Step011.14')
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, "#"+chart_parent_run_css, msg='Step011.15')
        chart_obj.verify_z_axis_label_in_run_window(expected_zval_list, "#"+chart_parent_run_css, msg='Step011.16')
        parent_css_with_tag_name="#jschart_HOLD_0 svg g rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 4, msg="Step 011.17:Verify number of risers at runtime")
        chart_obj.switch_to_default_content()
        
        """
        Step 12: Close the HTML output
        Step 13: Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == "__main__":
    unittest.main()