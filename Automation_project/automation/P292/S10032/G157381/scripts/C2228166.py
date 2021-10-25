'''
Created on Dec 26, 2017

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228166
TestCase Name = Verify promote multi-graph Chart to Document (82xx)
'''

import unittest,time
from common.wftools.chart import Chart
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.select import Select
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, active_miscelaneous

class C2228166_TestClass(BaseTestCase):

    def test_C2228166(self):
        
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2228166'
        
        chart_obj = Chart(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
         
        """
        Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/employee
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
           
        """
        Step 02: Double click "LAST_NAME", "CURR_SAL".
        """
        
        metaobj.datatree_field_click('LAST_NAME', 2, 1)
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 15)
           
        metaobj.datatree_field_click('CURR_SAL', 2, 1)
        parent_css="#TableChart_1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 15)
           
        """
        Step 03: Verify the following chart is displayed.
        """
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 03.01 : Verify X-Axis Title")
        yaxis_value="CURR_SAL"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 03.02 : Verify y-Axis Title")
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 03.03 : Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 11, 'Step 03.04 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 03.05 : Verify first bar color")
        time.sleep(5)
           
        """
        Step 04: Drag "DEPARTMENT" to "Multi-graph"(Query Pane).
        """
        chart_obj.drag_field_from_data_tree_to_query_pane('DEPARTMENT', 1, 'Multi-graph')
        parent_css="#queryTreeWindow"
        utillobj.synchronize_with_visble_text(parent_css, 'DEPARTMENT', 15)
           
        """
        Step 05: Verify the following is displayed in the Query pane.
        """
        
        metaobj.verify_query_pane_field('Vertical Axis', "CURR_SAL", 1, "Step 05.01 : ")
        metaobj.verify_query_pane_field('Horizontal Axis', "LAST_NAME", 1, "Step 05.02 : ")
        metaobj.verify_query_pane_field('Multi-graph', "DEPARTMENT", 1, "Step 05.03 : ")
        time.sleep(2)
           
        """
        Step 06: Click on "Document" button in "Design Grouping".
        """
        ribbonobj.select_ribbon_item('Home', 'Document')
        parent_css="#iaCanvasCaptionLabel"
        utillobj.synchronize_with_visble_text(parent_css, "Document", 20)
           
        """
        Step 07: Click on the Chart on Document canvas to highlight it.
        """
        source_elem = driver.find_element_by_css_selector("#TableChart_1")
        utillobj.click_on_screen(source_elem, 'start', x_offset=30, y_offset=30)
        utillobj.click_on_screen(source_elem, 'start', click_type=0, x_offset=30, y_offset=30)
        query_tree="#queryTreeWindow"
        utillobj.synchronize_with_number_of_element(query_tree, 1, 15, 1)
        time.sleep(5)
        
        """
        Step 08: Verify the following is displayed in the Query pane.
        """
        utillobj.synchronize_with_visble_text(query_tree, "DEPARTMENT", 30)
        metaobj.verify_query_pane_field('Vertical Axis', "CURR_SAL", 1, "Step 08.01 :")
        metaobj.verify_query_pane_field('Horizontal Axis', "LAST_NAME", 1, "Step 08.02 :")
        metaobj.verify_query_pane_field('Coordinated', "DEPARTMENT", 1, "Step 08.03 :")
         
        """
        Step 09: Click "Run".
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
          
        """
        Step 10: Verify charts are produced in Document - AHTML format.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 15)
        
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 10.01 : Verify X-Axis Title")
        yaxis_value="CURR_SAL"
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 10.02 : Verify y-Axis Title")
        expected_xval_list=['BLACKWOOD', 'CROSS', 'GREENSPAN', 'JONES', 'MCCOY', 'SMITH']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 10.03 :Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step 10.04 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 10.05 : Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0","CURR_SAL by LAST_NAME", "Step 10.06 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.07 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.08 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.09 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
          
        """
        Step 11: Click the "DEPARTMENT" dropdown > "PRODUCTION"
        """
        driver_ele = self.driver.find_element_by_css_selector('.arDashboardMergeDropdown')
        dropdown = Select(driver_ele)
        time.sleep(10)
        dropdown.select_by_value("PRODUCTION")
        core_utils.switch_to_default_content()
        utillobj.switch_to_frame(pause=2)
          
        """
        Step 12: Verify that another page (with different LAST_NAME) is displayed.
        """
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f", 'BANNING', 30)
        
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 12.01 : Verify X-Axis Title")
        yaxis_value="CURR_SAL"
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 12.02 : Verify y-Axis Title")
        expected_xval_list=['BANNING', 'IRVING', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 12.03 : Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step 12.04 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 12.05 : Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0","CURR_SAL by LAST_NAME", "Step 12.06 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 12.07 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 12.08 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 12.09 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        """
        Step 13:Hover on riser and verify tooltip values
        """
        expected_tooltip_list=['DEPARTMENT:PRODUCTION', 'LAST_NAME:BANNING', 'CURR_SAL:$29,700.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 13.01 : verify the default tooltip values')
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
          
        """
        Step 14:Click "IA" > "Save" > "C2228166" > "Save".
        """
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID + "_base1")
        time.sleep(10)
          
        """    
        Step 15: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """

        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
        Step 16:Run saved fex from bip using API
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228166.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID + "_base1"+'.fex','S10032_chart_1','mrid','mrpass')
        
        """
        Step 17:Verify the following chart is displayed.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 65)
         
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 17.01 : Verify X-Axis Title")
        yaxis_value="CURR_SAL"
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 17.02 : Verify y-Axis Title")
        expected_xval_list=['BLACKWOOD', 'CROSS', 'GREENSPAN', 'JONES', 'MCCOY', 'SMITH']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 17.03 : Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step 17.04 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 17.05 : Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0","CURR_SAL by LAST_NAME", "Step 17.06 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 17.07 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 17.08 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 17.09 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['DEPARTMENT:MIS', 'LAST_NAME:BLACKWOOD', 'CURR_SAL:$21,780.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 17.10 : verify the default tooltip values')
        time.sleep(5)
        
        """
        Step 18:Click the "DEPARTMENT" dropdown > "PRODUCTION"
        """
        dropdown_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0TABS [class*='arDashboardMergeDropdown']")
        core_utils.python_left_click(dropdown_css)
        production_css = driver.find_elements_by_css_selector("#IBILAYOUTDIV0TABS [class*='arDashboardMergeDropdown'] option")
        core_utils.python_left_click(production_css[1])
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f", 'BANNING', 30)
        
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 18.01 : Verify X-Axis Title")
        yaxis_value="CURR_SAL"
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step1 18.02 : Verify y-Axis Title")
        expected_xval_list=['BANNING', 'IRVING', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 18.03 : Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step 18.04 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 18.05 : Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0","CURR_SAL by LAST_NAME", "Step 18.06 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 18.07 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 18.08 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 18.09 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
      
        """
        Step 19:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(4)
             
        """
        Step 20:Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228166.fex
        Step 21: Verify the following chart is displayed.
        """
        utillobj.infoassist_api_edit(Test_Case_ID + "_base1", 'chart', 'S10032_chart_1',mrid='mrid',mrpass='mrpass')
       
        parent_css="#TableChart_1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 65)
        
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 21.01 : Verify X-Axis Title")
        yaxis_value="CURR_SAL"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 21.02 : Verify y-Axis Title")
        expected_xval_list=['BLACKWOOD', 'CROSS', 'GREENSPAN', 'JONES', 'MCCOY', 'SMITH']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 21.03 : Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 6, 'Step 21.04 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 21.05 : Verify first bar color")
        time.sleep(5)
        
        """
        Step 22:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()