'''
Created on Jan 8, 2018

@author: KS13172
TestSuite : 8202 New Features and product changes for existing functionality
TestCase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348450
TestCase Name: Able to add bin to Label Bucket of Simple Bar Chart Extension
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity

class C2348450_TestClass(BaseTestCase):

    def test_C2348450(self):
        """
        TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01:Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/ia?tool=idis&master=baseapp/WF_RETAIL&item=IBFS%3A%2FWFC%2FRepository%2FS10664
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail','P312/S10664_binning_2', 'mrid', 'mrpass')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 12, expire_time=10)  
         
        """ 
        Step 02: Right click 'Product' Attribute > "Price,Dollar" > Create Bin...
        """
        metaobj.datatree_field_click('Price,Dollars',1,1,'Create Bins...')
        time.sleep(0.3)
         
        """ 
        Step 03: Set bin width = 100
        Step 04: Click OK
        """
        wd_of_bin="input[id^='qbBinWidthTextField']"
        resultobj.wait_for_property(wd_of_bin, 1, expire_time=10)
        wd_elem=self.driver.find_element_by_css_selector(wd_of_bin)
        utillobj.set_text_field_using_actionchains(wd_elem,"100",keyboard_type=True)
        bin_ok_btn=driver.find_element_by_css_selector("[id^='qbBinsOkBtn']")
        time.sleep(0.3)    
        utillobj.click_on_screen(bin_ok_btn, "middle", click_type=0)
        time.sleep(0.3)
         
        """
        Step 05: Change chart type to HTML5 extension 'Simple Bar'
        """
        home_chart="#HomeAVChart [class^='bi-component tool-bar-menu-button-drop-down-arrow']"
        resultobj.wait_for_property(home_chart, 1, expire_time=10)
        ribbonobj.change_chart_type('simple_bar')
        utillobj.synchronize_with_visble_text("[class='bi-label dv-caption-label']","Simple bar1",10)        
          
        """
        Step06: Double click 'Revenue' to add Value bucket
        """
        metaobj.datatree_field_click('Revenue',2,1)
        time.sleep(0.3)
          
        """
        Step 07: Drag the bin (PRICE_DOLLARS_BIN_1) to the Label bucket
        """
        metaobj.drag_drop_data_tree_items_to_query_tree("PRICE_DOLLARS_BIN_1",1,"Label Bucket",0) 
        time.sleep(0.2) 
        parent_css= "#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 18, expire_time=10)
         
        """
        Step08: Verify bin (PRICE_DOLLARS_BIN_1) is added to label bucket
        """
        metaobj.verify_query_pane_field('Label Bucket',"PRICE_DOLLARS_BIN_1",1,"Step 08: Verify PRICE_DOLLARS_BIN_1 added to Label bucket")

        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 18,'Step 08.b: Verify the total number of risers displayed on preview', custome_css=" rect[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08.c: Verify first bar color")
        time.sleep(5)
        bar=['PRICE_DOLLARS_BIN_1:0.00', 'Revenue:$20,395,806.96']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 08.d: Verify bar value")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1",'Simple Bar Chart Extension',"Step 08:a(i) Verify Title",custom_css=" svg>g>text[class*='title']")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1",'Revenue', "Step 08:a(i) Verify Y-Axis Title", custom_css=" g text")        
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'footnote', "Step 08:a(i) Verify X-Axis Title",custom_css=" svg>g>text[class*='foot']")
        time.sleep(2)
                 
        """
        Step09: Logout using API (without saving)
        """
#         utillobj.infoassist_api_logout()



if __name__ == "__main__":
    unittest.main()