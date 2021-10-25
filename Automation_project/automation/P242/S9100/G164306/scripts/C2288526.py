'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288526'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_wizard

class C2288526_TestClass(AS_BaseTestCase):
    def test_C2288526(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_wizard_obj=as_wizard.AS_Wizard_Windows(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, right click on AS Framework->New->HTML/Document
                    Select Document (PDF, Excel...) File Type
                    Click Next, click Finish
                    Close Document2 tab'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                             
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
        
        as_wizard_obj.Html_Document_Wizard("Home","html_document","Document (PDF, Excel...)")  
        time.sleep(15)  
        
        as_utilobj.verify_picture_using_sikuli("step1_C2288526.png","Step 01: Verified that document invoked in default grid settings")
        
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        '''Step 02: Click AS menu->Options
                    Click Document 
                    Grid Settings, change value for Width and Height to 5
                    Click OK'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
          
        as_utilobj.select_element_appstudio_options(list_item="Document",edit_element="15002",write="5")
        time.sleep(2)
        
        as_utilobj.select_element_appstudio_options(edit_element="15004",write="5")
        time.sleep(2)
                    
        as_utilobj.select_any_dialog("OK")
        
        '''Step 03: In Environments Tree, right click on AS Framework->New->HTML/Document
                    Select Document (PDF, Excel...) File Type
                    Click Next, click Finish
                    Close Document2 tab'''
        
        tree_path="S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_wizard_obj.Html_Document_Wizard("Home","html_document","Document (PDF, Excel...)")  
        time.sleep(15)  
        
        as_utilobj.verify_picture_using_sikuli("step3_C2288526.png","Step 03: Verified that document invoked in width and height to '5' grid settings")
        
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        '''Step 04: Click AS menu->Options
                    Click Document
                    Grid Settings, change value for Width and Height to 0
                    Click OK'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
          
        as_utilobj.select_element_appstudio_options(list_item="Document",edit_element="15002",write="0")
        time.sleep(2)
        
        as_utilobj.select_element_appstudio_options(edit_element="15004",write="0")
        time.sleep(2)
                    
        as_utilobj.select_any_dialog("OK")
        
        '''Step 05: In Environments Tree, right click on AS Framework->New->HTML/Document
                    Select Document (PDF, Excel...) File Type
                    Click Next, click Finish
                    Close Document2 tab'''
        
        tree_path="S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_wizard_obj.Html_Document_Wizard("Home","html_document","Document (PDF, Excel...)")  
        time.sleep(15)  
        
        as_utilobj.verify_picture_using_sikuli("step5_C2288526.png","Step 05: Verified that document invoked in width and height to '0' grid settings")
        
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        '''Step 06: Click AS menu->Options
                    Click Document
                    Grid Settings, change value for Width and Height to 50
                    Click OK'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
          
        as_utilobj.select_element_appstudio_options(list_item="Document",edit_element="15002",write="50")
        time.sleep(2)
        
        as_utilobj.select_element_appstudio_options(edit_element="15004",write="50")
        time.sleep(2)
                    
        as_utilobj.select_any_dialog("OK")
        
        '''Step 07: In Environments Tree, right click on AS Framework->New->HTML/Document
                    Select Document (PDF, Excel...) File Type
                    Click Next, click Finish
                    Close Document2 tab'''
        
        tree_path="S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_wizard_obj.Html_Document_Wizard("Home","html_document","Document (PDF, Excel...)")  
        time.sleep(15)  
        
        as_utilobj.verify_picture_using_sikuli("step7_C2288526.png","Step 07: Verified that document invoked in width and height to '0' grid settings")
        
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        '''Step 08: Click AS menu->Options
                    Click "Reset All Options to Default"
                    Click Document
                    Click OK'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
         
        as_utilobj.select_element_appstudio_options(list_item="General",button="Reset All Options to Default")
        time.sleep(2)
        
        as_utilobj.select_element_appstudio_options(button="OK")
        time.sleep(2)
             
if __name__=='__main__' :
    unittest.main()      