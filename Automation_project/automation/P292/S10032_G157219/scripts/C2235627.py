'''
Created on Dec 3, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2235627
TestCase Name : Verify creating a Document based on a Reporting Object
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, wf_legacymainpage
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase


class C2235627_TestClass(BaseTestCase):

    def test_C2235627(self):
        
        Test_Case_ID = "C2235627"
        Test_Case_ID1 = "C2227520"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        browser=utillobj.parseinitfile('browser')
#         if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
#             wf_main_obj = wf_mainpage.Wf_Mainpage(self.driver)
#         else:
        wf_main_obj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
            
        """
            Step 01: Logon to WF:
            http://machine:port/ibi_apps/
            Step 02:Expand folder "S10032" > Right-click "C2227520" > New > Document
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("img[src*='discovery_domain']", 1, 30)
        time.sleep(5)
        wf_main_obj.select_repository_folder_item_menu('P292->S10032_infoassist_4', Test_Case_ID1, 'New->Document')
        utillobj.switch_to_window(1)
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document')
        
        """ 
            Step 03:Verify Canvas
        """
        ele=driver.find_element_by_css_selector("#canvasContainer")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step03_'+browser, image_type='actual',x=50, y=20, w=-50, h=-20)
#         ia_resultobj.create_report_data_set("TableChart_1", 10, 2, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 2, Test_Case_ID+"_Ds01.xlsx","Step 03:01:Verify report preview data")
        resultobj.verify_yaxis_title("TableChart_2", 'SALES', "Step 03:04: Verify X-Axis Title")
        
        """ 
            Step 04:Reposition Report and Chart component as displayed in the screenshot
        """
        elem=self.driver.find_element_by_css_selector("#TableChart_1")
        utillobj.click_on_screen(elem, 'top_middle', 0)
        time.sleep(1)
        ribbonobj.repositioning_document_component('1.02','0.35')
        time.sleep(5)
        elem=self.driver.find_element_by_css_selector("#TableChart_2")
        utillobj.click_on_screen(elem, 'top_middle', 0)
        time.sleep(1)
        ribbonobj.repositioning_document_component('0.35','3')
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step04_'+browser, image_type='actual',x=50, y=20, w=-50, h=-20)  
          
        """ 
            Step 05:Click "IA" > "Close" > Click "Yes" to save prompt
        """
        ribbonobj.select_tool_menu_item('menu_close')
        ia_resultobj.ia_exit_save("Yes") 
           
        """ 
            Step 06:Save as "C2235627" > Click "Save"
        """
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """ 
            Step 07:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        utillobj.infoassist_api_logout()
        
        """ 
            Step 08:Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2235627.fex&tool=Document
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', 'S10032_infoassist_4', mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document')
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step08_'+browser, image_type='actual',x=50, y=20, w=-50, h=-20)
        
        """ 
            Step 09:Click on the Report component on Canvas
        """
        canvas_css=self.driver.find_element_by_css_selector("#TableChart_1")
        utillobj.click_on_screen(canvas_css, 'middle', 0)
        time.sleep(2)
        
        """ 
            Step 10:Verify Query pane and Preview
        """
        metaobj.verify_query_pane_field('By', 'CAR', 1, "Step 10:01: ")
        metaobj.verify_query_pane_field('Sum', 'SALES', 1, "Step 10:02: ")
        
        """ 
            Step 11:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()


if __name__ == "__main__":
    unittest.main()