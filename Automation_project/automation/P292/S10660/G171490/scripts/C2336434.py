'''
Created on Nov 2, 2017

@author: BM13368
'''
import unittest, time, pyautogui
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, wf_mainpage,wf_legacymainpage
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.wftools import wf_mainpage

class C2336134_TestClass(BaseTestCase):


    def test_C2336134(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2336134'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        wf_mainpage_obj=wf_mainpage.Wf_Mainpage(self.driver)
        wftoolsobj=wf_mainpage.Wf_Mainpage(self.driver)
        
        """
            Step 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=wf_retail_lite
        """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10660_chart_2', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
              
        """
            Step 02: Double click "Revenue" and "Product, Category"
        """
        metadataobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(2)
        metadataobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(3)
        """
            Verify the created chart in live preview.
        """
        time.sleep(5)
        parent_css=("#TableChart_1 text[class^='xaxis'][class$='title']")
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 02:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 02:02: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue", "Step 02:03: Verify second bar color")
        resultobj.verify_number_of_riser('TableChart_1', 1, 7, 'Step 02.04: Verify Number chart segment')
        time.sleep(2)
        resultobj.verify_xaxis_title('TableChart_1', 'Product Category', "Step 02:05: Verify X-Axis Title")
        resultobj.verify_yaxis_title('TableChart_1', 'Revenue', "Step 02:06: Verify X-Axis Title")
        obj1=self.driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step02', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
              
        """
            Step 03: Click Save in the toolbar > Save as "C2336134" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
              
        """
            Step 04: Close tool window
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """
            Step 05:Run the saved fex from BIP
            http://domain.com:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%3A%2FWFC%2FRepository%2FS10660BIP_item=C2336134.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10660_chart_2", 'mrid', 'mrpass')
        """
            Step 05:01: Expected to see following chart
        """
        parent_css=("#jschart_HOLD_0 text[class^='xaxis'][class$='title']")
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0",expected_xval_list, expected_yval_list, 'Step 06:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 06:02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue", "Step 06:03: Verify second bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 7, 'Step 06.04: Verify Number chart segment')
        time.sleep(2)
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Category', "Step 06:05: Verify X-Axis Title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', 'Revenue', "Step 06:06: Verify X-Axis Title")
        first_barobj=self.driver.find_element_by_css_selector("#jschart_HOLD_0 rect[class*='riser!s0!g0!mbar']")
        bar_width_before=first_barobj.get_attribute('width')
        print(bar_width_before)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
            Step 06: Add the following code after *END of the of the *GRAPH_SCRIPT section and before ENDSTYLE:
            *GRAPH_JS
            xaxis:{
            groupFit:
            { rule: 'maxSize', value: 50}
            },
            *END
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        wftoolsobj.right_click_folder_item_and_select_menu("C2336134","Edit with text editor")
        utillobj.switch_to_window(1)
        search_obj=driver.find_element(By.CSS_SELECTOR,"#bipEditor #menu_bar [id='menu_button_search']")
        utillobj.click_on_screen(search_obj, coordinate_type='middle', click_type=0)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//td[contains(text(),'Find')]").click()
        time.sleep(1)
        elem=self.driver.find_element_by_css_selector("#findText")
        utillobj.click_on_screen(elem, coordinate_type='middle', click_type=0)
        text_string = "ENDSTYLE"
        pyautogui.typewrite(text_string, interval=0.2, pause=5)
        find_btn_elem=self.driver.find_element_by_css_selector("#btnFind")
        utillobj.click_on_screen(find_btn_elem, coordinate_type='middle', click_type=0)
        pyautogui.press('backspace',presses=1,interval=0.2, pause=1)
        text_string="*GRAPH_JS"
        pyautogui.typewrite(text_string, interval=0.2, pause=5)
        pyautogui.hotkey('enter')
        text_string="xaxis:{"
        pyautogui.typewrite(text_string, interval=0.2, pause=5)
        pyautogui.hotkey('enter')
        text_string="groupFit:"
        pyautogui.typewrite(text_string, interval=0.2, pause=5)
        pyautogui.hotkey('enter')
        text_string="{ rule: 'maxSize', value: 50}"
        pyautogui.typewrite(text_string, interval=0.2, pause=5)
        pyautogui.hotkey('enter')
        text_string="},"
        pyautogui.typewrite(text_string, interval=0.2, pause=5)
        pyautogui.hotkey('enter')
        text_string="*END"
        pyautogui.typewrite(text_string, interval=0.2, pause=5)
        pyautogui.hotkey('enter')
        text_string="ENDSTYLE"
        pyautogui.typewrite(text_string, interval=0.2, pause=5)
        save_obj=self.driver.find_element_by_css_selector("#toolbar_button_save")
        utillobj.click_on_screen(save_obj, coordinate_type='middle', click_type=0)
        time.sleep(0.5)
        wf_mainpage_obj.click_text_editor_ribbon_button('Run')
        time.sleep(3)
        utillobj.switch_to_window(2)
        
        """
            Step 07 : Save and execute the fex
        """
        parent_css=("#jschart_HOLD_0 text[class^='xaxis'][class$='title']")
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 07:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 07:02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue", "Step 07:03: Verify second bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 7, 'Step 07.04: Verify Number chart segment')
        time.sleep(2)
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Category', "Step 07:05: Verify X-Axis Title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', 'Revenue', "Step 07:06: Verify X-Axis Title")
        first_barobj=self.driver.find_element_by_css_selector("#jschart_HOLD_0 rect[class*='riser!s0!g0!mbar']")
        bar_width_after=first_barobj.get_attribute("width")
        print(bar_width_after)
        verify_bin_width=float(bar_width_after)-float(bar_width_before)
        print(verify_bin_width)
        if verify_bin_width <= 5:
            utillobj.asequal(True, True, 'Step 07:07 : Bar width is expanded to 150')
        else:
            utillobj.asequal(False, True, 'Step 07:08 : Bar width is not expanded to 100')
        obj1=driver.find_element_by_css_selector("#jschart_HOLD_0")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step07', image_type='actual',x=1, y=1, w=-1, h=-1)
        self.driver.close()
        time.sleep(4)
        
        """
            Step 08 : Replace added code by following after *END of the of the *GRAPH_SCRIPT section and before ENDSTYLE:
            *GRAPH_JS
            xaxis:{
            groupFit:
            { rule: 'minSize', value: 200}
            },
            *END
        """
        utillobj.switch_to_window(1)
        elem=self.driver.find_element_by_css_selector("#findReplace #findText")
        elem.clear()
        utillobj.click_on_screen(elem, coordinate_type='middle', click_type=0)
        text_string = "{ rule: 'maxSize', value: 50}"
        pyautogui.typewrite(text_string, interval=0.2, pause=2)
        replace_elem=self.driver.find_element_by_css_selector("#findReplace #replaceText")
        utillobj.click_on_screen(replace_elem, coordinate_type='middle', click_type=0)
        text_string = "{ rule: 'minSize', value: 200}"
        pyautogui.typewrite(text_string, interval=0.2, pause=2)
        replace_btn_obj=self.driver.find_element_by_css_selector("#findReplace #btnReplaceAll")
        utillobj.click_on_screen(replace_btn_obj, coordinate_type='middle', click_type=0)
        
        """
            Step 09 : Save and run the fex
        """
        save_obj=self.driver.find_element_by_css_selector("#toolbar_button_save")
        utillobj.click_on_screen(save_obj, coordinate_type='middle', click_type=0)
        time.sleep(0.5)
        wf_mainpage_obj.click_text_editor_ribbon_button('Run')
        time.sleep(3)
        utillobj.switch_to_window(2)
        """
            Verification : Expect to see the following chart
            Bar size minimum of 200 (scroll bar added to see full chart)
        """
        parent_css=("#jschart_HOLD_0 text[class^='xaxis'][class$='title']")
        resultobj.wait_for_property(parent_css, 1)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 09:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 09:02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue", "Step 09:03: Verify second bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 7, 'Step 09.04: Verify Number chart segment')
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Category', "Step 09:05: Verify X-Axis Title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', 'Revenue', "Step 09:06: Verify X-Axis Title")
        first_barobj=self.driver.find_element_by_css_selector("#jschart_HOLD_0 rect[class*='riser!s0!g0!mbar']")
        bar_width_after1=first_barobj.get_attribute("width")
        print(bar_width_after1)
        verify_bin_width=float(bar_width_after1)-float(bar_width_before)
        print(verify_bin_width)
        if verify_bin_width == 0:
            utillobj.asequal(True, True, 'Step 09:07 : Bar width is expanded to 150')
        else:
            utillobj.asequal(False, True, 'Step 09:08 : Bar width is not expanded to 100')
        obj1=driver.find_element_by_css_selector("#jschart_HOLD_0")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step09', image_type='actual',x=1, y=1, w=-1, h=-1)
        driver.close()
        time.sleep(2)
        """
           Step 10: Replace added code by following after *END of the of the *GRAPH_SCRIPT section and before ENDSTYLE :
            *GRAPH_JS
            xaxis:{
            groupFit:
            { rule: 'exactSize', value: 100}
            },
            *END
        """
        utillobj.switch_to_window(1)
        elem=self.driver.find_element_by_css_selector("#findReplace #findText")
        elem.clear()
        utillobj.click_on_screen(elem, coordinate_type='middle', click_type=0)
        text_string = "{ rule: 'minSize', value: 200}"
        pyautogui.typewrite(text_string, interval=0.2, pause=5)
        replace_elem=self.driver.find_element_by_css_selector("#findReplace #replaceText")
        replace_elem.clear()
        utillobj.click_on_screen(replace_elem, coordinate_type='middle', click_type=0)
        text_string = "{ rule: 'exactSize', value: 100}"
        pyautogui.typewrite(text_string, interval=0.2, pause=2)
        replace_btn_obj=self.driver.find_element_by_css_selector("#findReplace #btnReplaceAll")
        utillobj.click_on_screen(replace_btn_obj, coordinate_type='middle', click_type=0)
        save_obj=self.driver.find_element_by_css_selector("#toolbar_button_save")
        time.sleep(1)
        utillobj.click_on_screen(save_obj, coordinate_type='middle', click_type=0)
        time.sleep(0.5)
        
        """
            Step 11: save and run the fex
                         
        """
        wf_mainpage_obj.click_text_editor_ribbon_button('Run')
        time.sleep(3)
        utillobj.switch_to_window(2)
        """
            Verification : Verify the run time chart bar width
        """
        parent_css=("#jschart_HOLD_0 text[class^='xaxis'][class$='title']")
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 11:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 11:02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue", "Step 11:03: Verify second bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 7, 'Step 11.04: Verify Number chart segment')
        time.sleep(2)
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Category', "Step 11:05: Verify X-Axis Title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', 'Revenue', "Step 11:06: Verify X-Axis Title")
        first_barobj=self.driver.find_element_by_css_selector("#jschart_HOLD_0 rect[class*='riser!s0!g0!mbar']")
        bar_width_after1=first_barobj.get_attribute("width")
        print(bar_width_after1)
        verify_bin_width=float(bar_width_before)-float(bar_width_after1)
        print(verify_bin_width)
        if verify_bin_width >= 5:
            utillobj.asequal(True, True, 'Step 11:07 : Bar width is expanded to 150')
        else:
            utillobj.asequal(False, True, 'Step 11:08 : Bar width is not expanded to 100')
        obj1=driver.find_element_by_css_selector("#jschart_HOLD_0")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        """
            Step 12 : Close run window
        """
        driver.close()
        time.sleep(2)
        """
            Step 13: Logout using API
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
    
        
if __name__ == "__main__":
    unittest.main()       
        