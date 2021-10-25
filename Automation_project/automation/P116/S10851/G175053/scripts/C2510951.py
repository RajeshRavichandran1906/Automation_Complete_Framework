'''
Created on Jun 12, 2018

@author: BM13368
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2510951&group_by=cases:section_id&group_id=175053&group_order=asc
TestCase_Name : AHTML:Stacked Bar Bucket Syntax X-Axis labels - ACT-314
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, active_miscelaneous, ia_ribbon
from common.lib import utillity

class C2510951_TestClass(BaseTestCase):

    def test_C2510951(self):
        
        """ TESTCASE VARIABLES """
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        
        """
            Step 01 : Sign in to WebFOCUS
            http://machine:port/{alias}
            Step 02 :Navigate to folder: P292_S10032_G157266
            Execute the following URL:
            http://machine:port/{alias}/ia?tool=chart&master=baseapp/car&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10032_G157266%2F
            Change the Output type to Active Report.
        """
        utillobj.infoassist_api_login('chart','ibisamp/car','P116/S10851_1', 'mrid', 'mrpass')
        utillobj.wait_for_page_loads(20)
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        ribbonobj.change_output_format_type('active_report')
        
        """
            Step 03 : Click on Format tab and select Other Chart, then Stacked Bar
            Step 04 : Click Ok
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('bar', 'bar_stacked', 2, ok_btn_click=True)
        time.sleep(3)
        preview_chart_css="TableChart_1"
        
        
        expected_yval_list=['0', '40', '80', '120', '160', '200']
        expected_xval_list=['Group4','Group3','Group2','Group1','Group0']
        resultobj.verify_riser_chart_XY_labels(preview_chart_css, expected_xval_list, expected_yval_list, 'Step 02:01: X and Y axis labels')
        utillobj.verify_chart_color(preview_chart_css, "riser!s0!g4!mbar!", "bar_blue", "Step 02:02: Verify first bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s1!g4!mbar!", "pale_green", "Step 02:03: Verify first bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s2!g4!mbar!", "dark_green", "Step 02:03: Verify first bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s3!g0!mbar!", "pale_yellow_2", "Step 02:04: Verify first bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s4!g0!mbar!", "brick_red", "Step 02:05: Verify first bar color")
        resultobj.verify_riser_legends(preview_chart_css,['Series0','Series1','Series2','Series3','Series4'], 'Step 02.07 : Verify chart legends')
        resultobj.verify_number_of_riser(preview_chart_css, 1, 25, 'Step 02.08: Verify Number chart segment')
       
        """
            Step 05 : Select COUNTRY for Horizontal Axis, DEALER_COST for Vertical Axis, and CAR for Color
        """
        metaobj.datatree_field_click('COUNTRY', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class^='xaxis'][class$='title']", "COUNTRY", 15)
        
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class^='yaxis-title']", "DEALER_COST", 15)
        
        metaobj.datatree_field_click("CAR",1,1,'Add To Query','Color')
        utillobj.synchronize_with_visble_text("#TableChart_1 text.legend-title", "CAR", 20)
        
        
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels(preview_chart_css, expected_xval_list, expected_yval_list, 'Step 05:01: X and Y axis labels')
        utillobj.verify_chart_color(preview_chart_css, "riser!s0!g2!mbar!", "bar_blue", "Step 05:02: Verify first bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s1!g4!mbar!", "pale_green", "Step 05:03: Verify first bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s2!g4!mbar!", "dark_green", "Step 05:04: Verify first bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s3!g3!mbar!", "pale_yellow_2", "Step 05:05: Verify first bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s4!g0!mbar!", "brick_red", "Step 05:06: Verify first bar color")
        resultobj.verify_riser_legends(preview_chart_css,['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], 'Step 05.07 : Verify chart legends')
        resultobj.verify_number_of_riser(preview_chart_css, 1, 10, 'Step 05.08: Verify Number chart segment')
        
        
        """
            Step 06 : Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 35)
        utillobj.switch_to_frame(pause=2)
        runtime_chart_css="MAINTABLE_wbody0_f"
        
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels(runtime_chart_css, expected_xval_list, expected_yval_list, 'Step 06:01: X and Y axis labels')
        utillobj.verify_chart_color(runtime_chart_css, "riser!s0!g2!mbar!", "bar_blue", "Step 06:02: Verify first bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s1!g4!mbar!", "pale_green", "Step 06:03: Verify first bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s2!g4!mbar!", "dark_green", "Step 06:04: Verify first bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s3!g3!mbar!", "pale_yellow_2", "Step 06:05: Verify first bar color")
        utillobj.verify_chart_color(runtime_chart_css, "riser!s4!g0!mbar!", "brick_red", "Step 06:06: Verify first bar color")
        resultobj.verify_riser_legends(runtime_chart_css,['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], 'Step 06.07 : Verify chart legends')
        resultobj.verify_number_of_riser(runtime_chart_css, 1, 10, 'Step 06.08: Verify Number chart segment')
        miscobj.verify_chart_title("MAINTABLE_wbody0_ft", 'DEALER_COST by CAR, COUNTRY', "Step 06:09:Verify active chart title")
        miscobj.verify_acitive_chart_toolbar("#MAINTABLE_wmenu0", ['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], "Step 06:10:Verify active chart toolbar menu")
        

if __name__ == "__main__":
    unittest.main()