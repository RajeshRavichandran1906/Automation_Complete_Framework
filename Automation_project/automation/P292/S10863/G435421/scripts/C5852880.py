'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10863&group_by=cases:section_id&group_order=asc&group_id=435421
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5852880'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods

import time,unittest
import keyboard as keys

class C5852880_TestClass(AS_BaseTestCase):
    
    def test_C5852880(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        #hcanvas_web=html_canvas.Html_Canvas(self.se_driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains->P292_S10032_G157549->API"
        item="IbComposer setCurrentSelectionAS"
        run_item="IbComposer_setCurrentSelectionAS.htm"
        as_utilobj.select_home_button()
        browser = UtillityMethods.parseinitfile(self,'browser')
        
        '''Step 1. Navigate to Domains P292_S10032_G157549'''
        '''Step 1.1. Expand API folder'''
        
        hcanvas.open_html_canvas_document(tree_path, item)
        
        dialog_control=automation.WindowControl(ClassName="#32770")
        automation.WaitForExist(dialog_control, 30)
        dialog_control.ButtonControl(Name="Yes").Click()
        
        button_control=automation.PaneControl(Name="Set Current Selection API Test Page").ButtonControl(Name="Test Combo Box")
 
        hcanvas.wait_for_object_exist(button_control, 30)
         
        '''Step 1.2. Right click on IbComposer_setCurrentSelectionAS and click Open.'''
        
        'Verify the Design Pane'
        pane_control=automation.PaneControl(Name="Set Current Selection API Test Page")
        hcanvas.verify_object_exist(pane_control, True, 'Step 1. Verify Pane exists')
        hcanvas.verify_total_no_of_child_objects(pane_control, 27, 'Step 1. Verify Total no of objects inside Pane')
        
        text_control=automation.PaneControl(Name="Set Current Selection API Test Page").TextControl(Name="Testing API IbComposer_setCurrentSelection for various controls")
        hcanvas.verify_object_exist(text_control, True, 'Step 1. Verify Textbox exists')
        
        button_control=automation.PaneControl(Name="Set Current Selection API Test Page").ButtonControl(Name="Test Combo Box")
        hcanvas.verify_object_exist(button_control, True, 'Step 1. Verify Test Combo Box Button exists')
        
        '''fails here'''
        group_control=automation.PaneControl(Name="Set Current Selection API Test Page").GroupControl(AutomationId="treecontrol1")
        hcanvas.verify_object_exist(group_control, True, 'Step 1. Verify Country Groupbox exists')
        
        edit_control=automation.PaneControl(Name="Set Current Selection API Test Page").EditControl(AutomationId="textarea1")
        hcanvas.verify_object_exist(edit_control, True, 'Step 1. Verify TextArea exists')
        
        edit_control=automation.PaneControl(Name="Set Current Selection API Test Page").EditControl(AutomationId="calendar1")
        hcanvas.verify_object_exist(edit_control, True, 'Step 1. Verify Calendar control exists')
        
        combo_control=automation.PaneControl(Name="Set Current Selection API Test Page").ComboBoxControl(AutomationId="combobox1")
        hcanvas.verify_object_exist(combo_control, True, 'Step 1. Verify ComboBox Control exists')
        
        group_control=automation.PaneControl(Name="Set Current Selection API Test Page").GroupControl(AutomationId="radio1")
        hcanvas.verify_object_exist(group_control, True, 'Step 1. Verify ComboBox Control exists')
        
        group_control=automation.PaneControl(Name="Set Current Selection API Test Page").GroupControl(AutomationId="slider1")
        hcanvas.verify_object_exist(group_control, True, 'Step 1. Verify ComboBox Control exists')
         
        group_control=automation.PaneControl(Name="Set Current Selection API Test Page").GroupControl(AutomationId="customselect1")
        hcanvas.verify_object_exist(group_control, True, 'Step 1. Verify ComboBox Control exists')
        
         
        '''Step 1.3. Click Run from QAT toolbar and scroll to the bottom of page'''

        
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/API", run_item)
        
        '''Verify the runtime options'''
        time.sleep(4)
        hcanvas.wait_for_web_object_exist("[id^='combobox']", 8, 30, 1)
        
        hcanvas.verify_web_object_no_of_elements("[id^='button']", 11, 'Step 1.3 Verify no of buttons')
        hcanvas.verify_web_object_no_of_elements("[id^='listbox']", 1, 'Step 1.3 Verify no of listbox')
        hcanvas.verify_web_object_no_of_elements("[id^='textarea']", 1, 'Step 1.3 Verify no of textarea')
        hcanvas.verify_web_object_no_of_elements("[id^='radio']", 11, 'Step 1.3 Verify no of radio buttons')
        hcanvas.verify_web_object_no_of_elements("[id^='checkbox']", 11, 'Step 1.3 Verify no of checkbox buttons')
        hcanvas.verify_web_object_no_of_elements("[id^='slider']", 1, 'Step 1.3 Verify no of slider')
        hcanvas.verify_web_object_no_of_elements("[id^='customselect']", 7, 'Step 1.3 Verify no of custom select')
        hcanvas.verify_web_object_no_of_elements("[id^='treecontrol']", 13, 'Step 1.3 Verify no of tree control items')
        hcanvas.verify_web_object_no_of_elements("[id^='combobox']", 8, 'Step 1.3 Verify no of combobox items')
        hcanvas.verify_web_object_no_of_elements("[id^='calendar']", 1, 'Step 1.3 Verify no of calendar items')
        hcanvas.verify_web_object_no_of_elements("[id^='multisourcetreecontrol']", 98, 'Step 1.3 Verify no of multi source tree control items')
        
        hcanvas.verify_web_element_attribute("input[type='radio']:checked", 'defaultValue', 'Midwest', 'Step 1.3 Verify Seattle checked by Default.')
        
        hcanvas.verify_web_object_visible("#multisourcetreecontrol1_0_0:checked", True, 'Step 1. Verify Midwest selected by default on load for multitree')
       
        '''Step 1.4. Clicking on the buttons sets values to the controls using the API'''
        '''Step 1.5. Multisource tree control is expanded and only top item is selected by default.'''
        '''Step 2. Click Test buttons for Calendar, Text Box, List Box, Text Area, Single Tree and Multi Tree and West will be selected for Multi Tree'''
        '''Step 2.1. Selecting Calendar, Text Box, List Box, Text Area, Single Tree will display as shown in below image:'''

        
        '''calendar button'''
        hcanvas.click_on_web_element("#button4")
        time.sleep(5)
        hcanvas.verify_web_element_attribute("#calendar1", "rawvalue", "01/01/2012", 'Step 2. Test for Calendar')
        
        '''textbox'''
        hcanvas.click_on_web_element("#button5")
        time.sleep(5)
        hcanvas.verify_web_element_attribute("#edit1", "rawvalue", "Set Current Selection", 'Step 2. Test for Textbox')
        
        '''listbox'''
        hcanvas.click_on_web_element("#button6")
        time.sleep(5)
        hcanvas.verify_web_object_visible("#listbox1 > option:nth-child(3):checked", True, 'Step 2. Test for Listbox item Bananas')
        hcanvas.verify_web_object_visible("#listbox1 > option:nth-child(4):checked", True, 'Step 2. Test for Listbox item Grapes')
        
        '''textarea'''
        hcanvas.click_on_web_element("#button12")
        time.sleep(5)
        hcanvas.verify_web_element_attribute("#textarea1", "rawvalue", "Setting Text Area", 'Step 2. Test for Text area')
        
        '''singltree'''
        hcanvas.click_on_web_element("#button13")
        time.sleep(5)
        hcanvas.verify_web_object_visible("input[id^='treecontrol1_3_0']:checked", True, 'Step 2. Test for singletree')
        
        '''Step 2.2. Selecting Multisource tree control West will be selected as shown below'''
        '''fails here'''
        '''multi tree'''
        time.sleep(5)
        hcanvas.click_on_web_element("#button14")
        time.sleep(5)
        hcanvas.verify_web_object_visible("#multisourcetreecontrol1_0_3:checked", True, 'Step 2. Verify West selected for multitree')
        
        
        '''Step 3. Click Test buttons for Combo Box, Text Box, Check Box, Double List, Slider and Radio Button'''
        '''fails here'''
        '''combobox'''
        hcanvas.click_on_web_element("#button1")
        time.sleep(5)
        hcanvas.verify_web_element_attribute("#combobox1", "title", "Value3; Value4", 'Step 3. Test for combobox')
        
        '''checkbox'''
        hcanvas.click_on_web_element("#button2")
        time.sleep(5)
        hcanvas.verify_web_object_visible("#checkbox1_2:checked", True, 'Step 3. Test for checkbox Value3')
        hcanvas.verify_web_object_visible("#checkbox1_3:checked", True, 'Step 3. Test for checkbox Value4')
        
        '''double list'''
        '''doublelist'''
        hcanvas.click_on_web_element('#button11')
        time.sleep(5)
        hcanvas.verify_web_object_no_of_elements("#customselect1_selectfrom option", 4, 'Step 3. Verify no of from list items')
        hcanvas.verify_web_object_no_of_elements("#customselect1_selectto option", 2, 'Step 3. Verify no of to list items')
        
        '''radiobutton'''
        hcanvas.click_on_web_element("#button3")
        time.sleep(5)
        hcanvas.verify_web_object_visible("#radio1_3:checked", True, 'Step 3. Test for radiobutton Value4')
        
        '''slider'''
        hcanvas.click_on_web_element("#button17")
        time.sleep(5)
        hcanvas.verify_web_object_visible("#slider1 > div > a[style='left: 0%;']", False, 'Step 3. Test for slider')
        
        '''Step 4. Close HtmlPage browser page'''
        
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
        
if __name__=='__main__' :
    unittest.main()
