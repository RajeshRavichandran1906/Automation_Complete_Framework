'''
Created on Dec 27, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6986714&group_by=cases:section_id&group_order=asc&group_id=542388
Testcase Name : Verify the files under Hidden content folder
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools import report
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import core_utility

class C6986714_TestClass(BaseTestCase):

    def test_C6986714(self):
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(driver)
        core_utillobj=core_utility.CoreUtillityMethods(driver)
        report_obj=report.Report(driver)
        login_obj=login.Login(driver)
        wf_mainpage_obj=wf_mainpage.Wf_Mainpage(driver)
        wf_locator = WfMainPageLocators()
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        css="div.text-editor"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 1:Sign to WebFocus using "rsdev" user
        http://machine:port/ibi_apps
        """
        login_obj.invoke_home_page('mrdevid', 'mrdevpass')
 
        """
        Step 2:Expand Retail Samples > Click Hidden Content folder
        Verify the following folder and files are available
        """
        wf_mainpage_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(wf_locator.REPOSITORY_TREE_CSS, 1, wf_mainpage_obj.home_page_long_timesleep)
        wf_mainpage_obj.expand_repository_folder('Retail Samples->Hidden Content')
        
        """
        Step 3:Right click "Blog" >Edit
        Verify the Comments window
        """
        wf_mainpage_obj.right_click_folder_item_and_select_menu('Blog', context_menu_item_path='Edit')
        core_utillobj.switch_to_new_window()
 
        """
        Step 4:Click Add comment.. > Type "test" > Post
        Verify the comment is added
        """
        wf_mainpage_obj.add_comment_in_blog('test')
        wf_mainpage_obj.verify_comment_in_blog(1, 'Retail Samples DevelopertestReply...', "Step 4: Verify commment is added")
 
        """
        Step 5:Close the Comment
        """
        core_utillobj.switch_to_previous_window()
 
        """
        Step 6:Right click "blue_theme_accent" > Edit
        Verify it Css file opens in text editor
        """
        wf_mainpage_obj.right_click_folder_item_and_select_menu('blue_theme_accent', context_menu_item_path='Edit')
        core_utillobj.switch_to_new_window()
        utillobj.synchronize_until_element_is_visible(css, wf_mainpage_obj.home_page_long_timesleep)
        utillobj.verify_object_visible(css, True, "Step 6: Verify it Css file opens in text editor")
         
        """
        Step 7:Close the editor
        """
        core_utillobj.switch_to_previous_window()
        
        """
        Step 8:Double click Image folder
        Verify the following files are available
        """
        folder_item1='col_insert_marker_hover_57A8FA'
        folder_item2='networking'
        folder_item3='worldmap_transparent'
        
        wf_mainpage_obj.right_click_folder_item_and_select_menu('Images', click_option='double_click')
        utillobj.synchronize_with_visble_text(wf_locator.files_item_css, folder_item1, wf_mainpage_obj.home_page_medium_timesleep)
        
        """
        Step 9:Right click "col_insert_marker_hover_57A8FA" > View and close the output
        Verify the png file
        """
        IFRAME_CSS="[class='ibx-iframe-frame']"
        FOLDER_ADD_IMG_CSS="img[src*='col_insert_marker_hover_57A8FA']"
        wf_mainpage_obj.right_click_folder_item_and_select_menu(folder_item1, context_menu_item_path='View')
        report_obj.wait_for_number_of_element(IFRAME_CSS, 1, wf_mainpage_obj.home_page_medium_timesleep)
        report_obj.switch_to_frame(frame_css=IFRAME_CSS)
        utillobj.verify_object_visible(FOLDER_ADD_IMG_CSS, True, "Step 9: Verify col_insert_marker_hover_57A8FA image is displayed")
        core_utillobj.switch_to_default_content()
        css="[title='Close']"
        btn_elem=utillobj.validate_and_get_webdriver_object(css, 'close image view')
        core_utillobj.left_click(btn_elem)

        """
        Step 10:Right click "networking" > View and close the output
        Verify the Jpg file
        """
        NETWORKING_IMG_CSS="img[src*='networking']"
        wf_mainpage_obj.right_click_folder_item_and_select_menu(folder_item2, context_menu_item_path='View')
        report_obj.wait_for_number_of_element(IFRAME_CSS, 1, wf_mainpage_obj.home_page_medium_timesleep)
        report_obj.switch_to_frame(frame_css=IFRAME_CSS)
        utillobj.verify_object_visible(NETWORKING_IMG_CSS, True, "Step 10: Verify networking image is displayed")
        core_utillobj.switch_to_default_content()
        btn_elem=utillobj.validate_and_get_webdriver_object(css,'close image view')
        core_utillobj.left_click(btn_elem)
        utillobj.switch_to_main_window()

        """
        Step 11:Right click "worldmap_transparent" > View and close the output
        Verify the Jpg file
        """
        WORLDMAP_IMG_CSS="img[src*='worldmap_transparent']"
        wf_mainpage_obj.right_click_folder_item_and_select_menu(folder_item3, context_menu_item_path='View')
        report_obj.wait_for_number_of_element(IFRAME_CSS, 1, wf_mainpage_obj.home_page_medium_timesleep)
        report_obj.switch_to_frame(frame_css=IFRAME_CSS)
        utillobj.verify_object_visible(WORLDMAP_IMG_CSS, True, "Step 11: Verify worldmap image is displayed")
        core_utillobj.switch_to_default_content()
        btn_elem=utillobj.validate_and_get_webdriver_object(css, 'close image view')
        core_utillobj.left_click(btn_elem)
        utillobj.switch_to_main_window()

        """
        Step 12:Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()