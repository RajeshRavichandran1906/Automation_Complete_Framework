'''
Created on Nov 24, 2017

@author: Robert
TestCase Name : Verify Excel output formats
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2235581
'''
import unittest, time, filecmp, os, pyautogui
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon 
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from pywinauto.application import Application
from pathlib import Path

class C2235581_TestClass(BaseTestCase):

    def test_C2235581(self):
       
        Test_Case_ID = "C2235581"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """    1. Launch IA Report mode:  """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
          
        """    2. Double click "COUNTRY", "CAR", "DEALER_COST".    """
          
        metaobj.datatree_field_click('COUNTRY', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('CAR', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        
        """    "3. Select "IA" > Save as "C2235581" > Click "Save".    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """    "4. Click "HTML" dropdown > Verify the following formats are available.    """
        
        list1=['HTML', 'Active Report', 'PDF', 'Excel (xlsx)', 'PowerPoint (pptx)']
        ia_ribbobj.select_or_verify_output_type(launch_point="Home", expected_output_list=list1, msg='Step 4. Verify the formats')
        
        """    "5. Click arrow in "PowerPoint (pptx)" to access sub menu > Verify menu displayed    """
        """     6. Select "PowerPoint (pptx) > PowerPoint (pptx)"   """
        """    "7. Click "Run".    """
        
        list2=['PowerPoint (pptx)']
        ia_ribbobj.select_or_verify_output_type(launch_point="Home",item_select_path='PowerPoint (pptx)',  expected_output_list2=list2, msg2='Step 5. Verify Power point menu displayed')
        
        ia_ribbobj.select_or_verify_output_type(launch_point="Home",item_select_path='PowerPoint (pptx)->PowerPoint (pptx)')
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        """    "8. Verify the "PowerPoint (pptx)" formatted report is downloaded    """
        """    "9. Close the PowerPoint application    """
        
        ''' code to download and verify pptx'''
        my_file= Path(os.getcwd() + "\data\\" + "C2235581_Ds01_actual.pptx")
        if my_file.is_file():
            os.remove(os.getcwd() + "\data\\" + "C2235581_Ds01_actual.pptx")
            time.sleep(5)
        
        utillobj.save_file_from_browser('C2235581_Ds01_actual.pptx')
        time.sleep(8)
        
        try:
            my_file= Path(os.getcwd() + "\data\\" + "C2235581_Ds01_actual.pptx")
            if my_file.is_file():
                filebool=True
                os.popen(os.getcwd() + "\data\\" + "C2235581_Ds01_actual.pptx")
                time.sleep(10)
                app = Application().Connect(class_name='PPTFrameClass')
                pptframeclass = app.PPTFrameClass
                pptframeclass.SetFocus()
                pptframeclass.Maximize()
                time.sleep(10)
                pyautogui.hotkey('alt')
                time.sleep(1)
                pyautogui.hotkey('w')
                time.sleep(1)
                pyautogui.hotkey('q')
                time.sleep(3)
                window = app.Zoom
                if app.zoom.Exists() ==True:
                    pyautogui.hotkey('p')
                    time.sleep(2)
                    pyautogui.hotkey('ctrl','a')
                    time.sleep(2)
                    pyautogui.hotkey('del')
                    time.sleep(2)
                    pyautogui.typewrite('100', interval=0.3, pause=3)
                    button = window.OK
                    button.ClickInput()
                    time.sleep(6)
                    
                    
                utillobj.verify_picture_using_sikuli('C2235581_Step8.png', 'Step8. verification')
                app.Kill_()
        except FileNotFoundError:
            filebool=False
        utillobj.asequal(filebool,True,'PPTX File to compare')
              
        """    10. Click "Save"    """
        """    11. Logout: """
        
        utillobj.switch_to_window(0, pause=3)
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        """    12. Reopen saved FEX:    """
        """    13. Verify output format is set to "PowerPoint (pptx)"    """
        
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infosassist_4', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        
        time.sleep(8)
        
        def_output_css="div[id='HomeFormatType'] div[id^='BiLabel']"
        
        ele1=self.driver.find_element_by_css_selector(def_output_css)
        
        utillobj.asequal(ele1.text.strip(), 'PowerPoint (pptx)', 'Step 13. Verify Output format is set to "PowerPoint (pptx)')
        
        
        """    14. Logout:    """
        
        utillobj.infoassist_api_logout()
  
        
if __name__ == "__main__":
    unittest.main()