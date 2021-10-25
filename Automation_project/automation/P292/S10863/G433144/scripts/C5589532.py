'''
Created on May 16, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5589532
TestCase Name = Verify changing order of DEFINE fields 
'''
import time, keyboard
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, define_compute, visualization_ribbon, ia_resultarea
from common.lib.basetestcase import BaseTestCase

class C5589532_TestClass(BaseTestCase):

    def test_C5589532(self):
        
        Test_Case_ID = "C5589532"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        defcomp_obj=define_compute.Define_Compute(self.driver)
        iaresult= ia_resultarea.IA_Resultarea(self.driver)
        
        """ 
        Step 01 : Launch Report with car:
        http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/car&item=IBFS:/WFC/Repository/S10863
        """
        utillobj.invoke_infoassist_api_login('Report','ibisamp/car','P292_S10863/G433144', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 02 : Select Data Tab > Define
        """
        defcomp_obj.invoke_define_compute_dialog('define')
        parent_css="#fname"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 03: Add expression: RETAIL_COST - DEALER_COST
        """
        defcomp_obj.select_define_compute_field('Measures/Properties->RETAIL_COST', 1)
        time.sleep(2)
        defcomp_obj.select_calculation_btns(btn_series="minus")
        time.sleep(2)
        defcomp_obj.select_define_compute_field('Measures/Properties->DEALER_COST', 1)
        time.sleep(2)
         
        """
        Step 04: Click OK to create Define_1
        """
        defcomp_obj.close_define_compute_dialog('ok')
        time.sleep(4)
        
        """
        Step 05: Select Data Tab > Define
        """
        defcomp_obj.invoke_define_compute_dialog('define')
        parent_css="#fname"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 06: Add "DEALER_COST" to expression area > Click OK to create field Define_2
        """
        defcomp_obj.select_define_compute_field('Measures/Properties->DEALER_COST', 1)
        time.sleep(2)
        defcomp_obj.close_define_compute_dialog('ok')
        time.sleep(4)
        
        """
        Step 07: Select Data Tab > Define
        """
        defcomp_obj.invoke_define_compute_dialog('define')
        parent_css="#fname"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 08: Add "RETAIL_COST" to expression area > Click OK to create field Define_3
        """
        defcomp_obj.select_define_compute_field('Measures/Properties->RETAIL_COST', 1)
        time.sleep(2)
        defcomp_obj.close_define_compute_dialog('ok')
        time.sleep(4)
        
        """
        Step 09: Select View Source
        Step 10: View Source and verify DEFINE syntax generated as:
                DEFINE FILE ibisamp/car
                Define_1/D12.2=RETAIL_COST - DEALER_COST;
                Define_2/D12.2=CAR.BODY.DEALER_COST ;
                Define_3/D12.2=CAR.BODY.RETAIL_COST ;
                END
        """
        expected_syntax_list=["DEFINE FILE ibisamp/car","Define_1/D12.2=CAR.BODY.RETAIL_COST - CAR.BODY.DEALER_COST ;", "Define_2/D12.2=CAR.BODY.DEALER_COST ;","Define_3/D12.2=CAR.BODY.RETAIL_COST ;","END"]
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 10.1 : View Source and verify DEFINE syntax generated')
        
        """
        Step 11: Right-click Define_1 in the Data pane > Edit...
        """
        metaobj.datatree_field_click('Measures/Properties->Define_1', 1, 0, 'Edit...')
        parent_css="#fname"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 12: Change expression to: Define_3 - DEALER_COST
        """
        txt_ele = driver.find_element_by_id("ftext")
        utillobj.click_on_screen(txt_ele, 'middle')
        utillobj.click_on_screen(txt_ele, 'middle', click_type=0)
        time.sleep(3)
        keyboard.press('ctrl')
        keyboard.press('a')
        keyboard.release('a')
        keyboard.release('ctrl')
        time.sleep(3)
        keyboard.send('del')
        time.sleep(3)
        defcomp_obj.select_define_compute_field('Measures/Properties->Define_3', 1)
        time.sleep(2)
        defcomp_obj.select_calculation_btns(btn_series="minus")
        time.sleep(2)
        defcomp_obj.select_define_compute_field('Measures/Properties->DEALER_COST', 1)
        time.sleep(2)
        
        """
        Step 13: Click OK
        """
        defcomp_obj.close_define_compute_dialog('ok')
        time.sleep(4)
        
        """
        Step 14: Verify DEFINE syntax is reordered:
        DEFINE FILE ibisamp/car
        Define_2/D12.2=CAR.BODY.DEALER_COST ;
        Define_3/D12.2=CAR.BODY.RETAIL_COST ;
        Define_1/D12.2=Define_3 - DEALER_COST;
        END
        """
        expected_syntax_list=["DEFINE FILE ibisamp/car","Define_2/D12.2=CAR.BODY.DEALER_COST ;", "Define_3/D12.2=CAR.BODY.RETAIL_COST ;","Define_1/D12.2=Define_3 - CAR.BODY.DEALER_COST ;","END"]
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 10.1 : View Source and verify DEFINE syntax generated')
        time.sleep(4)
        
        """
        Step 15: Add fields: Define_1, Define_2, Define_3
        """
        metaobj.datatree_field_click("Measures/Properties->Define_1", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Measures/Properties->Define_2", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Measures/Properties->Define_3", 2, 1)
        time.sleep(5)
        
        coln_list = ['Define_1', 'Define_2', 'Define_3']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 15.1: Verify report titles")
#         iaresult.create_report_data_set('TableChart_1', 1, 3, Test_Case_ID+"_Ds01.xlsx")
        iaresult.verify_report_data_set('TableChart_1', 1, 3, Test_Case_ID+"_Ds01.xlsx", "Step 15.2: Verify live preview data")
        
        """
        Step 16: Select Save > Save as "C5589532" > Save
        """
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
        Step 17: Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 18: Reopen saved FEX:
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/S10863/C5589532.fex&tool=Report
        """
        utillobj.infoassist_api_edit_(Test_Case_ID, 'report', 'P292_S10863/G433144',mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 19: Verify Query pane and Live Preview
        """
        metaobj.verify_query_pane_field('Sum', "Define_1", 1, "Step 19.1")
        metaobj.verify_query_pane_field('Define_1', "Define_2", 1, "Step 19.2")
        metaobj.verify_query_pane_field('Define_2', "Define_3", 1, "Step 19.3")
        
        coln_list = ['Define_1', 'Define_2', 'Define_3']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 19:04: Verify report titles")
        iaresult.verify_report_data_set('TableChart_1', 1, 3, Test_Case_ID+"_Ds01.xlsx", "Step 19.5: Verify live preview data")
        
        """
        Step 20: Verify order of Defines in the Data pane
        """
        metaobj.verify_data_pane_field('ACCEL', 'Define_2', 1, "Step 20.1")
        metaobj.verify_data_pane_field('Define_2', 'Define_3', 1, "Step 20.2")
        metaobj.verify_data_pane_field('Define_3', 'Define_1', 1, "Step 20.3")
        
        """
        Step 21: Select View Source > Verify syntax order remains as:
        DEFINE FILE ibisamp/car
        Define_2/D12.2=CAR.BODY.DEALER_COST ;
        Define_3/D12.2=CAR.BODY.RETAIL_COST ;
        Define_1/D12.2=Define_3 - DEALER_COST ;
        END
        """
        expected_syntax_list=["DEFINE FILE ibisamp/car","Define_2/D12.2=CAR.BODY.DEALER_COST ;", "Define_3/D12.2=CAR.BODY.RETAIL_COST ;","Define_1/D12.2=Define_3 - CAR.BODY.DEALER_COST ;","END"]
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 21: View Source and verify DEFINE syntax generated')
        
        """
        Step 22: Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """