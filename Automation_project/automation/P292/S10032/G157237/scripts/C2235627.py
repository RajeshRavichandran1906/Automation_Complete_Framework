'''
Created on Dec 3, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2235627
TestCase Name : Verify creating a Document based on a Reporting Object
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase


class C2235627_TestClass(BaseTestCase):

    def test_C2235627(self):
        
        Test_Case_ID = "C2235627"
        Restore_fex = "C2227520"
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
            
        """
            Step 01: Logon to WF:
            http://machine:port/ibi_apps/
            Step 02:Launch MyReport (Document mode) using below API link
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10032_G157237/C2227520.fex&tool=Document
        """
        utillobj.infoassist_api_edit(Restore_fex, 'Document', 'S10032', mrid='mrid', mrpass='mrpass')
        table_preview_css="#TableChart_1"
        utillobj.synchronize_with_visble_text(table_preview_css, 'CAR', metaobj.chart_long_timesleep)
        
        """ 
            Step 03:Verify Canvas
        """
#         ia_resultobj.create_report_data_set("TableChart_1", 10, 2, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 2, Test_Case_ID+"_Ds01.xlsx","Step 03.01: Verify report preview data")
        resultobj.verify_yaxis_title("TableChart_2", 'SALES', "Step 03.02: Verify X-Axis Title")
        
        """ 
            Step 04:Reposition Report and Chart component as displayed in the screenshot
        """
        elem=self.driver.find_element_by_css_selector("#TableChart_1")
        core_utilobj.python_left_click(elem)
        time.sleep(1)
        ribbonobj.repositioning_document_component('1.02','0.35')
        time.sleep(5)
        elem=self.driver.find_element_by_css_selector("#TableChart_2")
#         browser = utillobj.parseinitfile('browser')
#         if browser == 'IE':
#             core_utilobj.python_left_click(elem, element_location='top_middle', yoffset=29)
#         else:
        core_utilobj.python_left_click(elem, element_location='top_middle', yoffset=29)
        time.sleep(1)
        ribbonobj.repositioning_document_component('0.35','3')
          
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
        utillobj.wf_logout()
        
        """ 
            Step 08:Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2235627.fex&tool=Document
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', 'S10032_infoassist_4', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text(table_preview_css, 'CAR', metaobj.chart_long_timesleep)
        
        """ 
            Step 09:Click on the Report component on Canvas
        """
        canvas_css=self.driver.find_element_by_css_selector("#TableChart_1")
        core_utilobj.python_left_click(canvas_css)
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody", 'CAR', metaobj.chart_long_timesleep)
        """ 
            Step 10:Verify Query pane and Preview
        """
        metaobj.verify_query_pane_field('By', 'CAR', 1, "Step 10.01")
        metaobj.verify_query_pane_field('Sum', 'SALES', 1, "Step 10.02")
        
        """ 
            Step 11:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()