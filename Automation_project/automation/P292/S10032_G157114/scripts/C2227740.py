'''
Created on December 28, 2017

@author: Praveen Ramkumar/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227740
TestCase Name = Chart: Verify that user is able to run a simple AHTML chart(82xx)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous
from common.lib import utillity
from common.wftools import active_report

class C2227740_TestClass(BaseTestCase):

    def test_C2227740(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="NB_AR_AHTML_002.fex"
               
        """
            Step 01 :Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G157266 Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=NB_AR_AHTML_002.fex
            Step 03:Verify the report is generated.
        """
        active_reportobj.run_active_report_using_api(fex_name)
        resobj.wait_for_property("#MAINTABLE_wbody0 svg g.risers >g>rect[class^='riser']",10,20)
        time.sleep(3)
        
        """
            Step 04 :Verify the AHTML formatted chart is generated.
            Step 05 :Dismiss the window and logout http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales BY Category, Product", "Step 05.1 : Verify chart title ")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 05.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c1!", "bar_blue", "Step 05.4: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","Product","Step 05.5: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 05.6: Verify yaxis title")
        expected_tooltip_list=['Category:Food', 'Product:Croissant', 'Unit Sales:630054', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!r0!c1!", expected_tooltip_list, "Step 05.7: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label=['Coffee','Food','Gifts']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0", "Columns", "Category",expected_label,"Step 05.11: Verify visualization column header lables")       
        utillobj.infoassist_api_logout() 
        
if __name__ == '__main__':
    unittest.main() 