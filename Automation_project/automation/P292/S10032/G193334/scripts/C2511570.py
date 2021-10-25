'''
Created on May 07, 2018

Created by :Bhagavathi

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227773
TestCase Name = Document:Verify the creation of a Document with multiple Reports
'''

import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2511570_TestClass(BaseTestCase):

    def test_C2511570(self):
        
        Test_Case_ID = "C2511570"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)

        """
        Step 01. Sign in to WebFOCUS as a developer user
        Step 02. Navigate to folder: P292_S10032_G193334
        Execute the following URL:
        http://machine:port/{alias}/ia?tool=document&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10032_G193334%2F
        Change the Output type to Active Report.
        Expect to see the following Live Preview pane, with the default Vertical Column Bar Chart on the canvas.
        """
        
        utillobj.infoassist_api_login_('Document', 'baseapp/wf_retail_lite', 'mrid01', 'mrpass01')
        utillobj.synchronize_with_number_of_element("#singleReportCaptionLabel img[src*='preview']", 1, 65)
        
        homeformattype_css="#HomeFormatType img[src*='active_reports']"
        utillobj.verify_object_visible(homeformattype_css, True, "Step 02.1: Verify output format as Active Report")
        
        outputformattype_css="#sbpOutputFormatPanel #sbpOutputFormat img[src*='active_reports']"
        utillobj.verify_object_visible(outputformattype_css, True, "Step 02.2: Verify output format as Active Report")
       
        canvas_css="#iaCanvasPanel"
        utillobj.verify_object_visible(canvas_css, True, "Step 02.3: Verify Document Canvas")
        
        """
        Step 03:From the Measures group, select the Sales sub-group of fields, then select the Gross_Profit field.
        From the Dimensions group, select the Product sub-group, then select the Product,Category field.
        Expect to see the following Live Preview.
        """
        metaobj.datatree_field_click("Cost of Goods",2,1)
        utillobj.synchronize_with_number_of_element("#TableChart_1  div[class^='x']", 2, 10, 1)
        
        metaobj.datatree_field_click("Product,Category",2,1)
        utillobj.synchronize_with_number_of_element("#TableChart_1  div[class^='x']", 18, 10, 1)
        
        """
        Expect to see the following Live Preview for the Report component of the Dashboard.
        """
        coln_list = ['ProductCategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 03.1: Verify report titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 7, 2, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 7, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 03.2: Verify report dataset')
        
        """
        Step 04.From the Insert tab at the top, select Chart for insertion.
        Position the Chart to the right of the Report, by dragging in the border area.
        From the Measures group, select the Sales sub-group, then select the Cost of Goods field.
        From the Dimensions group, select the Product sub-group, then select the Product, Category field.
        """
        
        ribbonobj.select_ribbon_item('Insert', 'Chart')
        
        parent_css="#TableChart_2"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
        
        ribbonobj.repositioning_document_component('5', '1')
        
        metaobj.datatree_field_click("Cost of Goods",2,1)
        utillobj.synchronize_with_number_of_element("#TableChart_2 rect[class^='riser']", 1, 20, 1)
        
        metaobj.datatree_field_click("Product,Category",2,1)
        utillobj.synchronize_with_number_of_element("#TableChart_2 rect[class^='riser']", 7, 20, 1)
        
        """
        Expect to see the following Live Preview for the Dashboard, which now contains a Report and a Chart.

        """
        resultobj.verify_number_of_riser("TableChart_2", 1, 7,'Step 4a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        
        resultobj.verify_riser_chart_XY_labels('TableChart_2', expected_xval_list, expected_yval_list, 
                                               'Step 4b Verify X Y labels')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar", "bar_blue1", "Step 04.c Verify first bar color")
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 04d(i) Verify X-Axis Title")
        yaxis_value="Cost of Goods"
        resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 04e(i) Verify X-Axis Title")
        
        """
        Step 05:Click the Run button to generate the Dashboard.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 35)
        utillobj.switch_to_frame(pause=3)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_1", 1, 30, 1)
        
        """
        Expect to see the following Active Dashboard, containing a report with 7 lines and a Bar Chart with 7 bars.
        Also verify that the values of Cost of Goods are equivalent in both the Dashboard components.
        """
        miscelaneousobj.verify_page_summary('0','7of7records,Page1of1', 'Step 05.1.a: Verify report1 Page summary')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_run_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_run_Ds01.xlsx', "Step 05.1.b: Verify report1")
        
        parentcss="MAINTABLE_wbody1"
        
        resultobj.verify_number_of_riser(parentcss, 1, 7,'Step 5a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Sys...', 'Televisions', 'Video Prod...']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        
        resultobj.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, 'Step 5b Verify X Y labels')
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g0!mbar", "bar_blue1", "Step 05.c Verify first bar color")
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title(parentcss, xaxis_value, "Step 05d(i) Verify X-Axis Title")
        yaxis_value="Cost of Goods"
        resultobj.verify_yaxis_title(parentcss, yaxis_value, "Step 05e(i) Verify X-Axis Title")
        element_css="#MAINTABLE_wbody1_ft table tbody td div"
        utillobj.verify_element_text(element_css, "Cost of Goods BY Product Category", 'Step 5. Verify Chart title')
        
        
        """
        Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()