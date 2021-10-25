'''
Created on Dec 05, 2017

@author: Praveen Ramkumar
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227582
Testcase Name : WITHIN report and aggregation 
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea,ia_run
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase


class C2227582_TestClass(BaseTestCase):

    def test_C2227582(self):
        
        TestCase_ID = "C2227582"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)

        
        """
        Step 01:Launch IA Report mode:http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/CAR','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        chart_type_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(chart_type_css, 1, 30)
        
        """
        Step 02:Double click "COUNTRY", "CAR", "DEALER_COST".
        """
        metaobj.datatree_field_click('COUNTRY', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15, string_value='COUNTRY', with_regular_exprestion=True)
        metaobj.datatree_field_click('CAR', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15, string_value='CAR', with_regular_exprestion=True)
        metaobj.datatree_field_click('DEALER_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15, string_value='DEALER_COST', with_regular_exprestion=True)
        
        """
        Step 03:Verify the following report is displayed.
        """
        utillobj.synchronize_with_number_of_element("[id*='ActivePreviewItem']", 6, 20)
#         ia_resultobj.create_report_data_set('TableChart_1', 10, 3, TestCase_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, TestCase_ID+"_Ds01.xlsx", msg="Step 03:Verify the following report is displayed.")
        
        """
        Step 04:Select "DEALER_COST" from Query pane > "Display".
        Step 05:Select "Aggregation" dropdown > Sum            
        """
        time.sleep(3)
        metaobj.querytree_field_click("DEALER_COST",1,0)
        time.sleep(3)
#         obj_locator=driver.find_element_by_css_selector("#FieldAggregation")
#         utillobj.click_on_screen(obj_locator, 'middle', click_type=0)
#         time.sleep(3)
        ribbonobj.select_ribbon_item('Field','aggregation')
        utillobj.select_or_verify_bipop_menu('Sum')
        
        """
        Step 06:Verify "DEALER_COST" is prefixed with SUM "SUM.DEALER_COST" in the Query pane.
        """
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='SUM.DEALER_COST', expire_time=20)
        metaobj.verify_query_pane_field('Sum','SUM.DEALER_COST',1,"Step 06.1: Verify SUM.DEALER_COST in query pane")
        
        """
        Step 07:Highlight "SUM.DEALER_COST" in the Query pane.
        """
        metaobj.querytree_field_click("SUM.DEALER_COST",1,0)
        
        """
        Step 08:Click "Within" dropdown > "By" > "COUNTRY".
        """
        time.sleep(3)
        ribbonobj.select_ribbon_item('Field','within')
        utillobj.select_or_verify_bipop_menu('By')
        utillobj.select_or_verify_bipop_menu('COUNTRY')
        
        """
        Step 09:Verify the "DEALER_COST" has been summed up.
        """ 
        time.sleep(3)
#         ia_resultobj.create_report_data_set('TableChart_1', 10, 3, TestCase_ID+"_Ds02.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, TestCase_ID+"_Ds02.xlsx", msg="Step 09:Verify the following report is displayed.")
        
        """
        Step 10:Click "Run".
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        
        """
        Step 11:Verify the report is displayed.
        """
#         ia_runobj.create_table_data_set("table[summary='Summary']",TestCase_ID+'_Ds03.xlsx') 
        ia_runobj.verify_table_data_set("table[summary='Summary']",TestCase_ID+"_Ds03.xlsx", 'Step 11: Verify HTML format report After Run')
        
        """
        Step 12:Click "IA" > "Save".
        Step 13:Enter Title = "C2227582".
        Step 14:Click "Save".        
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(8)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(TestCase_ID)
        time.sleep(8)
        
        """
        Step 15:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 16:Reopen saved FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227582.fex&tool=Report
        """
        utillobj.infoassist_api_edit(TestCase_ID,'Report', 'P292/S10032_infoassist_3',mrid='mrid',mrpass='mrpass')
        time.sleep(8)
        
        """
        Step 17:Reopen saved FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227582.fex&tool=Report
        """
        chart_type_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(chart_type_css, 1, 20)
        utillobj.synchronize_with_number_of_element("[id*='ActivePreviewItem']", 6, 10)
#         ia_resultobj.create_report_data_set('TableChart_1', 10, 3, TestCase_ID+"_Ds04.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, TestCase_ID+"_Ds04.xlsx", msg="Step 17:Verify the following report is displayed.")
        
        """
        Step 18:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()