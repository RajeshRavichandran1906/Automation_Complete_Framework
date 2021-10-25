'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227531
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_resultarea
from common.lib import utillity
from selenium.webdriver import ActionChains

class C2227531_TestClass(BaseTestCase):

    def test_C2227531(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2227531'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        browser=utillobj.parseinitfile('browser')
        suite = utillobj.parseinitfile('suite_id')
        
        """    1. Launch IA Chart mode: http://machine:port/ibi_apps/ia?tool=Chart&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032    """
        utillobj.infoassist_api_login('chart','ibisamp/car','P292/S10032', 'mrid', 'mrpass')
        element_css="#TableChart_1 g.legend path[class^='legend-markers']"
        utillobj.synchronize_with_number_of_element(element_css, 5, expire_time=20)
       
        """    2. Double click "COUNTRY", "SALES".    """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        element_css="#TableChart_1 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(element_css, 'COUNTRY', expire_time=20)
        
        metaobj.datatree_field_click("SALES", 2, 1)
        element_css="#TableChart_1 text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(element_css, 'SALES', expire_time=20)
        
        """    3. Click "IA" > "Save As".    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        element_css="#IbfsOpenFileDialog7_cbFileName input"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=20)

        """    4. Enter Title = "Chart001".    """
        """    5. Click "Save".    """
        utillobj.ibfs_save_as('Chart001')
        resultobj.wait_for_property("#IbfsOpenFileDialog7_cbFileName input", 0, expire_time=2)
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(5)
                
        """    6. Click "New" icon > "Build a Document" with CAR.MAS.    """
        ribbonobj.select_top_toolbar_item('toolbar_new')
        element_css="#splash_options"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=20)
        
        ribbonobj.select_item_in_splash_options("Build a Document")
        utillobj.select_masterfile_in_open_dialog('ibisamp', 'car.mas')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=10, string_value='Document')

        """    7. Verify the format is "Active Report"    """
        utillobj.verify_object_visible("#HomeFormatType img[src$='active_reports_32.png']", True, "Step 07: Verify the output Format is 'Active Report")
        
        """    8. Click "Active Report" dropdown > Select "PDF"    """
        ribbonobj.change_output_format_type("pdf")
        
        """    9. Select "Insert" > "Existing Report".    """
        ribbonobj.select_ribbon_item("Insert", "Existing_Report")
        
        """    10. Verify the "Open" window is displayed and "Chart001" is not available for selection.    """
        utillobj.verify_item_in_open_dialog(suite, 'Chart001', False, "Step 10: Verify 'Chart001' is not available for selection in Open Dialog")
        
        """    11. Click "Cancel".    """
        oCancelBtn=self.driver.find_element_by_id("IbfsOpenFileDialog7_btnCancel")
        utillobj.default_left_click(object_locator=oCancelBtn)
        time.sleep(4)
        
        """    12. Select "Insert" > "Chart".    """
        ribbonobj.select_ribbon_item("Insert", "Chart")
        
        """    13. Double click "COUNTRY","SALES".    """
        metaobj.datatree_field_click("COUNTRY", 2, 1)

        metaobj.datatree_field_click("SALES", 2, 1)
        ribbonobj.repositioning_document_component('1.25', '2.25')
      
        
        """    14. Verify the following chart is displayed.    """
        metaobj.verify_query_pane_field('Measure (Sum)',"SALES",1,"Step 14a")
        metaobj.verify_query_pane_field('X Axis',"COUNTRY",1,"Step 14b")
        ele=driver.find_element_by_css_selector("div[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step14_'+browser, image_type='actual',x=50, y=20, w=-50, h=-20)
        
        """    15. Click "Text Box" icon.    """
        ribbonobj.select_ribbon_item("Insert", "Text_Box")
        time.sleep(4)
        
        """    16. Re-position the newly added Textbox so that it will not be on top of the chart.    """
        ribbonobj.resizing_document_component('0.25', '2.5')
        ribbonobj.repositioning_document_component('1.25', '1.25')
        
        """    17. Double click the Textbox and enter "This is a Textbox".    """
        iaresult.enter_text_in_Textbox('Text_1', "This is a Textbox")
        
        """    18. Click "Image" icon.    """
        ribbonobj.select_ribbon_item("Insert", "Image")
        
        """    19. Verify the following "open file" window    """
        """    20. Expand "EDASERVE"    """
        """    21. Select ibisamp > Select smplogo1.gif    """
        """    22. Click Open    """
        resultobj.wait_for_property("#IbfsOpenFileDialog7_cbFileName input", 1, expire_time=10)
        apps_css="#paneIbfsExplorer_exTree > div.bi-tree-view-body-content table tr"
        x=[el.text.strip() for el in driver.find_elements_by_css_selector(apps_css)]
        apps=driver.find_elements_by_css_selector(apps_css)
        apps[x.index('Domains')].find_element_by_css_selector("img[src*='triangle']").click()
        time.sleep(1)
        utillobj.select_masterfile_in_open_dialog('EDASERVE->ibisamp', 'smplogo1.gif')
        
        """    23. Re-position the image on the canvas.    """
        ribbonobj.repositioning_document_component('4.75', '1.25')
        
        """    24. Click "Page 1" > "Page Options".    """
        iaresult.select_or_verify_document_page_menu('Page Options...')
        
        """    25. Select "Page 1" > click "Duplicate Page" icon > "OK".    """
        utillobj.select_item_in_dialog("#pageOptionsDlg #iaPageList", "Page 1")
        dupBtn=driver.find_element_by_css_selector("#duplicatePageBtn")
        utillobj.default_left_click(object_locator=dupBtn)
        time.sleep(4)
        
        """    26. Select "Page 1( Copy )" from "Page Options" window.    """
        utillobj.select_item_in_dialog("#pageOptionsDlg #iaPageList", "Page 1 ( Copy )")
        
        """    27. Verify the other icons are now enabled.    """
        # verify Delete button enabled
        oDelClass=driver.find_element_by_id("deletePageBtn").get_attribute('class')
        oStatus=bool('disabled' in oDelClass)
        utillobj.asequal(False, oStatus, "Step 27a: Verify 'Delete' button enabled under Page list")
        oMoveUpClass=driver.find_element_by_id("moveUpBtn").get_attribute('class')
        oStatus=bool('disabled' in oMoveUpClass)
        utillobj.asequal(False, oStatus, "Step 27b: Verify 'Move Up' button enabled under Page list")
        
        """    28. Click OK button in "Page Options" window to close it.    """
        okBtn=driver.find_element_by_id("pageOptionsOkBtn")
        utillobj.default_left_click(object_locator=okBtn)
        time.sleep(4)
        
        """    29. Click "Page 1" (dropdown) > Select "Page 1( Copy ).    """
        iaresult.select_or_verify_document_page_menu('Page 1 ( Copy )')
        
        """    30. Verify Page Menu changed to "Page 1( Copy )".    """
        oPage1Copy=driver.find_element_by_xpath("//div[@id='iaPagesMenuBtn']//div[contains(text(), 'Page 1 ( Copy )')]")
        utillobj.verify_object_visible('css', True, "Step 29a: Verify Page Menu changed to 'Page 1( Copy )'", elem_obj=oPage1Copy)
        
        """    31. Click the Textbox, enlarge it and enter "This is the 2nd page Textbox".    """
        iaresult.enter_text_in_Textbox('Text_2', "This is the 2nd page Textbox")
        
        """    32. Verify the document displays as followed. """
        #Verify Chart
        ele=driver.find_element_by_css_selector("div[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step32a_'+browser, image_type='actual',x=50, y=20, w=-50, h=-20)
        iaresult.verify_text_in_Textbox('#Text_2', 'This is the 2nd page Textbox', "Step 32e: Verify Textbox text in Page1_copy")
        # verify Image
        oImg=driver.find_element_by_id("PageItemImage_2").find_element_by_css_selector("img[src*='PageItemImage_2']").is_displayed()
        utillobj.asequal(True, oImg, "Step 32f: Verify Image displayed")
        
        """    33. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        """    34. Verify the chart along with the inserted components are displayed.    """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step34_'+browser, image_type='actual',x=50, y=20, w=-50, h=-20)
        
        """    35. Scroll down to the 2nd page and verify the inserted components are displayed.    """
        oFrame=driver.find_element_by_css_selector("[id^='ReportIframe']")
        oPDF_width=oFrame.size['width']
        oPDF_heigth=oFrame.size['height']
        action1 = ActionChains(self.driver)
        j=0
        while j<4:
            action1.move_to_element_with_offset(oFrame, oPDF_width-8, oPDF_heigth-30).click().perform()
            j=j+1
        time.sleep(5)
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step35_'+browser, image_type='actual',x=50, y=20, w=-50, h=-20)
        
        """    36. Click "IA" > "Save As".    """
        """    37. Enter Title = "C2227531".    """
        """    38. Click "Save".    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    39. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        
        """    40. Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227531.fex&tool=Document    """
        oFolder=utillobj.parseinitfile('suite_id')
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', oFolder, mrid='mrid', mrpass='mrpass')
#         resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document') 
        element_css="#iaCanvasCaptionLabel"
        utillobj.synchronize_with_visble_text(element_css, 'Document', expire_time=20)
              
        """    41. Verify Canvas    """
        ele=driver.find_element_by_css_selector("div[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step41_'+browser, image_type='actual',x=50, y=20, w=-50, h=-20)
        # Verify Text
        iaresult.verify_text_in_Textbox('#Text_1', 'This is a Textbox', "Step 41a: Verify Textbox text in Page1_copy")
        # verify Image
        oImg=driver.find_element_by_id("PageItemImage_1").find_element_by_css_selector("img[src*='PageItemImage_1']").is_displayed()
        utillobj.asequal(True, oImg, "Step 41b: Verify Image displayed")
        
        
        """    42. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
    
if __name__ == '__main__':
    unittest.main()