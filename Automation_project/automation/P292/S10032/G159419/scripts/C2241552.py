'''
Created on Nov 30, 2017

@author: PM14587
Testcase Name : API > New > Report
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2241552
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import  visualization_resultarea, visualization_ribbon,ia_run,ia_resultarea
from common.lib import utillity
from common.wftools.report import Report

class C2241552_TestClass(BaseTestCase):

    def test_C2241552(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2241552'
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        report = Report(self.driver)
        
        
        """
            COMMON TEST CASE CSS
        """
        qwerty_tree_css = "#queryTreeWindow"
        report_css = "#TableChart_1"
    
        """
            Step 01 : Launch Report mode with IA API: http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10032_infoassist_5', 'mrid', 'mrpass')
        report.wait_for_visible_text(report_css, "Drag")
        
        """
            Step 02 : Verify IA Report mode is launched
        """
        utillobj.verify_element_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(1)",'Report (wf_retail_lite)','Step 02.1 : Verify IA Report mode is launched')
        
        """
            Step 03 : Double click on fields "Cost of Goods" and "Product,Category"
        """
        report.double_click_on_datetree_item("Cost of Goods", 1)
        report.wait_for_visible_text(qwerty_tree_css, "Cost of Goods")

        report.double_click_on_datetree_item("Product,Category", 1)
        report.wait_for_visible_text(qwerty_tree_css, "Product,Category")
        
        """
            Step 03.1 : Verify the canvas,
        """
        iaresult.verify_across_report_data_set('TableChart_1', 1,2,8,2,Test_Case_ID+'_DataSet_01.xlsx','Step 03.1 : Verify the canvas')
        
        """
            Step 04 : Verify the output,
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("table[summary]>tbody>tr:nth-child(1)>td:nth-child(2)", 1,20,string_value='Cost of Goods')
        time.sleep(2)
        iarun.verify_table_data_set('table[summary]',Test_Case_ID+'_DataSet_02.xlsx','Step 04.1 : Verify the outpu')
        utillobj.switch_to_default_content(3)
        
        """
            Step 05 : Click "Save" > Save As "C2241552" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        report.wait_for_visible_text("#IbfsOpenFileDialog7_btnOK", "Save")
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 06 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()