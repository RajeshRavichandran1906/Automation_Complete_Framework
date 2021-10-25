'''@author: Adithyaa

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6670633'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators

class C6670633_TestClass(AS_BaseTestCase):
    def test_C6670633(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Test case Properties'''
        
        environments_detail_pane_item="318"
        context_bar_pane="221"
        status_bar_pane="59393"
        help_wizard_pane="2054"
        
        '''Test-case verifications'''
        
        verify_dialogs=["Select Server Node","Open File","Report Wizard","Chart Wizard","HTML / Document Wizard"]
        verify_image_1="step1_C6670633.png"
        verify_image_3="step11_C6670633.png"
        verify_msg_1_2_3="Step 01 & 02: Verify there are four sections: a) Data & Metdata, b) Content, c) Configure and d) View available in the ribbon. Options in content sections are: Report, Chart and HTML/Document"
        verify_msg_4="Step 04: Verify 'Select Server Node' opens with choices of environments and their data servers"
        verify_msg_5="Step 05: Verify 'Select Server Node' opens with choices of environments and their data servers."
        verify_msg_6="Step 06: Verify Open file dialogue opens"
        verify_msg_7="Step 06: Verify 'Select Server Node' opens with choices of environments and their data servers."
        verify_msg_8="Step 08: Verify first page of Report wizard opens. Recent reports show on the left. There are three options to choose from: Create Report, Create SQL Report & Open Existing"
        verify_msg_9="Step 09: Verify Chart wizard opens. Recent charts display on the left and there are three options to: Create Chart, Create SQL Chart & Open Existing"
        verify_msg_10="Step 10: Verify HTML / Document wizard Opens"
        verify_msg_11="Step 11: Verify View section"
        verify_msg_12="Step 12: Verify Environments Details is now enabled"
        verify_msg_13="Step 13: Verify Context Bar is now enabled"
        verify_msg_14="Step 14: Verify Status Bar is now enabled"
        verify_msg_15="Step 15: Verify Help Wizard is now enabled"

        '''Test-Script'''
          
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 01,02 & 03: Review Home Ribbon, Review Data & Metadata section.Review content section'''
         
        as_utilobj.verify_picture_using_sikuli(verify_image_1,verify_msg_1_2_3)
        time.sleep(1)
         
        '''Step 04: Click 'Create' options under Data & Metadata .
                    Click Cancel on the Select Server Node dialog.'''
         
        as_utilobj.select_home_button()
        time.sleep(1)
         
        as_utilobj.click_element_using_ui(button_item=True,name=locators.create_button)
        time.sleep(1)
         
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialogs[0],verify_msg_4)
        time.sleep(1)
         
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(1)
         
        '''Step 05: Select 'Design' option under Data & Metadata.
                    Click Cancel on the Select Server Node dialog.'''
         
        as_utilobj.click_element_using_ui(button_item=True,name=locators.design_button)
        time.sleep(1)
         
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialogs[0],verify_msg_5)
        time.sleep(1)
         
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(1)
        
        '''Step 06: Select 'Open' under Data & Metadata.
                    Click Cancel on the Open File dialog.'''
         
        as_utilobj.click_element_using_ui(button_item=True,name=locators.ribbon_open_button)
        time.sleep(1)
         
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialogs[1],verify_msg_6)
        time.sleep(1)
         
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(1)
         
        '''Step 07: Select 'Upload Data' option under Data & Metadata.
                    Click Cancel on the Select Server Node dialog.'''
         
        as_utilobj.click_element_using_ui(button_item=True,name=locators.upload_data_button)
        time.sleep(1)
         
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialogs[0],verify_msg_7)
        time.sleep(1)
         
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(1)
        
        '''Step 08: Click Report icon in Home ribbon.
                    Click Cancel on Report wizard'''
         
        as_utilobj.logout_conf_env(envpath=True)
        time.sleep(4)
                                
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"envpath")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                       
        tree_path="Domains->P292_S10032_G156803"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.click_element_using_ui(button_item=True,name=locators.report_button) 
        time.sleep(1)
         
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialogs[2],verify_msg_8)
        time.sleep(1)
         
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(1)
         
        '''Step 09: Click Chart icon in Home ribbon.
                    Click Cancel on Chart wizard'''
         
        as_utilobj.click_element_using_ui(button_item=True,name=locators.chart_button) 
        time.sleep(1)
         
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialogs[3],verify_msg_9)
        time.sleep(1)
         
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(1)
         
        '''Step 10: Click HTML/Document icon in Home ribbon.
                    Click Cancel on HTML wizard'''
         
        as_utilobj.click_element_using_ui(button_item=True,name=locators.htmldocument_button) 
        time.sleep(1)
         
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialogs[4],verify_msg_10)
        time.sleep(1)
         
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(1)
         
        '''Step 11: Review View section.'''
         
        as_utilobj.select_home_button()
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_image_3,verify_msg_11)
        time.sleep(3)
        
        '''Step 12: Select each Unchecked Options in the View section.
                    Check&Uncheck Environments Detail'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.environmentsdetail_button)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_12,pane_item=environments_detail_pane_item)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.environmentsdetail_button)
        time.sleep(1)
        
        '''Step 13: UnCheck Environments Detail
                    Check Context Bar'''
    
        as_utilobj.click_element_using_ui(button_item=True,name=locators.contextbar_button)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_13,pane_item=context_bar_pane)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.contextbar_button)
        time.sleep(1)
        
        '''Step 14: UnCheck Context Bar
                    Expand Framework folder
                    Right click on 161337 and select Open
                    Click Home Tab
                    Check Status Bar'''
    
        as_utilobj.click_element_using_ui(button_item=True,name=locators.statusbar_button)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_14,pane_item=status_bar_pane)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.statusbar_button)
        time.sleep(1)
        
        '''Step 15: Uncheck Status bar
                    Close 161337 tab
                    Check Help Wizard
                    Uncheck Help Wizard'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.helpwizard_button)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_15,pane_item=help_wizard_pane)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.helpwizard_button)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()   