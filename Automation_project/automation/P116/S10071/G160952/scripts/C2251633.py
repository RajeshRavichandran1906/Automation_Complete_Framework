'''
Created on Jan 16, 2018

@author: Sowmiya 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc&group_id=160949
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2251633
TestCase Name : Verify Dashboard report, pie is displayed in single chart (157411)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous, ia_run
from common.lib import utillity

class C2251633_TestClass(BaseTestCase):

    def test_C2251633(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251633'
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelanousobj =active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        """        
            Step 01:Sign in to WebFOCUS as a Basic user
                    Execute the attached repro - ahtml_compound_report.fex.
        """
        utillobj.active_run_fex_api_login("ahtml_compound_report.fex", "S10071_2", 'mrid', 'mrpass')
        parent_css="div[class='activeReport'] div[id='MAINTABLE_all0']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
        
        """
            Step 02:Verify the AHTML formatted report is generated.
        """
        expected_title='Sample dashboard page'
        miscelanousobj.verify_chart_title('LOBJtext11', expected_title, msg='Step 2.1 : Verify page title')
        menu=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart']
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu0', menu, msg='Step 2.2 : Verify menu items')
        expected_title="SALES by CAR"
        miscelanousobj.verify_chart_title('MAINTABLE_wbody0_ft', expected_title, msg='Step 2.3 : Verify title')
        expected_tooltip_list=[['BMW: 80,390 (38.57%)'],['DATSUN: 43,000 (20.63%)'],['ALFA ROMEO: 30,200 (14.49%)']]
        miscelanousobj.verify_active_chart_tooltip('MAINTABLE_0', 'riser!s2!g0!mwedge!', expected_tooltip_list[0], msg='Step 2.4 : Verify tooltip values')
        miscelanousobj.verify_active_chart_tooltip('MAINTABLE_0', 'riser!s3!g0!mwedge!', expected_tooltip_list[1], msg='Step 2.5 : Verify tooltip values')
        miscelanousobj.verify_active_chart_tooltip('MAINTABLE_0', 'riser!s0!g0!mwedge!', expected_tooltip_list[2], msg='Step 2.6 : Verify tooltip values')
        utillobj.verify_chart_color('MAINTABLE_0', 'riser!s0!g0!mwedge!', color='cerulean_blue_1', msg='Step 2.7 : Verify color')
        utillobj.verify_chart_color('MAINTABLE_0', 'riser!s2!g0!mwedge!', color='sun_yellow', msg='Step 2.8 : Verify color')
        utillobj.verify_chart_color('MAINTABLE_0', 'riser!s3!g0!mwedge!', color='milky_carrot', msg='Step 2.9 : Verify color')
        expected_legend_list=['ALFA ROMEO','AUDI','BMW','DATSUN','JAGUAR','JENSEN']
        result_obj.verify_legends(expected_legend_list, '#MAINTABLE_0', msg='Step 2.10 : Verify legends')
        expected_label_list=['SALES']
        result_obj.verify_riser_pie_labels_and_legends('MAINTABLE_0', expected_label_list, msg='Step 2.11 : ')
        expected_title="DEALER_COST, RETAIL_COST by CAR"
        miscelanousobj.verify_chart_title('MAINTABLE_wbody1_ft', expected_title, msg='Step 2.12 : Verify title')
        menu=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart']
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu1', menu, msg='Step 2.13 : Verify menu items')
        expected_xval_list=['AL...', 'AUDI', 'BMW', 'DA...', 'JA...', 'JE...', 'MA...', 'PE...', 'TO...', 'TR...']
        expected_yval_list=['0', '17.5K', '35K', '52.5K', '70K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_1', expected_xval_list, expected_yval_list, msg='Step 2.14 :', x_axis_label_length=2)
        expected_legend_list=['DEALER_COST','RETAIL_COST']
        result_obj.verify_legends(expected_legend_list, '#MAINTABLE_1', legend_length=None, msg='Step 2.15 : Verify legends')       
        miscelanousobj.verify_page_summary(2, '18of18records,Page1of1', "Step 2.19:  18of18records,Page1of1 Active Report. - page summary verification of table 1")
        table_css="#ITableData2"
        ia_runobj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", msg='Step 2.20 : Verify the table 3')
               
        """
            Step 02 : Dismiss the window and logout.
                        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """   
        
        
if __name__ == '__main__':
    unittest.main()