'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226982
TestCase Name = Test that running an Auto Drill report deferred or scheduled does not have the Auto Drill links when opened
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_run, wf_mainpage, rc_misc
from common.locators.rc_advance_locators import RCAdvanceLocators
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2230841_TestClass(BaseTestCase):
    def test_C2230841(self):
        driver = self.driver
        #driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2230841"
        Test_Case_ID = Test_ID + "_" + browser_type
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        rc_miscobj=rc_misc.RC_Misc(self.driver)
        
        
        """    Open IA_Shell for edit using the API 
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """    2. Click IA > Save As > Type C2230841 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    3. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2230841.fex&tool=report    """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
         
        """    4. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(4)
         
        """    5. Click Save button in QAT    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(4)
        
        """    6. Click OK to the message    """
        btn_css="div[id^='BiDialog'] div[class=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('OK')].click()
        time.sleep(15)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    7. Run the saved fex from BIP tree using API.
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%3A%2FWFC%2FRepository%2FS9970&BIP_item=C2230841.fex    """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S9970", 'mrid', 'mrpass')
        time.sleep(25)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=7)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 07a: verify Auto Drill, drill down data set", desired_no_of_rows=7)
        iarun.verify_table_cell_property("table[summary= 'Summary']", 3, 1, text='EMEA', font_color = 'cerulean_blue_2', msg='Step 07b ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 6, 2, text='Media Player', font_color = 'cerulean_blue_2', msg='Step 07c ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 14, 2, text='Computers', font_color = 'cerulean_blue_2', msg='Step 07d ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 21, 1, text='Oceania', font_color = 'cerulean_blue_2', msg='Step 07e ')
        time.sleep(8)
        utillobj.switch_to_default_content(1)
        time.sleep(3)
        
        """    8. Logout    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    9. Enter credentials to login    """
        utillobj.login_wf('mrid','mrpass')
        time.sleep(6)        
        
        """    10. From Resource tree, Right click on C2230841 under S9970 folder and select Run Deferred    """
        project_id=utillobj.parseinitfile('project_id')
        folder = utillobj.parseinitfile('suite_id')
        mainobj.select_repository_menu(project_id + "->" + folder + "->" + Test_Case_ID, "Run Deferred")
        time.sleep(25)
        utillobj.switch_to_window(1)
        time.sleep(5)
        driver.maximize_window()
        time.sleep(5)
        actual_val=driver.find_element_by_css_selector("#deferMsg > span > #new_description").get_attribute("value")
        utillobj.asequal(Test_Case_ID, actual_val, "Step 10a: Verify the text in the Description box should be C2230841")
        
        """    11. Click OK to submit    """
        driver.find_element_by_css_selector("#deferMsg > div > #okButton").click()
        time.sleep(5)
        #defer_notification=driver.find_element_by_css_selector("deferTitle").text.strip()
        #utillobj.asequal("Deferred Report Notification", defer_notification, "Step 11a: Verify Deferred Report Notification displayed")
        rc_miscobj.verify_defered_report_notification(Test_Case_ID)
        
        """    12. Click on Deferred Report Status link    """
        rc_miscobj.click_defered_report_notification_link()
        #driver.find_element_by_css_selector("#deferMsg > a[href]").click()
        time.sleep(15)
        owebpage=driver.title
        utillobj.asequal("Deferred Report Status", owebpage, "Step 12a: Verify ' Deferred Report Status ' page displayed")
        
        """    13. Find the report C2230841 from the list and click on View     """
        """    Note: Wait 1 minute for the job to complete.    """
        for i in range(10):
            time.sleep(10)
            if i > 7:
                oRefresh=driver.find_element_by_css_selector("td>a[href]>img[src*='images'][title='Refresh']")
                utillobj.default_left_click(object_locator=oRefresh)
        time.sleep(5)
        cust_windows=driver.window_handles
        rc_miscobj.click_defered_report_button(Test_Case_ID, "View")
        #oView=driver.find_element_by_css_selector("td>a[href]>img[title='View']")
        #utillobj.default_left_click(object_locator=oView)
        time.sleep(5)
        utillobj.switch_to_window(3, custom_windows=cust_windows)
        time.sleep(5)
        driver.maximize_window()
        time.sleep(5)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 13a: verify Auto Drill, drill down data set", desired_no_of_rows=7)
        iarun.verify_table_cell_property("table[summary= 'Summary']", 3, 1, text='EMEA', font_color = 'gray8', msg='Step 13b ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 6, 2, text='Media Player', font_color = 'gray8', msg='Step 13c ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 14, 2, text='Computers', font_color = 'gray8', msg='Step 13d ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 21, 1, text='Oceania', font_color = 'gray8', msg='Step 13e ')
        
        """    14. Close the opened report    """
        driver.close()
        time.sleep(5)
        utillobj.switch_to_window(1)
        time.sleep(5)
        
        """    15. Click on Delete under options from the Deferred Report Status list.    """
        """    16. Click Ok the message     """
        rc_miscobj.click_defered_report_button(Test_Case_ID, "Delete")
        
        """    17. Close the Deferred Report Status.    """
        driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(5)
        
        """    18. From Resource tree, Right click on C2230841 under S9970 folder > Schedule > Report Library    """
        mainobj.select_repository_menu(project_id + "->" + folder + "->" + Test_Case_ID, "Schedule->Report Library")
        time.sleep(15)
        try:
            driver.find_element_by_css_selector("div[id='BasicScheduleEditor_btnShowDistribution'][class*='button-checked']").is_displayed()       
            utillobj.asequal(True, True, "Step 18a: Verify Schedule basic opens in distribution tab")
        except:
            utillobj.asequal(True, False, "Step 18a: Verify Schedule basic opens in distribution tab")
        
        """    19. Click on Task tab > Execution ID > Enter "srvadmin" (Remove those if any already is there)    """
        """    20. Click password button > Enter "srvadmin" in both password and confirm password text boxes > OK    """
        oTask=driver.find_element_by_css_selector("#BasicScheduleEditor_btnShowTask img")
        utillobj.default_left_click(object_locator=oTask)
        time.sleep(5)
        user_id=driver.find_element_by_css_selector("#TaskStandardReportPane_execidListComboBox input")
        passwd_btn=driver.find_element_by_css_selector("#TaskStandardReportPane_execpassButton")
        rc_miscobj.set_task_password(user_id, "srvadmin", passwd_btn, "srvadmin")
        time.sleep(5)
        
        """    21. Click on Properties tab > Enter "C2230841a" in title text box.    """
        oProperties=driver.find_element_by_css_selector("#BasicScheduleEditor_btnShowGeneral img")
        utillobj.default_left_click(object_locator=oProperties)
        time.sleep(5)
        oInput=driver.find_element_by_css_selector("#BasicScheduleEditor_nameTextField")
        utillobj.set_text_field_using_actionchains(oInput, Test_Case_ID + "_a")
        
        """    22. Click on RC > Save button and click Save in Save As prompt with default title C2230841a.    """
        rc_btn=self.driver.find_element(*RCAdvanceLocators.rc_menu_btn)
        utillobj.default_left_click(self, object_locator=rc_btn)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("Save")
        time.sleep(10)
        driver.find_element_by_id("IbfsOpenFileDialog7_btnOK").click()
        time.sleep(5)
        
        """    23. Click Run Button on the top.    """
        oRun=driver.find_element_by_css_selector("#BasicScheduleEditor_btnRun img")
        utillobj.default_left_click(object_locator=oRun)
        time.sleep(3)
        
        """    24. Click OK to the warning message    """
        cap_text='Warning'
        cap_css="div[id^='BiDialog']>div[class*='window-active'] [class*='caption'] [class*='bi-label']"
        utillobj.verify_popup("div[id^='BiDialog']>div[class$='window-active']", "Step 24a: Verify the warning message displayed", caption_css=cap_css, caption_text=cap_text)
        btn_css="div[id^='BiDialog']>div[class$='window-active'] div[class=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('OK')].click()
        time.sleep(3)
        
        """    25. Click OK to the warning message    """
        cap_css="div[id^='BiDialog']>div[class*='window-active'] [class*='caption'] [class*='bi-label']"
        cap_text='Warning'
        popup_css="div[id^='BiDialog']>div[class$='window-active'] [class='bi-component'] [class*='bi-label']"
        pop_text="The schedule has been submitted for execution and the job ID"
        utillobj.verify_popup("div[id^='BiDialog']>div[class*='window-active']", "Step 25a: Verify the warning message displayed", caption_css=cap_css, caption_text=cap_text, popup_text_css=popup_css, popup_text=pop_text)
        btn_css="div[id^='BiDialog']>div[class$='window-active'] div[class=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('OK')].click()
               
        """    26. Click on Log Reports tab and find the Job number is created in step#24.    """
        oLogRpt=driver.find_element_by_css_selector("#BasicScheduleEditor_btnShowHistory img")
        utillobj.default_left_click(object_locator=oLogRpt)
        time.sleep(3)
        
        """    27. Click on Refresh Button in the bottom until the Report status gets displayed.    """
        for i in range(10):
            oStatus=driver.find_element_by_css_selector("#BasicScheduleEditor_logGrid2 > div[class$='content'] > table > tbody > tr:nth-child(1) > td:nth-child(4)").text.strip()
            if oStatus != 'Sucess':
                driver.find_element_by_css_selector("#BasicScheduleEditor_btnRefreshHistory>div").click()
                time.sleep(5)
            else:
                break
        
        """    28. Click on Save&close.    """
        oSaveExit=driver.find_element_by_css_selector("#BasicScheduleEditor_btnSaveClose img")
        utillobj.default_left_click(object_locator=oSaveExit)
        time.sleep(5)
        
        """    29. From Resource tree, Double click on C2230841a library report under S9970 folder    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.login_wf('mrid','mrpass')
        time.sleep(6)
        mainobj.expand_repository_tree(project_id + "->" + folder + "->" + Test_Case_ID)
        oLibraryReport=driver.find_element_by_css_selector("#bipTreePanel #treeView table>tbody>tr>td>img[class='icon'][src*='bid/library']")
        utillobj.click_on_screen(oLibraryReport, coordinate_type='middle', click_type=2,mouse_duration=2.5)
        #utillobj.default_left_click(object_locator=oLibraryReport)
        time.sleep(15)
        utillobj.switch_to_window(1)
        time.sleep(5)
        driver.maximize_window()
        time.sleep(5)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 29a: verify Auto Drill, drill down data set", desired_no_of_rows=7)
        iarun.verify_table_cell_property("table[summary= 'Summary']", 3, 1, text='EMEA', font_color = 'gray8', msg='Step 29b ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 6, 2, text='Media Player', font_color = 'gray8', msg='Step 29c ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 14, 2, text='Computers', font_color = 'gray8', msg='Step 29d ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 21, 1, text='Oceania', font_color = 'gray8', msg='Step 29e ')
        
        """    30. Close the output    """ 
        driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(5)
        
        """    31. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
