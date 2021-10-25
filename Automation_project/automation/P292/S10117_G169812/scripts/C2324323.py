'''
Created on 06-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324323
TestCase Name = Portal Designer_Design Properties : Page_Refresh
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, wf_mainpage, vfour_portal_ribbon, vfour_portal_canvas, vfour_portal_run, vfour_portal_properties, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase
from selenium.common.exceptions import NoSuchElementException

class C2324323_TestClass(BaseTestCase):

    def test_C2324323(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainpageobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        
        """ Step 1: Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        """ Step 2: Edit the 'BIP_xxx_Portal123_V4' portal
        """
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        utillobj.switch_to_window(1)
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        time.sleep(5)
        
        """ Step 3: Add another page
                    Enter page title as 'Page refresh testing'
        """
        portal_canvas.add_page('1 Column',Page_title='Page refresh testing')
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('Page refresh testing', "Step 3: Verify Page Refresh Testing added.")
        
        """ Step 4: Verify the Show Refresh checkbox is checked under the properties section
        """
        portal_canvas.select_page_in_navigation_bar('Page refresh testing')
        time.sleep(2)
        portal_properties.verify_input_control('page', 'Show Refresh', 'checkbox', 'Step 4: Verify the Show Refresh checkbox is checked under the properties section.', checkbox_input='check')
        
        """ Step 5: Click BIP icon then save and yes
        """
        portal_ribbon.select_tool_menu_item('menu_Save')
        
        """ Step 6: Exit and Run the portal
        """
        portal_ribbon.select_tool_menu_item('menu_Exit')
        utillobj.switch_to_window(0)
        time.sleep(5)
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        
        """ Step 7: Right Click on the page tab
                    Verify that refresh shows
        """
        portal_canvas.verify_page_menu('Page refresh testing', ['Refresh'], 'Step 7: Verify that refresh shows')
        portal_canvas.select_column(1)
        
        """ Step 8: Add new page and check the page tab menu options
                    Change title, page layout, delete and refresh
        """
        
        portal_canvas.add_page('1 Column',Page_title='Page refresh testing1')
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('Page refresh testing1', "Step 8: Verify Page refresh testing1 added in run portal.")
        portal_canvas.verify_page_menu('Page refresh testing1', ['Change Title', 'Page Layout', 'Refresh', 'Delete'], 'Step 8.1: Verify that Page menu option Change title, page layout, delete and refresh.')
        
        """ Step 9: Click the close link
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        """ Step 10: Edit the portal
        """
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        utillobj.switch_to_window(1)
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        time.sleep(5)
        
        """ Step 11: Click on the Page refresh testing page
        """
        portal_canvas.select_page_in_navigation_bar('Page refresh testing')
        
        """ Step 12: Uncheck the Show refresh box
        """
        time.sleep(2)
        portal_properties.edit_input_control('page', 'Show Refresh', 'checkbox', checkbox_input='uncheck', msg="Step 12:")
        
        """ Step 13: Save and exit the portal
        """
        portal_ribbon.select_tool_menu_item('menu_Save')
        portal_ribbon.select_tool_menu_item('menu_Exit')
        utillobj.switch_to_window(0)
        time.sleep(5)
        
        """ Step 14: Run the portal
        """
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        
        """ Step 15: Right Click on the page tab
                    Verify that refresh does not show
        """
        elems=self.driver.find_elements_by_css_selector("div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton']")
        tab_elem=elems[[el.text.strip() for el in elems].index('Page refresh testing')]
        utillity.UtillityMethods.click_on_screen(self, tab_elem, 'middle', click_type=1)
        status_ = False
        try:
            bipopup_css="div[id^='BiPopup'][style*='inherit']"
            menu_option = driver.find_element_by_css_selector(bipopup_css).text
            if menu_option == '':
                status_ = True
            else:
                status_ = False
        except NoSuchElementException:
            status_ = True
        utillobj.asequal(True, status_, "Step 15: Verify that refresh does not show.")
        
        """ Step 16: Right click on the other base pages
                     Verify that refresh does show for the other pages.
        """
        portal_canvas.verify_page_menu('Page 1', ['Refresh'], 'Step 16: Verify that refresh shows')
        
        """ Step 17: Check the menus for the new page added in run time
                     Change title, page layout, delete and refresh
        """
        portal_canvas.verify_page_menu('Page refresh testing1', ['Change Title', 'Page Layout', 'Refresh', 'Delete'], 'Step 17: Verify that Page menu option Change title, page layout, delete and refresh.')
        
        """ Step 18: Close the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        """ Step 19: Sign Out from WebFOCUS
        """
        time.sleep(5)
                
if __name__ == '__main__':
    unittest.main()