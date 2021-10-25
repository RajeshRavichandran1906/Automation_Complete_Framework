'''
Created on Dec 13, 2017

@author: BM13368
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227498
TestCase Name : Verify request with User Selection
'''
import unittest, time, re
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, wf_administration_console, ia_ribbon, ia_run,wf_mainpage
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2227498_TestClass(BaseTestCase):

    def test_C2227498(self):
        
        Test_Case_ID = "C2227498"
        driver = self.driver
        utillobj = utillity.UtillityMethods(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        admin_obj = wf_administration_console.Wf_Administration_Console(driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(driver)
        ia_runobj = ia_run.IA_Run(driver)
        main_page=wf_mainpage.Wf_Mainpage(self.driver)
        
        
        """
            Step 01:Logon to WF:
            http://machine:port/ibi_apps/
            Step 02:Select "Administration" > "Administration Console".
        """
        utillobj.invoke_webfocu('mrid01', 'mrpass01')
        parent_css="#SignonBannerPanelHelpMenuBtn"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(4)
        main_page.select_or_verify_top_banner_links("Administration->Administration Console")
        utillobj.switch_to_window(1)
        
        """
            Step 03:Select "InfoAssist+ Properties" > Check off "User Selection" Show checkbox.
        """
        
        admin_obj.select_admin_console_tree("#console_tree_Configuration_Settings .bi-tree-view-body-content", "InfoAssist+ Properties")
        time.sleep(5)
        admin_obj.input_bihbox("#idInfoassistPropertiesPage", "User Selection", input_control='checkbox')
        time.sleep(8)
        """ 
            Step 04:Scroll down > Click "Save".
            Step 05:Click OK in the save confirmation
        """
        admin_obj.save_cancel_restoredefaultvalues_button("down", 'Save', 4)
        time.sleep(2)
        self.driver.close()
          
        """
            Step 06:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.switch_to_window(0)
        utillobj.infoassist_api_logout()
        """  
            Step 07:Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        """  
            Step 08:Double click "COUNTRY", "CAR", "SALES".
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('SALES', 2, 1)
        time.sleep(4)
        """  
            Step 09:Select "Home" tab > Click "HTML" dropdown > Verify "User Selection" is available.
            Step 10:Click "User Selection" icon.
        """
        list1=['HTML', 'Active Report', 'PDF', 'Excel (xlsx)', 'PowerPoint (pptx)'] 
        ia_ribbonobj.select_or_verify_output_type(launch_point='Home', expected_output_list1=list1, msg1="Step 10:01: Verify output formats.", item_select_path='HTML')
        time.sleep(2)
        ribbonobj.select_ribbon_item("Home", "format_type")
        user_css=driver.find_element_by_css_selector("#HomeFormatTypeMenu #menu_UserOptionOFF_btn").is_displayed()
        utillobj.asequal(user_css, True, "Step 10:02: Verify User Selection Object is visible")
        user_css1=driver.find_element_by_css_selector("#HomeFormatTypeMenu #menu_UserOptionOFF_btn")
        utillobj.click_on_screen(user_css1, "middle", 0)
        time.sleep(2)       
        """  
            Step 11:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe"]')))
        time.sleep(10)
               
        """ 
            Step 12:Verify Auto Prompt is displayed, with output type dropdown menu.
            Step 13:Click on the output type dropdown menu > Verify output types.
            Step 14:Select Output Type = "Active Report".
        """
        html_amper_btn=driver.find_element_by_css_selector("div.autop-pane div[class*='autop-amper-select'] a[id^='ui-id']")
        utillobj.default_left_click(object_locator=html_amper_btn)
        time.sleep(2)
        list_items=driver.find_elements_by_css_selector("div[id='ui-id-1-listbox-popup'] [class*='ui-selectmenu-list ui-listview'] li")
        actual_popup_list=[el.text.strip() for el in list_items  if bool(re.match('\S+', el.text.strip()))]
        print(actual_popup_list)
        list_items[[el.text for el in list_items].index("Active Report")].click()
        time.sleep(2)
        expected_popup_list=['HTML', 'Active Report', 'PDF', 'Excel 2000', 'Excel Formula', 'Excel 2007', 'Excel Formula (xlsx)', 'PowerPoint 2007']
        utillobj.asequal(actual_popup_list, expected_popup_list, "Step 14:01: Verify list of output types")
         
        """  
            Step 15:Click "Run" button.
        """
        ia_runobj.select_amper_menu('Run')
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        time.sleep(4)
        """ 
            Step 16:Verify Active Report output is displayed.
        """
        #ia_runobj.create_table_data_set("table[id='ITableData0']", Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", Test_Case_ID+"_Ds02.xlsx", "Step 16:01: Verify output at runtime using autoprompt")
        """    
            Step 17:Click "IA" > "Save As".
            Step 18:Enter Title = "C2227498".
            Step 19:Click "Save".
        """
        utillobj.switch_to_default_content(pause=1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """  
            Step 20:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        """    
            Step 21:Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227498.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        """  
            Step 22:Select "Home" tab > Click "HTML" dropdown > Verify "User Selection" is selected.
        """
        ribbonobj.select_ribbon_item("Home", "format_type")
        time.sleep(3)
        user_btn=driver.find_element_by_css_selector("#HomeFormatTypeMenu #menu_UserOptionOn_btn")
        status=True if bool(re.match('.*-checked.*', user_btn.get_attribute("class"))) else False
        utillobj.asequal(True, status, "Step 22:01: Verify  button is selected.")
        
        """ 
            Step 23:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        """  
            Step 24:Logon to WF:
            http://machine:port/ibi_apps/
            Step 25:Select "Administration" > "Administration Console".
        """
        utillobj.invoke_webfocu('mrid01', 'mrpass01')
        parent_css="#SignonBannerPanelHelpMenuBtn"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(4)
        main_page.select_or_verify_top_banner_links("Administration->Administration Console")
        utillobj.switch_to_window(1)
        time.sleep(8)
        
        """  
            Step 26:Select "InfoAssist+ Properties" > Uncheck "User Selection" Show checkbox.
        """
        admin_obj.select_admin_console_tree("#console_tree_Configuration_Settings .bi-tree-view-body-content", "InfoAssist+ Properties")
        time.sleep(1)
        admin_obj.input_bihbox("#idInfoassistPropertiesPage", "User Selection", input_control='checkbox')
        time.sleep(3)
        """     
            Step 27:Scroll down > Click "Save" > Click OK
        """
        admin_obj.save_cancel_restoredefaultvalues_button("down", 'Save', 4)
        driver.close()
        """     
            Step 28:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.switch_to_window(0)
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    unittest.main()