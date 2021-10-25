'''
Created on Nov 2, 2017

@author: BM13368
'''
import unittest, time, pyautogui
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.wftools import wf_mainpage
from common.lib.core_utility import CoreUtillityMethods
import keyboard
from common.wftools.report import Report
from common.wftools.chart import Chart

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
        coreutilobj = CoreUtillityMethods(self.driver)
        reportobj = Report(self.driver)
        chartobj = Chart(self.driver)
           
             
        """
            Step 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=wf_retail_lite
        """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10660_chart_2', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_until_element_is_visible(parent_css, metadataobj.chart_long_timesleep)
               
        """
            Step 02: Double click "Revenue" and "Product, Category"
        """
        metadataobj.datatree_field_click('Revenue', 2, 1)
        query_tree = '#queryTreeWindow'
        utillobj.synchronize_with_visble_text(query_tree, 'Revenue', metadataobj.chart_long_timesleep)
        metadataobj.datatree_field_click('Product,Category', 2, 1)
        utillobj.synchronize_with_visble_text(query_tree, 'Product,Category', metadataobj.chart_long_timesleep)
        """
            Verify the created chart in live preview.
        """
        parent_css=("#TableChart_1 text[class^='xaxis'][class$='title']")
        chartobj.wait_for_number_of_element('#TableChart_1 rect', 9)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 02.01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 02.02: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue", "Step 02.03: Verify second bar color")
        resultobj.verify_number_of_riser('TableChart_1', 1, 7, 'Step 02.04: Verify Number chart segment')
        resultobj.verify_xaxis_title('TableChart_1', 'Product Category', "Step 02.05: Verify X-Axis Title")
        resultobj.verify_yaxis_title('TableChart_1', 'Revenue', "Step 02.06: Verify X-Axis Title")
               
        """
            Step 03: Click Save in the toolbar > Save as "C2336134" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
               
        """
            Step 04: Close tool window
        """
        utillobj.infoassist_api_logout()
        """
            Step 05:Run the saved fex from BIP
            http://domain.com:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%3A%2FWFC%2FRepository%2FS10660BIP_item=C2336134.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10660_chart_2", 'mrid', 'mrpass')
        """
            Step 05:01: Expected to see following chart
        """
        parent_css=("#jschart_HOLD_0 text[class^='xaxis'][class$='title']")
        utillobj.synchronize_with_number_of_element('#jschart_HOLD_0 rect', 9, metadataobj.chart_long_timesleep)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0",expected_xval_list, expected_yval_list, 'Step 05.01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 05.02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue", "Step 05.03: Verify second bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 7, 'Step 05.04: Verify Number chart segment')
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Category', "Step 05.05: Verify X-Axis Title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', 'Revenue', "Step 05.06: Verify X-Axis Title")
        utillobj.infoassist_api_logout()
       
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
        wf_mainpage_obj.select_content_from_sidebar()
        folder = 'P292_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)->S10660_chart_2'  
        wf_mainpage_obj.right_click_folder_item_and_select_menu("C2336134","Edit with text editor", folder)
        coreutilobj.switch_to_new_window()
        chartobj.wait_for_visible_text('div.ace_scroller > div > div.ace_layer.ace_text-layer', 'SET')
        exact_line = utillobj.validate_and_get_webdriver_object('div.ace_scroller > div > div.ace_layer.ace_text-layer > div:nth-child(51) > span:nth-child(2)', 'Keyvalue')
        coreutilobj.python_left_click(exact_line, xoffset=200)
        keyboard.press_and_release('enter')
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
                
        """
            Step 07 : Save and execute the fex
        """
        save_obj=self.driver.find_element_by_css_selector('div[title="Save"]')
        utillobj.click_on_screen(save_obj, coordinate_type='middle', click_type=0)
        time.sleep(0.5)
        coreutilobj.switch_to_default_content()
        reportobj.click_preview_canvas('div[title="Preview"]')
        time.sleep(3)
        
        '''
         Step 07.10 : Expected to see bar size maximum of 50 and labels are arranged as (if label is long, automatically rotated to vertical)
        '''
        coreutilobj.switch_to_new_window(window_maximize=False)
        chartobj.wait_for_number_of_element('#jschart_HOLD_0 rect', 9)
        chart_ = utillobj.validate_and_get_webdriver_object("#jschart_HOLD_0 rect[class*= 'riser!s0!g0!mbar!']", 'chart')
        widthofbar = int(chart_.size['width'])
        status=False
        if widthofbar in range(27,30):
            status=True
        utillobj.asequal(True, status,"Step 07.10: verify the width of chart")
        heightofbar = int(chart_.size['height'])
        status=False
        if heightofbar in range(140,170):
            status=True
        utillobj.asequal(True, status,"Step 07.11: verify the height of chart")

        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 07.12: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 07:13: Verify bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 7, 'Step 07.14: Verify Number chart segment')
        
        '''
        Step 07.20 : Maximize the window to see following
        '''
        driver.maximize_window()
        chartobj.wait_for_number_of_element('#jschart_HOLD_0 rect', 9)
        chart_ = utillobj.validate_and_get_webdriver_object("#jschart_HOLD_0 rect[class*= 'riser!s0!g0!mbar!']", 'chart')
        widthofbar = int(chart_.size['width'])
        status=False
        if widthofbar in range(27,30):
            status=True
        utillobj.asequal(True, status,"Step 07.21 :verify the width of chart")
        heightofbar = int(chart_.size['height'])
        status=False
        if heightofbar in range(275,295):
            status=True
        utillobj.asequal(True, status,"Step 07.22 :verify the height of chart")

        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 07.23: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 07.24: Verify bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 7, 'Step 07.25: Verify Number chart segment')
        coreutilobj.switch_to_previous_window()
    
        """
            Step 08 : Replace added code by following after *END of the of the *GRAPH_SCRIPT section and before ENDSTYLE:
            *GRAPH_JS
            xaxis:{
            groupFit:
            { rule: 'minSize', value: 200}
            },
            *END
        """
        chartobj.wait_for_visible_text('div.ace_scroller > div > div.ace_layer.ace_text-layer', 'SET')
