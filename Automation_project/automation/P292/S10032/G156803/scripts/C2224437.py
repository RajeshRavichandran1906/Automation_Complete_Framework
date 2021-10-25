'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2224437'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators
from common.pages import as_ribbon

class C2224437_TestClass(AS_BaseTestCase):
    def test_C2224437(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        as_ribbon_obj=as_ribbon.AS_Ribbon(driver)
        
        '''Test-case property variables'''
        
        key_pattern_1=['down']
        key_pattern_2=['down','down']
        key_pattern_3=['down','down','down']
        wait_time=[0,1,2,3,4,5,6,7,8]
        
        '''Test-case verifications'''
        
        verify_dialogs=["Data Source Definition Wizard","Select Server Node","Report Wizard","Chart Wizard","HTML / Document Wizard"]
        verify_image_1="step1_C2224437.png"
        verify_image_2="step2_C2224437.png"
        verify_image_3="step11_C2224437.png"
        verify_msg_1_2="Step 01 & 02: Verify there are four sections: a) Content, b) Utilities, c) View and d) Windows. Available options in content sections are: Data, Report, Chart and HTML/Document"
        verify_msg_3="Step 03: Verify Options under Data are: a) Synonym via Metadata Canvas, b) Synonym, c) Manage Adapters, d) Data Source Password , e) Rebuild Data Source"
        verify_msg_4="Step 04: Verify Data Source Definition Wizard opens"
        verify_msg_5="Step 05: Verify Data Source Definition window closes"
        verify_msg_6="Step 06: Verify Select Server Node dialog opens."
        verify_msg_7="Step 06: Verify 'Select Server Node' opens with choices of environments and their data servers."
        verify_msg_8="Step 08: Verify first page of Report wizard opens. Recent reports show on the left. There are three options to choose from: Create Report, Create SQL Report & Open Existing"
        verify_msg_9="Step 09: Verify Chart wizard opens. Recent charts display on the left and there are three options to: Create Chart, Create SQL Chart & Open Existing"
        verify_msg_10="Step 10: Verify HTML / Document wizard Opens"
        verify_msg_11="Step 11: Verify Help Wizard will be unckecked if unchecked at start of App Studio"
        verify_msg_12="Step 12: Verify Environments Details is now checked"
        verify_msg_13="Step 13: Verify Context Bar is now checked"
        verify_msg_14="Step 14: Verify Status Bar is now checked"
        verify_msg_15="Step 15: Verify Help Wizard is now checked"

        '''Test-Script'''
          
        as_utilobj.select_home_button()
        time.sleep(wait_time[0])
        
        '''Step 01&02: Review Home Ribbon & Review Content section.'''
        
        as_utilobj.verify_picture_using_sikuli(verify_image_1,verify_msg_1_2)
        time.sleep(wait_time[1])
        
        '''Step 03: Click Data icon.'''
        
        as_utilobj.click_element_using_ui(split_button_with_offset=locators.data_splitbutton,x=0.35,y=0.85)
        time.sleep(wait_time[1])
        
        as_utilobj.verify_picture_using_sikuli(verify_image_2,verify_msg_3)
        time.sleep(wait_time[1])
        
        '''Step 04: 'Select Synonym via Metadata Canvas' options under Data'''
        
        as_utilobj.select_home_button()
        time.sleep(wait_time[0])
        
        as_utilobj.click_element_using_ui(split_button_with_offset=locators.data_splitbutton,send_keys=key_pattern_1,x=0.35,y=0.85)
        time.sleep(wait_time[0])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialogs[0],verify_msg_4)
        time.sleep(wait_time[0])
        
        '''Step 05: Click Cancel on the Metadata wizard.'''
        
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(wait_time[0])
        
        as_utilobj.Verify_Current_Dialog_Closes(verify_dialogs[0],verify_msg_5)
        time.sleep(wait_time[1])
        
        '''Step 06: Select 'Synonym' option under Data.
                    Click Cancel on the Select Server Node dialog.'''
        
        as_utilobj.click_element_using_ui(split_button_with_offset=locators.data_splitbutton,send_keys=key_pattern_2,x=0.35,y=0.85)
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialogs[1],verify_msg_6)
        time.sleep(wait_time[1])

        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(wait_time[0])
        
        '''Step 07: Select 'Manage Adapters' under Data.
                    Click Cancel on the Select Server Node dialog.'''
        
        as_utilobj.click_element_using_ui(split_button_with_offset=locators.data_splitbutton,send_keys=key_pattern_3,x=0.35,y=0.85)
        time.sleep(wait_time[0])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialogs[1],verify_msg_7)
        time.sleep(wait_time[0])
        
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(wait_time[0])
        
        '''Step 08: Click Report icon in Home ribbon.
                    Click Cancel on Report wizard'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.report_button) 
        time.sleep(wait_time[0])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialogs[2],verify_msg_8)
        time.sleep(wait_time[0])
        
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(wait_time[0])
        
        '''Step 09: Click Chart icon in Home ribbon.
                    Click Cancel on Chart wizard'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.chart_button) 
        time.sleep(wait_time[0])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialogs[3],verify_msg_9)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(wait_time[0])
        
        '''Step 10: Click HTML/Document icon in Home ribbon.
                    Click Cancel on HTML wizard'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.htmldocument_button) 
        time.sleep(wait_time[0])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialogs[4],verify_msg_10)
        time.sleep(wait_time[0])
        
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(wait_time[0])
        
        '''Step 11: Review View section.'''
        
        as_utilobj.select_home_button()
        time.sleep(wait_time[0])
        
        as_utilobj.verify_picture_using_sikuli(verify_image_3,verify_msg_11)
        time.sleep(wait_time[3])
        
        '''Step 12: Select each Unchecked Options in the View section.
                    Check&Uncheck Environments Detail'''
        
        as_ribbon_obj.verify_click_checkbox(msg=None,click=locators.environmentsdetail_checkbox)
        time.sleep(wait_time[0])
        
        as_utilobj.verify_element_using_ui(verify_msg_12,check_box=locators.environmentsdetail_checkbox)
        time.sleep(wait_time[0])
        
        '''Step 13: UnCheck Environments Detail
                    Check Context Bar'''
        
        as_ribbon_obj.verify_click_checkbox(msg=None,uncheck=locators.environmentsdetail_checkbox)
        time.sleep(wait_time[0])

        as_ribbon_obj.verify_click_checkbox(msg=None,click=locators.contextbar_checkbox)
        time.sleep(wait_time[0])
        
        as_utilobj.verify_element_using_ui(verify_msg_13,check_box=locators.contextbar_checkbox)
        time.sleep(wait_time[0])
        
        as_ribbon_obj.verify_click_checkbox(msg=None,uncheck=locators.contextbar_checkbox)
        time.sleep(wait_time[0])
        
        '''Step 14: Check Status Bar
                    Uncheck Status bar'''
        
        as_ribbon_obj.verify_click_checkbox(msg=None,click=locators.statusbar_checkbox)
        time.sleep(wait_time[0])
        
        as_utilobj.verify_element_using_ui(verify_msg_14,check_box=locators.statusbar_checkbox)
        time.sleep(wait_time[0])
        
        as_ribbon_obj.verify_click_checkbox(msg=None,uncheck=locators.statusbar_checkbox)
        time.sleep(wait_time[0])
        
        '''Step 15: Check Help Wizard
                    Uncheck Help Wizard'''
        
        as_ribbon_obj.verify_click_checkbox(msg=None,click=locators.helpwizard_checkbox)
        time.sleep(wait_time[0])
        
        as_utilobj.verify_element_using_ui(verify_msg_15,check_box=locators.helpwizard_checkbox)
        time.sleep(wait_time[0])
        
        as_ribbon_obj.verify_click_checkbox(msg=None,uncheck=locators.helpwizard_checkbox)
        time.sleep(wait_time[0])
        
if __name__=='__main__' :
    unittest.main()   