'''
Created on December 28, 2017

@author: Nasir/Updated by :Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227739
TestCase Name = Document: Verify that user is able to run a simple AHTML Document(82xx)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous
from common.lib import utillity
from common.wftools import active_report

class C2511606_TestClass(BaseTestCase):

    def test_C2511606(self):
        
        """
            TESTCASE VARIABLES
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="NB_AR_AHTML_003.fex"
        report_dataset_name="AHTML_ON_001a"
               
        """
            Step 01 :Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G157266 Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=NB_AR_AHTML_003.fex
            Step 03:Verify the report is generated.
        """
        active_reportobj.run_active_report_using_api(fex_name,column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text='Category')
        element_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 10, expire_time=20)       
        
        """
            Step 04 :Verify Active Report is displayed and all the report menu options are present on a report.
            Step 05 :Dismiss the window and logout http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        #Report
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelaneous_obj.verify_column_heading('ITableData0', expected_list,'Step 05.01: Verify column heading')
        miscelaneous_obj.verify_page_summary(0, '107of107records,Page1of2', "Step 05.02:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',report_dataset_name+".xlsx", "Step 05.03: AHTML_OFF_001.fex data verification")   
        expected_menu_list=['Sort Ascending', 'Sort Descending', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Export', 'Print', 'Window', 'Restore Original']
        miscelaneous_obj.verify_menu_items("ITableData0",0, None,expected_menu_list, 'Step 05.04:  Verify all the report menu options are present on a report')
        
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody1_ft","Sequence# by Category, Product", "Step 05.05 : Verify chart title ")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval1_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval1_list, "Step 05.06: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 10, 'Step 05.07: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c1!", "bar_blue", "Step 05c.4: Verify  riser color")
#         resobj.verify_xaxis_title("MAINTABLE_wbody1","Product","Step 05c.5: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody1", "Sequence#", "Step 05.08: Verify yaxis title")
        
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 05.09: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 05.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 05.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label=['Coffee','Food','Gifts']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", "Columns", "Category : Product",expected_label,"Step 05.12: Verify visualization column header lables")       
        
if __name__ == '__main__':
    unittest.main()
