'''
Created on Sep 19, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6419799&group_by=cases:section_id&group_id=170570&group_order=asc.
Testcase Name : Verify to Lasso with 'Sales by Region Dashboard - Pie chart'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart, visualization
from common.lib import utillity

class C6419799_TestClass(BaseTestCase):

    def test_C6419799(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        utillobj=utillity.UtillityMethods(driver)
        visual_obj=visualization.Visualization(driver)
    
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        medium_wait= 70
        username= 'mrbasid'
        password= 'mrbaspass'
        fex_name='Sales_by_Region_Dashboard_Active'
        folder_name='Retail_Samples/Documents'
        
        """----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"""
        
        ringpie_expected_label_list=['Revenue']
        ringpie_expected_legendlist=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        ringpie_riser_css1="[class='riser!s4!g0!mwedge!']"
        ringpie_riser_css2="[class='riser!s0!g0!mwedge!']"
        ringpie_riser_css3="[class='riser!s3!g0!mwedge!']"
        ringpie_risers="[class*='riser!s']"
        ringpie_chart_title='Sales by Product Category'
        
        active_chart_toolbar_list1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        ringpie_parent_css="MAINTABLE_0"
        ringpie_label_css="#"+ringpie_parent_css+" [class^='totalLabel']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
            Step 1 : Sign to Webfocus using rsbas (basic user)
            http://machine:port/ibi_apps
            Step 2 : Run the Document using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Documents&BIP_item=Sales_by_Region_Dashboard_Active.fex
        """
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=ringpie_label_css, no_of_element=1)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0 .legend text", 8, active_chart_obj.chart_long_timesleep)
        """
            Step 3 : Go to the Pie chart "Sales by Product Category"
            Step 4: Lasso 5 points on the Pie chart > Click "Exclude from chart". Note: (Clockwise select slices from Red to Green)
        """
        ringpie_expected_totallabel1=['70.1M']
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist, parent_css="#"+ringpie_parent_css, msg="Step 03:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'brick_red', parent_css="#"+ringpie_parent_css, msg="Step 03:02: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css2, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 03:03: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css3, 'pale_yellow', parent_css="#"+ringpie_parent_css, msg="Step 03:04: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 03:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel1, "Step 03:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!g']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 7, "Step 03:07: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 03:08:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 03:09: Verify active chart toolbar", parent_css="#"+ringpie_parent_css)
        
        source_element_css="#"+ringpie_parent_css+" [class*='riser!s4!g0!mwedge!']"
        target_element_css="#"+ringpie_parent_css+" [class*='riser!s0!g0!mwedge!']"
        source_obj=utillobj.validate_and_get_webdriver_object(source_element_css, "blue color part of ringpie chart")
        target_obj=utillobj.validate_and_get_webdriver_object(target_element_css, "pale orange color part of ringpie chart")
        visual_obj.create_lasso(source_obj, target_obj, source_yoffset=10, target_xoffset=10,source_element_location='top_left', target_element_location='top_right') 
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        
        css="#"+ringpie_parent_css+" text[class^='totalLabel!g']"
        chart_obj.wait_for_visible_text(css, '21.7M', medium_wait)
        
        """
            Step 5: Verify the Result
        """
        ringpie_expected_totallabel1=['21.7M']
        ringpie_expected_legendlist1=['Product Category','Computers', 'Media Player']
        ringpie_riser_css4="[class='riser!s0!g0!mwedge!']"
        ringpie_riser_css5="[class='riser!s1!g0!mwedge!']"
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist1, parent_css="#"+ringpie_parent_css, msg="Step 05:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css4, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 05:03: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css5, 'pale_green', parent_css="#"+ringpie_parent_css, msg="Step 05:04: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 05:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel1, "Step 05:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!g']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 2, "Step 05:07: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 05:08: Verify Ringpie chart title")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 05:09: Verify active chart toolbar", parent_css="#"+ringpie_parent_css)
        
        """
            Step 6: Hover over slices on "Product Category - Computers" > Click Remove Filter
            Verify the filter condition is removed
        """
        
        css="riser!s0!g0!mwedge!"
        menu_path="Remove Filter"
        visual_obj.select_tooltip(css, menu_path, parent_css=ringpie_parent_css, move_to_tooltip=True)
        
        ringpie_expected_totallabel1=['70.1M']
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist, parent_css="#"+ringpie_parent_css, msg="Step 06:01: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'brick_red', parent_css="#"+ringpie_parent_css, msg="Step 06:02: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css2, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 06:03:")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css3, 'pale_yellow', parent_css="#"+ringpie_parent_css, msg="Step 06:04:")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 06:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel1, "Step 06:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!g']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 7, "Step 06:07: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 06:08: Verify Ringpie chart title")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 06:09: Verify active chart toolbar", parent_css="#"+ringpie_parent_css)
        
        """
            Step 7: Lasso 6 points on Pie chart > Click Filter chart. Note: (Clockwise select slices from Red to Dark Green)
        """
        source_element_css="#"+ringpie_parent_css+" [class*='riser!s5!g0!mwedge!']"
        target_element_css="#"+ringpie_parent_css+" [class*='riser!s2!g0!mwedge!']"
        source_obj=utillobj.validate_and_get_webdriver_object(source_element_css, "Blue color part of ringpie chart")
        target_obj=utillobj.validate_and_get_webdriver_object(target_element_css, "Dark green color part of ringpie chart")
        visual_obj.create_lasso(source_obj, target_obj, source_element_location='middle_left')
        visual_obj.select_lasso_tooltip('Filter Chart')
        
        css="#"+ringpie_parent_css+" text[class^='totalLabel!g']"
        chart_obj.wait_for_visible_text(css, '50.8M', medium_wait)
        
        """
            Step 8: Verify the selected chart is filtered
        """
        ringpie_expected_totallabel1=['50.8M']
        ringpie_expected_legendlist1=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Stereo Systems', 'Televisions', 'Video Production']

        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist1, parent_css="#"+ringpie_parent_css, msg="Step 08:01: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'brick_red', parent_css="#"+ringpie_parent_css, msg="Step 08:02: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css2, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 08:03:")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css3, 'pale_yellow', parent_css="#"+ringpie_parent_css, msg="Step 08:04:")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 08:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel1, "Step 08:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!g']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 6, "Step 08:07: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 08:08: Verify Ringpie chart title")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 08:09: Verify active chart toolbar", parent_css="#"+ringpie_parent_css)
        
        """
            Step 9 : Click Remove Filter icon on top
        """
        active_chart_obj.click_chart_menu_bar_items(ringpie_parent_css, 4)
        
        css="#"+ringpie_parent_css+" text[class^='totalLabel!g']"
        chart_obj.wait_for_visible_text(css, '70.1M', medium_wait)
        
        """
            Verify the filter condition is removed
        """
        ringpie_expected_totallabel1=['70.1M']
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist, parent_css="#"+ringpie_parent_css, msg="Step 09:01: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'brick_red', parent_css="#"+ringpie_parent_css, msg="Step 09:02: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css2, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 09:03:")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css3, 'pale_yellow', parent_css="#"+ringpie_parent_css, msg="Step 09:04:")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 09:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel1, "Step 09:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!g']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 7, "Step 09:07: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 09:08: Verify Ringpie chart title")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 09:09: Verify active chart toolbar", parent_css="#"+ringpie_parent_css)
        
        """
            Step 10 :Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
        
        

if __name__ == "__main__":
    unittest.main()