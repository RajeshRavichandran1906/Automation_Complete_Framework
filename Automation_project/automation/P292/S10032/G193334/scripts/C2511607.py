'''
Created on December 29, 2017

@author: Nasir/Updated by :Bhagavathi 

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2511607
TestCase Name = Report-Chart: Verify Rollup tool 'Series' options(82xx)
'''
import unittest, time, re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, active_chart_rollup, active_tools
from common.lib import utillity
from common.wftools import active_report

class C2511607_TestClass(BaseTestCase):

    def test_C2511607(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)       
        toolobj= active_tools.Active_Tools(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
        
        """    1. Sign in to WebFOCUS as a Basic user - http://machine:port/{alias}    """
        """    2. Expand folder P292_S10032_G193334, Execute the following URL: http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001a.fex    """
        """    3. Verify the report is generated.    """
        
        active_reportobj.run_active_report_using_api(fex_name,column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text='Category')
        
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelaneous_obj.verify_column_heading('ITableData0', expected_list,'Step 03r.1: Verify column heading')
        miscelaneous_obj.verify_page_summary(0, '107of107records,Page1of2', "Step 03r.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',report_dataset_name+".xlsx", "Step 03r.3: AHTML_OFF_001.fex data verification", desired_no_of_rows=20)
        
        """    4. Select State > Chart - Select Pie chart type and Select Category column under Pie chart type.    """
        miscelaneous_obj.select_menu_items('ITableData0', 3, 'Chart','Pie','Category')
        utillobj.synchronize_with_visble_text("#wall1 .arWindowBarTitle>span", 'State by Category', 15)
       
        miscelaneous_obj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['Coffee','State: 30','28.0% of 107'],"Step 04a: Verify Chart tooltip and color")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','bar_blue',"Step 04b: Verify Chart piebevel Color")
        #Pie Label
        resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 04c: Verify Chart Label")
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Coffee','Food','Gifts'], "Step 04d: Verify Chart Legends")
        #Title
        miscelaneous_obj.verify_popup_title('wall1', 'State by Category', 'Step 04e: Verify the dialog title')
        #Menu
        rollobj.verify_arChartMenu('wall1',"Step 04f: Verify the chart Menu")
        
        """    5. Click Advanced Chart/Rollup Tool icon - Verify it opens up Advance Chart pop up - Verify pop up has following tabs: Series, Charts    """
        rollobj.click_chart_menu_bar_items('wall1', 6)
        time.sleep(5)
        tabs="#charttoolt2 .arToolColumnBorder tr"
        actual_tab=[el.strip() for el in self.driver.find_element_by_css_selector(tabs).text.split("\n") if bool(re.match('\S', el))]
        utillobj.asequal(['Series','Charts'],actual_tab,"Step 05a: Verify Chart/Rollup Tool 2 tabs")
        
        """    6. By Default, user is on Series tab, Verify this tab shows:- Columns - Group By - Measure    """
        toolobj.chart_rollup_tool_verify_columns('charttoolt2','tpanel_0_2_0', 1,['Columns','Category','Product ID','Product','State', 'Unit Sales','Dollar Sales'],"Step 06a: Verify Chart/Rollup Columns")
        toolobj.chart_rollup_tool_verify_columns('charttoolt2','tpanel_0_2_0', 2,['Group By', 'Category'],"Step 06b: Verify Chart/Rollup Group By")
        toolobj.chart_rollup_tool_verify_columns('charttoolt2','tpanel_0_2_0', 3,['Measure', 'Count:', 'State'],"Step 06c: Verify Chart/Rollup Measure")
        
        """    7. Drag and drop Product column next to Category under Group By section and click OK    """
        toolobj.chart_rollup_tool_drag_drop_items('charttoolt2', 'Columns', 'Product', 1, 'Group By', 1)
        toolobj.chart_rollup_tool_close('charttoolt2', 'Ok')
        time.sleep(5)
        
        rollobj.verify_arChartMenu("wall1", "Step 07a Verify the Chart Menu bar labels displayed on Run chart")
        x_val_list=['Coffee/Capu...', 'Coffee/Espre...', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee...', 'Gifts/Coffee...', 'Gifts/Mug', 'Gifts/Thermos']
        y_val_list=['0', '3', '6', '9', '12']
        resobj.verify_riser_chart_XY_labels('wall1', x_val_list, y_val_list, "Step 07b")
        expected_tooltip=['State: 8','X: Coffee/Capuccino']
        miscelaneous_obj.verify_active_chart_tooltip('wall1', 'riser!s0!g0!mbar', expected_tooltip,  "Step 07c: verify the chart tooltip")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mbar','bar_blue',"Step 07d: Verify Chart piebevel Color ")
        miscelaneous_obj.verify_popup_title('wall1', 'State by Category', 'Step 07e: Verify the dialog title')
        miscelaneous_obj.verify_chart_title("wall1 #wbody1_ft","State by Category, Product", "Step 07f : Verify chart title ")
        
        
        """    8. Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
        
if __name__ == '__main__':
    unittest.main()
