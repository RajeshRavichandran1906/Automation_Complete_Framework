'''
Created on Dec 14, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2336431
TestCase Name : Verify PARTITION_REF function
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, define_compute, visualization_ribbon, ia_run
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report

class C2336431_TestClass(BaseTestCase):

    def test_C2336431(self):
        
        Test_Case_ID = "C2336431"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        defcomp_obj=define_compute.Define_Compute(self.driver)
        ia_run_obj=ia_run.IA_Run(self.driver)
        report = Report(self.driver)
#         ia_resultarea_obj=ia_resultarea.IA_Resultarea(self.driver)

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
            Step 02:Add fields "Product,Category" and "Product,Subcategory" from Product Dimension
            Step 03:Expand Measures > Shipments > Add field "Days,Delayed"
        """
        report.double_click_on_datetree_item("Product,Category", 1)
        report.wait_for_visible_text(query_css, "Product,Category")
        
        report.double_click_on_datetree_item("Product,Subcategory", 1)
        report.wait_for_visible_text(query_css, "Product,Subcategory")
        
        report.double_click_on_datetree_item("Days,Delayed", 1)
        report.wait_for_visible_text(query_css, "Days,Delayed")
         
        """ 
            Step 04:Select Dat Tab > Compute
        """
        defcomp_obj.invoke_define_compute_dialog('compute')
         
        """ 
            Step 05:Type name NEWDAYS > Change Format to I5
        """
        field_name = self.driver.find_element_by_id("fname")
        field_format = self.driver.find_element_by_id("fformat")
        utillobj.set_text_field_using_actionchains(field_name, "NEWDAYS", keyboard_type=True)
        utillobj.set_text_field_using_actionchains(field_format, "I5", keyboard_type=True)
             
        """
            Step 06:Copy/paste following syntax in the expession area:
            PARTITION_REF (WF_RETAIL_LITE.WF_RETAIL_SHIPMENTS.DAYSDELAYED, WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY, -1)
        """
        text_strings = "PARTITION_REF (WF_RETAIL_LITE.WF_RETAIL_SHIPMENTS.DAYSDELAYED, WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY, -1)"
        css_text=driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #fldCreatorSplitPane #ftext")
        utillobj.set_text_field_using_actionchains(css_text, text_strings, keyboard_type=True)
        time.sleep(2)
             
        """ 
            Step 07:Click OK
        """
        defcomp_obj.close_define_compute_dialog("ok")
        time.sleep(2)
          
        """
            Step 08:Verify Query pane and Live Preview
        """
        metaobj.verify_query_pane_field("Sum", "NEWDAYS", 2, "Step 08:01:")
        """ 
            Step 09:Right-click NEWDAYS in the Query pane > Edit Compute
        """
        metaobj.querytree_field_click("NEWDAYS", 1, 1)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("Edit Compute")
        parent_css="div[id^='QbDialog'] [class*='active']"
        resultobj.wait_for_property(parent_css, 1)
        """  
            Step 10:Verify expression showing field Titles > Click OK
        """
        css_text=driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #fldCreatorSplitPane #ftext")
        act_textarea_value=css_text.get_attribute("value").strip()
        textarea_value='PARTITION_REF ("Days,Delayed", "Product,Category", -1)'
        utillobj.asequal(act_textarea_value, textarea_value, "Step 10:01: Verify textarea displays the field title")
        defcomp_obj.close_define_compute_dialog("ok")
        time.sleep(2)
         
        """ 
            Step 11:Click Run > Verify output
        """
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
#         ia_run_obj.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds01.xlsx")
        ia_run_obj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds01.xlsx", 'Step 11:01: Verify report at runtime')
        utillobj.switch_to_default_content(pause=1)
         
        """ 
            Step 12:Click "Save" > Save As "C2336431" > Click Save
        """
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        report.wait_for_visible_text(cancel_css, "Cancel")
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
                 
        """ 
            Step 13:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """     
        utillobj.infoassist_api_logout()
        """ 
            Step 14:Reopen the saved fex:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2336431.fex&tool=report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10660_infoassist_2',mrid='mrid', mrpass='mrpass')
        parent_css= "#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """ 
            Step 15:Verify Query pane and Live Preview
        """
        metaobj.verify_query_pane_field("Sum", "NEWDAYS", 2, "Step 15:01:")
        coln_list = ['ProductCategory', 'ProductSubcategory', 'DaysDelayed', 'NEWDAYS']
        resultobj.verify_report_titles_on_preview(4, 8, "TableChart_1", coln_list, "Step 15:01: Verify column titles")
        
        """ 
            Step 16:Right-click NEWDAYS in the Query pane > Edit Compute
        """
        metaobj.querytree_field_click("NEWDAYS", 1, 1)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("Edit Compute")
        parent_css="div[id^='QbDialog'] [class*='active']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        """ 
            Step 17:Verify expression showing field Titles > Click Cancel
        """
        text_strings ='PARTITION_REF ( "Days,Delayed" , "Product,Category" , -1 )'
        css_text=driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #fldCreatorSplitPane #ftext")
        act_textarea_value=css_text.get_attribute("value").strip()
        utillobj.asequal(act_textarea_value, text_strings, "Step 17:01: Verify textarea displays the field title")
        time.sleep(0.5)
        defcomp_obj.close_define_compute_dialog("Cancel")
        """ 
            Step 18:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    unittest.main()