'''
Created on Dec 04, 2017

@author: PM14587
Testcase Name : Document with dynamic group
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2231673
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_run,ia_resultarea,active_miscelaneous
from common.lib import utillity

class C2231673_TestClass(BaseTestCase):

    def test_C2231673(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2231673'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
            Step 01 : Launch IA Document mode with wf_retail_lite: http://machine:port/ibi_apps/ia?tool=document&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('document','baseapp/wf_retail_lite','P292/S10032_infoassist_5', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasPanel #iaCanvasCaptionLabel", 1,60,string_value='Document')
        time.sleep(3)
        
        """
            Step 02 : Select Insert Tab > Click "Report" 
        """
        ribbonobj.select_ribbon_item('Insert','report')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
         
        """
            Step 02.1 : Verify Document canvas
        """
        default_text=self.driver.find_element_by_css_selector("#canvasContainer #TableChart_1 div[align='justify']").text.strip()
        utillobj.asin("Drag and drop fields onto the",default_text,'Step 02.1 : Verify Document canvas')
         
        """
            Step 03 : Drag "Sale Unit(s)" into the "Sum" bucket
        """
#         metaobj.datatree_field_click('Sale Unit(s)',2,1)
        metaobj.drag_drop_data_tree_items_to_query_tree('Sale Unit(s)',1,'Sum',0)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,20,string_value='Sale Unit(s)')
         
        """
            Step 04 : Drag "Customer,Business,Region" into the "Coordinated" bucket
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Customer,Business,Region',1,'Coordinated',0)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(7)", 1,30,string_value='Customer,Business,Region')
         
        """
            Step 05: Drag "Customer,Country" into the "By" bucket
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Customer,Country',1,'By',0)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,30,string_value='Customer,Country')
         
        """
            Step 06 : Right-click "Customer,Business,Region" in "Coordinated" > Select "Create Group..."
        """
        metaobj.querytree_field_click('Customer,Business,Region',1,1,'Create Group...')
         
        """
            Step 07 : Multi-select "North America" and "South America"
            Step 08 : Click "Group"
            Step 09 : Click OK
        """
        metaobj.create_ia_group('Group', ['North America','South America'],close_button='ok')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(8)", 1,30,string_value='BUSINESS_REGION_1')
         
        """
            Step 10 : Verify BUSINESS_REGION_1 appears in the Data and Query panes
        """
        metaobj.verify_query_pane_field('Coordinated','BUSINESS_REGION_1',1,'Step 10.1 : Verify Verify BUSINESS_REGION_1 appears in the Data and Query panes',color='Trolley_Grey',font_style='italic')
        metaobj.verify_data_pane_field('Values', 'BUSINESS_REGION_1', 1,'Step 10.2')
        
        """
            Step 11: Select Insert Tab > Click "Chart"
        """
        ribbonobj.select_ribbon_item('Insert','chart')
        resultobj.wait_for_property(" #pfjTableChart_2 g>text[class='legend-labels!s0!']", 1,30,string_value='Series0')
         
        """
            Step 12 : Move the Chart component next to the Report component
        """
        ribbonobj.repositioning_document_component('4','1.04')
         
        """
            Step 13 : Verify Chart component displays BUSINESS_REGION_1 in the Coordinated bucket
        """
        metaobj.verify_query_pane_field('Chart1 (wf_retail_lite)','BUSINESS_REGION_1',12,'Step 13.1 : Verify Verify BUSINESS_REGION_1 appears in the Data and Query panes',color='Trolley_Grey',font_style='italic')
         
        """
            Step 14 : Double-click fields "Gross Profit" and "Customer,Country" to add them to the Chart
        """
        metaobj.datatree_field_click('Gross Profit',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(8)", 1,20,string_value='Gross Profit')
         
        metaobj.datatree_field_click('Customer,Country',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(10)", 1,20,string_value='Customer,Country')
        time.sleep(3)

        """
            Step 14.1 : Verify preview
        """
        iaresult.verify_across_report_data_set('TableChart_1 ',2,2,30,2,Test_Case_ID+'_DataSet_01.xlsx','Step 14.1 : Verify preview report')
        expectes_xaisx_label=['Austria', 'Belgium', 'China', 'Czech Republic', 'Denmark', 'Egypt', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Malaysia', 'Netherlands', 'Norway', 'Philippines']
        expectes_yaisx_label=['0','4M','8M','12M','16M','20M','24M']
        resultobj.verify_riser_chart_XY_labels('pfjTableChart_2',expectes_xaisx_label, expectes_yaisx_label,'Step 14.2 : ')
        resultobj.verify_xaxis_title('pfjTableChart_2','Customer Country','Step 14.3 : Verify X-Axis Title')
        resultobj.verify_yaxis_title('pfjTableChart_2','Gross Profit','Step 14.4 : Verify Y-Axis Title')
        resultobj.verify_number_of_riser('pfjTableChart_2',1,34,'Step 14.5 : Verify number of risers')
        utillobj.verify_chart_color('pfjTableChart_2','riser!s0!g14!mbar!','bar_blue1','Step 14.6 : Verify chart riser color')
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element,Test_Case_ID+'_Actual_Step_14','actual')

        """
            Step 15 : Click IA > Save As > "C2231673" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)

        """
            Step 16 : Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1,45,string_value='Customer Country')
        
        """
            Step 17 : Verify Active Report output with BUSINESS_REGION_1 dropdown menu
        """
        utillobj.verify_element_text("#IBILAYOUTDIV0TABS table[id^='iLayTB'] td:nth-child(1)>span","BUSINESS_REGION_1","Step 17.1 : Verify Active Report output with BUSINESS_REGION_1 dropdown menu")
        
        """
            Step 17.1 : Verify Report and Chart
        """
        iarun.verify_table_data_set("#ITableData0",Test_Case_ID+'_DataSet02.xlsx','Step 17.0 : Verify Report data')
        active.verify_page_summary(0,"34of42records,Page1of1",'Step 17.1 : Verify page summary')
        active.verify_chart_title("MAINTABLE_wbody1_ft","Gross Profit BY Customer Country","Step 17.2 : Verify chart title")
        expectes_xaisx_label=['Austria', 'Belgium', 'China', 'Czech Republic', 'Denmark', 'Egypt', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Malaysia', 'Netherlands', 'Norway', 'Philippines']
        expectes_yaisx_label=['0','4M','8M','12M','16M','20M','24M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f',expectes_xaisx_label, expectes_yaisx_label,'Step 17.3 : ')
        resultobj.verify_xaxis_title('MAINTABLE_wbody1_f','Customer Country','Step 17.3 : Verify X-Axis Title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1_f','Gross Profit','Step 17.5 : Verify Y-Axis Title')
        resultobj.verify_number_of_riser('MAINTABLE_wbody1_f',1,34,'Step 17.6 : Verify number of risers')
        utillobj.verify_chart_color('MAINTABLE_wbody1_f','riser!s0!g14!mbar!','bar_blue1','Step 17.7 : Verify chart riser color')
        expected_tooltip_list=['BUSINESS_REGION_1:  EMEA', 'Customer Country:  Germany', 'Gross Profit:  $19,687,587.83', 'Filter Chart', 'Exclude from Chart']
        active.verify_active_chart_tooltip("MAINTABLE_wbody1_f","riser!s0!g8!mbar!", expected_tooltip_list,"Step 17.8 : Verify chart tooltip values")
        active.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 17.9 : Verify Chart toolbar")
        active.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 17.10 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        active.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 17.11 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        
        """
            Step 18 : Click on the BUSINESS_REGION_1 dropdown menu > Select "North America and South America:
        """
        expected_options=['EMEA', 'North America and South America', 'Oceania']
        utillobj.select_or_verify_html_drop_down_option("#IBILAYOUTDIV0TABS select[class='arDashboardMergeDropdown']",'North America and South America',verify_default_option='EMEA',verify_options=expected_options,msg='Step 18.1 : Verify BUSINESS_REGION_1 options')
        resultobj.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-labels!g6!mgroupLabel!']", 1,20,string_value='United States')
        
        """
            Step 19 : Verify output is updated with selection
        """
        iarun.verify_table_data_set("#ITableData0",Test_Case_ID+'_DataSet03.xlsx','Step 19.0 : Verify Report data')
        active.verify_page_summary(0,"7of42records,Page1of1",'Step 19.1 : Verify page summary')
        active.verify_chart_title("MAINTABLE_wbody1_ft","Gross Profit BY Customer Country","Step 19.2 : Verify chart title")
        expectes_xaisx_label=['Argentina', 'Brazil', 'Canada', 'Chile', 'Colombia', 'Mexico', 'United States']
        expectes_yaisx_label=['0','20M','40M','60M','80M','100M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f',expectes_xaisx_label, expectes_yaisx_label,'Step 19.3 : ')
        resultobj.verify_xaxis_title('MAINTABLE_wbody1_f','Customer Country','Step 19.4 : Verify X-Axis Title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1_f','Gross Profit','Step 19.5 : Verify Y-Axis Title')
        resultobj.verify_number_of_riser('MAINTABLE_wbody1_f',1,7,'Step 19.6 : Verify number of risers')
        utillobj.verify_chart_color('MAINTABLE_wbody1_f','riser!s0!g6!mbar!','bar_blue1','Step 19.7 : Verify chart riser color')
        expected_tooltip_list=['BUSINESS_REGION_1:  North America and South America', 'Customer Country:  United States', 'Gross Profit:  $94,033,986.65', 'Filter Chart', 'Exclude from Chart']
        active.verify_active_chart_tooltip("MAINTABLE_wbody1_f","riser!s0!g6!mbar!", expected_tooltip_list,"Step 19.8 : Verify chart tooltip values")
        active.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 19.9 : Verify Chart toolbar")
        active.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 19.10 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        active.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 019.11 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(3)
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element,Test_Case_ID+'_Actual_Step_19','actual')
                 
        """
            Step 20 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 21 :Reopen FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2231673.fex&tool=document
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'document','P292/S10032_infoassist_5',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#pfjTableChart_2 text[class='xaxisOrdinal-title']", 1,45,string_value='Customer Country')
        time.sleep(2)
        
        iaresult.verify_across_report_data_set('TableChart_1 ',2,2,30,2,Test_Case_ID+'_DataSet_01.xlsx','Step 21.1 : Verify preview report')
        expectes_xaisx_label=['Austria', 'Belgium', 'China', 'Czech Republic', 'Denmark', 'Egypt', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Malaysia', 'Netherlands', 'Norway', 'Philippines']
        expectes_yaisx_label=['0','4M','8M','12M','16M','20M','24M']
        resultobj.verify_riser_chart_XY_labels('pfjTableChart_2',expectes_xaisx_label, expectes_yaisx_label,'Step 21.2 : ')
        resultobj.verify_xaxis_title('pfjTableChart_2','Customer Country','Step 21.3 : Verify X-Axis Title')
        resultobj.verify_yaxis_title('pfjTableChart_2','Gross Profit','Step 21.4 : Verify Y-Axis Title')
        resultobj.verify_number_of_riser('pfjTableChart_2',1,34,'Step 21.5 : Verify number of risers')
        utillobj.verify_chart_color('pfjTableChart_2','riser!s0!g14!mbar!','bar_blue1','Step 21.6 : Verify chart riser color')
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element,Test_Case_ID+'_Actual_Step_21','actual')
        
        """
            Step 22 : Click on the Report component on Canvas
        """
        report=self.driver.find_element_by_id("TableChart_1")
        utillobj.click_on_screen(report,'middle',0)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        
        """
            Step 23 : Verify BUSINESS_REGION_1 field appears in the Data and Query panes
        """
        metaobj.verify_query_pane_field('Coordinated','BUSINESS_REGION_1',1,'Step 23.1 : Verify Verify BUSINESS_REGION_1 appears in the Query panes',color='Trolley_Grey',font_style='italic')
        metaobj.verify_data_pane_field('Customer', 'BUSINESS_REGION_1', 1,'Step 23.2')
          
        """
            Step 24 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp 
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()