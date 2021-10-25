'''
Created on 18-Sep-2018

@author: KK14897

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970&group_by=cases:section_id&group_order=asc&group_id=156533
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226963
TestCase Name = Test that Auto Drill works with Reporting Objects
'''
import unittest, time
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from selenium.common.exceptions import NoSuchElementException

class C2226963_TestClass(BaseTestCase):
    def test_C2226963(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        Test_Case_ID = "C2226963"
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        

        """    1.Re-open the saved fex using below API link
               http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P276/S9970/RO-Chart.fex&tool=Chart
        """        
        utillobj.infoassist_api_edit("RO-Chart", 'chart', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element("rect[class='riser!s4!g4!mbar!r0!c0!']", 1, 150)
          
        """    2. Click Format tab > Autodrill button    """
        ribbonobj.switch_ia_tab("Format")
        if driver.find_element_by_css_selector("#FormatAutoDrillCluster").value_of_css_property("Visibility") == 'hidden':
            autolink_altbtn=driver.find_element_by_css_selector("#FormatAutoDrillCluster_altButton img")
            utillobj.default_left_click(object_locator=autolink_altbtn)
            time.sleep(2)
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        utillobj.synchronize_with_number_of_element("#runButton img", 1, 50)
         
        """    3. Click RUN    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')        
        utillobj.synchronize_with_number_of_element("#jschart_HOLD_0 svg g.risers >g>rect[class^='riser']", 139, 50)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 3a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 139, 'Step 3b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 3c(1): Verify first segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g1!mbar!r0!c0!", "bar_green", "Step 3c(2): Verify second segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g4!mbar!r0!c1!", "med_green", "Step 3c(3): Verify third segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g3!mbar!r0!c1!", "pale_yellow_2", "Step 3c(4): Verify fourth segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s4!g3!mbar!r0!c0!", "brick_red", "Step 3c(5): Verify fifth segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s5!g0!mbar!r0!c1!", "light_brick", "Step 3c(6): Verify sixth segment in the bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 3d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 3d(ii): Verify Y-Axis Title")
                
        """    4. Hover over the highest bar under North America/Stereo Systems. Then hover over Drill down to and select Store Business Sub Region    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s5!g4!mbar!r0!c1!', 'Drill down to->Store Business Sub Region')
        elem = "#jschart_HOLD_0 g.chartPanel rect[class^='riser!s0']"
        utillobj.synchronize_with_number_of_element(elem , 8, 90)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 8, "Step 04b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 04c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 04d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 04e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c5!", "bar_blue1", "Step 04f: Verify bar color") 
        
        """    5. Hover hover the Stereo Systems bar in the West Sub Region. Then hover over Drill down to and select Sale Year/Quarte    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Sale Year/Quarter')
        elem = "#jschart_HOLD_0 g.chartPanel rect[class^='riser!s0']"
        utillobj.synchronize_with_number_of_element(elem, 1, 50)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 4, 1, "Step 05b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 05c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 05d: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 05e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g0!mbar!r0!c0!", "pale_yellow_2", "Step 05f: Verify bar color") 
        
        """    6. Hover over the top bar. Then hover over Drill down to and selected Product Subcategory    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s3!g0!mbar!r0!c0!', 'Drill down to->Product Subcategory')
        elem = "#jschart_HOLD_0 g.chartPanel rect[class^='riser!s0']"
        utillobj.synchronize_with_number_of_element(elem, 4, 50)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 4, "Step 06b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Subcategory", "Step 06c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 06d: verify Y axis title")
        expected_xval_list=['Home Theater Systems', 'Receivers', 'Speaker Kits', 'iPod Docking Station']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 06e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g2!mbar!r0!c0!", "bar_blue1", "Step 06f: Verify bar color") 
        utillobj.switch_to_default_content(pause=1)
        #utillobj.switch_to_default_content(pause=1)
        
        """    7. Click IA > Save As > Type C2226963a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID+"a")
        utillobj.synchronize_with_number_of_element("#runButton img", 1, 15)
        
        """    8. Dismiss IA window    """
        utillobj.infoassist_api_logout()
        
        """    9. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226963a.fex&tool=Chart    """
        utillobj.infoassist_api_edit(Test_Case_ID+"a", 'chart', 'S9970', mrid='mrid', mrpass='mrpass')
        elem1="rect[class^='riser!s4']"
        utillobj.synchronize_with_number_of_element(elem1, 1, 70)
        
        """    10. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_number_of_element("#FormatAutoDrill", 1, 30)
        try:
            disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        except:
            print ("Step:10 There is not such element exception")
        utillobj.asequal(disabled, None, "Step 10a: Active_Report - Verify Autodrill button should be active")
        
        """    11. Click on HTML5 output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        utillobj.synchronize_with_number_of_element("#runButton img", 1, 50)
         
        """    12. Click RUN    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 svg g.risers >g>rect[class^='riser']", 139, 50)
        
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, 'Step 12a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 139, 'Step 12b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 12c(1): Verify first segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g1!mbar!r0!c0!", "pale_green", "Step 12c(2): Verify second segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g4!mbar!r0!c1!", "dark_green", "Step 12c(3): Verify third segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g3!mbar!r0!c1!", "pale_yellow", "Step 12c(4): Verify fourth segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s4!g3!mbar!r0!c0!", "brick_red", "Step 12c(5): Verify fifth segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s5!g0!mbar!r0!c1!", "orange", "Step 12c(6): Verify sixth segment in the bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 12d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 12d(ii): Verify Y-Axis Title")
         
        """    13. Hover over the highest bar under North America/Stereo Systems. Then hover over Drill down to and select Store Business Sub Region    """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s5!g4!mbar!r0!c1!', 'Drill down to->Store Business Sub Region')
        elem = "#MAINTABLE_wbody0 g.chartPanel rect[class^='riser!s0']"
        utillobj.synchronize_with_number_of_element(elem, 8, 50)

        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 8, "Step 13b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 13c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 13d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 13e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c5!", "bar_blue", "Step 13f: Verify bar color") 
        
        """    14. Hover hover the Stereo Systems bar in the West Sub Region. Then hover over Drill down to and select Sale Year/Quarte    """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Sale Year/Quarter')
        elem = "#MAINTABLE_wbody0 g.chartPanel rect[class^='riser!s0']"
        utillobj.synchronize_with_number_of_element(elem, 1, 50)
        
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 4, 1, "Step 14b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 14c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 14d: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 14e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g0!mbar!r0!c0!", "pale_yellow", "Step 14f: Verify bar color") 
        
        
        """    15. Hover over the top bar. Then hover over Drill down to and selected Product Subcategory    """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s3!g0!mbar!r0!c0!', 'Drill down to->Product Subcategory')
        elem = "#MAINTABLE_wbody0 g.chartPanel rect[class^='riser!s']"
        utillobj.synchronize_with_number_of_element(elem, 4, 50)
        
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 4, "Step 15b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Subcategory", "Step 15c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 15d: verify Y axis title")
        expected_xval_list=['Home Theater Systems', 'Receivers', 'Speaker Kits', 'iPod Docking Station']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 15e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!r0!c0!", "bar_blue", "Step 15f: Verify bar color") 
        utillobj.switch_to_default_content(pause=1)
        utillobj.synchronize_with_number_of_element("#applicationButton img", 1, 50)
        
        """    16. Click IA > Save As > Type C2226963b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID+"b")
        utillobj.synchronize_with_number_of_element("#runButton img", 1, 15)
        
        """    17. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226963a.fex&tool=Chart    """
        utillobj.infoassist_api_logout()
        
        utillobj.infoassist_api_edit(Test_Case_ID+"b", 'chart', 'S9970', mrid='mrid', mrpass='mrpass')
        elem1="rect[class^='riser!s4']"
        utillobj.synchronize_with_number_of_element(elem1, 4, 70)
         
        """    18. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_number_of_element("#FormatAutoDrill", 1, 20)
        try:
            disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        except NoSuchElementException:
            print ("Step:18 There is not such element exception")                
        utillobj.asequal(disabled, None, "Step 18a: Active_Report - Verify Autodrill button should be active")
          
        """    19. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()
    
