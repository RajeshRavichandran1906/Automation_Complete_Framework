'''
Created on December 29, 2017

@author: Nasir/Updated by :Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227738
TestCase Name = Report-Chart: Verify Rollup tool 'Series' options(82xx)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, active_chart_rollup
from common.lib import utillity
from common.wftools import active_report

class C2227738_TestClass(BaseTestCase):

    def test_C2227738(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID='C2227738'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        obrowser=utillobj.parseinitfile('browser')
        
        fex_name ="AHTML_OFF_001a.fex"
        report_dataset_name="AHTML_OFF_001a"
        
        """    1. Sign in to WebFOCUS as a Basic user - http://machine:port/{alias}    """
        """    2. Expand folder P292_S10032_G157266, Execute the following URL: http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex    """
        """    3. Verify the report is generated.    """
        
        active_reportobj.run_active_report_using_api(fex_name,column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text='Category')       
        
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelaneous_obj.verify_column_heading('ITableData0', expected_list,'Step 03r.1: Verify column heading')
        miscelaneous_obj.verify_page_summary(0, '107of107records,Page1of2', "Step 03r.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")
        
        """    4. Select State > Chart - Select Pie chart type and Select Category column under Pie chart type.    """
        miscelaneous_obj.select_menu_items('ITableData0', 3, 'Chart','Pie','Category')
        resobj.wait_for_property("#wall1 .arWindowBarTitle>span",1,10,string_value='State by Category')
        time.sleep(2)
        miscelaneous_obj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['Coffee','State: 30','28.0% of 107'],"Step 04a: Verify Chart tooltip and color")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','bar_blue',"Step 04b: Verify Chart piebevel Color")
        resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 04c: Verify Chart Label")
        resobj.verify_riser_legends('wall1', ['Coffee','Food','Gifts'], "Step 04d: Verify Chart Legends")
        miscelaneous_obj.verify_popup_title('wall1', 'State by Category', 'Step 04e: Verify the dialog title')
        rollobj.verify_arChartMenu('wall1',"Step 04f: Verify the chart Menu")
        
        """    5.  Click First dropdown button, Verify dropdown menu    """
        """    6. Click First dropdown button > Group By (x) > Product ID, Verify Chart adds up Product ID in the display.    """
        
        if obrowser == "IE":
            expected_menu_list=['New', 'Group By (X)', 'Add (Y)', 'Export to', 'Top', 'Chart/Rollup Tool', 'Restore Original']
        else :    
            expected_menu_list=['New', 'Group By (X)', 'Add (Y)', 'Top', 'Chart/Rollup Tool', 'Restore Original']
        rollobj.create_new_item(0, 'Group By (X)->Product ID', verify_main_menu_list=expected_menu_list, msg="Step 05a: ")
        
        miscelaneous_obj.verify_popup_title('wall1', 'State by Category', 'Step 06a: Verify the dialog title')
        miscelaneous_obj.verify_chart_title("wall1 #wbody1_ft","State by Category, Product ID", "Step 06b : Verify chart title ")
        resobj.verify_riser_legends('wall1', ['Coffee/C141', 'Coffee/C142', 'Coffee/C144', 'Food/F101', 'Food/F102', 'Food/F103', 'Gifts/G100', 'Gifts/G104', 'Gifts/G110', 'Gifts/G121'], "Step 06c: Verify Chart piebevel Legends for Top 5")
        miscelaneous_obj.verify_active_chart_tooltip('wall1',"riser!s2!g0!mwedge", ['Coffee/C144','State: 8','7.5% of 107'],"Step 06d: Verify Chart piebevel tooltip for Unit Sales")
        time.sleep(5)
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','bar_blue',"Step 06e: Verify Chart piebevel Color ")
        rollobj.verify_arChartMenu('wall1',"Step 06f: Verify the chart Menu")
        resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 06g: Verify Chart Label")
        
        """    7. Click Rollup table icon from the tool bar, Verify roll up table shows Category, Product ID and State in the display    """
        rollobj.click_chart_menu_bar_items('wall1',5)
        time.sleep(5)
        parent_css="#IWindowBody1 tr:nth-child(3) td:nth-child(1)"
        resobj.wait_for_property(parent_css, 1, string_value='Coffee', with_regular_exprestion=True)
        miscelaneous_obj.verify_popup_title('wall1', 'State by Category', 'Step 07a: Verify the dialog title')
        #utillobj.create_popup_data_set('wall1', 'ITableData1', Test_Case_ID+"_Ds02.xlsx")        
        utillobj.verify_popup_data_set('wall1', 'ITableData1', Test_Case_ID+"_Ds02.xlsx", 'Step 07: Verify roll up table shows Category, Product ID and State in the display')
        
        """    8. Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
        
        
if __name__ == '__main__':
    unittest.main()
