'''
Created on 15-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324266
TestCase Name = Properties testing : Change title
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, wf_mainpage, vfour_portal_canvas, vfour_portal_run, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324266_TestClass(BaseTestCase):

    def test_C2324266(self):
        """
        TESTCASE VARIABLES
        """
        BIP_Portal_Path = 'P292->S10117->BIP_V4_Portal'
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainpageobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        
        """ Step 1: Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(1)
        
        """ Step 2: Open P292->S10117 from Domains tree,
                    Right click on 'BIP_Responsive' portal and choose Change Title
        """
        wf_mainpageobj.change_repository_elem_title(BIP_Portal_Path+'->BIP_Responsive', 'Change Title', 'testing change title')
         
        """ Step 3: Change the title to "testing change title"
                    Verify that the title has been changed.
        """
        wf_mainpageobj.verify_repositery_item(BIP_Portal_Path,'testing change title', msg='3')
         
        """ Step 4: Right Click on Accordion report and choose Change title
                    Enter title as "Accordion_change_title"
                    Verify that the title has been changed.
        """
        wf_mainpageobj.change_repository_elem_title(BIP_Portal_Path+'->Accordion_report', 'Change Title', 'Accordion_change_title')
        time.sleep(1)
        wf_mainpageobj.verify_repositery_item('P292->S10117->BIP_V4_Portal','testing change title', msg='4')
         
        """ Step 5: Right click on the IA_Chart1_1 and choose properties
                    Change the title there and click OK
                    Verify that the title has been changed.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->IA_Chart1_1', 'Properties')
        time.sleep(2)
        wf_mainpageobj.edit_properties_dialog('Main Properties', 'textbox', 'Title', textbox_input='IA_Chart1_1_1')
        wf_mainpageobj.edit_properties_dialog('Main Properties', 'button', 'OK')
        time.sleep(2)
        wf_mainpageobj.verify_repositery_item('P292->S10117->BIP_V4_Portal','IA_Chart1_1_1', msg='5')
         
        """ Step 6: Run the V4 portal "testing change title" located under P292->S10117 .
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->testing change title', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        time.sleep(5)
         
        """ Step 7: Add a new one column page
        """
        portal_canvas.add_page('1 Column',Page_title='Page 5')
         
        """ Step 8: Right click on the page and choose change title
        """
        """ Step 9: Enter testing change page title as title
                    Verify that you get no errors
        """
        portal_canvas.manage_page_menu('Page 5', 'Change Title', change_title='testing change page title')
        portal_canvas.verify_page_in_navigation_bar('testing change page title', "Step 9: Verify that you get no errors and page title changed.")
         
        """ Step 10: Click Close
                     Open the portal hierarchy on the tree
                     Verify that the title change shows on the portal tree under the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(5)
        wf_mainpageobj.verify_repositery_item('P292->S10117->BIP_V4_Portal->BIP_Responsive Resources','testing change title', msg='10')
         
        """ Step 11: Rerun the portal
                     Verify that page is still there and the new title as well.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->testing change title', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        time.sleep(5)
        portal_canvas.verify_page_in_navigation_bar('testing change page title', "Step 11: Verify that page is still there and the new title as well.")
        
        """ Step 12: Right click on the page and choose delete
        """
        portal_canvas.manage_page_menu('testing change page title', 'Delete')
        
        """ Step 13: Click Close
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        """ Step 4: Sign Out from WebFOCUS
        """
        time.sleep(5)
                

if __name__ == '__main__':
    unittest.main()