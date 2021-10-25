'''
Created on Nov 27, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349044
TestCase Name = Verify Demographic layer is displayed in Storyboard
'''

import unittest
import time, pyautogui, os
from common.lib import utillity
from common.pages import visualization_resultarea, visualization_ribbon, wf_map
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2349044_TestClass(BaseTestCase):

    def test_C2349044(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2349044'
        
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis', 'baseapp/wf_retail_lite', 'P292/S10032_esrimap_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css,1)
            
        """
        Step 02: Click "Change" dropdown > "Choropleth" (ESRI)
        """
        ribbonobj.change_chart_type("choropleth_map")
        time.sleep(5)
        parent_css="[class*='esriScalebarSecondNumber']"
        resultobj.wait_for_property(parent_css,2)
         
        """
        Step 03: Go to Format tab > "Demographic Layers"
        """
        ribbonobj.select_ribbon_item('Format','Demographiclayers')
         
        """
        Step 04: Verify the demographic layer dialog
        """
        Demographic_css="[id^='QbDemographicLayersDlg'] [id^='DemographicLayerGrid']"
        resultobj.wait_for_property(Demographic_css, 2)
 
        """
        Step 05: Check "USA Unemployment Rate 2012", "USA Tapestry Segmentation 2012" 
        Step 06: Click OK
        """
        lifestyle_list=[('USA Tapestry Segmentation 2012',0)]
        population_list=[('USA Unemployment Rate 2012',9)]
        wfmapobj.select_demographic_layer(lifestyle_list, population_list, btn_click='Ok')
        time.sleep(5)
         
        """
        Step 07: Verify the map is updated
        """
        scale_bar_css="[class*='esriScalebarSecondNumber']"
        resultobj.wait_for_property(scale_bar_css, 2)
        time.sleep(6)
        ele=driver.find_element_by_css_selector("#TableChart_1")
        utillobj.take_screenshot(ele,'C2349044_Actual_step07', image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """
        Step 08: Go to Home tab
        Step 09: Click "Add"
        """
        ribbonobj.select_ribbon_item('Home','Add_storyboard')
        time.sleep(8)
          
        """
        Step 10: Click OK in the dialog
        """
        parent_css="div[id^='BiDialog'] img[src*='infomark']"
        resultobj.wait_for_property(parent_css, 1)
        btn_css="div[id^='BiDialog'] div[class=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('OK')].click()
        time.sleep(5)
          
        """
        Step 11: Click "Show" in the Ribbon
        """
        ribbonobj.select_ribbon_item('Home','show_storyboard')
        time.sleep(8)
          
        """
        Step 12: Open the PowerPoint file
        Step 13: Verify the map is displayed in the slide
        Step 14: Dismiss PowerPoint and return to Visualization
        """
        if utillobj.browser == 'Chrome':
            actual_file=Test_Case_ID+'_actual_13_'+utillobj.browser+'_1'
            print(actual_file)
            if os.path.isfile(os.getcwd()+"\\data\\"+actual_file+".pptx"):
                os.remove(os.getcwd()+"\\data\\"+actual_file+".pptx")
            pyautogui.typewrite(os.getcwd()+"\\data\\"+actual_file, pause=2)
            pyautogui.press('enter',  pause=7)
            os.startfile(os.getcwd()+"\\data\\"+actual_file+".pptx")
            time.sleep(5)
        else:
            os.system(os.getcwd()+"\\common\\lib\\Open_file.exe "+utillobj.browser)
        time.sleep(15)
        pyautogui.press('f5', pause=5)
        time.sleep(1)
        utillobj.take_monitor_screenshot(Test_Case_ID+'_Actual_Step13', image_type='actual', left=145, top=0, right=145, bottom=0)  
        time.sleep(7)
        pyautogui.press('esc', pause=5)
        utillobj.kill_process('POWERPNT')
        time.sleep(9)
        utillobj.switch_to_main_window()
        time.sleep(2)
        utillobj.switch_to_default_content()
        time.sleep(10)
        
        """
        Step 15: Click "Layers"
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(6)
        layer1="div[class^='TableOfContentsButton UIButton']"
        layerbutton=driver.find_element_by_css_selector(layer1)
        
        browser = utillobj.parseinitfile('browser')
        if browser == 'Chrome':
            try:
                print("Inside try")
                utillobj.click_on_screen(layerbutton, 'top_middle', y_offset=-35)
                time.sleep(2)
                utillobj.click_on_screen(layerbutton, 'top_middle', click_type=0, y_offset=-35)
            except:
                print("Exception happened")
                utillobj.click_on_screen(layerbutton, 'top_middle', y_offset=-35)
                time.sleep(2)
                utillobj.click_on_screen(layerbutton, 'top_middle', click_type=0, y_offset=-35)
        else:
            try:
                print("Inside try")
                utillobj.click_on_screen(layerbutton, 'middle')
                time.sleep(2)
                utillobj.click_on_screen(layerbutton, 'middle', click_type=0)
            except:
                print("Exception happened")
                utillobj.click_on_screen(layerbutton, 'middle')
                time.sleep(2)
                utillobj.click_on_screen(layerbutton, 'middle', click_type=0)
        time.sleep(3)
        
        """
        Step 16: Uncheck "USA Unemployment Rate 2012"
        """
        parent_css="div[class*='toc-title-container']  input[type^='checkbox']"
        resultobj.wait_for_property(parent_css, 2)
        val_obj=driver.find_elements_by_css_selector(parent_css)
        driver.execute_script("arguments[0].scrollIntoView(true);", val_obj[1])
        time.sleep(1)
        check_box=driver.find_elements_by_css_selector("div[class*='toc-title-container']  input[type^='checkbox']")
        if browser == 'Chrome':
            utillobj.click_on_screen(check_box[1], 'top_middle', y_offset=-40)
            utillobj.click_on_screen(check_box[1], 'top_middle', click_type=0, y_offset=-40)
        else:
            utillobj.click_on_screen(check_box[1], coordinate_type='middle')
            utillobj.click_on_screen(check_box[1], coordinate_type='middle', click_type=0)
        time.sleep(6)
        
        """
        Step 17: Verify the map is updated
        """
        scale_bar_css="[class*='esriScalebarSecondNumber']"
        resultobj.wait_for_property(scale_bar_css, 2)
        time.sleep(6)
        ele=driver.find_element_by_css_selector("#TableChart_1")
        utillobj.take_screenshot(ele,'C2349044_Actual_step17', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 18: Click "Layers"
        """
        time.sleep(5)
        layer1="div[class^='TableOfContentsButton UIButton']"
        layerbutton=driver.find_element_by_css_selector(layer1)
        if browser == 'Chrome':
            try:
                print("Inside try")
                utillobj.click_on_screen(layerbutton, 'top_middle', y_offset=-35)
                time.sleep(2)
                utillobj.click_on_screen(layerbutton, 'top_middle', click_type=0, y_offset=-35)
            except:
                print("Exception happened")
                utillobj.click_on_screen(layerbutton, 'top_middle', y_offset=-35)
                time.sleep(2)
                utillobj.click_on_screen(layerbutton, 'top_middle', click_type=0, y_offset=-35)
        else:        
            try:
                print("Inside try")
                utillobj.click_on_screen(layerbutton, coordinate_type='middle')
                utillobj.click_on_screen(layerbutton, coordinate_type='middle', click_type=0)
            except:
                print("Exception happened")
                utillobj.click_on_screen(layerbutton, coordinate_type='middle')
                utillobj.click_on_screen(layerbutton, coordinate_type='middle', click_type=0)
        time.sleep(3)
        
        """
        Step 19: Click "Add" > OK
        """
        ribbonobj.select_ribbon_item('Home','Add_storyboard')
        time.sleep(8)
        parent_css="div[id^='BiDialog'] img[src*='infomark']"
        resultobj.wait_for_property(parent_css, 1)
        
        btn_css="div[id^='BiDialog'] div[class=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('OK')].click()
        time.sleep(5)
        
        """
        Step 20: Click "Show"
        """
        ribbonobj.select_ribbon_item('Home','show_storyboard')
        
        """
        Step 21: Open the PowerPoint file
        Step 22: Click the 2nd slide
        Step 23: Verify the slide is displayed correctly
        Step 24: Dismiss PowerPoint and return to Visualization
        """
        if utillobj.browser == 'Chrome':
            actual_file1=Test_Case_ID+'_actual_23_'+utillobj.browser+'_1'
            print(actual_file1)
            if os.path.isfile(os.getcwd()+"\\data\\"+actual_file1+".pptx"):
                os.remove(os.getcwd()+"\\data\\"+actual_file1+".pptx")
            pyautogui.typewrite(os.getcwd()+"\\data\\"+actual_file1, pause=2)
            pyautogui.press('enter',  pause=7)
            os.startfile(os.getcwd()+"\\data\\"+actual_file1+".pptx")
            time.sleep(5)
        else:
            os.system(os.getcwd()+"\\common\\lib\\Open_file.exe "+utillobj.browser)
        time.sleep(15)
        pyautogui.press('f5', pause=5)
        time.sleep(3)
        pyautogui.press('down', pause=5)
        time.sleep(1)
        utillobj.take_monitor_screenshot(Test_Case_ID+'_Actual_Step23', image_type='actual', left=145, top=0, right=145, bottom=0)  
        time.sleep(7)
        pyautogui.press('esc', pause=5)
        utillobj.kill_process('POWERPNT')
        time.sleep(9)
        utillobj.switch_to_main_window()
        time.sleep(2)
        utillobj.switch_to_default_content()
        
        """
        Step 25: Click "Save" icon
        Step 26: Enter Title "C2229101"
        Step 27: Click "Save"
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """
        Step 28: Click "IA" > "Exit"
        Step 29: Click "No" in the "Save Storyboard" dialog
        """
        ribbonobj.select_tool_menu_item('menu_exit')
        time.sleep(5)
        self.driver.find_element_by_css_selector("div[id^='BiDialog'] img[src*='questionmark']").is_displayed()
        btn_css="div[id^='BiDialog'] div[class=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('No')].click()
        time.sleep(10)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 30: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2229101.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_esrimap_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 31: Verify Visualization is restored, preserving the map
        """
        elem=(By.CSS_SELECTOR,'#TableChart_1')
        resultobj._validate_page(elem)
        scale_bar_css="[class*='esriScalebarSecondNumber']"
        resultobj.wait_for_property(scale_bar_css, 2)
        time.sleep(6)
        ele=driver.find_element_by_css_selector("#TableChart_1")
        utillobj.take_screenshot(ele,'C2349044_Actual_step31', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)
        
        """
        Step 32: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
                
if __name__ == '__main__':
    unittest.main()