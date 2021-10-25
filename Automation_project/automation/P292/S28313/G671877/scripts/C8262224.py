"""---------------------------------------------------------------
Author Name : Prabhakaran.
Automated On : 25-September-2019
---------------------------------------------------------------"""
from common.wftools.login import Login
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage

class C8262224_TestClass(BaseTestCase):
    
    def test_C8262224(self):
        
        """
            Class Objects
        """
        login = Login(self.driver)
        homepage = Wf_Mainpage(self.driver) 
        utils = UtillityMethods(self.driver)
        
        """
            Common Variables
        """
        folder_path = 'P292_S28313->G671877'
        tags = ['P292_S10660', 'P292_S11397', 'Retail Samples']
        
        """
            STEP 01 : Login WebFoucs http://machine:port/{alias}
        """
        login.invoke_home_page('mrid', 'mrpass')
        
        """
            STEP 02 : Navigate "G671877" folder under "P292_S28313" domain.
        """
        homepage.expand_repository_folder(folder_path)
        
        """
            STEP 03 : Click "Workbook" under "Designer" category options.
        """
        homepage.select_action_bar_tab('Designer')
        homepage.select_action_bar_tabs_option('Workbook')
        
        """
            STEP 03 - Expected : Check the Data picker dialog appears.
        """
        homepage.resource_dialog().verify_caption_title("Open", "03.01")
        
        """
            STEP 04 : Click the "Repository tab" and Click "Domains".
        """
        homepage.resource_dialog().click_tab('Repository')
        utils.synchronize_with_visble_text(".pop-top", 'Workspaces', homepage.home_page_short_timesleep)
        homepage.resource_dialog().click_crumb_item("Workspaces")
        utils.synchronize_with_visble_text(".pop-top", 'Retail Samples', homepage.home_page_short_timesleep)
        
        """
            STEP 04 - Expected : Check that you see the list of items under domains and the tags.
        """
        homepage.resource_dialog().verify_tags(tags, "Step 04.01 : Verify list of items under domains and the tags", "asin")
        
        """
            STEP 05 : Click the "Server tab"
        """
        homepage.resource_dialog().click_tab('Server')
        utils.synchronize_with_visble_text(".pop-top", 'ibisamp', homepage.home_page_short_timesleep)
        
        """
            STEP 05 - Expected : Check the Data picker dialog appears.
        """
        homepage.resource_dialog().verify_files(['baseapp', 'ibisamp'], "Step 05.01 : heck the Data picker dialog appears", 'asin')
        
        """
            STEP 06 : Click the "Repository tab"
        """
        homepage.resource_dialog().click_tab('Repository')
        utils.synchronize_with_visble_text(".pop-top", 'Workspaces', homepage.home_page_short_timesleep)
        
        """
            STEP 06 - Expected : Check that you see the list of items under domains and the tags.
        """
        homepage.resource_dialog().verify_tags(tags, "Step 06.01 : Verify list of items under domains and the tags", "asin")
        
        """
            STEP 07 : Click "Cancel" button.
        """
        homepage.resource_dialog().click_button('Cancel')
        
        """
            STEP 08 : Logout - http://machine:port/{alias}/service/wf_security_logout.jsp
        """