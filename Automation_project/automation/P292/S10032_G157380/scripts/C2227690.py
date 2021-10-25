'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227690
'''
import unittest
import time, pyautogui, os
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity

class C2227690_TestClass(BaseTestCase):
    def test_C2227690(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227690'
        bar1=['Product Category:Media Player', 'Revenue:$246,073,059.36', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M','200M', '250M', '300M', '350M']
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
              
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """    2. Double click "Product,Category", "Revenue"    """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(8)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!", bar1, "Step 2(i): Verify Cost of Goods Local Currency bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 2:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 2:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 2:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 2.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g6!mbar!", "lochmara", "Step 2.c(i): Verify first bar color")
        time.sleep(1)
        
        """    3. Click "Add" in the Home tab    """
        ribbonobj.select_ribbon_item('Home','Add_storyboard')
        
        """    4. Click OK in the dialog    """
        self.driver.find_element_by_css_selector("div[id^='BiDialog'] img[src*='infomark']").is_displayed()
        btn_css="div[id^='BiDialog'] div[class=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('OK')].click()
        time.sleep(5)
        
        """    5. Click "Save" icon    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(5)
        
        """    6. Enter Title "C2160117" > Save    """
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    7. Click "IA" button > "Exit"    """
        ribbonobj.select_tool_menu_item('menu_exit')
        time.sleep(3)
        
        
        """    8. Click "Yes" in the dialog to save storyboard    """
        self.driver.find_element_by_css_selector("div[id^='BiDialog'] img[src*='questionmark']").is_displayed()
        btn_css="div[id^='BiDialog'] div[class=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('Yes')].click()
        time.sleep(5)
        
        """    9. Save the PowerPoint file (dependent on browser)    """
        """    10. Verify the IA window is closed    """
        """    11. Open the PowerPoint file    """
        """    12. Verify the slide    """
        """    13. Dismiss PowerPoint    """
        if utillobj.browser == 'Chrome':
            actual_file=Test_Case_ID+'_actual_12_'+utillobj.browser+'_1'
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
        utillobj.take_monitor_screenshot(Test_Case_ID+'_Actual_Step12', image_type='actual', left=145, top=0, right=145, bottom=0)  
        time.sleep(7)
        pyautogui.press('esc', pause=5)
        utillobj.kill_process('POWERPNT')
        time.sleep(9)
        utillobj.switch_to_main_window()
        time.sleep(2)
        utillobj.switch_to_default_content()
        
        
if __name__ == '__main__':
    unittest.main()

