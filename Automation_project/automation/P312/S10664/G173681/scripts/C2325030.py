'''
Created on Jan 1, 2018

@author: BM13368
TestSuite : 8202 New Features and product changes for existing functionality
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2325030
TestCase Name: Filter on Bin Value
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import metadata, visualization_metadata, visualization_resultarea
from common.lib import utillity

class C2325030_TestClass(BaseTestCase):

    def test_C2325030(self):
        """
        TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        
        """
            Step 01:Launch IA API to create new visualization with wf_retail
            http://machine:port/alias/ia?tool=idis&master=baseapp/WF_RETAIL&item=IBFS%3A%2FWFC%2FRepository%2FS10664
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail','P312/S10664_binning_2', 'mrid', 'mrpass')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 12, 30)
        """ 
            Step 02:Double click Customer/Full Name/Attributes/Age > Create Bin
        """
        metaobj.datatree_field_click("Age",1,1, 'Create Bins...')
        time.sleep(2)
          
        """ 
            Step 03:Leave defaults > OK
        """
        parent_css="div[id^='QbDialog'] [class*='active'] [class*='caption']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        bin_ok_btn=driver.find_element_by_css_selector("#qbBinsOkBtn")
        utillobj.default_click(bin_ok_btn)
        time.sleep(2)
            
        """  
            Step 04:Drag AGE_BIN_1 to Horizontal Axis
        """
        metadataobj.collapse_data_field_section('Attributes->Full,Name->Customer')
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Dimensions->AGE_BIN_1', 1, 'Horizontal Axis', 0)
        riser_css="#TableChart_1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(riser_css, 9, 30)
        """  
            Step 05:Double click Revenue to add to Vertical axis
        """
        metaobj.datatree_field_click("Revenue",2,1)
        time.sleep(3)
        
        """  
            Step 06:Right click Revenue in Query pane > More > Aggregation > Count
        """
        metaobj.querytree_field_click("Revenue", 1, 1)
        time.sleep(0.50)
        utillobj.select_or_verify_bipop_menu('More')
        time.sleep(0.50)
        utillobj.select_or_verify_bipop_menu('Aggregation Functions')
        time.sleep(0.50)
        utillobj.select_or_verify_bipop_menu('Count')
        time.sleep(2)
        metaobj.verify_query_pane_field("Vertical Axis", "CNT.Revenue", 1, "Step 05: ")
        """ 
            Step 07:Select 1 or more risers and review tooltip
            Tooltip shows options to filter and/or exclude
        """
        riser_css="#TableChart_1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(riser_css, 7, expire_time=20)
        resultobj.verify_yaxis_title("TableChart_1", 'CNT Revenue', "Step 07:01: Verify y-Axis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'AGE_BIN_1', "Step 07:02: Verify x-Axis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 7, 'Step 07:03: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '100K', '200K', '300K', '400K','500K','600K']
        expected_xval_list=['10', '20', '30', '40', '50', '60', '70']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 07:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 07:05: Verify first bar color")
        
        """
            Verify default tooltip: hover on any riser to verify tooltip values
        """
        expected_tooltip_list=['AGE_BIN_1:10', 'CNT Revenue:116581', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("TableChart_1", "riser!s0!g0!mbar", expected_tooltip_list, "Step 07:06: Verify first riser to verify tooltip values")
        """ 
            Step 08:Logout using API (without saving)
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()


if __name__ == "__main__":
    unittest.main()