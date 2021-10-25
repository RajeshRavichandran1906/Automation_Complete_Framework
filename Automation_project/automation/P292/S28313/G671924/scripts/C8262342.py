'''
Created on September 30, 2019

@author: AA14564.
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262342
TestCase Name = Alpha Variable Length field formats
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer_chart import Designer_Chart, Designer_calculation_edit_format
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.text_editor import wf_texteditor
from common.lib import utillity
from common.lib import core_utility
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables


class C8262342_TestClass(BaseTestCase):
    
    def test_C8262342(self):
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
         
        step4=""" Step 4: Change Length to 4093 and Select Variable length check box -
        """
        designer_calculation_edit.select_datatype_in_dialog('alpha')
        designer_calculation_edit.modify_length_value_in_alpha('4093')
        designer_calculation_edit.select_variable_length_check_uncheck_in_alpha('check')
        utillobj.capture_screenshot('04.00', step4)
         
        step5=""" Step 5: Click OK
        """
        designer_calculation_edit.close_dialog('OK')
        utillobj.capture_screenshot('05.00', step5)
         
        step6=""" Step 6: Double click on LASTNAME in Field list
        """
        designer_chart_obj.double_click_on_calculation_fields('LASTNAME')
        utillobj.capture_screenshot('06.00', step6)
         
        step7=""" Step 7: Click OK to close the calculator
                    click on the vertical dots to the right of Dimensions and click on New calculation
        """
        designer_chart_obj.click_button_on_calculation('OK')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.select_new_calculation_from_dimensions_or_measures('dimensions')
        utillobj.capture_screenshot('07.00', step7)
         
        step8=""" Step 8: Click Edit format button
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        utillobj.capture_screenshot('08.00', step8)
         
        step9=""" Step 9: Change Length to 5000 and Select Variable length check box
                NOTE: The length changes to 4093 because of Variable length check box selected
        """
        designer_calculation_edit.select_datatype_in_dialog('alpha')
        designer_calculation_edit.modify_length_value_in_alpha('5000')
        designer_calculation_edit.select_variable_length_check_uncheck_in_alpha('check')
        time.sleep(5)
        designer_calculation_edit.verify_length_value_in_alpha('4093', '09.00')
        utillobj.capture_screenshot('09.00', step9)
         
        step10=""" Step 10: Click OK
        """
        designer_calculation_edit.close_dialog('OK')
        utillobj.capture_screenshot('10.00', step10)
         
        step11=""" Step 11: Double click on FIRSTNAME in Field list
        """
        designer_chart_obj.double_click_on_calculation_fields('FIRSTNAME')
        utillobj.capture_screenshot('11.00', step11)
         
        step12=""" Step 12: Click OK to close Calculator
                    click on the vertical dots to the right of Dimensions and click on New calculation
        """
        designer_chart_obj.click_button_on_calculation('OK')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.select_new_calculation_from_dimensions_or_measures('dimensions')
        utillobj.capture_screenshot('12.00', step12)
         
        step13=""" Step 13: Click Edit format button
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        utillobj.capture_screenshot('13.00', step13)
         
        step14=""" Step 14: Change Length to 50 and Select Variable length check box
        """
        designer_calculation_edit.select_datatype_in_dialog('alpha')
        designer_calculation_edit.modify_length_value_in_alpha('50')
        designer_calculation_edit.select_variable_length_check_uncheck_in_alpha('check')
        utillobj.capture_screenshot('14.00', step14)
         
        step15=""" Step 15: Click OK
        """
        designer_calculation_edit.close_dialog('OK')
        utillobj.capture_screenshot('15.00', step15)
         
        step16=""" Step 16: Double click on TITLE in Field list
        """
        designer_chart_obj.double_click_on_calculation_fields('TITLE')
        utillobj.capture_screenshot('16.00', step16)
         
        step17=""" Step 17: Click OK to close Calculator
                    click on the vertical dots to the right of Dimensions and click on New calculation
        """
        designer_chart_obj.click_button_on_calculation('OK')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.select_new_calculation_from_dimensions_or_measures('dimensions')
        utillobj.capture_screenshot('17.00', step17)
         
        step18=""" Step 18: Click Edit format button
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        utillobj.capture_screenshot('18.00', step18)
         
        step19=""" Step 19: Change Length to 0 and Select Variable length check box
                    NOTE: The length changes to 1 because of Variable length check box selected
        """
        designer_calculation_edit.select_datatype_in_dialog('alpha')
        designer_calculation_edit.modify_length_value_in_alpha('0')
        designer_calculation_edit.select_variable_length_check_uncheck_in_alpha('check')
        time.sleep(5)
        designer_calculation_edit.verify_length_value_in_alpha('1', '19.00')
        utillobj.capture_screenshot('19.00', step19)
         
        step20=""" Step 20: Click OK
        """
        designer_calculation_edit.close_dialog('OK')
        utillobj.capture_screenshot('20.00', step20)
         
        step21=""" Step 21: Double click on LASTNAME in Field list
        """
        designer_chart_obj.double_click_on_calculation_fields('LASTNAME')
        utillobj.capture_screenshot('21.00', step21)
         
        step22=""" Step 22: Click OK to close Calculator
        """
        designer_chart_obj.click_button_on_calculation('OK')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('22.00', step22)
         
        step23=""" Step 23: Double click SALARY, Double click DEPT to add to the chart
        """
        designer_chart_obj.double_click_on_measures_field('SALARY')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box", "SALARY", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_dimension_field('DEPT')
        utillobj.synchronize_until_element_is_visible("[id*='chartpreview'] .risers rect", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(['ACCOUNTING', 'ADMIN SERVICES', 'CONSULTING', 'CUSTOMER SUPPORT', 'MARKETING', 'PERSONNEL', 'PROGRAMMING & DVLPMT', 'SALES'], msg='Step 23.00')
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '100K', '200K', '300K', '400K', '500K', '600K'], msg='Step 23.01')
        designer_chart_obj.verify_x_axis_title_in_preview(['DEPT'], msg='Step 23.02')
        designer_chart_obj.verify_y_axis_title_in_preview(['SALARY'], msg='Step 23.03')
        designer_chart_obj.verify_number_of_risers("[id*='chartpreview'] .risers rect", 1, 8, msg='Step 23.04')
        utillobj.capture_screenshot('23.00', step23)
         
        step24=""" Step 24: Click on Save icon and save as C8262342
        """
        designer_chart_obj.save_as_from_application_menu(g_var.current_test_case)
        utillobj.capture_screenshot('24.00', step24)
         
        step25=""" Step 25: Logout using API
                        http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
        utillobj.capture_screenshot('25.00', step25)
         
        step26=""" Step 26: Open the fex in Text editor
                    https://machine:port/{alias}/TED?rootFolderPath=IBFS:/WFC/Repository&folderPath=IBFS:/WFC/Repository/P292_S28313/G671774&itemName=C8262342.fex
        """
        login_page.invoke_home_page('mrid', 'mrpass')
        main_page_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(wf_locator.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Domains')
        main_page_obj.expand_repository_folder(folder_path)
        main_page_obj.right_click_folder_item_and_select_menu(g_var.current_test_case, context_menu_item_path='Edit with text editor')
        core_utill_obj.switch_to_new_window()
        utillobj.capture_screenshot('26.00', step26)
         
        step27=""" Step 27: Verify lines 4-7 in the code
        """
        text_editor.verify_line_in_texteditor(['Calculation_1/A4093V=EMPDATA.EMPDATA.LASTNAME;'], '27.00', comparison_type='asin')
        text_editor.verify_line_in_texteditor(['Calculation_2/A4093V=EMPDATA.EMPDATA.FIRSTNAME;'], '27.01', comparison_type='asin')
        text_editor.verify_line_in_texteditor(['Calculation_3/A50V=EMPDATA.EMPDATA.TITLE;'], '27.02', comparison_type='asin')
        text_editor.verify_line_in_texteditor(['Calculation_4/A1V=EMPDATA.EMPDATA.LASTNAME;'], '27.03', comparison_type='asin')
        utillobj.capture_screenshot('27.00', step27, expected_image_verify=True)
        core_utill_obj.switch_to_previous_window()
         
        step28=""" Step 28: Logout using API
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
        utillobj.capture_screenshot('28.00', step28)
        
        step29=""" Step 29: Reopen the chart with
                http://machine:port/alias/designer?&item=IBFS:/WFC/Repository/P292_S28313/G671774/c8262342.fex
        """
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api(g_var.current_test_case.lower()+'.fex', tool='workbook')
        utillobj.synchronize_until_element_is_visible("[id*='chartpreview'] .risers rect", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(['ACCOUNTING', 'ADMIN SERVICES', 'CONSULTING', 'CUSTOMER SUPPORT', 'MARKETING', 'PERSONNEL', 'PROGRAMMING & DVLPMT', 'SALES'], msg='Step 29.00')
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '100K', '200K', '300K', '400K', '500K', '600K'], msg='Step 29.01')
        designer_chart_obj.verify_x_axis_title_in_preview(['DEPT'], msg='Step 29.02')
        designer_chart_obj.verify_y_axis_title_in_preview(['SALARY'], msg='Step 29.03')
        designer_chart_obj.verify_number_of_risers("[id*='chartpreview'] .risers rect", 1, 8, msg='Step 29.04')
        utillobj.capture_screenshot('29.00', step29)
        
        step30=""" Step 30: scrolldown in Dimensions with scroll bar, right click Calculation_1, select edit calculation
        """
        designer_chart_obj.right_click_on_dimensions_field('Calculation_1', context_menu_item_path='Edit calculation...')
        utillobj.capture_screenshot('30.00', step30)
        
        step31=""" Step 31: Click Edit format
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        designer_calculation_edit.verify_length_value_in_alpha('4093', '31.00')
        designer_calculation_edit.verify_variable_length_check_uncheck_in_alpha('check', '31.01')
        utillobj.capture_screenshot('31.00', step31)
        
        step32=""" Step 32: Click OK to close data formatter, Click close to close Calculator
                    scrolldown in Dimensions with scroll bar, right click Calculation_2, select edit calculation
        """
        designer_calculation_edit.close_dialog('OK')
        designer_chart_obj.click_button_on_calculation('Cancel')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.right_click_on_dimensions_field('Calculation_2', context_menu_item_path='Edit calculation...')
        utillobj.capture_screenshot('32.00', step32)
        
        step33=""" Step 33: Click Edit format
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        designer_calculation_edit.verify_length_value_in_alpha('4093', '33.00')
        designer_calculation_edit.verify_variable_length_check_uncheck_in_alpha('check', '33.01')
        utillobj.capture_screenshot('33.00', step33)
        
        step34=""" Step 34: Click OK to close data formatter, Click close to close Calculator
                    scrolldown in Dimensions with scroll bar, right click Calculation_3, select edit calculation
        """
        designer_calculation_edit.close_dialog('OK')
        designer_chart_obj.click_button_on_calculation('Cancel')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.right_click_on_dimensions_field('Calculation_3', context_menu_item_path='Edit calculation...')
        utillobj.capture_screenshot('34.00', step34)
        
        step35=""" Step 35: Click Edit format
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        designer_calculation_edit.verify_length_value_in_alpha('50', '35.00')
        designer_calculation_edit.verify_variable_length_check_uncheck_in_alpha('check', '35.01')
        utillobj.capture_screenshot('35.00', step35)
        
        step36=""" Step 36: Click OK to close data formatter, Click close to close Calculator
                    scrolldown in Dimensions with scroll bar, right click Calculation_4, select edit calculation
        """
        designer_calculation_edit.close_dialog('OK')
        designer_chart_obj.click_button_on_calculation('Cancel')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.right_click_on_dimensions_field('Calculation_4', context_menu_item_path='Edit calculation...')
        utillobj.capture_screenshot('36.00', step36)
        
        step37=""" Step 37: Click Edit format
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        designer_calculation_edit.verify_length_value_in_alpha('1', '37.00')
        designer_calculation_edit.verify_variable_length_check_uncheck_in_alpha('check', '37.01')
        utillobj.capture_screenshot('37.00', step37)
        
        step38=""" Step 38: Logout using API
                http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_calculation_edit.close_dialog('OK')
        designer_chart_obj.click_button_on_calculation('Cancel')
        designer_chart_obj.api_logout()
        utillobj.capture_screenshot('38.00', step38)
        
    if __name__ == "__main__":
        unittest.main()