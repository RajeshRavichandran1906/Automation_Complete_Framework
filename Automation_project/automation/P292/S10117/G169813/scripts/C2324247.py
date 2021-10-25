'''
Created on Oct 04, 2017

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10117&group_by=cases:section_id&group_id=169813&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2324247
TestCase Name = Portal Designer_Design content : Edit_Portal_add_new_page_and_Content2
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import vfour_portal_ribbon, vfour_portal_canvas, visualization_resultarea, wf_legacymainpage
from common.lib import utillity,core_utility

class C2324247_TestClass(BaseTestCase):
    
    def test_C2324247(self):
        driver = self.driver #Driver reference object created
        """
            TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        coreutillobj=core_utility.CoreUtillityMethods(self.driver)
        suite_id = utillobj.parseinitfile('suite_id')
        project_id = utillobj.parseinitfile('project_id')
        Portal_Name = 'BIP_xxx_Portal123_V4'
        BIP_Portal_Path = project_id+'->'+suite_id+'->BIP_V4_Portal'
        Page_Name = 'Test_Page2'
        wf_main_obj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        vfour_ribbon_obj = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        vfour_portal_canvas_obj=vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        vfour_canvasobj = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)

        """    1. Sign into http://machine:port/alias/ as WF developer    """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css="#bipTreePanel tbody tr:nth-child(1)> td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        
        
        """    2. Edit 'BIP_xxx_Portal123_V4' portal    """
        wf_main_obj.select_repository_menu(BIP_Portal_Path+'->'+Portal_Name, 'Edit')
        time.sleep(5)
        coreutillobj.switch_to_new_window()
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 120)
        
        
        """    3. Click the new page icon    """
        """    4. Choose 4 Columns; rename the new page to 'Test_Page2'.    """
        vfour_portal_canvas_obj.add_page('4 Column', Page_title="Test_Page2")
        time.sleep(5)
        vfour_portal_canvas_obj.verify_page_in_navigation_bar(Page_Name, "Step 04a: Verify that the Test_Page2 is Created", verify=True)
        
        """    5. From F8 resource tree on right hand side, drag contents from the WebFOCUS Resources tree and drop it all 4 columns in the page;
        Verify each column is populated as an example but you can add anything (category sales, regional sales trend, stores sales by region, revenue region bar) all from the retail samples domain    """
        
        vfour_ribbon_obj.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        utillobj.synchronize_with_number_of_element('#treeContainer', 1, 120)
        time.sleep(3)
        vfour_portal_canvas_obj.select_column(1)
        time.sleep(3)
        item_path="Retail Samples->Portal->Small Widgets->Category Sales"
        vfour_portal_canvas_obj.dragdrop_repository_item_to_canvas(item_path, "column",1)
        resobj.wait_for_property('Category Sales', None, expire_time=190, string_value='Category Sales', parent_object=vfour_portal_canvas_obj.get_current_page())
        vfour_portal_canvas_obj.verify_column_panel_caption(1, 'Category Sales', "Step 05(1)a: Verify first panel title")        
        time.sleep(3)
        
        vfour_portal_canvas_obj.select_column(2)
        time.sleep(3)
        item_path="Retail Samples->Portal->Small Widgets->Regional Sales Trend"
        vfour_portal_canvas_obj.dragdrop_repository_item_to_canvas(item_path, "column",2)
        resobj.wait_for_property('Regional Sales Trend', None, expire_time=190, string_value='Regional Sales Trend', parent_object=vfour_portal_canvas_obj.get_current_page())
        vfour_portal_canvas_obj.verify_column_panel_caption(2, 'Regional Sales Trend', "Step 05(2)a: Verify second panel title")
        
        vfour_portal_canvas_obj.select_column(3)
        time.sleep(3)
        item_path="Retail Samples->Portal->Large Widgets->Store Sales by Region"
        vfour_portal_canvas_obj.dragdrop_repository_item_to_canvas(item_path, "column",3)
        resobj.wait_for_property('Store Sales by Region', None, expire_time=190, string_value='Store Sales by Region', parent_object=vfour_portal_canvas_obj.get_current_page())
        vfour_portal_canvas_obj.verify_column_panel_caption(3, 'Store Sales by Region', "Step 05(3)a: Verify third panel title")
        time.sleep(3)
        
        vfour_portal_canvas_obj.select_column(4)
        item_path="Retail Samples->Portal->Small Widgets->Revenue Region Bar"
        vfour_portal_canvas_obj.dragdrop_repository_item_to_canvas(item_path, "column",4)
        resobj.wait_for_property('Revenue Region Bar', None, expire_time=190, string_value='Revenue Region Bar', parent_object=vfour_portal_canvas_obj.get_current_page())
        vfour_portal_canvas_obj.verify_column_panel_caption(4, 'Revenue Region Bar', "Step 05(4)a: Verify fourth panel title")
        time.sleep(3)
        
        """    6. Open the Resources folder and try to drag a page onto the page canvas...Verify that you get the no drop icon    """
        
        target_elem = driver.find_element_by_css_selector("#BIPortalPanel")
        vfour_canvasobj.verify_no_drag_drop_icon_on_canvas(BIP_Portal_Path+'->BIP_xxx_Portal123_V4 Resources->Test_Page', target_elem, 'C2324247', 'Step 06: Verify that you get the no drop icon', ty_offset=150, mouse_move_duration=1)
        
        """    7. Click the new page icon...Verify that the page templates appear    """
        driver.find_element_by_css_selector("div[id^='BipNavigatorTop'] div[id^='BipAddButton']").click()
        time.sleep(7)
        css="#dlgTitleExplorer"
        css1 = css + "[style*='inherit'] [class*='active'] [class*='caption'] [class*='bi-label']"
        utillobj.verify_popup(css, "Step 03:02 : Verify that the Page Templates dialog showed.", caption_css=css1, caption_text='Add Page')
        page_tempcss=css+" div[class*='tile_exp_header']"
        utillobj.verify_popup(css, "Step 04:Add Page dialog window shown", popup_text_css=page_tempcss, popup_text='Page Templates')
        
        """    8. Click Cancel    """
        utillobj.click_dialog_button("#dlgTitleExplorer", "Cancel")
        time.sleep(3)
        
        """    9. Save the portal and exit    """
        vfour_ribbon_obj.select_tool_menu_item('menu_Save')
        time.sleep(2)
        vfour_ribbon_obj.select_tool_menu_item('menu_Exit')
        
        time.sleep(2)
        
        """    10. Sign Out from WebFOCUS and close the browser    """
        
        
if __name__ == "__main__":
    unittest.main()