'''
Created on Dec 1, 2017

@author:Praveen Ramkumar
Testcase Name : API > New > Reporting Object
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2241559
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,ia_resultarea,visualization_metadata,wf_reporting_object,ia_run,visualization_ribbon
from common.lib import utillity

class C2241559_TestClass(BaseTestCase):

    def test_C2241559(self):
        
        """   
                TESTCASE VARIABLES 
        """
        driver = self.driver #Driver reference object created
        TestCase_ID = 'C2241559'
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        wfreporting=wf_reporting_object.Wf_Reporting_Object(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
            Step 01 : Launch Reporting Object with IA API:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=reportingobject&master=baseapp/WF_RETAIL_LITE
        """
        utillobj.infoassist_api_login('reportingobject','baseapp/wf_retail_lite','P292/S10032_infoassist_5', 'mrid', 'mrpass')
        parent_css="#RoRibbon div [class*='bi-label cluster-box-title']"
        resultobj.wait_for_property(parent_css,2,expire_time=20)
        
        """
            Step 02 :Verify Reporting Object tool is launched
            Step 03:Double click on "Report" component
        """
        wfreporting.select_ro_tree_item("Report",2)
        time.sleep(5)
        utillobj.switch_to_window(1)
        
        """
            Step 04:Double click on fields "Cost of Goods" and "Product,Category"            
        """
        utillobj.synchronize_with_number_of_element("iaMetaDataBrowser", 1, 20)
        metaobj.datatree_field_click('Cost of Goods', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15,string_value='Cost of Goods', with_regular_exprestion=True)
        metaobj.verify_query_pane_field('Sum','Cost of Goods',1,"Step 04.1: Verify query pane")
        
        metaobj.datatree_field_click('Product,Category', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15, string_value='Product,Category', with_regular_exprestion=True)
        metaobj.verify_query_pane_field('By','Product,Category',1,"Step 04.2: Verify query pane")
#         iaresult.create_across_report_data_set('TableChart_1', 2, 2, 7, 2,TestCase_ID+'_DataSet_01.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1',2,2,7,2,TestCase_ID+'_DataSet_01.xlsx','Step 04: Verify report')
        
        """
            Step 05:Click IA Globe > Exit > Yes to save prompt > OK       
        """
        ribbonobj.select_tool_menu_item('menu_exit')
        time.sleep(3)
        btnYes=driver.find_element_by_id('btnYes')
        utillobj.default_left_click(object_locator=btnYes)
        
        """
            Step 06:Click RUN 
                Verify the output,
        """
        utillobj.switch_to_main_window()
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)
#         iarun.create_table_data_set("table[summary='Summary']",TestCase_ID+'_Ds02.xlsx')
        iarun.verify_table_data_set("table[summary='Summary']",TestCase_ID+"_Ds02.xlsx", 'Step 06: Verify HTML format report After Run')
        self.driver.close()
        utillobj.switch_to_window(0)
        time.sleep(5)
        
        """
            Step 07:Click "Save" > Save As "C2241559" > Click Save
        """
        wfreporting.select_ro_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(TestCase_ID)
        
        """
            Step 08:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(8)
        
if __name__ == '__main__':
    unittest.main()