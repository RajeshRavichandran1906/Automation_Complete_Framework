'''
Created on Jan 17, 2019

@author: Vpriya

Testsuite =  http://172.19.2.180/testrail/index.php?/suites/view/10670&group_by=cases:section_id&group_id=432673&group_order=asc
Testcase id=http://172.19.2.180/testrail/index.php?/cases/view/5852860
TestCase Name = Add Global filter to Document for a report and a chart (MERGE=ADVANCED).
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import active_chart
from common.wftools import active_report
from common.wftools import document
from common.wftools import visualization
from common.lib import utillity
from common.lib import core_utility
from common.pages import webfocus_editor
import time

class C5852860_TestClass(BaseTestCase):

    def test_C5852860(self):
        
        """
            TESTCASE VARIABLES
        """
        
        Testcase_ID="C5852860"
        doc_obj=document.Document(self.driver)
        report_obj=report.Report(self.driver)
        vis_obj=visualization.Visualization(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        webfocus_editor_obj=webfocus_editor.WebfocusEditor(self.driver)
        active_report_obj=active_report.Active_Report(self.driver)
        folder_name="P116_S10670/G432673"
        report_css="#TableChart_1"
        Page2_panel_css="#singleReportPanel"
        add_filter_css="[class='arFilter']"
        menu_css="#MAINTABLE_wbodyMain0"
        filter_css=".arDashboardBar .arDashboardBarGlobalButton [title='Global Filter'] img"
        MEDIUM_WAIT_TIME=45
        SHORT_WAIT_TIME=10
        preview2_parent_css="#TableChart_2"
        chart_run_parent_css="#MAINTABLE_1"
        chart_xaxis_run=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croi...', 'Food : Scone', 'Gifts : Coff...', 'Gifts : Coff...', 'Gifts : Mug', 'Gifts : The...', ]
        chart_yaxis_run=['0', '3M', '6M', '9M', '12M']
        filter_parent_css="#MAINTABLE_wbody1_f"
        filter_pop_up_css="#FiltTable1 .arFilterItem"
        
            
        """
        Step 1:Create a new Document using the ggsales file.
        Select Active Report as the Output Format
        http://machine:port/{alias}/ia?tool=document&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116_S10670%2FG432673%2F
        """
        report_obj.invoke_ia_tool_using_new_api_login("Document", "ibisamp/ggsales")
                
        """
        Step 2:From the insert menu icon, add a Text Box and insert the text 
        "Global Filter for Document containing Report & Chart".
        Expect to see the following Text Box on the canvas..
        """
        vis_obj.select_ribbon_item('Insert','text_box')
        active_chart_obj.wait_for_number_of_element("#theCanvas #Text_1", 1, 35)
        doc_obj.resizing_document_component('0.25', '4.5')
        doc_obj.enter_text_in_document_Textbox('Text_1', 'Global Filter for Document containing Report & Chart')
        time.sleep(2)
        doc_obj.verify_text_in_document_Textbox('#Text_1', 'Global Filter for Document containing Report & Chart', "Step 02:01: Verify textbox value")
               
        """
        Step 3:From the insert menu icon, add a Report to the canvas below the Text Box.
        Select fields Category, Product, Unit Sales & Dollar Sales..
        Expect to see the following canvas with Text Box and Report preview.
        """
        report_obj.select_ia_ribbon_item('Insert', 'report')
        utill_obj.synchronize_with_number_of_element(report_css, 1,15)
        doc_obj.drag_drop_document_component('#Text_1', '#TableChart_1', 0, 30, target_drop_point='bottom_middle')
            
        field_name_1='Category'
        field_name_2='Product'
        field_name_3='Unit Sales'
        field_name_4='Dollar Sales'
            
        element_css="#TableChart_1"
            
        report_obj.double_click_on_datetree_item(field_name_1, 1)
        active_chart_obj.wait_for_visible_text(element_css, field_name_1,MEDIUM_WAIT_TIME)
            
        report_obj.double_click_on_datetree_item(field_name_2, 1)
        active_chart_obj.wait_for_visible_text(element_css, field_name_2,MEDIUM_WAIT_TIME)
            
        report_obj.double_click_on_datetree_item(field_name_3, 1)
        active_chart_obj.wait_for_visible_text(element_css, field_name_3,MEDIUM_WAIT_TIME)
            
        report_obj.double_click_on_datetree_item(field_name_4, 1)
        active_chart_obj.wait_for_visible_text(element_css, field_name_4,MEDIUM_WAIT_TIME)
            
        coln_list = ['Category', 'Product', 'Unit Sales', 'Dollar Sales']
        report_obj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 4.1: Verify Category, Product, Unit Sales report.")
            
        """
        Step 4:Click the Page icon in the upper left to create Page 2.
        Insert a Chart.
        Expect to see the following Chart preview panel on Page 2.
        """
        doc_obj.select_or_verify_document_page_menu("New Page")
        active_chart_obj.wait_for_number_of_element(Page2_panel_css, 1,MEDIUM_WAIT_TIME)
            
        report_obj.select_ia_ribbon_item('Insert', 'Chart')
            
        active_chart_obj.verify_x_axis_label_in_preview(['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4'],parent_css=preview2_parent_css,msg='Step 04.01')
        active_chart_obj.verify_y_axis_label_in_preview(['0', '10', '20', '30', '40', '50'],parent_css=preview2_parent_css,msg='Step 04.02')
        active_chart_obj.verify_legends_in_preview(['Series0', 'Series1', 'Series2', 'Series3', 'Series4'],parent_css=preview2_parent_css,msg='Step 04.03')
        active_chart_obj.verify_number_of_risers_in_preview('rect', 1, 25,parent_css=preview2_parent_css,msg='Step 04.05: Verify number of bar risers')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css=preview2_parent_css, msg='Step 04.06')
               
        """
        Step 5:Add fields Category, Product, Budget Units & Budget Dollars to the preview..
        Expect to see the following Chart preview on Page 2.
        """
        field_name_1='Category'
        field_name_2='Product'
        field_name_3='Budget Units'
        field_name_4='Budget Dollars'
            
        element_css_2="#TableChart_2"
            
        report_obj.double_click_on_datetree_item(field_name_1, 1)
        active_chart_obj.wait_for_visible_text(element_css_2, field_name_1,MEDIUM_WAIT_TIME)
            
        report_obj.double_click_on_datetree_item(field_name_2,1)
        active_chart_obj.wait_for_visible_text(element_css_2, field_name_2,MEDIUM_WAIT_TIME)
            
        report_obj.double_click_on_datetree_item(field_name_3,1)
        active_chart_obj.wait_for_visible_text(element_css_2, field_name_3,MEDIUM_WAIT_TIME)
            
        report_obj.double_click_on_datetree_item(field_name_4,1)
        active_chart_obj.wait_for_visible_text(element_css_2, field_name_4,MEDIUM_WAIT_TIME)
            
        """chart verification"""
            
        active_chart_obj.verify_x_axis_label_in_preview(['Coffee : Capuccino', 'Coffee : Espresso'],parent_css=preview2_parent_css,msg='Step 05.01')
        active_chart_obj.verify_y_axis_label_in_preview(['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M'],parent_css=preview2_parent_css,msg='Step 05.02')
        active_chart_obj.verify_legends_in_preview(['Unit Sales', 'Dollar Sales'],parent_css=preview2_parent_css,msg='Step 05.03')
        active_chart_obj.verify_number_of_risers_in_preview('rect', 1, 4,parent_css=preview2_parent_css,msg='Step 05.04: Verify number of bar risers')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css=preview2_parent_css, msg='Step 05.05')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g0!mbar!']", 'pale_green', parent_css=preview2_parent_css, msg='Step 05.06')
            
        """
        Step 6:Save the document as C5852860.fex
        """
        active_chart_obj.save_as_chart_from_menubar(Testcase_ID)
            
        """Step 7:Open the saved C5852860.fex using below API
        http://machine:port/alias/tools/portlets/resources/markup/sharep/SPEditorBoot.jsp?folderPath=IBFS%253A%252FWFC%252FRepository%252FP116_S10670/G432673description=C5852860&itemName=C5852860.fex&isReferenced=true&type=items
        Change the Keyword/value pair SHOW_GLOBALFILTER=OFF to SHOW_GLOBALFILTER=ON.
        Save and execute.
            
        """
        report_obj.api_logout()
        webfocus_editor_obj.invoke_fex_using_text_editor(folder_name,Testcase_ID,'mrid','mrpass')
        webfocus_editor_obj.find_and_replace_in_text_editor("SHOW_GLOBALFILTER=OFF","SHOW_GLOBALFILTER=ON")
        webfocus_editor_obj.click_text_editor_ribbon_button('Save')
        report_obj.api_logout()
          
        """
        Expect to see the following Dashboard with Text Box and Report on Page 1.
        """
        report_obj.run_fex_using_api_url(folder_name,Testcase_ID,'mrid','mrpass',run_table_css='#ITableData0 #TCOL_0_C_0 span',wait_time=90)
        utill_obj.verify_object_visible(filter_css,True,"Step:7.1 verify active filter icon is available")
        #report_obj.create_table_data_set("#ITableData0",Testcase_ID+"_1.xlsx")
        report_obj.verify_table_data_set("#ITableData0", Testcase_ID+"_1.xlsx",msg="Step:7.2 verify table dataset for report1")
        active_report_obj.verify_page_summary(0,"10of10records,Page1of1",msg="Step:7.3 verify page summary")
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        active_chart_obj.wait_for_number_of_element(chart_run_parent_css,1,SHORT_WAIT_TIME)
        active_chart_obj.verify_x_axis_label_in_run_window(chart_xaxis_run,parent_css=chart_run_parent_css,msg='Step:7.4')
        active_chart_obj.verify_y_axis_label_in_preview(chart_yaxis_run,parent_css=chart_run_parent_css,msg='Step:7.5')
        active_chart_obj.verify_x_axis_title_in_run_window(['Category : Product'],chart_run_parent_css,msg="Step:7.6")
        active_chart_obj.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], chart_run_parent_css, 2, msg="Step:7.7")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 20,parent_css=chart_run_parent_css,msg='Step 07.08: Verify number of bar risers')
        
        
        """
        Step 8:Click the Global Filter icon, select Add Condition, select Category, then from the dropdown pick 'Gifts'.
        Expect to see the following Filter menu on Page 1.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 1')
        core_utill_obj.python_left_click(utill_obj.validate_and_get_webdriver_object(filter_css,'Filter_icon'))
        active_report_obj.add_global_condition_field('Category','0_globalop_x__0')
        utill_obj.synchronize_with_number_of_element(add_filter_css,1,45)
        active_report_obj.create_filter(1,'Equals',value1='Gifts')
        
        
        """
        Step 9:Click the Filter button.
        Expect to see the following Filtered Report on Page 1 contain only Gifts.
        """
        active_report_obj.filter_button_click('Filter')
        time.sleep(2)
        #report_obj.create_table_data_set("#ITableData0",Testcase_ID+"_2.xlsx")
        report_obj.verify_table_data_set("#ITableData0", Testcase_ID+"_2.xlsx",msg="Step:9.2 verify table dataset for report2")
        
        
        """
        Step 10:Switch to Page 2.
        Expect to see the following Filtered Chart on Page 2 contain only Gifts.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        axis_css="#MAINTABLE_wbody1_f text[class='xaxisOrdinal-labels!g3!mgroupLabel!']"
        active_chart_obj.wait_for_visible_text(axis_css,'Gifts : The...', 45)
        active_chart_obj.verify_x_axis_label_in_run_window(['Gifts : Coff...', 'Gifts : Coff...', 'Gifts : Mug', 'Gifts : The...'],parent_css=chart_run_parent_css,msg='Step:8.4')
        active_chart_obj.verify_y_axis_label_in_preview(['0', '1M', '2M', '3M', '4M', '5M'],parent_css=filter_parent_css,msg='Step:10.1')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 8,parent_css=filter_parent_css,msg='Step 10.2: Verify number of bar risers')
        
        """
        Step 11:Switch back to Page 1.
        Click the Add Condition, select Product, change the operator to Not Equal, then from the drop-down select Thermos.
        Click the Filter button.
        """
        """
        Expect to see the Report on Page 1 with Thermos eliminated from the Category Gifts.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 1')
        time.sleep(2)
        active_report_obj.add_global_condition_field('Product','0_globalop_0')
        utill_obj.synchronize_with_number_of_element(add_filter_css,1,45)
        active_report_obj.create_filter(2,'Not equal',value1='Thermos')
        active_report_obj.filter_button_click('Filter')
        
        #report_obj.create_table_data_set("#ITableData0",Testcase_ID+"_3.xlsx")
        report_obj.verify_table_data_set("#ITableData0", Testcase_ID+"_3.xlsx",msg="Step:11.1 verify table dataset for report2")

        
        """
        Step 12:Switch to Page 2.
        Expect to see the Chart on Page 2 with Thermos eliminated from the Category Gifts.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        time.sleep(2)
        active_chart_obj.verify_x_axis_label_in_run_window(['Gifts : Coffee Grinder', 'Gifts : Coffee Pot', 'Gifts : Mug'],parent_css=filter_parent_css,msg='Step:12')
        active_chart_obj.verify_y_axis_label_in_preview(['0', '1M', '2M', '3M', '4M', '5M'],parent_css=filter_parent_css,msg='Step:12.1')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 6,parent_css=filter_parent_css,msg='Step 12.2: Verify number of bar risers')
        
        """
        Step 13:Click on Clear All button and click on the Global Filter x button to close the Global Filter menu.
        Expect to see Global Filter menu removed from the Chart on Page 2.
        """
        """
        Expect to see Global Filter menu removed from the Chart on Page 1.
        """
        
        doc_obj.select_active_document_page_layout_menu_run_window('Page 1')
        time.sleep(2)
        active_report_obj.filter_button_click('Clear All')
        utill_obj.synchronize_with_number_of_element(menu_css,1,20)
        active_report_obj.close_filter_dialog()
        utill_obj.verify_object_visible(filter_pop_up_css, False, "Step 13:Filter menu removed from the filter dialog")
        report_obj.verify_table_data_set("#ITableData0", Testcase_ID+"_1.xlsx",msg="Step:13.1 verify table dataset for report1")
        active_report_obj.verify_page_summary(0,"10of10records,Page1of1",msg="Step:13.2 verify page summary")
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        axis_1_css="#MAINTABLE_wbody1_f text[class='xaxisOrdinal-labels!g9!mgroupLabel!']"
        active_chart_obj.wait_for_visible_text(axis_1_css,"Gifts : The...",45)
        active_chart_obj.verify_x_axis_label_in_run_window(chart_xaxis_run,parent_css=chart_run_parent_css,msg='Step:13.3')
        active_chart_obj.verify_y_axis_label_in_preview(chart_yaxis_run,parent_css=chart_run_parent_css,msg='Step:13.4')
        active_chart_obj.verify_x_axis_title_in_run_window(['Category : Product'],chart_run_parent_css,msg="Step:13.5")
        active_chart_obj.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], chart_run_parent_css, 2, msg="Step:13.6")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 20,parent_css=filter_parent_css,msg='Step 13.7: Verify number of bar risers')
        
        
        """
        Step 14:Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()