'''
Created on 07-May-2018

@author: AAkhan(AA14564)

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324339
TestCase Name = Help : Help_Run
'''
import unittest, time
from common.lib import utillity,core_utility
from common.pages import wf_legacymainpage, vfour_miscelaneous, vfour_portal_run
from common.lib.basetestcase import BaseTestCase

class C2324339_TestClass(BaseTestCase):

    def test_C2324339(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        core_util_object = core_utility.CoreUtillityMethods(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        BIP_Portal_Path = str(project_id)+'->'+str(suite_id)+'->BIP_V4_Portal'
        portal_name = 'BIP_xxx_Portal123_V4'
        welcome_page_parent_css = "#PortalResourcevBOX table tr td"
        run_page_parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        information_builder_logo_css="[id*='site'][id*='header'] a[class*='brand'] img"
        information_builder_navigation_link_css="[id*='site'][id*='header'] ul:nth-child(1) li a"
        title_css = "div.container div.col-md-8 h1"
        test_case_id="C2324339"
        
        """ Step 1: Sign into WebFOCUS home page as Developer User Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """ Step 2: Right click on 'BIP_xxx_Portal123_V4' and choose Run
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        
        """ Step 3: Click on the Help link
        """
        """ Step 4: Click on WebFOCUS Online Help link
                    Verify link opens without error.
                    Close Help window.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Help', option='Online Help')
        core_util_object.switch_to_new_window()
        '''verify help window left panel'''
        portal_misobj.verify_help_window_left_panel('Navigating the WebFOCUS Home Page', 'Step 4: Verify that you are in the Portal Designer Overview section.')
        
        '''verify help window right panel'''
        msg='Step 4.1: Verify that you are in Navigating the WebFOCUS Home Page section.'
        portal_misobj.verify_help_window_right_panel(['WebFOCUS Home Page>Introducing WebFOCUS and the Home Page'], msg, right_panel_css="div.help_breadcrumbs")
        msg='Step 4.2: Verify that you are in Navigating the WebFOCUS Home Page section.'
        portal_misobj.verify_help_window_right_panel(['Navigating the  WebFOCUS Home Page'], msg)
        time.sleep(3)
        utillobj.take_browser_snapshot(test_case_id+'_Actual_Step_4')
        time.sleep(3)
        core_util_object.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        
        """ Step 5: Click on Information Center link
                    Verify link opens without error.
                    Close Information Center window.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Help', option='Information Center')
        core_util_object.switch_to_new_window()
        utillobj.synchronize_with_number_of_element(information_builder_logo_css, 1, 90)
        expected_title="InformationCenter"
        actual_title=self.driver.title.strip().replace(' ','')
        utillobj.asin(expected_title, actual_title, "Step 5: Verify Information Center page title.")
        expected_title='https://webfocusinfocenter.informationbuilders.com/wfappent/'
        actual_title=self.driver.current_url
        utillobj.asequal(expected_title, actual_title, "Step 5.1: Verify Information Center page URL link.")
        status=self.driver.find_element_by_css_selector(information_builder_logo_css).is_displayed()
        utillobj.asequal(True, status, "Step 5.2: Verify Information Center page logo verification.")
        information_builder_navigation_link_elems = self.driver.find_elements_by_css_selector(information_builder_navigation_link_css)
        actual_item = [elem for elem in [elem.text.strip() for elem in information_builder_navigation_link_elems if elem != ''] if elem != '']
        expected_item = ['Our Products', 'Our Company', 'Contact Us']
        for item in expected_item:
            if item in actual_item:
                status=True
            else:
                status=True
                break
        if status== True:
            utillobj.asequal(True, status, "Step 5.3: Verify Information Center page navigation link verification.") 
        else:
            utillobj.asin(item, actual_item, "Step 5.3: Verify Information Center page navigation link verification.")
        time.sleep(3)
        utillobj.take_browser_snapshot(test_case_id+'_Actual_Step_5')
        time.sleep(3)
        core_util_object.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        
        """ Step 6: Click on VideoAssist link
                    Verify link opens without error.
                    Close VideoAssist window.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Help', option='VideoAssist')
        core_util_object.switch_to_new_window()
        utillobj.synchronize_with_number_of_element(information_builder_logo_css, 1, 90)
        expected_title="Videos"
        actual_title=self.driver.title.strip().replace(' ','')
        utillobj.asin(expected_title, actual_title, "Step 6: Verify VideoAssist page title.")
        expected_title='https://webfocusinfocenter.informationbuilders.com/wfappent/video.html'
        actual_title=self.driver.current_url
        utillobj.asequal(expected_title, actual_title, "Step 6.1: Verify VideoAssist page URL link.")
        status=self.driver.find_element_by_css_selector(information_builder_logo_css).is_displayed()
        utillobj.asequal(True, status, "Step 6.2: Verify VideoAssist page logo verification.")
        information_builder_navigation_link_elems = self.driver.find_elements_by_css_selector(information_builder_navigation_link_css)
        actual_item = [elem for elem in [elem.text.strip() for elem in information_builder_navigation_link_elems if elem != ''] if elem != '']
        expected_item = ['Our Products', 'Our Company', 'Contact Us']
        for item in expected_item:
            if item in actual_item:
                status=True
            else:
                status=True
                break
        if status== True:
            utillobj.asequal(True, status, "Step 6.3: Verify VideoAssist page navigation link verification.") 
        else:
            utillobj.asin(item, actual_item, "Step 6.3: Verify VideoAssist page navigation link verification.")
        expected_text = "VideoAssist"
        actual_text  = self.driver.find_element_by_css_selector(title_css).text.strip()
        utillobj.asequal(expected_text, actual_text, "Step 6.4: Verify VideoAssist page 'VideoAssist' title verification.")
        time.sleep(3)
        utillobj.take_browser_snapshot(test_case_id+'_Actual_Step_6')
        time.sleep(3)
        core_util_object.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        
        """ Step 7: Click on Technical Library link.
                    Verify link opens without error.
                    Close Technical Library window.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Help', option='Technical Library')
        core_util_object.switch_to_new_window()
        utillobj.synchronize_with_number_of_element(information_builder_logo_css, 1, 90)
        expected_title="TechnicalContent"
        actual_title=self.driver.title.strip().replace(' ','')
        utillobj.asin(expected_title, actual_title, "Step 7: Verify Technical Library page title.")
        expected_title='https://webfocusinfocenter.informationbuilders.com/wfappent/technical-library.html'
        actual_title=self.driver.current_url
        utillobj.asequal(expected_title, actual_title, "Step 7.1: Verify Technical Library page URL link.")
        status=self.driver.find_element_by_css_selector(information_builder_logo_css).is_displayed()
        utillobj.asequal(True, status, "Step 7.2: Verify Technical Library page logo verification.")
        information_builder_navigation_link_elems = self.driver.find_elements_by_css_selector(information_builder_navigation_link_css)
        actual_item = [elem for elem in [elem.text.strip() for elem in information_builder_navigation_link_elems if elem != ''] if elem != '']
        expected_item = ['Our Products', 'Our Company', 'Contact Us']
        for item in expected_item:
            if item in actual_item:
                status=True
            else:
                status=True
                break
        if status== True:
            utillobj.asequal(True, status, "Step 7.3: Verify Technical Library page navigation link verification.") 
        else:
            utillobj.asin(item, actual_item, "Step 7.3: Verify Technical Library page navigation link verification.")
        expected_text = "Technical Content"
        actual_text  = self.driver.find_element_by_css_selector(title_css).text.strip()
        utillobj.asequal(expected_text, actual_text, "Step 7.4: Verify Technical Library page 'Technical Library' title verification.")
        time.sleep(3)
        utillobj.take_browser_snapshot(test_case_id+'_Actual_Step_7')
        time.sleep(3)
        core_util_object.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        
        """ Step 8: Click on Community link.
                    Verify link opens without error.
                    Close Community window.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Help', option='Community')
        core_util_object.switch_to_new_window()
        information_builder_logo_css="a[title='Home']"
        utillobj.synchronize_with_number_of_element(information_builder_logo_css, 1, 90)
        expected_title="Community"
        actual_title=self.driver.title.strip().replace(' ','')
        utillobj.asin(expected_title, actual_title, "Step 8: Verify Community page title.")
        expected_title='https://www.informationbuilders.com/support/wf_dev_center'
        actual_title=self.driver.current_url
        utillobj.asequal(expected_title, actual_title, "Step 8.1: Verify Community page URL link.")
        status=self.driver.find_element_by_css_selector(information_builder_logo_css).is_displayed()
        utillobj.asequal(True, status, "Step 8.2: Verify Community page logo verification.")
        information_builder_navigation_link_css="nav[role='navigation'] ul[class*='primary'][role='menubar'] li[role='menuitem']"
        information_builder_navigation_link_elems = self.driver.find_elements_by_css_selector(information_builder_navigation_link_css)
        actual_item = [elem for elem in [elem.text.strip() for elem in information_builder_navigation_link_elems if elem != ''] if elem != '']
        expected_item = ['Our Products', 'Our Company']
        for item in expected_item:
            if item in actual_item:
                status=True
            else:
                status=True
                break
        if status== True:
            utillobj.asequal(True, status, "Step 8.3: Verify Community page navigation link verification.") 
        else:
            utillobj.asin(item, actual_item, "Step 8.3: Verify Community page navigation link verification.")
        title_css="h1.m-feature-title"
        expected_text = "Customer Community"
        actual_text = self.driver.find_element_by_css_selector(title_css).text.strip()
        utillobj.asequal(expected_text, actual_text, "Step 8.4: Verify Community page 'Customer Community' title verification.")
        time.sleep(3)
        utillobj.take_browser_snapshot(test_case_id+'_Actual_Step_8')
        time.sleep(3)
        core_util_object.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
         
        """ Step 9: Click on Information Builders Home link.
                    Verify link opens without error.
                    Close Information Builders Home window.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Help', option='Information Builders Home')
        core_util_object.switch_to_new_window()
        information_builder_logo_css="a[title='Home']"
        utillobj.synchronize_with_number_of_element(information_builder_logo_css, 1, 90)
        expected_title="InformationBuilders"
        actual_title=self.driver.title.strip().replace(' ','')
        utillobj.asin(expected_title, actual_title, "Step 9: Verify Information Builders page title.")
        expected_title='https://www.informationbuilders.com/'
        actual_title=self.driver.current_url
        utillobj.asequal(expected_title, actual_title, "Step 9.1: Verify Information Builders page URL link.")
        status=self.driver.find_element_by_css_selector(information_builder_logo_css).is_displayed()
        utillobj.asequal(True, status, "Step 9.2: Verify Information Builders page logo verification.")
        information_builder_navigation_link_css="nav[role='navigation'] ul[class*='primary'][role='menubar'] li[role='menuitem']"
        information_builder_navigation_link_elems = self.driver.find_elements_by_css_selector(information_builder_navigation_link_css)
        actual_item = [elem for elem in [elem.text.strip() for elem in information_builder_navigation_link_elems if elem != ''] if elem != '']
        expected_item = ['Our Products', 'Our Company']
        for item in expected_item:
            if item in actual_item:
                status=True
            else:
                status=True
                break
        if status== True:
            utillobj.asequal(True, status, "Step 9.3: Verify Information Builders page navigation link verification.") 
        else:
            utillobj.asin(item, actual_item, "Step 9.3: Verify Information Builders page navigation link verification.")
        time.sleep(3)
        utillobj.take_browser_snapshot(test_case_id+'_Actual_Step_9')
        time.sleep(3)
        core_util_object.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        
        """ Step 10: Click on about Webfoucs
                     Verify that you get the gen information.
                     Close about Webfoucs window
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Help', option='About')
        core_util_object.switch_to_new_window()
        title_css="table tr:nth-child(1)"
        utillobj.synchronize_with_number_of_element(title_css, 1, 90)
        expected_title='About'
        actual_title=self.driver.title.strip().replace(' ','')
        utillobj.asin(expected_title, actual_title, "Step 10: Verify About page title.")
        expected_title='http://unxrh7:19064/ibi_apps/tools/console/wfinformationpage.jsp'
        actual_title=self.driver.current_url
        utillobj.asequal(expected_title, actual_title, "Step 10.1: Verify About page URL link.")
        status=self.driver.find_element_by_css_selector(title_css).text.strip()
        utillobj.asequal('WebFOCUS Business Intelligence', status, "Step 10.2: Verify About page title verification.")
        about_css="table tr.Ulabel td:nth-child(2)"
        about_elems = self.driver.find_elements_by_css_selector(about_css)
        actual_item = [elem for elem in [elem.text.strip() for elem in about_elems if elem != ''] if elem != '']
        about_css1="table tr.Ulabel td:nth-child(4)"
        about_elems1 = self.driver.find_elements_by_css_selector(about_css1)
        actual_item1 = [elem for elem in [elem.text.strip() for elem in about_elems1 if elem != ''] if elem != '']
        expected_item = ['Edition:', 'Product Release:', 'Service Pack:', 'Package Name:', 'Release ID:', 'Build/GEN Number:', 'Build/GEN Date:', 'Application Server:']
        for item in expected_item:
            if item in actual_item and actual_item1[expected_item.index(item)] != None:
                status=True
            else:
                status=True
                break
        if status== True:
            utillobj.asequal(True, status, "Step 10.3: Verify About page gen information verification.") 
        else:
            utillobj.asin(item, actual_item, "Step 10.3: Verify About page gen information verification.")
        core_util_object.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        
        """ Step 11: Click on Licenses
                     Verify that you get a list of 3rd party information.
                     Close Licenses window.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Help', option='Licenses')
        core_util_object.switch_to_new_window()
        title_css="table tr:nth-child(1) td.h6"
        utillobj.synchronize_with_number_of_element(title_css, 1, 90)
        expected_title='3rdPartyInformation'
        actual_title=self.driver.title.strip().replace(' ','')
        utillobj.asin(expected_title, actual_title, "Step 11: Verify 3rd Party Information page title.")
        expected_title='http://unxrh7:19064/ibi_apps/licenseinfopage.jsp'
        actual_title=self.driver.current_url
        utillobj.asequal(expected_title, actual_title, "Step 11.1: Verify 3rd Party Information page URL link.")
        status=self.driver.find_element_by_css_selector(title_css).text.strip()
        utillobj.asequal('3rd Party Information', status, "Step 11.2: Verify 3rd Party Information page title verification.")
        Party_header_css="table td.console-header span"
        Party_header_elems = self.driver.find_elements_by_css_selector(Party_header_css)
        actual_item = [elem for elem in [elem.text.strip() for elem in Party_header_elems if elem != ''] if elem != '']
        expected_item = ['Description', 'Version', 'File(s)', 'Licenses', 'Third Party Links', 'Release', 'Update History', 'Date']
        for item in expected_item:
            if item in actual_item:
                status=True
            else:
                status=True
                break
        if status== True:
            utillobj.asequal(True, status, "Step 11.3: Verify 3rd Party Information Header verification.") 
        else:
            utillobj.asin(item, actual_item, "Step 11.3: Verify 3rd Party Information Header verification.")
        party_info_css="table td.console-header a"
        b4_obj=utillobj.beautifulsoup_object_creation()
        total_info = b4_obj.select(party_info_css)
        acutal_info = [elem for elem in [elem.get_text(strip=True) for elem in total_info] if elem != '']
        for item in acutal_info:
            if 'Apache' in item:
                status_=True
                break
            else:
                status_=False
        if status_== True:
            utillobj.asequal(True, status_, "Step 11.4: Verify 3rd Party Information verification.") 
        else:
            utillobj.asin('Apache', acutal_info, "Step 11.4: Verify 3rd Party Information verification.")
        core_util_object.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 90)
        time.sleep(2)
        
        """ Step 12: Click Close link
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """ Step 13: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()