'''
Created on Nov 14, 2018

@author: Magesh

Testcase Name : Verify to Run and Interact with 'US Sales Map' html file
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2293374
'''

import unittest, time
from common.wftools import chart, report
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity

class C2293374_TestClass(BaseTestCase):
    
    def test_C2293374(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        utillobj = utillity.UtillityMethods(driver)
        report_obj=report.Report(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        TestCase_ID = "C2293374"
        USER_NAME='mrbasuser'
        PASSWORD= 'mrbaspass'
        FEX_NAME='US_Sales_Map'
        FOLDER_NAME='Retail_Samples/InfoApps/Maps'
        medium_wait=90
        sleep_time=8
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css="jschart_HOLD_0"
        RISER_CSS1="#jschart_HOLD_0 rect[class^='riser']"
        RISER_CSS2="#jschart_HOLD_0 path[class^='riser']"
        MAP_SEGMENT_CSS="#emfobject1_layers g path:not([transform^='matrix'])"
        iframe1_css="[id^='chart1']"
        iframe2_css="[id^='chart2']"
        iframe3_css="[id^='report1']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to WebFocus using "rsbas"
        http://machine:port/ibi_apps
        Step 02: Run html file using below API link:
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/InfoApps/Maps&BIP_item=US_Sales_Map.htm
        """
        chart_obj.run_htmlfex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=MAP_SEGMENT_CSS, no_of_element=49)
        utillobj.wait_for_page_loads(20)
        """
        Verify the following HTML output
        """
        "---1. esri map---"
        map_parent_css="emfobject1_layers"
        chart_obj.verify_number_of_chart_segment(map_parent_css, 49, "Step 01.1: Verify number of esri map riser segments in runtime", custom_css="g path:not([transform^='matrix'])")
        chart_obj.verify_number_of_chart_segment(map_parent_css, 44, "Step 01.2: Verify number of esri map riser markers in runtime", custom_css="g path[transform^='matrix']")
        chart_obj.verify_chart_color(map_parent_css, 'riser!s0!g0!mbar!', 'drak_green', "Step 01.3: Verify chart color", custom_css="g path[fill='rgb(0, 104, 55)']")
        
        region_label_css="#checkbox1 label"
        region_labels=utillobj.validate_and_get_webdriver_objects(region_label_css, 'Region control labels')
        actual_list=[el.text.strip() for el in region_labels]
        expected_list=['East', 'Midwest', 'Northeast', 'South', 'Southeast', 'West']
        utillobj.as_List_equal(actual_list,expected_list,'Step 1.4: Verify Region control labels in esri map')
        
        "---2. Bar chart---"
        chart_obj.switch_to_frame(iframe1_css)
        chart_obj.wait_for_number_of_element(RISER_CSS1, 5, medium_wait)
        expected_x_axis_labels=['New York', 'Houston', 'Chicago', 'Detroit', 'Atlanta']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, msg="Step 01.5: Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '8M', '16M', '24M', '32M']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, msg="Step 01.6: Verify y-axis label in runtime")
        expected_y_axis_title_list=['Revenue']
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 01.7: Verify y_axis title at runtime")
        parent_css_with_tag_name="#jschart_HOLD_0 rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 5, msg="Step 01.8:Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mbar!', 'elf_green', "Step 01.9: Verify chart color")
        chart_obj.verify_chart_title('Top 5 Stores by Revenue', 'run', "Step 01.10: Verify bar chart title at runtime")
        legend_list=['Gross Profit', '2.3M', '3.6M', '4.8M', '6M', '7.3M']
        chart_obj.verify_legends_in_run_window(legend_list, "#"+chart_parent_run_css, 5, 'Step 01.11: Verify bar chart Legend List in run window')
        chart_obj.switch_to_default_content()
        
        "---3. Ring pie chart---"
        chart_obj.switch_to_frame(iframe2_css)
        utillobj.wait_for_page_loads(5)
        chart_obj.wait_for_number_of_element(RISER_CSS2, 7, medium_wait)
        EXPECTED_LEGEND_LIST=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        PIE_LABEL_LIST=['Gross Profit']
        PIE_LABEL=['151.8M']
        RISER_CSS= "[class='riser!s0!g0!mwedge!']"
        
        chart_obj.verify_riser_pie_labels_and_legends(chart_parent_run_css, PIE_LABEL_LIST, "Step 01.12:",custom_css="text[class*='pieLabel']")
        chart_obj.verify_legends_in_run_window(EXPECTED_LEGEND_LIST, "#"+chart_parent_run_css, 5, 'Step 01.13: Verify pie Legend List in run window')
        chart_obj.verify_riser_pie_labels_and_legends(chart_parent_run_css, PIE_LABEL, "Step 01.14: Verify pie total label values in run window",custom_css="text[class^='totalLabel!']",same_group=True)
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RISER_CSS, 'bar_blue', "#"+chart_parent_run_css,msg="Step 01.15: Verify pie chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 7, "Step 01.16: Verify number of pie segments in run window")
        chart_obj.switch_to_default_content()
        
        "---4. report---"
        chart_obj.switch_to_frame(iframe3_css)
        TABLE_CSS="table"
#         report_obj.create_table_data_set(TABLE_CSS, TestCase_ID+"_Ds01.xlsx")
        report_obj.verify_table_data_set(TABLE_CSS, TestCase_ID+"_Ds01.xlsx", "Step 01.17: Verify report data at runtime.")
        chart_obj.switch_to_default_content()
        
        """
        Step 03: In Region uncheck "Northeast", "South" > Click Run button
        """
        itemlist=["Northeast", "South"]
        chart_obj.select_regionlabel_checkbox_in_run_window(itemlist)
        
        run_btn_css="div[class^='IBI_DesktopContainer'] input[id='Submit']"
        reference_name="run button in html esri map"
        run_btn=utillobj.validate_and_get_webdriver_object(run_btn_css, reference_name)
        run_btn.click()
        time.sleep(sleep_time)
        
        """
        Verify the map gets refreshed and the following output is displayed
        """
        chart_obj.wait_for_number_of_element(MAP_SEGMENT_CSS, 34, medium_wait)
        
        """
        Verify the following HTML output
        """
        "---1. esri map---"
        map_parent_css="emfobject1_layers"
        chart_obj.verify_number_of_chart_segment(map_parent_css, 34, "Step 03.1: Verify number of esri map riser segments in runtime", custom_css="g path:not([transform^='matrix'])")
        chart_obj.verify_number_of_chart_segment(map_parent_css, 28, "Step 03.2: Verify number of esri map riser markers in runtime", custom_css="g path[transform^='matrix']")
        chart_obj.verify_chart_color(map_parent_css, 'riser!s0!g0!mbar!', 'drak_green', "Step 03.3: Verify chart color", custom_css="g path[fill='rgb(0, 104, 55)']")
        
        region_label_css="#checkbox1 label"
        region_labels=utillobj.validate_and_get_webdriver_objects(region_label_css, 'Region control labels')
        actual_list=[el.text.strip() for el in region_labels]
        expected_list=['East', 'Midwest', 'Northeast', 'South', 'Southeast', 'West']
        utillobj.as_List_equal(actual_list,expected_list,'Step 3.4: Verify Region control labels in esri map')
        
        "---2. Bar chart---"
        chart_obj.switch_to_frame(iframe1_css)
        chart_obj.wait_for_number_of_element(RISER_CSS1, 5, medium_wait)
        expected_x_axis_labels=['New York', 'Chicago', 'Detroit', 'San Diego', 'Rochester']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, msg="Step 03.5: Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '8M', '16M', '24M', '32M']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, msg="Step 03.6: Verify y-axis label in runtime")
        expected_y_axis_title_list=['Revenue']
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 03.7: Verify y_axis title at runtime")
        parent_css_with_tag_name="#jschart_HOLD_0 rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 5, msg="Step 03.8:Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mbar!', 'elf_green', "Step 03.9: Verify chart color")
        chart_obj.verify_chart_title('Top 5 Stores by Revenue', 'run', "Step 03.10: Verify bar chart title at runtime")
        legend_list=['Gross Profit', '1.7M', '3M', '4.5M', '6M', '7.3M']
        chart_obj.verify_legends_in_run_window(legend_list, "#"+chart_parent_run_css, 5, 'Step 03.11: Verify bar chart Legend List in run window')
        chart_obj.switch_to_default_content()
        
        "---3. Ring pie chart---"
        chart_obj.switch_to_frame(iframe2_css)
        element_css="#jschart_HOLD_0 text[class^='totalLabel!']"
        chart_obj.wait_for_visible_text(element_css, '131.2M', medium_wait)
        EXPECTED_LEGEND_LIST=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        PIE_LABEL_LIST=['Gross Profit']
        PIE_LABEL=['131.2M']
        RISER_CSS= "[class='riser!s0!g0!mwedge!']"
        
        chart_obj.verify_riser_pie_labels_and_legends(chart_parent_run_css, PIE_LABEL_LIST, "Step 03.12:",custom_css="text[class*='pieLabel']")
        chart_obj.verify_legends_in_run_window(EXPECTED_LEGEND_LIST, "#"+chart_parent_run_css, 5, 'Step 03.13: Verify pie Legend List in run window')
        chart_obj.verify_riser_pie_labels_and_legends(chart_parent_run_css, PIE_LABEL, "Step 03.14: Verify pie total label values in run window",custom_css="text[class^='totalLabel!']",same_group=True)
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RISER_CSS, 'bar_blue', "#"+chart_parent_run_css,msg="Step 03.15: Verify pie chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 7, "Step 03.16: Verify number of pie segments in run window")
        chart_obj.switch_to_default_content()
        
        "---4. report---"
        chart_obj.switch_to_frame(iframe3_css)
        TABLE_CSS="table"
        self.driver.set_page_load_timeout(100) #firefox need time to load
        time.sleep(8)
#         report_obj.create_table_data_set(TABLE_CSS, TestCase_ID+"_Ds02.xlsx")
        report_obj.verify_table_data_set(TABLE_CSS, TestCase_ID+"_Ds02.xlsx", "Step 03.17: Verify report data at runtime.")
        chart_obj.switch_to_default_content()
        
        """
        Step 04: Click Change base map icon, Select Imagery then close the basemap
        """
        chart_obj.select_mainmenu_btn_in_esrimap(mainmenu_css="#mainMenuemfobject1", btn_name='basemap')
        time.sleep(sleep_time)
        parent_css="#emfobject1_imFloatingPane"
        chart_obj.wait_for_number_of_element(parent_css, 1, medium_wait)
        
        world_imagery_css="#emfobject1_imFloatingPane div[id='satellite'] img[title='Imagery']"
        reference_name="world_imagery from basemap dialog in esri map"
        world_imagery=utillobj.validate_and_get_webdriver_object(world_imagery_css, reference_name)
        world_imagery.click()
        time.sleep(sleep_time)
        chart_obj.close_basemap_dialog_in_esrimap()
        
        """
        Verify the map background changed to streets
        """
        map_imagery_css="#emfobject1_layers img[src*='World_Imagery']"
        chart_obj.wait_for_number_of_element(map_imagery_css, 20, medium_wait)
        
        map_parent_css="emfobject1_layers"
        chart_obj.verify_number_of_chart_segment(map_parent_css, 20, "Step 04.1: Verify the world imagery is applied and map background changed to streets", custom_css="img[src*='World_Imagery']")
        chart_obj.verify_number_of_chart_segment(map_parent_css, 34, "Step 04.2: Verify number of esri map riser segments in runtime", custom_css="g path:not([transform^='matrix'])")
        chart_obj.verify_number_of_chart_segment(map_parent_css, 28, "Step 04.3: Verify number of esri map riser markers in runtime", custom_css="g path[transform^='matrix']")
        chart_obj.verify_chart_color(map_parent_css, 'riser!s0!g0!mbar!', 'drak_green', "Step 04.4: Verify chart color", custom_css="g path[fill='rgb(0, 104, 55)']")
        
        """
        Step 05: Close the HTML output
        """
        
if __name__ == "__main__":
    unittest.main()