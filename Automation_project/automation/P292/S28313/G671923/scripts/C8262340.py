'''
Created on September 26, 2019

@author: VN14982.
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262340
TestCase Name = Date fields day format
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer_chart import Designer_Chart, Designer_calculation_edit_format
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.text_editor import wf_texteditor
from common.lib import utillity
from common.lib import core_utility
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables


class C8262340_TestClass(BaseTestCase):
    
    def test_C8262340(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        designer_chart_obj=Designer_Chart(self.driver)
        designer_calculation_edit=Designer_calculation_edit_format(self.driver)
        main_page_obj = Wf_Mainpage(self.driver)
        login_page = Login(self.driver)
        text_editor = wf_texteditor(self.driver)
        g_var = Global_variables
        wf_locator = WfMainPageLocators
        project_id = core_utill_obj.parseinitfile('project_id')
        suite_id = core_utill_obj.parseinitfile('suite_id')
        group_id = core_utill_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        
        
        def Query_bucket_tooltip(Query_bucket_Field,expected_tooltip,msg):
            Field_object=self.driver.find_element_by_css_selector('div[data-ibx-name="bucketPills"] div[title*="{0}"]'.format(Query_bucket_Field))
            Field_tooltip = Field_object.get_attribute('title').replace('\n','').strip()
            utillobj.asin(Field_tooltip,expected_tooltip,msg)
        
        step1=""" Step 1: Launch the API to create new Designer Chart with empdata master file.
                http://machine:port/alias/designer?is508=false&master=ibisamp%2Fempdata&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api("ibisamp/empdata")
        utillobj.synchronize_until_element_is_visible("[id*='chartpreview'] rect[class*='riser']", designer_chart_obj.chart_long_timesleep)
        utillobj.capture_screenshot('01.00', step1)
    
        step2=""" Step 2: Click on the vertical dots to the right of Dimensions and click on New calculation
        """
        utillobj.synchronize_until_element_is_visible("div[class*='metadata-container'][class*='dimension-tree-box']", designer_chart_obj.home_page_medium_timesleep)
        designer_chart_obj.select_new_calculation_from_dimensions_or_measures('dimensions')
        utillobj.capture_screenshot('02.00', step2)
         
        step3=""" Step 3: Click Edit format button
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        utillobj.capture_screenshot('03.00', step3)
         
        step4=""" Step 4: Click on Data Type (Date) 12/31/2018
        """
        designer_calculation_edit.select_datatype_in_dialog('date')
        utillobj.capture_screenshot('04.00', step4)
         
        step5="""Click on Date format drop down and select "31(day)"
        """
        designer_calculation_edit.select_date_format_in_date('31 (day)')
        utillobj.capture_screenshot('05.00', step5)
         
        step6=""" Step 6: Click OK
        """
        designer_calculation_edit.close_dialog('OK')
        utillobj.capture_screenshot('06.00', step6)
         
        step7=""" Step 7: Double click on HIREDATE in Field list
        """
        designer_chart_obj.double_click_on_calculation_fields('HIREDATE')
        utillobj.capture_screenshot('07.00', step7)
         
        step8=""" Step 8: Click OK to close the calculator
        """
        designer_chart_obj.click_button_on_calculation('OK')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('08.00', step8)
         
        step9 ="""step 9:Select "Grid Chart" from chart picker component
        """
        designer_chart_obj.select_chart_from_chart_picker('datagrid')
        utillobj.synchronize_until_element_is_visible('.innerTable',designer_chart_obj.home_page_medium_timesleep)
        utillobj.capture_screenshot('09.00', step9)
         
        step10 ="""Double click "Dept" and "Calculation_1"
        Fields are added to grid chart
        """
        designer_chart_obj.double_click_on_dimension_field("DEPT")
        utillobj.synchronize_with_visble_text('.rowTitle','DEPT',designer_chart_obj.home_page_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('Calculation_1')
        utillobj.synchronize_with_visble_text('.colHeaderScroll','Calculation_1',designer_chart_obj.home_page_medium_timesleep)
        designer_chart_obj.create_data_grid_set(g_var.current_test_case)
        designer_chart_obj.verify_data_grid_set(g_var.current_test_case,"step 10.01")
        utillobj.capture_screenshot('10.00', step10,True)
         
        step11 ="""Right click Calculation_1 under Measure > select edit calculation
        """
        designer_chart_obj.right_click_on_measures_field('Calculation_1','Edit calculation...')
        utillobj.synchronize_until_element_is_visible(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('11.00', step11)
         
        step12 ="""Click Edit format button
        Verify correct format is set
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        designer_calculation_edit.verify_selected_datatype_in_dialog('date', '12.00')
        designer_calculation_edit.verify_date_format_in_date('31 (day)','12.02')
        utillobj.capture_screenshot('12.00', step12,True)
         
        step13 ="""Click Cancel (2X)
        """
        designer_calculation_edit.close_dialog('Cancel')
        designer_chart_obj.click_button_on_calculation('Cancel')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('13.00', step13)
         
        step14 ="""Click Preview button to run Designer Chart
        """
        designer_chart_obj.click_toolbar_item('Preview')
        core_utill_obj.switch_to_frame(frame_css='iframe[src*="TableChart_1"] ')
        utillobj.synchronize_until_element_is_visible("[class ='riser!s0!g0!mcellFill!r2!c0!']",designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('14.00',step14)
         
        step15 = """Hover over any values under Calculation_1
        Verify the tooltip
        """
        designer_chart_obj.verify_data_grid_tooltip('13',['DEPT:CONSULTING', 'Calculation_1:13'], msg="Step:0.15")
        utillobj.capture_screenshot('15.00',step15,True)
         
        step16 = """Click blue color button to go back to designer chart and Click Save
        """
        core_utill_obj.switch_to_default_content()
        designer_chart_obj.go_back_to_design_from_preview()
        utillobj.capture_screenshot('16.00',step16)
         
        step17 = """Click Save and Enter title as "C8262340" > Save
        """
        designer_chart_obj.save_as_from_application_menu('C8262340')
        utillobj.capture_screenshot('17.00',step17)
         
        step18 = """Logout using API:
        http://machine:port/alias/service/wf_security_logout.jsp.
        """
        designer_chart_obj.api_logout()
        utillobj.capture_screenshot('18.00',step18)
        
        step19 ="""Open the fex in Text editor
        Verify format in the syntax
        """
        login_page.invoke_home_page('mrid', 'mrpass')
        main_page_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(wf_locator.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Domains')
        main_page_obj.expand_repository_folder(folder_path)
        main_page_obj.right_click_folder_item_and_select_menu(g_var.current_test_case, context_menu_item_path='Edit with text editor')
        core_utill_obj.switch_to_new_window()
        text_editor.verify_line_in_texteditor(['Calculation_1/D=EMPDATA.EMPDATA.HIREDATE;'], '19.00', comparison_type='asin')
        utillobj.capture_screenshot('19.00', step19,True)
        
        step20 ="""Reopen the chart with
        http://machine:port/alias/designer?&item=IBFS:/WFC/Repository/P292_S28313/G671774/c8262340.fex
        Restore successful with calculated fields
        """
        core_utill_obj.switch_to_previous_window()
        designer_chart_obj.api_logout()
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api('c8262340')
        designer_chart_obj.verify_data_grid_set(g_var.current_test_case,"step 20.01")
        utillobj.capture_screenshot('20.00', step20,True)
        
        step21 = """Hover over Calculation_1 under bucket pane
        Verify tooltip
        """
        Query_bucket_tooltip('Calculation_1',['Calculation_1Format: DSegment: EMPDATAName: Calculation_1Alias: Title: Calculation_1Description: Calculation_1'],"Step:21")
        utillobj.capture_screenshot('21.00', step21)
        
        step22=""" Step 22: Logout using API
                http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
        utillobj.capture_screenshot('22.00', step22)
        
 
    if __name__ == "__main__":
        unittest.main()