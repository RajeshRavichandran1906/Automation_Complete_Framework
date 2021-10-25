'''
Created on October 01, 2019

@author: AA14564.
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262004
TestCase Name = Create and modify thumbnail
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer_chart import Designer_Chart
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib import utillity
from common.lib import core_utility
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables


class C8262004_TestClass(BaseTestCase):
    
    def test_C8262004(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        designer_chart_obj=Designer_Chart(self.driver)
        main_page_obj = Wf_Mainpage(self.driver)
        login_page = Login(self.driver)
        g_var = Global_variables
        wf_locator = WfMainPageLocators
        project_id = core_utill_obj.parseinitfile('project_id')
        suite_id = core_utill_obj.parseinitfile('suite_id')
        group_id = core_utill_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        thumbnail_css = ".wfc-main-toolbar div[data-ibx-name='wfcThumbnail']"
        
        
        step1=""" Step 1: Launch the IA API with Chart (edit the domain, port and alias of the URL - do not use the URL as is)
                http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api("baseapp/wf_retail_lite")
        utillobj.synchronize_until_element_is_visible("[id*='chartpreview'] rect[class*='riser']", designer_chart_obj.chart_long_timesleep)
        utillobj.capture_screenshot('01.00', step1)
         
        step2=""" Step 2: Add fields 'Product,Category' and 'Cost of Goods'
        """
        designer_chart_obj.double_click_on_dimension_field('Product->Product->Product,Category')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box", "Product,Category", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_measures_field('Sales->Cost of Goods')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box", "Cost of Goods", designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('02.00', step2)
         
        step3=""" Step 3: Drag 'Gross Profit' into the Color bucket
                Fields added to appropriate buckets and canvas updated.
        """
        designer_chart_obj.drag_measure_field_to_query_bucket('Sales->Gross Profit', 'Color')
        utillobj.synchronize_with_visble_text("[id*='chartpreview'] text.colorScaleLegend-title", 'Gross Profit', designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg='Step 03.00')
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '40M', '80M', '120M', '160M', '200M', '240M'], msg='Step 03.01')
        designer_chart_obj.verify_x_axis_title_in_preview(['Product Category'], msg='Step 03.02')
        designer_chart_obj.verify_y_axis_title_in_preview(['Cost of Goods'], msg='Step 03.03')
        designer_chart_obj.verify_number_of_risers("[id*='chartpreview'] .risers rect", 1, 7, msg='Step 03.04')
        designer_chart_obj.verify_legends_in_preview(['Gross Profit', '16.8M', '28.4M', '40M', '51.5M', '63M', '74.6M', '86.2M'], msg='Step 03.05')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview("[class='riser!s0!g0!mbar!']", 'pattens_blue_2', msg='Step 03.06')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview("[class='riser!s0!g4!mbar!']", 'Cobalt', msg='Step 03.07')
        utillobj.capture_screenshot('03.00', step3, expected_image_verify=True)
         
        step4=""" Step 4: Hover on Camera icon (Thumbnail)
                Tooltip value displays as "Thumbnail".
        """
        thumbnail_obj =  utillobj.validate_and_get_webdriver_object(thumbnail_css, 'Thumbnail toolbar')
        thumbnail_text = utillobj.get_element_attribute(thumbnail_obj, 'title').strip()
        utillobj.asequal('Thumbnail', thumbnail_text, 'Step 04.00: Verify Tooltip value displays as "Thumbnail".')
        utillobj.capture_screenshot('04.00', step4)
         
        step5=""" Step 5: Click on the Camera icon button in the toolbar
                Thumbnail dialog displayed.
        """
        designer_chart_obj.click_toolbar_item('Thumbnail')
        utillobj.synchronize_with_visble_text(".pop-top", 'Save Thumbnail', designer_chart_obj.home_page_long_timesleep)
        utillobj.verify_picture_using_sikuli('step05.png', 'Step 05.00: Verify Thumbnail dialog displayed.')
        thumbnail_dialog =  utillobj.validate_and_get_webdriver_object('.pop-top', 'Thumbnail toolbar').text.strip().split('\n')
        utillobj.as_List_equal(['Save Thumbnail', 'OK', 'Cancel'],thumbnail_dialog, 'Step 05.01: Verify Thumbnail dialog displayed.')
        utillobj.capture_screenshot('05.00', step5, expected_image_verify=True)
         
        step6=""" Step 6: Click OK
        """
        main_page_obj.click_button_on_popup_dialog('OK')
        utillobj.capture_screenshot('06.00', step6)
         
        step7=""" Step 7: Click "Save" button in top toolbar > Save As "C6778137" > Click Save
        """
        designer_chart_obj.save_as_from_application_menu(g_var.current_test_case)
        utillobj.capture_screenshot('07.00', step7)
        designer_chart_obj.api_logout()
         
        step8=""" Step 8: Navigate to Homepage using the below URL:
                http://machine:port/alias
        """
        login_page.invoke_home_page('mrid', 'mrpass')
        main_page_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(wf_locator.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        utillobj.capture_screenshot('08.00', step8)
         
        step9=""" Step 9: Navigate to the following folder P292_S28313 > 'G671774'
                Thumbnail does show for the saved chart in the content area.
        """
        main_page_obj.click_repository_folder('Domains')
        main_page_obj.expand_repository_folder(folder_path)
        main_page_obj.right_click_folder_item_and_select_menu(g_var.current_test_case, click_option='left_click')
        core_utill_obj.python_move_to_offset(x_offset=0, y_offset=0)
        utillobj.verify_picture_using_sikuli('step09.png', 'Step 09.00: Verify Thumbnail dialog displayed.')
        utillobj.capture_screenshot('09.00', step9)
         
        step10=""" Step 10: Right-click the saved "C6778137" fex in the Domains tree > Select "Properties" .
        """
        main_page_obj.right_click_folder_item_and_select_menu(g_var.current_test_case, context_menu_item_path='Properties')
        utillobj.synchronize_with_visble_text(".propPage .ibx-csl-items-container", 'Advanced', main_page_obj.home_page_medium_timesleep)
        utillobj.capture_screenshot('10.00', step10)
         
        step11=""" Step 11: Click "Advanced" Tab.
                Verify thumbnail saved .
        """
        main_page_obj.select_property_tab_value('Advanced')
        utillobj.synchronize_with_visble_text(".propPage", 'Embedded', main_page_obj.home_page_medium_timesleep)
        utillobj.verify_picture_using_sikuli('step11.png', 'Step 11.00: Verify Thumbnail saved.')
        utillobj.capture_screenshot('11.00', step11, expected_image_verify=True)
         
        step12=""" Step 12: Click OK.
        """
        main_page_obj.close_property_dialog()
        time.sleep(5)
        utillobj.capture_screenshot('12.00', step12)
        designer_chart_obj.api_logout()
        
        step13=""" Step 13: Restore the C6778137.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
                http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2Fc6778137.fex
        """
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api(g_var.current_test_case.lower()+'.fex', tool='workbook')
        utillobj.synchronize_with_visble_text("[id*='chartpreview'] text.colorScaleLegend-title", 'Gross Profit', designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg='Step 13.00')
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '40M', '80M', '120M', '160M', '200M', '240M'], msg='Step 13.01')
        designer_chart_obj.verify_x_axis_title_in_preview(['Product Category'], msg='Step 13.02')
        designer_chart_obj.verify_y_axis_title_in_preview(['Cost of Goods'], msg='Step 13.03')
        designer_chart_obj.verify_number_of_risers("[id*='chartpreview'] .risers rect", 1, 7, msg='Step 13.04')
        designer_chart_obj.verify_legends_in_preview(['Gross Profit', '16.8M', '28.4M', '40M', '51.5M', '63M', '74.6M', '86.2M'], msg='Step 13.05')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview("[class='riser!s0!g0!mbar!']", 'pattens_blue_2', msg='Step 13.06')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview("[class='riser!s0!g4!mbar!']", 'Cobalt', msg='Step 13.07')
        utillobj.capture_screenshot('13.00', step13, expected_image_verify=True)
        
        step14=""" Step 14: Right-click "Gross Profit" field in the Query pane > Remove.
        """
        designer_chart_obj.select_query_bucket_field_context_menu('Color', 'Gross Profit', 'Remove')
        utillobj.synchronize_with_visble_text("[id*='chartpreview']", 'Gross Profit', designer_chart_obj.home_page_long_timesleep, condition_type='asnotin')
        utillobj.capture_screenshot('14.00', step14)
        
        step15=""" Step 15: Click on the Camera icon button in the toolbar.
                Thumbnail displayed.
        """
        designer_chart_obj.click_toolbar_item('Thumbnail')
        utillobj.synchronize_with_visble_text(".pop-top", 'Save Thumbnail', designer_chart_obj.home_page_long_timesleep)
        utillobj.verify_picture_using_sikuli('step15.png', 'Step 15.00: Verify Thumbnail dialog displayed.')
        thumbnail_dialog =  utillobj.validate_and_get_webdriver_object('.pop-top', 'Thumbnail toolbar').text.strip().split('\n')
        utillobj.as_List_equal(['Save Thumbnail', 'OK', 'Cancel'],thumbnail_dialog, 'Step 15.01: Verify Thumbnail dialog displayed.')
        utillobj.capture_screenshot('15.00', step15, expected_image_verify=True)
        
        step16=""" Step 16: Click Cancel.
        """
        main_page_obj.click_button_on_popup_dialog('Cancel')
        utillobj.capture_screenshot('16.00', step16)
        
        step17=""" Step 17: Click "Save" button in top toolbar
        """
        designer_chart_obj.click_toolbar_item('Save')
        utillobj.capture_screenshot('17.00', step17)
        designer_chart_obj.api_logout()
        
        step18=""" Step 18: Navigate to Homepage using the below URL:
                http://machine:port/alias
        """
        login_page.invoke_home_page('mrid', 'mrpass')
        utillobj.capture_screenshot('18.00', step18)
        
        step19=""" Step 19: Navigate to the following folder P292_S28313 > 'G671774'
                Thumbnail does show for the saved chart in the content area.
        """
        main_page_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(wf_locator.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Domains')
        main_page_obj.expand_repository_folder(folder_path)
        main_page_obj.right_click_folder_item_and_select_menu(g_var.current_test_case, click_option='left_click')
        core_utill_obj.python_move_to_offset(x_offset=0, y_offset=0)
        utillobj.verify_picture_using_sikuli('step19.png', 'Step 19.00: Verify Thumbnail dialog displayed.')
        utillobj.capture_screenshot('19.00', step19, expected_image_verify=True)
        
        step20=""" Step 20: Logout using API
                http://domain:port/alias/service/wf_security_logout.jsp 
        """
        designer_chart_obj.api_logout()
        utillobj.capture_screenshot('20.00', step20)
        
    if __name__ == "__main__":
        unittest.main()