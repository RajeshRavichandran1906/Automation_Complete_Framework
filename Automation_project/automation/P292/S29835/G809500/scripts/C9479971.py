'''
Created on Sep 12, 2019

@author: Niranjan
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9479971
TestCase Name = Verify promoting HOLD file to Document mode
'''

from common.wftools.report import Report
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.pages.visualization_metadata import Visualization_Metadata
import unittest
import time

class C9479971_TestClass(BaseTestCase):

    def test_C9479971(self):
    
        """
            CLASS OBJECTS
        """
        report_ = Report(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        meta = Visualization_Metadata(self.driver)
        
        def double_click_datpane_field(datapane_filed):
            core_utils.left_click(datapane_filed)
            SELECTED_DATA_FIELD_CSS="#iaMetaDataBrowser [id^='QbMetaDataTree'] table[class='bi-tree-view-table']>tbody>tr[class*='selected']>td>img[class*='icon']"
            field_object = self.driver.find_element_by_css_selector(SELECTED_DATA_FIELD_CSS)
            core_utils.double_click(field_object, xoffset=30, mouse_move_duration=0)
        
        step1 = """  Step 1: Launch the API to create new Report with CAR.
                http://machine:port/{alias}/ia?is508=false&tool=report&master=ibisamp/car&item=IBFS:/WFC/Repository/P292_S29835/G781455   """
        report_.invoke_ia_tool_using_new_api_login(mrid= 'mrid', mrpass='mrpass', master='ibisamp/car')
        utils.capture_screenshot('01', step1)
        
        step2 = """  Step 2: Double click "COUNTRY", "CAR","DEALER_COST" and "RETAIL_COST" in Data pane. 
            Step 2.00 : Check the Live preview.   """
        report_.double_click_on_datetree_item('COUNTRY')
        report_.wait_for_visible_text('#queryTreeWindow', 'COUNTRY')
        report_.double_click_on_datetree_item('CAR')
        report_.wait_for_visible_text('#queryTreeWindow', 'CAR')
        report_.double_click_on_datetree_item('DEALER_COST')
        report_.wait_for_visible_text('#queryTreeWindow', 'DEALER_COST')
        report_.double_click_on_datetree_item('RETAIL_COST')
        report_.wait_for_visible_text('#queryTreeWindow', 'RETAIL_COST')
#         report_.create_report_data_set_in_preview('TableChart_1', 10, 4, 'C9479971_01.xlsx')
        report_.verify_report_data_set_in_preview('TableChart_1', 10, 4, 'C9479971_01.xlsx', msg= 'Step 02.00 : Check the preview')
        report_.verify_row_total_report_titles_on_preview(4, 4, 'TableChart_1', ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST'], "Step 02.01 : Verify report title ")
        utils.capture_screenshot('02', step2)
        
        step3 = """  Step 3: Click "File" icon under Home tab.   """
        report_.select_ia_ribbon_item('Home', 'file')
        time.sleep(10)
        utils.capture_screenshot('03', step3)
        
        step4 = """  Step 4: Click "Save" button (with default name and format).   
        Step 4.00 : Check the Status bar.
        Step 5 : Click "Create Report" at the bottom of Canvas.
        """
        report_.wait_for_number_of_element('#IbfsOpenFileDialog7_btnOK', 1)
        save  = utils.validate_and_get_webdriver_object('#IbfsOpenFileDialog7_btnOK', 'save button')
        core_utils.left_click(save)
        utils.synchronize_until_element_disappear('#IbfsOpenFileDialog7_btnOK', 30)
        report_.wait_for_number_of_element('#createFromHoldButton', 1)
        create_report  = utils.validate_and_get_webdriver_object('#createFromHoldButton', 'Create Report')
        core_utils.python_left_click(create_report)
        utils.capture_screenshot('04', step4)
        
        step6 = """  Step 6: Click "Document" under Home tab.   """
        report_.select_ia_ribbon_item('Home', 'document')
        time.sleep(20)
        utils.capture_screenshot('06', step6)
        
        step7 = """  Step 7: Click "HTML Analytic Document" dropdown and Select "PDF" format.   """
        report_.change_output_format_type('pdf')
        time.sleep(20)
        utils.capture_screenshot('07', step7)
        
        step8 = """ Step 8: Click on the "Empty Report" component in Canvas.  
        Step 8.00 : Check the following Canvas.  """
        empty_report  = utils.validate_and_get_webdriver_object('#TableChart_2', 'empty report')
        core_utils.left_click(empty_report)
        empty_data = empty_report.get_attribute('text').replace('\n', '').replace('\xa0','')
        expcted = 'Drag and drop fields onto thecanvas or into the query paneto begin building your report.'
        utils.asequal(expcted, empty_data, 'Step 08.00: Check the canvas')
        utils.capture_screenshot('08', step8)
        
        step9 = """  Step 9: Double click "COUNTRY", "CAR" and "DEALER_COST" in Data pane.   
        Step 09.00 : Check the following Canvas."""
        datapane_filed = utils.validate_and_get_webdriver_object('div[id*="QbMetaDataTree"] table[class="bi-tree-view-table"]>tbody>tr:nth-child(2)>td>img[class="icon"]', 'Country')
        double_click_datpane_field(datapane_filed)
        report_.wait_for_visible_text('#queryTreeWindow', 'COUNTRY')
        datapane_filed = utils.validate_and_get_webdriver_object('div[id*="QbMetaDataTree"] table[class="bi-tree-view-table"]>tbody>tr:nth-child(3)>td>img[class="icon"]', 'car')
        double_click_datpane_field(datapane_filed)
        report_.wait_for_visible_text('#queryTreeWindow', 'CAR')
        datapane_filed = utils.validate_and_get_webdriver_object('div[id*="QbMetaDataTree"] table[class="bi-tree-view-table"]>tbody>tr:nth-child(5)>td>img[class="icon"]', 'dealer cost')
        double_click_datpane_field(datapane_filed)
        report_.wait_for_visible_text('#queryTreeWindow', 'DEALER_COST')
#         report_.create_report_data_set_in_preview("TableChart_2", 10, 3, "C9479971_02.xlsx")
        report_.verify_report_data_set_in_preview("TableChart_2", 10, 3, "C9479971_02.xlsx", "Step 09.00: Check the canvas")
        report_.verify_report_titles_on_preview(3, 3, 'TableChart_2', ['COUNTRY', 'CAR', 'DEALER_COST'], msg = 'Step 09.01: Verify column title of report')
        utils.capture_screenshot('09', step9)
        
        step10 = """  Step 10: Click "Run" from toolbar. 
        Step 10.00 : Check the following Output. """
        report_.run_report_from_toptoolbar()
        report_.wait_for_number_of_element('#resultAreaWindowManager img', 1)
        pdf_ele = utils.validate_and_get_webdriver_object('#resultAreaWindowManager img', 'pdf')
        pdf = pdf_ele.is_displayed()
        utils.asequal(pdf, True, 'Step 10.00: Check the canvas')
        utils.capture_screenshot('10', step10)
        
        
        step11 = """  Step 11: Click "Save" in toolbar Enter "C9479971" and Click "Save" button.   """
        report_.save_report_from_toptoolbar()
        report_.save_file_in_save_dialog('C9479971')
        time.sleep(15)
        utils.capture_screenshot('11', step11)
        
        step12 = """  Step 12: Click "IA" menu and Select "Close" option. """
        report_.select_ia_application_menu('close')
        report_.wait_for_number_of_element('#TableChart_2', 1)
        utils.capture_screenshot('12', step12)
        
        step13 = """  Step 13: Click "IA" menu and Select "Close" option. 
        Step 14 : Click "NO" option."""
        report_.close_ia_without_save()
        time.sleep(15)
        utils.capture_screenshot('13', step13)
        
        step15 = """  Step 15: Logout 
        http://machine:port/ibi_apps/service/wf_security_logout.jsp  """
        report_.api_logout()
        utils.capture_screenshot('15', step15)
        
        step16 = """  Step 16: Reopen the saved fex using API link
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S29835/G781455/C9479971.fex&tool=Document 
            Step 16.00 : Check the Data pane, Query pane and Canvas."""
        report_.edit_fex_using_api_url('C9479971')
        time.sleep(30)
        report_.verify_report_data_set_in_preview("TableChart_2", 10, 3, "C9479971_02.xlsx", "Step 16.00: Check the canvas")
        report_.verify_report_titles_on_preview(3, 3, 'TableChart_2', ['COUNTRY', 'CAR', 'DEALER_COST'], msg = 'Step 16.01: Verify column title of report')
        report_.verify_all_fields_in_query_pane(['Files', 'File1 (car)'], msg='Step 16.02: Verify the query pane')
        meta.verify_all_data_panel_fields(['Dimensions', 'COUNTRY', 'CAR', 'Measures/Properties', 'DEALER_COST', 'RETAIL_COST'], msg='Step 16.03: Verify the data pane')
        utils.capture_screenshot('16', step16)
        
        """ Logout 
        http://machine:port/ibi_apps/service/wf_security_logout.jsp """
        
if __name__ == '__main__':
    unittest.main()