#         parentobj = self.driver.find_element_by_css_selector('div.ace_scroller > div > div.ace_layer.ace_text-layer')
        exact_line = utillobj.validate_and_get_webdriver_object('div:nth-child(55)', 'Keyvalue')
        coreutilobj.python_left_click(exact_line, xoffset=400)
        pyautogui.press('backspace',presses=28,interval=0.2, pause=1)
        text_string = "rule: 'minSize', value: 200}"
        pyautogui.typewrite(text_string, interval=0.2, pause=2)
        
        """
            Step 09 : Save and run the fex
        """
        save_obj=self.driver.find_element_by_css_selector('div[title="Save"]')
        utillobj.click_on_screen(save_obj, coordinate_type='middle', click_type=0)
        time.sleep(0.5)
        reportobj.click_preview_canvas('div[title="Preview"]')
        time.sleep(3)
        
        """
           Step 09.00 : Bar size minimum of 200 (scroll bar added to see full chart)
        """
        coreutilobj.switch_to_new_window(window_maximize=False)
        chartobj.wait_for_number_of_element('#jschart_HOLD_0 rect', 16)
        chart_ = utillobj.validate_and_get_webdriver_object("#jschart_HOLD_0 rect[class*= 'riser!s0!g0!mbar!']", 'chart')
        widthofbar = int(chart_.size['width'])
        status=False
        if widthofbar in range(113,115):
            status=True
        utillobj.asequal(True, status,"Step 09.00 :verify the width of chart")
        heightofbar = int(chart_.size['height'])
        status=False
        if heightofbar in range(165,190):
            status=True
        utillobj.asequal(True, status,"Step 09.01 :verify the height of chart")
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 09.02: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 09.03: Verify bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 7, 'Step 09.04: Verify Number chart segment')
                
        """
           Step 09.10 : Maximize the window
        """
        driver.maximize_window()
        chartobj.wait_for_number_of_element('#jschart_HOLD_0 rect', 9)
        chart_ = utillobj.validate_and_get_webdriver_object("#jschart_HOLD_0 rect[class*= 'riser!s0!g0!mbar!']", 'chart')
        widthofbar = int(chart_.size['width'])
        status=False
        if widthofbar in range(128,130):
            status=True
        utillobj.asequal(True, status,"Step 09.11 :verify the width of chart")
        heightofbar = int(chart_.size['height'])
        status=False
        if heightofbar in range(295,327):
            status=True
        utillobj.asequal(True, status,"Step 09.12 :verify the height of chart")
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 09.13: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 09.14: Verify bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 7, 'Step 09.15: Verify Number chart segment')
        coreutilobj.switch_to_previous_window()
        
        """
           Step 10: Replace added code by following after *END of the of the *GRAPH_SCRIPT section and before ENDSTYLE :
            *GRAPH_JS
            xaxis:{
            groupFit:
            { rule: 'exactSize', value: 100}
            },
            *END
        """
        chartobj.wait_for_visible_text('div.ace_scroller > div > div.ace_layer.ace_text-layer', 'SET')
