'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2303731'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.pages import as_ribbon
import pyautogui as keys
from common.lib import as_utility
import uiautomation as automation

class C2303731_TestClass(AS_BaseTestCase):
    def test_C2303731(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_ribbon_obj= as_ribbon.AS_Ribbon(driver) 
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Login into WebFocus Environment'''
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
            
        '''Step 01: Launch App Studio, click down arrow for Data'''
               
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Data','Synonym via Metadata Canvas',"Step 01a: Verified Synonym via Metadata Canvas - create or open existing data source definitions exist",15,60,5,20)
        time.sleep(1)
                 
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Data','Import Synonym',"Step 01b: Verified Import Synonym - Import a data source definitions exist",15,60,5,40)
        time.sleep(1)
                 
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Data','Manage Adapters',"Step 01c: Verified Manage Adapters - Add new or manage existing adapter connections exist",15,60,5,70)
        time.sleep(1)
                 
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Data','DBA Password',"Step 01d: Verified DBA Password - Specify the DBA and user password for the data sources exist",15,60,5,85)
        time.sleep(1)
                 
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Data','Rebuild FOCUS Data Source',"Step 01e: Verified Rebuild FOCUS Data Source - Restructure a data source, rebuild indexes, or check the integrity of data sources exist",15,60,5,105)
        time.sleep(1)
               
        '''Step 02: Click on drop down arrow next to WebFOCUS Administration'''
               
        '''WebFOCUS Administration Console'''
              
        as_ribbon_obj.Verify_Dropdown_Tooltip('WebFOCUS Administration','WebFOCUS Administration Console',"Step 02a: Verified WebFOCUS Administration Console - Administration of webFOCUS Environment exist",5,20)
        time.sleep(1)
               
        '''Reporting Server Console'''
        as_ribbon_obj.Verify_Dropdown_Tooltip('WebFOCUS Administration','Reporting Server Console', "Step 02b: Verified Reporting Server Console - Administration of Reporting Server exist",5,40)
        time.sleep(1)
                
        '''Security Center'''
        as_ribbon_obj.Verify_Dropdown_Tooltip('WebFOCUS Administration','WebFOCUS Security Center',"Step 02c: Verified WebFOCUS Security Center - Administration of WebFOCUS Security Center settings exist",5,60)
        time.sleep(1)
                           
        '''BI Portal'''
        as_ribbon_obj.Verify_Dropdown_Tooltip('WebFOCUS Administration','WebFOCUS BI Portal',"Step 02d: Verified WebFOCUS BI Portal - Launch the WebFOCUS BI Portal exist",5,85)
        time.sleep(1)
                 
        '''Deferred Status'''
        as_ribbon_obj.Verify_Dropdown_Tooltip('WebFOCUS Administration','WebFOCUS Deferred Status',"Step 02e: Verified WebFOCUS Deferred Status - Administration of webFOCUS Deferred status exist",5,105)
        time.sleep(1)
               
        '''ReportCaster Console'''
        as_ribbon_obj.Verify_Dropdown_Tooltip('WebFOCUS Administration','WebFOCUS ReportCaster Console',"Step 02f: Verified WebFOCUS ReportCaster Console - Launch the WebFOCUS ReportCaster Console exist",5,125)
        time.sleep(1)
              
        '''Step 03: New Window is disabled'''
            
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
            
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
            
        automation.SendKey(automation.Keys.VK_W, waitTime=3)
        time.sleep(2)
              
        as_utilobj.verify_picture_using_sikuli("step2_C2303731.png","Step 03: Verify New window option is disabled")
        time.sleep(2)
              
        '''Step 04: Click on drop down arrow next to Style'''
             
        automation.SplitButtonControl(Name="Style").Click()
        time.sleep(1)
             
        as_utilobj.verify_picture_using_sikuli("step4_C2303731.png","Step 04: Verify Style dropdown displays Blue,Black,Silver,Aqua style themes")
        time.sleep(2) 
      
        '''Step 05: Click on drop down arrow next to '''
               
        '''Help Topics'''
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Help Topics','Help Topics',"Step 05a: Verified Help Topics - List Help Topics exist",27,10,5,20)
                   
        '''Focal Point Forums'''
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Help Topics','Focal Point Forums',"Step 05b: Verified is Focal Point Forums - Launch the IBI Focal Point Website exist",27,10,5,40)
                 
        '''Display Welcome Screen'''
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Help Topics','Display Welcome Screen',"Step 05c: Verified Display Welcome Screen -Display Welcome Screen exist",27,10,5,70)
                             
        '''Reset Layout'''
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Help Topics','Reset Layout',"Step 05d: Verified Reset Layout - Reset ribbon, style and panels to installed settings exist",27,10,5,90)
                   
        '''About'''
        as_ribbon_obj.Verify_Dropdown_Tooltip_Splitbox('Help Topics','About',"Step 05e: Verified Tooltip is About - Display program information, version number and copyright exist",27,10,5,115)
        time.sleep(4)
             
#         '''Step 06: In Environments Tree, set filter to show Procedure files
#                     In Domains, navigate to CC - Appstudio->AS Files, double click on 160526009
#                     Click on Home tab, click the drop down arrow under Windows'''
#             
#         as_utilobj.logout_conf_env(webfocus_environment=True)
#         time.sleep(4)
#                                                 
#         tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(3)
#                     
#         tree_path="Domains->S9100->160526009"
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(8) 
#             
#         as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
#         time.sleep(2)
#               
#         automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
#         time.sleep(2)
#              
#         automation.SendKey(automation.Keys.VK_H, waitTime=3)
#         time.sleep(2)
#              
#         automation.SendKey(automation.Keys.VK_W, waitTime=3)
#         time.sleep(2)
#                
#         as_utilobj.verify_picture_using_sikuli("step6_C2303731.png","Step 06: Verify New Window is enabled and the open report is listed.")
#         time.sleep(2)
#       
#         '''Step 07: in Domains, CC-Appstudio->AS Files, double click on ChartParm
#                     Click on Home tab, click the drop down arrow under Windows'''
#              
#         as_utilobj.click_element_using_ui(tree_item="ChartParm")
#         time.sleep(12)
#                    
#         as_utilobj.double_click_element(driver.find_element_by_name('Home'))
#         time.sleep(1)
#              
#         automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
#         time.sleep(2)
#             
#         automation.SendKey(automation.Keys.VK_H, waitTime=3)
#         time.sleep(2)
#             
#         automation.SendKey(automation.Keys.VK_W, waitTime=3)
#         time.sleep(2)
#              
#         as_utilobj.verify_picture_using_sikuli("step7_C2303731.png","Step 07: Verify 2 open files are listed in the drop down in the order they were opened, the most recent one on top and in focus.")
#         time.sleep(2) 
#              
#         keys.hotkey('esc')
#         time.sleep(1)
#          
#         '''Step 08 & 09: Click on 16052609
#                          Click the drop down arrow under Windows
#                          Close 16052609
#                          Click on Home tab, click the drop down arrow under Windows'''
#      
#              
#         as_utilobj.close_canvas_item()
#         time.sleep(8)
#              
#         as_utilobj.close_canvas_item()
#         time.sleep(8)
#           
#         tree_path="ChartParm"
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(20) 
#            
#         as_utilobj.double_click_element(driver.find_element_by_name('Home'))
#         time.sleep(1)
#            
#         automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
#         time.sleep(2)
#            
#         automation.SendKey(automation.Keys.VK_H, waitTime=3)
#         time.sleep(2)
#            
#         automation.SendKey(automation.Keys.VK_W, waitTime=3)
#         time.sleep(2)
#            
#         as_utilobj.verify_picture_using_sikuli("step9_C2303731.png","Step 09: Verify closed file has been removed from list of windows. (only one remains).")
#         time.sleep(2) 
#            
#         keys.hotkey('esc')
#         time.sleep(1)
#           
#         '''Step 10: Click the drop down arrow for Windows on the Home ribbon and select the last option 'Windows'.
#                     Click Windows'''
#          
#         automation.SplitButtonControl(Name="Windows").Click(ratioX =0.5,ratioY =0.85,waitTime=2)
#         time.sleep(1)
#          
#         as_utilobj.Verify_Current_Dialog_Opens("Windows","Step 10: Windows dialog opens showing open with function buttons. The current file in focus is highlighted in the dialog.")
#         time.sleep(1)
#          
#         '''Step 11: Close the "Windows" window
#                     Close ChartParm'''
#          
#         as_utilobj.select_any_dialog("Close Window(s)")
#         time.sleep(4)
#          
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(2)

if __name__=='__main__' :
    unittest.main()  