'''
Created on Dec 18, 2017
@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2228152
TestCase Name : Verify HOLD format jpg and import created jpg image into Document (82xx)
'''

import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2228152_TestClass(BaseTestCase):

    def test_C2228152(self):
        
        Test_Case_ID = "C2228512"
        Test_Case_ID2 = "IA-VAL-CHART-003-01"
        Test_Case_ID1 = "IA-VAL-CHART-003"
        driver = self.driver
        utillobj = utillity.UtillityMethods(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        ia_ribbon_obj=ia_ribbon.IA_Ribbon(driver)
        browser=utillobj.parseinitfile('browser')
        """
            Step 01:Launch WF, New > Chart with EMPLOYEE.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """
            Step 02:Select HTML output format under Home tab.
        """
        ia_ribbon_obj.select_or_verify_output_type(launch_point='Home', item_select_path='HTML')
        time.sleep(2)
                  
        """ 
            Step 03:Double Click "LAST_NAME", "CURR_SAL".
        """
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("CURR_SAL", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1)
              
        """ 
            Step 04:Verify the following chart is displayed.
        """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step04_'+browser, image_type='actual',x=20, y=20, w=-50, h=-20)
        """ 
            Step 05:On "Home" tab, click on "File" dropdown.
        """
        ribbonobj.select_ribbon_item('Home', 'file_dropdown')
        time.sleep(2)
        """ 
            Step 06:Click "Select a location and format...".
        """
        utillobj.select_or_verify_bipop_menu("Select a location and format...")
        time.sleep(3)
          
        """ 
            Step 07:Click on baseapp folder to highlight it.
            Step 08:Change default File1 output format to JPEG (*.jpg).
            Step 09:Click "Save".
        """
        utillobj.select_masterfile_in_open_dialog("baseapp", "File1", "JPEG (*.jpg)") 
             
        """ 
            Step 10:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(pause=2)
        """ 
            Step 11:Verify the following message appears.
        """
        pre_msg=driver.find_element_by_css_selector("html body pre")
        text_msg=pre_msg.text.strip()
        expected_pre_msg1 = "JPEG FILE SAVED ..."
        expected_pre_msg2 = "12  PLOT POINTS="
        utillobj.asin(expected_pre_msg1, text_msg, "Step 11:01: Verify the text message")
        utillobj.asin(expected_pre_msg2, text_msg, "Step 11:02: Verify the text message")
        utillobj.switch_to_default_content(pause=1)
        """ 
            Step 12:Click "IA" > "Save".
            Step 13:Enter Title = "IA-VAL-CHART-003".
            Step 14:Click "Save".
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID1)
        time.sleep(5)     
        """ 
            Step 15:Click "IA" > "Exit".
        """
        ribbonobj.select_tool_menu_item("menu_exit")
        time.sleep(5)
        utillobj.infoassist_api_logout()
        """ 
            Step 16:Right mouse click on working folder > New > Document with EMPLOYEE.MAS.
            note : only api calls using for selenium development
        """
        utillobj.infoassist_api_login('document','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document')
        """ 
            Step 17:Click "Insert" tab.
            Step 18:Click "Image" icon.
        """
        ribbonobj.select_ribbon_item("Insert", "Image")
       
        """ 
            Step 19:Locate EDASERVE > Baseapp > "File1.jpg" > Click "Open".
        """
        resultobj.wait_for_property("#IbfsOpenFileDialog7_cbFileName input", 1, expire_time=10)
        apps_css="#paneIbfsExplorer_exTree > div.bi-tree-view-body-content table tr"
        x=[el.text.strip() for el in driver.find_elements_by_css_selector(apps_css)]
        apps=driver.find_elements_by_css_selector(apps_css)
        apps[x.index('Domains')].find_element_by_css_selector("img[src*='triangle']").click()
        time.sleep(1)
        utillobj.expand_domain_folders_in_open_dialog('EDASERVE->baseapp')
        utillobj.select_item_from_ibfs_explorer_list('file1.jpg')
        
        """ 
            Step 20:Verify the chart appears on canvas under Document mode.
        """
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document')
        parent_css="img[src*='PageItemImage_1']"
        resultobj.wait_for_property(parent_css, 1)
        oImg=driver.find_element_by_id("PageItemImage_1").find_element_by_css_selector("img[src*='PageItemImage_1']").is_displayed()
        utillobj.asequal(True, oImg, "Step 20:01: Verify Image displayed")
        
        """ 
            Step 21:Click "IA" > "Save".
            Step 22:Enter Title = "IA-VAL-CHART-003-01".
            Step 23:Click "Save".
        """ 
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID2)
        time.sleep(5)

        """ 
            Step 24:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        
                
        """ 
            Step 25:Verify output is the same chart that was displayed on "Live Preview".
        """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID2+'_Actual_Step25_'+browser, image_type='actual',x=30, y=20, w=-50, h=-20)
        
        """ 
            Step 26:Click "IA" > "Exit".
        """ 
        ribbonobj.select_tool_menu_item("menu_exit")
        time.sleep(3)
#         utillobj.switch_to_window(0)
        utillobj.infoassist_api_logout()
        """ 
            Step 27:Locate the saved fex ("IA-VAL-CHART-003-01") > Right mouse click > Run.
        """
        
        utillobj.active_run_fex_api_login(Test_Case_ID2+".fex", "S10032_chart_1", 'mrid', 'mrpass')
        parent_css="#orgdiv0 div[id^='LOBJPageItemImage']"
        resultobj.wait_for_property(parent_css, 1)
                
        """ 
            Step 28:Verify the saved fex can be executed and output is the same chart that was displayed on "Live Preview".
        """
        ele=driver.find_element_by_css_selector("#orgdiv0 div[id^='LOBJPageItemImage']")
        utillobj.take_screenshot(ele,Test_Case_ID2+'_Actual_Step28_'+browser, image_type='actual',x=50, y=20, w=-50, h=-20)
        utillobj.infoassist_api_logout()
        
        """ 
            Step 29:Locate the saved fex > Right mouse click > "Edit".
        """
        utillobj.infoassist_api_edit(Test_Case_ID2, 'document', 'S10032_chart_1', mrid='mrid', mrpass='mrpass')
        
        """ 
            Step 30:Verify that it launches IA tool and display the chart on "Live Preview".
        """
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document')
        time.sleep(8)
        oImg=driver.find_element_by_id("PageItemImage_1").click()
        
        time.sleep(1)
        oImg=driver.find_element_by_id("PageItemImage_1").find_element_by_css_selector("img[src*='PageItemImage_1']").is_displayed()
        utillobj.asequal(True, oImg, "Step 30:01: Verify Image displayed")
        
        """ 
            Step 31:Click "IA" > "Exit".
        """
        ribbonobj.select_tool_menu_item("menu_exit")
        time.sleep(3)
        
        
if __name__ == "__main__":
    unittest.main()