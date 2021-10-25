'''
Created on Jan 4, 2018

@author: BM13368
TestSuite : 8202 New Features and product changes for existing functionality
http://lnxtestrail.ibi.com/testrail//index.php?/runs/view/61162&group_by=cases:section_id&group_order=asc&group_id=173681
TestCase ID :http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2343339
TestCase Name :Filter prompt refreshed with new values after bin width edit
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import metadata, visualization_metadata, visualization_resultarea, visualization_ribbon, visualization_properties
from common.lib import utillity

class C2343340_TestClass(BaseTestCase):

    def test_C2343340(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        
        """
            Step 01:Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10666&tool=chart&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail','P312/S10664_binning_2', 'mrid', 'mrpass')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser!']"
        utillobj.synchronize_with_number_of_element(parent_css, 12, 35)
        """  
            Step 02:Right click on "Price,Dollars" > Create bins..
        """
        
        metaobj.datatree_field_click("Price,Dollars", 1, 1, "Create Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
         
        """  
            Step 03:Set Width of bins= 100
            Step 04:Click OK
        """
        metaobj.create_bin("PRICE_DOLLARS_BIN_1", btn_click='OK', bin_width='100')
        time.sleep(3)
        bar_width_css=self.driver.find_element_by_css_selector("#TableChart_1 svg>g rect[class='riser!s0!g0!mbar!']")
        bar_width_before=bar_width_css.size['width']
        metadataobj.collapse_data_field_section('Attributes->Model->Product')
        time.sleep(5) 
        """  
            Step 05:Double click "Quantity,Sold", "PRICE_DOLLARS_BIN_1" to add fields
        """
        metaobj.datatree_field_click("Quantity,Sold", 2, 1)
        time.sleep(6)
        metaobj.datatree_field_click("Dimensions->PRICE_DOLLARS_BIN_1", 2, 1)
        time.sleep(3)
        table_css="#TableChart_1 svg>g rect[class='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(table_css, 1, expire_time=25)
        """
            Verify preview
        """
        resultobj.verify_yaxis_title("TableChart_1", 'Quantity Sold', "Step 05:04: Verify y-Axis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'PRICE_DOLLARS_BIN_1', "Step 05:05: Verify x-Axis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 18, 'Step 04:03: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        expected_xval_list=['.00', '100.00', '200.00', '300.00', '400.00', '500.00', '600.00', '700.00', '800.00', '900.00', '1,100.00', '1,200.00', '1,300.00', '1,900.00', '2,200.00', '3,300.00', '3,400.00', '3,900.00']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 05:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 05:05: Verify first bar color")
        time.sleep(2)
#         """
#             Verify Tooltip
#         """
#         expected_tooltip_list=['PRICE_DOLLARS_BIN_1:.00', 'Quantity Sold:284,474']
#         resultobj.verify_default_tooltip_values("TableChart_1", "riser!s0!g0!mbar", expected_tooltip_list, "Step 05:09: Verify first riser to verify tooltip values")
#         time.sleep(3)
         
        """  
            Step 06:Add bin to filter pane, Change operator to "equal to" All with show prompt
        """
        metaobj.datatree_field_click('Dimensions->PRICE_DOLLARS_BIN_1', 1, 1, "Filter")
        time.sleep(15)
        filter_css="#avFilterOkBtn"
        resultobj.wait_for_property(filter_css,1)
        operator_combo_elem=self.driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Equal to'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 06:01: Verify dialog') 
        time.sleep(2)
        item_list=['[All]']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', msg = 'step 06:02: Verify dialog')
        time.sleep(2)
        """ 
            Step 07:Click OK
        """
        filter_css=self.driver.find_element_by_css_selector("#avFilterOkBtn")
        utillobj.click_on_screen(filter_css, "middle", click_type=0)
        time.sleep(15)
        
        """  
            Step 08:Verify following preview with prompt displayed
        """
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step 08:01: Verify 10 is checked in filter prompt")
        menu_list=['[All]', '.00', '100.00', '200.00', '300.00', '400.00', '500.00', '600.00', '700.00', '800.00', '900.00', '1,100.00', '1,200.00', '1,300.00', '1,900.00', '2,200.00', '3,300.00', '3,400.00', '3,900.00']
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', menu_list, msg="Step 08:02: Verify 10 is checked in filter prompt")
        resultobj.verify_yaxis_title("TableChart_1", 'Quantity Sold', "Step 08:03: Verify y-Axis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'PRICE_DOLLARS_BIN_1', "Step 08:04: Verify x-Axis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 18, 'Step 08:05: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        expected_xval_list=['.00', '100.00', '200.00', '300.00', '400.00', '500.00', '600.00', '700.00', '800.00', '900.00', '1,100.00', '1,200.00', '1,300.00', '1,900.00', '2,200.00', '3,300.00', '3,400.00', '3,900.00']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 08:06: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 08:07: Verify first bar color")
        time.sleep(2)
         
#         """
#             Verify Tooltip
#         """
#         expected_tooltip_list=['PRICE_DOLLARS_BIN_1:.00', 'Quantity Sold:284,474']
#         resultobj.verify_default_tooltip_values("TableChart_1", "riser!s0!g0!mbar", expected_tooltip_list, "Step 08:09: Verify first riser to verify tooltip values")
#         time.sleep(3)
        """ 
            Step 09:Right click "PRICE_DOLLARS_BIN_1" Bin in query pane > Edit Bin > Change bin width to 500
        """
        metaobj.querytree_field_click("PRICE_DOLLARS_BIN_1", 1, 1, "Edit Bins...")
        time.sleep(4)
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        resultobj.wait_for_property(parent_css, 1)
         
        """
            Step 10:Click OK
        """
        metaobj.create_bin("PRICE_DOLLARS_BIN_1", btn_click='OK', bin_width='500')
        time.sleep(14)
        """  
            Step 11:Verify filter prompt and preview updated
        """
        bar_width_css=self.driver.find_element_by_css_selector("#TableChart_1 svg>g rect[class='riser!s0!g0!mbar!']")
        after_bar_width=bar_width_css.size['width']
        verify_bin_width=float(bar_width_before)-float(after_bar_width)
        if verify_bin_width > 30:
            utillobj.asequal(True, True, 'Step 11:01 : Bar width is expanded to 500')
        else:
            utillobj.asequal(False, True, 'Step 11:02 : Bar width is expanded to 500')
 
        
        """ 
            Step 12:Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        parent_css="#MAINTABLE_wbody1 svg>g rect[class^='riser!']"
        resultobj.wait_for_property(parent_css, 7, expire_time=30)
        """  
            Step 13:Hover over on run time chart and Verify tooltip values
        """
        xaxis_value="PRICE_DOLLARS_BIN_1"
        yaxis_value="Quantity Sold"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 13:01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 13:02: Verify Y-Axis Title")
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M']
        expected_xval_list=['.00', '500.00', '1,000.00', '1,500.00', '2,000.00', '3,000.00', '3,500.00']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, 'Step 13:04: X and Y axis labels')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 13:05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 13:06: Verify first bar color")
        time.sleep(2)
        
        expected_tooltip_list=['PRICE_DOLLARS_BIN_1:.00', 'Quantity Sold:3,132,520']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar!", expected_tooltip_list,"Step 13:07:Verify tooltip values")
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step 13:08: Verify 10 is checked in filter prompt")
        menu_list=['[All]', '.00', '100.00', '200.00', '300.00', '400.00', '500.00', '600.00', '700.00', '800.00', '900.00', '1,100.00', '1,200.00', '1,300.00', '1,900.00', '2,200.00', '3,300.00', '3,400.00', '3,900.00']
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', menu_list, msg="Step 13:08: Verify 10 is checked in filter prompt")
        """ 
            Step 14:Close run window
        """
        self.driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        """  
            Step 15:Logout using API (without saving)
            http://machine:port/alias/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()