'''
Created on Jan 30, 2019

@author: Magesh

Testsuite =  http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/20311&group_by=cases:section_id&group_id=685341&group_order=asc
Testcase id = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8358935
TestCase Name = Add Global filter to Document for a report and a chart (MERGE=ADVANCED).
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import active_chart
from common.wftools import active_report
from common.wftools import document
from common.wftools import visualization
from common.wftools import wf_mainpage, login
from common.lib import utillity
from common.lib import core_utility
from common.pages import webfocus_editor
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8358935_TestClass(BaseTestCase):

    def test_C8358935(self):
        
        """
        TESTCASE VARIABLES
        """
        Testcase_ID="C8358935"
        doc_obj=document.Document(self.driver)
        report_obj=report.Report(self.driver)
        vis_obj=visualization.Visualization(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        webfocus_editor_obj=webfocus_editor.WebfocusEditor(self.driver)
        active_report_obj=active_report.Active_Report(self.driver)
        wf_mainpage_obj=wf_mainpage.Wf_Mainpage(self.driver)
        login_obj = login.Login(self.driver)
        project_id = utill_obj.parseinitfile('project_id')
        suite_id = utill_obj.parseinitfile('suite_id')
        group_id = utill_obj.parseinitfile('group_id')
            
        """
        COMMON VARIABLES
        """
        folder_name=project_id+'_'+suite_id
        folder_name_path=folder_name+'->'+group_id
        MEDIUM_WAIT_TIME=45
        chart_xaxis_run=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croi...', 'Food : Scone', 'Gifts : Coff...', 'Gifts : Coff...', 'Gifts : Mug', 'Gifts : The...', ]
        chart_yaxis_run=['0', '3M', '6M', '9M', '12M']
        
        """
        COMMON CSS
        """
        report_css="#TableChart_1"
        Page2_panel_css="#singleReportPanel"
        add_filter_css="[class='arFilter']"
        menu_css="#MAINTABLE_wbodyMain0"
        filter_css=".arDashboardBar .arDashboardBarGlobalButton [title='Global Filter'] img"
        preview2_parent_css="#TableChart_2"
        chart_run_parent_css="#MAINTABLE_1"
        filter_parent_css="#MAINTABLE_wbody1_f"
        filter_pop_up_css="#FiltTable1 .arFilterItem"
            
        """
        Step 1: Sign in to WebFOCUS
        http://machine:port/{alias}
        Step 2: Create a new Document using the ggsales file.
        Select Active Report as the Output Format
        http://machine:port/{alias}/ia?tool=document&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116_S10670%2FG432673%2F
        """
        report_obj.invoke_ia_tool_using_new_api_login("Document", "ibisamp/ggsales")
                 
        """
        Step 3: From the insert menu icon, add a Text Box and insert the text 
        "Global Filter for Document containing Report & Chart".
        Expect to see the following Text Box on the canvas..
        """
        vis_obj.select_ribbon_item('Insert','text_box')
        active_chart_obj.wait_for_number_of_element("#theCanvas #Text_1", 1, 35)
        doc_obj.resizing_document_component('0.25', '4.5')
        doc_obj.enter_text_in_document_Textbox('Text_1', 'Global Filter for Document containing Report & Chart')
        time.sleep(2)
        doc_obj.verify_text_in_document_Textbox('#Text_1', 'Global Filter for Document containing Report & Chart', "Step 03:01: Verify textbox value")
                
        """
        Step 4: From the insert menu icon, add a Report to the canvas below the Text Box.
        """
        report_obj.select_ia_ribbon_item('Insert', 'report')
        utill_obj.synchronize_with_number_of_element(report_css, 1,15)
        doc_obj.drag_drop_document_component('#Text_1', '#TableChart_1', 0, 30, target_drop_point='bottom_middle')
        
        """
        Step 5: Select fields Category, Product, Unit Sales & Dollar Sales..
        Expect to see the following canvas with Text Box and Report preview.
        """     
        field_name_list=['Category', 'Product', 'Unit Sales', 'Dollar Sales']
        for field in field_name_list:
            report_obj.double_click_on_datetree_item(field, 1)
            active_chart_obj.wait_for_visible_text(report_css, field, MEDIUM_WAIT_TIME)
        report_obj.verify_report_titles_on_preview(4, 4, "TableChart_1", field_name_list, "Step 5.1: Verify Category, Product, Unit Sales report.")
        report_obj.verify_report_data_set_in_preview("TableChart_1", 2, 4, Testcase_ID+'_DS_01.xlsx', msg="Step 05.2: Verify report dataset")
             
        """
        Step 6: Click the Page icon in the upper left to create Page 2.
        Insert a Chart.
        Expect to see the following Chart preview panel on Page 2.
        """
        doc_obj.select_or_verify_document_page_menu("New Page")
        active_chart_obj.wait_for_number_of_element(Page2_panel_css, 1,MEDIUM_WAIT_TIME)
        report_obj.select_ia_ribbon_item('Insert', 'Chart')
        active_chart_obj.verify_x_axis_label_in_preview(['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4'],parent_css=preview2_parent_css,msg='Step 06.01')
        active_chart_obj.verify_y_axis_label_in_preview(['0', '10', '20', '30', '40', '50'],parent_css=preview2_parent_css,msg='Step 06.02')
        active_chart_obj.verify_legends_in_preview(['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4'],parent_css=preview2_parent_css,msg='Step 06.03')
        active_chart_obj.verify_number_of_risers_in_preview('rect', 1, 25,parent_css=preview2_parent_css,msg='Step 06.05: Verify number of bar risers')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css=preview2_parent_css, msg='Step 06.06')
                
        """
        Step 7: Add fields Category, Product, Budget Units & Budget Dollars to the preview.
        Expect to see the following Chart preview on Page 2.
        """
        field_name_list=['Category', 'Product', 'Budget Units', 'Budget Dollars']
        for field in field_name_list: 
            report_obj.double_click_on_datetree_item(field, 1)
            active_chart_obj.wait_for_visible_text(preview2_parent_css, field, MEDIUM_WAIT_TIME)
             
        """chart verification"""
        active_chart_obj.verify_x_axis_label_in_preview(['Coffee : Capuccino', 'Coffee : Espresso'],parent_css=preview2_parent_css,msg='Step 07.01')
        active_chart_obj.verify_y_axis_label_in_preview(['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M'],parent_css=preview2_parent_css,msg='Step 07.02')
        active_chart_obj.verify_legends_in_preview(['Budget Units', 'Budget Dollars'],parent_css=preview2_parent_css,msg='Step 07.03')
        active_chart_obj.verify_number_of_risers_in_preview('rect', 1, 4,parent_css=preview2_parent_css,msg='Step 07.04: Verify number of bar risers')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css=preview2_parent_css, msg='Step 07.05')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g0!mbar!']", 'pale_green', parent_css=preview2_parent_css, msg='Step 07.06')
             
        """
        Step 8: Save the document as C8358935.fex and logut
        """
        active_chart_obj.save_as_chart_from_menubar(Testcase_ID)
        report_obj.api_logout()  
          
        """
        Step 9: From home page right click C8358935.fex and select edit with text editor and and change GLOBAL FILTER OFF TO ON and click preview.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        utill_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait*5)
        wf_mainpage_obj.expand_repository_folder(folder_name_path)
        wf_mainpage_obj.right_click_folder_item_and_select_menu(item_name=Testcase_ID, context_menu_item_path='Edit with text editor')
        report_obj.switch_to_new_window()
        utill_obj.synchronize_with_number_of_element("div[class*='menu-button'][title='Preview']",1,45)
        webfocus_editor_obj.edit_fex_in_text_editor_using_find_and_replace("SHOW_GLOBALFILTER=OFF", "SHOW_GLOBALFILTER=ON", button_name='replace_all')
        webfocus_editor_obj.click_menu_bar_button(button_name='Preview')
        report_obj.switch_to_new_window()
          
        """
        Expect to see the following Dashboard with Text Box and Report on Page 1.
        """
        utill_obj.synchronize_with_number_of_element(filter_css,1,45)
        utill_obj.verify_object_visible(filter_css,True,"Step:9.1 verify active filter icon is available")
        report_obj.verify_table_data_set("#ITableData0", Testcase_ID+"_DS01.xlsx", msg="Step:9.2 verify table dataset for report1")
        active_report_obj.verify_page_summary(0,"10of10records,Page1of1",msg="Step:9.3 verify page summary")
        
        """
        Step 10: Click the Global Filter icon, select Add Condition, select Category, then from the dropdown pick 'Gifts'. 
        Expect to see the following Filter menu on Page 1.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 1')
        core_utill_obj.python_left_click(utill_obj.validate_and_get_webdriver_object(filter_css,'Filter_icon'))
        active_report_obj.add_global_condition_field('Category','0_globalop_x__0')
        utill_obj.synchronize_with_number_of_element(add_filter_css,1,45)
        active_report_obj.create_filter(1,'Equals',value1='Gifts')
        
        """
        Step 11: Click the Filter button.
        Expect to see the following Filtered Report on Page 1 contain only Gifts.
        """
        active_report_obj.filter_button_click('Filter')
        time.sleep(2)
        report_obj.verify_table_data_set("#ITableData0", Testcase_ID+"_DS02.xlsx", msg="Step:11 verify table dataset for report2")
        
        """
        Step 12: Switch to Page 2.
        Expect to see the following Filtered Chart on Page 2 contain only Gifts.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        utill_obj.synchronize_with_number_of_element(filter_parent_css+" rect[class^='riser']",8,45)
        active_chart_obj.verify_x_axis_label_in_run_window(['Gifts : Coff...', 'Gifts : Coff...', 'Gifts : Mug', 'Gifts : The...'], parent_css=chart_run_parent_css, msg='Step:12.1')
        active_chart_obj.verify_y_axis_label_in_preview(['0', '1M', '2M', '3M', '4M', '5M'], parent_css=filter_parent_css, msg='Step:12.2')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 8, parent_css=filter_parent_css, msg='Step 12.3: Verify number of bar risers')
        
        """
        Step 13: Switch back to Page 1.
        Click the Add Condition, select Product, change the operator to Not Equal, then from the drop-down select Thermos.
        Click the Filter button.
        Expect to see the Report on Page 1 with Thermos eliminated from the Category Gifts.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 1')
        time.sleep(2)
        active_report_obj.add_global_condition_field('Product','0_globalop_0')
        utill_obj.synchronize_with_number_of_element(add_filter_css,1,45)
        active_report_obj.create_filter(2,'Not equal',value1='Thermos')
        active_report_obj.filter_button_click('Filter')
        report_obj.verify_table_data_set("#ITableData0", Testcase_ID+"_DS03.xlsx", msg="Step:13.1 verify table dataset for report2")
        
        """
        Step 14: Switch to Page 2.
        Expect to see the Chart on Page 2 with Thermos eliminated from the Category Gifts.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        time.sleep(2)
        active_chart_obj.verify_x_axis_label_in_run_window(['Gifts : Coffee Grinder', 'Gifts : Coffee Pot', 'Gifts : Mug'],parent_css=filter_parent_css,msg='Step:14')
        active_chart_obj.verify_y_axis_label_in_preview(['0', '1M', '2M', '3M', '4M', '5M'],parent_css=filter_parent_css,msg='Step:14.1')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 6,parent_css=filter_parent_css,msg='Step 14.2: Verify number of bar risers')
        
        """
        Step 15: Click on Clear All button and click on the Global Filter x button to close the Global Filter menu.
        Expect to see Global Filter menu removed from the Chart on Page 2.
        Expect to see Global Filter menu removed from the Chart on Page 1.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 1')
        time.sleep(4)
        active_report_obj.filter_button_click('Clear All')
        utill_obj.synchronize_with_number_of_element(menu_css,1,20)
        active_report_obj.close_filter_dialog()
        utill_obj.verify_object_visible(filter_pop_up_css, False, "Step 15:Filter menu removed from the filter dialog")
        report_obj.verify_table_data_set("#ITableData0", Testcase_ID+"_DS01.xlsx",msg="Step:15.1 verify table dataset for report1")
        active_report_obj.verify_page_summary(0,"10of10records,Page1of1",msg="Step:15.2 verify page summary")
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        axis_1_css="#MAINTABLE_wbody1_f text[class='xaxisOrdinal-labels!g9!mgroupLabel!']"
        active_chart_obj.wait_for_visible_text(axis_1_css,"Gifts : The...",45)
        active_chart_obj.verify_x_axis_label_in_run_window(chart_xaxis_run,parent_css=chart_run_parent_css,msg='Step:15.3')
        active_chart_obj.verify_y_axis_label_in_preview(chart_yaxis_run,parent_css=chart_run_parent_css,msg='Step:15.4')
        active_chart_obj.verify_x_axis_title_in_run_window(['Category : Product'],chart_run_parent_css,msg="Step:15.5")
        active_chart_obj.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], chart_run_parent_css, 2, msg="Step:15.6")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 20,parent_css=filter_parent_css,msg='Step 15.7: Verify number of bar risers')
        utill_obj.switch_to_main_window()
        
        """
        Step 16: Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()