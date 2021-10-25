'''
Created on Oct 04, 2017

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10117&group_by=cases:section_id&group_id=169813&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2324247
TestCase Name = Portal Designer_Design content : Edit_Portal_add_new_page_and_Content2
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage, vfour_portal_ribbon, vfour_portal_canvas, visualization_resultarea, ia_resultarea, wf_legacymainpage
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2324247_TestClass(BaseTestCase):
    
    def test_C2324247(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the testpass
        """
            TESTCASE VARIABLES
        """
        Portal_Name = 'BIP_xxx_Portal123_V4'
        BIP_Portal_Path = 'P292->S10117->BIP_V4_Portal'
        Page_Name = 'Test_Page2'
        utillobj = utillity.UtillityMethods(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_main_obj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_main_obj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        vfour_ribbon_obj = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        vfour_portal_canvas_obj=vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        #vfour_miscelaneous_obj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        #vfour_portal_run_obj=vfour_portal_run.Vfour_Portal_Run(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        iaresultobj=ia_resultarea.IA_Resultarea(self.driver)

        """    1. Sign into http://machine:port/alias/ as WF developer    """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#topBannerMenuBox [id^='SignonBannerPanelToolsMenuBtn']"
        result_obj.wait_for_property(parent_css, 1, expire_time=20, string_value="Tools", with_regular_exprestion=True)
        
        """    2. Edit 'BIP_xxx_Portal123_V4' portal    """
        wf_main_obj.select_repository_menu(BIP_Portal_Path+'->'+Portal_Name, 'Edit')
        time.sleep(5)
        utillobj.switch_to_window(1)
        driver.maximize_window()
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        result_obj.wait_for_property(parent_css, 1, expire_time=50)
        
        
        """    3. Click the new page icon    """
        """    4. Choose 4 Columns; rename the new page to 'Test_Page2'.    """
        vfour_portal_canvas_obj.add_page('4 Column', Page_title="Test_Page2")
        time.sleep(2)
        #vfour_portal_canvas_obj.manage_page_menu('4 Column', 'Change Title', change_title='Test_Page2')
        time.sleep(5)
        vfour_portal_canvas_obj.verify_page_in_navigation_bar(Page_Name, "Step 04a: Verify that the Test_Page2 is Created", verify=True)
        
        """    5. From F8 resource tree on right hand side, drag contents from the WebFOCUS Resources tree and drop it all 4 columns in the page;
        Verify each column is populated as an example but you can add anything (category sales, regional sales trend, stores sales by region, revenue region bar) all from the retail samples domain    """
        
        vfour_ribbon_obj.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        elem1=(By.CSS_SELECTOR, "#treeContainer")
        resobj._validate_page(elem1)
        time.sleep(3)
        vfour_portal_canvas_obj.select_column(1)
        time.sleep(3)
        item_path="Retail Samples->Portal->Small Widgets->Category Sales"
        vfour_portal_canvas_obj.dragdrop_repository_item_to_canvas(item_path, "column",1)
        time.sleep(10)
        vfour_portal_canvas_obj.verify_column_panel_caption(1, 'Category Sales', "Step 05(1)a: Verify first panel title")        
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Panel_1']",frame_height_value=0)
        time.sleep(8)  
        parent_css="#jschart_HOLD_0 path[class*='riser!']"
        resobj.wait_for_property(parent_css, 7)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0",7, 'Step 05(1)b: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='pieLabel!g0!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Revenue',"Step 05(1)c: Verify X-axis label")
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='totalLabel!g0!mtotalLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'1.1B',"Step 05(1)d: Verify total label")
        legend=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resobj.verify_riser_legends("jschart_HOLD_0", legend, "Step05(1)e: Verify legend Title")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mwedge!", "bar_blue1", "Step 05(1)f: Verify first bar color")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        
        vfour_portal_canvas_obj.select_column(2)
        time.sleep(3)
        item_path="Retail Samples->Portal->Small Widgets->Regional Sales Trend"
        vfour_portal_canvas_obj.dragdrop_repository_item_to_canvas(item_path, "column",2)
        time.sleep(15)
        vfour_portal_canvas_obj.verify_column_panel_caption(2, 'Regional Sales Trend', "Step 05(2)a: Verify second panel title")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Panel_2']",frame_height_value=0)
        time.sleep(8)
        parent_css="#jschart_HOLD_0 path[class*='riser!']"
        resobj.wait_for_property(parent_css, 4)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 4, 'Step 05(2)b: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        legend=['EMEA', 'North America', 'Oceania', 'South America']
        resobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 05(2)c: Verify legend Title")
        resobj.verify_xaxis_title("jschart_HOLD_0", "Month", "Step 05(2)d: Verify -xAxis Title")
        resobj.verify_yaxis_title("jschart_HOLD_0", "Revenue", "Step 05(2)e: Verify -yAxis Title")
        time.sleep(2)
        expected_xval_list=['1','2','3','4','5','6','7','8','9','10','11','12']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M']
        resobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step 05(2)f: Verify XY labels")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mline!", "bar_blue1", "Step 05(2)g: Verify first bar color", attribute_type='stroke')
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        
        vfour_portal_canvas_obj.select_column(3)
        time.sleep(3)
        item_path="Retail Samples->Portal->Large Widgets->Store Sales by Region"
        vfour_portal_canvas_obj.dragdrop_repository_item_to_canvas(item_path, "column",3)
        time.sleep(15)
        vfour_portal_canvas_obj.verify_column_panel_caption(3, 'Store Sales by Region', "Step 05(3)a: Verify third panel title")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Panel_3']",frame_height_value=0)
        time.sleep(8)
        parent_css="#jschart_HOLD_0 circle[class*='riser!']"
        resobj.wait_for_property(parent_css, 86)
        time.sleep(3)
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mmarker!", "bar_blue1", "Step 05(3)b(1): Verify first segment in the Map color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g4!mmarker!", "bar_green", "Step 05(3)b(2): Verify second segment in the Map color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g0!mmarker!", "pale_yellow_2", "Step 05(3)b(3): Verify third segment in the Map color")
        #legend=['EMEA', 'North America', 'Oceania', 'South America']
        legend=['Store Business Region', 'EMEA', 'North America', 'Oceania', 'South America', 'Revenue', '327.8M', '164M']
        resobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 05(3)c: Verify legend Title")
        time.sleep(8)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        
        vfour_portal_canvas_obj.select_column(4)
        item_path="Retail Samples->Portal->Small Widgets->Revenue Region Bar"
        vfour_portal_canvas_obj.dragdrop_repository_item_to_canvas(item_path, "column",4)
        time.sleep(20)
        vfour_portal_canvas_obj.verify_column_panel_caption(4, 'Revenue Region Bar', "Step 05(4)a: Verify fourth panel title")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Panel_4']",frame_height_value=0)
        time.sleep(8)
        parent_css="#jschart_HOLD_0 rect[class*='riser!']"
        resobj.wait_for_property(parent_css, 28)
        time.sleep(3)
        expected_xval_list=['EMEA', 'North America', 'Oceania', 'South America']
        expected_yval_list=['0%', '40%', '80%', '120%']
        resobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 05(4)b: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 05(4)c(1): Verify first segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g1!mbar!", "bar_green", "Step 05(4)c(2): Verify second segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g1!mbar!", "med_green", "Step 05(4)c(3): Verify third segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g2!mbar!", "pale_yellow_2", "Step 05(4)c(4): Verify fourth segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s4!g2!mbar!", "brick_red", "Step 05(4)c(5): Verify fifth segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s5!g3!mbar!", "light_brick", "Step 05(4)c(6): Verify sixth segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s6!g3!mbar!", "periwinkle_gray", "Step 05(4)c(7): Verify seventh segment in the bar color")
        xaxis_value="Store Business Region"
        yaxis_value="Revenue"
        legend=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        #legend=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 05(4)d: Verify legend Title")
        resobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 05(4)e: Verify X-Axis Title")
        resobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 05(4)f: Verify Y-Axis Title")
        #legend_css="#jschart_HOLD_0 .legend text"
        time.sleep(8)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        
        """    6. Open the Resources folder and try to drag a page onto the page canvas...Verify that you get the no drop icon    """
        ''' Step done by manual team '''
        
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
        vfour_ribbon_obj.bip_save_and_exit('Yes')
        time.sleep(2)
        
        """    10. Sign Out from WebFOCUS and close the browser    """
        utillobj.switch_to_window(0)
        time.sleep(3)
        
if __name__ == "__main__":
    unittest.main()