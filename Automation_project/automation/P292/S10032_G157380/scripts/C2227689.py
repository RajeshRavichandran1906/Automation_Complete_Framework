'''
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2227689

'''

import unittest,time, pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,ia_run,ia_styling,ia_resultarea
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators


class C2227689_TestClass(BaseTestCase):
    
    def test_C2227689(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227689'
        bar1=['Sale Year:2014', 'Cost of Goods Local Currency:540,969,939.93', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        bar2=['Sale Year:2016', 'Cost of Goods:$325,821,316.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        expected_xval_list=['2011', '2012', '2013', '2014', '2015', '2016']
        expected_yval_list=['0', '0.4B', '0.8B', '1.2B','1.6B', '2B', '2.4B']
        oLegends=['Cost of Goods Local Currency','Cost of Goods']
        
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_styobj=ia_styling.IA_Style(self.driver)
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """    2. Drag "Cost of Goods,Local Currency" to Vertical Axis.    """
        metaobj.datatree_field_click("Cost of Goods,Local Currency", 2, 1)
        time.sleep(8)
        
        """    3. Drag "Cost of Goods" to Vertical Axis.    """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(8)
        
        """    4. Drag "Sale,Year" to Horizontal Axis.    """
        metaobj.datatree_field_click("Sale,Year", 2, 1)
        time.sleep(8)
        
        """    5. Select "Format" > "Report" > "Header & Footer" (dropdown) > "Page Header".    """
        ribbonobj.select_ribbon_item('Format','Header_footer', opt='Page Header')
        
        """    6. Type "Test for Page Header".    """
        iframe=driver.find_element_by_css_selector("#subheaderDlg #Editor")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        w_fr=iframe.size['width']
        pyautogui.moveTo(x_fr+(w_fr/2), y_fr+100)
        time.sleep(1)
        pyautogui.click(x_fr+(w_fr/2), y_fr+100)
        time.sleep(1)
        pyautogui.press('home')
        time.sleep(3)
        for i in range(0,15):
            pyautogui.press('delete')
        time.sleep(3)
        pyautogui.typewrite("Test for Page Header")
        time.sleep(3)
        
        """    7. Change to Bold, Center, Font color = Blue (RGB = (0,128,192)), Size = 14 > Click "Apply".    """
        pyautogui.moveTo(x_fr+(w_fr/2), y_fr+100)
        time.sleep(1)
        pyautogui.click(x_fr+(w_fr/2), y_fr+100)
        ia_styobj.set_header_footer_style(font_size='14', bold=True, center_justify=True, text_color='light_blue')
        time.sleep(2) 
        driver.find_element_by_css_selector("#subheaderDlg #applyBtn").click()
        time.sleep(15)
        
        """    8. Verify the Header styling has been applied on the canvas.    """
        oHead=driver.find_element_by_css_selector("#MAINTABLE_1 foreignObject[class='title'] span").text.strip()
        utillobj.asequal("Test for Page Header",oHead, "step 08a: Verify Header styling has been applied on the canvas")
        
        """    9. Click "Page Footer" on "Header & Footer" window.    """
        elem=driver.find_element_by_css_selector("#subheaderDlg #pgFting img")
        utillobj.default_left_click(object_locator=elem)
        time.sleep(5)
        
        """    10. Type "Test for Page Footer".    """
        pyautogui.moveTo(x_fr+(w_fr/2), y_fr+100)
        time.sleep(1)
        pyautogui.click(x_fr+(w_fr/2), y_fr+100)
        time.sleep(1)
        pyautogui.press('home')
        time.sleep(3)
        for i in range(0,15):
            pyautogui.press('delete')
        time.sleep(3)
        pyautogui.typewrite("Test for Page Footer")
        time.sleep(3)
        
        """    11. Change to Bold, Font color = Red (RGB = (255, 0, 0)), Size = 14 > Click "Apply".    """
        pyautogui.moveTo(x_fr+(w_fr/2), y_fr+100)
        time.sleep(1)
        pyautogui.click(x_fr+(w_fr/2), y_fr+100)
        ia_styobj.set_header_footer_style(font_size='14', bold=True, text_color='red')
        time.sleep(2) 
        driver.find_element_by_css_selector("#subheaderDlg #applyBtn").click()
        time.sleep(15)
        
        """    12. Click "OK".    """
        driver.find_element_by_id("okBtn").click()
        time.sleep(8)
        
        """    13. Verify the following is displayed.    """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!", bar1, "Step 13(i): Verify Cost of Goods Local Currency bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g5!mbar!", bar2, "Step 13(ii): Verify Cost of Goods bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Sale Year', "Step 13:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", oLegends, "Step 13:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 13:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 13.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 13.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "pale_green", "Step 13.c(ii): Verify first bar color")
        time.sleep(1)
        resultobj.verify_header_footer_text("title", font_color='light_blue', bold=True, msg='Step 13 d(i):')
        resultobj.verify_header_footer_text("footnote", font_color='red', bold=True, msg='Step 13 d(ii):')
        
        """    14. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(10)
        
        """    15. Verify the following is displayed.    """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!", bar1, "Step 15(i): Verify Cost of Goods Local Currency bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g5!mbar!", bar2, "Step 15(ii): Verify Cost of Goods bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Sale Year', "Step 15:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", oLegends, "Step 15:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 15:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 15.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 15.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "pale_green", "Step 15.c(ii): Verify first bar color")
        time.sleep(1)
        resultobj.verify_header_footer_text("title", font_color='light_blue', bold=True, msg='Step 15 d(i):')
        resultobj.verify_header_footer_text("footnote", font_color='red', bold=True, msg='Step 15 d(ii):')
        
        """    16. Dismiss the "Run" window.    """
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """    17. Click "IA" > "Save" > "C2160093" > "Save".    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    18. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """    19. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160093.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(20)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    20. Verify the following is displayed.    """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!", bar1, "Step 20(i): Verify Cost of Goods Local Currency bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g5!mbar!", bar2, "Step 20(ii): Verify Cost of Goods bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Sale Year', "Step 20:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", oLegends, "Step 20:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 20:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 20.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 20.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "pale_green", "Step 20.c(ii): Verify first bar color")
        time.sleep(1)
        resultobj.verify_header_footer_text("title", font_color='light_blue', bold=True, msg='Step 20 d(i):')
        resultobj.verify_header_footer_text("footnote", font_color='red', bold=True, msg='Step 20 d(ii):')
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step20', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    21. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()