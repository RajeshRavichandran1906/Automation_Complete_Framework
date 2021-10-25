'''
Created on 12-Dec-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324318
TestCase Name = Run Mode_Run Content : Adding Content at run time
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, wf_mainpage, vfour_portal_canvas, wf_legacymainpage, vfour_portal_run, vfour_portal_ribbon, vfour_miscelaneous, vfour_portal_properties
from common.lib.basetestcase import BaseTestCase

class C2324318_TestClass(BaseTestCase):

    def test_C2324318(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID="C2324318"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainpageobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        BIP_Portal_Path = 'P292->S10117->BIP_V4_Portal'
        portal_name = 'test_run_content'
        
        """ Step 1: Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(1)
        
        """ Step 2: Expand P292 domain , right click on S10117 folder,
                    Create a new portal named 'test_run_content'
        """
        wf_mainpageobj.create_portal(BIP_Portal_Path, portal_name)
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
        portal_misobj.verify_page_template("Step 2: Verify when Portal Designer loads you are on the Layout tab", page_template="1 Column")
        
        """ Step 3: Choose the Single Area layout and name it as 'page1_self_service'
        """
        portal_misobj.select_page_template(page_template="Single Area", Page_title='page1_self_service', btn_name='Create')
                
        """ Step 4: Unlock the page
                    Save and exit the portal
        """
        portal_canvas.select_page_in_navigation_bar('page1_self_service')
        time.sleep(2)
        portal_properties.edit_input_control('page', 'Lock Page', 'checkbox', checkbox_input='uncheck', msg='Step 4: ')
        time.sleep(2)
        portal_canvas.add_page('2 Column',Page_title='Page 2')
        time.sleep(1)
        portal_canvas.select_page_in_navigation_bar('Page 2')
        time.sleep(2)
        portal_properties.edit_input_control('page', 'Lock Page', 'checkbox', checkbox_input='uncheck', msg='Step 4.1: ')
        time.sleep(2)
        portal_ribbon.select_tool_menu_item('menu_Save')
        portal_canvas.manage_page_menu('Page 2', 'Remove')
        time.sleep(1)
        portal_ribbon.bip_save_and_exit(btn_name='Yes')
        utillobj.switch_to_window(0, pause=5)
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(1)
        
        """ Step 5: Run the portal
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        
        """ Step 6: Drag the 'page1_self_service' page in the page tab area
                    Verify that you get a message stating the page already is in the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Resources')
        item_path=BIP_Portal_Path+"->test_run_content Resources->page1_self_service"
        target_elem=driver.find_element_by_css_selector("div[id^='BipNavigatorTop'] div[id^='BipAddButton']")
        portal_run.drag_portal_resource_tree_item(item_path, target_elem)
        time.sleep(1)
        utillobj.verify_js_alert('Page already in portal.', 'Step 6: Verify that you get a message stating the page already is in the portal.')
        
        """ Step 7: Run any report on that first page.
                    Verify that the report output appears in the area
        """
        portal_misobj.select_resource_menu(BIP_Portal_Path + '->Accordion_report', 'Run')
        utillobj.switch_to_window(1)
        portal_run.create_table_data_set("table[ibiattr='table1']", Test_Case_ID+'_Ds01.xlsx')
        portal_run.verify_table_data_set("table[ibiattr='table1']", Test_Case_ID+'_Ds01.xlsx', "Step 7: Accordion_report verification ")
        driver.close()
        time.sleep(1)
        utillobj.switch_to_window(0, pause=5)
        time.sleep(1)
        
        """ Step 8: Drag any other page on to the page tab area and change the title
        """
        item_path=BIP_Portal_Path+"->test_run_content Resources->Page 2"
        target_elem=driver.find_element_by_css_selector("div[id^='BipNavigatorTop'] div[id^='BipAddButton']")
        portal_run.drag_portal_resource_tree_item(item_path, target_elem)
        time.sleep(1)
        portal_canvas.manage_page_menu('Page 2', 'Change Title', change_title='Page 2 Change Title')
        
        """ Step 9: Close and rerun the portal
                    Verify that the report output is not there
                    Verify that the title change is still there.
        """ 
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(1)
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        actual_text = portal_run.get_current_page()
        utillobj.asequal('', actual_text.text, 'Step 9: Verify that the report output is not there.')
        portal_canvas.verify_page_in_navigation_bar('Page 2 Change Title', 'Step 9.1: Verify that the title change is still there.')
        
        """ Step 10: Right click on the second page and choose Remove
        """
        portal_canvas.manage_page_menu('Page 2 Change Title', 'Remove')
        
        """ Step 11: Close the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(1)
        
        """ Step 12: Sign Out from WebFOCUS 
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()