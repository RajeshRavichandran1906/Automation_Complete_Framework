'''
Created on Dec 7, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2235629
TestCase Name = Verify creating a Reporting Object with WHERE condition
'''

import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, wf_reporting_object, ia_resultarea, active_miscelaneous, ia_ribbon, wf_mainpage, wf_legacymainpage
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2235629_TestClass(BaseTestCase):

    def test_C2235629(self):
        
        Test_Case_ID = "C2235629"
        Test_Case_ID_DOC = "C2235629_DOC"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        wfreportobj = wf_reporting_object.Wf_Reporting_Object(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        iaribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        legacymainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        
        """
        Step 01 : Launch Reporting Object with wf_retail_lite::http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=reportingobject&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('reportingobject','new_retail/wf_retail_lite','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#applicationButton img[src*='reporting_objects']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(6)
                
        """
        Step 02 : Right-click "Where Statements" component > Select "New"
        """ 
        wfreportobj.select_ro_tree_item("Where Statements")
        time.sleep(2)
        wfreportobj.select_ro_tree_item("Where Statements",1,'New')
        time.sleep(5)
                
        """
        Step 03: Double-click where indicated in the Filter dialog > Select field "Product,Category"
        """
        ok_btn="#dlgWhere  #dlgWhere_btnOK"
        resultobj.wait_for_property(ok_btn, 1, expire_time=20)            
        time.sleep(2) 
        where_indicated=driver.find_element_by_css_selector("#dlgWhereWhereTree > div.bi-tree-view-body-content tbody > tr:nth-child(2) > td > span > span")
        utillobj.click_on_screen(where_indicated, 'left', click_type=2,pause=1)
        time.sleep(3)
               
        field_elem=self.driver.find_element_by_css_selector("#dlgWhere #dlgWhereWhereTree table tr:nth-child(2) span[class='selected lead']>span>span")
        utillobj.click_on_screen(field_elem, 'left', click_type=0,pause=1)
        time.sleep(3)
               
        field_ok_btn="#wndWhereFieldPopup_btnOK"
        resultobj.wait_for_property(field_ok_btn, 1, expire_time=20)            
        time.sleep(2) 
        wfreportobj.ro_where_filter_field_click("Product,Category", 1)
        value_elem=self.driver.find_element_by_css_selector("[id*='InlineControlValue'] div[class^='bi-button button']")
        utillobj.click_on_screen(value_elem, 'right',pause=1)
        utillobj.click_on_screen(value_elem, 'right', click_type=2,pause=1)
                
        """
        Step 04: Click Get Values > All
        Step 05: Double-click "Computers" and "Televisions" to add values to right panel
        Step 06: Click OK > OK
        """
        ok_btn="#wndWhereValuePopup_btnOK"
        resultobj.wait_for_property(ok_btn, 1, expire_time=20)     
        iaribbonobj.select_filter_values('constant', 'All', ['Computers', 'Televisions'])
        ok=driver.find_element_by_css_selector(ok_btn)
        utillobj.click_on_screen(ok, 'middle', click_type=0)
        time.sleep(2)
        iaribbonobj.close_filter_dialog(btn='ok')
        time.sleep(5) 
                
        """    
        Step 07: Right-click "Report" component > Open
        """
        wfreportobj.select_ro_tree_item("Report")
        time.sleep(2)
        wfreportobj.select_ro_tree_item("Report",1,'Open')
        time.sleep(5)
        utillobj.switch_to_window(1)
        time.sleep(8)
                
        """    
        Step 08: Double-click fields "Product,Category" and "Cost of Goods"
        """
        parent_css="[id^=QbMetaDataTree]"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
        time.sleep(2)
                
        metaobj.datatree_field_click("Product,Category", 2, 1)
        resultobj.wait_for_property("#TableChart_1  div[class^='x']", 4, expire_time=10) 
        time.sleep(3)    
                
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        resultobj.wait_for_property("#TableChart_1  div[class^='x']", 8, expire_time=10) 
        time.sleep(3)
                
        """    
        Step 09: Verify WHERE condition is applied
        """
        coln_list = ['ProductCategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 09.1: Verify report titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds01.xlsx", no_of_cells=4)
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 09.2: Verify report dataset', no_of_cells=4)
                
        """    
        Step 10: Select IA > Exit > click "Yes" to save
        """
        ribbonobj.select_tool_menu_item('menu_exit')
        time.sleep(5)
        self.driver.find_element_by_css_selector("div[id^='loginForm'] div[id*='saveChangesLabel']").is_displayed()
        btn_css="div[id*='loginForm'] div[class^='bi-button-label']"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('Yes')].click()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(5)
        parent_css="#applicationButton img[src*='reporting_objects']"
        resultobj.wait_for_property(parent_css, 1)
                
        """    
        Step 11: Right-click "Chart" component > Open
        """
        wfreportobj.select_ro_tree_item("Chart")
        time.sleep(2)
        wfreportobj.select_ro_tree_item("Chart",1,'Open')
        time.sleep(5)
        utillobj.switch_to_window(1)
        time.sleep(8)
                
        """    
        Step 12: Double-click fields "Product,Category" and "Cost of Goods"
        """
        parent_css="[id^=QbMetaDataTree]"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
        time.sleep(2)
                
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#TableChart_2 rect[class*='riser!']"
        resultobj.wait_for_property(parent_css, 2, expire_time=15)   
                
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        resultobj.wait_for_property("#TableChart_2 text[class='yaxis-title']", 1, expire_time=10, string_value='Cost of Goods')
               
        """    
        Step 13: Verify WHERE condition is applied
        """ 
        time.sleep(5)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 13:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 13:a(ii) Verify X-Axis Title")
        expected_xval_list=['Computers', 'Televisions']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M', '80M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step13.b:Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step13.c: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar!", "bar_blue", "Step13.d: Verify first bar color")
                
        """    
        Step 14: Select IA > Exit > click "Yes" to save
        """
        ribbonobj.select_tool_menu_item('menu_exit')
        time.sleep(5)
        self.driver.find_element_by_css_selector("div[id^='loginForm'] div[id*='saveChangesLabel']").is_displayed()
        btn_css="div[id*='loginForm'] div[class^=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('Yes')].click()
        time.sleep(6)
        utillobj.switch_to_window(0)
        time.sleep(5)
        parent_css="#applicationButton img[src*='reporting_objects']"
        resultobj.wait_for_property(parent_css, 1)
                
        """    
        Step 15: Click "RO" menu > Save As > "C2235629" > Click "Save"
        """
        time.sleep(2)
        wfreportobj.select_ro_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5) 
                
        """
        Step 16: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
              
        """
        Step 17: Reopen saved RO: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2235629.fex&tool=reportingobject
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'reportingobject', 'S10032_infoassist_4',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
              
        """
        Step 18: Verify restore and filter: Expand "Where Statements" > Verify Where_1 component is present
        """
        parent_css="#applicationButton img[src*='reporting_objects']"
        resultobj.wait_for_property(parent_css, 1)
        wfreportobj.select_ro_tree_item('Where Statements') 
        wfreportobj.select_ro_tree_item('Where Statements', click_type=2)
        time.sleep(3)
        ro_tool_name=['Reporting Object', 'Preprocessing Other', 'Joins', 'Defines', 'Filters', 'Where Statements', 'Where_1', 'Report', 'Chart', 'Postprocessing Other']
        wfreportobj.verify_ro_tree_item(ro_tool_name,"Step 18: Verify Where_1 component is present")
              
        """
        Step 19: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
          
        """
        Step 20: Logon to WF: http://machine:port/ibi_apps/
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        time.sleep(8)
          
        """
        Step 21: Expand folder "S10032" > Right-click "C2235629" > New > Document
        """
#         if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst04','wfinst05'):
#             mainobj.select_repository_folder_item_menu('P292->S10032_infoassist_4','C2235629','New->Document')
#         else:
        legacymainobj.select_repository_menu('P292->S10032_infoassist_4->C2235629', 'New->Document')
        time.sleep(6)
        utillobj.switch_to_window(1)
        time.sleep(5)
           
        """
        Step 22: Verify Canvas
        """
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        coln_list = ['ProductCategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 22.1: Verify report titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 22.2: Verify report dataset', no_of_cells=4)
        parent_css="#TableChart_2"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 22:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 22:a(ii) Verify X-Axis Title")
        expected_xval_list=['Computers', 'Televisions']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M', '80M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step22.b:Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step22.c: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar!", "bar_blue", "Step22.d: Verify first bar color")
           
        canvas_width=driver.find_element_by_css_selector("#theCanvas")
        a=canvas_width.size['width']
        print("a:",a)
          
        """
        Step 23: Select Layout Tab > Click Orientation > Landscape
        """ 
        ribbonobj.select_ribbon_item('Layout', 'orientation', opt='Landscape')
        time.sleep(10) 
          
        """
        Step 24: Verify Canvas
        """
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        coln_list = ['ProductCategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 24.1: Verify report titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 24.2: Verify report dataset', no_of_cells=4)
        time.sleep(5)
        parent_css="#TableChart_2"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.verify_object_visible(parent_css, True, 'Step 24.3: Verify chart is displayed')
        b=canvas_width.size['width']
        print("b:",b)
        c=b>a
        utillobj.asequal(c,True,"Step 24.e: Landscape applied in canvas")
          
        """
        Step 25: Click on the Chart component > resize component from the corners to make component smaller and drag next to Report component
        """ 
        source_elem = driver.find_element_by_css_selector("#TableChart_2")
        target_elem = driver.find_element_by_css_selector("#TableChart_1")
        utillobj.click_on_screen(source_elem, 'start', x_offset=10, y_offset=10)
        utillobj.click_on_screen(source_elem, 'start', click_type=0, x_offset=10, y_offset=10)
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            offset_value = 5
        else:
            offset_value = 7
        utillobj.drag_drop_using_uisoup(source_elem, target_elem, src_cord_type='start', trg_cord_type='top_right', sx_offset=20, tx_offset=20, sy_offset=offset_value)
           
        """    
        Step 26: Select Insert Tab > Click "Report"
        """
        time.sleep(5)
        ribbonobj.select_ribbon_item('Insert', 'Report')
           
        """    
        Step 27: Double-click fields "Product,Category", "Product,Subcategory" and "Cost of Goods"
        """
        parent_css="[id^=QbMetaDataTree]"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
        time.sleep(2)
            
        metaobj.datatree_field_click("Product,Category", 2, 1)
        resultobj.wait_for_property("#TableChart_3  div[class^='x']", 4, expire_time=10) 
        time.sleep(3)    
            
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        resultobj.wait_for_property("#TableChart_3  div[class^='x']", 11, expire_time=10) 
        time.sleep(3)    
            
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        resultobj.wait_for_property("#TableChart_3  div[class^='x']", 18, expire_time=15) 
        time.sleep(3)
           
        """    
        Step 28: Verify WHERE condition is applied to the new Report component
        """
        coln_list = ['ProductCategory', 'ProductSubcategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_3", coln_list, "Step 28.1: Verify report titles")
        ia_resultobj.verify_report_data_set('TableChart_3', 5, 3, Test_Case_ID+"_Ds02.xlsx", 'Step 28.2: Verify report dataset', no_of_cells=6)
        time.sleep(3)
           
        """
        Step 29: Drag the new Report component under the existing Report component
        """ 
        source_elem = driver.find_element_by_css_selector("#TableChart_3")
        target_elem = driver.find_element_by_css_selector("#TableChart_1")
        utillobj.click_on_screen(source_elem, 'start', x_offset=10, y_offset=10)
        utillobj.click_on_screen(source_elem, 'start', click_type=0, x_offset=10, y_offset=10)
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            offset_value = 5
        else:
            offset_value = 7
        utillobj.drag_drop_using_uisoup(source_elem, target_elem, src_cord_type='start', trg_cord_type='bottom_left', sx_offset=20, ty_offset=20, sy_offset=offset_value)
           
        """
        Step 30: Click Save in the toolbar > Save As "C2235629_DOC" > Click Save
        """
        time.sleep(8)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID_DOC)
        time.sleep(3)
           
        """    
        Step 31: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(2)
         
        """
        Step 32: Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2235629_DOC.fex&tool=Document
        """
        utillobj.infoassist_api_edit(Test_Case_ID_DOC, 'Document', 'S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(10)
         
        """
        Step 33: Verify successful restore
        """
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        coln_list = ['ProductCategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 33.1: Verify report titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 33.2: Verify report dataset', no_of_cells=4)
        time.sleep(5)
        parent_css="#TableChart_2"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 33:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 33:a(ii) Verify X-Axis Title")
        expected_xval_list=['Computers', 'Televisions']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M', '80M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step33.b:Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step33.c: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar!", "bar_blue", "Step33.d: Verify first bar color")
         
        parent_css="#TableChart_3"
        resultobj.wait_for_property(parent_css, 1) 
        coln_list = ['ProductCategory', 'ProductSubcategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_3", coln_list, "Step 33.1: Verify report titles")
        ia_resultobj.verify_report_data_set('TableChart_3', 5, 3, Test_Case_ID+"_Ds02.xlsx", 'Step 33.2: Verify report dataset', no_of_cells=6)
 
        """
        Step 34: Click Run > Verify output
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2) 
        
        time.sleep(5)
        miscelaneousobj.verify_page_summary('0','2of2records,Page1of1', 'Step 34.1.a: Verify report1 Page summary')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_run_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_run_Ds01.xlsx', "Step 34.1.b: Verify report1")
        
        time.sleep(5) 
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 34:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 34:a(ii) Verify X-Axis Title")
        expected_xval_list=['Computers', 'Televisions']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M', '80M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step34.b:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step34.c: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step34.d: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody1","Cost of Goods BY Product Category", "Step 34.e : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 34.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step34.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 34.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 34.i: verify the default tooltip values')
        
        time.sleep(5)
        miscelaneousobj.verify_page_summary('2','5of5records,Page1of1', 'Step 34.2.a: Verify Page summary')
#         utillobj.create_data_set('ITableData2', 'I2r', Test_Case_ID+'_run_Ds02.xlsx')
        utillobj.verify_data_set('ITableData2', 'I2r', Test_Case_ID+'_run_Ds02.xlsx', "Step 34.2.b: Verify report2")
        
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#orgdiv0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step34', image_type='actual',x=1, y=1, w=-1, h=-1)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        
        """
        Step 35: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()