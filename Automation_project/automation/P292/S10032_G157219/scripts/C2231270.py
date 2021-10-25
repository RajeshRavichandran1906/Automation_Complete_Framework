'''
Created on Dec 26, 2017

@author: BM13368
TestCse ID :
TestCase Name :
TestCase Suite :
'''

import unittest, time, re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, wf_reporting_object, ia_resultarea, active_miscelaneous, ia_ribbon, wf_legacymainpage, ia_run
from common.lib import utillity

class C2231270_TestClass(BaseTestCase):

    def test_C2231270(self):
        
        """   
            TESTCASE VARIABLES 
        """
        
        Test_Case_ID = 'C2231270'
        Test_Case_ID1='C2231270_DOC'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarunobj = ia_run.IA_Run(self.driver)
        ia_result_obj = ia_resultarea.IA_Resultarea(self.driver)
        wfreportobj = wf_reporting_object.Wf_Reporting_Object(self.driver)
        ia_ribbon_obj = ia_ribbon.IA_Ribbon(self.driver)
        legacymainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)                                                      
        browser = utillobj.parseinitfile('browser')
        """
            Step 01:Launch Reporting Object with wf_retail_lite:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=reportingobject&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('reportingobject','new_retail/wf_retail_lite','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#applicationButton img[src*='reporting_objects']"
        resultobj.wait_for_property(parent_css, 1)
            
        """  
            Step 02:Right-click "Filters" component > Select "New" > Type "Product" > OK
        """
        wfreportobj.select_ro_tree_item("Filters")
        time.sleep(2)
        wfreportobj.select_ro_tree_item("Filters",1,'New')
        parent_css=self.driver.find_element_by_css_selector("#promptDlg")
        resultobj.wait_for_property(parent_css, 1)
        wfreportobj.ro_create_filter_group("Product", "Step 02:01: Verify the given input value is valid")
        """  
            Step 03:Right-click "Product" under Filters > Select "New" > Type "Product Category" > OK
        """
        
        wfreportobj.select_ro_tree_item("Product")
        time.sleep(1)
        wfreportobj.select_ro_tree_item("Product",1,'New')
        parent_css=self.driver.find_element_by_css_selector("#promptDlg")
        resultobj.wait_for_property(parent_css, 1)
        wfreportobj.ro_create_filter_group("Product,Category", "Step 04:01: Verify the given input value is valid")
        """  
            Step 04:Double-click where indicated in the Filter dialog > Select field "Product,Category"
        """
        ok_btn="#dlgWhere  #dlgWhere_btnOK"
        resultobj.wait_for_property(ok_btn, 1, expire_time=20)
        time.sleep(2) 
        where_indicated=self.driver.find_element_by_css_selector("#dlgWhereWhereTree > div.bi-tree-view-body-content tbody > tr:nth-child(2) > td > span > span")
        utillobj.click_on_screen(where_indicated, 'left', click_type=2,pause=1)
        time.sleep(3)
               
        field_elem=self.driver.find_element_by_css_selector("#dlgWhere #dlgWhereWhereTree table tr:nth-child(2) span[class='selected lead']>span>span")
        utillobj.click_on_screen(field_elem, 'left', click_type=0,pause=1)
        time.sleep(3)
               
        field_ok_btn="#wndWhereFieldPopup_btnOK"
        resultobj.wait_for_property(field_ok_btn, 1, expire_time=20)            
        wfreportobj.ro_where_filter_field_click("Product,Category", 1)
        value_elem=self.driver.find_element_by_css_selector("[id*='InlineControlValue'] div[class^='bi-button button']")
        utillobj.click_on_screen(value_elem, 'right',pause=1)
        utillobj.click_on_screen(value_elem, 'right', click_type=2,pause=1)
        """  
            Step 05:Click Get Values > All
        """
        ok_btn="#wndWhereValuePopup_btnOK"
        resultobj.wait_for_property(ok_btn, 1, expire_time=20)   
        """
            Step 06:Double-click "Computers" and "Televisions" to add values to right panel
        """  
        ia_ribbon_obj.select_filter_values('constant', 'All', ['Computers', 'Televisions'])
        ok=self.driver.find_element_by_css_selector(ok_btn)
        utillobj.click_on_screen(ok, 'middle', click_type=0)
        time.sleep(2)
        
        """ 
            Step 07:Click OK > OK
        """
        ia_ribbon_obj.close_filter_dialog(btn='ok')
        time.sleep(5)
        """  
            Step 08:Right-click "Report" component > Open
        """
        wfreportobj.select_ro_tree_item("Report")
        time.sleep(2)
        wfreportobj.select_ro_tree_item("Report",1,'Open')
        time.sleep(5)
        utillobj.switch_to_window(1)
        time.sleep(8)
        """  
            Step 09:Double-click fields "Product,Category" and "Cost of Goods"
        """
        parent_css="[id^=QbMetaDataTree]"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
                
        metaobj.datatree_field_click("Product,Category", 2, 1)
        resultobj.wait_for_property("#TableChart_1  div[class^='x']", 4, expire_time=20) 
                
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        resultobj.wait_for_property("#TableChart_1  div[class^='x']", 8, expire_time=20)
        """
            Verify report data at live preview
        """
        coln_list = ['ProductCategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 09:011: Verify report titles")
        ia_result_obj.create_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds01.xlsx", no_of_cells=4)
        ia_result_obj.verify_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 09:02: Verify report dataset', no_of_cells=4)
        
        """ 
            Step 10:Select IA > Exit > click "Yes" to save
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
            Step 11:Right-click "Chart" component > Open
        """
        wfreportobj.select_ro_tree_item("Chart")
        time.sleep(1)
        wfreportobj.select_ro_tree_item("Chart",1,'Open')
        time.sleep(5)
        utillobj.switch_to_window(1)
        """  
            Step 12:Double-click fields "Product,Category" and "Cost of Goods"
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
            Verify the created chart shows cost of goods and Product Category values
        """
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 12:01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 12:02: Verify X-Axis Title")
        expected_xval_list=['Computers', 'Televisions']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M', '80M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step 12:03: Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step 12:04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar!", "bar_blue", "Step 12:05: Verify first bar color")
        """
            Step 13:Select IA > Exit > click Yes to save
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
            Step 14:Click "RO" menu > Save As > "C2231270" > Click "Save"
        """
        wfreportobj.select_ro_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)    
        """  
            Step 15:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        """  
            Step 16:Reopen saved RO:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2231270.fex&tool=reportingobject
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'reportingobject', 'S10032_infoassist_4',mrid='mrid',mrpass='mrpass')
        
        """  
            Step 17:Verify restore and filter:
            Expand Filters > Product > Product Category
        """
        parent_css="#applicationButton img[src*='reporting_objects']"
        resultobj.wait_for_property(parent_css, 1)
        wfreportobj.select_ro_tree_item('Filter') 
        wfreportobj.select_ro_tree_item('Filter', click_type=2)
        time.sleep(3)
        ro_tool_name=['Reporting Object', 'Preprocessing Other', 'Joins', 'Defines', 'Filters', 'Product', 'Product,Category', 'Where Statements', 'Report', 'Chart', 'Postprocessing Other']
        wfreportobj.verify_ro_tree_item(ro_tool_name,"Step 17: Verify Where_1 component is present")
        """ 
            Step 18:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
            Step 19:Logon to WF:''Using Api calls onetime logout only will happen
            http://machine:port/ibi_apps/
        """
        utillobj.infoassist_api_logout()
        
        """  
            Step 20:Expand folder "S10032" > Right-click "C2231270" > New > Document
        """
        legacymainobj.select_repository_menu('P292->S10032_infoassist_4->C2235629', 'New->Document')
        time.sleep(6)
        utillobj.switch_to_window(1)
        time.sleep(5)
        """
            Verify canvas
        """
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        coln_list = ['ProductCategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 20:01: Verify report titles")
        ia_result_obj.verify_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 20:02: Verify report dataset', no_of_cells=4)
        parent_css="#TableChart_2"
        resultobj.wait_for_property(parent_css, 1)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 20:03: Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 20:04: Verify X-Axis Title")
        expected_xval_list=['Computers', 'Televisions']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M', '80M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step 20:05:Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step 20:06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar!", "bar_blue", "Step 20:07: Verify first bar color")
           
        canvas_width=self.driver.find_element_by_css_selector("#theCanvas")
        a=canvas_width.size['width']
        print("a:",a)
        """  
            Step 21:Select Layout Tab > Select Orientation > Landscape
        """
        ribbonobj.select_ribbon_item('Layout', 'orientation', opt='Landscape')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """  
            Step 22:Click on the Report component > Verify Canvas
        """
        report_comp_elem =self.driver.find_element_by_css_selector("#TableChart_1")
        utillobj.click_on_screen(report_comp_elem, "middle", click_type=0)
        
        coln_list = ['ProductCategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 22:01: Verify report titles")
        ia_result_obj.verify_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 22:02: Verify report dataset', no_of_cells=4)
        
        parent_css="#TableChart_2"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.verify_object_visible(parent_css, True, 'Step 22:03: Verify chart is displayed')
        b=canvas_width.size['width']
        print("b:",b)
        c=b>a
        utillobj.asequal(c,True,"Step 22:04: Landscape applied in canvas")
        """ 
            Step 23:Right-click the "Product/Product Category" filter in the Filter pane > Select "Include"
        """
        filter_condition=self.driver.find_element_by_css_selector("#filterBox #qbFilterBox img")
        utillobj.click_on_screen(filter_condition, "middle", click_type=1)
        utillobj.select_or_verify_bipop_menu("Include")
        filter_apply_btn=self.driver.find_element_by_css_selector("#filterBox  #qbFilterBox img[src*='apply']").is_displayed()
        utillobj.asequal(True, filter_apply_btn, 'Step 23: Product/Product Category filter is applied or included')
        """  
            Step 24:Move the Report component up, then select the Chart component and move it right under the Report component (as displayed in the screen shot)
        """
        
        ribbonobj.repositioning_document_component('1.02','0.35')
        time.sleep(5)
        elem=self.driver.find_element_by_css_selector("#TableChart_2")
        utillobj.click_on_screen(elem, 'top_middle', 0)
        time.sleep(1)
        ribbonobj.repositioning_document_component('0.35','3')
        """ 
            Step 25:Click on the Chart Component > Right-click the "Product/Product Category" filter in the Filter pane > Select "Include"
        """
        filter_condition=self.driver.find_element_by_css_selector("#filterBox #qbFilterBox img")
        utillobj.click_on_screen(filter_condition, "middle", click_type=1)
        utillobj.select_or_verify_bipop_menu("Include")
        filter_apply_btn=self.driver.find_element_by_css_selector("#filterBox  #qbFilterBox img[src*='apply']").is_displayed()
        utillobj.asequal(True, filter_apply_btn, 'Step 25: Product/Product Category filter is applied or included')
        
        """  
            Step 26:Verify filter is applied to both the Report and Chart components
        """
        coln_list = ['ProductCategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 09:011: Verify report titles")
        ia_result_obj.create_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds02.xlsx", no_of_cells=4)
        ia_result_obj.verify_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds02.xlsx", 'Step 26:01: Verify report dataset', no_of_cells=4)
        
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 26:02: Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 26:03: Verify X-Axis Title")
        expected_xval_list=['Computers', 'Televisions']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M', '80M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step 26:04: Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step 26:05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar!", "bar_blue", "Step 26:06: Verify first bar color")
        """ 
            Step 27:Click the "Page 1" menu in the upper right corner > Select "Page Options.."
        """
        ia_result_obj.select_or_verify_document_page_menu('Page Options...')
        """  
            Step 28:Click "Page 1" > Click the duplicate icon
        """
        utillobj.select_item_in_dialog("#pageOptionsDlg #iaPageList", "Page 1")
        dupBtn=self.driver.find_element_by_css_selector("#duplicatePageBtn")
        utillobj.default_left_click(object_locator=dupBtn)
        time.sleep(4)
        """ 
            Step 29:Verify Page 1 is duplicated > click OK
        """
        oDialog=self.driver.find_element_by_css_selector("#pageOptionsDlg #iaPageList")
        item_list=oDialog.self.find_elements_by_css_selector("table tr")
        actual_popup_list=[el.text.strip() for el in item_list if bool(re.match('\S+', el.text.strip()))]
        expected_list=['Page 1', 'Page 1 ( Copy )']
        utillobj.asequal(actual_popup_list, expected_list, "Step 29:Page 1 Copy is visible in the page options")
        utillobj.select_item_in_dialog("#pageOptionsDlg #iaPageList", "Page 1 ( Copy )")
        okBtn=self.driver.find_element_by_id("pageOptionsOkBtn")
        utillobj.default_left_click(object_locator=okBtn)
        time.sleep(4)
        """ 
            Step 30:Click Save in the toolbar > Save As "C2231270_DOC" > Click Save
        """ 
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID1)
        time.sleep(3)   
        """  
            Step 31:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """  
            Step 32:Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2231270_DOC.fex&tool=Document
        """
        utillobj.infoassist_api_edit(Test_Case_ID1, 'report', 'S10032_infoassist_4',mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        """  
            Step 33:Verify Preview and successful restore
        """
        ele=self.driver.find_element_by_css_selector("div[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step33_'+browser, image_type='actual',x=50, y=20, w=-50, h=-20)
        
        """ 
            Step 34:Click the 'Page 1' menu > Select "Page 1 (Copy)"
        """
        ia_result_obj.select_or_verify_document_page_menu('Page 1 ( Copy )')
          
        """  
            Step 35:Verify Preview
        """
        oPage1Copy=self.driver.find_element_by_xpath("//div[@id='iaPagesMenuBtn']//div[contains(text(), 'Page 1 ( Copy )')]")
        utillobj.verify_object_visible('css', True, "Step 29a: Verify Page Menu changed to 'Page 1( Copy )'", elem_obj=oPage1Copy)
        
        ele=self.driver.find_element_by_css_selector("#canvasContainer #theCanvas")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step35a_'+browser, image_type='actual',x=50, y=20, w=-50, h=-20)
        """ 
            Step 36:Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        """  
            Step 37:Verify Active Report output
        """
        coln_list = ['ProductCategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 37:01: Verify report titles")
        ia_result_obj.create_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds03.xlsx", no_of_cells=4)
        ia_result_obj.verify_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds03.xlsx", 'Step 37:02: Verify report dataset', no_of_cells=4)
        """ 
            Step 38:Click "Page 1 (Copy)" in the Active Report output
        """
        select_css = "#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']"
        self.driver.find_element_by_css_selector(select_css).click()
        time.sleep(5)
        """  
            Step 39:Verify output
        """
        
        resultobj.verify_yaxis_title("MAINTABLE_wbody3", "Cost of Goods", "Step 39:01: Verify -yAxis Title")
        time.sleep(1)
        resultobj.verify_xaxis_title("MAINTABLE_wbody3", "Product,Category", "Step 39:02: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody3", expected_xval_list, expected_yval_list, "Step 39:03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody3", 1, 2, 'Step 39:04: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody3", "riser!s0!g2!mbar!", "bar_blue", "Step 39:05: Verify  bar color")
        miscelanousobj.verify_chart_title('MAINTABLE_wbody3_ft', 'Cost of Goods BY Product Category', 'Step 39:06: Verify Chart Title')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu3', ['More Options','Advanced Chart','Original Chart'],"Step 39:07: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu3', ['Aggregation'],"Step 39:08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu3', ['Sum'],"Step 39:09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['COUNTRY:ITALY', 'SALES:30200', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody3", "riser!s0!g2!mbar!", expected_tooltip_list, "Step 39:10 Verify bar value")
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        """ 
            Step 40:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()