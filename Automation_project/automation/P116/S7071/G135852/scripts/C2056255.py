'''
Created on Aug 25, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7071&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2056255
TestCase Name = Using Tab Windows Navigation options. 
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_chart_rollup, visualization_metadata, visualization_ribbon, visualization_resultarea, metadata
from common.lib import utillity


class C2056255_TestClass(BaseTestCase):

    def test_C2056255(self):
        def verify_tabs(tabs_text,msg):
            otab_val=driver.find_element_by_css_selector("#MAINTABLE_0 #MAINTABLE_wmenu0>table>tbody>tr").text
            ocheck=otab_val.strip().split("\n")==tabs_text
            utillity.UtillityMethods.asequal(self,True, ocheck, msg + ": verifying Report and Chart Tabs displayed on top of the Run Report")
            
        def report_checkpoint(msg):
            miscelanousobj.verify_page_summary(0, '14of14records,Page1of1', msg + ".a: Verify the Run Report Heading")
            column_list=['Store Business Region', 'Store Business Sub Region', 'Quantity Sold', 'Gross Profit']
            miscelanousobj.verify_column_heading('ITableData0', column_list, msg + ".b: Verify the Run Report column heading")
            utillobj.verify_data_set('ITableData0','I0r','C2054055_Ds_01.xlsx', msg + ".c: Verify entire Data set in Run Report on Page 1") 
        
        def rollup_checkpoint(msg):
            rollupobj.verify_arChartMenu("wall1", msg + ".a: Verify the Chart Menu bar labels displayed on Run chart")
            column=['Store Business Region', 'Gross Profit']
            miscelanousobj.verify_column_heading('ITableData1',column, msg + ".b: Expect to see the Rollup Report heanding for Chart(Rollup)")
            utillobj.verify_data_set('ITableData1','I1r', "C2054055_Ds_02.xlsx", msg + ".c: Verify data set of rollup data")
            miscelanousobj.verify_page_summary(1, "4of4records,Page1of1", msg + ".d: Verifying the rollup data records")
            
        def pivot_checkpoint(msg):
            utillobj.verify_pivot_data_set("piv2", "C2056255_Ds_03.xlsx", msg + ".d: Expect to see a Grid(Matrix) Report")
        
        def chart_checkpoint(msg):
            rollupobj.verify_arChartMenu("wall3", msg + ".a Verify the Chart Menu bar labels displayed on Run chart")
            x_val_list=['EMEA', 'North America', 'Oceania', 'South America']
            y_val_list=['0', '2', '4', '6', '8', '10']
            result.verify_riser_chart_XY_labels('wall3', x_val_list, y_val_list, msg + ".b")
            
                
        """
            Step 01a:    Start an InfoAssist session, create a new report.
            Step 01b:    select the wf_retail file
            Step 01c:    Change the output Format to AHTML
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        rollupobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        result=visualization_resultarea.Visualization_Resultarea(self.driver)
        metaobj1=metadata.MetaData(self.driver)
        
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P116/S7071', 'mrid', 'mrpass')
        element_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(element_css, 1, 65)
        
        ribbonobj.change_output_format_type('active_report', 'Home')
   
        """
            Step 02a:    Select Quantity,Sold and Gross Profit from the Sales group for the Measure fields.
                         Select Store,Business,Region and Store,Business,Sub Region from the Store group as the Dimension fields.
        """
        metaobj.datatree_field_click("Quantity,Sold",2,1)
        element_css="div[id^='ActivePreview']"
        utillobj.synchronize_with_number_of_element(element_css, 2, 30)
        
        metaobj.datatree_field_click("Gross Profit",2,1)
        element_css="div[id^='ActivePreview']"
        utillobj.synchronize_with_number_of_element(element_css, 4, 30)
        
        metaobj1.collapse_data_field_section('Measure Groups')
        time.sleep(3)
        
        metaobj.datatree_field_click("Store,Business,Region", 2, 1)
        element_css="div[id^='ActivePreview']"
        utillobj.synchronize_with_number_of_element(element_css, 6, 30)
        
        metaobj.datatree_field_click("Store,Business,Sub Region", 2, 1)
        element_css="div[id^='ActivePreview']"
        utillobj.synchronize_with_number_of_element(element_css, 8, 30)
        list1 = ['StoreBusinessRegion', 'StoreBusinessSub Region', 'QuantitySold', 'Gross Profit']
        result.verify_report_titles_on_preview(4, 12, "TableChart_1", list1, "Step 01: Verify column titles on preview")
        
        """
            Step 03: Click the Run button.
                     From the drop down for Store,Business,Region select the Window option, then select Tabs.
        """
        ribbonobj.select_top_toolbar_item("toolbar_run")
        utillobj.switch_to_frame(pause=5)
#         WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        report_checkpoint("Step 03")
        miscelanousobj.select_menu_items("ITableData0", "0", "Window","Tabs")
        otab1=driver.find_element_by_css_selector("#MAINTABLE_0 #MAINTABLE_wmenu0>table>tbody>tr>#tab_0").text
        otab=otab1.strip()=='Report'
        utillity.UtillityMethods.asequal(self,True, otab, "Step 03.d: Verify that the initial Tab says 'Report' and is located above the report body")
         
        """
        Step 04: From the drop down for Gross Profit select the Rollup option by Business,Store,Region.
        Expect to see the Rollup Report replace the initial report and a Tab appear for Chart(Rollup).
        """
        browser= utillobj.parseinitfile('browser')
        if browser.lower() in ['edge','chrome', 'firefox']:           
            miscelanousobj.select_menu_items("ITableData0", "3", "Rollup","Store Business Region")
        else:
            col_heading_click = driver.find_element_by_css_selector("#ITableData0 td#TCOL_0_C_3")
            utillobj.click_on_screen(col_heading_click,'middle', click_type=0)
            drop=driver.find_element_by_css_selector("#ITableData0 td div#popid0_3 img")
            utillobj.click_on_screen(drop,'middle', click_type=0)
            rollup = driver.find_element_by_css_selector("#menulist td span#set0_3_0_6i_t")
            utillobj.click_on_screen(rollup,'middle', click_type=0)
            col_tab = driver.find_element_by_css_selector("#menulist table #dt0_3_0_6.m0out0 table td span#set0_3_0_6_0i_t")
            utillobj.click_on_screen(col_tab, 'middle')
            col=driver.find_element_by_css_selector("#menulist table #dt0_3_0_6.m0out0 table td span#set0_3_0_6_2i_t")
            utillobj.click_on_screen(col,'middle', click_type=0)
            
        tabs=['Report ', 'Chart']
        verify_tabs(tabs, "Step 04")
        rollup_checkpoint("Step 04")
        
        """
            Step 05: Click the Report tab at the top to return to the initial report.
                        From the drop down for Quantity,Sold select the Pivot option
                        Select Store,Business,Sub Region for the BY field and Store,Business,Region for the Across field.
             
        Expect to see the Pivot Report replace the initial report and a Tab appear for Pivot
        """
        miscelanousobj.navigate_tabbed_report(0,1)
        report_checkpoint("Step 05r")
        if browser.lower() in ['edge','chrome', 'firefox']:              
            miscelanousobj.select_menu_items("ITableData0", "2", "Pivot (Cross Tab)","Store Business Sub Region","Store Business Region")
        else:
            col_head=self.driver.find_element_by_css_selector("#ITableData0 td#TCOL_0_C_1")
            utillobj.click_on_screen(col_head,'middle', click_type=0)
            drop=self.driver.find_element_by_css_selector("#ITableData0 td div#popid0_2 img")
            utillobj.click_on_screen(drop,'middle', click_type=0)
            rollup = self.driver.find_element_by_css_selector("#menulist td span#set0_2_0_7i_t")
            utillobj.click_on_screen(rollup,'middle', click_type=0)
            col=driver.find_element_by_css_selector("#menulist table #dt0_2_0_7.m0out0 table td span")            
            utillobj.click_on_screen(col,'middle')
            col1=driver.find_element_by_css_selector("#menulist table #dt0_2_0_7.m0out0 table td span#set0_2_0_7_3i_t")            
            utillobj.click_on_screen(col1,'middle', click_type=0)
            col2=driver.find_element_by_css_selector("#menulist table #dt0_2_0_7.m0out0 table td span#set0_2_0_7_3_0i_t")            
            utillobj.click_on_screen(col2,'middle')
            col3=driver.find_element_by_css_selector("#menulist table #dt0_2_0_7.m0out0 table td span#set0_2_0_7_3_2i_t")            
            utillobj.click_on_screen(col3,'middle', click_type=0)
        tabs=['Report ', 'Chart', 'Pivot']
        verify_tabs(tabs, "Step 05")
        pivot_checkpoint("Step 05p")
         
        """
            Step 06: Click the Report tab at the top to return to the initial report.
                        From the drop down for Store,Business,Sub Region select the Chart option, then Column for the chart
                        type, then Store,Business,Region as the Group BY field.
             
        Expect to see the Bar Chart replace the initial report and a Tab appear for Chart. This chart contains counts.
        """
        miscelanousobj.navigate_tabbed_report(0,1)
        if browser.lower() in ['edge','chrome', 'firefox']:              
            miscelanousobj.select_menu_items("ITableData0", "1", "Chart","Column","Store Business Region")
        else:
            col_head=self.driver.find_element_by_css_selector("#ITableData0 td#TCOL_0_C_2")
            utillobj.click_on_screen(col_head,'middle', click_type=0)
            drop=self.driver.find_element_by_css_selector("#ITableData0 td div#popid0_1 img")
            utillobj.click_on_screen(drop,'middle', click_type=0)
            rollup = self.driver.find_element_by_css_selector("#menulist td span#set0_1_0_5i_t")
            utillobj.click_on_screen(rollup,'middle', click_type=0)
            col=driver.find_element_by_css_selector("#menulist table #dt0_1_0_5.m0out0 table td span")
            utillobj.click_on_screen(col,'middle')
            col1=driver.find_element_by_css_selector("#menulist table #dt0_1_0_5.m0out0 table td span#set0_1_0_5_2i_t")
            utillobj.click_on_screen(col1,'middle', click_type=0)
            col2=driver.find_element_by_css_selector("#menulist table #dt0_1_0_5.m0out0 table td span#set0_1_0_5_2_0i_t")
            utillobj.click_on_screen(col2,'middle')
            col3=driver.find_element_by_css_selector("#menulist table #dt0_1_0_5.m0out0 table td span#set0_1_0_5_2_2i_t")
            utillobj.click_on_screen(col3,'middle', click_type=0)
        tabs=['Report ', 'Chart', 'Pivot', 'Chart']
        verify_tabs(tabs, "Step 06")
        utillobj.switch_to_default_content(pause=2)
#         driver.switch_to_default_content()
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2056255_Actual_Step06', image_type='actual', x=1, w=-600, h=-300)
        utillobj.switch_to_frame(pause=5)
#         WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))   
        chart_checkpoint("Step 06c")
        expected_tooltip=['Store Business Sub Region: 8', 'X: North America']
        miscelanousobj.verify_active_chart_tooltip('wbody3_f', 'riser!s0!g1!mbar!', expected_tooltip, "Step 06c.c: verify the chart tooltip with fill color")
         
        """
            Step 07: Click the Report tab at the top to return to the initial report.
                        From the drop down for Store,Business,Region select the Window option and the select the Cascade option..
              
        Expect to see the initial report overlay the other three components created as Tabs.
        """
        miscelanousobj.navigate_tabbed_report(0,1)
        report_checkpoint("Step 07r")
        miscelanousobj.select_menu_items("ITableData0", "0", "Window","Cascade")
        r_title=driver.find_element_by_css_selector('#wall1 div.arWindowBar>table>tbody>tr>td.arWindowBarTitle').text
        r_cond=r_title.strip()=='Gross Profit BY Store Business Region'
        utillity.UtillityMethods.asequal(self,True, r_cond, 'Step 7r: Verifying the rollup dialog title')
        rollup_checkpoint("Step 07r")
        p_title=driver.find_element_by_css_selector('#wall2 div.arWindowBar>table>tbody>tr>td.arWindowBarTitle').text
        p_cond=p_title.strip()=='Quantity Sold BY Store Business Region, Store Business Sub Region'
        utillity.UtillityMethods.asequal(self,True, p_cond, 'Step 07p: Verifying the pivot dialog title')
        pivot_checkpoint("Step 07p")
        c_title=driver.find_element_by_css_selector('#wall3 div.arWindowBar>table>tbody>tr>td.arWindowBarTitle').text
        c_cond=c_title.strip()=='Store Business Sub Region BY Store Business Region'
        utillity.UtillityMethods.asequal(self,True, c_cond, 'Step 07c: Verifying the chart dialog title')
        chart_checkpoint("Step 07c")
        utillobj.switch_to_default_content(pause=2)
#         driver.switch_to_default_content()
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2056255_Actual_Step07', image_type='actual', x=1, w=-600, h=-300)
        utillobj.switch_to_frame(pause=5)
#         WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]'))) 
                  
        """
            Step 08: Click all of the minimize buttons of the partially hidden Tab components
                        Expect to see all of the partially covered components reduced to buttons at the bottom of the initial report
        """
        for i in range(3,0,-1):
#             driver.find_element_by_css_selector("#wall" + str(i) + " div.arWindowBar table>tbody>tr>td>div[onclick='minwin(" + str(i) + ")']").click()
            min_button_css="#wall" + str(i) + " div.arWindowBar table>tbody>tr>td>div[onclick='minwin(" + str(i) + ")']"
            min_button_obj=self.driver.find_element_by_css_selector(min_button_css)
            utillobj.default_click(obj_locator=min_button_obj)

        if browser.lower() == 'firefox':
            expected_tabPaging=['Gross Profit BY Store Business Region:rgb(255, 255, 255):rgb(104, 154, 213)', 'Quantity Sold BY Store Business Region, Store Business Sub Region:rgb(255, 255, 255):rgb(104, 154, 213)', 'Store Business Sub Region BY Store Business Region:rgb(255, 255, 255):rgb(104, 154, 213)']
        else:
            expected_tabPaging=['Gross Profit BY Store Business Region:rgba(255, 255, 255, 1):rgba(104, 154, 213, 1)', 'Quantity Sold BY Store Business Region, Store Business Sub Region:rgba(255, 255, 255, 1):rgba(104, 154, 213, 1)', 'Store Business Sub Region BY Store Business Region:rgba(255, 255, 255, 1):rgba(104, 154, 213, 1)']
        actual_tabPaging=[]
        total_min=driver.find_elements_by_css_selector("#wall0 table>tbody>tr>td.tabPagingText1")
        for i in range(1,len(total_min)+1):
            paging_text=driver.find_element_by_css_selector("#wall0 table>tbody>tr>td[onclick='maxwin(" + str(i) + ")']").text
            paging_color=driver.find_element_by_css_selector("#wall0 table>tbody>tr>td[onclick='maxwin(" + str(i) + ")']").value_of_css_property("color")
            paging_bgcolr=driver.find_element_by_css_selector("#wall0 table>tbody>tr>td[onclick='maxwin(" + str(i) + ")']").value_of_css_property("background-color")
            actual_tabPaging.append(paging_text.strip() + ":" + paging_color + ":" + paging_bgcolr)   
#         print(actual_tabPaging)
#         print(expected_tabPaging)
        utillity.UtillityMethods.asequal(self,actual_tabPaging, expected_tabPaging, 'Step 8.a: Expect to see all of the partially covered components reduced to buttons at the bottom of the initial report')        
          
        """
            Step 09: Click the first entry in the list at the bottom, for Gross Profit BY Store Business Region.
                        Expect to see the Rollup report on top of the initial report.
        """
#         driver.find_element_by_css_selector("#wall0 table>tbody>tr>td[onclick='maxwin(1)']").click()
        gross_list_box_css="#wall0 table>tbody>tr>td[onclick='maxwin(1)']"
        gross_list_box_obj=self.driver.find_element_by_css_selector(gross_list_box_css)
        utillobj.default_click(obj_locator=gross_list_box_obj)
        
        r_title=driver.find_element_by_css_selector('#wall1 div.arWindowBar>table>tbody>tr>td.arWindowBarTitle').text
        r_cond=r_title.strip()=='Gross Profit BY Store Business Region'
        utillity.UtillityMethods.asequal(self,True, r_cond, 'Step 9r: Verifying the rollup dialog title')
        rollup_checkpoint("Step 9r")
          
        """
            Step 10:  Minimize the Rollup report.
                        Click the second entry in the list at the bottom, for Quantity Sold BY Store Business Region, Store Business Sub Region.
        """

        min_rollup_css="#wall1 div.arWindowBar table>tbody>tr>td>div[onclick='minwin(1)']"
        min_rollup_obj=self.driver.find_element_by_css_selector(min_rollup_css)
        utillobj.default_click(obj_locator=min_rollup_obj)
        

        max_rollup_css="#wall0 table>tbody>tr>td[onclick='maxwin(2)']"
        max_rollup_obj=self.driver.find_element_by_css_selector(max_rollup_css)
        utillobj.default_click(obj_locator=max_rollup_obj)
        
        p_title=driver.find_element_by_css_selector('#wall2 div.arWindowBar>table>tbody>tr>td.arWindowBarTitle').text
        p_cond=p_title.strip()=='Quantity Sold BY Store Business Region, Store Business Sub Region'
        utillity.UtillityMethods.asequal(self,True, p_cond, 'Step 10p: Verifying the pivot dialog title')
        pivot_checkpoint("Step 10p")
          
        """
            Step 11:  Minimize the Pivot report.
                        Click the third entry in the list at the bottom, for Store Business Sub Region BY Store Business Region.
        """

        min_pivot_css="#wall2 div.arWindowBar table>tbody>tr>td>div[onclick='minwin(2)']"
        min_pivot_obj=self.driver.find_element_by_css_selector(min_pivot_css)
        utillobj.default_click(obj_locator=min_pivot_obj)
        

        max_pivot_css="#wall0 table>tbody>tr>td[onclick='maxwin(3)']"
        max_pivot_obj=self.driver.find_element_by_css_selector(max_pivot_css)
        utillobj.default_click(obj_locator=max_pivot_obj)
        
        utillobj.switch_to_default_content(pause=2)

        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2056255_Actual_Step11', image_type='actual', x=1, w=-600, h=-300)
        utillobj.switch_to_frame(pause=5)

        c_title=driver.find_element_by_css_selector('#wall3 div.arWindowBar>table>tbody>tr>td.arWindowBarTitle').text
        c_cond=c_title.strip()=='Store Business Sub Region BY Store Business Region'
        utillity.UtillityMethods.asequal(self,True, c_cond, 'Step 11c: Verifying the chart dialog title')
        chart_checkpoint("Step 11c")

        utillobj.switch_to_default_content(pause=2)
      
        
if __name__ == '__main__':
    unittest.main()