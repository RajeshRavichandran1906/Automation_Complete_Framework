'''
Created on Jan 8, 2018

@author: KS13172
TestSuite : 8202 New Features and product changes for existing functionality
TestCase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348451
TestCase Name: Can add Bin to Detail bucket of Scatter chart
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity

class C2348451_TestClass(BaseTestCase):

    def test_C2348451(self):
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
        utillobj.infoassist_api_login('idis','baseapp/wf_retail','P312/S10664_binning_2', 'mrid', 'mrpass')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        utillity.UtillityMethods.synchronize_with_number_of_element(self, parent_css, 12, 40)
        
        """ 
        Step 02: Right click Product attribute "Price,Dollar" > Create Bin
        """
        metaobj.datatree_field_click('Price,Dollars',1,1,'Create Bins...')
        time.sleep(1)
        
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
        Step 05: Click change drop down> Select Scatter chart
        """
        home_chart="#HomeAVChart [class^='bi-component tool-bar-menu-button-drop-down-arrow']"
        resultobj.wait_for_property(home_chart, 1, expire_time=10)
        ribbonobj.change_chart_type('scatter')
        utillobj.synchronize_with_visble_text("[class='bi-label dv-caption-label']","Scatter1",10)        
        
        """
        Step 06: Drag "PRICE_DOLLARS_BIN_1" bin field to Detail bucket
        """
        
        metaobj.drag_drop_data_tree_items_to_query_tree("Dimensions->PRICE_DOLLARS_BIN_1",1,"Detail",0) 
        time.sleep(0.2) 
        parent_css= "#TableChart_1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 18, expire_time=10)
        
        """
        Step07: Verify "PRICE_DOLLARS_BIN_1" bin field added to detail bucket
        """
        metaobj.verify_query_pane_field('Detail',"PRICE_DOLLARS_BIN_1",1,"Step 07: Verify PRICE_DOLLARS_BIN_1 added to detail bucket")
                
        """
        Step08: Logout using API (without saving)
        """
#         utillobj.infoassist_api_logout()



if __name__ == "__main__":
    unittest.main()