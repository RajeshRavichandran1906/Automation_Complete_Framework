'''
Created on September 25, 2019

@author: AA14564.
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262333
TestCase Name = Date fields YYMD formats
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


class C8262333_TestClass(BaseTestCase):
    
    def test_C8262333(self):
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
        
        step4=""" Step 4: Click on Data Type (Date) 12/31/2018
        """
        designer_calculation_edit.select_datatype_in_dialog('date')
        utillobj.capture_screenshot('04.00', step4)
        
        step5=""" Step 5: Click OK
        """
        designer_calculation_edit.close_dialog('OK')
        utillobj.capture_screenshot('05.00', step5)
        
        step6=""" Step 6: Double click on HIREDATE in Field list
        """
        designer_chart_obj.double_click_on_calculation_fields('HIREDATE')
        utillobj.capture_screenshot('06.00', step6)
        
        step7=""" Step 7: Click OK to close the calculator
        """
        designer_chart_obj.click_button_on_calculation('OK')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('07.00', step7)
        
        step8=""" Step 8: Click on the vertical dots to the right of Dimensions and click on New calculation
        """
        designer_chart_obj.select_new_calculation_from_dimensions_or_measures('dimensions')
        utillobj.capture_screenshot('08.00', step8)
        
        step9=""" Step 9: Click Edit format button
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        utillobj.capture_screenshot('09.00', step9)
        
        step10=""" Step 10: Click on Data Type (Date) 12/31/2018
        """
        designer_calculation_edit.select_datatype_in_dialog('date')
        utillobj.capture_screenshot('10.00', step10)
        
        step11=""" Step 11: Click on drop down for Date separator and select '-' (dash)
        """
        designer_calculation_edit.select_date_separator_in_date("'-' (dash)")
        utillobj.capture_screenshot('11.00', step11)
        
        step12=""" Step 12: Click OK
        """
        designer_calculation_edit.close_dialog('OK')
        utillobj.capture_screenshot('12.00', step12)
        
        step13=""" Step 13: Double click on HIREDATE in Field list
        """
        designer_chart_obj.double_click_on_calculation_fields('HIREDATE')
        utillobj.capture_screenshot('13.00', step13)
        
        step14=""" Step 14: Click OK to close Calculator
        """
        designer_chart_obj.click_button_on_calculation('OK')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('14.00', step14)
        
        step15=""" Step 15: Click on the vertical dots to the right of Dimensions and click on New calculation
        """
        designer_chart_obj.select_new_calculation_from_dimensions_or_measures('dimensions')
        utillobj.capture_screenshot('15.00', step15)
        
        step16=""" Step 16: Click Edit format button
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        utillobj.capture_screenshot('16.00', step16)
        
        step17=""" Step 17: Click on Data Type (Date) 12/31/2018
        """
        designer_calculation_edit.select_datatype_in_dialog('date')
        utillobj.capture_screenshot('17.00', step17)
        
        step18=""" Step 18: Click on drop down for Date separator and select '.' (dot)
        """
        designer_calculation_edit.select_date_separator_in_date("'.' (dot)")
        utillobj.capture_screenshot('18.00', step18)
        
        step19=""" Step 19: Click OK
        """
        designer_calculation_edit.close_dialog('OK')
        utillobj.capture_screenshot('19.00', step19)
        
        step20=""" Step 20: Double click on HIREDATE in Field list
        """
        designer_chart_obj.double_click_on_calculation_fields('HIREDATE')
        utillobj.capture_screenshot('20.00', step20)
        
        step21=""" Step 21: Click OK to close Calculator
        """
        designer_chart_obj.click_button_on_calculation('OK')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('21.00', step21)
        
        step22=""" Step 22: Click on the vertical dots to the right of Dimensions and click on New calculation
        """
        designer_chart_obj.select_new_calculation_from_dimensions_or_measures('dimensions')
        utillobj.capture_screenshot('22.00', step22)
        
        step23=""" Step 23: Click Edit format button
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        utillobj.capture_screenshot('23.00', step23)
        
        step24=""" Step 24: Click on Data Type (Date) 12/31/2018
        """
        designer_calculation_edit.select_datatype_in_dialog('date')
        utillobj.capture_screenshot('24.00', step24)
        
        step25=""" Step 25: Click on drop down for Date separator and select ' ' (space)
        """
        designer_calculation_edit.select_date_separator_in_date("' ' (space)")
        utillobj.capture_screenshot('25.00', step25)
        
        step26=""" Step 26: Click OK
        """
        designer_calculation_edit.close_dialog('OK')
        utillobj.capture_screenshot('26.00', step26)
        
        step27=""" Step 27: Double click on HIREDATE in Field list
        """
        designer_chart_obj.double_click_on_calculation_fields('HIREDATE')
        utillobj.capture_screenshot('27.00', step27)
        
        step28=""" Step 28: Click OK to close Calculator
        """
        designer_chart_obj.click_button_on_calculation('OK')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('28.00', step28)
        
        step29=""" Step 29: Double click SALARY, Double click DEPT
        """
        designer_chart_obj.double_click_on_measures_field('SALARY')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box", "SALARY", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_dimension_field('DEPT')
        utillobj.synchronize_until_element_is_visible("[id*='chartpreview'] .risers rect", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(['ACCOUNTING', 'ADMIN SERVICES', 'CONSULTING', 'CUSTOMER SUPPORT', 'MARKETING', 'PERSONNEL', 'PROGRAMMING & DVLPMT', 'SALES'], msg='Step 29.00')
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '100K', '200K', '300K', '400K', '500K', '600K'], msg='Step 29.01')
        designer_chart_obj.verify_x_axis_title_in_preview(['DEPT'], msg='Step 29.02')
        designer_chart_obj.verify_y_axis_title_in_preview(['SALARY'], msg='Step 29.03')
        designer_chart_obj.verify_number_of_risers("[id*='chartpreview'] .risers rect", 1, 8, msg='Step 29.04')
        utillobj.capture_screenshot('29.00', step29, expected_image_verify=True)
        
        step30=""" Step 30: Click on Save icon and save as C8262333
        """
        designer_chart_obj.save_as_from_application_menu(g_var.current_test_case)
        utillobj.capture_screenshot('30.00', step30)
        
        step31=""" Step 31: Logout using API
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
        utillobj.capture_screenshot('31.00', step31)
        
        step32=""" Step 32: Open the fex in Text editor
                https://machine:port/{alias}/TED?rootFolderPath=IBFS:/WFC/Repository&folderPath=IBFS:/WFC/Repository/P292_S28313/G671774&itemName=c8262333.fex
        """
        login_page.invoke_home_page('mrid', 'mrpass')
        main_page_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(wf_locator.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Domains')
        main_page_obj.expand_repository_folder(folder_path)
        main_page_obj.right_click_folder_item_and_select_menu(g_var.current_test_case, context_menu_item_path='Edit with text editor')
        core_utill_obj.switch_to_new_window()
        utillobj.capture_screenshot('32.00', step32)
        
        step33=""" Step 33: Verify lines 4-7 in the code
        """
        text_editor.verify_line_in_texteditor(['Calculation_1/YYMD=EMPDATA.EMPDATA.HIREDATE;'], '33.00', comparison_type='asin')
        text_editor.verify_line_in_texteditor(['Calculation_2/YYMD-=EMPDATA.EMPDATA.HIREDATE;'], '33.01', comparison_type='asin')
        text_editor.verify_line_in_texteditor(['Calculation_3/YYMD.=EMPDATA.EMPDATA.HIREDATE;'], '33.02', comparison_type='asin')
        text_editor.verify_line_in_texteditor(['Calculation_4/YYMDB=EMPDATA.EMPDATA.HIREDATE;'], '33.03', comparison_type='asin')
        utillobj.capture_screenshot('33.00', step33, expected_image_verify=True)
        core_utill_obj.switch_to_previous_window()
        designer_chart_obj.api_logout()
        
        step34=""" Step 34: Reopen the chart with
                    http://machine:port/alias/designer?&item=IBFS:/WFC/Repository/P292_S28313/G671774/c8262333.fex
        """
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api(g_var.current_test_case.lower()+'.fex', tool='workbook')
        utillobj.synchronize_until_element_is_visible("[id*='chartpreview'] .risers rect", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(['ACCOUNTING', 'ADMIN SERVICES', 'CONSULTING', 'CUSTOMER SUPPORT', 'MARKETING', 'PERSONNEL', 'PROGRAMMING & DVLPMT', 'SALES'], msg='Step 34.00')
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '100K', '200K', '300K', '400K', '500K', '600K'], msg='Step 34.01')
        designer_chart_obj.verify_x_axis_title_in_preview(['DEPT'], msg='Step 34.02')
        designer_chart_obj.verify_y_axis_title_in_preview(['SALARY'], msg='Step 34.03')
        designer_chart_obj.verify_number_of_risers("[id*='chartpreview'] .risers rect", 1, 8, msg='Step 34.04')
        utillobj.capture_screenshot('34.00', step34, expected_image_verify=True)
        
        step35=""" Step 35: scroll_down in Dimensions with scroll bar, right click Calculation_1, select edit calculation
        """
        designer_chart_obj.right_click_on_dimensions_field('Calculation_1', context_menu_item_path='Edit calculation...')
        utillobj.capture_screenshot('35.00', step35)
        
        step36=""" Step 36: Click Edit format
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        designer_calculation_edit.verify_selected_datatype_in_dialog('date', '36.00')
        designer_calculation_edit.verify_date_separator_in_date("'/' (slash)", '36.01')
        utillobj.capture_screenshot('36.00', step36, expected_image_verify=True)
        
        step37=""" Step 37: Click OK to close data formatter, Click close to close Calculator
                scrolldown in Dimensions with scroll bar, right click Calculation_2, select edit calculation
        """
        designer_calculation_edit.close_dialog('OK')
        designer_chart_obj.click_button_on_calculation('Cancel')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.right_click_on_dimensions_field('Calculation_2', context_menu_item_path='Edit calculation...')
        utillobj.capture_screenshot('37.00', step37)
        
        step38=""" Step 38: Click Edit format
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        designer_calculation_edit.verify_selected_datatype_in_dialog('date', '38.00')
        designer_calculation_edit.verify_date_separator_in_date("'-' (dash)", '38.01')
        utillobj.capture_screenshot('38.00', step38, expected_image_verify=True)
        
        step39=""" Step 39: Click OK to close data formatter, Click close to close Calculator
                scrolldown in Dimensions with scroll bar, right click Calculation_3, select edit calculation
        """
        designer_calculation_edit.close_dialog('OK')
        designer_chart_obj.click_button_on_calculation('Cancel')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.right_click_on_dimensions_field('Calculation_3', context_menu_item_path='Edit calculation...')
        utillobj.capture_screenshot('39.00', step39)
        
        step40=""" Step 40: Click Edit format
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        designer_calculation_edit.verify_selected_datatype_in_dialog('date', '40.00')
        designer_calculation_edit.verify_date_separator_in_date("'.' (dot)", '40.01')
        utillobj.capture_screenshot('40.00', step40, expected_image_verify=True)
        
        step41=""" Step 41: Click OK to close data formatter, Click close to close Calculator
                scrolldown in Dimensions with scroll bar, right click Calculation_4, select edit calculation
        """
        designer_calculation_edit.close_dialog('OK')
        designer_chart_obj.click_button_on_calculation('Cancel')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.right_click_on_dimensions_field('Calculation_4', context_menu_item_path='Edit calculation...')
        utillobj.capture_screenshot('41.00', step41)
        
        step42=""" Step 42: Click Edit format
        """
        designer_calculation_edit.click_edit_format_on_calculation_dialog()
        designer_calculation_edit.verify_selected_datatype_in_dialog('date', '42.00')
        designer_calculation_edit.verify_date_separator_in_date("' ' (space)", '42.01')
        utillobj.capture_screenshot('42.00', step42, expected_image_verify=True)
        designer_calculation_edit.close_dialog('OK')
        designer_chart_obj.click_button_on_calculation('Cancel')
        utillobj.synchronize_until_element_disappear(".pop-top [title='Edit format']", designer_chart_obj.home_page_long_timesleep)
        
        step43=""" Step 43: Logout using API
                http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
        utillobj.capture_screenshot('14.00', step43)
        
 
    if __name__ == "__main__":
        unittest.main()