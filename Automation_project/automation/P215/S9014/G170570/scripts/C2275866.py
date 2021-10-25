'''
Created on Oct 16, 2018

@author: Magesh

Testcase Name : Verify to Run and Interaction with 'Sales by Region Dashboard - Treemap'
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275866
'''

import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables
from common.wftools import visualization, chart, active_chart

class C2275866_TestClass(BaseTestCase):

    def test_C2275866(self):
        
        "-------------------------------------------------------------------CLASS OBJECTS--------------------------------------------------------------------------"
        driver = self.driver
        chart_obj = chart.Chart(driver)
        utillobj = utillity.UtillityMethods(driver)
        visual_obj = visualization.Visualization(driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        username= 'mrbasid'
        password= 'mrbaspass'
        fex_name='Sales_by_Region_Dashboard_Active'
        folder_name='Retail_Samples/Documents'
        wait_time=90
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        treemap_parent_css="MAINTABLE_3"
        no_of_risers="rect[class^='riser']"
        treemap_no_of_riser_css="#"+treemap_parent_css+" "+no_of_risers
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to Webfocus using rsbas (basic user)
        http://machine:port/ibi_apps
        Step 02: Run the Document using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Documents&BIP_item=Sales_by_Region_Dashboard_Active.fex
        """
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=treemap_no_of_riser_css, no_of_element=31)
         
        """Verify output"""
        treemap_parent_css="MAINTABLE_3"
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 31, "Step 02:1: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        treemap_riser_css="riser!sSpecialty Brand-_-Harman Kardon!g0!mnode"
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'persian_red', "Step 02:2: Verify Treemap chart color")
        treemap_expected_legend_list=['Gross Profit %', '20', '28.5', '37', '45.6', '54.1']
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list, parent_css="#"+treemap_parent_css, msg="Step 02:3: Verify legends in tree map at runtime")
        treemap_x_axis_label1=['Major Brand', 'Specialty Brand', 'Sony', 'Panasonic', 'LG', 'Pioneer', 'JVC', 'Samsung', 'Canon', 'Sharp', 'Sanyo', 'Philips', 'T', 'BOSE', 'Onkyo', 'Yamaha']
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 02:4: Verify Treemap labels at runtime")
        treemap_chart_title='Gross Profit % By Brand'
        chart_obj.verify_chart_title_in_run_window('run_chart_title1', treemap_chart_title, msg="Step 02:5: ")
        active_chart_toolbar_list1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Avg']
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 02:6: Verify active chart toolbar", parent_css="#"+treemap_parent_css)
        
        """
        Step 03: Go to Treemap "Gross Profit% By Brand"
        Step 04: Hover over on Treemap for the Brand "Sony" > Click Filter Chart
        """
        parent_css='MAINTABLE_wbody3'
        riser_css1='riser!sMajor Brand-_-Sony!g0!mnode'
        menu_path1='Filter Chart'
        visual_obj.select_tooltip(riser_css1, menu_path1, parent_css, element_location='middle', move_to_tooltip=True)
        
        """Verify output"""
        element_css1="#MAINTABLE_wbody3 rect[class^='riser']"
        visual_obj.wait_for_number_of_element(element_css1, expected_number=1, time_out=wait_time)
        treemap_parent_css="MAINTABLE_3"
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 1, "Step 04.1: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        treemap_riser_css="riser!sMajor Brand-_-Sony!g0!mnode"
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'Cumulus1', "Step 04.2: Verify Treemap chart color")
        treemap_expected_legend_list=['Gross Profit %', '31.3', '31.8', '32.3', '32.8', '33.3']
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list, parent_css="#"+treemap_parent_css, msg="Step 04.3: Verify legends in tree map at runtime")
        treemap_x_axis_label1=['Major Brand', 'Sony']
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 04.4: Verify Treemap labels at runtime")
        treemap_chart_title='Gross Profit % By Brand'
        chart_obj.verify_chart_title_in_run_window('run_chart_title1', treemap_chart_title, msg="Step 04.5: ")
        active_chart_toolbar_list1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Avg']
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 04.6: Verify active chart toolbar", parent_css="#"+treemap_parent_css)
        
        """
        Step 05: Click Remove Filter icon on top
        """
        treemap_parent_css="MAINTABLE_3"
        active_chart_obj.click_chart_menu_bar_items(treemap_parent_css, 4)

        """
        Verify Filter is removed
        """
        element_css1="#MAINTABLE_wbody3 rect[class^='riser']"
        visual_obj.wait_for_number_of_element(element_css1, expected_number=31, time_out=wait_time)
        treemap_parent_css="MAINTABLE_3"
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 31, "Step 05.1: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        treemap_riser_css="riser!sSpecialty Brand-_-Harman Kardon!g0!mnode"
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'persian_red', "Step 05.2: Verify Treemap chart color")
        treemap_expected_legend_list=['Gross Profit %', '20', '28.5', '37', '45.6', '54.1']
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list, parent_css="#"+treemap_parent_css, msg="Step 05.3: Verify legends in tree map at runtime")
        treemap_x_axis_label1=['Major Brand', 'Specialty Brand', 'Sony', 'Panasonic', 'LG', 'Pioneer', 'JVC', 'Samsung', 'Canon', 'Sharp', 'Sanyo', 'Philips', 'T', 'BOSE', 'Onkyo', 'Yamaha']
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 05.4: Verify Treemap labels at runtime")
        treemap_chart_title='Gross Profit % By Brand'
        chart_obj.verify_chart_title_in_run_window('run_chart_title1', treemap_chart_title, msg="Step 05.5: ")
        active_chart_toolbar_list1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Avg']
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 05.6: Verify active chart toolbar", parent_css="#"+treemap_parent_css)
        
        """
        Step 06: Lasso 5 points on the Top > Click Filter chart
        """
        time.sleep(Global_variables.longwait)
        source_css_locator="#MAINTABLE_wbody3 [class='riser!sMajor Brand-_-Sony!g0!mnode']"
        target_css_locator="#MAINTABLE_wbody3 [class*='riser!sMajor Brand-_-Samsung!g0!mnode']"
        source_element=utillobj.validate_and_get_webdriver_object(source_css_locator, "Source Lasso bar riser")
        target_element=utillobj.validate_and_get_webdriver_object(target_css_locator, "Target Lasso bar riser")
        source_element_location='top_middle'
        target_element_location='bottom_middle'
        visual_obj.create_lasso(source_element, target_element, source_element_location=source_element_location, target_element_location=target_element_location)
        visual_obj.select_lasso_tooltip('Filter Chart')
        
        """
        Step 07: Verify the Result
        """
        element_css1="#MAINTABLE_wbody3 rect[class^='riser']"
        visual_obj.wait_for_number_of_element(element_css1, expected_number=5, time_out=wait_time)
        treemap_parent_css="MAINTABLE_3"
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 5, "Step 07.1: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        treemap_riser_css="riser!sMajor Brand-_-JVC!g0!mnode"
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'elf_green', "Step 07.2: Verify Treemap chart color")
        treemap_expected_legend_list=['Gross Profit %', '29', '30.5', '32.1', '33.7', '35.3']
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list, parent_css="#"+treemap_parent_css, msg="Step 07.3: Verify legends in tree map at runtime")
        treemap_x_axis_label1=['Major Brand', 'Sony', 'Panasonic', 'LG', 'JVC', 'Samsung']
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 07.4: Verify Treemap labels at runtime")
        treemap_chart_title='Gross Profit % By Brand'
        chart_obj.verify_chart_title_in_run_window('run_chart_title1', treemap_chart_title, msg="Step 07.5: ")
        active_chart_toolbar_list1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Avg']
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 07.6: Verify active chart toolbar", parent_css="#"+treemap_parent_css)
        
        """
        Step 08 : Click "Restore Original" from first menu icon
        """
        active_chart_obj.create_new_item("MAINTABLE_3", "Restore Original", index=3)
        
        """
        Verify the Treemap restored back to original
        """
        element_css1="#MAINTABLE_wbody3 rect[class^='riser']"
        visual_obj.wait_for_number_of_element(element_css1, expected_number=31, time_out=wait_time)
        treemap_parent_css="MAINTABLE_3"
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 31, "Step 08.1: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        treemap_riser_css="riser!sSpecialty Brand-_-Harman Kardon!g0!mnode"
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'persian_red', "Step 08.2: Verify Treemap chart color")
        treemap_expected_legend_list=['Gross Profit %', '20', '28.5', '37', '45.6', '54.1']
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list, parent_css="#"+treemap_parent_css, msg="Step 08.3: Verify legends in tree map at runtime")
        treemap_x_axis_label1=['Major Brand', 'Specialty Brand', 'Sony', 'Panasonic', 'LG', 'Pioneer', 'JVC', 'Samsung', 'Canon', 'Sharp', 'Sanyo', 'Philips', 'T', 'BOSE', 'Onkyo', 'Yamaha']
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 08.4: Verify Treemap labels at runtime")
        treemap_chart_title='Gross Profit % By Brand'
        chart_obj.verify_chart_title_in_run_window('run_chart_title1', treemap_chart_title, msg="Step 08.5: ")
        active_chart_toolbar_list1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Avg']
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 08.6: Verify active chart toolbar", parent_css="#"+treemap_parent_css)
        
        """
        Step 09: Lasso 23 points on the bottom > Click Exclude from chart
        """
        time.sleep(Global_variables.longwait)
        source_css_locator="#MAINTABLE_wbody3 [class='riser!sMajor Brand-_-Canon!g0!mnode']"
        target_css_locator="#MAINTABLE_wbody3 [class*='riser!sSpecialty Brand-_-Polaroid!g0!mnode']"
        source_element=utillobj.validate_and_get_webdriver_object(source_css_locator, "Source Lasso bar riser")
        target_element=utillobj.validate_and_get_webdriver_object(target_css_locator, "Target Lasso bar riser")
        source_element_location='middle'
        target_element_location='bottom_right'
        visual_obj.create_lasso(source_element, target_element, source_element_location=source_element_location, target_element_location=target_element_location)
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        
        """
        Step 10: Verify the Result
        """
        element_css1="#MAINTABLE_wbody3 rect[class^='riser']"
        visual_obj.wait_for_number_of_element(element_css1, expected_number=8, time_out=wait_time)
        treemap_parent_css="MAINTABLE_3"
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 8, "Step 10.1: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        treemap_riser_css="riser!sMajor Brand-_-JVC!g0!mnode"
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'elf_green', "Step 10.2: Verify Treemap chart color")
        treemap_expected_legend_list=['Gross Profit %', '23.7', '26.6', '29.5', '32.4', '35.3']
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list, parent_css="#"+treemap_parent_css, msg="Step 10.3: Verify legends in tree map at runtime")
        treemap_x_axis_label1=['Major Brand', 'Specialty Brand', 'Sony', 'Panasonic', 'LG', 'Pioneer', 'JVC', 'Samsung', 'BOSE', 'Onkyo']
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 11.4: Verify Treemap labels at runtime")
        treemap_chart_title='Gross Profit % By Brand'
        chart_obj.verify_chart_title_in_run_window('run_chart_title1', treemap_chart_title, msg="Step 10.5: ")
        active_chart_toolbar_list1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Avg']
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 10.6: Verify active chart toolbar", parent_css="#"+treemap_parent_css)
        
        """
        Step 11: Right click on the Brand "Panasonic" > Click Remove Filter
        """
        parent_css='MAINTABLE_wbody3'
        riser_css1='riser!sMajor Brand-_-Panasonic!g0!mnode'
        menu_path1='Remove Filter'
        visual_obj.select_tooltip(riser_css1, menu_path1, parent_css, element_location='middle', move_to_tooltip=True)
        
        """
        Verify the Treemap restored back to original
        """
        element_css1="#MAINTABLE_wbody3 rect[class^='riser']"
        visual_obj.wait_for_number_of_element(element_css1, expected_number=31, time_out=wait_time)
        treemap_parent_css="MAINTABLE_3"
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 31, "Step 11.1: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        treemap_riser_css="riser!sSpecialty Brand-_-Harman Kardon!g0!mnode"
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'persian_red', "Step 11.2: Verify Treemap chart color")
        treemap_expected_legend_list=['Gross Profit %', '20', '28.5', '37', '45.6', '54.1']
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list, parent_css="#"+treemap_parent_css, msg="Step 11.3: Verify legends in tree map at runtime")
        treemap_x_axis_label1=['Major Brand', 'Specialty Brand', 'Sony', 'Panasonic', 'LG', 'Pioneer', 'JVC', 'Samsung', 'Canon', 'Sharp', 'Sanyo', 'Philips', 'T', 'BOSE', 'Onkyo', 'Yamaha']
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 11.4: Verify Treemap labels at runtime")
        treemap_chart_title='Gross Profit % By Brand'
        chart_obj.verify_chart_title_in_run_window('run_chart_title1', treemap_chart_title, msg="Step 11.5: ")
        active_chart_toolbar_list1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Avg']
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 11.6: Verify active chart toolbar", parent_css="#"+treemap_parent_css)
        
        """
        Step 12: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()