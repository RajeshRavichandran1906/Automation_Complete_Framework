'''
Created on Nov 14, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229099
TestCase Name = Verify Export data 
'''

import unittest,time,pyautogui
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2229099_TestClass(BaseTestCase):

    def test_C2229099(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2229099'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_esrimap_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css,1)
         
        """
        Step 02: Double click "Store,Country", "Revenue"
        """
        time.sleep(4)
        metaobj.datatree_field_click("Store,Country",2,1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 42)
         
        metaobj.datatree_field_click("Revenue",2,1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css,34)
         
        time.sleep(3)
        xaxis_value="Store Country"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 02:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 02:a(ii) Verify Y Axis Title")
        expected_xval_list=['Australia', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Czech Republic', 'Denmark', 'Egypt', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Mexico', 'Netherlands', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Singapore', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'United Kingdom', 'United States']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M', '600M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 02:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 34, 'Step 02.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar", "bar_blue1", "Step 02.c: Verify first bar color")
        time.sleep(5)
        bar=['Store Country:Canada', 'Revenue:$51,147,788.36', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!", bar, "Step 02.d: Verify bar value")
        time.sleep(5)
         
        """
        Step 03: Click "Change" dropdown > "ESRI Choropleth"
        """
        ribbonobj.change_chart_type('choropleth_map')
        time.sleep(5)        
        parent_css2="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css2, 33) 
        
        """
        Step 04: Click the Show Data menu dropdown
        Step 05: Select "Export Data" > "Summary"
        """
        resultobj.select_panel_caption_btn(0, select_type='menu')
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Export Data', verify='true', expected_popup_list=['Show Data','Show Data with Related Columns','Export Data'],msg='Step04: Verify Show data menu')
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Summary')
        
        """
        Step 06: Download and Open the Excel file
        Step 07: Verify the excel spreadsheet contains the data from the fields
        Step 08: Dismiss ExceD:\work
        """
        browser = utillobj.parseinitfile('browser')
        time.sleep(20)
        if browser == 'IE':
            pyautogui.hotkey('alt', 'f4')
        if browser == 'Chrome':
            utillobj.save_window('C2229099_actual_'+browser, pyautogui_save=True)
            time.sleep(5)
            utillobj.create_excel('C2229099_actual_'+browser+'.xls','C2229099_actual_'+browser+'.xlsx', pyautogui_save=True)
        else:
            time.sleep(10)
            utillobj.saveas_excel_sheet_esrimap('C2229099_actual_'+browser+'.xlsx')
        time.sleep(5)
        utillobj.verify_excel_sheet('C2229099_base_'+browser+'.xlsx', 'C2229099_actual_'+browser+'.xlsx', 'Sheet1', 'Step 07: Verify the excel spreadsheet contains the data from the fields')
        time.sleep(2)
        if browser != 'IE':
            utillobj.switch_to_main_window()
            
            
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(2)

        """
        Step 09: Click "Save" icon
        Step 10: Enter Title "C2229099"
        Step 11: Click "Save" and dismiss IA
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(4)
        
if __name__ == '__main__':
    unittest.main()