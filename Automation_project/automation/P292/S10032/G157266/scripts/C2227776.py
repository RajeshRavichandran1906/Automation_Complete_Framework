'''
Created on December 19, 2017

@author: Praveen Ramkumar

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227776
TestCase Name = Report-Chart: Verify Chart types options
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_resultarea
from common.lib import utillity
from common.wftools import active_report

class C2227776_TestClass(BaseTestCase):

    def test_C2227776(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_OFF_001a.fex"
        report_dataset_name="AHTML_OFF_001a"
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G157266Execute the following URL:http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        """
             Step 03 : Verify the report is generated.
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")
        
        """
             Step 04: Select State > Chart
        """
        miscelanousobj.select_menu_items('ITableData0',3,'Chart')
        
        """
             Verify Chart menu shows : Pie, Line and Bar chart types
        """
        expected_list=['Pie', 'Line', 'Column']
        miscelanousobj.verify_menu_items('ITableData0',3,'Chart',expected_list,'Step 04.1 : Verify Filter menu shows all the filter options mentioned in the Test Description')
        
        """
             Step 05: Select any chart type. For instance: Pie
             Verify following options are displayed:
             - Group By (X)
             - All Columns of the report
        """
        
        expected_list=['Group By (X)', 'Category','Product ID','Product','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_menu_items('ITableData0',3,'Chart->Pie',expected_list,'Step 05.1 : Verify Filter menu shows all the filter options mentioned in the Test Description')
        
        """
             Step 06: Select Category column under Pie chart type,wall1
        """
        
        miscelanousobj.select_menu_items("ITableData0", 3, "Chart","Pie","Category")
        miscelanousobj.verify_chart_title("wall1","State by Category", "Step 06.1 : Verify chart title ")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge!', 'bar_blue', 'Step 06.2a: Verify Color')
        utillobj.verify_chart_color('wall1', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 06.2b: Verify Color')
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 06.3: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 06.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Count'],"Step 06.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resultobj.verify_riser_pie_labels_and_legends('wall1', ['State'], "Step 06.7:",custom_css="text[class*='pieLabel']",same_group=True) 
        ia_resultobj.verify_number_of_chart_segment('wall1', 3, "Step 06.8: Verify number of pie",custom_css="path[class^='riser']")
        expected_label_list=['Coffee', 'Food', 'Gifts']
        resultobj.verify_riser_legends('wall1', expected_label_list, 'Step 06.9: Verify Legends')
        time.sleep(2)
        
        """
             Step 07: Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
             
if __name__ == '__main__':
    unittest.main()