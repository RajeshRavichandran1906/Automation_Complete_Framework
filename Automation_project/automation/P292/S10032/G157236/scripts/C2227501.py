'''
Created on Nov 16, 2017

@author: BM13368
Testcase Name : Verify InfoMini request with Chart mode 
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227501
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity, global_variables

class C2227501_TestClass(BaseTestCase):

    def test_C2227501(self):
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2227501'
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
            Step 01 : Launch IA Chart mode:
            http://machine:port/ibi_apps/ia?tool=Chart&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('chart','ibisamp/car','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        """
            Step 02 : Double click "CAR", "SALES".
        """
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("SALES", 2, 1)
        time.sleep(4)
        """
            Step 03 : Verify the following "Chart" in Live Preview
        """
        time.sleep(5)
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 03:01: X and Y axis labels')
        resultobj.verify_xaxis_title('TableChart_1', 'CAR', "Step 03:02: Verify X-Axis Title")
        resultobj.verify_yaxis_title('TableChart_1', 'SALES', "Step 03:03: Verify Y-Axis Title")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 03:04: Verify first bar color")
        
        """
            Step 04 : Select "Format" > "InfoMini" (dropdown) > "Resources/Field Tab" and "Series Tab".
        """
        ribbonobj.select_ribbon_item("Format", "Infomini_arrow")
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu("Resources/Field Tab")
        time.sleep(0.5)
        ribbonobj.select_ribbon_item("Format", "Infomini_arrow")
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu("Series Tab")
        time.sleep(8)
        
        """
            Step 05 : Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        time.sleep(10)
        utillobj.switch_to_frame(pause=2)
        """
            Step 06 : Verify InfoMini application is displayed in a new window.
        """
        time.sleep(5)
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 06:01: X and Y axis labels')
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'CAR', "Step 06:02: Verify X-Axis Title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', 'SALES', "Step 06:03: Verify Y-Axis Title")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 06:04: Verify first bar color")
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 06:05: Verify X-Axis Title")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'SALES:30200']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 06:06 Verify tooltiptip values")
        utillobj.switch_to_default_content(pause=1)
        
        if global_variables.Global_variables.browser_name == 'ie':
            outer_height = self.driver.execute_script("return window.outerHeight;")
            availHeight = self.driver.execute_script("return screen.availHeight;")
            browser_height =  (outer_height-availHeight)+6
            global_variables.Global_variables.current_working_area_browser_y=browser_height
            
        """
            Step 07 : On InfoMini application, click "Edit" button.
        """
        ribbonobj.select_top_toolbar_item('infomini_edit')
        time.sleep(5)
        parent_css="#IaToolbar"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(10)
        """
            Step 08 : Verify "Series" tab is displayed and InfoMini entered into "Edit Mode" (Data, Filter and Query pane).
        """
        css_obj=self.driver.find_element_by_css_selector("#IaToolbar #SeriesTab_tabButton")
        status=css_obj.is_displayed()
        utillobj.asequal(status, True, 'Step 08:01: Veirfy series tab is dispalyed')
        metaobj.verify_query_pane_field("Vertical Axis", "SALES", 1, 'Step 08:02: Verify in query pane Vertical axis has SALES')
        metaobj.verify_query_pane_field("Horizontal Axis", "CAR", 1, 'Step 08:03: Verify in query pane Horizontal axis has CAR')
        """
            Step 09 : Select "Format" > "Chart Types" > Pie.
        """
        ribbonobj.select_ribbon_item("Format", "Pie")
        time.sleep(3)
        """
            Step 10 : Click "Run" in InfoMini.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(10)
        """
            Step 11 : Verify the Pie chart is displayed.
        """
        ""
        time.sleep(2)
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mwedge!", "bar_blue", "Step 11:02: Verify pie chart color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g0!mwedge!", "dark_green", "Step 11:03: Verify second pie chart slice color")
        resultobj.verify_number_of_pie_segments("jschart_HOLD_0", 1, 10, "Step 11:04: Verify number pie chart segments")
        resultobj.verify_riser_pie_labels_and_legends('jschart_HOLD_0', ['SALES'],"'Step 11:05: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
        resultobj.verify_riser_legends('jschart_HOLD_0',['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], 'Step 11:06: Verify chart legends')
        expected_tooltip_list=['CAR:ALFA ROMEO', 'SALES:30200  (14.49%)']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mwedge!", expected_tooltip_list, "Step 11:07: Verify pie slice tooltip value")
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        
        if global_variables.Global_variables.browser_name == 'ie':
            outer_height = self.driver.execute_script("return window.outerHeight;")
            availHeight = self.driver.execute_script("return screen.availHeight;")
            browser_height =  (outer_height-availHeight)+6
            global_variables.Global_variables.current_working_area_browser_y=browser_height
         
        """
            Step 12 : Click Series tab
            Step 13 : Click Data labels
        """
        ribbonobj.select_ribbon_item("Series", "Data_Labels")
        time.sleep(8)
         
        """
            Step 14 : Click Run in infomini
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(10)
        """
            Step 15 : Verify the Pie chart is displayed with feelers line
        """
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mwedge!", "bar_blue", "Step 15:01: Verify pie chart color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g0!mwedge!", "dark_green", "Step 15:02: Verify second pie chart slice color")
        resultobj.verify_number_of_pie_segments("jschart_HOLD_0", 1, 6, "Step 15:03: Verify number pie chart segments")
        labels_list=['SALES']
        resultobj.verify_riser_pie_labels_and_legends('jschart_HOLD_0', labels_list,"'Step 15:04: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'SALES:30200  (14.49%)']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mwedge!", expected_tooltip_list, "Step 15:05: Verify pie slice tooltip value")
        resultobj.verify_riser_legends('jschart_HOLD_0',['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], 'Step 15:06: Verify chart legends')
        expected_datalabel=['14%', '4%', '39%', '21%', '6%', '17%']
        resultobj.verify_data_labels("jschart_HOLD_0", expected_datalabel, "Step 15:07: Verify the data lables in the pie chart", custom_css="svg > g.chartPanel text[class*='mdataLabels']")
         
        """
            Step 16 : On InfoMini application, click "Save" 
        """
        utillobj.switch_to_default_content(pause=1)
        
        if global_variables.Global_variables.browser_name == 'ie':
            outer_height = self.driver.execute_script("return window.outerHeight;")
            availHeight = self.driver.execute_script("return screen.availHeight;")
            browser_height =  (outer_height-availHeight)+6
            global_variables.Global_variables.current_working_area_browser_y=browser_height
             
        """
            Step 17 :Enter Title = "C2227501" > "Save".
        """
        ribbonobj.select_top_toolbar_item('infomini_save')
        utillobj.ibfs_save_as(Test_Case_ID)
         
        """
            Step 18 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
            Step 19 : Logon to WF:
            http://machine:port/ibi_apps/
            Step 20 : Right-click "C2227501" > Run
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10032_infoassist_4", 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 190)
        utillobj.switch_to_frame(pause=2)
#         parent_css="#jschart_HOLD_0 text[class^='pieLabel!g']"
#         resultobj.wait_for_property(parent_css, 1)
        time.sleep(10)
         
        """
            Step 21 : Verify InfoMini application is displayed as follows
        """
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mwedge!", "bar_blue", "Step 21:01: Verify pie chart color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g0!mwedge!", "dark_green", "Step 21:02: Verify second pie chart slice color")
        resultobj.verify_number_of_pie_segments("jschart_HOLD_0", 1, 6, "Step 21:03: Verify number pie chart segments")
        labels_list=['SALES']
        resultobj.verify_riser_pie_labels_and_legends('jschart_HOLD_0', labels_list,"'Step 21:04: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'SALES:30200  (14.49%)']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mwedge!", expected_tooltip_list, "Step 21:05: Verify pie slice tooltip value")
        resultobj.verify_riser_legends('jschart_HOLD_0',['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], 'Step 21:06: Verify chart legends')
        expected_datalabel=['14%', '4%', '39%', '21%', '6%', '17%']
        resultobj.verify_data_labels("jschart_HOLD_0", expected_datalabel, "Step 21:07: Verify the data lables in the pie chart", custom_css="svg > g.chartPanel text[class*='mdataLabels']")
         
        """
            Step 22 : Close InfoMini application window.
        """
        driver.close()
        utillobj.switch_to_window(0)
        utillobj.wf_logout()
        time.sleep(3)
        
        """
            Step 23 : Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227501.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_infosassist_4', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1", 1, 190)
        
        """
            Step 24 : Verify successful restore
        """
        time.sleep(5)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!", "bar_blue", "Step 24:01: Verify pie chart color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mwedge!", "dark_green", "Step 24:02: Verify second pie chart slice color")
        resultobj.verify_number_of_pie_segments("TableChart_1", 1, 6, "Step 24:03: Verify number pie chart segments")
        labels_list=['SALES']
        resultobj.verify_riser_pie_labels_and_legends('TableChart_1', labels_list,"'Step 24:04: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
        resultobj.verify_riser_legends('TableChart_1',['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], 'Step 24:06: Verify chart legends')
        expected_datalabel=['14%', '4%', '39%', '21%', '6%', '17%']
        resultobj.verify_data_labels("TableChart_1", expected_datalabel, "Step 24:07: Verify the data lables in the pie chart", custom_css="svg > g.chartPanel text[class*='mdataLabels']")
         
        """
            Step 25 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
#         utillobj.infoassist_api_logout()
#         time.sleep(3)

    if __name__ == "__main__":
        unittest.main()