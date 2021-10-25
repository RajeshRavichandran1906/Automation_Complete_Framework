'''
Created on Jun 6, 2018

@author: BM13368
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2318042&group_by=cases:custom_automation_status&group_id=6&group_order=asc
TestCase_Name : Verify Funnel Chart in others tab under Format menu.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, active_miscelaneous, ia_ribbon
from common.lib import utillity

class C2318043_TestClass(BaseTestCase):

    def test_C2318043(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """
            Step 01 : Sign in to WebFOCUS as a basic user
            http://machine:port/{alias}
            Step 02 :Create new chart using following API link
            http://machine:port/{alias}/ia?tool=chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS7074%2F
            Change format to Active Report
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 65)
        ribbonobj.change_output_format_type('active_report', location='Home')
        
        """
            Expect to see the following Live Preview pane, with the default Vertical Column Bar Chart on the canvas
        """
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval1_list=['0', '10', '20', '30', '40', '50']
        result_obj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 02.1: Verify XY labels")
        result_obj.verify_number_of_riser("TableChart_1", 1, 25, 'Step 02.2: Verify the total number of risers displayed on preview')
        result_obj.verify_data_labels("TableChart_1", ['Series 0','Series 1','Series 2','Series 3','Series 4'], "Step 02:03: Verify data labels in the default chart", custom_css="[class^='legend-label']")
        
        """
            Step 03:Add fields Product, Dollar Sales.
        """
        metadataobj.datatree_field_click('Product', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='xaxisOrdinal-title'", "Product", 15)
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='yaxis-title'", "Dollar Sales", 15)
        
        result_obj.verify_xaxis_title("TableChart_1", "Product", "Step 03.1: Verify -xAxis Title")
        result_obj.verify_yaxis_title("TableChart_1", "Dollar Sales", "Step 03.2: Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval1_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.3: Verify XY labels")
        result_obj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 03.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue', 'Step 3.5: Verify Color')
        
        """
            Step 04:Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        utillobj.switch_to_frame(pause=1)
        
        """
            Verify chart at runtime
        """
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Product', "Step 4.1: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", 'Dollar Sales', "Step 4.2: Verify Y-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 4.3: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 4.4: ')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', 'bar_blue', 'Step 4.5: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales BY Product', 'Step 4.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 4.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 4.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 4.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=1)
        
        """
            Step 05:
            Select Format > Other.
            Select the Special chart menu group.
            From the Special charts, select Pyramid Chart.
            Click OK.
        """
        ribbonobj.select_ribbon_item("Format", "Other")
        ia_ribbonobj.select_other_chart_type('special', 'pyramid', 7,ok_btn_click=True)
        
        """
            Expect to see the Clustered bar chart converted into the Preview pane for Funnel Chart.
        """
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mriser!', 'bar_blue', 'Step 5.1: Verify Color')
        result_obj.verify_legends(['Product', 'Capuccino', 'Espresso'], "#TableChart_1", msg="Step 5.2: Verify funnel chart legend")
        
        """
            Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        utillobj.switch_to_frame(pause=1)
        
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mriser!', 'bar_blue', 'Step 5.1: Verify Color')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g0!mriser!', 'pale_green', 'Step 5.2: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales BY Product', 'Step 5.3: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 5.4: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 5.5: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 5.6: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        result_obj.verify_legends(['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos'], "#MAINTABLE_wbody0", msg="Step 5.7: Verify funnel chart legend")

if __name__ == "__main__":
    unittest.main()