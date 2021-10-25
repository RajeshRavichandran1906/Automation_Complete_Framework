"""-------------------------------------------------------------------------------------------
Created on November 21, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325149
Test Case Title =  Verify Ellipsis (...) appears when title is long for the domain
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login

class C2325149_TestClass(BaseTestCase):

    def test_C2325149(self):
        
        """
            CLASS OBJECTS 
        """
        wf_login = Login(self.driver)
        wf_home = Wf_Mainpage(self.driver)
        utlis = UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        LONG_WAIT_TIME = 120
        SEARCH_TEXTBOX_CSS = ".toolbar div[data-ibx-type='advancedFolderSearch'] input[type='search']"
        
        """
            STEP 01 : Sign in to WebFOCUS as Developer User.
        """
        wf_login.invoke_home_page('mriddev', 'mrpassdev')
        utlis.synchronize_with_visble_text(".left-main-panel .left-main-panel-content-button", 'Content', LONG_WAIT_TIME)
        
        """
            STEP 02 : Click on the Content tree from the sidebar.
        """
        wf_home.select_content_from_sidebar()
        
        """
            STEP 03 : Expand Domain > P292_S10660>G169261>Click on "Breadcrumb Trail and Search" from the tree
        """
        wf_home.select_option_from_crumb_box("Workspaces")
        wf_home.expand_repository_folder('P292_S10660->G169261->Breadcrumb Trail and Search')
        
        """
            STEP 03.1 : Verify "Search Breadcrum..." appears in the Search box
        """
        wf_home.verify_search_textbox_value('Search Breadcrumb Trail and Search', 'Step 03.01 : Verify Search Breadcrum.. is displayed in search textbox')
        search_textbox_obj = utlis.validate_and_get_webdriver_object(SEARCH_TEXTBOX_CSS, 'Home page search textbox')
        text_overflow = search_textbox_obj.value_of_css_property('text-overflow')
        utlis.asequal("ellipsis", text_overflow, "Step 03.02 : Verify Search Breadcrumb Trail and Search displayed with ... in search textbox")
        
        """
            STEP 04 : In the banner link, click on the top right username > Sign out.
        """
        wf_home.signout_from_username_dropdown_menu()
        