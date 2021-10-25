'''
Created on Sep 5, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324218
TestCase Name = Portal Designer_Design Tree : Create_Chart_under_F8_Resource_Tree 
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, wf_mainpage, vfour_miscelaneous, vfour_portal_canvas, visualization_metadata, visualization_ribbon, vfour_portal_ribbon, wf_legacymainpage
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2324218_TestClass(BaseTestCase):

    def test_C2324218(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2324218'
        
        """
        Step 01: Sign in as WF Developer
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        vfour_misc0bj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vfour_ribbonobj = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(1)
        
        """
        Step 02: Edit 'BIP_xxx_Portal123_V4' from P292 domain->S10117 folder
        """
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
        time.sleep(5)
        utillobj.switch_to_window(1)
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(3)
        portal_canvas.select_page_in_navigation_bar('Page 1')
        time.sleep(2)
        vfour_ribbonobj.invoke_and_verify_wf_resource_tree()
        win_ = driver.window_handles
        
        """
        Step 03: Create new chart under the domain
        Step 04: Choose car.mas
        """
        time.sleep(2)
        vfour_misc0bj.select_resource_menu('P292->S10117->BIP_V4_Portal', 'New->Chart')
        time.sleep(8)
        utillobj.switch_to_window(2, custom_windows=win_)
        time.sleep(4)
        utillobj.select_masterfile_in_open_dialog('ibisamp','car')
        time.sleep(3)
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        parent_css="#pfjTableChart_1 g.chartPanel g text"
        resultobj.wait_for_property(parent_css, 11)         
        time.sleep(5)
        
        """
        Step 05: Double click Country and Dealer_Cost
        """
        metaobj.datatree_field_click("COUNTRY",2,1)
        time.sleep(4)
        parent_css= "#TableChart_1 g.chartPanel g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 5)
        
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        time.sleep(4)
        parent_css= "#TableChart_1 g.chartPanel g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        
        result_obj.verify_xaxis_title("TableChart_1", 'COUNTRY', "Step 05a: Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'DEALER_COST', "Step 05b: Verify Y-Axis Title")
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 05c: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 5, 'Step 05d: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 05e: Verify first series first riser Color')
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 06: Click the IA button and choose Save. Name it as 'IA_Chart1'
        """
        time.sleep(3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
        Step 07: Exit out of IA
        """
        time.sleep(5)
        ribbonobj.select_tool_menu_item('menu_exit')
        time.sleep(5)
        utillobj.switch_to_window(1)
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """Verify the chart is listed under Resource tree."""
        time.sleep(2)
        vfour_misc0bj.verify_resource_item('P292->S10117->BIP_V4_Portal', Test_Case_ID, '07', item_exit=True)
        
        """
        Step 08: Exit portal designer. 
        """
        time.sleep(2)
        vfour_ribbonobj.select_tool_menu_item('menu_Exit')
        time.sleep(2)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=WfMainPageLocators.__dict__['banner_administrator']
        resultobj._validate_page(elem1)
        
        """Sign Out from WebFOCUS"""
        
        
if __name__ == '__main__':
    unittest.main()