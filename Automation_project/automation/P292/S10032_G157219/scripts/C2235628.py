'''
Created on Dec 4, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2235628
TestCase Name : Verify conversion with Report based on a Reporting Object
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, wf_legacymainpage, ia_resultarea
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase


class C2235628_TestClass(BaseTestCase):

    def test_C2235628(self):
        
        Test_Case_ID = "C2235628"
        Test_Case_ID1 = "C2227520"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(self.driver)
        
        """
            Step 01:Logon to WF:
            http://machine:port/ibi_apps/
            Step 02:Expand folder "S10032" > Right-click "C2227520" > New > Report
        """
#         if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
#             wf_main_obj = wf_mainpage.Wf_Mainpage(self.driver)
#         else:
        wf_main_obj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        utillobj.invoke_webfocu('mrid', 'mrpass')
        wf_main_obj.select_repository_folder_item_menu('P292->S10032_infoassist_4', Test_Case_ID1, 'New->Report')
        utillobj.switch_to_window(1)
        resultobj.wait_for_property("#singleReportCaptionLabel", 1, expire_time=20, string_value='Live Preview (500 Records)')
        
        """ 
            Step 03:Verify Query pane and Preview
        """
        metaobj.verify_query_pane_field('By', 'CAR', 1, "Step 03:01: ")
        metaobj.verify_query_pane_field('Sum', 'SALES', 1, "Step 03:02: ")
        ia_resultarea_obj.create_report_data_set("TableChart_1", 10, 2, Test_Case_ID+"_Ds01.xlsx")
        ia_resultarea_obj.verify_report_data_set("TableChart_1", 10, 2, Test_Case_ID+"_Ds01.xlsx","Step 03:01:Verify report preview data")
        """ 
            Step 04:Click "Chart" in the Home Tab
        """
        ribbonobj.select_ribbon_item('Home', 'Chart')
        """ 
            Step 05;Verify Chart
        """
        parent_css="#TableChart_1 svg>g text[class='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 1)
        resultobj.verify_xaxis_title("TableChart_1", 'CAR', "Step 05:01: Verify X-Axis Title")
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        expected_xval_list=['ALFA ROMEO', 'AUDI','BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA','TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 05:02: X and Y axis labels',x_axis_label_length=1)
        resultobj.verify_number_of_riser('TableChart_1',1,10, 'Step 05:03: Verify Number chart segment')
        resultobj.verify_yaxis_title("TableChart_1", 'SALES', "Step 05:04: Verify X-Axis Title")
        
        """ 
            Step 06:Select View Tab > Click "Switch Report" > Verify only Report1 and Chart1 are listed
        """
        ribbonobj.select_ribbon_item('View', 'switch_report')
        time.sleep(1)
        a=['Report1','Chart1']
        utillobj.select_or_verify_bipop_menu('Report1', verify='True', expected_popup_list=a, msg="Step 06:01:Verify only Report1 and Chart1 are listed")
         
        """ 
            Step 07:Select Report1 > Verify Report is displayed
        """
        ia_resultarea_obj.verify_report_data_set("TableChart_1", 10, 2, Test_Case_ID+"_Ds01.xlsx", "Step 07:01: Verify report data in preview")
        """
            Step 08:Click "Document" in the Home Tab > Verify Document canvas
        """ 
        ribbonobj.select_ribbon_item('Home', 'Document')   
        """ 
            Step 09:Click "IA" > "Save" > Save as "C2235628_Doc" > Click "Save"
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID+"_Doc")     
        """ 
            Step 10:Click IA Globe > Close
            Step 11:Click "IA" > "Close" > Click "No" to Report1 prompt
        """
        ribbonobj.select_tool_menu_item('menu_close')
        ribbonobj.select_tool_menu_item('menu_close')
        ia_resultarea_obj.ia_exit_save("No")
        
        """ 
            Step 12:Click "IA" > "Save As" to save Chart
            Step 13:Save as "C2235628_Chart" > Click "Save"
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID+"_Chart")
        
        """ 
            Step 14:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        """ 
            Step 15:Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2235628_Doc.fex&tool=Document
        """
        utillobj.infoassist_api_edit(Test_Case_ID+"_Doc", 'Document', 'S10032_infoassist_4', mrid='mrid', mrpass='mrpass')
        time.sleep(5)
        """ 
            Step 16:Verify successful restore
        """
        ia_resultarea_obj.verify_report_data_set("TableChart_1", 10, 2, Test_Case_ID+"_Ds01.xlsx", "Step 16:01: Verify report data in document preview")
        """ 
            Step 17:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
                
        """ 
            Step 18:Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2235628_Chart.fex&tool=Chart
        """
        utillobj.infoassist_api_edit(Test_Case_ID+"_Chart", 'Chart', 'S10032_infoassist_4', mrid='mrid', mrpass='mrpass')
        time.sleep(5)
        parent_css="#TableChart_1 svg>g text[class='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 1)
        """ 
            Step 19:Verify successful restore
        """
        resultobj.verify_xaxis_title("TableChart_1", 'CAR', "Step 19:01: Verify X-Axis Title")
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        expected_xval_list=['ALFA ROMEO', 'AUDI','BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA','TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 19:02: X and Y axis labels',x_axis_label_length=1)
        resultobj.verify_number_of_riser('TableChart_1',1,10, 'Step 19:03: Verify Number chart segment')
        resultobj.verify_yaxis_title("TableChart_1", 'SALES', "Step 19:04: Verify X-Axis Title")
        """ 
            Step 20:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    unittest.main()