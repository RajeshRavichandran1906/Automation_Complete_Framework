'''
Created on Oct 29, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6986709&group_by=cases:section_id&group_id=542386&group_order=asc
Testcase Name : Verify the HTML files under Test Widgets
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.wftools import report
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables

class C6986709_TestClass(BaseTestCase):

    def test_C6986709(self):
        
        """
            CLASS OBJECTS 
        """
        Testcase_ID="C6986709"
        wf_login = login.Login(self.driver)
        wf_home = wf_mainpage.Wf_Mainpage(self.driver)
        utill=utillity.UtillityMethods(self.driver)
        report_obj=report.Report(self.driver)
        wf_locator = WfMainPageLocators()
        
        """ 
            VARIABLES
        """
        USERNAME='mrbasid'
        PASSWORD='mrbaspass'
        FOLDER_PATH='Retail Samples->Portal->Test Widgets'
        
        """ 
            CSS 
        """
        IFRAME_CSS="[class='ibx-iframe-frame']"
        color_list = ['Blue', 'Gray', 'Green', 'Red', 'Silver', 'Yellow']
        COLOR_CSS="html body[style='background-color:{0}']"
        view_type = 'View'
        
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
            Step 1 : Sign to WebFocus using rsbas (basic user)
            http://machine:port/ibi_apps
            Step 2:Expand "Retail Samples => Portal => Test Widgets"
            Verify the HTML files under Test Widgets
        """
        wf_login.invoke_home_page(USERNAME, PASSWORD)
        
        """
            Step 3:Right Click Blue > View
            Verify output is blue color
        """
        wf_home.select_content_from_sidebar()
        utill.synchronize_with_number_of_element(wf_locator.REPOSITORY_TREE_CSS, 1, wf_home.home_page_long_timesleep)
        wf_home.right_click_folder_item_and_select_menu(color_list[0], view_type, FOLDER_PATH)
        report_obj.wait_for_number_of_element(IFRAME_CSS, 1, wf_home.home_page_medium_timesleep)
        utill.switch_to_frame(frame_css=IFRAME_CSS)
        utill.synchronize_until_element_is_visible(COLOR_CSS.format(color_list[0].lower()), wf_home.home_page_long_timesleep)
        utill.verify_object_visible(COLOR_CSS.format(color_list[0].lower()), True, "Step 3: Verify Test Widgets blue color item shown as blue color")
        utill.switch_to_default_content()
        wf_home.close_view_dialog(color_list[0])
         
         
        """
            Step 4:Right Click Gray > View
            Verify output is Gray color
        """
     
        wf_home.right_click_folder_item_and_select_menu(color_list[1], view_type)
        report_obj.wait_for_number_of_element(IFRAME_CSS, 1, wf_home.home_page_medium_timesleep)
        utill.switch_to_frame(frame_css=IFRAME_CSS)
        utill.synchronize_until_element_is_visible(COLOR_CSS.format('dim'+color_list[1].lower()), wf_home.home_page_long_timesleep)
        utill.verify_object_visible(COLOR_CSS.format('dim'+color_list[1].lower()), True, "Step 04 : Verify Dim Gray is displayed")
        utill.switch_to_default_content()
        wf_home.close_view_dialog(color_list[1])
         
        """
            Step 5:Right Click Green > View
            Verify output is Green color
        """
        wf_home.right_click_folder_item_and_select_menu(color_list[2], view_type)
        report_obj.wait_for_number_of_element(IFRAME_CSS, 1, wf_home.home_page_medium_timesleep)
        utill.switch_to_frame(frame_css=IFRAME_CSS)
        utill.synchronize_until_element_is_visible(COLOR_CSS.format(color_list[2].lower()), wf_home.home_page_long_timesleep)
        utill.verify_object_visible(COLOR_CSS.format(color_list[2].lower()), True, "Step 04 : Verify GREEN color is displayed")
        utill.switch_to_default_content()
        wf_home.close_view_dialog(color_list[2])
          
        """
            Step 6:Right Click Red > View
            Verify output is Red color
        """
        wf_home.right_click_folder_item_and_select_menu(color_list[3], view_type)
        report_obj.wait_for_number_of_element(IFRAME_CSS, 1, wf_home.home_page_medium_timesleep)
        utill.switch_to_frame(frame_css=IFRAME_CSS)
        utill.synchronize_until_element_is_visible(COLOR_CSS.format(color_list[3].lower()), wf_home.home_page_long_timesleep)
        utill.verify_object_visible(COLOR_CSS.format(color_list[3].lower()), True, "Step 04 : Verify RED color is displayed")
        utill.switch_to_default_content()
        wf_home.close_view_dialog(color_list[3])
                 
        """
            Step 7:Right Click Silver > View
            Verify output is Silver color
        """
        wf_home.right_click_folder_item_and_select_menu(color_list[4], view_type)
        report_obj.wait_for_number_of_element(IFRAME_CSS, 1, wf_home.home_page_medium_timesleep)
        utill.switch_to_frame(frame_css=IFRAME_CSS)
        utill.synchronize_until_element_is_visible(COLOR_CSS.format(color_list[4].lower()), wf_home.home_page_long_timesleep)
        utill.verify_object_visible(COLOR_CSS.format(color_list[4].lower()), True, "Step 04 : Verify SILVER color is displayed")
        utill.switch_to_default_content()
        wf_home.close_view_dialog(color_list[4])
         
        """
            Step 8:Right Click Yellow > View
            Verify output is Yellow color
        """
        wf_home.right_click_folder_item_and_select_menu(color_list[5], view_type)
        utill.switch_to_frame(frame_css=IFRAME_CSS)
        utill.synchronize_until_element_is_visible(COLOR_CSS.format(color_list[5].lower()), wf_home.home_page_long_timesleep)
        utill.verify_object_visible(COLOR_CSS.format(color_list[5].lower()), True, "Step 04 : Verify YELLOW color is displayed")
        utill.switch_to_default_content()
        wf_home.close_view_dialog(color_list[5])
        
        """
            Step 9:Right Click Test Widgets > View
            Verify the following output
        """
        TABLE_CSS="html body table"
        wf_home.right_click_folder_item_and_select_menu('Test Widget', view_type, FOLDER_PATH)
        utill.switch_to_frame(frame_css=IFRAME_CSS)
        report_obj.wait_for_visible_text(TABLE_CSS, 'Screen', time_out=wf_home.home_page_long_timesleep)
        if Global_variables.browser_name == 'firefox':
#             report_obj.create_table_data_set(TABLE_CSS, Testcase_ID+"_ff_Ds01.xlsx")
            report_obj.verify_table_data_set(TABLE_CSS, Testcase_ID+"_ff_Ds01.xlsx", "Step 09: Verify table data")
        else:
#             report_obj.create_table_data_set(TABLE_CSS, Testcase_ID+"_Ds01.xlsx")
            report_obj.verify_table_data_set(TABLE_CSS, Testcase_ID+"_Ds01.xlsx", "Step 09: Verify table data")
        utill.switch_to_default_content()
        wf_home.close_view_dialog('Test Widget')
        
        
        """
            Step 10:Logout:
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()