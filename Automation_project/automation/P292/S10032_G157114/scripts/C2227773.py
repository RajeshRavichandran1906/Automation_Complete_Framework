'''
Created on Dec 16, 2017

@author: Magesh

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
        Step 01: Start InfoAssist and create a New Document. Select wf-retail_lite as the file.
        """
        utillobj.infoassist_api_login('Document','new_retail/wf_retail_lite','P292/S10032_ahtml_off', 'mrid', 'mrpass')
        
        """
        Expect to see the following default development canvas with output format as Active Report
        """
        time.sleep(4)
        parent_css= "#resultArea"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
        homeformattype_css="#HomeFormatType img[src*='active_reports']"
        utillobj.verify_object_visible(homeformattype_css, True, "Step 01.1: Verify output format as Active Report")
        outputformattype_css="#sbpOutputFormatPanel #sbpOutputFormat img[src*='active_reports']"
        utillobj.verify_object_visible(outputformattype_css, True, "Step 01.2: Verify output format as Active Report")
        time.sleep(5)
        
        """
        Step 02: Create the first report by selecting Quantity,Sold from the Sales group under Measures and Product,Category from from the Product group under Dimensions.
        """
        metaobj.datatree_field_click("Quantity,Sold",2,1)
        time.sleep(4)
        resultobj.wait_for_property("#TableChart_1  div[class^='x']", 3, expire_time=10) 
        time.sleep(3) 
        
        metaobj.datatree_field_click("Product,Category",2,1)
        time.sleep(4)
        resultobj.wait_for_property("#TableChart_1  div[class^='x']", 18, expire_time=15) 
        time.sleep(3) 
        
        """
        Expect to see two Reports on the canvas.
        """
        coln_list = ['ProductCategory', 'QuantitySold']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 02.1: Verify report titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 7, 2, Test_Case_ID+"_Ds01.xlsx", no_of_cells=4)
        ia_resultobj.verify_report_data_set('TableChart_1', 7, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 02.2: Verify report dataset', no_of_cells=4)
        time.sleep(3)
        
        """
        Step 03: From the tool bar at the top, click Insert, then Report.
        """
        time.sleep(5)
        ribbonobj.select_ribbon_item('Insert', 'Report')
        
        parent_css="#TableChart_2"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
        time.sleep(2)
        
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
        resultobj.wait_for_property("#TableChart_2  div[class^='x']", 2, expire_time=10) 
        time.sleep(3)    
            
        metaobj.datatree_field_click("Product,Category", 2, 1)
        resultobj.wait_for_property("#TableChart_2  div[class^='x']", 18, expire_time=15) 
        time.sleep(3)    
            
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        resultobj.wait_for_property("#TableChart_2  div[class^='x']", 55, expire_time=15) 
        time.sleep(3)
        
        """
        Expect to see two Reports on the canvas.
        """
        coln_list = ['ProductCategory', 'ProductSubcategory', 'Gross Profit']
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_2", coln_list, "Step 03.1: Verify report titles")
#         ia_resultobj.create_report_data_set('TableChart_2', 21, 3, Test_Case_ID+"_Ds02.xlsx", no_of_cells=6)
        ia_resultobj.verify_report_data_set('TableChart_2', 21, 3, Test_Case_ID+"_Ds02.xlsx", 'Step 03.2: Verify report dataset', no_of_cells=6)
        time.sleep(3)
        
        """
        Step 04: Click the Run button to generate the Document.
        Expect to see two Active Reports in the Document.
        Expect to see 7 records on the first report and 16 records on the second report.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2) 
        
        time.sleep(10)
        miscelaneousobj.verify_page_summary('0','7of7records,Page1of1', 'Step 04.1.a: Verify report1 Page summary')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_run_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_run_Ds01.xlsx', "Step 04.1.b: Verify report1")
        
        time.sleep(5)
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