'''
Created on Jan 6, 2018

@author: BM13368
TestSuite : 8202 New Features and product changes for existing functionality
http://lnxtestrail.ibi.com/testrail//index.php?/runs/view/61162&group_by=cases:section_id&group_order=asc&group_id=173681
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2327075
TestCase Name : Edit 'Width of Bins' while field is being used in visualization filter
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
import pyautogui

class C2327075_TestClass(BaseTestCase):

    def test_C2327075(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        
        """
            Step 01:Launch the IA API with visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/car
        """
        utillobj.infoassist_api_login('idis','ibisamp/car','P312/S10664_binning_2', 'mrid', 'mrpass')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser!']"
        utillobj.synchronize_with_number_of_element(parent_css, 12, metaobj.home_page_long_timesleep)
        """  
            Step 02:Right-click SALES > Create Bins.
        """
        metaobj.datatree_field_click("SALES",1,1,"Create Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, metaobj.home_page_long_timesleep)
        """  
            Step 03:Type 1000 for 'Width of Bins' > OK.
        """
        metaobj.create_bin("SALES_BIN_1", btn_click='OK', bin_width='1000')
        utillobj.synchronize_with_visble_text("[id^='QbMetaDataTree']", 'SALES_BIN_1', metaobj.home_page_long_timesleep)
        bar_width_css = utillobj.validate_and_get_webdriver_object("#TableChart_1 svg>g rect[class='riser!s0!g0!mbar!']", 'Riser Bar')
        bar_width_before=bar_width_css.size['width']
        
        """  
            Step 04:Drag SALES_BIN_1 into the Filter pane > OK.
        """
        sales_bin_elem = utillobj.validate_and_get_webdriver_object('#iaMetaDataBrowser  div.bi-tree-view-body-content > table > tbody > tr:nth-child(6)>td>img:nth-child(2)', 'Sales_bin field')
        sales_bin_coordinate = core_utillobj.get_web_element_coordinate(sales_bin_elem)
        core_utillobj.left_click(sales_bin_elem)
        pyautogui.mouseDown(sales_bin_coordinate['x'], sales_bin_coordinate['y'], duration=2)
        filter_elem = utillobj.validate_and_get_webdriver_object('#qbFilterBox', 'Filter area')
        filter_elem_coordinate=core_utillobj.get_web_element_coordinate(filter_elem)
        pyautogui.moveTo(filter_elem_coordinate['x'], filter_elem_coordinate['y'], duration =2)
        pyautogui.mouseUp()
        
        filter_css="#avFilterOkBtn"
        utillobj.synchronize_with_number_of_element(filter_css, 1, metaobj.home_page_long_timesleep)
        filter_css = utillobj.validate_and_get_webdriver_object("#avFilterOkBtn", 'Ok button')
        core_utillobj.left_click(filter_css)
        utillobj.synchronize_until_element_is_visible('#ar_Prompt_1 span[id$="s_min"]', metaobj.home_page_long_timesleep)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min', 0,'int', msg="Step 04:01 Verify minimum Slider range is 10")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max', 43000,'int', msg="Step 04:02 Verify minimum Slider range is 70")
        
        """  
            Step 05:Right-click SALES_BIN_1 in Data pane > Edit Bins.
        """
        metaobj.datatree_field_click("Dimensions->SALES_BIN_1",1,1,"Edit Bins...")
        
        """  
            Step 06:Change 'Width of Bins' to 5000 > OK
        """
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, metaobj.home_page_long_timesleep)
        metaobj.create_bin("SALES_BIN_1", btn_click='OK', bin_width='5000')
        utillobj.synchronize_until_element_disappear(parent_css, metaobj.home_page_medium_timesleep)
        
        """  
            Step 07:Verify the output.
        """
        bar_width_css = utillobj.validate_and_get_webdriver_object("#TableChart_1 svg>g rect[class='riser!s0!g0!mbar!']", 'Riser Bar')
        bar_width_after=bar_width_css.size['width']
        verify_bin_width=float(bar_width_before)-float(bar_width_after)
        if verify_bin_width > 30:
            status = True
        else:
            status = False
        utillobj.asequal(status, True, 'Step 07:01 : Bar width is expanded to 5000')  
        utillobj.verify_object_visible("#qbFilterBox div table tbody tr:nth-child(1)", True, "Step 07:02: Verify filterpane is visible")
        
        """ 
            Step 08:Logout using API (without saving)
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()