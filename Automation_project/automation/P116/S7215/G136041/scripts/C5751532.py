'''
Created on Jun 10, 2018

@author: BM13368
'''
import time, unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous
from common.lib import utillity

class C5751532_TestClass(BaseTestCase):

    def test_C5751532(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        fex_name="143860.fex"
        Test_Case_ID="C5751532"
        
        """
            Step 01 : Run 143860.fex from following URL
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP116%252FS7215&BIP_item=143860.fex
        """
        utillobj.active_run_fex_api_login(fex_name, "S7215", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(1)", "ENGLAND", 65)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Execute the 108268.fex")
        column_list=['COUNTRY', 'CAR', 'MODEL', 'SEATS']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report 143860.fex')
#         utillobj.create_data_set("ITableData0", 'I0r', Test_Case_ID+'Ds01.xlsx')
        utillobj.verify_data_set("ITableData0", 'I0r', Test_Case_ID+'Ds01.xlsx', "Step 01:03:Verify dataset")
        time.sleep(2)
        
        """
            Step 02 : In report click seats dropdown select Chart->Pie->Country.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Chart', 'Pie','COUNTRY')
        utillobj.synchronize_with_number_of_element("#wall1", 1, 20)
        
        """
            Step 03:Verify that chart opens noramally without any additional scrollbars.
        """
        miscelanousobj.verify_chart_title('wbody1_ft', 'SEATS by COUNTRY', 'Step 3.1: Verify Chart Title')
        miscelanousobj.verify_arChartToolbar('wmenu1', ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart'],"Step 2.2: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wmenu1', ['Aggregation'],"Step 3.2: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wmenu1', ['Sum'],"Step 3.3: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        expected_datalabel=['48.57%', '11.43%', '14.29%', '7.14%', '18.57%']
        result_obj.verify_data_labels("Pie1_0", expected_datalabel, "Step 03:4: Verify the data lables in the pie chart", custom_css=".highcharts-data-labels text")
        result_obj.verify_data_labels_("Pie1_0", ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], "Step 03:5: Verify the data lables in the pie chart", custom_css="[class*='highcharts-legend'] text")
        
        
if __name__ == "__main__":
    unittest.main()