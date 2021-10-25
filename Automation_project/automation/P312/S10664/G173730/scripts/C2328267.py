'''
Created on Jan 12, 2018

@author: BM13368
TestSuite Name : 8202 New Features and product changes for existing functionality
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10664&group_by=cases:section_id&group_order=asc&group_id=173730
TestCase ID :http://172.19.2.180/testrail/index.php?/cases/view/2328267
TestCase Name : Verify Horizontal label format of bin field
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods

class C2328267_TestClass(BaseTestCase):

    def test_C2328267(self):
        """
        TESTCASE VARIABLES
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        core_utillobj = CoreUtillityMethods(self.driver)
        
        """
            Step 01:Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_binning_2', 'mrid', 'mrpass')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 12, metaobj.home_page_long_timesleep)
        
        """
            Step 02:Right click "Revenue" > Create Bin
        """
        metaobj.datatree_field_click("Revenue", 1, 1,"Create Bins...") 
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.synchronize_with_number_of_element(parent_css, 1, metaobj.home_page_long_timesleep)
       
        """
            Step 03:Bin width = 1000
            Step 04: Click 'Format' button to set "D15.2CM " format in edit dialog
            Step 05:Click "OK(2x)"
        """
        metaobj.create_bin("REVENUE_US_BIN_1", btn_click='OK', bin_format_btn='true', check_box_list=['Use Comma (C)'], field_length='15', ok_btn=True, bin_width='1000')
        utillobj.synchronize_with_visble_text("[id^='QbMetaDataTree']", 'REVENUE_US_BIN_1', metaobj.home_page_medium_timesleep)
             
        """ 
            Step 05:Add bin to Horizontal axis
        """
        metaobj.datatree_field_click('Dimensions->REVENUE_US_BIN_1',1,1,'Add To Query','Horizontal Axis')
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        metaobj.verify_query_pane_field("Horizontal Axis", "REVENUE_US_BIN_1", 1, "Sep 05:01:")
        
        """ 
            Step 06:Verify horizontal axis labels are showing with decimal and comma.
        """
        riser_css="#TableChart_1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(riser_css, 16, metaobj.home_page_long_timesleep)
        resultobj.verify_xaxis_title("TableChart_1", 'REVENUE_US_BIN_1', "Step 06:01: Verify x-Axis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 16, 'Step 06:02: Verify the total number of risers displayed on livepreview Chart')
        expected_datalabel=['$.00', '$1,000.00', '$2,000.00', '$3,000.00','$4,000.00']
        resultobj.verify_data_labels("TableChart_1", expected_datalabel, "Step 06:03: Verify x-axis label values", data_label_length=1, custom_css="svg>g[class='chartPanel'] text[class*='mgroupLabel']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 06:04: Verify first bar color")
        bar_width_css = utillobj.validate_and_get_webdriver_object("#TableChart_1 svg>g rect[class='riser!s0!g0!mbar!']", 'Riser bar')
        bar_width=bar_width_css.size['width']
        status_ = True if bar_width > 40 else False
        utillobj.asequal(True, status_, 'Step 06:03 : Bar width is expanded to 1000')

        """ 
            Step 07:Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utillobj.switch_to_new_window()
             
        """
            Step 08:Verify same in run time
        """
        riser_css="#MAINTABLE_wbody1_fmg svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(riser_css, 16, metaobj.home_page_long_timesleep)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'REVENUE_US_BIN_1', "Step 08:01: Verify x-Axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 16, 'Step 08:02: Verify the total number of risers displayed on livepreview Chart')
        expected_datalabel=['$.00', '$1,000.00', '$2,000.00', '$3,000.00','$4,000.00']
        resultobj.verify_data_labels("MAINTABLE_wbody1", expected_datalabel, "Step 08:03: Verify x-axis label values", data_label_length=1, custom_css="svg>g[class='chartPanel'] text[class*='mgroupLabel']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08:04: Verify first bar color")
        
        """
            Verify default tooltip: hover on any riser to verify tooltip values
        """
        expected_tooltip_list=['REVENUE_US_BIN_1:$.00']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", expected_tooltip_list, "Step 08:05: Verify first riser to verify tooltip values")
        """     
           Step 09: Dismiss run window  
        """
        """     
           Step 10: Logout using API (without saving)   
        """       
        core_utillobj.switch_to_previous_window()

if __name__ == "__main__":
    unittest.main()