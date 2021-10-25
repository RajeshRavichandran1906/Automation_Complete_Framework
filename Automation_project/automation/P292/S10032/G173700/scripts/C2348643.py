'''
Created on Dec 07, 2017

@author: Praveen Ramkumar
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348643
Testcase Name :Responsive Autoprompt- All values check box should be checked after running with the filter values
'''
import unittest, time
from common.pages import ia_run,wf_legacymainpage,visualization_resultarea
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase


class C2348643_TestClass(BaseTestCase):

    def test_C2348643(self):
        Restore_fex = "C2348643"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(driver)
        
        """
        Step 01: Logon to WF:
        http://machine:port/{alias}/
        """
#        Fex uploaded in CM package
#         utillobj.invoke_webfocu('mrid', 'mrpass')
        utillobj.invoke_legacyhomepage('mrid', 'mrpass')
        time.sleep(4)
        parent_css="#bipTreePanel tbody tr:nth-child(1)> td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='Workspaces', expire_time=30)
        parent_css = "#topBannerMenuBox [id^='SignonBannerPanelToolsMenuBtn']"
        result_obj.wait_for_property(parent_css, 1, expire_time=40, string_value="Tools", with_regular_exprestion=True)
        time.sleep(15)
        br = utillobj.get_browser_height() # Some time browser height not update correctly in login page method. 
        utillity.UtillityMethods.browser_x = br['browser_width']
        utillity.UtillityMethods.browser_y = br['browser_height']
         
        """
        Step 02: Expand "P292_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)" > S10032_infoassist_5 folder
        Step 03: Right click the "C2348643.fex" > click "Properties" option
        """
        time.sleep(4)
        wf_mainobj.select_repository_folder_item_menu('P292_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)->S10032_infoassist_5', Restore_fex, "Properties")
        utillobj.synchronize_with_number_of_element("#dlgProperties [class*='active']", 1, 20)
#         wf_mainobj.verify_properties_dialog("checkbox", {"Prompt for Parameters":'enable'}, msg='Step 02:Verify properity',tab_name='Main Properties',enable=True)
        time.sleep(1)
        popup_css = "#dlgProperties [class*='active']"
        tab_title_elems = driver.find_elements_by_css_selector(popup_css + " #propTabPane [id*='BiTabBar'] [id*='BiTabButton']") 
        elem_list = [elem.text.strip() for elem in tab_title_elems]
        print('elem_list:', elem_list)
        a=elem_list.index('Main Properties')
        print(a)
        actual_tab = tab_title_elems[[elem.text.strip() for elem in tab_title_elems].index('Main Properties')]
        utillobj.default_click(actual_tab)
        item=driver.find_element_by_css_selector("#chkParams")
        status=item.find_element_by_css_selector("input").is_enabled()
        utillobj.asequal(status,True,"Step 03: Verify that Prompt for parameters options is checked")
         
        """
        Step 04:Click ok in the properties dialog
        """
        wf_mainobj.verify_properties_dialog('button', 'OK', 'Step 3:')
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        Step 05:Run the saved fex from BIP using API link
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=simple_optional.fex
        """
        utillobj.active_run_fex_api_login("C2348643.fex",'S10032_infoassist_5', 'mrid', 'mrpass')
        time.sleep(8)
        """
        Step 06:In Autoprompt window verify that all check box is checked for country values
        Step 07:Click run with filter values in autoprompt window.
        """
        utillobj.synchronize_with_number_of_element("div[class='autop-amper-ctrl-container']", 1,45)
        actual1=self.driver.find_element_by_css_selector("div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='COUNTRY:']").text.strip().replace('\n','')
        expected_paramter1='COUNTRY:All'
        utillobj.asequal(actual1,expected_paramter1,'Step 06.1 : Verify default amper value for Paramater1')
        actual_2=self.driver.find_element_by_css_selector("div[class^='autop-amper'][title='COUNTRY:'] input[type='text']").get_attribute('value').strip()
        expected_paramter2="All Values"
        utillobj.asequal(actual_2,expected_paramter2,'Step 06.2 : Verify default amper value for Paramater1')
        ia_runobj.select_amper_menu('Run')
                
        """
        Step 08:Click the show filter panel icon the autoprompt window.Verify that All check box should be checked.
        """ 
        time.sleep(5)       
        css="#header [class*='autop-btn-show-prompts ui-btn-left ui-btn ui-icon-bars ui-btn-icon-notext ui-corner-all']"
        elem=driver.find_element_by_css_selector(css)
        elem.click()
        time.sleep(5)
        all_checkbox = "[class='autop-chk-foc-null ui-checkbox'] label[class*='ui-checkbox-on']"
        utillobj.verify_object_visible(all_checkbox, True, 'Step 07 : Verify that All check box should be checked.')
        actual1=driver.find_element_by_css_selector("div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='COUNTRY:']").text.strip().replace('\n','')
        print(actual1)
        expected_paramter1='COUNTRY:All'
        utillobj.asequal(actual1,expected_paramter1,'Step 07.1 : Verify default amper value for Paramater1')
        actual_2=driver.find_element_by_css_selector("div[class^='autop-amper'][title='COUNTRY:'] input[type='text']").get_attribute('value').strip()
        expected_paramter2="All Values"
        utillobj.asequal(actual_2,expected_paramter2,'Step 07.2 : Verify default amper value for Paramater1')
        time.sleep(5)
        
        """
        Step 09:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()        