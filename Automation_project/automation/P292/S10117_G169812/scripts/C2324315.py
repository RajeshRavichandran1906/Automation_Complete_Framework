'''
Created on 01-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324315
TestCase Name = Portal Designer_Design Content : Drill Down Opens a Portal Page
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, wf_mainpage, vfour_portal_ribbon, vfour_portal_canvas, vfour_portal_run, ia_run, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324315_TestClass(BaseTestCase):

    def test_C2324315(self):
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
        iarunobj = ia_run.IA_Run(self.driver)
        
        """ Step 1: Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        """ Step 2: Open P292 -> S10117 from domains tree,
                    Right Click on 'BIP_xxx_Portal123_V4' and choose edit
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
        
        """ Step 3: Add Page 1 with 2 Column layout
        """
        portal_canvas.add_page('2 Column', Page_title='Page 1')
        
        """ Step 4: Press F8
                    Choose Drilldown_to_portal_page from P292 -> S10117 -> 'BIP_V4_Portal' and drag it to the page canvas to add content there.
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        item_path="P292->S10117->BIP_V4_Portal->Drilldown_to_portal_page"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "column", 1)
        time.sleep(5)
        portal_canvas.verify_panel_caption('Drilldown_to_portal_page', "Step 4: Verify Drilldown_to_portal_page panel drag in canvas.")
        
        """ Step 5: Click New page enter page2 (i.e 2 column) and add some content there.
        """
        portal_canvas.add_page('2 Column', Page_title='page2')
        time.sleep(2)
        item_path="P292->S10117->BIP_V4_Portal->cd7"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "column", 1)
        time.sleep(5)
        portal_canvas.verify_panel_caption('cd7', "Step 5: Verify Drilldown_to_portal_page panel drag in canvas.")
        
        """ Step 6: Click Page 1
                    Click the ENGLAND drill down.
                    Verify that you are now on page 2
                    If you get any errors please make sure that alias in the report matches yours and also that the page2 is the right name.
        """
        portal_canvas.select_page_in_navigation_bar('Page 1')
        column1 = portal_canvas.get_column_obj(1)
        driver.switch_to.frame(column1.find_element_by_css_selector("[class*='bi-iframe iframe'][name^='Panel']"))
        iarunobj.select_and_verify_drilldown_report_field("table[summary='Summary']", 2, 1)
        utillobj.switch_to_default_content(pause=2)
        portal_canvas.verify_panel_caption('cd7', 'Step 6: Verify Page 2 shown and cd7 pangel Displayed.')
        
        """ Step 7: Exit and save
        """
        portal_ribbon.select_tool_menu_item('menu_Save')
        portal_ribbon.select_tool_menu_item('menu_Exit')
        utillobj.switch_to_window(0)
        time.sleep(5)
        
        """ Step 8: Run the portal
        """
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        
        """ Step 9: Click Page 1 and click the ENGLAND drill down.
                    Verify that you are now on page2
        """
        portal_canvas.select_page_in_navigation_bar('Page 1')
        column1 = portal_canvas.get_column_obj(1)
        driver.switch_to.frame(column1.find_element_by_css_selector("[class*='bi-iframe iframe'][name^='Panel']"))
        iarunobj.select_and_verify_drilldown_report_field("table[summary='Summary']", 2, 1)
        utillobj.switch_to_default_content(pause=2)
        portal_canvas.verify_panel_caption('cd7', 'Step 9: Verify Page 2 shown and cd7 pangel Displayed.')
        
        """ Step 10: Click Close
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(5)
        
        
        """ Step 11: Sign Out from WebFOCUS
        """
        time.sleep(5)
                

if __name__ == '__main__':
    unittest.main()