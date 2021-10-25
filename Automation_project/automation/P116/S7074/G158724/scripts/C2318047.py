'''
Created on May 28, 2018

@author: BM13368
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2318047
TestCase_Name : Verify Tag Cloud Chart in others tab under Format menu.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_ribbon, ia_resultarea, active_miscelaneous

class C2318047_TestClass(BaseTestCase):


    def test_C2318047(self):
        
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj =active_miscelaneous.Active_Miscelaneous(self.driver)
        
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        preview_chart_css="TableChart_1"
        runtime_default_tagcloud_chart_css="#MAINTABLE_wbody0 text[class*='riser']"
        
        """
            Step 01 :Right click on folder created in IA and create a new Chart using the GGSALES file.
            From Home tab Select Active Report as Output file format.
        """
        utillobj.infoassist_api_login('chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)

        """
            Step 02:Add fields Product, Unit Sales.
        """
        ribbonobj.switch_ia_tab("Home")
        ia_ribbonobj.select_or_verify_output_type(launch_point='Home', item_select_path='Active Report')
        
        metadataobj.datatree_field_click("Product",2,1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='xaxisOrdinal-title']", "Product", 15)
        
        metadataobj.datatree_field_click("Unit Sales",2,1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='yaxis-title']", "Unit Sales", 15)
        
        """
            Step 03:Click the Run button.
            Expect to see the following Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 40)
        utillobj.switch_to_frame(pause=2)
        
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 3:01: Verify -xAxis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 3:02: Verify -xAxis Title")
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grin...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 03:03 Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 03:04: Verify the total number of risers displayed on preview')
        
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 03:05: Verify  bar color")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Product', 'Step 03:06: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03:07: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03:08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03:09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=1)
        
        """
            Step 04:Select Format > Other >HTML5
            and choose Tag Cloud Chart.
            Expect to see the Clustered bar chart converted into the Preview pane for Tag Cloud Chart.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('html5', 'html5_tagCloud', 4, ok_btn_click=True)
        
        expected_text_list=['Espresso', 'Capuccino']
        ia_resultarea_obj.verify_tagcloud_chart_text("#"+preview_chart_css, expected_text_list, "Step 04:01: Verify the tag cloud text")
        expected_text_color_dict={'Espresso':'bar_blue','Capuccino':'bar_blue'}
        ia_resultarea_obj.verify_tagcloud_chart_text_color("#"+preview_chart_css, expected_text_color_dict, "Step 04:02: Verify tag cloud chart text colors")

        """
            Step 05:Verify the field is added correctly as Product under Detail and Unit Sales under Size.
            Click OK.
            Expect to see the Clustered bar chart converted into the Preview pane for Tag Cloud Chart.
        """
        metadataobj.verify_query_pane_field('Detail', 'Product', 1, "Step 05::01: Verify Query Pane whether Product is added underneath Detail bucket")
        metadataobj.verify_query_pane_field('Size', 'Unit Sales', 1, "Step 05::02: Verify Query Pane whether Unit Sales is added underneath Size bucket")

        """
            Step 06:Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 25)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element(runtime_default_tagcloud_chart_css, 10, 25)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Product', 'Step 06:01: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06:02: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06:03: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06:04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_text_list=['Latte', 'Croissant', 'Biscotti', 'Mug', 'Scone', 'Espresso', 'Coffee Pot', 'Thermos', 'Capuccino', 'Coffee Grinder']
        ia_resultarea_obj.verify_tagcloud_chart_text("#MAINTABLE_wbody0", expected_text_list, "Step 06:05: Verify the tag cloud text")
        expected_text_color_dict={'Espresso':'bar_blue','Capuccino':'bar_blue'}
        ia_resultarea_obj.verify_tagcloud_chart_text_color("#MAINTABLE_wbody0", expected_text_color_dict, "Step 06:06: Verify tag cloud chart text colors")
        

if __name__ == "__main__":
    unittest.main()