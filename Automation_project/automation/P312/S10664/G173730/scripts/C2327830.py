'''
Created on Jan 11, 2018

@author: BM13368
TestSuite Name : 8202 New Features and product changes for existing functionality
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10664&group_by=cases:section_id&group_order=asc&group_id=173730
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2327830
TestCase Name : Bin field values are updated after bin expression is modified
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_properties, visualization_ribbon
from common.lib import utillity
from common.wftools import visualization

class C2327830_TestClass(BaseTestCase):

    def test_C2327830(self):
        """
        TESTCASE VARIABLES
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visual_obj= visualization.Visualization(self.driver)
        """
            Step 01:Launch the IA API with visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=new_retail/wf_retail_lite
        """ 
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_binning_2', 'mrid', 'mrpass')
        utillobj.wait_for_page_loads(20)
#         time.sleep(4)
#         parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
#         utillobj.synchronize_with_number_of_element(parent_css, 12, 35)
#             
        """    
            Step 02:Right click "Revenue" in data pane and create bin with bin width of 1000
        """
        visual_obj.right_click_on_datetree_item("Revenue", 1, "Create Bins...")
        utillobj.synchronize_with_number_of_element('div[id^="QbDialog"]', 1, visual_obj.chart_medium_timesleep)
        visual_obj.create_bins("REVENUE_US_BIN_1", bin_width='1000')
        utillobj.synchronize_until_element_disappear('div[id^="QbDialog"]', visual_obj.chart_medium_timesleep)
#         bar_width_css=self.driver.find_element_by_css_selector("#TableChart_1 svg>g rect[class='riser!s0!g0!mbar!']")
#         bar_width_before=bar_width_css.size['width']
             
        """ 
            Step 03:Add "REVENUE_US_BIN_1" bin to Horizontal
        """ 
        visual_obj.drag_field_from_data_tree_to_query_pane('Dimensions->REVENUE_US_BIN_1', 1, 'Horizontal Axis')
        utillobj.synchronize_with_number_of_element('text[class*="labels"]', 16, visual_obj.chart_medium_timesleep)
        
            
        """ 
            Step 04:Verify the preview,data pane and query pane
        """
        metaobj.verify_query_pane_field("Horizontal Axis", "REVENUE_US_BIN_1", 1, "Sep 03:01:")
        riser_css="#TableChart_1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(riser_css, 16, visual_obj.chart_medium_timesleep)
        resultobj.verify_xaxis_title("TableChart_1", 'REVENUE_US_BIN_1', "Step 04:01: Verify x-Axis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 16, 'Step 04:02: Verify the total number of risers displayed on livepreview Chart')
        expected_datalabel=['$.00', '$1,000.00', '$2,000.00', '$3,000.00','$4,000.00']
        resultobj.verify_data_labels("TableChart_1", expected_datalabel, "Step 04:03: Verify x-axis label values", data_label_length=1, custom_css="svg>g[class='chartPanel'] text[class*='mgroupLabel']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 04:05: Verify first bar color")
        
        """ 
            Step 05:Right click "REVENUE_US_BIN_1" in query pane > Edit bins...
        """
        visual_obj.right_click_on_datetree_item("Dimensions->REVENUE_US_BIN_1", 1, "Edit Bins...")
        utillobj.synchronize_with_number_of_element('div[id^="QbDialog"]', 1, visual_obj.chart_medium_timesleep)

        """ 
            Step 06:Change bin width of 5000
            Step 07:Click OK
        """
        metaobj.create_bin("REVENUE_US_BIN_1", btn_click='OK', bin_width='5000')
        utillobj.synchronize_until_element_disappear('div[id^="QbDialog"]', visual_obj.chart_medium_timesleep)
#         resultobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step 07:01: Verify the total number of risers displayed on livepreview Chart')
#         bar_width_css=self.driver.find_element_by_css_selector("#TableChart_1 svg>g rect[class='riser!s0!g0!mbar!']")
#         after_bar_width=bar_width_css.size['width']
#         print(after_bar_width)
#         verify_bin_width=float(bar_width_before)-float(after_bar_width)
#         if verify_bin_width > 30:
#             utillobj.asequal(True, True, 'Step 07:01 : Bar width is expanded to 5000')
#         else:
#             utillobj.asequal(False, True, 'Step 07:02 : Bar width is expanded to 5000')
#             
        """ 
            Step 08:Add the "REVENUE_US_BIN_1" bin to the filter > change to "Equal to"
        """
        metaobj.datatree_field_click("Dimensions->REVENUE_US_BIN_1", 1, 1, "Filter")
        utillobj.synchronize_with_number_of_element('#avFilterOkBtn', 1, visual_obj.chart_medium_timesleep)
        operator_combo_elem=self.driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Equal to'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify=True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 08:01: Verify dialog') 
        time.sleep(2)
                
        """ 
            Step 09:Verify the following on the filter dialog
            Step 10:Click OK
        """
        item_list=['[All]', '$.00', '$5,000.00', '$10,000.00', '$15,000.00']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', Ok_button=True, msg='step 09.01',)
        utillobj.synchronize_until_element_disappear('#avFilterOkBtn', visual_obj.chart_medium_timesleep)
        
        """  
            Step 11:Verify the filter prompt values
        """
        metaobj.verify_filter_pane_field('REVENUE_US_BIN_1',1,"Step 11:01: Verify 'REVENUE_US_BIN_1' appears in filter pane")
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step 11:02: Verify All is checked in filter prompt")
        menu_list=['[All]', '$.00', '$5,000.00', '$10,000.00', '$15,000.00']
        propertyobj.select_or_verify_show_prompt_item(1, 'x', menu_list=menu_list, msg="Step 11:03: Verify prompt values")
        time.sleep(5)
        
        """
            Verify live preview Chart
        """
        resultobj.verify_xaxis_title("TableChart_1", 'REVENUE_US_BIN_1', "Step 11:01: Verify x-Axis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step 11:02: Verify the total number of risers displayed on livepreview Chart')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 11:03: Verify first bar color")
        expected_datalabel=['$.00', '$5,000.00', '$10,000.00', '$15,000.00']
        resultobj.verify_data_labels("TableChart_1", expected_datalabel, "Step 11:04: Verify x-axis label values", custom_css="svg>g[class='chartPanel'] text[class*='mgroupLabel']")
        
        """"
            Step 12:Click Run
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.wait_for_page_loads(10)
        utillobj.switch_to_window(1)
        utillobj.wait_for_page_loads(15)  
        """ 
            Step 13:Verify run time chart
        """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'REVENUE_US_BIN_1', "Step 13:01: Verify x-Axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 13:02: Verify the total number of risers displayed on livepreview Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 13:03: Verify first bar color")
        expected_datalabel=['$.00', '$5,000.00', '$10,000.00', '$15,000.00']
        resultobj.verify_data_labels("MAINTABLE_wbody1", expected_datalabel, "Step 13:04: Verify x-axis label values", custom_css="svg>g[class='chartPanel'] text[class*='mgroupLabel']")
        
        """ 
            Step 14:Dismiss run window
        """
        self.driver.close()        
        """ 
            Step 15:Logout using API (without saving)
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.switch_to_window(0)

if __name__ == "__main__":
    unittest.main()