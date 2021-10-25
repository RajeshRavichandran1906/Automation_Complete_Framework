'''
Created on Jan 2, 2018

@author: BM13368
TestSuite : 8202 New Features and product changes for existing functionality
http://lnxtestrail.ibi.com/testrail//index.php?/runs/view/61162&group_by=cases:section_id&group_order=asc&group_id=173681
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2343327
TestCase Name : Run time filter on Bin value
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import metadata, visualization_metadata, visualization_resultarea, visualization_ribbon, visualization_run
from common.lib import utillity

class C2343327_TestClass(BaseTestCase):

    def test_C2343327(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID='C2343327'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        vis_run_obj=visualization_run.Visualization_Run(driver)
        metadataobj = metadata.MetaData(self.driver)
        """
            Step 01:Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10666&tool=idis&master=baseapp/wf_retail
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail','P312/S10664_binning_2', 'mrid', 'mrpass')
        time.sleep(4)
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser!']"
        resultobj.wait_for_property(parent_css, 12, expire_time=35) 
        """  
            Step 02:Right click on "Age" (customer/full name/age) > Create Bins...
        """
        metaobj.datatree_field_click("Age",1,1,'Create Bins...')
        time.sleep(3)
        """ 
            Step 03:Click OK to accept default values
        """
        parent_css="div[id^='QbDialog'] [class*='active'] [class*='caption']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        bin_ok_btn=driver.find_element_by_css_selector("#qbBinsOkBtn")
        utillobj.default_click(bin_ok_btn)
        time.sleep(2)
        """  
            Step 04:Double click "Revenue" and "AGE_BIN_1" BIN
        """
        metadataobj.collapse_data_field_section('Attributes->Full,Name->Customer')
        time.sleep(5)
        metaobj.datatree_field_click("Revenue",2,1)
        time.sleep(1)
        parent_css="#TableChart_1 text[class='yaxis-title']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        metaobj.datatree_field_click('Dimensions->AGE_BIN_1',2,1)
        time.sleep(1)
        parent_css="#TableChart_1 svg>g.chartPanel rect[class^='riser!']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 30)
        """  
            Step 05:Verify following preview displayed
        """
        resultobj.verify_yaxis_title("TableChart_1", 'Revenue', "Step 05:01: Verify y-Axis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'AGE_BIN_1', "Step 05:02: Verify x-Axis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 7, 'Step 05:03: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        expected_xval_list=['10', '20', '30', '40', '50', '60', '70']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 05:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 05:05: Verify first bar color")
        time.sleep(2)
#         """
#             Verify Tooltip
#         """
#         expected_tooltip_list=['AGE_BIN_1:10', 'Revenue:$49,637,717.49', 'Filter Chart', 'Exclude from Chart']
#         resultobj.verify_default_tooltip_values("TableChart_1", "riser!s0!g0!mbar", expected_tooltip_list, "Step 05:06: Verify first riser to verify tooltip values")
#         time.sleep(3)
        
        """ 
            Step 06:Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 [class^='riser!']"
        resultobj.wait_for_property(parent_css, 7, expire_time=30)
        """
            Verify chart at runtime
        """
        xaxis_value="AGE_BIN_1"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 06:01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 06:02: Verify Y-Axis Title")  
        expected_xval_list=['10', '20', '30', '40', '50', '60', '70']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 06:03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 06:04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 06:05: Verify first bar color")
        time.sleep(2)
        
        """  
            Step 07:Click on "10" riser
            Step 08:Click Exclude from chart
        """
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class='riser!s0!g0!mbar!']")
        utillobj.click_on_screen(parent_elem, 'middle', mouse_duration=3, click_type=0)
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g0!mbar!", "Exclude from Chart", default_move=True, click_menu=True)
        time.sleep(5)
        """  
            Step 09:Verify "10" riser excluded
            Riser disappears, 6 risers left
        """
        parent_css="#MAINTABLE_wbody1 [class^='riser!']"
        resultobj.wait_for_property(parent_css, 6, expire_time=30)
        xaxis_value="AGE_BIN_1"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 09:01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 09:02: Verify Y-Axis Title")  
        expected_xval_list=['20', '30', '40', '50', '60', '70']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09:03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 6, 'Step 09:04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09:05: Verify first bar color")
#         time.sleep(5)
#         bar=['AGE_BIN_1:20', 'Revenue:$195,669,188.40', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 09:06: Verify bar value")
#         time.sleep(2)
        
        """ 
            Step 10:Hover over tallest riser (60) > Filter chart
        """
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g4!mbar!", "Filter Chart")
        time.sleep(2)
        """  
            Step 11:Verify One riser displays (60).
        """
        parent_css="#MAINTABLE_wbody1 [class^='riser!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=35)
        xaxis_value="AGE_BIN_1"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 11:01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 11:02: Verify Y-Axis Title")  
        expected_xval_list=['60']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11:03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 11:04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11:05: Verify first bar color")
#         bar=['AGE_BIN_1:60', 'Revenue:$203,584,082.12', 'Undo Filter', 'Remove Filter']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 11:06: Verify bar value")
        """ 
            Step 12:Click Remove filter icon
        """
        vis_run_obj.select_run_menu_option('MAINTABLE_menuContainer1',"remove_filter")
        
        """ 
            Step 13:Verify all filtered results cleared
            7 risers display from 10 to 70
        """
        parent_css="#MAINTABLE_wbody1 [class^='riser!']"
        resultobj.wait_for_property(parent_css, 7, expire_time=35)
        xaxis_value="AGE_BIN_1"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 13:01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 13:02: Verify Y-Axis Title")  
        expected_xval_list=['10', '20', '30', '40', '50', '60', '70']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 13:03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 13:04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 13:05: Verify first bar color")
#         time.sleep(5)
#         bar=['AGE_BIN_1:10', 'Revenue:$49,637,717.49', 'Filter Chart', 'Exclude from Chart']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 13:06: Verify bar value")
        """ 
            Step 14:Lasso the 5 central risers
        """
        resultobj.create_lasso('MAINTABLE_wbody1', 'rect', 'riser!s0!g1!mbar!', target_tag='rect', target_riser='riser!s0!g5!mbar')
        """ 
            Step 15:Click Filter chart
        """
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(2)
        """
            Step 16:Verify filtered result displayed
            5 risers display starting at 20 and ending with 60. 10 and 70 are not showing.
        """
        parent_css="#MAINTABLE_wbody1 [class^='riser!']"
        resultobj.wait_for_property(parent_css, 5, expire_time=35)
        xaxis_value="AGE_BIN_1"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16:01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 16:02: Verify Y-Axis Title")  
        expected_xval_list=['20', '30', '40', '50', '60']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16:03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 5, 'Step 16:04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16:05: Verify first bar color")
#         bar=['AGE_BIN_1:20', 'Revenue:$195,669,188.40', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 16:06: Verify bar value")
        """ 
            Step 17:Close run window
        """
        driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        """  
            Step 18:Click Save in the toolbar > Save as "C2343327" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        """  
            Step 19:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    unittest.main()