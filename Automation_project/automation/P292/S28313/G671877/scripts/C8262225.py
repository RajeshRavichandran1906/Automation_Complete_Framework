"""---------------------------------------------------------------
Author Name : Prabhakaran.
Automated On : 24-September-2019
---------------------------------------------------------------"""
from common.wftools.login import Login
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage

class C8262225_TestClass(BaseTestCase):
    
    def test_C8262225(self):
        
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
        files_css = ".sd-tab-page div[class*='sd-files']:not([style*='none'])"
        
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
            STEP 04 : Double click "ibisamp" folder.
        """
        homepage.resource_dialog().navigate_to_file('ibisamp')
        
        """
            STEP 05 : Enter "car" in "Search" text box.
        """
        homepage.resource_dialog().enter_search_input('car')
        utils.synchronize_with_visble_text(files_css, 'car', homepage.home_page_short_timesleep)
        
        """
            STEP 05 Expected : Check the following Output.
        """
        homepage.resource_dialog().verify_files_contains_specific_value('car', "05.01")
        
        """
            STEP 06 : Click the "Repository tab".
        """
        homepage.resource_dialog().click_tab('Repository')
        utils.synchronize_with_visble_text(files_css, '', homepage.home_page_short_timesleep)
        
        """
            STEP 06 - Expected : Check the "car" search is not seen and the list of items under the domain/folder appear.
        """
        actual_text = self.driver.find_element_by_css_selector(files_css).text.strip()
        utils.asequal('', actual_text, "Step 06.01 : Verify the 'car' search is not seen and the list of items under the domain/folder appear")
        
        """
            STEP 07 : Click the "Server tab" and Enter "empdata" in "Search" text box.
        """
        homepage.resource_dialog().click_tab('Server')
        homepage.resource_dialog().enter_search_input('empdata')
        utils.synchronize_with_visble_text(files_css, 'empdata', homepage.home_page_short_timesleep)
        
        """
            STEP 07 Expected : Check the following Output.
        """
        homepage.resource_dialog().verify_files_contains_specific_value('empdata', "07.01")
        
        """
            STEP 08 : Click the "Repository tab".
        """
        homepage.resource_dialog().click_tab('Repository')
        utils.synchronize_with_visble_text(files_css, '', homepage.home_page_short_timesleep)
        
        """
            STEP 08 - Expected : Check the "empdata" search is not seen and the list of items under the domain/folder appear.
        """
        actual_text = self.driver.find_element_by_css_selector(files_css).text.strip()
        utils.asequal('', actual_text, "Step 08.01 : Verify the 'empdata' search is not seen and the list of items under the domain/folder appear")
        
        """
            STEP 09 : Click "Cancel" button.
        """
        homepage.resource_dialog().click_button('Cancel')
        
        """
            STEP 10 : Logout - http://machine:port/{alias}/service/wf_security_logout.jsp
        """