'''
Created on Oct 10, 2017

@author: BM13368
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib.basetestcase import BaseTestCase

class C2316726_TestClass(BaseTestCase):
    
    def test_C2316726(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2316726'
        Test_Case_ID1 = 'C2316722'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        
        """
            Step 01 : Restore C2316726_base.fex using IA API:(edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2316726_base.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID1, 'chart', 'P292/S10660_chart_1', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1 svg g.risers >g>rect[class^='riser']", 15, 85)
        
        """
            Verification : Verify the livepreview chart
        """
        
        resultobj.verify_yaxis_title("TableChart_1", 'Quantity Sold', "Step 01:01 Verify -yAxis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'PRICE', "Step 01:02 : Verify -xAxis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 15, 'Step 01:03 : Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        expected_xval_list=['$0', '$150', '$300', '$450', '$600', '$750', '$900', '$1,050', '$1,200', '$1,350', '$1,950', '$2,100', '$3,300', '$3,450', '$3,900']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 01:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 01:05: Verify first bar color")
        """
            Step 02 : Drag the bin into the filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter('Dimensions->PRICE', 1)
        time.sleep(4)
        
        """
            Step 03 : Click Get Values > All
        """
        ia_ribbonobj.create_constant_filter_condition('All',['$600 (600)','$750 (750)','$900 (900)','$1,050 (1050)','$1,200 (1200)', '$1,350 (1350)'])
        
        """
            Step 04 : Multi select $600(600) to $1,350(1350) > click arrow to move to right panel > OK > OK
        """
        time.sleep(5)
        resultobj.verify_yaxis_title("TableChart_1", 'Quantity Sold', "Step 4:01 Verify -yAxis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'PRICE', "Step 4:02 : Verify -xAxis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 6, 'Step 4:03 : Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '30K', '60K', '90K', '120K']
        expected_xval_list=['$600', '$750', '$900', '$1,050', '$1,200', '$1,350']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 4:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 4:05: Verify first bar color")
        
        """
            Step 05 : Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 35)
        
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
                
        """
            Verification : Step 05:01 : Verify the chart at runtime.
        """
        
        resultobj.verify_yaxis_title("jschart_HOLD_0", 'Quantity Sold', "Step 5:01 Verify -yAxis Title")
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'PRICE', "Step 5:02 : Verify -xAxis Title")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 6, 'Step 5:03 : Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '30K', '60K', '90K', '120K']
        expected_xval_list=['$600', '$750', '$900', '$1,050', '$1,200', '$1,350']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 5:04: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 5:05: Verify first bar color")
        expected_tooltip_list=['PRICE:$600', 'Quantity Sold:110,413']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar", expected_tooltip_list, "Step  5:06: Verify Salary bar value")
        utillobj.switch_to_default_content(pause=1)
        obj1=driver.find_element_by_css_selector("#resultArea")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        """
            Step 06: Save and Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
            Step 07 : Run from bip
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10660&BIP_item=C2316726_base.fex
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10660_chart_1", 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#jschart_HOLD_0 svg g.risers >g>rect[class^='riser']", 6, 65)
        
        resultobj.verify_yaxis_title("jschart_HOLD_0", 'Quantity Sold', "Step 6:01: Verify -yAxis Title")
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'PRICE', "Step 6:02: Verify -xAxis Title")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 6, 'Step 6:03: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '30K', '60K', '90K', '120K']
        expected_xval_list=['$600', '$750', '$900', '$1,050', '$1,200', '$1,350']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 6:04: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 6:05: Verify first bar color")
        expected_tooltip_list=['PRICE:$600', 'Quantity Sold:110,413']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar", expected_tooltip_list, "Step  6:06: Verify Salary bar value")
        
        """
        Step 08 :Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
            Step 09 : Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2316726_base.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1 svg g.risers >g>rect[class^='riser']", 6, 65)
        
        resultobj.verify_yaxis_title("TableChart_1", 'Quantity Sold', "Step 8:01 Verify -yAxis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'PRICE', "Step 8:02 : Verify -xAxis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 6, 'Step 8:03 : Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '30K', '60K', '90K', '120K']
        expected_xval_list=['$600', '$750', '$900', '$1,050', '$1,200', '$1,350']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 8:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 8:05: Verify first bar color")
        
        
if __name__ == "__main__":
    unittest.main()