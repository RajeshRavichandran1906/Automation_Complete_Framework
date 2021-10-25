'''
Created on Sep 17, 2019

@author: Niranjan Das
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9336782
TestCase Name = Verify basic creation of a REPORT, with a Report and Bar Chart.
'''

from common.wftools.report import Report
from common.wftools.chart import Chart
from common.wftools.active_report import Active_Report
from common.wftools.document import Document
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.pages.ia_miscelaneous import IA_Miscelaneous
import unittest

class C9336782_TestClass(BaseTestCase):

    def test_C9336782(self):
    
        """
            CLASS OBJECTS
        """
        report_ = Report(self.driver)
        utils = UtillityMethods(self.driver)
        act_report = Active_Report(self.driver)
        doc = Document(self.driver)
        misc = IA_Miscelaneous(self.driver)
        chart_ = Chart(self.driver)
        
        Step1 = """  Step 1 : Invoke following api url as below
                http://machine:port/{alias}/ia?tool=document&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10032_G157266%2F
            Step 01.00: Expect to see the following default Dashboard canvas. """
        misc.invoke_ia_tool_using_api_(tool='document', master='baseapp/wf_retail_lite', folder_path= 'P292_S10032_G157266')
        doc.wait_for_number_of_element("#resultArea", 1, misc.home_page_long_timesleep)
        utils.wait_for_page_loads(misc.home_page_long_timesleep)
        utils.capture_screenshot("01.00", Step1)
        
        Step2 = """  Step 2: From the Measures group, select the Sales sub-group, then select the Cost of Goods field.   """
        utils.synchronize_with_visble_text("#wndApp", "Refreshing...", misc.home_page_long_timesleep, condition_type="asnotin")
        report_.double_click_on_datetree_item('Cost of Goods')
        report_.wait_for_visible_text('#queryTreeWindow', 'Cost of Goods')
        utils.capture_screenshot("02.00", Step2)
        
        Step3 = """   Step 3: From the Dimensions group, select the Product sub-group, then select the Product, Category field.
        Step 03.00: Expect to see the following Live Preview for the Report component of the Dashboard. """
        report_.double_click_on_datetree_item('Product,Category')
        report_.wait_for_visible_text('#queryTreeWindow', 'Product,Category')
#         report_.create_acrossreport_data_set_in_preview("TableChart_1", 2, 2, 7, 2, "C9336782_DS01.xlsx")
        report_.verify_across_report_data_set_in_preview("TableChart_1", 2, 2, 7, 2, "C9336782_DS01.xlsx", "Step 03.00: Verify report")
        utils.capture_screenshot("03.00", Step3)
         
        Step4 = """   Step 4: Click on Insert tab at the top and select Chart from Reports group.    """
        self.driver.set_page_load_timeout(100)
        report_.select_ia_ribbon_item('Insert', 'chart')
        utils.capture_screenshot("04.00", Step4)
        
        Step5 = """  Step 5: Position the Chart to the right of the Report, by dragging in the border area..  """
        doc.drag_drop_document_component( '#TableChart_2', '#TableChart_1', 400, 0)
        utils.capture_screenshot("05.00", Step5)
        
        Step6 = """  Step 6: From the Measures group, select the Sales sub-group, then select the Cost of Goods field."""
        report_.double_click_on_datetree_item('Cost of Goods')
        report_.wait_for_visible_text('#queryTreeWindow', 'Cost of Goods')
        utils.capture_screenshot("06.00", Step6)
        
        Step7 = """  Step 7: From the Dimensions group, select the Product sub-group, then select the Product, Category field.
        Step 07.00: Expect to see the following Live Preview for the Dashboard, which now contains a Report and a Chart."""
        report_.double_click_on_datetree_item('Product,Category')
        report_.wait_for_visible_text('#queryTreeWindow', 'Product,Category', 60)
        report_.verify_across_report_data_set_in_preview("TableChart_1", 2, 2, 7, 2, "C9336782_DS01.xlsx", "Step 07.00: Verify report")
        expected_x_labels = ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_y_labels = ['0', '40M', '80M', '120M', '160M', '200M', '240M']
        chart_.verify_x_axis_label_in_preview(expected_x_labels, '#TableChart_2', msg = 'Step 07.01')
        chart_.verify_y_axis_label_in_preview(expected_y_labels, '#TableChart_2', msg = 'Step 07.02')
        chart_.verify_number_of_risers('#TableChart_2 rect', 1, 7, msg= "Step 07.03")
        chart_.verify_x_axis_title_in_preview(['Product Category'], '#TableChart_2', msg ='Step 07.04')
        chart_.verify_y_axis_title_in_preview(['Cost of Goods'], '#TableChart_2', msg ='Step 07.05')
        chart_.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s0!g0!mbar!"]', 'bar_blue', '#TableChart_2', msg = 'Step 07.06')
        utils.capture_screenshot("07.00", Step7)
        
        step8 = """  Step 8: Click the Run button to generate the Dashboard.  
        Step 08.00: Expect to see the following Active Dashboard, containing a report with 7 lines and a Bar Chart with 7 bars.
        Also verify that the values of Cost of Goods are equivalent in both the Dashboard components."""
        
        report_.run_report_from_toptoolbar()
        utils.wait_for_page_loads(10)
        report_.switch_to_frame()
        report_.wait_for_visible_text('table[class="arGridBar"]', '7 of 7 records, Page 1 of 1')
        report_.wait_for_number_of_element('#ITableData0  .arGridColumnHeading > td', 2)
        act_report.verify_column_heading('ITableData0', ['ProductCategory', 'Cost of Goods'], msg = 'Step 08.00: Verify column heading of active report')
        
        summary_ele = self.driver.find_element_by_css_selector('table[class="arGridBar"]')
        summary = summary_ele.text
        utils.asequal(summary, '7 of 7 records, Page 1 of 1', 'Step 08.01: Verify 7 records on the active report')
        
#         act_report.create_active_report_dataset('C9336782_DS02.xlsx', table_css='#ITableData0', desired_no_of_rows=7, starting_rownum=1)
        act_report.verify_active_report_dataset('C9336782_DS02.xlsx', table_css='#ITableData0', desired_no_of_rows=7, starting_rownum=1, msg= 'Step 08.02 : Verify active report')
        chart_.verify_number_of_risers('#MAINTABLE_1 rect', 1, 7, msg= "Step 08.02")
        chart_.verify_x_axis_title_in_run_window(['Product Category'], '#MAINTABLE_1', msg ='Step 08.03')
        chart_.verify_y_axis_title_in_run_window(['Cost of Goods'], '#MAINTABLE_1', msg ='Step 08.04')
        chart_.verify_chart_color_using_get_css_property_in_run_window('rect[class="riser!s0!g0!mbar!"]', 'bar_blue', '#MAINTABLE_1', msg = 'Step 08.05')
#         expected_list = ['Product Category:  Accessories', 'Cost of Goods:  $89,753,898.00', 'Filter Chart', 'Exclude from Chart']
#         chart_.verify_active_chart_tooltip('MAINTABLE_wbodyMain1', 'riser!s0!g0!mbar!', expected_list, msg= 'Step 08.06: Verify values of Cost of Goods are equivalent')
        utils.capture_screenshot("08.00", step8)
        
        """  Step 9. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()