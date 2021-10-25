'''
Created on July 30, 2019.

@author: Aftab

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2510944
TestCase Name = Run a PGX
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.locators.page_designer_design import ContentTab
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Preview
from common.pages.page_designer_miscelaneous import PageDesignerMiscelaneous

class C2510944_TestClass(BaseTestCase):

    def test_C2510944(self):
        
        """
        TESTCASE OBJECT'S
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        main_page_run_obj=wf_mainpage.Run(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        pd_locator_obj=ContentTab()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_preview_obj = Preview(self.driver)
        pd_miscelanouns_obj=PageDesignerMiscelaneous(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        folder_name="Domains->Retail Samples->InfoApps"
        fex_name="Sales Dashboard (Filtered)"
        filter_panle_css = ".pd-regular-filter-wrapper"
        
        ''' local methods '''
        def verify_move(step_number):
            category_sales = pd_miscelanouns_obj.get_pd_container_object("Category Sales")
            before_move=core_util_obj.get_web_element_coordinate(category_sales,  element_location='top_left')
            source_cord=core_util_obj.get_web_element_coordinate(category_sales, element_location="top_middle", yoffset=21)
            target_cord=core_util_obj.get_web_element_coordinate(category_sales, element_location="bottom_right")
            core_util_obj.drag_and_drop(source_cord['x'], source_cord['y'], target_cord['x'], target_cord['y'])
            after_move=core_util_obj.get_web_element_coordinate(category_sales,  element_location='top_left')
            status = 'panel moved'
            if before_move == after_move:
                status = 'panel not moved'
            util_obj.asequal('panel not moved', status, "Step " + step_number + ": Verify you are not able to move the panels at run-time when you try to drag them.")
        
        def verify_size_increase(step_number):
            category_sales = pd_miscelanouns_obj.get_pd_container_object("Category Sales")
            before_resize = category_sales.size
            source_cord=core_util_obj.get_web_element_coordinate(category_sales, element_location="bottom_right", xoffset=-3, yoffset=-3)
            core_util_obj.drag_and_drop_without_using_click(source_cord['x'], source_cord['y'], int(source_cord['x'])+49, int(source_cord['y'])+49)
            after_resize = pd_miscelanouns_obj.get_pd_container_object("Category Sales").size
            status = 'Panel resized'
            if before_resize == after_resize:
                status = 'Panel not resized'
            util_obj.asequal('Panel not resized', status, "Step " + step_number + ": Verify that you can't increase the size of the panel ")
        
        def verify_chart_without_overlapping(step_number):
            
            ''' [csmr]Category Sales middle right (x)  and [rstml]Regional Sales Trend middle left (x) location '''
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Category Sales")
            csmr=core_util_obj.get_web_element_coordinate(container_obj,element_location="middle_right")['x']
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Regional Sales Trend")
            rstml=core_util_obj.get_web_element_coordinate(container_obj,element_location="middle_left")['x']
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Regional Sales Trend")
            rstbm=core_util_obj.get_web_element_coordinate(container_obj,element_location="bottom_middle")['y']
            
            ''' Regional Sales Trend middle right (x)  and Discount by Region middle left (x) location ''' 
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Regional Sales Trend")
            rstmr=core_util_obj.get_web_element_coordinate(container_obj,element_location="middle_right")['x']
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Discount by Region")
            dbrml=core_util_obj.get_web_element_coordinate(container_obj,element_location="middle_left")['x']
            
            ''' Discount by Region middle right (x)  and Regional Profit by Category middle left (x) location ''' 
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Discount by Region")
            dbrmr=core_util_obj.get_web_element_coordinate(container_obj,element_location="middle_right")['x']
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Discount by Region")
            dbrbm=core_util_obj.get_web_element_coordinate(container_obj,element_location="bottom_middle")['y']
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Regional Profit by Category")
            rpcml=core_util_obj.get_web_element_coordinate(container_obj,element_location="middle_left")['x']
            
            ''' Category Sales middle right (x)  and Example of a Tab Container middle left (x) location ''' 
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Category Sales")
            csbm=core_util_obj.get_web_element_coordinate(container_obj,element_location="bottom_middle")['y']
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Example of a Tab Container")
            etctm=core_util_obj.get_web_element_coordinate(container_obj,element_location="top_middle")['y']
            
            ''' Regional Profit by Category middle right (x)  and Example of a Carousel Container middle left (x) location ''' 
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Regional Profit by Category")
            rpbcbm=core_util_obj.get_web_element_coordinate(container_obj,element_location="bottom_middle")['y']
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Example of a Carousel Container")
            eccbm=core_util_obj.get_web_element_coordinate(container_obj,element_location="top_middle")['y']
            
            ''' filter panel and panel location '''
            fpbm = core_util_obj.get_web_element_coordinate(util_obj.validate_and_get_webdriver_object(filter_panle_css, 'filter_panle_css'), element_location="bottom_middle")['y']
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Category Sales")
            cstm=core_util_obj.get_web_element_coordinate(container_obj,element_location="top_middle")['y']
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Regional Sales Trend")
            rsttm=core_util_obj.get_web_element_coordinate(container_obj,element_location="top_middle")['y']
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Discount by Region")
            dbrtm=core_util_obj.get_web_element_coordinate(container_obj,element_location="top_middle")['y']
            container_obj=pd_miscelanouns_obj.get_pd_container_object("Regional Profit by Category")
            rpbctm=core_util_obj.get_web_element_coordinate(container_obj,element_location="top_middle")['y']
            
            ''' comparison '''
            status = 'Overlapped'
            if csmr<rstml and rstmr<dbrml and dbrmr<rpcml and csbm<etctm and rstbm<etctm and rpbcbm<eccbm and dbrbm<eccbm and fpbm<cstm and fpbm<rsttm and fpbm<dbrtm and fpbm<rpbctm:
                status = 'Not overlapped'
            util_obj.asequal('Not overlapped', status, "Step " + step_number + ": chart visible clearly without overlapping")
            
        """
        Step 1: Login WF as domain developer.
        Click on Content view from side bar.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 2: Navigate to Retail Samples > InfoApp folder.
        """
        main_page_obj.expand_repository_folder(folder_name)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, fex_name, main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 3: Right click "Sales Dashboard (Filtered)" page and select Run.
                Verify that the page runs with no resource selector on the left and no property panel on the right.
        """
        main_page_obj.right_click_folder_item_and_select_menu(fex_name, "Run")
        util_obj.synchronize_until_element_is_visible(".ibx-iframe-frame", main_page_obj.home_page_long_timesleep)
        core_util_obj.switch_to_frame(frame_css=".ibx-iframe-frame")
        page_designer_preview_obj.switch_to_container_frame('Category Sales', timeout=main_page_obj.home_page_long_timesleep)
        util_obj.synchronize_until_element_is_visible("#jschart_HOLD_0", main_page_obj.home_page_long_timesleep)
        core_util_obj.switch_to_default_content()
        core_util_obj.switch_to_frame(frame_css=".ibx-iframe-frame")
        try:
            util_obj.validate_and_get_webdriver_objects(pd_locator_obj.PARENT_CSS, 'resource selector')
            status = 'Resource selector visible'
        except AttributeError:
            status = 'Resource selector not visible'
        util_obj.asequal('Resource selector not visible', status, 'Step 03.00: Verify that the page runs with no resource selector on the left.')
        try:
            util_obj.validate_and_get_webdriver_object(".pd-right-pane div[data-ibx-type='ibxTabPane']", 'property panel')
            status = 'Property panel visible'
        except AttributeError:
            status = 'Property panel not visible'
        util_obj.asequal('Property panel not visible', status, 'Step 03.00: Verify that the page runs with no property panel on the right.')
            
        """ 
        Step 4: Click on Category Sales and try to move it.
                Verify you are not able to move the panels at run-time when you try to drag them.
        """
        verify_move('04.00')
        
        """ 
        Step 5: Click on Category Sales and increase the size of the container.
                Verify that you can't increase the size of the panel.
        """
        verify_size_increase('05.00')
        
        """ 
        Step 6: Click on Show Filters present in top right corner of the page.
                Verify filter section visible and chart visible clearly without overlapping.
        """
        page_designer_preview_obj.click_show_filters()
        util_obj.synchronize_with_visble_text(filter_panle_css, 'Region', 9)
        page_designer_preview_obj.verify_filter_control_labels(['Region:', 'Category:', 'Model:', '', '', ''], "Step 06.00 : Verify filter section visible")
        verify_chart_without_overlapping('06.01')
        
        """ 
        Step 7: Close the run window.
        """
        core_util_obj.switch_to_default_content()
        main_page_run_obj.close()
        
        """ 
        Step 8: Double click on "Sales Dashboard (Filtered)" page to run Run.
        """
        main_page_obj.double_click_on_content_area_items(fex_name)
        util_obj.synchronize_until_element_is_visible(".ibx-iframe-frame", main_page_obj.home_page_long_timesleep)
        core_util_obj.switch_to_frame(frame_css=".ibx-iframe-frame")
        page_designer_preview_obj.switch_to_container_frame('Category Sales', timeout=main_page_obj.home_page_long_timesleep)
        util_obj.synchronize_until_element_is_visible("#jschart_HOLD_0", main_page_obj.home_page_long_timesleep)
        core_util_obj.switch_to_default_content()
        core_util_obj.switch_to_frame(frame_css=".ibx-iframe-frame")
        
        """ 
        Step 9: Click on Category Sales and try to move it.
                Verify you are not able to move the panels at run-time when you try to drag them.
        """
        verify_move('09.00')
        
        """ 
        Step 10: Click on Category Sales and increase the size of the container.
                 Verify that you can't increase the size of the panel.
        """
        verify_size_increase('10.00')
        
        """ 
        Step 11: Click on Show Filters present in top right corner of the page.
                 Verify filter section visible and chart visible clearly without overlapping.
        """
        page_designer_preview_obj.click_show_filters()
        util_obj.synchronize_with_visble_text(filter_panle_css, 'Region', 9)
        page_designer_preview_obj.verify_filter_control_labels(['Region:', 'Category:', 'Model:', '', '', ''], "Step 11.00: Verify filter section visible")
        verify_chart_without_overlapping('11.01')
        
        """ 
        Step 12: Close the run window.
        """
        core_util_obj.switch_to_default_content()
        main_page_run_obj.close()
        
        """
        Step 13 : Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()