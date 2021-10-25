'''
Created on Jan 10, 2018

@author: BM13368
TestSuite : 8202 New Features and product changes for existing functionality
http://lnxtestrail.ibi.com/testrail//index.php?/runs/view/61162&group_by=cases:section_id&group_order=asc&group_id=173681
TestCase ID :http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2327087
TestCase NAme : Verify modified values in a Visualization Filter based on Bin field updates the Filter dialog and filter prompt.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
import pyautogui

class C2327087_TestClass(BaseTestCase):

    def test_C2327087(self):
        """
        TESTCASE VARIABLES
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        coreutils = CoreUtillityMethods(self.driver)
        
        """
            Step 01:Launch the IA API with visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/car
        """ 
        utillobj.infoassist_api_login('idis','ibisamp/car','P312/S10664_binning_2', 'mrid', 'mrpass')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 12, 35)
        """
            Step 02:Right-click SALES > Create Bins.
        """
        metaobj.datatree_field_click("SALES", 1, 1,"Create Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        """
            Step 03:Type 5000 for 'Width of Bins' > Click OK
        """
        metaobj.create_bin("SALES_BIN_1", btn_click='OK', bin_width='5000')
        utillobj.synchronize_with_visble_text("[id^='QbMetaDataTree']", 'SALES_BIN_1', metaobj.home_page_long_timesleep)
        bar_width_css = utillobj.validate_and_get_webdriver_object("#TableChart_1 svg>g rect[class='riser!s0!g0!mbar!']", 'Riser bar')
        bar_width_before=int(bar_width_css.size['width'])
        
        """
            Step 04:Drag SALES_BIN_1 into Filter pane > Select Operator "Equal To" > Click OK.
        """
        sales_bin_elem = utillobj.validate_and_get_webdriver_object('#iaMetaDataBrowser  div.bi-tree-view-body-content > table > tbody > tr:nth-child(6)>td>img:nth-child(2)', 'Sales_bin field')
        sales_bin_coordinate = coreutils.get_web_element_coordinate(sales_bin_elem)
        coreutils.left_click(sales_bin_elem)
        pyautogui.mouseDown(sales_bin_coordinate['x'], sales_bin_coordinate['y'], duration=2)
        filter_elem = utillobj.validate_and_get_webdriver_object('#qbFilterBox', 'Filter area')
        filter_elem_coordinate=coreutils.get_web_element_coordinate(filter_elem)
        pyautogui.moveTo(filter_elem_coordinate['x'], filter_elem_coordinate['y'], duration =2)
        pyautogui.mouseUp()
        utillobj.synchronize_with_number_of_element("div[class ='bi-window active window ']", 1, metaobj.home_page_long_timesleep)
        operator_combo_elem = utillobj.validate_and_get_webdriver_object("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']", 'Combo box')
        elem = 'Equal to'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify=True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 06:01: Verify dialog') 
        time.sleep(2)
        item_list=['[All]', '0', '5000', '10000', '15000', '35000', '40000']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', Ok_button=True, msg='step 04.01 :',)
        utillobj.synchronize_until_element_is_visible("#qbFilterBox", metaobj.home_page_medium_timesleep)
         
        """
            Verify Prompt values
        """
        metaobj.verify_filter_pane_field('SALES_BIN_1',1,"Step 04:02: Verify 'SALES_BIN_1' appears in filter pane")
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step 04:03: Verify 10 is checked in filter prompt")
        menu_list=['[All]', '0', '5000', '10000', '15000', '35000', '40000']
        propertyobj.select_or_verify_show_prompt_item(1, 'x', menu_list=menu_list, msg="Step 04:05: Verify prompt values")
        """
            Step 05:Right-click SALES_BIN_1 in the Data pane > Edit Bins.
        """
        metaobj.datatree_field_click('Dimensions->SALES_BIN_1', 1, 1,"Edit Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, metaobj.home_page_long_timesleep)
        """
            Step 06:Change 'Width of Bins' to 10000 > Click OK.
        """ 
        metaobj.create_bin("SALES_BIN_1", btn_click='OK', bin_width='10000')
        utillobj.synchronize_with_visble_text("[id^='QbMetaDataTree']", 'SALES_BIN_1', metaobj.home_page_long_timesleep)
        bar_width_css = utillobj.validate_and_get_webdriver_object("#TableChart_1 svg>g rect[class='riser!s0!g0!mbar!']", 'Riser bar')
        after_bar_width=int(bar_width_css.size['width'])
        verify_bin_width=bar_width_before -after_bar_width
        
        if verify_bin_width > 30:
            status = True
        else:
            status = False
            
        utillobj.asequal(status, True, 'Step 5.01 : Bar width is expanded to 500')
            
        """
            Step 07:Right click the filter prompt > Edit.
            Verify both the values match.
        """
        
        metaobj.verify_filter_pane_field('SALES_BIN_1',1,"Step 07:01: Verify 'SALES_BIN_1' appears in filter pane")
        metaobj.filter_tree_field_click('SALES_BIN_1',1,1)
        utillobj.select_or_verify_bipop_menu('Edit...',verify='true',expected_popup_list=['Edit...', 'Hide Prompt', 'Delete'],msg='Step 07:02: Right click "SALES_BINr" filter in the Filter pane')
        filter_css="#avFilterOkBtn"
        utillobj.synchronize_with_number_of_element(filter_css, 1, metaobj.home_page_long_timesleep)
        item_list=['[All]', '0', '10000', '30000', '40000']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', Ok_button=True, msg="Step 07:03:", )
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step 07:04: Verify 10 is checked in filter prompt")
        menu_list=['[All]', '0', '10000', '30000', '40000']
        propertyobj.select_or_verify_show_prompt_item(1, 'x', menu_list=menu_list, msg="Step 07:05: Verify prompt values")
        
        """
            Step 08:Logout using API (without saving)
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()