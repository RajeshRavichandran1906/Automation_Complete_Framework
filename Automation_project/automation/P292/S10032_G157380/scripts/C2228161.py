'''
Created on Dec 26, 2017

@author: BM13368
TestCase ID :http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228161
TestCase Name : Verify Data Labels with “Currency General” format (82xx)
TestSuite :http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2228161_TestClass(BaseTestCase):

    def test_C2228161(self):
        
        Test_Case_ID1 = "IA-CHART-VAL-016"
        driver = self.driver
        utillobj = utillity.UtillityMethods(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        ia_ribbon_obj=ia_ribbon.IA_Ribbon(driver)
        
        """
            Step 01:Launch WF, New > Chart with EMPLOYEE.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10660_chart_1', 'mrid', 'mrpass')
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1)
        """  
            Step 02:Double click "LAST_NAME", "SALARY", "GROSS".
        """
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 11)
        metaobj.datatree_field_click("SALARY", 2, 1)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.datatree_field_click("GROSS", 2, 1)
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 22)
        
        """  
            Step 03:Select "Series" tab.
            Step 04:Click "Data Labels" (dropdown) > "More Data Label Options".
        """
        ribbonobj.select_ribbon_item('Series', 'Data_labels_menubtn', opt='More Data Label Options')
        parent_css="[id^='QbDialog'] [class*='active'] [class*='window-caption']"
        resultobj.wait_for_property(parent_css, 1, expire_time=30)
       
        """ 
            Step 05:Check "Show Data Labels" check box.
        """
        ia_ribbon_obj.set_format_labels_general('checkbox', 'show_data_label', 'uncheck')
        """ 
            Step 06:Click "General" (dropdown) next to "Format Labels".
            Step 07:Select "Currency General".
        """
        ia_ribbon_obj.set_format_labels_general('combobox', 'format_labels', 'Currency general')
        
        """ 
            Step 08:Click "OK" in the "Format Labels" window.
        """
        ok_btn=driver.find_element_by_css_selector("#dataLabelsOkBtn")
        utillobj.click_on_screen(ok_btn, "middle", click_type=0)
        """  
            Step 09:Verify Data Labels in currency format are added to the chart in "Live Preview".
        """
        parent_css="#TableChart_1 text[class*='dataLabels']"
        resultobj.wait_for_property(parent_css, 22)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 09:01: Verify x-axis title")
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 09:02: Verify x-axis labels")
        resultobj.verify_number_of_riser("TableChart_1", 2, 11, 'Step 09:03: Verify the total number of risers displayed on preview')
        legend=['SALARY', 'GROSS']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step 09:04:")
        expected_data_labels1=['$29,700.00', '$21,780.00', '$52,837.00', '$17,650.00', '$51,282.00', '$36,230.00', '$18,480.00', '$31,100.00', '$21,120.00', '$31,750.00', '$21,000.00']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels1, 'Step 09:05: Verify data labels1', custom_css="text[class*='dataLabels!s0']")
        expected_data_labels2=['$2,475.00', '$9,075.00', '$22,013.75', '$2,970.84', '$17,094.00', '$6,099.50', '$1,540.00', '$9,130.00', '$7,040.00', '$14,983.36', '$9,000.02']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels2, 'Step 09:06: Verify data labels2', custom_css="text[class*='dataLabels!s1']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 09:07: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step 09:08: Verify first bar color")
        
        """ 
            Step 10:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        
        """  
            Step 11:Verify the same chart displayed in "Live Preview" is displayed at runtime.
        """
        parent_css="#jschart_HOLD_0 text[class*='dataLabels']"
        resultobj.wait_for_property(parent_css, 22, expire_time=50)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 11:01: Verify x-axis title")
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step 11:02: Verify x-axis labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 2, 11, 'Step 15:03: Verify the total number of risers displayed on preview')
        legend=['SALARY', 'GROSS']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 15:04:")
        expected_data_labels1=['$29,700.00', '$21,780.00', '$52,837.00', '$17,650.00', '$51,282.00', '$36,230.00', '$18,480.00', '$31,100.00', '$21,120.00', '$31,750.00', '$21,000.00']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels1, 'Step 15:05: Verify data labels1', custom_css="text[class*='dataLabels!s0']")
        expected_data_labels2=['$2,475.00', '$9,075.00', '$22,013.75', '$2,970.84', '$17,094.00', '$6,099.50', '$1,540.00', '$9,130.00', '$7,040.00', '$14,983.36', '$9,000.02']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels2, 'Step 15:06: Verify data labels2', custom_css="text[class*='dataLabels!s1']")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 15:07: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar", "bar_green", "Step 15:08: Verify first bar color")
        bar=['LAST_NAME:BANNING', 'SALARY:$29,700.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar", bar,"Step 15:09: Verify bar value")
            
        """ 
            Step 12:Click "IA" > "Save".
            Step 13:Enter Title = "IA-CHART-VAL-016".
            Step 14:Click "Save" and dismiss IA window.
        """
        utillobj.switch_to_default_content(pause=2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID1)
        time.sleep(5)
        utillobj.infoassist_api_logout()  
       
        """  
            Step 15:Locate the saved fex > Right mouse click > "Run".
        """
        utillobj.active_run_fex_api_login(Test_Case_ID1+".fex", "S10032_chart_1", 'mrid', 'mrpass')
        
        """  
            Step 16:Verify the chart is run in a new window.
        """
        parent_css="#jschart_HOLD_0 text[class*='dataLabels']"
        resultobj.wait_for_property(parent_css, 22)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 16:01: Verify x-axis title")
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step 16:02: Verify x-axis labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 2, 11, 'Step 16:03: Verify the total number of risers displayed on preview')
        legend=['SALARY', 'GROSS']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 16:04:")
        expected_data_labels1=['$29,700.00', '$21,780.00', '$52,837.00', '$17,650.00', '$51,282.00', '$36,230.00', '$18,480.00', '$31,100.00', '$21,120.00', '$31,750.00', '$21,000.00']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels1, 'Step 16:05: Verify data labels1', custom_css="text[class*='dataLabels!s0']")
        expected_data_labels2=['$2,475.00', '$9,075.00', '$22,013.75', '$2,970.84', '$17,094.00', '$6,099.50', '$1,540.00', '$9,130.00', '$7,040.00', '$14,983.36', '$9,000.02']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels2, 'Step 16:06: Verify data labels2', custom_css="text[class*='dataLabels!s1']")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 16:07: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar", "bar_green", "Step 16:08: Verify first bar color")
        bar=['LAST_NAME:BANNING', 'SALARY:$29,700.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar", bar,"Step 16:09: Verify bar value")
        """ 
            Step 17:Dismiss the chart run window.
        """
        utillobj.infoassist_api_logout()
        """  
            Step 18:Locate the saved fex > Right mouse click > "Edit".
        """
        utillobj.infoassist_api_edit(Test_Case_ID1, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1)
        """  
            Step 19:Verify IA is launched and the chart is preserved in "Live Preview".
        """
        parent_css="#TableChart_1 text[class*='dataLabels']"
        resultobj.wait_for_property(parent_css, 22)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 19:01: Verify x-axis title")
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 19:02: Verify x-axis labels")
        resultobj.verify_number_of_riser("TableChart_1", 2, 11, 'Step 19:03: Verify the total number of risers displayed on preview')
        legend=['SALARY', 'GROSS']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step 19:04:")
        expected_data_labels1=['$29,700.00', '$21,780.00', '$52,837.00', '$17,650.00', '$51,282.00', '$36,230.00', '$18,480.00', '$31,100.00', '$21,120.00', '$31,750.00', '$21,000.00']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels1, 'Step 19:05: Verify data labels1', custom_css="text[class*='dataLabels!s0']")
        expected_data_labels2=['$2,475.00', '$9,075.00', '$22,013.75', '$2,970.84', '$17,094.00', '$6,099.50', '$1,540.00', '$9,130.00', '$7,040.00', '$14,983.36', '$9,000.02']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels2, 'Step 19:06: Verify data labels2', custom_css="text[class*='dataLabels!s1']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 19:07: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step 19:08: Verify first bar color")
        
        """ 
            Step 20:Click "IA" > "Exit".
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    unittest.main()