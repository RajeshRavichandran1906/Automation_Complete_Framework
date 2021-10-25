'''
Created on DEC 06, 2017

@author: Pavithra 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2349637
TestCase Name = Whole numbers for Y axis Count - chart-2014
'''
import unittest
import time, pyautogui
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,ia_ribbon,wf_legacymainpage
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

from common.locators.loginpage_locators import LoginPageLocators

class C2349637_TestClass(BaseTestCase):

    def test_C2349637(self):
        
        Test_Case_ID = "C2349637"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        """        
            Step 01:Create new chart with emptdata using API
                    http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=empdata
        """
         
        utillobj.infoassist_api_login('chart','baseapp/empdata','P292/S10660_chart_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        time.sleep(5)
        
        """
            Step 02:Drag PIN to Vertical
        """
        metadataobj.drag_drop_data_tree_items_to_query_tree('PIN',1, 'Vertical Axis',0)
        parent_css="#queryTreeWindow tr:nth-child(7) td"
        resobj.wait_for_property(parent_css, 1, string_value='CNT.PIN', with_regular_exprestion=True,expire_time=50)
        """
            Step 03:Drage DEPT to Horizontal
        """
        metadataobj.datatree_field_click("DEPT", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(9) td"
        resobj.wait_for_property(parent_css, 1, string_value='DEPT', with_regular_exprestion=True,expire_time=50)
         
        """
            Step 04:Drag DIV to Filter
        """
        metadataobj.datatree_field_click("DIV", 1, 1,'Filter')
        parent_css="#dlgWhereValue #id_wv_text_value"
        resobj.wait_for_property(parent_css, 1, expire_time=50)
         
        """
            Step 05:Type CE in Value and click the double arrow to add to filter value > OK > OK
                     
                    Y axis shows floating points (1, 1.5, etc.)
        """
        ia_ribbonobj.create_constant_filter_condition_for_textfield("CE",filter_dialog_close=True)
        resobj.verify_xaxis_title("TableChart_1", 'DEPT', "Step 05.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("TableChart_1", 'CNT PIN', "Step 05.2: Verify X-Axis Title")
        expected_xval_list=['ADMIN SERVICES', 'MARKETING', 'PERSONNEL', 'PROGRAMMING & DVLPMT', 'SALES']
        expected_yval_list=['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 05.3: Verify XY Label')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 05.4: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 5, 'Step 05.5: Verify the total number of risers displayed on preview')
         
         
        """
            Step 06:Save with name C2349637 and close.
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        """
            Step 07:Open C2349637 with text editor.
        """
        
        utillobj.invoke_webfocu('mrid', 'mrpass')
        mainobj.select_repository_folder_item_menu('P292->S10660_chart_2', Test_Case_ID, 'Edit With...->Text Editor')
        parent_css='[id="menu_button_search"]'
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        """
            Step 08:Add syntax before the final *END:
                    *GRAPH_JS_FINAL
                    yaxis: {mode: 'count'}
        """
        search_btn = driver.find_element(By.CSS_SELECTOR,'[id="menu_button_search"]')
        utillobj.default_left_click(object_locator=search_btn)
        utillobj.select_or_verify_bipop_menu('Go To')
        GoToLine = driver.find_element_by_id('txtGoToLine')
        utillobj.default_left_click(object_locator=GoToLine)
        pyautogui.typewrite("48", interval=0.2, pause=5)
        btnGoToLine= driver.find_element_by_id('btnGoToLine')
        utillobj.default_left_click(object_locator=btnGoToLine)
        pyautogui.hotkey('enter')
        pyautogui.typewrite("*GRAPH_JS_FINAL", interval=0.2, pause=5)
        pyautogui.hotkey('enter')
        pyautogui.typewrite("yaxis: {mode: 'count'}", interval=0.2, pause=5)
        pyautogui.hotkey('enter')
        """
            Step 09:Save and close.
        """
        mainobj.click_text_editor_ribbon_button('Save')
        mainobj.click_text_editor_window_caption_button("close")
        time.sleep(3)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        """
            Step 10:Run the fex C2349637 with API call
                    
                    http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10660&BIP_item=C2349637.fex
                    Y Axis shows only integers.
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10660_chart_2", 'mrid', 'mrpass')        
        parent_css="#jschart_HOLD_0 text[class*='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        resobj.verify_xaxis_title("jschart_HOLD_0", 'DEPT', "Step 10.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("jschart_HOLD_0", 'CNT PIN', "Step 10.2: Verify X-Axis Title")
        expected_xval_list=['ADMIN SERVICES', 'MARKETING', 'PERSONNEL', 'PROGRAMMING & DVLPMT', 'SALES']
        expected_yval_list=['0', '1', '2', '3', '4']
        resobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 10.3: Verify XY Label')
        utillobj.verify_chart_color('jschart_HOLD_0', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 10.4: Verify Color')
        resobj.verify_number_of_riser("jschart_HOLD_0", 1, 5, 'Step 10.5: Verify the total number of risers displayed on preview')
        
        """
            Step 11:Close Output window.
        """
        time.sleep(3)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        """
            Step 12:Restore fex C2349637 with API call 
                    http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2349637.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'Chart','S10660_chart_2')
        time.sleep(8)
        loginid = utillobj.parseinitfile('mrid')
        loginpwd = utillobj.parseinitfile('mrpass')
        usename= self.driver.find_element(*LoginPageLocators.uname)
        usename.click()
        time.sleep(2)
        usename.send_keys(loginid)
        time.sleep(1)
        if loginpwd!=None:
            passwd =self.driver.find_element(*LoginPageLocators.pword)
            passwd.send_keys(loginpwd)
            time.sleep(1)
        sign_in =self.driver.find_element(*LoginPageLocators.submit)
        sign_in.click()
        time.sleep(4)
        """
            Step 13:Click OK on message Chart opens in edit mode without error
            
        """
        utillobj.verify_js_alert("File Was Modified Outside of InfoAssist+. Continue?", 'Step 10: Verify Alert')
        time.sleep(3)
        resobj.verify_xaxis_title("TableChart_1", 'DEPT', "Step 13.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("TableChart_1", 'CNT PIN', "Step 13.2: Verify X-Axis Title")
        expected_xval_list=['ADMIN SERVICES', 'MARKETING', 'PERSONNEL', 'PROGRAMMING & DVLPMT', 'SALES']
        expected_yval_list=['0', '1', '2', '3', '4']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 13.3: Verify XY Label')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 13.4: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 5, 'Step 13.5: Verify the total number of risers displayed on preview')
        
if __name__ == '__main__':
    unittest.main()
        