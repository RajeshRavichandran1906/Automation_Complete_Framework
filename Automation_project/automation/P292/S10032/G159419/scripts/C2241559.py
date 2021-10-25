'''
Created on Dec 1, 2017

@author:Praveen Ramkumar
Testcase Name : API > New > Reporting Object
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2241559
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import ia_resultarea,visualization_metadata,wf_reporting_object,ia_run,visualization_ribbon
from common.lib import utillity

class C2241559_TestClass(BaseTestCase):

    def test_C2241559(self):
        
        """   
                TESTCASE VARIABLES 
        """
        TestCase_ID = 'C2241559'
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        wfreporting=wf_reporting_object.Wf_Reporting_Object(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
            Step 01 : Launch Reporting Object with IA API:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=reportingobject&master=baseapp/WF_RETAIL_LITE
        """
        utillobj.infoassist_api_login('reportingobject','baseapp/wf_retail_lite','P292/S10032_infoassist_5', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#editorViewPane table>tbody>tr:nth-child(1)", 'Reporting Object', 80)
        
        """
            Step 02 : Verify Reporting Object tool is launched
            Step 03 : Double click on "Report" component
        """
        wfreporting.select_ro_tree_item("Report")
        wfreporting.select_ro_tree_item("Report", click_type = 2)
       
        utillobj.switch_to_window(1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(2)", 'Sum', 80)
        
        """
            Step 04 : Double click on fields "Cost of Goods" and "Product,Category"            
        """
        metaobj.datatree_field_click('Cost of Goods', 2, 0)
        utillobj.synchronize_with_visble_text("#queryTreeWindow table tr:nth-child(3) td", 'Cost of Goods', 20)
        
        metaobj.datatree_field_click('Product,Category', 2, 0)
        utillobj.synchronize_with_visble_text("#queryTreeWindow table tr:nth-child(5) td", 'Product,Category', 20)
        
        """
            STEP 04.1 : Verify the canvas,
        """
#         iaresult.create_across_report_data_set('TableChart_1', 2, 2, 7, 2,TestCase_ID+'_DataSet_01.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1',2,2,7,2,TestCase_ID+'_DataSet_01.xlsx','Step 04.01 : Verify the canvas report')
        
        """
            Step 05 : Click IA Globe > Exit > Yes to save prompt > OK       
        """
        ribbonobj.select_tool_menu_item('menu_exit')
        utillobj.synchronize_with_visble_text("#saveAllDlg #btnYes", 'Yes', 8)
        
        btnYes = self.driver.find_element_by_id('btnYes')
        utillobj.default_left_click(object_locator=btnYes)
        utillobj.switch_to_window(0)
        
        """
            Step 06 : Click RUN
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        
        """
            Step 06.1 : Verify the output,
        """
#         iarun.create_table_data_set("table[summary='Summary']",TestCase_ID+'_Ds02.xlsx')
        iarun.verify_table_data_set("table[summary='Summary']",TestCase_ID+"_Ds02.xlsx", 'Step 06.01 : Verify HTML format report After Run')
        self.driver.close()
        utillobj.switch_to_window(0)
        
        """
            Step 07 : Click "Save" > Save As "C2241559" > Click Save
        """
        wfreporting.select_ro_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(TestCase_ID)
        
        """
            Step 08 : Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()