'''
Created on Nov 19, 2017

@author: BM13368
Testcase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2227503
Testcase_Name : Verify InfoMini request with Document mode

'''
import unittest,time, re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon
from common.lib import utillity, core_utility


class C2227503_TestClass(BaseTestCase):

    def test_C2227503(self):
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2227503'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_ribbon_obj = ia_ribbon.IA_Ribbon(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
            Step 01 : Launch IA Document mode:
            http://machine:port/ibi_apps/ia?tool=Document&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('document','ibisamp/car','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        canvas_container_css="#canvasContainer"
        utillobj.synchronize_until_element_is_visible(canvas_container_css, metaobj.chart_long_timesleep)
        
        """
            Step 02 : Double click "COUNTRY", "CAR", "SALES".
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        utillobj.synchronize_with_visble_text(canvas_container_css, 'COUNTRY', metaobj.chart_long_timesleep)
        metaobj.datatree_field_click("CAR", 2, 1)
        utillobj.synchronize_with_visble_text(canvas_container_css, 'CAR', metaobj.chart_long_timesleep)
        metaobj.datatree_field_click("SALES", 2, 1)
        utillobj.synchronize_with_visble_text(canvas_container_css, 'SALES', metaobj.chart_long_timesleep)
        
        """
            Step 03 : Select "Home" > "Active Report" dropdown > "PDF"
        """
        ia_ribbon_obj.select_or_verify_output_type(launch_point='Home', item_select_path='PDF')
        time.sleep(1)
        
        """
            Step 04 : Select "Format" > "InfoMini" (dropdown) > "Insert Tab", "Resources/Field Tab".
        """
        vis_ribbon_obj.select_ribbon_item("Format", "Infomini_arrow")
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("Insert Tab")
        time.sleep(2)
        vis_ribbon_obj.select_ribbon_item("Format", "Infomini_arrow")
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("Resources/Field Tab")
        time.sleep(2)
        
        """
            Step 05 : Click "Run".
        """
        browser=utillobj.parseinitfile('browser')
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        core_util_obj.switch_to_new_window()
        
        """
            Verify report in document mode
        """
        utillobj.synchronize_until_element_is_visible("#resultArea", metaobj.chart_long_timesleep)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step05'+'_'+browser, image_type='actual')  
        time.sleep(3)
        
        """
            Step 06 : Click "Edit" button in the InfoMini application    
        """
        vis_ribbon_obj.select_top_toolbar_item('infomini_edit')
        parent_css="#IaToolbar"
        utillobj.synchronize_until_element_is_visible(parent_css, metaobj.chart_long_timesleep)
        
        """
            Step 07 : Verify "Insert" tab is displayed and InfoMini entered into "Edit Mode" (Data, Filter and Query pane).
        """
        css_obj=self.driver.find_element_by_css_selector("#IaToolbar  #InsertTab_tabButton")
        status=css_obj.is_displayed()
        utillobj.asequal(status, True, 'Step 07:01: Verify Insert tab is displayed')
        
        """ Verify data-pane
        """
        css_datapane=self.driver.find_element_by_css_selector("#iaMetaDataBrowser")
        status=css_datapane.is_displayed()
        utillobj.asequal(status, True, 'Step 07:02: Verify Datapane is displayed')
        """
            Verify query-pane
        """
        css_datapane=self.driver.find_element_by_css_selector("#queryTreeWindow")
        status=css_datapane.is_displayed()
        utillobj.asequal(status, True, 'Step 07:03: Verify Query-pane is displayed')
        """
            Verify Filter-pane
        """
        css_datapane=self.driver.find_element_by_css_selector("#qbFilterWindow")
        status=css_datapane.is_displayed()
        utillobj.asequal(status, True, 'Step 07:04: Verify Filter-pane is displayed')
        """
            Verify report data
        """
        coln_list = ['COUNTRY', 'CAR', 'SALES']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 07:04: Verify Canvas column titles")
#         ia_resultarea_obj.create_report_data_set('TableChart_1', 10, 3, 'C2227503_Ds01.xlsx', desired_no_of_rows=5)
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 10, 3, "C2227503_Ds01.xlsx", 'Step 07:05: Verify report dataset')
       
        """
            Step 08 : Dismiss Infomini application
        """
        core_util_obj.switch_to_previous_window()
        
        """
            Step 09 : Click "IA" > Save > Enter Title= "C2227503" > Click Save
        """
        utillobj.synchronize_until_element_is_visible(canvas_container_css, metaobj.chart_long_timesleep)
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        """
            Step 10 : Logout, http://machine:port/ibi_apps/service/wf_security_logout.jsp  

        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """
            Step 11 : Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227503.fex&tool=Document
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_4',mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_visble_text(parent_css, 'COUNTRY', metaobj.chart_long_timesleep)
        
        """
            Step 12 : Verify Report on "Canvas".
        """
        coln_list = ['COUNTRY', 'CAR', 'SALES']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 12:01: Verify Canvas column titles")
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 10, 3, "C2227503_Ds01.xlsx", 'Step 12:02: Verify report dataset')
        
        """
            Step 13 : Select Format > Verify "Infomini" button is selected
        """
        vis_ribbon_obj.switch_ia_tab("Format")
        utillobj.synchronize_until_element_is_visible("#FormatApplicationRibbonEnable", metaobj.home_page_long_timesleep)
        infomini_css=self.driver.find_element_by_css_selector("#FormatApplicationRibbonEnable")
        status=True if bool(re.match('.*menu-button-checked.*', infomini_css.get_attribute("class"))) else False
        utillobj.asequal(True, status, "Step 13:01: Verify infomini is selected.")
        """
            Step 14 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()