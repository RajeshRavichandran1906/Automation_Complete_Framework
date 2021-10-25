'''
Created on Dec 15, 2017
@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2336431
TestCase Name : Verify PARTITION_AGGR function 8202 New Features and product changes for existing functionality Infoassist - Computes
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, define_compute, visualization_ribbon, ia_run, ia_resultarea
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report

class C2336432_TestClass(BaseTestCase):

    def test_C2336432(self):
        
        Test_Case_ID = "C2336432"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        defcomp_obj=define_compute.Define_Compute(self.driver)
        ia_run_obj=ia_run.IA_Run(self.driver)
        iaresultobj=ia_resultarea.IA_Resultarea(self.driver)
        define = define_compute.DefineCompute(self.driver)
        report = Report(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        live_preview_css = "#TableChart_1"
        query_css = "#queryBoxColumn"
        cancel_css = "#IbfsOpenFileDialog7_btnCancel"
        
        """
        Step 01:Launch Report mode:
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        report.wait_for_visible_text(live_preview_css, "Drag and drop")
        
        """  
        Step 02:Expand Dimension "Customer" > Add field "Customer,Business,Region"
        Step 03:Expand Dimension "Sales_Related" > "Transaction Date, Simple" > Add fields "Sale,Quarter" and "Sale,Month"
        Step 04:Expand Measures "Sales" > Add field "Cost of Goods"
        """
        report.double_click_on_datetree_item("Customer,Business,Region", 1)
        report.wait_for_visible_text(query_css, "Customer,Business,Region")
        
        report.double_click_on_datetree_item("Sale,Quarter", 1)
        report.wait_for_visible_text(query_css, "Sale,Quarter")
        
        report.double_click_on_datetree_item("Sale,Month", 1)
        report.wait_for_visible_text(query_css, "Sale,Month")
        
        report.double_click_on_datetree_item("Cost of Goods", 1)
        report.wait_for_visible_text(query_css, "Cost of Goods")
        
        """  
        Step 05:Select Data Tab > Compute
        """
        defcomp_obj.invoke_define_compute_dialog('compute')
        
        """  
        Step 06:Type name "RollingAverage" > Change Format to D12.2M
        """
        field_name = self.driver.find_element_by_id("fname")
        field_format = self.driver.find_element_by_id("fformat")
        utillobj.set_text_field_using_actionchains(field_name, "RollingAverage", keyboard_type=True)
        utillobj.set_text_field_using_actionchains(field_format, "D12.2M", keyboard_type=True)
        
        """  
        Step 07:Copy/paste following syntax in expression area:
        PARTITION_AGGR ( "Cost of Goods" , "Sale,Quarter" , -1 , C , AVE )
        """
        text_strings = 'PARTITION_AGGR ( "Cost of Goods" , "Sale,Quarter" , -1 , C , AVE )'
        css_text=driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #fldCreatorSplitPane #ftext")
        utillobj.set_text_field_using_actionchains(css_text, text_strings, keyboard_type=True)
        time.sleep(3)
        
        """ 
        Step 08:Click OK
        """
        define.click_ok_button()
        resultobj.wait_for_property("#queryTreeColumn div[class='bi-tree-view-body-content']>table>tbody>tr:nth-child(4)", 1, expire_time=20, string_value='RollingAverage') 
        
        """  
        Step 09:Verify Query pane and Live Preview
        """
        metaobj.verify_query_pane_field("Sum", "RollingAverage", 2, "Step 09:01:")
        time.sleep(8)
#         iaresultobj.create_across_report_data_set('TableChart_1', 3, 5, 12, 5, Test_Case_ID+"_Ds02.xlsx")
        iaresultobj.verify_across_report_data_set('TableChart_1', 3, 5, 12, 5, Test_Case_ID+"_Ds02.xlsx", "Step 09.02: Verify Live Preview")
        
        """ 
        Step 10:Right-click "RollingAverage" in the Query pane > Edit Compute
        """
        metaobj.querytree_field_click("RollingAverage", 1, 1)
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu("Edit Compute")
        parent_css="div[id^='QbDialog'] [class*='active']"
        resultobj.wait_for_property(parent_css, 1)
        
        """  
        Step 11:Verify expression displays field Titles
        """
        css_text=driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #fldCreatorSplitPane #ftext")
        act_textarea_value=css_text.get_attribute("value").strip()
        textarea_value='PARTITION_AGGR ( "Cost of Goods" , "Sale,Quarter" , -1 , C , AVE )'
        utillobj.asequal(act_textarea_value, textarea_value, "Step 11:01: Verify textarea displays the field title")
        time.sleep(3)
           
        """ 
        Step 12:Click OK
        """
        define.click_ok_button()
        time.sleep(2)
        
        """  
        Step 13:Click Run > Verify output
        """
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        ia_run_obj.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds01.xlsx")
        ia_run_obj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds01.xlsx", 'Step 13:01: Verify report at runtime')
        utillobj.switch_to_default_content(pause=1)
        
        """ 
        Step 14:Click "Save" > Save As "C2336432" > Click Save
        """
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        report.wait_for_visible_text(cancel_css, "Cancel")
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """  
        Step 15:Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()  
         
        """  
        Step 16:Reopen the saved fex:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2336432.fex&tool=report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10660_infoassist_2',mrid='mrid', mrpass='mrpass')
        parent_css= "#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        
        """  
        Step 17:Verify Query pane and Live Preview
        """
        time.sleep(5)
        metaobj.verify_query_pane_field("Sum", "RollingAverage", 2, "Step 15:01:")
        coln_list = ['CustomerBusinessRegion', 'SaleQuarter', 'SaleMonth', 'Cost of Goods', 'RollingAverage']
        resultobj.verify_report_titles_on_preview(5, 15, "TableChart_1", coln_list, "Step 17:01: Verify column titles")
        
        """ 
        Step 18:Right-click "RollingAverage" in the Query pane > Edit Compute
        """
        metaobj.querytree_field_click("RollingAverage", 1, 1)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("Edit Compute")
        parent_css="div[id^='QbDialog'] [class*='active']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        
        """  
        Step 19:Verify expression displays field Titles
        """
        text_strings ='PARTITION_AGGR ( "Cost of Goods" , "Sale,Quarter" , -1 , C , AVE )'
        css_text=driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #fldCreatorSplitPane #ftext")
        act_textarea_value=css_text.get_attribute("value").strip()
        utillobj.asequal(act_textarea_value, text_strings, "Step 19:01: Verify textarea displays the field title")
        time.sleep(5)
        
        """ 
        Step 20:Click Cancel
        """
        define.click_cancel_button()
        time.sleep(4)
           
        """  
        Step 21:Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    unittest.main()