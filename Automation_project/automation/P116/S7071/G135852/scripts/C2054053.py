'''
Created on Aug 22, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7071&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2054053
TestCase Name = Using Tab Windows Navigation options. 
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_chart_rollup
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea

class C2054053_TestClass(BaseTestCase):

    def test_C2054053(self):
        def report_checkpoint(msg):
            miscelanousobj.verify_page_summary(0, '7of7records,Page1of1', msg + ".a: Verify the Run Report Heading")
            column_list=['Product Category', 'Gross Profit']
            miscelanousobj.verify_column_heading('ITableData0', column_list, msg + ".b: Verify the Run Report column heading")
            utillobj.verify_data_set('ITableData0','I0r','C2054053_Ds_01.xlsx', msg + ".c: Verify entire Data set in Run Report on Page 1") 
        def verify_tabs(tabs_text,msg):
            otab_val=driver.find_element_by_css_selector("#MAINTABLE_0 #MAINTABLE_wmenu0>table>tbody>tr").text
            ocheck=otab_val.strip().split("\n")==tabs_text
            utillity.UtillityMethods.asequal(self,True, ocheck, msg + ": verifying Report and Chart Tabs displayed on top of the Run Report")
        def chart_checkpoint(msg):
            rollupobj.verify_arChartMenu("wall1", msg + ".a Verify the Chart Menu bar labels displayed on Run chart")
            x_val_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo', 'Televisions', 'Video']
            y_val_list=['0', '20M', '40M', '60M', '80M', '100M']
            result.verify_riser_chart_XY_labels('wall1', x_val_list, y_val_list, msg + ".b")
            
            expected_tooltip=['Gross Profit: 86.2M', 'X: Stereo Systems']            
            miscelanousobj.verify_active_chart_tooltip('wbody1_f', 'riser!s0!g4!mbar', expected_tooltip, msg + ".c: verify the chart tooltip")
        
        """
            Step 01a:    Start an InfoAssist session, create a new report and select the wf_retail file.
            Step 01b:    Change the output Format to AHTML.
            Step 01c:    Select Quantity,Sold from the Sales group as the Measure.
            Step 01d:    Select Product,Category from the Product group as theDimension.
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        result=visualization_resultarea.Visualization_Resultarea(self.driver)
        rollupobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P116/S7071', 'mrid', 'mrpass')
        
        element_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(element_css, 1, 65)
        
        ribbonobj.change_output_format_type('active_report', 'Home')
        time.sleep(3)
        metaobj.datatree_field_click("Gross Profit",2,1)
        element_css="#TableChart_1 [id^='ActivePreviewI']:nth-child(1)"
        utillobj.synchronize_with_number_of_element(element_css, 1, 30)
        
        metaobj.datatree_field_click("Product,Category", 2, 1)
        element_css="#TableChart_1 [id^='ActivePreviewI']"
        utillobj.synchronize_with_number_of_element(element_css, 10, 30)
         
        list1 = ['ProductCategory', 'Gross Profit']
        result.verify_report_titles_on_preview(2, 4, "TableChart_1", list1, "Step 01: Verify column titles on preview")
        
        """
            Step 02: Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 40)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        report_checkpoint("Step 02")
        
        """
            Step 03: Click the drop down arrow for Product,Category, select the Window option and position on the Tabs option.
                    Do not click Tabs.
        """
        option=['Cascade', 'Tabs']
        miscelanousobj.verify_menu_items('ITableData0',0,'Window',option,'step03.a: Expect to see the Active Report menu for Window/Tabs selection')
        
        """
            Step 04: Now click the Tabs option.
            
        Expect to see the Active Report appear, now with a Tab Window control at the top
        """
        miscelanousobj.select_menu_items("ITableData0", "0", "Window","Tabs")
        otab1=driver.find_element_by_css_selector("#MAINTABLE_0 #MAINTABLE_wmenu0>table>tbody>tr>#tab_0").text
        otab=otab1.strip()=='Report'
        utillity.UtillityMethods.asequal(self,True, otab, 'step04.a: Verify Active Report appear with a Tab Window control at the top')
        
        """
            Step 05: Click the drop down arrow for Gross Profit, select Chart, then Column and position on Produt,Category for Group By.
                    Do not click the Group By option.
            
        Expect to see the following Active Report with the menu for the Column Chart.
        """
        option=['Group By (X)', 'Product Category', 'Gross Profit']
        miscelanousobj.verify_menu_items('ITableData0',1,'Chart->Column',option,'step05.a: Expect to see the Active Report menu for the Column Chart')
        
        """
            Step 06: Now click the Group By choice of Product,Category .
            
        Expect to see the following Bar chart appear, with the Tab Window at the top now showing a Report and a Chart.
        """
        miscelanousobj.select_menu_items("ITableData0", "1", "Chart","Column","Product Category")
        tabs=['Report ', 'Chart']
        verify_tabs(tabs, "Step 06")
        #take_screenshot_inside_iframe(pview_x, pview_y, (driver.find_element_by_css_selector("#wall1"),'C2054053_Base_step06a', image_type='base')
        utillobj.switch_to_default_content(pause=2)
        
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2054053_Actual_step06a', image_type='actual')
        utillobj.switch_to_frame(pause=2)
        
        chart_checkpoint("Step 06c")
        
        """
            Step 07: Click the Report Tab on top of the Chart..
              
        Expect to switch back to the Report, with both Tabs at the top
        """
        miscelanousobj.navigate_tabbed_report(0,1)
        report_checkpoint("Step 07r")
          
        """
            Step 08: Click the drop down for Product,Category, select Window and select the Cascade option..
              
        Expect to see both the Report and Chart on the same screen.
        """              
        miscelanousobj.select_menu_items("ITableData0", "0", "Window","Cascade")
        miscelanousobj.move_active_popup(1,'200', '50')
        report_checkpoint("Step 08r")
        c_title=driver.find_element_by_css_selector('#wall1 div.arWindowBar>table>tbody>tr>td.arWindowBarTitle').text
        c_cond=c_title.strip()=='Gross Profit BY Product Category'
        utillity.UtillityMethods.asequal(self,True, c_cond, 'Step 08c: Verifying the chart dialog title')
        utillobj.switch_to_default_content(pause=2)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2054053_Actual_step08', image_type='actual')
        utillobj.switch_to_frame(pause=2)
        chart_checkpoint("Step 08c")
           
        """
            Step 09: Click the drop down for Product,Category, select Window, the select Tabs.
               
        Expect to see the Tabs re-appear again over the Report.
        """
        miscelanousobj.select_menu_items("ITableData0", "1", "Window","Tabs")
           
        tabs=['Report ', 'Chart']
        verify_tabs(tabs, "Step 09q")
        report_checkpoint("Step 09r")
           
        """
            Step 10: Click the 'X' next to the Chart Tab..
               
        Expect to see the Active Report, now only showing a Tab for Report..
        """
        close_chart_tab_css="#tabb_0_1"
        close_chart_tab_obj=self.driver.find_element_by_css_selector(close_chart_tab_css)
        utillobj.default_click(obj_locator=close_chart_tab_obj)
        
        otab_val=driver.find_element_by_css_selector("#MAINTABLE_0 #MAINTABLE_wmenu0>table>tbody>tr").text
        ocheck=otab_val.strip()=='Report'
        utillity.UtillityMethods.asequal(self,True, ocheck,'Step 10.a: verifying Report Tab displayed on top of the Run Report')
        report_checkpoint("Step 10r")   
        utillobj.switch_to_default_content(pause=1)
        
        
if __name__ == '__main__':
    unittest.main()