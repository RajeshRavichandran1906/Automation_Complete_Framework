'''
Created on October 22, 2018

@author: Robert
Testcase Name : Verify Ask WebFOCUS Side Bar option show/are functional for Admin Users
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2967306
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,page_designer
from common.lib import core_utility
from common.pages import page_designer_miscelaneous
from common.lib import utillity

class C2967306_TestClass(BaseTestCase):
    
    def test_C2967306(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        page_designer_obj = page_designer.Design(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        page_misc_obj = page_designer_miscelaneous.PageDesignerMiscelaneous(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        crumb_box_css = ".crumb-box .ibx-label-text"
        medium_wait = 45
        content_list=['Content','Portals', 'Favorites', 'Mobile Favorites', 'Ask WebFOCUS']
     
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 1.1. Verify sidebar listed with the following options :
            1.Content View (By default selected).
            2.Portals View.
            3.Favorites View.
            4.Mobile Favorites View.
            5.Ask WebFOCUS.
        """
        
        main_page_obj.verify_left_panel(content_list, 'Step 1.1 Verify Sidebar options')
        
        """
        Step 2. Click Ask WebFOCUS from the sidebar.
        """
        main_page_obj.select_ask_webfocus_from_sidebar()

        """
        Step 2.1. Verify that the Search box is displays with the three options are as follows:
            1.Search by Voice
            2.Search
            3.Search options (drop down)
        Also verify that 'Last Viewed Questions' with Clear (disable) button is shown.
        
        """
        main_page_obj.ask_webfocus_search_bar_options('text_box', True, 'Step 2.1.1 Verify Search textbox present')
        main_page_obj.ask_webfocus_search_bar_options('speech_mic', True, 'Step 2.1.2 Verify Search by Voice present')
        main_page_obj.ask_webfocus_search_bar_options('search_image', True, 'Step 2.1.3 Verify Search image present')
        main_page_obj.ask_webfocus_search_bar_options('dropdown', True, 'Step 2.1.4 Verify Search options (dropdown) present')
        

        main_page_obj.ask_webfocus_content_area('title', 'Last Viewed Questions', 'Step 2.1.5. Verify Last Viewed Questions text present in content area')
        main_page_obj.ask_webfocus_content_area('title_button_state', True, 'Step 2.1.6. Verify Clear button is disabled in content area')
        main_page_obj.ask_webfocus_content_area('title_button_text', 'Clear','Step 2.1.7. Verify Clear button is present')
        
        
        """
        Step 3. Click on the Collapse side bar icon.
        """
        main_page_obj.collapse_side_bar()
        
        """
        Step 3.1. Verify that the sidebar is collapsed and following should be displayed:
            1.Five sidebar menu icons.
            2.Information Builders text logo will convert into the simplified square Information Builders logo
        """
        main_page_obj.verify_left_panel([], "Step3.1: Verify Side bar(left panel) options doesn't show any text",'')
        utillobj.verify_picture_using_sikuli("collapse_content.png", "Step3.2a: Verify content image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_portal.png", "Step3.2b: Verify portals image displayed")
        utillobj.verify_picture_using_sikuli("collapse_favourites.png", "Step3.2c: Verify favorites image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_mobile_favs.png", "Step3.2d: Verify mobile favorites image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_logo.png", "Step3.2e: Verify collapse logo image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_ask_webfocus.png", "Step3.2f: Verify collapse ask webfocus image is displayed")
        """
        Step 4. Sign Out and Sign back into WebFOCUS Home Page as Admin User.
        
        """
        main_page_obj.signout_from_username_dropdown_menu()
        login_obj.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(crumb_box_css, "Mobile Favorites", medium_wait)
        
        """
        Step 4.1. Verify that the state of the sidebar should be remembered when the user signs out of the Home Page and signs back in.
        """
        main_page_obj.verify_left_panel([], "Step4.1: Verify Side bar(left panel) options doesn't show any text",'')
        utillobj.verify_picture_using_sikuli("collapse_content.png", "Step4.2a: Verify content image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_portal.png", "Step4.2b: Verify portals image displayed")
        utillobj.verify_picture_using_sikuli("collapse_favourites.png", "Step4.2c: Verify favorites image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_mobile_favs.png", "Step4.2d: Verify mobile favorites image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_logo.png", "Step4.2e: Verify collapse logo image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_ask_webfocus.png", "Step4.2f: Verify collapse ask webfocus image is displayed") 

        """
        Step 5. Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        files_box_css =".content-box.ibx-widget .files-box .ibx-label-text"
        main_page_obj.expand_side_bar()
        main_page_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", 45)
        main_page_obj.verify_left_panel(content_list, "Step5.1: Verify Side bar(left panel) options")
        
        """
        Step 6. Sign Out WebFOCUS Home Page.
        """
        main_page_obj.signout_from_username_dropdown_menu()

        
if __name__ == '__main__':
    unittest.main()