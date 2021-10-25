'''
Created on Oct 12, 2017

@author: BM13368
TestCase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2321262&group_by=cases:section_id&group_order=asc&group_id=169528
TestCase_Name : New Bucketized Horizontal Dual-axis Clustered Bar Chart
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_ribbon

class C2321238_TestClass(BaseTestCase):


    def test_C2321238(self):
        
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2321238'
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        runtime_chart_css="jschart_HOLD_0"
        preview_chart_css="TableChart_1"
        
        """
            Step 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=ibisamp/car
        """
        utillobj.infoassist_api_login('chart','ibisamp/car','P292/S10660_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
                
        """
            Step 02 : Format > Chart Type > Other > HTML5 > Mekko Chart
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('html5', 'html5_Mekko', 2, ok_btn_click=True)
        
        """
            Verification : Expect to see the following Mekko Chart Preview.
        """
        default_label_css="#"+preview_chart_css+" svg>g text[class^='xaxis'][class*='labels']"
        utillobj.synchronize_with_number_of_element(default_label_css, 5, 65)
        
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        expected_xval_list=['Group4','Group3','Group2','Group1','Group0']
        resultobj.verify_riser_chart_XY_labels(preview_chart_css, expected_xval_list, expected_yval_list, 'Step 02:01: X and Y axis labels')
        utillobj.verify_chart_color(preview_chart_css, "riser!s0!g4!mbar!", "bar_blue", "Step 02:02: Verify first bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s1!g4!mbar!", "pale_green", "Step 02:03: Verify first bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s2!g4!mbar!", "dark_green", "Step 02:03: Verify first bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s3!g0!mbar!", "pale_yellow_2", "Step 02:04: Verify first bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s4!g0!mbar!", "brick_red", "Step 02:05: Verify first bar color")
        resultobj.verify_riser_legends(preview_chart_css,['Series0','Series1','Series2','Series3','Series4'], 'Step 02.07 : Verify chart legends')
        resultobj.verify_number_of_riser(preview_chart_css, 1, 25, 'Step 02.08: Verify Number chart segment')
        expected_data_labels=['175', '150', '125', '100', '75']
        resultobj.verify_data_labels(preview_chart_css, expected_data_labels, "Step 02:09 : Verify data labels top level x labels", custom_css="svg>g text[class*='stackTotalLabel']")
        time.sleep(1)
        
        """
            Step 03 : Add Car to the Horizontal axis bucket.
            Add Dealer_Cost and Weight to the Vertical axis bucket.
        """
        xaxis_title_css="#"+preview_chart_css+" svg>g text[class='xaxisOrdinal-title']"
        visible_xaxis_element_text="CAR"
        expire_time=50
        
        yaxis_title_css="#"+preview_chart_css+" svg>g text[class='yaxis-title']"
        visible_yaxis_element_text="DEALER_COST"
        legend_css="#TableChart_1 [class*='legend-labels']"
        
        metadataobj.datatree_field_click('CAR', 2, 1)
        utillobj.synchronize_with_visble_text(xaxis_title_css, visible_xaxis_element_text, expire_time)
        
        metadataobj.datatree_field_click('DEALER_COST', 2, 1)
        utillobj.synchronize_with_visble_text(yaxis_title_css, visible_yaxis_element_text, expire_time)
        
        metadataobj.datatree_field_click('WEIGHT', 2, 1)
        utillobj.synchronize_with_number_of_element(legend_css, 2, 35)
        
        """
            Verification : Expect to see the following Mekko Chart Preview after adding fields.
        """
        
        resultobj.verify_xaxis_title(preview_chart_css, 'CAR', "Step 03:01: Verify X-Axis Title")
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'A...', 'P...', 'T...', 'T', 'D']
        resultobj.verify_riser_chart_XY_labels(preview_chart_css, expected_xval_list, expected_yval_list, 'Step 03:02: X and Y axis labels',x_axis_label_length=1)
        expected_datalabel=[]
        resultobj.verify_data_labels(preview_chart_css, expected_datalabel, "Step 03:03: Verify data labels in the top of the chart")
        utillobj.verify_chart_color(preview_chart_css, "riser!s0!g2!mbar!", "bar_blue", "Step 03:04: Verify lower bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s1!g2!mbar!", "pale_green", "Step 03:05: Verify top bar color")
        resultobj.verify_riser_legends(preview_chart_css,['DEALER_COST','WEIGHT'], 'Step 03.09 : Verify chart legends')
        resultobj.verify_number_of_riser(preview_chart_css,1,20, 'Step 03.10: Verify Number chart segment')
        
        """
            Step 04 : Click the Run button.
            Hover over the upper block for BMW.
            Hover over the lower block for BMW.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 60)
        utillobj.switch_to_frame(pause=2)
        
        xaxis_title_css="#"+runtime_chart_css+" text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(xaxis_title_css, "CAR", 60)
        
        resultobj.verify_xaxis_title(runtime_chart_css, 'CAR', "Step 04:01: Verify X-Axis Title")
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'A...', 'P...', 'T...', 'T', 'D']
        resultobj.verify_riser_chart_XY_labels(runtime_chart_css, expected_xval_list, expected_yval_list, 'Step 04:02: X and Y axis labels',x_axis_label_length=1)
        utillobj.verify_chart_color(runtime_chart_css, "riser!s0!g2!mbar!", "bar_blue", "Step 04:03: Verify lower bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s1!g2!mbar!", "pale_green", "Step 04:04: Verify top bar color")
        resultobj.verify_riser_legends(runtime_chart_css,['DEALER_COST','WEIGHT'], 'Step 04.05 : Verify chart legends')
        resultobj.verify_number_of_riser(runtime_chart_css,1,20, 'Step 04.06: Verify Number chart segment')
        time.sleep(8)
        expected_tooltip_list=['CAR:BMW', 'WEIGHT:11,300  (18.59%)']
        resultobj.verify_default_tooltip_values(runtime_chart_css, "riser!s1!g2!mbar!", expected_tooltip_list, "Step 4:07: Verify Upper bar value")
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500  (81.41%)']
        resultobj.verify_default_tooltip_values(runtime_chart_css, "riser!s0!g2!mbar!", expected_tooltip_list, "Step 4:08: Verify Lower bar value")
        expected_datalabel=['60,800', '28,700', '26,256', '23,450', '18,940', '7,634', '7,491', '6,533', '5,1...', '4,...']
        resultobj.verify_data_labels(runtime_chart_css, expected_datalabel, "Step 04:09: Verify data labels in the top of the chart", custom_css="svg>g>g .groupPanel text[class*='stackTotalLabel']", data_label_length=1)
        
        
        """
            Step 05 : Add Country to the Color By bucket.
            Click the Run button.
            Hover over the lower block for BMW.
        """
        utillobj.switch_to_default_content(pause=1)
        metadataobj.datatree_field_click("COUNTRY",1,1,'Add To Query','Color')
        utillobj.synchronize_with_visble_text("#queryTreeColumn div table tbody tr:nth-child(10)", "COUNTRY", 40)
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 60)
        utillobj.switch_to_frame(pause=2)
        
        parent_css="#"+runtime_chart_css+" text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(parent_css, "CAR", 45)
        
        resultobj.verify_xaxis_title(runtime_chart_css, 'CAR', "Step 05:01: Verify X-Axis Title")
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'A...', 'P...', 'T...', 'T', 'D']
        resultobj.verify_riser_chart_XY_labels(runtime_chart_css, expected_xval_list, expected_yval_list, 'Step 05:02: X and Y axis labels', x_axis_label_length=1)
        utillobj.verify_chart_color(runtime_chart_css, "riser!s8!g2!mbar!", "moss_green", "Step 05:04: Verify first bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s4!g6!mbar!", "brick_red", "Step 05:05: Verify 2nd bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s0!g4!mbar!", "bar_blue", "Step 05:06: Verify third bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s4!g0!mbar!", "brick_red", "Step 05:07: Verify four bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s0!g5!mbar!", "bar_blue", "Step 05:08: Verify five bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s8!g1!mbar!", "moss_green", "Step 05:09: Verify six bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s2!g7!mbar!", "dark_green", "Step 05:10: Verify seven bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s0!g9!mbar!", "bar_blue", "Step 05:11: Verify eight bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s6!g8!mbar!", "periwinkle_gray", "Step 04512: Verify nine bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s9!g2!mbar!", "pale_yellow1", "Step 05:13: Verify ten bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s5!g6!mbar!", "light_brick", "Step 05:14: Verify top bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s1!g4!mbar!", "pale_green", "Step 05:15: Verify lower bar color")
        time.sleep(3)
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500  (81.41%)', 'COUNTRY:W GERMANY']
        resultobj.verify_default_tooltip_values(runtime_chart_css, "riser!s8!g2!mbar!", expected_tooltip_list, "Step 05:16 Verify Lower bar value")
        expected_legends=['DEALER_COST : ENGLAND', 'WEIGHT : ENGLAND', 'DEALER_COST : FRANCE', 'WEIGHT : FRANCE', 'DEALER_COST : ITALY', 'WEIGHT : ITALY', 'DEALER_COST : JAPAN', 'WEIGHT : JAPAN', 'DEALER_COST : W GERMANY', 'WEIGHT : W GERMANY']
        resultobj.verify_riser_legends(runtime_chart_css,expected_legends, 'Step 05.17 : Verify chart legends')
        resultobj.verify_number_of_riser(runtime_chart_css,1,20, 'Step 05.18: Verify Number chart segment')
        expected_datalabel=['60,800', '28,700', '26,256', '23,450', '18,940', '7,634', '7,491', '6,533', '5,...', '4,...']
        resultobj.verify_data_labels(runtime_chart_css, expected_datalabel, "Step 05:19: Verify data labels in the top of the chart", custom_css="svg>g>g .groupPanel text[class*='stackTotalLabel']", data_label_length=1)
        
        """
            Step 06 : Add Sales to the Tool Tip bucket.
            Click the Run button.
            Hover over the lower area for Jaguar.
        """
        utillobj.switch_to_default_content(pause=1)
        metadataobj.datatree_field_click("SALES",1,1,'Add To Query','Tooltip')
        utillobj.synchronize_with_visble_text("#queryTreeColumn div table tbody tr:nth-child(12)", "SALES", 50)
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 60)
        
        utillobj.switch_to_frame(pause=2)
        parent_css="#"+runtime_chart_css+" text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(parent_css, "CAR", 45)
        
        resultobj.verify_xaxis_title(runtime_chart_css, 'CAR', "Step 06:01: Verify X-Axis Title")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'A...', 'P...', 'T...', 'T', 'D']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resultobj.verify_riser_chart_XY_labels(runtime_chart_css, expected_xval_list, expected_yval_list, 'Step 06:02: X and Y axis labels', x_axis_label_length=1)
        utillobj.verify_chart_color(runtime_chart_css, "riser!s8!g2!mbar!", "moss_green", "Step 06:03: Verify first bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s4!g6!mbar!", "brick_red", "Step 06:04: Verify first bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s0!g4!mbar!", "bar_blue", "Step 06:05: Verify first bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s4!g0!mbar!", "brick_red", "Step 06:06: Verify first bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s0!g5!mbar!", "bar_blue", "Step 06:07: Verify first bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s8!g1!mbar!", "moss_green", "Step 06:08: Verify first bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s2!g7!mbar!", "dark_green", "Step 06:09: Verify first bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s0!g9!mbar!", "bar_blue", "Step 06:10: Verify first bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s6!g8!mbar!", "periwinkle_gray", "Step 06:11 Verify first bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s9!g2!mbar!", "pale_yellow1", "Step 06:12: Verify first bar color")
        resultobj.verify_number_of_riser(runtime_chart_css,1,20, 'Step 06.13: Verify Number chart segment')
        expected_legends=['DEALER_COST : ENGLAND', 'WEIGHT : ENGLAND', 'DEALER_COST : FRANCE', 'WEIGHT : FRANCE', 'DEALER_COST : ITALY', 'WEIGHT : ITALY', 'DEALER_COST : JAPAN', 'WEIGHT : JAPAN', 'DEALER_COST : W GERMANY', 'WEIGHT : W GERMANY']
        resultobj.verify_riser_legends(runtime_chart_css,expected_legends, 'Step 06.14 : Verify chart legends')
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500  (81.41%)', 'COUNTRY:W GERMANY', 'SALES:80390']
        resultobj.verify_default_tooltip_values(runtime_chart_css, "riser!s8!g2!mbar!", expected_tooltip_list, "Step 06:15: Verify Lower bar value")
        expected_datalabel=['60,800', '28,700', '26,256', '23,450', '18,940', '7,634', '7,491', '6,533', '5,...', '4,...']
        resultobj.verify_data_labels(runtime_chart_css, expected_datalabel, 'Step 06:16: Verify data labels', custom_css="svg>g>g .groupPanel text[class*='stackTotalLabel']", data_label_length=1)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(1)
        obj1=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
            Step 07 : Click Save in the toolbar > Save as "C2321238" > Click Save
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 08 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(4)
        
        """
            Step 09 : Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2321238.fex
            Expect to see the regenerated Mekko Chart.
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        
        xaxis_title_css="#"+preview_chart_css+" text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(xaxis_title_css, "CAR", 65)
       
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'A...', 'P...', 'T...', 'T', 'D']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 08:01: X and Y axis labels', x_axis_label_length=1)
        resultobj.verify_xaxis_title("TableChart_1", 'CAR', "Step 08:02: Verify -xAxis Title")
        utillobj.verify_chart_color("TableChart_1", "riser!s8!g2!mbar!", "moss_green", "Step 08:03: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g6!mbar!", "brick_red", "Step 08:04: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g4!mbar!", "bar_blue", "Step 08:05: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mbar!", "brick_red", "Step 08:06: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g5!mbar!", "bar_blue", "Step 08:07: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s8!g1!mbar!", "moss_green", "Step 08:08: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g7!mbar!", "dark_green", "Step 08:09: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g9!mbar!", "bar_blue", "Step 08:10: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s6!g8!mbar!", "periwinkle_gray", "Step 08:11 Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s9!g2!mbar!", "pale_yellow1", "Step 08:12: Verify first bar color")
        resultobj.verify_number_of_riser('TableChart_1',1,20, 'Step 08.13: Verify Number of risers')
        expected_legends=['DEALER_COST : ENGLAND', 'WEIGHT : ENGLAND', 'DEALER_COST : FRANCE', 'WEIGHT : FRANCE', 'DEALER_COST : ITALY', 'WEIGHT : ITALY', 'DEALER_COST : JAPAN', 'WEIGHT : JAPAN', 'DEALER_COST : W GERMANY', 'WEIGHT : W GERMANY']
        resultobj.verify_riser_legends('TableChart_1',expected_legends, 'Step 08.14: Verify chart legends')
        expected_datalabel=['60,800', '28,700', '26,256', '23,450', '18,940', '7,634', '7,491', '6,533', '5,...', '4,...']
        resultobj.verify_data_labels("TableChart_1", expected_datalabel, "Step 08:15: Verify data labels in the top of the chart", custom_css="svg>g>g .groupPanel text[class*='stackTotalLabel']", data_label_length=1)
        
        """
            Step 10:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()