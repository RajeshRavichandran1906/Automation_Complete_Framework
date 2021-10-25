'''
Created on Dec 18, 2017
@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2228152
TestCase Name : Verify HOLD format jpg and import created jpg image into Document (82xx)
'''

import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase

class C2228152_TestClass(BaseTestCase):
    
    def test_C2228152(self):
        
        Test_Case_ID = "C2228152"
        Test_Case_ID2 = "C2228152_Document"
        driver = self.driver
        utillobj = utillity.UtillityMethods(driver)
        core_utillobj = core_utility.CoreUtillityMethods(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        ia_ribbon_obj=ia_ribbon.IA_Ribbon(driver)
        browser=utillobj.parseinitfile('browser')
        
        """
        Step 01:Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/employee
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_until_element_is_visible(parent_css, ia_ribbon_obj.home_page_long_timesleep)
         
        """
        Step 02:Select HTML output format under Home tab.
        """
        ia_ribbon_obj.select_or_verify_output_type(launch_point='Home', item_select_path='HTML')
        utillobj.synchronize_with_visble_text("#HomeFormatType", 'HTML', ia_ribbon_obj.home_page_long_timesleep)
          
        """ 
        Step 03:Double Click "LAST_NAME", "CURR_SAL".
        """
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        utillobj.synchronize_with_number_of_element(parent_css, 1, ia_ribbon_obj.home_page_medium_timesleep)
         
        metaobj.datatree_field_click("CURR_SAL", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        utillobj.synchronize_with_number_of_element(parent_css, 1, ia_ribbon_obj.home_page_medium_timesleep)
               
        """ 
        Step 04:Verify the following chart is displayed.
        """
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step04_'+browser.lower()+'.png', "Step 04.00: Verify the following chart is displayed")
         
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
#         utillobj.select_masterfile_in_open_dialog("foccache", "File1", "JPEG (*.jpg)")
        file_name_input_css="#IbfsOpenFileDialog7_cbFileName input"
        utillobj.synchronize_with_number_of_element(file_name_input_css, 1, ia_ribbon_obj.home_page_medium_timesleep)
        utillobj.ibfs_save_as("file1", file_type="JPEG (*.jpg)", save_folder="baseapp") 
              
        """ 
        Step 10:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, ia_ribbon_obj.home_page_medium_timesleep)
        utillobj.switch_to_frame()
         
        """ 
        Step 11:Verify the following message appears.
        """
        pre_msg=driver.find_element_by_css_selector("html body pre")
        text_msg=pre_msg.text.strip()
        expected_pre_msg1 = "JPEG FILE SAVED ..."
        expected_pre_msg2 = "12  PLOT POINTS="
        utillobj.asin(expected_pre_msg1, text_msg, "Step 11.01: Verify the text message")
        utillobj.asin(expected_pre_msg2, text_msg, "Step 11.02: Verify the text message")
        utillobj.switch_to_default_content()
         
        """ 
        Step 12: Click Save in the toolbar > Save as "C2228152" > Click Save
        """
        ribbonobj.select_top_toolbar_item('infomini_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
            
        """ 
        Step 13: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """ 
        Step 14: Launch the IA API with Document in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=Document&master=ibisamp/employee
        """
        utillobj.infoassist_api_login('document','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', ribbonobj.home_page_long_timesleep)
        
        """ 
        Step 15: Click "Insert" tab.
        Step 16: Click "Image" icon.
        """
        ribbonobj.select_ribbon_item("Insert", "Image")
        
        """ 
        Step 17: Locate EDASERVE > foccache > "File1.jpg" > Click "Open".
        """
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", ribbonobj.home_page_long_timesleep)
        apps_css="#paneIbfsExplorer_exTree > div.bi-tree-view-body-content table tr"
        x=[el.text.strip() for el in driver.find_elements_by_css_selector(apps_css)]
        apps=driver.find_elements_by_css_selector(apps_css)
        obj_exp = apps[x.index('Workspaces')].find_element_by_css_selector("img[src*='triangle']")
        core_utillobj.left_click(obj_exp)
        time.sleep(1)
        utillobj.select_masterfile_in_open_dialog('EDASERVE->baseapp', 'file1.jpg')
        
        """ 
        Step 18:Verify the chart appears on canvas under Document mode.
        """
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', ribbonobj.home_page_medium_timesleep)
        parent_css="img[src*='PageItemImage_1']"
        utillobj.synchronize_until_element_is_visible(parent_css, ribbonobj.home_page_long_timesleep)
        oImg=driver.find_element_by_id("PageItemImage_1").find_element_by_css_selector("img[src*='PageItemImage_1']").is_displayed()
        utillobj.asequal(True, oImg, "Step 18.00: Verify Image displayed")
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step18_'+browser.lower()+'.png', "Step 18.01: Verify the following chart is displayed")
        
        """ 
        Step 19:Click Save in the toolbar > Save as " C2228152_Document" > Click Save 
        """ 
        ribbonobj.select_top_toolbar_item('infomini_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID2)
        utillobj.synchronize_until_element_disappear("#IbfsOpenFileDialog7_cbFileName input", ribbonobj.home_page_medium_timesleep)
        
        """ 
        Step 20:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
             
        """ 
        Step 21:Verify output is the same chart that was displayed on "Live Preview".
        """
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step21_'+browser.lower()+'.png', "Step 21.00: Verify the following chart is displayed")
        
        """ 
        Step 22:Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """ 
        utillobj.infoassist_api_logout()
        
        """ 
        Step 23:Run fex using API code :
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228152_Document.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID2+".fex", "S10032_chart_1", 'mrid', 'mrpass')
        parent_css="#orgdiv0 div[id^='LOBJPageItemImage']"
        utillobj.synchronize_until_element_is_visible(parent_css, ribbonobj.home_page_long_timesleep)
                
        """ 
        Step 24:Verify the saved fex can be executed and output is the same chart that was displayed on "Live Preview".
        """
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step24_'+browser.lower()+'.png', "Step 24.00: Verify the following chart is displayed")
        utillobj.infoassist_api_logout()
        
        """ 
        Step 25:Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228152_Document.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID2, 'document', 'S10032_chart_1', mrid='mrid', mrpass='mrpass')
        
        """ 
        Step 26:Verify that it launches IA tool and display the chart on "Live Preview".
        """
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', resultobj.home_page_long_timesleep)
        oImg=driver.find_element_by_id("PageItemImage_1")
        core_utillobj.left_click(oImg)
        oImg=driver.find_element_by_id("PageItemImage_1").find_element_by_css_selector("img[src*='PageItemImage_1']").is_displayed()
        utillobj.asequal(True, oImg, "Step 26.00: Verify Image displayed")
        time.sleep(10)
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step26_'+browser.lower()+'.png', "Step 26.01: Verify the following chart is displayed")
        
        """ 
        Step 27:Logout using API: http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == "__main__":
    unittest.main()