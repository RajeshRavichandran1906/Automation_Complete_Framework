'''
Created on Jan 5, 2018

@author: BM13368
TestSuite : 8202 New Features and product changes for existing functionality
http://lnxtestrail.ibi.com/testrail//index.php?/runs/view/61162&group_by=cases:section_id&group_order=asc&group_id=173681
TestCase ID :http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2343343
TestCase Name :Visualization: Verify bin gets created without error.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods

class C2327802_TestClass(BaseTestCase):

    def test_C2327802(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        core_utillobj = CoreUtillityMethods(self.driver)
        
        """
            Step 01:Launch the IA API with visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/car
        """
        utillobj.infoassist_api_login('idis','ibisamp/car','P312/S10664_binning_2', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#TableChart_1", metaobj.home_page_long_timesleep)
            
        """  
            Step 02:Right click on SALES and select Create Bins.
        """
        metaobj.datatree_field_click("SALES", 1, 1, 'Create Bins...')
        
        """  
            Step 03:Choose all the defaults and click OK.
        """
        parent_css="div[id^='QbDialog'] [class*='active'] [class*='caption']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, metaobj.home_page_long_timesleep)
        bin_ok_btn = utillobj.validate_and_get_webdriver_object('#qbBinsOkBtn', 'OkBtn')
        core_utillobj.left_click(bin_ok_btn)
        utillobj.synchronize_with_visble_text("[id^='QbMetaDataTree']", 'SALES_BIN_1', metaobj.home_page_long_timesleep)
        
        """  
            Step 04:Drag Sales_BIN_1 to Horizontal Axis.
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Dimensions->SALES_BIN_1', 1, 'Horizontal Axis', 0)
        
        """
            Step 05:Verify, preview appears without any error.
        """
        riser_css="#TableChart_1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(riser_css, 13, metaobj.home_page_long_timesleep)
        resultobj.verify_xaxis_title("TableChart_1", 'SALES_BIN_1', "Step 05:01: Verify x-Axis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 13, 'Step 05:02: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=[]
        expected_xval_list=['0', '4800', '7800', '8900', '8950', '12000', '12400', '13000', '14000', '15600', '18940', '35030', '43000']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 05:03: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 05:04: Verify first bar color")
#         expected_tooltip_list=['SALES_BIN_1:0', 'Filter Chart', 'Exclude from Chart']
#         resultobj.verify_default_tooltip_values("TableChart_1", "riser!s0!g0!mbar", expected_tooltip_list, "Step 05:04:Verify tooltip values")
        """ 
            Step 06:Logout using API (without saving)
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()