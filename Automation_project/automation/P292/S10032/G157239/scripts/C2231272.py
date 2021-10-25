'''
Created on Dec 05, 2017

@author: Praveen Ramkumar
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2231272
Testcase Name : Verify Preview context menus 
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon, ia_run
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase


class C2231272_TestClass(BaseTestCase):

    def test_C2231272(self):
        
        TestCase_ID = "C2231272"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        
        
        """
            Step 01: Launch IA Report mode with wf_retail_lite:
            http://machine:port/ibi_apps/ia?tool=report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
         
        """
            Step 02: Double-click "Product,Category"
        """
         
        metaobj.datatree_field_click('Product,Category', 2, 0)
         
        """
            Step 03: Drag and drop "Product,Category" from the Query pane into the Filter panel Filter Values...
        """
         
        metaobj.querytree_field_click("Product,Category",1,1,"Filter Values...")
         
         
        """
            Step 04: Select Get Values > All
            Step 05: Double-click values "Computers" and "Televisions"
            Step 06: Click OK > OK
        """
        parent_css="#dlgWhere  #dlgWhere_btnOK"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)            
        time.sleep(2)
        ia_ribbobj.create_constant_filter_condition('All', ['Computers', 'Televisions'])
        time.sleep(10)
         
        """
            Step 07: Verify Preview
        """
        metaobj.verify_filter_pane_field('Product,Category Equal to Computers or Televisions',1,"Step25:")  
        time.sleep(10)
        #ia_resultobj.create_across_report_data_set('TableChart_1', 2,1,2,1,TestCase_ID+'_DataSet_07.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,1,2,1,TestCase_ID+'_DataSet_07.xlsx','Step 07: Verify report')
         
        """
            Step 08:Select the Home Tab > Click "File" > Select format "SQL Script" > Click "Save"
        """
         
        ribbonobj.select_ribbon_item('Home', 'File')
        utillobj.ibfs_save_as("File1", "SQL Script (*.sql)")

        """
            Step 09:Click "Create Report" at the bottom
            Step 10:Verify canvas
        """
        elem=self.driver.find_element_by_css_selector("#createFromHoldButton")
        utillobj.click_on_screen(elem, 'middle', click_type=2)
        parent_css="#TableChart_2"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        metaobj.verify_query_pane_field('Files','File1 (wf_retail_lite)',1,"Step 10.1: Verify query pane")
        metaobj.verify_query_pane_field('Report (File1)','Sum',1,"Step 10.2: Verify query pane")
        metaobj.verify_query_pane_field('Report (File1)','By',2,"Step 10.3: Verify query pane")
        metaobj.verify_query_pane_field('Report (File1)','Across',3,"Step 10.4: Verify query pane")
         
        """
            Step 11:Select Data Tab > Click "Switch" > Select wf_retail_lite
            Step 12:Double-click fields "Revenue" and "Product,Category"
        """
         
        ribbonobj.select_ribbon_item('Data','switch',opt='baseapp/wf_retail_lite')
        metaobj.datatree_field_click('Revenue', 2, 0)
        metaobj.datatree_field_click('Product,Category', 2, 0)
         
        """
            Step 13:Drag and drop "Store,Business,Region" into "Across" container in the Query pane
            Step 14:Verify Preview and Query pane
        """
         
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Business,Region', 1, 'Across',0)
        parent_css='#queryTreeWindow tr:nth-child(9) td'
        resultobj.wait_for_property(parent_css, 1,string_value='Store,Business,Region',expire_time=15)
        metaobj.verify_query_pane_field('Files','File1 (wf_retail_lite)',1,"Step 13.1: Verify query pane")
        metaobj.verify_query_pane_field('Report (wf_retail_lite)','Sum',1,"Step 13.2: Verify query pane")
        metaobj.verify_query_pane_field('Sum','Revenue',1,"Step 13.3: Verify query pane")
        metaobj.verify_query_pane_field('By','Product,Category',1,"Step 13.4: Verify query pane")
        metaobj.verify_query_pane_field('Across','Store,Business,Region',1,"Step 13.4: Verify query pane")
         
        """
            Step 15:Select Data Tab > Click "Filter" > Double-click where indicated
            Step 16:Select Type:Subquery > "In list"
            Step 17:Click <Subquery> then select "File1" from the menu > Click OK
        """
        ribbonobj.select_ribbon_item('Data','Filter')
        obj_locator=driver.find_element_by_css_selector("#dlgWhereWhereTree > div.bi-tree-view-body-content tbody > tr:nth-child(2) > td > span > span")
        utillobj.click_on_screen(obj_locator, 'middle', click_type=2)
        time.sleep(3)
        condition_elem=self.driver.find_element_by_css_selector("#dlgWhere #dlgWhereWhereTree table tr:nth-child(2) span[class='selected lead']>span>span")
        utillobj.click_on_screen(condition_elem, 'left', click_type=0)
        utillobj.click_on_screen(condition_elem, 'left', click_type=2)
        time.sleep(3)
        utillobj.select_combobox_item("id_where_field_subquery_type_combo", "Subquery")
#         utillobj.select_or_verify_bipop_menu('In list')

        css="div[id*='InlineControlSubqueryValue']"
        elem=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(elem, 'left', click_type=0)
        utillobj.select_or_verify_bipop_menu('File1')
        
        btnok=driver.find_element_by_id('dlgWhere_btnOK')
        utillobj.default_left_click(object_locator=btnok)
        time.sleep(8)
        
        """
            Step 18:Verify Preview
            Step 19:Click Run > Verify output
            Step 20:Close the output
            Step 21:Click Save > Save As "C2223508" > Click Save
        """
        browser=utillobj.parseinitfile('browser')
        if browser == 'Firefox':
#             ia_resultobj.create_across_report_data_set('TableChart_2', 3,5,2,5,TestCase_ID+'_DataSet_18_'+browser+'.xlsx')
            ia_resultobj.verify_across_report_data_set('TableChart_2',3,5,2,5,TestCase_ID+'_DataSet_18_'+browser+'.xlsx','Step 18: Verify Preview report')
        else:
#             ia_resultobj.create_across_report_data_set('TableChart_2', 3,5,2,5,TestCase_ID+'_DataSet_18.xlsx')
            ia_resultobj.verify_across_report_data_set('TableChart_2',3,5,2,5,TestCase_ID+'_DataSet_18.xlsx','Step 18: Verify report')
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
#         ia_runobj.create_table_data_set("table[summary='Summary']",TestCase_ID+'_Ds19.xlsx') 
        ia_runobj.verify_table_data_set("table[summary='Summary']",TestCase_ID+"_Ds19.xlsx", 'Step 19: Verify HTML format report After Run')
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(TestCase_ID)
        time.sleep(8)
        
        """
            Step 22:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
            Step 23:Reopen FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2223508.fex&tool=report
        """
        
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """            
            Step 23:Reopen FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2223508.fex&tool=report
        """
        
        utillobj.infoassist_api_edit(TestCase_ID,'Report', 'P292/S10032_infoassist_4',mrid='mrid',mrpass='mrpass')
        time.sleep(8)
        
        
        """
            Step 24:Verify Preview and successful restore
            
        """
        
#         ia_resultobj.create_across_report_data_set('TableChart_2', 3,5,2,5,TestCase_ID+'_DataSet_24.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_2',3,5,2,5,TestCase_ID+'_DataSet_24.xlsx','Step 24: Verify report')
        
        """
            Step 25:Verify Preview and successful restore            
        """
        
        metaobj.querytree_field_click("File1 (wf_retail_lite)",1,1,"Edit")
        time.sleep(2)
        
        """
            Step 26:Verify Preview and successful restore            
        """        
  
        metaobj.verify_query_pane_field('By','Product,Category',1,"Step 26.1: Verify query pane")
        metaobj.verify_filter_pane_field('Product,Category Equal to Computers or Televisions',1,"Step 26.2: Verify Product,Category Equal to Computers or Televisions appears in filter pane")
        
        """
            Step 27:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp       
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()  
        