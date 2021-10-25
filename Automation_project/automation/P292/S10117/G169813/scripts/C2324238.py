'''
Created on Sep 14, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324238
TestCase Name = Run Mode_Run Tree : Run_Reports_frm_Resource_tree_Panel_And_Close_Portal_Run_Mode
'''

import unittest, time
from common.lib import utillity, core_utility
from common.pages import visualization_resultarea, ia_resultarea, vfour_portal_run, wf_legacymainpage, vfour_portal_canvas
from common.lib.basetestcase import BaseTestCase

class C2324238_TestClass(BaseTestCase):

    def test_C2324238(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        Test_Case_ID = 'C2324238'
        Image_ID = 'C2324118'
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        vfour_runobj = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        coreutillobj=core_utility.CoreUtillityMethods(self.driver)
        proj_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        parent_folder_name='BIP_V4_Portal'
        BIP_Portal_Path = str(proj_id)+'->'+str(suite_id)+'->'+parent_folder_name
        
        """
        Step 01: Sign into WebFOCUS home page as Developer User
                 Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190) 
        
        """
        Step 02: Run 'BIP_xxx_Portal123_V4' portal under P292 domain -> S10117 folder.
        """
        wf_mainobj.select_repository_menu(BIP_Portal_Path+'->BIP_xxx_Portal123_V4', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        
        """
        Step 03: From the Resource tree panel Panel1(located inside the panel1 in run mode); 
        Double click on P292->S10117-> 'BIP_V4_Portal' folder and run all the created reports such as Accordion report, 
        tagCloud chart, cd7, babydeer, honda_integra, bluehills and IA_Chart1.
        Verify it runs fine without any error.
        """
        portal_canvas.select_page_in_navigation_bar('Page_New')
        time.sleep(9)
        parent_css="#treeView tbody>tr>td>img[src*='discovery_domain']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 120)
        time.sleep(5)
         
        """Accordion report"""
        vfour_runobj.select_portal_resource_menu(BIP_Portal_Path+'->Accordion report', 'Run', option_click=2, expand_resource_tree=True)
        time.sleep(3)
        coreutillobj.switch_to_new_window()
        time.sleep(5)
        parent_css="[ibiattr='table1']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 120)
        time.sleep(3) 
        vfour_runobj.verify_table_data_set("[ibiattr='table1']",  Test_Case_ID+ "_Ds01.xlsx","Step 03.1: Verify Accordion report data set")
        time.sleep(2)
        coreutillobj.switch_to_previous_window()
        time.sleep(2)
        utillobj.synchronize_with_number_of_element('#BIPortalPanel', 1, 120) 
          
        """tagCloud chart""" 
        vfour_runobj.select_portal_resource_menu(BIP_Portal_Path+'->tagCloud chart', 'Run', option_click=2)
        time.sleep(3)
        coreutillobj.switch_to_new_window()
        time.sleep(5) 
        parent_css="#jschart_HOLD_0 text[class*='riser!']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, 120)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 5, 'Step03.2: Verify number of tagcloud labels displayed', custom_css="svg g>text[class^='riser!s']")
         
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='riser!s0!g0!mtag!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'ENGLAND',"Step03.3: Verify ENGLAND label text")
         
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='riser!s0!g1!mtag!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'FRANCE',"Step03.4: Verify FRANCE label text")
         
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='riser!s0!g2!mtag!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'ITALY',"Step03.5: Verify ITALY label text")
         
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='riser!s0!g3!mtag!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'JAPAN',"Step03.6: Verify JAPAN label text")
         
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='riser!s0!g4!mtag!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'W GERMANY',"Step03.7: Verify W GERMANY label text")
        time.sleep(3)
        coreutillobj.switch_to_previous_window()
        time.sleep(2)
        utillobj.synchronize_with_number_of_element('#BIPortalPanel', 1, 120)
        
        """cd7"""
        vfour_runobj.select_portal_resource_menu(BIP_Portal_Path+'->cd7', 'View', option_click=2)
        time.sleep(3)
        coreutillobj.switch_to_new_window()
        parent_css="img[src*='cd7']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 120)
        utillobj.verify_picture_using_sikuli(Image_ID+"_Base_step3.png","Step3.8:verfiy picture of cd7.gif")
        coreutillobj.switch_to_previous_window()
        time.sleep(2)
        utillobj.synchronize_with_number_of_element('#BIPortalPanel', 1, 120)
          
        """babydeer"""
        vfour_runobj.select_portal_resource_menu(BIP_Portal_Path+'->babydeer', 'View', option_click=2)
        time.sleep(3)
        coreutillobj.switch_to_new_window()
        utillobj.verify_picture_using_sikuli(Image_ID+"_Base_step3.2.png","Step3.9:verfiy picture of baby deer")
        coreutillobj.switch_to_previous_window()
        time.sleep(2)
        utillobj.synchronize_with_number_of_element('#BIPortalPanel', 1, 120)
          
        """honda_integra"""
        vfour_runobj.select_portal_resource_menu(BIP_Portal_Path+'->honda_integra', 'View', option_click=2)
        time.sleep(3)
        coreutillobj.switch_to_new_window()
        utillobj.verify_picture_using_sikuli(Image_ID+"_Base_step3.1.png","Step3.10:verfiy picture of honda integra")
        coreutillobj.switch_to_previous_window()
        time.sleep(2)
        utillobj.synchronize_with_number_of_element('#BIPortalPanel', 1, 120) 
          
        """Bluehills""" 
        vfour_runobj.select_portal_resource_menu(BIP_Portal_Path+'->Bluehills', 'View', option_click=2)
        time.sleep(3)
        coreutillobj.switch_to_new_window()
        utillobj.verify_picture_using_sikuli(Image_ID+"_Base_step3.3.png","Step3.11:verfiy picture of blue hills")
        coreutillobj.switch_to_previous_window()
        time.sleep(2)
        utillobj.synchronize_with_number_of_element('#BIPortalPanel', 1, 120)
          
        """IA_Chart1""" 
        vfour_runobj.select_portal_resource_menu(BIP_Portal_Path+'->IA_Chart1', 'Run', option_click=2)
        time.sleep(3)
        coreutillobj.switch_to_new_window()
        time.sleep(5) 
        parent_css="#jschart_HOLD_0 rect[class*='riser!']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, 120)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 5, 'Step03.13: Verify number of risers displayed', custom_css="svg g>rect[class^='riser!s']")
        resultobj.verify_xaxis_title("jschart_HOLD_0", "COUNTRY", "Step 03.14: Verify -xAxis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", "DEALER_COST", "Step 03.15: Verify -yAxis Title")
        time.sleep(2)
        expected_xval_list=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step 03.16: Verify XY labels")
        time.sleep(3)
        coreutillobj.switch_to_previous_window()
        time.sleep(2)
        utillobj.synchronize_with_number_of_element('#BIPortalPanel', 1, 120) 
        
        """
        Step 04: Close the portal run mode by clicking on the Close Menubar link.
        """
        vfour_runobj.select_or_verify_portal_menu_bar_item(select='Close', msg='Step 04: Close the portal run mode by clicking on the Close Menubar link.')
        time.sleep(2)
        
        """
        Step 05: Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.navigate_to_legacyhomepage()
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190) 
        
        """
        Step 06: Expand P292 domain ->S10117 folder.
                 Verify that you are back on the main portal page and the portal is still present
        """
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190) 
        time.sleep(1) 
        wf_mainobj.get_repository_item_availability(BIP_Portal_Path+'->BIP_xxx_Portal123_V4')
        
        """
        Step 07: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
        
        
if __name__ == '__main__':
    unittest.main()