#         parentobj = self.driver.find_element_by_css_selector('div.ace_scroller > div > div.ace_layer.ace_text-layer')
        exact_line = utillobj.validate_and_get_webdriver_object('div:nth-child(55)', 'Keyvalue')
        coreutilobj.python_left_click(exact_line, xoffset=400)
        pyautogui.press('backspace',presses=28,interval=0.2, pause=1)
        text_string = "rule: 'minSize', value: 100}"
        pyautogui.typewrite(text_string, interval=0.2, pause=2)
                
        """
            Step 11: save and run the fex               
        """
        save_obj=self.driver.find_element_by_css_selector('div[title="Save"]')
        utillobj.click_on_screen(save_obj, coordinate_type='middle', click_type=0)
        time.sleep(0.5)
        reportobj.click_preview_canvas('div[title="Preview"]')
        time.sleep(3)
        
        """
            Step 11.00 : Expected to see bar arranged to size of 100.
        """
        coreutilobj.switch_to_new_window(window_maximize=False)
        chartobj.wait_for_number_of_element('#jschart_HOLD_0 rect', 9)
        chart_ = utillobj.validate_and_get_webdriver_object("#jschart_HOLD_0 rect[class*= 'riser!s0!g0!mbar!']", 'chart')
        widthofbar = int(chart_.size['width'])
        status=False
        if widthofbar in range(55,60):
            status=True
        utillobj.asequal(True, status,"Step 11.00 :verify the width of chart")
        heightofbar = int(chart_.size['height'])
        status=False
        if heightofbar in range(165,200):
            status=True
        utillobj.asequal(True, status,"Step 11.01 :verify the height of chart")
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 11.02: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 11.03: Verify bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 7, 'Step 11.04: Verify Number chart segment')

        """
            Step 11.10 : Maximize the window
        """
        driver.maximize_window()
        chartobj.wait_for_number_of_element('#jschart_HOLD_0 rect', 9)
        chart_ = utillobj.validate_and_get_webdriver_object("#jschart_HOLD_0 rect[class*= 'riser!s0!g0!mbar!']", 'chart')
        widthofbar = int(chart_.size['width'])
        status=False
        if widthofbar in range(120,140):
            status=True
        utillobj.asequal(True, status,"Step 11.11 :verify the width of chart")
        heightofbar = int(chart_.size['height'])
        status=False
        if heightofbar in range(295,327):
            status=True
        utillobj.asequal(True, status,"Step 11.12 :verify the height of chart")
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 11.13: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 11.14: Verify bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 7, 'Step 11.15: Verify Number chart segment')
        coreutilobj.switch_to_previous_window()
        
        """
            Step 12 : Close run window
        """
        coreutilobj.switch_to_previous_window()
               
        """
            Step 13: Logout using API
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        wf_mainpage_obj.signout_from_username_dropdown_menu()
        
if __name__ == "__main__":
    unittest.main()       