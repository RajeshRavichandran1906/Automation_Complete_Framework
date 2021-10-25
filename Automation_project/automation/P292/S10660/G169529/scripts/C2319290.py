'''
Created on Oct 16, 2017

@author: BM13368:Bhagavathi

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2319290&group_by=cases:section_id&group_id=169529&group_order=asc
Test case Name =  New Histogram
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib import utillity

class C2319290_TestClass(BaseTestCase):

    def test_C2319290(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2319290'
        
        driver = self.driver #Driver reference object created
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        
        """
            Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=baseapp/wf_retail
        """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail','P292/S10660_chart_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        """
            Step 02: Format > Chat Type > Other > Bar > Vertical Histogram     
        """
        
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('bar', 'vertical_histogram', 6, ok_btn_click=True)
        
                   
        """
            Step 03: Expand Product > Model > Attributes. Drag Price,Dollars to Measure bucket
        """
        time.sleep(4)
        metaobj.datatree_field_click("Price,Dollars",1,0,'Add To Query','Measure')
        time.sleep(4)
        
        """
            Verification : verify query-pane that Price,Dollars added under Measure Bucket
        """
        metaobj.verify_query_pane_field('Measure', 'CNT.Price,Dollars', 1, "Step 03::01: Verify Query Pane that Price, Dollars added under Measure Bucket")
        metaobj.verify_query_pane_field('Measure', 'PRICE_DOLLARS_BIN_1', 2, "Step 03::02: Verify Query Pane that Price, Dollars added under Measure Bucket")
        
        """"
            Verification : Verify live preview data
        """
        
        parent_css="#TableChart_1 svg>g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 35)
        
        expected_yval_list=['0','3','6','9','12','15']
        expected_xval_list=['20.00', '50.00', '60.00', '70.00', '80.00', '90.00', '100.00', '110.00', '120.00', '140.00', '150.00', '160.00', '170.00', '180.00', '190.00', '210.00', '220.00', '230.00', '240.00', '260.00', '270.00', '280.00', '290.00', '310.00', '330.00', '340.00', '360.00', '370.00', '380.00', '390.00', '440.00', '470.00', '480.00', '490.00', '520.00', '540.00', '590.00', '640.00', '680.00', '690.00', '780.00', '790.00', '880.00', '890.00', '990.00', '1,180.00', '1,290.00', '1,390.00', '1,990.00', '2,240.00', '3,390.00', '3,490.00', '3,990.00']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 03:03: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 03:04: Verify first bar color")
        resultobj.verify_number_of_riser("TableChart_1", 1, 53, 'Step 03:05 Verify the total number of risers displayed on live preview Chart')
        resultobj.verify_xaxis_title("TableChart_1", 'PRICE_DOLLARS_BIN_1', "Step 03:06 : Verify live preview x-axis title")
        resultobj.verify_yaxis_title("TableChart_1",'CNT Price Dollars', "Step 03:07 : Verify live preview y-axis title")
           
        """
            Step 04: Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 svg>g text[class='xaxisOrdinal-title']"
        
        expected_yval_list=['0','3','6','9','12','15']
        expected_xval_list=['20.00', '50.00', '60.00', '70.00', '80.00', '90.00', '100.00', '110.00', '120.00', '140.00', '150.00', '160.00', '170.00', '180.00', '190.00', '210.00', '220.00', '230.00', '240.00', '260.00', '270.00', '280.00', '290.00', '310.00', '330.00', '340.00', '360.00', '370.00', '380.00', '390.00', '440.00', '470.00', '480.00', '490.00', '520.00', '540.00', '590.00', '640.00', '680.00', '690.00', '780.00', '790.00', '880.00', '890.00', '990.00', '1,180.00', '1,290.00', '1,390.00', '1,990.00', '2,240.00', '3,390.00', '3,490.00', '3,990.00']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 04:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 04:02: Verify first bar color")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 53, 'Step 04:03 Verify the total number of risers displayed on live preview Chart')
        bar=['PRICE_DOLLARS_BIN_1:20.00', 'CNT Price Dollars:1']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar!", bar, "Step 04:04: Verify bar value")
        time.sleep(1)
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'PRICE_DOLLARS_BIN_1', "Step 04:04 : Verify live preview x-axis title")
        resultobj.verify_yaxis_title("jschart_HOLD_0",'CNT Price Dollars', "Step 04:05 : Verify live preview y-axis title")
        utillobj.switch_to_default_content(pause=1)
        time.sleep(1)
        obj1=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
            Step 05: Save with name C2319290 and close
        """       
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
                 
        """
           Step 06 :  Logout using API
           http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(4)
        
        """
            Step 07 :Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2319290.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10660_chart_2', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1 svg>g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_number_of_element("#TableChart_1", 1, 65)
      
        expected_yval_list=['0','3','6','9','12','15']
        expected_xval_list=['20.00', '50.00', '60.00', '70.00', '80.00', '90.00', '100.00', '110.00', '120.00', '140.00', '150.00', '160.00', '170.00', '180.00', '190.00', '210.00', '220.00', '230.00', '240.00', '260.00', '270.00', '280.00', '290.00', '310.00', '330.00', '340.00', '360.00', '370.00', '380.00', '390.00', '440.00', '470.00', '480.00', '490.00', '520.00', '540.00', '590.00', '640.00', '680.00', '690.00', '780.00', '790.00', '880.00', '890.00', '990.00', '1,180.00', '1,290.00', '1,390.00', '1,990.00', '2,240.00', '3,390.00', '3,490.00', '3,990.00']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 06:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 06:02: Verify first bar color")
        resultobj.verify_number_of_riser("TableChart_1", 1, 53, 'Step 06:03 Verify the total number of risers displayed on live preview Chart')
        resultobj.verify_xaxis_title("TableChart_1", 'PRICE_DOLLARS_BIN_1', "Step 06:04 : Verify live preview x-axis title")
        resultobj.verify_yaxis_title("TableChart_1",'CNT Price Dollars', "Step 06:05 : Verify live preview y-axis title")
        
        """
            Step 08 :Logout using API
            http://machine:port/alias/service/wf_security_logout.js
        """
    

if __name__ == '__main__':
    unittest.main()



    
     
        