'''
Created on Sep 26, 2018

@author: vishnu priya

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=169269&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2325140
TestCase Name = Select folder from drop down list
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity, javascript, core_utility
from common.locators import wf_mainpage_locators

class C2325140_TestClass(BaseTestCase):

    def test_C2325140(self):
        
        """
        TESTCASE Objects 
        """
        driver = self.driver #Driver reference object created
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        utillobj = utillity.UtillityMethods(self.driver)
        j_script=javascript.JavaScript(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        
        def verify_context_popup_style_attribute(context_menu_option_name, msg):
            context_popup_css = "div[class*='pop-top'][data-ibx-type='ibxMenu'] div[data-ibx-type*='MenuItem']"
            context_popup_elems = utillobj.validate_and_get_webdriver_objects(context_popup_css, 'Context menu popup')
            context_popup_elem_list = j_script.get_elements_text(context_popup_elems)
            return_style_value = utillobj.get_element_attribute(context_popup_elems[context_popup_elem_list.index(context_menu_option_name)], 'style').replace(' ','')
            utillobj.asin('font-weight:bold', return_style_value.lower(), msg)
        
        '''
        TESTCASE VARIABLES
        '''
        medium_wait = 60
        tree_css = wf_mainpage_locators.WfMainPageLocators.REPOSITORY_TREE_CSS
        breadcrumb_path1='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->Reports'
        breadcrumb_path='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->Visualizations'
        expected_Report_item_list= ['Margin by Product Category', 'Quantity Sold By Stores', 'Sales Metrics YTD', 'Yearly Product Metrics']
        expected_right_arrow_option = ['My Content', 'Reports', 'Charts', 'Documents', 'Visualizations', 'Portal', 'InfoApps', 'Mobile']
        banner_elem=".banner-group-spacer"
        
        """ Step 1: Sign in to WebFOCUS as Basic User.
        """
        wftools_login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """Step 2: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_until_element_is_visible(tree_css, medium_wait)
        
        """ Step 3: Expand Domain > P292_S10660 > G169261 > Breadcrumb Trail and Search > Retail Samples
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        time.sleep(3)
        wfmain_obj.verify_crumb_box(breadcrumb_path, 'Step 2:verify breadcrumb path')
        
        """ Step 4: Click on > before Visualizations in the breadcrumb
            Verify the drop-down list appears with My Content, Reports, Charts, Documents, Visualizations (appears in bold), Portal, InfoApps, Mobile
        """
        wfmain_obj.verify_options_form_right_arrow_in_crumb_box('Retail Samples', expected_right_arrow_option, '3')
        verify_context_popup_style_attribute('Visualizations', 'Step:3.1 verify visualization appears on bold')
        banner_obj=utillobj.validate_and_get_webdriver_object(banner_elem,'Home page banner css')
        core_utilobj.left_click(banner_obj)
        
        """Step 5: Select Reports from drop down list
           Verify breadcrumb trail is ""Domains > P292_S10660 > G169261 > Breadcrumb Trail and Search > Retail Samples > Reports". 
           Verify Reports the in tree and items in Reports folder appear in the canvas area
        """
        wfmain_obj.select_options_form_right_arrow_in_crumb_box('Retail Samples','Reports')
        wfmain_obj.verify_crumb_box(breadcrumb_path1, 'Step 4:verify breadcrumb path')
        
        wfmain_obj.verify_items_in_grid_view(expected_Report_item_list, 'asin','Step 4.1 verify items in dashboard views' )
        
        
        """ Step 6: Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_until_element_is_visible(tree_css, medium_wait)
        wfmain_obj.select_option_from_crumb_box('Workspaces')
        
        """ Step 7: In the banner link, click on the top right username > Sign out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()         
