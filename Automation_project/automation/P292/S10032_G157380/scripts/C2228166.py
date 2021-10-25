'''
Created on Dec 26, 2017

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228166
TestCase Name = Verify promote multi-graph Chart to Document (82xx)
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, active_miscelaneous
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2228166_TestClass(BaseTestCase):

    def test_C2228166(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2228166'
        Test_Case_saveas_ID ="C2021059"
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        
        """
        Step 01: Launch WF, New > Chart with EMPLOYEE.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        time.sleep(5)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
           
        """
        Step 02: Double click "LAST_NAME", "CURR_SAL".
        """
        time.sleep(3)
        metaobj.datatree_field_click('LAST_NAME', 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 11)
           
        metaobj.datatree_field_click('CURR_SAL', 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
           
        """
        Step 03: Verify the following chart is displayed.
        """
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step03:a(i) Verify X-Axis Title")
        yaxis_value="CURR_SAL"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step03:a(ii) Verify y-Axis Title")
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step03:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 11, 'Step03.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 03.c: Verify first bar color")
        time.sleep(5)
           
        """
        Step 04: Drag "DEPARTMENT" to "Multi-graph"(Query Pane).
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('DEPARTMENT', 1, 'Multi-graph', 0)
        time.sleep(2)
        parent_css="#queryTreeWindow table tr:nth-child(15) td"
        resultobj.wait_for_property(parent_css, 1, expire_time=15, string_value="DEPARTMENT")
           
        """
        Step 05: Verify the following is displayed in the Query pane.
        """
        time.sleep(2)
        metaobj.verify_query_pane_field('Vertical Axis', "CURR_SAL", 1, "Step 05a:")
        metaobj.verify_query_pane_field('Horizontal Axis', "LAST_NAME", 1, "Step 05b:")
        metaobj.verify_query_pane_field('Multi-graph', "DEPARTMENT", 1, "Step 05c:")
        time.sleep(2)
           
        """
        Step 06: Click on "Document" button in "Design Grouping".
        """
        ribbonobj.select_ribbon_item('Home', 'Document')
        time.sleep(8)
        parent_css="#iaCanvasCaptionLabel"
        resultobj.wait_for_property(parent_css, 1, expire_time=15, string_value="Document")
           
        """
        Step 07: Click on the Chart on Document canvas to highlight it.
        """
        source_elem = driver.find_element_by_css_selector("#TableChart_1")
        utillobj.click_on_screen(source_elem, 'start', x_offset=10, y_offset=10)
        utillobj.click_on_screen(source_elem, 'start', click_type=0, x_offset=10, y_offset=10)
           
        """
        Step 08: Verify the following is displayed in the Query pane.
        """
        parent_css="#queryTreeWindow table tr:nth-child(15) td"
        resultobj.wait_for_property(parent_css, 1, expire_time=15, string_value="DEPARTMENT")
        time.sleep(5)
        metaobj.verify_query_pane_field('Vertical Axis', "CURR_SAL", 1, "Step 08a:")
        metaobj.verify_query_pane_field('Horizontal Axis', "LAST_NAME", 1, "Step 08b:")
        metaobj.verify_query_pane_field('Coordinated', "DEPARTMENT", 1, "Step 08c:")
         
        """
        Step 09: Click "Run".
        """
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
          
        """
        Step 10: Verify charts are produced in Document - AHTML format.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step10:a(i) Verify X-Axis Title")
        yaxis_value="CURR_SAL"
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step10:a(ii) Verify y-Axis Title")
        expected_xval_list=['BLACKWOOD', 'CROSS', 'GREENSPAN', 'JONES', 'MCCOY', 'SMITH']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 10.c: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0","CURR_SAL BY LAST_NAME", "Step 10.e : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step10.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['DEPARTMENT:MIS', 'LAST_NAME:BLACKWOOD', 'CURR_SAL:$21,780.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 10.i: verify the default tooltip values')
        time.sleep(5)
          
        """
        Step 11: Click the "DEPARTMENT" dropdown > "PRODUCTION"
        """
        dropdown_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0TABS [class*='arDashboardMergeDropdown']")
        utillobj.click_on_screen(dropdown_css, 'middle')
        utillobj.click_on_screen(dropdown_css, 'middle', click_type=0)
        time.sleep(2)
        production_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0TABS [class*='arDashboardMergeDropdown'] option[value='PRODUCTION']")
        production_css.click()
          
        """
        Step 12: Verify that another page (with different LAST_NAME) is displayed.
        """
        time.sleep(5) 
        parent_css="#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step12:a(i) Verify X-Axis Title")
        yaxis_value="CURR_SAL"
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step12:a(ii) Verify y-Axis Title")
        expected_xval_list=['BANNING', 'IRVING', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step12.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 12.c: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0","CURR_SAL BY LAST_NAME", "Step 12.e : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 12.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step12.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 12.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['DEPARTMENT:PRODUCTION', 'LAST_NAME:BANNING', 'CURR_SAL:$29,700.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 12.i: verify the default tooltip values')
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
          
        """
        Step 13: Click "IA" > "Save" > "C2021059" > "Save".
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_saveas_ID)
        time.sleep(10)
          
        """    
        Step 14: Click "IA" > "Exit".
        Step 15: Click "No" to "Save Changes to 'Chart1'?". (If we follow the step driver gets closed, hence calling api to logout)
        """
#         ribbonobj.select_tool_menu_item('menu_exit')
#         time.sleep(15)
#         parent_css="#saveAllDlg"
#         resultobj.wait_for_property(parent_css, 1)
#         btn_css="div[id*='loginForm'] div[class^=bi-button-label]"
#         dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
#         btn_text_list=[el.text.strip() for el in dialog_btns]
#         dialog_btns[btn_text_list.index('No')].click()
#         time.sleep(8)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
        Step 16: Highlight "C2021059" > Right mouse click > "Run".
        """
        utillobj.active_run_fex_api_login(Test_Case_saveas_ID+'.fex','S10032_chart_1','mrid','mrpass')
        time.sleep(10) 
        
        """
        Step 17: Verify the following chart is displayed.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5) 
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step17:a(i) Verify X-Axis Title")
        yaxis_value="CURR_SAL"
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step17:a(ii) Verify y-Axis Title")
        expected_xval_list=['BLACKWOOD', 'CROSS', 'GREENSPAN', 'JONES', 'MCCOY', 'SMITH']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step17:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step17.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 17.c: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0","CURR_SAL BY LAST_NAME", "Step 17.e : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 17.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step17.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 17.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['DEPARTMENT:MIS', 'LAST_NAME:BLACKWOOD', 'CURR_SAL:$21,780.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 17.i: verify the default tooltip values')
        time.sleep(5)
        
        """
        Step 18: Click the "DEPARTMENT" dropdown > "PRODUCTION"
        """
        dropdown_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0TABS [class*='arDashboardMergeDropdown']")
        utillobj.click_on_screen(dropdown_css, 'middle')
        utillobj.click_on_screen(dropdown_css, 'middle', click_type=0)
        time.sleep(2)
        production_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0TABS [class*='arDashboardMergeDropdown'] option[value='PRODUCTION']")
        production_css.click()
        time.sleep(5) 
        parent_css="#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step18:a(i) Verify X-Axis Title")
        yaxis_value="CURR_SAL"
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step18:a(ii) Verify y-Axis Title")
        expected_xval_list=['BANNING', 'IRVING', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step18:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step18.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 18.c: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0","CURR_SAL BY LAST_NAME", "Step 18.e : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 18.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step18.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 18.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['DEPARTMENT:PRODUCTION', 'LAST_NAME:BANNING', 'CURR_SAL:$29,700.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 18.i: verify the default tooltip values')
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#orgdiv0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step18', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 19: Close output and IA window.
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 20: Highlight "C2021059" > Right mouse click > "Edit".
        """
        utillobj.infoassist_api_edit(Test_Case_saveas_ID, 'idis', 'S10032_chart_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 21: Verify the following chart is displayed.
        """
        elem=(By.CSS_SELECTOR,'#TableChart_1')
        resultobj._validate_page(elem)
        time.sleep(5)
        parent_css="#TableChart_1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step21:a(i) Verify X-Axis Title")
        yaxis_value="CURR_SAL"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step21:a(ii) Verify y-Axis Title")
        expected_xval_list=['BLACKWOOD', 'CROSS', 'GREENSPAN', 'JONES', 'MCCOY', 'SMITH']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step21:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 6, 'Step21.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 21.c: Verify first bar color")
        time.sleep(5)
        
        """
        Step 22: Dismiss the tool window.
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()