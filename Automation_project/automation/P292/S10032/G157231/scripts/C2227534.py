'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227534
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_resultarea
from common.lib import utillity

class C2227534_TestClass(BaseTestCase):

    def test_C2227534(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2227534'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        browser=utillobj.parseinitfile('browser')
        oFolder=utillobj.parseinitfile('suite_id')
        time_out=30
        
        """    1. Launch IA Report mode: http://machine:port/ibi_apps/ia?tool=Chart&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032    """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_2', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
       
        """    2. Double click "CAR", "SALES".    """
        metaobj.datatree_field_click("CAR", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 11, time_out)
        metaobj.datatree_field_click("SALES", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 22, time_out)
        
        """    3. Click "IA" > "Save As".    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.synchronize_with_number_of_element("#IbfsOpenFileDialog7_cbFileName input", 1, time_out)

        """    4. Enter Title = "Report003".    """
        """    5. Click "Save".    """
        utillobj.ibfs_save_as('Report003')
        utillobj.synchronize_with_number_of_element("#applicationButton img", 1, time_out)
        ribbonobj.select_tool_menu_item('menu_close')
                
        """    6. Click "New" icon > "Build a Document" with CAR.MAS.    """
        ribbonobj.select_top_toolbar_item('toolbar_new')
        utillobj.synchronize_with_number_of_element("#splash_options", 1, time_out)
        ribbonobj.select_item_in_splash_options("Build a Document")  
        utillobj.select_masterfile_in_open_dialog('ibisamp', 'car')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", visble_element_text='Document', expire_time=time_out)
        
        """    7. Click "Active Report" dropdown > Select "PDF"    """
        ribbonobj.change_output_format_type("pdf")
        time.sleep(5)
        
        """    8. Select "Insert" > "Existing Report" > "Report003" > "Open".    """
        utillobj.synchronize_with_number_of_element("#InsertTab_tabButton", 1, time_out)
        ribbonobj.select_ribbon_item("Insert", "Existing_Report")
        utillobj.select_masterfile_in_open_dialog(oFolder, "Report003")
        #ribbonobj.repositioning_document_component('1.25', '2.25')
        time.sleep(4)
        
        """   9. Verify "Report003" is displayed.    """
        coln_list = ["CAR", "SALES"]
        resultobj.verify_report_titles_on_preview(2, 2, "IncludeTable_1 ", coln_list, "Step 09a: Verify column titles")
        #iaresult.create_report_data_set('IncludeTable_1 ', 9, 2, 'C2227534_Ds01.xlsx')
        iaresult.verify_report_data_set('IncludeTable_1 ', 9, 2, 'C2227534_Ds01.xlsx', 'Step 09b: Verify Preview report dataset')
        
        """    10. Click "Text Box" icon.    """
        ribbonobj.select_ribbon_item("Insert", "Text_Box")
        time.sleep(4)
        
        """    11. Re-position the newly added Textbox so that it will not be on top of the Report.    """
        ribbonobj.resizing_document_component('0.25', '2.5')
        ribbonobj.repositioning_document_component('4.25', '1.25')
        
        """    12. Double click the Textbox and enter "This is a Textbox".    """
        iaresult.enter_text_in_Textbox('Text_1', "This is a Textbox")
        
        """    13. Click "Image" icon.    """
        ribbonobj.select_ribbon_item("Insert", "Image")
        
        """    14. Verify the following "open file" window    """
        """    15. Expand "Edaserve" > Select "ibisamp"    """
        """    16. Select "smplogo1.gif" > "open".    """
        utillobj.synchronize_with_number_of_element("#IbfsOpenFileDialog7_cbFileName input", 1, time_out)
        apps_css="#paneIbfsExplorer_exTree > div.bi-tree-view-body-content table tr"
        x=[el.text.strip() for el in driver.find_elements_by_css_selector(apps_css)]
        apps=driver.find_elements_by_css_selector(apps_css)
        apps[x.index('Domains')].find_element_by_css_selector("img[src*='triangle']").click()
        time.sleep(1)
        utillobj.select_masterfile_in_open_dialog('EDASERVE->ibisamp', 'smplogo1.gif')
        
        """    17. Re-position the image on the canvas.    """
        ribbonobj.repositioning_document_component('4.25', '2.25')
        
        """    18. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        
        """    19. Verify all inserted components are displayed..    """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step34_'+browser, image_type='actual',x=50, y=20, w=-50, h=-20)
        
        """    20. Click "IA" > "Save As".    """
        """    21. Enter Title = "C2227534".    """
        """    22. Click "Save".    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    23. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        
        """    24. Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227534.fex&tool=Document    """
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', oFolder, mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", visble_element_text='Document', expire_time=time_out)
        
        """    25. Verify successful restore    """
        coln_list = ["CAR", "SALES"]
        resultobj.verify_report_titles_on_preview(2, 2, "IncludeTable_1", coln_list, "Step 25a: Verify column titles")
        iaresult.verify_report_data_set('IncludeTable_1 ', 9, 2, 'C2227534_Ds01.xlsx', 'Step 25b: Verify Preview report dataset')
        # Verify Text
        iaresult.verify_text_in_Textbox('#Text_1', 'This is a Textbox', "Step 25c: Verify Textbox text in Page1_copy")
        # verify Image
        oImg=driver.find_element_by_id("PageItemImage_1").find_element_by_css_selector("img[src*='PageItemImage_1']").is_displayed()
        utillobj.asequal(True, oImg, "Step 25b: Verify Image displayed")
        
        
        """    42. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
    
if __name__ == '__main__':
    unittest.main()