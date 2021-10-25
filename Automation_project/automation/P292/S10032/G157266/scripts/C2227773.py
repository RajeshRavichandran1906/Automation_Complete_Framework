'''
Created on Dec 16, 2017

@author: Magesh/ Updated by :Bhagavathi

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227773
TestCase Name = Document:Verify the creation of a Document with multiple Reports
'''

import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2227773_TestClass(BaseTestCase):

    def test_C2227773(self):
        
        Test_Case_ID = "C2227773"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)

        """
        Step 01: Sign in to WebFOCUS as a developer user
        http://machine:port/{alias}
        """
        
        utillobj.infoassist_api_login_('Document', 'baseapp/wf_retail_lite', 'mrid01', 'mrpass01')
        
        """
        Expect to see the following default development canvas with output format as Active Report
        """
        utillobj.synchronize_with_number_of_element("#singleReportCaptionLabel img[src*='preview']", 1, 65)
        
        """
        Step 02: Navigate to folder: P292_S10032_G157266
        Execute the following URL:
        http://machine:port/{alias}/ia?tool=document&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10032_G157266%2F
        Change the Output type to Active Report.
        Step 03:Create the first report by selecting Quantity,Sold from the Sales group under Measures and Product,Categoryfrom from the Product group under Dimensions.
        """
        
        homeformattype_css="#HomeFormatType img[src*='active_reports']"
        utillobj.verify_object_visible(homeformattype_css, True, "Step 01.1: Verify output format as Active Report")
        outputformattype_css="#sbpOutputFormatPanel #sbpOutputFormat img[src*='active_reports']"
        utillobj.verify_object_visible(outputformattype_css, True, "Step 01.2: Verify output format as Active Report")
        time.sleep(5)
        
        metaobj.datatree_field_click("Quantity,Sold",2,1)
        utillobj.synchronize_with_number_of_element("#TableChart_1  div[class^='x']", 3, 20)
        
        metaobj.datatree_field_click("Product,Category",2,1)
        utillobj.synchronize_with_number_of_element("#TableChart_1  div[class^='x']", 18, 20)
        
        """
        Expect to see the first report component on the canvas.
        """
        coln_list = ['ProductCategory', 'QuantitySold']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 02.1: Verify report titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 7, 2, Test_Case_ID+"_Ds01.xlsx", no_of_cells=4)
        ia_resultobj.verify_report_data_set('TableChart_1', 7, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 02.2: Verify report dataset', no_of_cells=4)
        
        """
        Step 04: From the tool bar at the top, click Insert, then Report.
        """
        
        ribbonobj.select_ribbon_item('Insert', 'Report')
        parent_css="#TableChart_2"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        
        """
        Drag the new report to the right of the first report.
        """
        source_elem = driver.find_element_by_css_selector("#TableChart_2")
        target_elem = driver.find_element_by_css_selector("#TableChart_1")
        utillobj.click_on_screen(source_elem, 'start', x_offset=10, y_offset=10)
        utillobj.click_on_screen(source_elem, 'start', click_type=0, x_offset=10, y_offset=10)
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            offset_value = 5
        else:
            offset_value = 7
        utillobj.drag_drop_using_uisoup(source_elem, target_elem, src_cord_type='start', trg_cord_type='top_right', sx_offset=20, tx_offset=40, sy_offset=offset_value)
         
        """
        Select Gross Profit from the Sales group under Measures.
        Then add Product,Category and Product,Subcategory from the Product group under Dimensions.
        """    
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_2  div[class^='x']", 2, 15)
            
        metaobj.datatree_field_click("Product,Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_2  div[class^='x']", 18, 15)
            
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_2  div[class^='x']", 55, 15)
        
        """
        Expect to see two Reports on the canvas.
        """
        coln_list = ['ProductCategory', 'ProductSubcategory', 'Gross Profit']
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_2", coln_list, "Step 03.1: Verify report titles")
#         ia_resultobj.create_report_data_set('TableChart_2', 21, 3, Test_Case_ID+"_Ds02.xlsx", no_of_cells=6)
        ia_resultobj.verify_report_data_set('TableChart_2', 21, 3, Test_Case_ID+"_Ds02.xlsx", 'Step 03.2: Verify report dataset', no_of_cells=6)
        
        """
        Step 05: Click the Run button to generate the Document.
        Expect to see two Active Reports in the Document.
        Expect to see 7 records on the first report and 16 records on the second report.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 35)
        utillobj.switch_to_frame(pause=2) 
        time.sleep(10)
        miscelaneousobj.verify_page_summary('0','7of7records,Page1of1', 'Step 04.1.a: Verify report1 Page summary')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_run_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_run_Ds01.xlsx', "Step 04.1.b: Verify report1")
        
        miscelaneousobj.verify_page_summary('1','21of21records,Page1of1', 'Step 04.2.a: Verify Page summary')
#         utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_run_Ds02.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_run_Ds02.xlsx', "Step 04.2.b: Verify report2")
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        
        """
        Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()