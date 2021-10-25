'''
Created on Jan 18, 2019

@author: Vpriya

Testsuite =  http://172.19.2.180/testrail/index.php?/suites/view/10670&group_by=cases:section_id&group_id=432673&group_order=asc
Testcase id=http://172.19.2.180/testrail/index.php?/cases/view/5823947
TestCase Name = Add Global filter in a Document for charts (GRMERGE=ADVANCED).
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import active_chart
from common.wftools import active_report
from common.wftools import document
from common.lib import utillity
from common.lib import core_utility
from common.pages import webfocus_editor
import time

class C5823947_TestClass(BaseTestCase):

    def test_C5823947(self):
        
        """
        CLASS OBJECTS
        """
        
        Testcase_ID="C5823947"
        doc_obj=document.Document(self.driver)
        report_obj=report.Report(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        webfocus_editor_obj=webfocus_editor.WebfocusEditor(self.driver)
        active_report_obj=active_report.Active_Report(self.driver)
        project_id=core_utill_obj.parseinitfile('project_id')
        suite_id=core_utill_obj.parseinitfile('suite_id')
        group_id=core_utill_obj.parseinitfile('group_id')
        
        """
        CSS
        """
        chart_css="#TableChart_1"
        add_filter_css="[class='arFilter']"
        filter_css=".arDashboardBar .arDashboardBarGlobalButton [title='Global Filter'] img"
        canvas_container_css="#canvasContainer"
        chart_1_run_css="#MAINTABLE_wbody0_f"
        chart_2_run_css="#MAINTABLE_wbody1_f"
        parent_run_css2="#MAINTABLE_wbodyMain1"
        
        """
        TESTCASE VARIABLES
        """
        folder_name=project_id+"_"+suite_id+"/"+group_id
        MEDIUM_WAIT_TIME=45
        SHORT_WAIT_TIME=10
        expected_x_title_list=['State']
        expected_y_title_list=['Unit Sales']
        expected_X_label_list=['CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA']
        expected_y_label_list=['0', '20K', '40K', '60K', '80K', '100K']
        
        expected_x_title_list2=['State : Category']
        expected_y_title_list2=['Unit Sales']
        expected_x_label_list2=['CA : Coffee', 'CT : Coffee', 'FL : Coffee', 'GA : Coffee', 'IL : Coffee', 
                                'MA : Coffee', 'MO : Coffee', 'NY : Coffee', 'TN : Coffee', 'TX : Coffee', 
                                'WA : Coffee']
        expected_y_label_list2=['0', '20K', '40K', '60K', '80K', '100K']
        expected_x_run_label_list=['CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA']
        expected_y_run_label_list=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K']
        expected_x_run_label_list2=['CA : Coffee', 'CA : Food', 'CA : Gifts', 'CT : Coffee', 'CT : Food', 'CT : Gifts', 
                                    'FL : Coffee', 'FL : Food', 'FL : Gifts', 'GA : Coffee', 'GA : Food', 'GA : Gifts', 
                                    'IL : Coffee', 'IL : Food', 'IL : Gifts', 'MA : Coffee', 'MA : Food', 'MA : Gifts', 'MO : Coffee', 
                                    'MO : Food', 'MO : Gifts', 'NY : Coffee']
        expected_y_run_label_list2=['0', '40K', '80K', '120K', '160K', '200K', '240K', '280K']
        filtered_x_label = ['FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA']
        filtered_y_label =  ['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        filtered_x_label_two = ['FL : Coffee', 'FL : Food', 'FL : Gifts', 'GA : Coffee', 'GA : Food', 'GA : Gifts', 
                                'IL : Coffee', 'IL : Food', 'IL : Gifts', 'MA : Coffee', 'MA : Food', 'MA : Gifts', 
                                'MO : Coffee', 'MO : Food', 'MO : Gifts', 'NY : Coffee', 'NY : Food', 'NY : Gifts', 'TN : Coffee', 'TN : Food', 'TN : Gifts']
        filtered_y_label_two = ['0', '30K', '60K', '90K', '120K', '150K']
        
        """
        Step 1:Create a new Document using the ggsales file.
        Select Active Report as the Output Format
        http://machine:port/{alias}/ia?tool=document&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116_S10670%2FG432673%2F
        """
        report_obj.invoke_ia_tool_using_new_api_login("Document", "ibisamp/ggsales")
                 
        """
        Step 2:From the insert menu icon, add a Text Box and insert the text 
        "Global Filter for Document containing Charts".
        Expect to see the following Document canvas with the Text Box added.
        """
        report_obj.select_ia_ribbon_item('Insert','text_box')
        active_chart_obj.wait_for_number_of_element("#theCanvas #Text_1", 1, 35)
        doc_obj.resizing_document_component('0.25', '3.7')
        doc_obj.enter_text_in_document_Textbox('Text_1', 'Global Filter for Document containing Charts')
        time.sleep(2)
        doc_obj.verify_text_in_document_Textbox('#Text_1', 'Global Filter for Document containing Charts', "Step 02:01: Verify textbox value")
                
        """
        Step 3:Use the Insert button to add a Chart underneath the TextBox.
        Add Unit Sales as the measure and State as the X Axis sort field..
        Expect to see the following Chart preview pane appear.
        """
        report_obj.select_ia_ribbon_item('Insert', 'Chart')
        utill_obj.synchronize_with_number_of_element(chart_css, 1,SHORT_WAIT_TIME)
        doc_obj.drag_drop_document_component('#Text_1', '#TableChart_1', 0, 20, target_drop_point='middle')
             
        field_name_1='Unit Sales'
        field_name_2='State'
             
        element_css="#TableChart_1"
         
        report_obj.double_click_on_datetree_item(field_name_1, 1)
        active_chart_obj.wait_for_visible_text(element_css, field_name_1,MEDIUM_WAIT_TIME)
         
        report_obj.double_click_on_datetree_item(field_name_2, 1)
        active_chart_obj.wait_for_visible_text(element_css, field_name_2,MEDIUM_WAIT_TIME)
         
        active_chart_obj.verify_x_axis_title_in_preview(expected_x_title_list,msg="Step:03 Verify x axis title")
        active_chart_obj.verify_y_axis_title_in_preview(expected_y_title_list,msg="Step:03.01 verify y axis title")
        active_chart_obj.verify_x_axis_label_in_preview(expected_X_label_list,msg="Step:03.02 verify x axis label list")
        active_chart_obj.verify_y_axis_label_in_preview(expected_y_label_list,msg="Step:03.03 Verify y axis label")
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s0!g0!mbar!"]','bar_blue',msg="Step:03.04 verify colour of the risers")
        active_chart_obj.verify_number_of_risers_in_preview("rect", 1, 11,msg="step:03.05 Number of risers in run window")
         
        """       
        Step 4:Click the Page button at the top left to create a second page for the Document.
        Expect to see a blank canvas for Page 2.
        """
        doc_obj.select_or_verify_document_page_menu("New Page")
        canvas_container_elem=utill_obj.validate_and_get_webdriver_object(canvas_container_css,"Canvas and container object")
        canvas_text=canvas_container_elem.text
        actual_canvas_area=''
        utill_obj.asequal(canvas_text,actual_canvas_area,"Step.4.1:Expect to see a blank canvas for Page 2")
         
        """
        Step 5:Using the Insert button, add another Chart to the canvas.
        Select fields State and Category for the X Axis and Unit Sales for the measure.
        Move the Chart slightly upwards, so that the entire Chart preview is visible.
        """
        report_obj.select_ia_ribbon_item('Insert', 'Chart')
         
        field_name_1='State'
        field_name_2='Category'
        field_name_3='Unit Sales'
         
        element_css_2="#TableChart_2"
         
        report_obj.double_click_on_datetree_item(field_name_1, 1)
        active_chart_obj.wait_for_visible_text(element_css_2, field_name_1,MEDIUM_WAIT_TIME)
         
        report_obj.double_click_on_datetree_item(field_name_2, 1)
        active_chart_obj.wait_for_visible_text(element_css_2, field_name_2,MEDIUM_WAIT_TIME)
         
        report_obj.double_click_on_datetree_item(field_name_3, 1)
        active_chart_obj.wait_for_visible_text(element_css_2, field_name_3,MEDIUM_WAIT_TIME)
 
        """
        Expect to see the preview pane for the Page 2 Chart.
        """
        active_chart_obj.verify_x_axis_title_in_preview(expected_x_title_list2,parent_css=element_css_2,msg="Step:05 Verify x axis title for chart2")
        active_chart_obj.verify_y_axis_title_in_preview(expected_y_title_list2,parent_css=element_css_2,msg="Step:05.1 Verify y axis title for chart2")
        active_chart_obj.verify_x_axis_label_in_preview(expected_x_label_list2, parent_css=element_css_2,msg="Step:05.02 Verify x axis label for chart2")
        active_chart_obj.verify_y_axis_label_in_preview(expected_y_label_list2, parent_css=element_css_2,msg="Step:05.03 Verify y axis label for chart2")
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css=element_css_2,msg="Step:05.04 Verify chart colour for chart2")
        active_chart_obj.verify_number_of_risers_in_preview("rect", 1, 11,parent_css=element_css_2,msg="step:05.05 Number of risers in run window")
         
        """
        Step 6:Save the report as C5823947.fex and run the report
        """
        active_chart_obj.save_as_chart_from_menubar(Testcase_ID)
         
        """
        Step 7:Edit the saved Fex with the Text Editor and change the Keyword/Value combination from SHOW_GLOBALFILTER=OFF to SHOW_GLOBALFILTER=ON.
        http://machine:port/alias/tools/portlets/resources/markup/sharep/SPEditorBoot.jsp?folderPath=IBFS%253A%252FWFC%252FRepository%252FP116_S10670/G432673description=C5823947&itemName=C5823947.fex&isReferenced=true&type=items
        Expect to see the changed line in each saved Fex.
        """
        """
        Step 8:Save each changed version and exit the editor.
        """
        report_obj.api_logout()
        webfocus_editor_obj.invoke_fex_using_text_editor(folder_name,Testcase_ID,'mrid','mrpass')
        webfocus_editor_obj.find_and_replace_in_text_editor("SHOW_GLOBALFILTER=OFF","SHOW_GLOBALFILTER=ON")
        webfocus_editor_obj.click_text_editor_ribbon_button('Save')
        report_obj.api_logout()

        """
        Step 9:Execute the saved Document(GLOBALFILTER=ON)
        Expect to see the following initial display for each version.
        Page 1 containing 11 Bars:
        """
        report_obj.run_fex_using_api_url(folder_name,Testcase_ID,'mrid','mrpass',run_table_css=chart_1_run_css,wait_time=90)
        active_chart_obj.verify_x_axis_title_in_run_window(expected_x_title_list,parent_css=chart_1_run_css,msg="Step:09 Verify x axis title")
        active_chart_obj.verify_y_axis_title_in_run_window(expected_y_title_list,parent_css=chart_1_run_css,msg="Step:09.1 Verify y axis title")
        active_chart_obj.verify_x_axis_label_in_run_window(expected_x_run_label_list, parent_css=chart_1_run_css,msg="Step:09.02 Verify x axis label")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_y_run_label_list, parent_css=chart_1_run_css,msg="Step:09.03 Verify x axis label")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css=chart_1_run_css,msg="Step:09.04 Verify chart colour for chart2")
        active_chart_obj.verify_number_of_risers_in_run_window("rect", 1, 11,parent_css=chart_1_run_css,msg="step:09.05 Number of risers in run window")
        
        """
        Page 2 containing 33 Bars, 3 Categories for each of the 11 States:
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        active_chart_obj.wait_for_number_of_element("#MAINTABLE_wbody1_f text[class^='xaxis']", 34, active_chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_title_in_run_window(expected_x_title_list2,parent_css=chart_2_run_css,msg="Step:09.06 Verify x axis title")
        active_chart_obj.verify_y_axis_title_in_run_window(expected_y_title_list2,parent_css=chart_2_run_css,msg="Step:09.07 Verify y axis title")
        active_chart_obj.verify_x_axis_label_in_run_window(expected_x_run_label_list2, parent_css=chart_2_run_css,msg="Step:09.08 Verify x axis label")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_y_run_label_list2, parent_css=chart_2_run_css,msg="Step:09.09 Verify x axis label")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css=chart_2_run_css,msg="Step:09.10 Verify chart colour for chart2")
        active_chart_obj.verify_number_of_risers_in_run_window("rect", 1, 33,parent_css=chart_2_run_css,msg="step:09.11 Number of risers in run window")
        
        """
        10:Tap the Global Filter icon to apply a Global filter to the Document.
        Expect to see the Global Filter panel appear.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 1')
        core_utill_obj.python_left_click(utill_obj.validate_and_get_webdriver_object(filter_css,'Filter_icon'))
        active_report_obj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 10.1: Verify Filter that the selection menu appears:")
        active_report_obj.move_active_popup('1', '350', '120')
        
        """
        11:Click the Add Condition tab and select State as the Filter field.
        Change the operator from Equals to Not equal.
        From the drop down list of values select CA & CT for exclusion.
        """
        
        active_report_obj.add_global_condition_field('State','0_globalop_x__0')
        utill_obj.synchronize_with_number_of_element(add_filter_css,1,45)
        active_report_obj.create_filter(1,'Not equal',value1='CA',value2='CT')
        active_report_obj.verify_filter_selection_dialog(True,msg="Step11.1")
        
        """
        Step 12:Click the Filter button to apply the selections.
        Expect to see the following Filtered reports.
        Page 1 containing 9 Bars, with CA & CT removed.
        """
        active_report_obj.filter_button_click('Filter')
        active_chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0_f text[class^='xaxis']", 10, active_chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(filtered_x_label, msg='Step 12.1: Verify x axis labels')
        active_chart_obj.verify_y_axis_label_in_run_window(filtered_y_label, msg='Step 12.2: Verify y axis label')
        active_chart_obj.verify_x_axis_title_in_run_window(['State'], msg='Step 12.3: Verify x title')
        active_chart_obj.verify_y_axis_title_in_run_window(['Unit Sales'], msg='Step 12.4: Verify y title')
        active_chart_obj.verify_number_of_risers_in_run_window('rect',  1, 9, '#MAINTABLE_wbody0_f', 'Step 12.5: Verify the 9 bars')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window('rect[class="riser!s0!g0!mbar!"]', 'bar_blue', '#MAINTABLE_wbody0_f', attribute='fill', msg='Step 12.6: Verify chart color')
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        
        """
        Page 2 containing 27 Bars, with CA & CT removed.
        """
        
        active_chart_obj.wait_for_number_of_element("#MAINTABLE_wbody1_f text[class^='xaxis']", 28, active_chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(filtered_x_label_two, parent_css=parent_run_css2, msg='Step 12.7: Verify x axis labels')
        active_chart_obj.verify_y_axis_label_in_run_window(filtered_y_label_two, parent_css=parent_run_css2,  msg='Step 12.8: Verify y axis label')
        active_chart_obj.verify_x_axis_title_in_run_window(['State : Category'], parent_css=parent_run_css2, msg='Step 12.9: Verify x title')
        active_chart_obj.verify_y_axis_title_in_run_window(['Unit Sales'], parent_css=parent_run_css2,  msg='Step 12.10: Verify y title')
        active_chart_obj.verify_number_of_risers_in_run_window('rect',  1, 27, '#MAINTABLE_wbody1_f', 'Step 12.11: Verify the 27 riser bars')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window('rect[class="riser!s0!g0!mbar!"]', 'bar_blue', '#MAINTABLE_wbody1_f', attribute='fill', msg='Step 12.12: Verify chart color')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 12.13: Verify the tool items', parent_css='#MAINTABLE_wmenu1' )
        doc_obj.select_active_document_page_layout_menu_run_window('Page 1')
        active_chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0_f text[class^='xaxis']", 10, active_chart_obj.chart_medium_timesleep)
        """
        13:Click on Clear All button and click on the Global Filter x button to close
        Expect to see the original reports, with all States appearing.
        """
        active_report_obj.filter_button_click('Clear All')
        active_chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0_f text[class^='xaxis']", 12, active_chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_x_run_label_list, msg='Step 13.01:Verify x axis labels')
        active_chart_obj.verify_y_axis_label_in_run_window(expected_y_run_label_list, msg='Step 13.02: Verify y axis label')
        active_chart_obj.verify_x_axis_title_in_run_window(expected_x_title_list, msg='Step 13.04: Verify x title')
        active_chart_obj.verify_y_axis_title_in_run_window(expected_y_title_list, msg='Step 13.05: Verify y title')
        active_chart_obj.verify_number_of_risers_in_run_window('rect',  1, 11, '#MAINTABLE_wbody0_f', 'Step 13.06: Verify the 11 bars')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window('rect[class="riser!s0!g0!mbar!"]', 'bar_blue', '#MAINTABLE_wbody0_f', attribute='fill', msg='Step 13.07: Verify chart color')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 13.08: Verify the tool items', parent_css='#MAINTABLE_wmenu0' )
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        active_chart_obj.wait_for_number_of_element("#MAINTABLE_wbody1_f text[class^='xaxis']", 34, active_chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_x_run_label_list2, parent_css=parent_run_css2, msg='Step 13.09: Verify x axis labels')
        active_chart_obj.verify_y_axis_label_in_run_window(expected_y_run_label_list2, parent_css=parent_run_css2,  msg='Step 13.10: Verify y axis label')
        active_chart_obj.verify_x_axis_title_in_run_window(expected_x_title_list2, parent_css=parent_run_css2, msg='Step 13.11: Verify x title')
        active_chart_obj.verify_y_axis_title_in_run_window(expected_y_title_list2, parent_css=parent_run_css2,  msg='Step 13.12: Verify y title')
        active_chart_obj.verify_number_of_risers_in_run_window('rect',  1, 33, chart_2_run_css, 'Step 13.13: Verify the riser bar')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window('rect[class="riser!s0!g0!mbar!"]', 'bar_blue', '#MAINTABLE_wbody1_f', attribute='fill', msg='Step 13.14: Verify chart color')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 13.15: Verify the tool items', parent_css='#MAINTABLE_wmenu1' )
        
        """
        Step 14:Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
if __name__ == '__main__':
    unittest.main()