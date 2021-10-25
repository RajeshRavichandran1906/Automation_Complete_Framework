'''
Created on 13-Mar-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2231112
TestCase Name = Test drilling all the way down and up a long hierarchy path - AHTML
'''

from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity  
import time, unittest

class C2231112_TestClass(BaseTestCase):
    
    def test_C2231112(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = "C2231112_"+browser_type
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
      
        """    
            STEP 01 : Open IA_Chart for edit using the API 
            http://machine:port/ibi_apps/ia?tool=Chart&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Chart.fex&tool=Chart   
        """
        utillobj.infoassist_api_edit("IA-Chart", 'chart', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("text[class='legend-title']", 'Sale Year', 180)
        
        """    
            STEP 02 : Click HTML5 and select Active Report format from format group in Home tab   
        """
        ribbonobj.change_output_format_type('active_report')
        utillobj.synchronize_with_visble_text("#HomeFormatType", 'Active Report', 60)
        
        """    
            STEP 03 : Click Format tab > Autodrill button    
        """
        ribbonobj.switch_ia_tab("Format")
        if self.driver.find_element_by_css_selector("#FormatAutoDrillCluster").value_of_css_property("Visibility") == 'hidden':
            autolink_altbtn=self.driver.find_element_by_css_selector("#FormatAutoDrillCluster_altButton img")
            utillobj.default_left_click(object_locator=autolink_altbtn)
            time.sleep(2)
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, 15)
        
        """    
            STEP 04 : Click RUN    
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("iframe[id^='ReportIframe']", 1, 40)
        frame_size = self.driver.find_element_by_css_selector("iframe[id^='ReportIframe']").location
        utillobj.switch_to_frame(pause=3)
        utillobj.switch_to_frame(pause=3, frame_css = 'iframe[src]')
        utillobj.browser_x = frame_size['x']
        utillobj.browser_y = frame_size['y']
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='legend-title']", 'Sale Year', 80)
        
        """
            STEP 04.1 : Verify output
        """
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 4a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 139, 'Step 4b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 4c(1): Verify first segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g1!mbar!r0!c0!", "pale_green", "Step 4c(2): Verify second segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g0!mbar!r0!c1!", "dark_green", "Step 4c(3): Verify third segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g1!mbar!r0!c1!", "pale_yellow", "Step 4c(4): Verify fourth segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s4!g1!mbar!r0!c0!", "brick_red", "Step 4c(5): Verify fifth segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s5!g0!mbar!r0!c1!", "orange", "Step 4c(6): Verify sixth segment in the bar color")
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 4d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 4d(ii): Verify Y-Axis Title")
       
        """    
            STEP 05 : Hover over the top bar (2016) in North America/Stereo Systems. Then hover over the Drill down to and select Store Business Sub Region.    
        """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s5!g4!mbar!r0!c1!', 'Drill down to->Store Business Sub Region')
        utillobj.synchronize_with_visble_text("foreignObject span a", 'Home', 40)
        
        """
            STEP 05.1 : Verify output
        """
        #a =['Store Business Sub Region:Midwest', 'Product Category:Stereo Systems', 'Revenue:$6,990,028.64', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to Store Business Region', 'Drill down to']
        #resultobj.verify_default_tooltip_values('MAINTABLE_wbody0','riser!s0!g0!mbar!r0!c3!',a,"Step 05a: Verify Midwest tooltip values")
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 8, "Step 05b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 05c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 05d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c5!", "bar_blue", "Step 05f: Verify bar color") 
        
        """    
            STEP 06 : Hover over West and drill down to Store Country    
        """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Store Country')
        utillobj.synchronize_with_visble_text("foreignObject span:last-child", 'West', 40) 
       
        """
            STEP 06.1 : Verify output 
        """
        #a =['Store Country:United States', 'Product Category:Stereo Systems', 'Revenue:$52,755,657.67', 'Sale Year:2016', 'Restore Original', 'Drill up to Store Business Sub Region', 'Drill down to']
        #resultobj.verify_default_tooltip_values('MAINTABLE_wbody0','riser!s0!g0!mbar!r0!c0!',a,"Step 06a: Verify Midwest tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 1, "Step 06b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 06c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 06d: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 06e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 06f: Verify bar color") 
       
        """    
            STEP 07 : Hover over United States and drill down to Store State Province    
        """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c0!', 'Drill down to->Store State Province')
        utillobj.synchronize_with_visble_text("foreignObject span:last-child", 'United States', 40) 
        
        """
            STEP 07.1 : Verify output
        """
        #a =['Store State Province:Idaho', 'Product Category:Stereo Systems', 'Revenue:$47,337,478.19', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to Store Country', 'Drill down to']
        #resultobj.verify_default_tooltip_values('MAINTABLE_wbody0','riser!s0!g0!mbar!r0!c4!',a,"Step 07a: Verify Midwest tooltip values")
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 9, "Step 07b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 07c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 07d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 07e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c4!", "bar_blue", "Step 07f: Verify bar color") 
        
        """    
            STEP 08 : Hover over California and drill down to Store City    
        """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c1!', 'Drill down to->Store City')
        utillobj.synchronize_with_visble_text("foreignObject span:last-child", 'California', 40)
         
        """
            STEP 08.1 : Verify output
        """
        #a =['Store City:Los Angeles', 'Product Category:Stereo Systems', 'Revenue:$663,518.80', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to Store State Province', 'Drill down to']
        #resultobj.verify_default_tooltip_values('MAINTABLE_wbody0','riser!s0!g0!mbar!r0!c0!',a,"Step 08a: Verify Midwest tooltip values")
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 3, "Step 08b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 08c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 08d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 08e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c1!", "bar_blue", "Step 08f: Verify bar color") 
        
        """    
            STEP 09 : Hover over San Diego and drill down to Store Postal Code    
        """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c1!', 'Drill down to->Store Postal Code')
        utillobj.synchronize_with_visble_text("foreignObject span:last-child", 'San Diego', 40)
        
        """
            STEP 09.1 : Verify output
        """
        #a =['Store Postal Code:92101', 'Product Category:Stereo Systems', 'Revenue:$810,080.62', 'Sale Year:2016', 'Restore Original', 'Drill up to Store City', 'Drill down to']
        #resultobj.verify_default_tooltip_values('MAINTABLE_wbody0','riser!s0!g0!mbar!r0!c0!',a,"Step 09a: Verify Midwest tooltip values")
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 1, "Step 09b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 09c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 09d: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 09e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 09f: Verify bar color") 
       
        """   
            STEP 10 : Hover over 92101 and drill down to Store Name    
        """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c0!', 'Drill down to->Store Name')
        utillobj.synchronize_with_visble_text("foreignObject span:last-child", '92101', 40)
        
        """
            STEP 10.1 : Verify output
        """
        #a =['Store Name:San Diego','Product Category:Stereo Systems', 'Revenue:$810,080.62', 'Sale Year:2016', 'Restore Original', 'Drill up to Store Postal Code', 'Drill down to']
        #resultobj.verify_default_tooltip_values('MAINTABLE_wbody0','riser!s0!g0!mbar!r0!c0!',a,"Step 10a: Verify Midwest tooltip values")
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 1, "Step 10b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 10c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 10d: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 10e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 10f: Verify bar color") 
        
        """    
            STEP 11 : Hover over San Diego and select Drill up to Store Postal Code    
        """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c0!', 'Drill up to Store Postal Code')
        utillobj.synchronize_with_visble_text("foreignObject span:last-child", 'San Diego', 40)
        
        """
            STEP 11.1 : Verify output
        """
        #a =['Store Postal Code:92101', 'Product Category:Stereo Systems', 'Revenue:$810,080.62', 'Sale Year:2016', 'Restore Original', 'Drill up to Store City', 'Drill down to']
        #resultobj.verify_default_tooltip_values('MAINTABLE_wbody0','riser!s0!g0!mbar!r0!c0!',a,"Step 11a: Verify Midwest tooltip values")
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 1, "Step 11b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 11c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 11d: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 11e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 11f: Verify bar color") 
       
        """    
            STEP 12 : Hover over 92101 and select Drill up to Store City    
        """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c0!', 'Drill up to Store City')
        utillobj.synchronize_with_visble_text("foreignObject span:last-child", 'California', 40)
        
        """
            STEP 12.1 : Verify output
        """
        #a =['Store City:Los Angeles', 'Product Category:Stereo Systems', 'Revenue:$663,518.80', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to Store State Province', 'Drill down to']
        #resultobj.verify_default_tooltip_values('MAINTABLE_wbody0','riser!s0!g0!mbar!r0!c0!',a,"Step 12a: Verify Midwest tooltip values")
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 3, "Step 12b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 12c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 12d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 12e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c1!", "bar_blue", "Step 12f: Verify bar color") 
        
        """    
            STEP 13 : Hover over San Diego and select Drill up to Store State Province    
        """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c1!', 'Drill up to Store State Province')
        utillobj.synchronize_with_visble_text("foreignObject span:last-child", 'United States', 40)
        
        """
            STEP 13.1 : Verify output
        """
        #a =['Store State Province:Idaho', 'Product Category:Stereo Systems', 'Revenue:$47,337,478.19', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to Store Country', 'Drill down to']
        #resultobj.verify_default_tooltip_values('MAINTABLE_wbody0','riser!s0!g0!mbar!r0!c4!',a,"Step 13a: Verify Midwest tooltip values")
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 9, "Step 13b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 13c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 13d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 13e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c4!", "bar_blue", "Step 13f: Verify bar color") 
        
        """    
            STEP 14 : Hover over California and select Drill up to Store Country   
        """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c1!', 'Drill up to Store Country')
        utillobj.synchronize_with_visble_text("foreignObject span:last-child", 'West', 40) 
        
        """
            STEP 14.1 : Verify output 
        """
        #a =['Store Country:United States', 'Product Category:Stereo Systems', 'Revenue:$52,755,657.67', 'Sale Year:2016', 'Restore Original', 'Drill up to Store Business Sub Region', 'Drill down to']
        #resultobj.verify_default_tooltip_values('MAINTABLE_wbody0','riser!s0!g0!mbar!r0!c0!',a,"Step 14a: Verify Midwest tooltip values")
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 1, "Step 14b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 14c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 14d: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 14e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 14f: Verify bar color") 
        
        """    
            STEP 15 : Hover over United States and select Drill up to Store Business Sub Region    
        """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c0!', 'Drill up to Store Business Sub Region')
        utillobj.synchronize_with_visble_text("foreignObject span a", 'Home', 40)
        
        """
            STEP 15.1 : Verify output 
        """
        #a =['Store Business Sub Region:Midwest', 'Product Category:Stereo Systems', 'Revenue:$6,990,028.64', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to Store Business Region', 'Drill down to']
        #resultobj.verify_default_tooltip_values('MAINTABLE_wbody0','riser!s0!g0!mbar!r0!c3!',a,"Step 15a: Verify Midwest tooltip values")
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 8, "Step 15b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 15c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 15d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 15e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c5!", "bar_blue", "Step 15f: Verify bar color") 
        
        """    
            STEP 16 : Hover over West and select Drill up to Store Business Region    
        """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c7!', 'Drill up to Store Business Region')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f .legend-clip text[class='legend-labels!s5!']", '2016', 40)
        
        """
            STEP 16.1 : Verify output
        """
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 16a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 139, 'Step 16b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 16c(1): Verify first segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g1!mbar!r0!c0!", "pale_green", "Step 16c(2): Verify second segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g0!mbar!r0!c1!", "dark_green", "Step 16c(3): Verify third segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g1!mbar!r0!c1!", "pale_yellow", "Step 16c(4): Verify fourth segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s4!g1!mbar!r0!c0!", "brick_red", "Step 16c(5): Verify fifth segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s5!g0!mbar!r0!c1!", "orange", "Step 16c(6): Verify sixth segment in the bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 16d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 16d(ii): Verify Y-Axis Title")
        utillobj.switch_to_default_content()
        utillobj.take_screenshot(self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2231112_Actual_step10', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    
            STEP 17 : Click IA > Save As > Type C2231112 > click Save    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.infoassist_api_logout()
        
        """    
            STEP 18 : Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2231112.fex&tool=Chart    
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S9970', mrid='mrid', mrpass='mrpass')
         
        """    
            STEP 19 : Click format tab and Verify Autodrill button is still selected    
        """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, 20)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 19a: Active_Report - Verify Autodrill button should be active")
         
        """    
            STEP 20 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        
if __name__ == '__main__':
    unittest.main()
    
