'''
Created on Dec 21, 2017

@author: Praveen

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229113
Test case Name =  Create a Map with Advanced Filter, Dynamic Parameter prompt
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon, wf_map,ia_run
from common.lib import utillity, core_utility
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import report

class C2229113_TestClass(BaseTestCase):

    def test_C2229113(self):
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        report_obj = report.Report(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C2229113"
        
        '''    1.Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=jsonmaps/africa.mas   '''
         
        utillobj.infoassist_api_login('chart','jsonmaps/africa','P292/S10032_leaflet_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
           
        '''    2. Add fields REGION_NAME, RANDOM_NUMBER    '''
        metaobj.datatree_field_click('COUNTRY_NAME', 2, 1)
        parent_css = "#queryTreeColumn"
        utillobj.synchronize_with_visble_text(parent_css, 'COUNTRY_NAME', 20)
        metaobj.datatree_field_click('RANDOM_NUMBER', 2, 1)
        utillobj.synchronize_with_visble_text(parent_css, 'RANDOM_NUMBER', 20)
           
        '''    3. Select Format tab    '''
        '''    4. Select "Other" > "Map" > "Leaflet Choropleth"  '''
        '''    5. Select Territory "Africa"    '''
                   
        ribbonobj.select_ribbon_item("Format", "Other")
        ia_ribbonobj.select_other_chart_type('map', 'leaflet_choropleth', 1)
        utillobj.synchronize_with_visble_text('#RightPane_Map', 'Territory', 20)
        combo_btn_obj=self.driver.find_element_by_css_selector("div[id^='SelectChartTypeDlg'] div[id^='RightPane'] div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn_obj, 'Africa')
        ok_btn_css="div[id='qbSelectChartTypeDlgOkBtn']"
        utillobj.synchronize_with_visble_text(ok_btn_css, 'OK', 20)
        self.driver.find_element_by_css_selector(ok_btn_css).click()
        time.sleep(3)
          
        '''   6. Select "Country_name" from Geographic Role > OK   '''
        wfmapobj.set_location_geo_role(role_name='country_name (Algeria, Angola, Benin)', btn_click='Ok')
          
        '''    7. Select Data tab
                8.Click "Filter"
                9.Double click the red text
                10.Select "COUNTRY_NAME" > OK
        '''
          
        ribbonobj.select_ribbon_item("Data", "filter")
        obj_locator=driver.find_element_by_css_selector("#dlgWhereWhereTree > div.bi-tree-view-body-content tbody > tr:nth-child(2) > td > span > span")
        utillobj.click_on_screen(obj_locator, 'middle', click_type=2)
        time.sleep(3)
        field_elem=self.driver.find_element_by_css_selector("#dlgWhere #dlgWhereWhereTree table tr:nth-child(2) span[class='selected lead']>span>span")
        utillobj.click_on_screen(field_elem, 'left', click_type=0,pause=1)
        time.sleep(3)      
        report_obj.select_field_in_filter_tree("Dimensions->COUNTRY_NAME", 1)
        ok_filter_button = utillobj.validate_and_get_webdriver_object('#wndWhereFieldPopup_btnOK', 'ok button')
        core_utils.left_click(ok_filter_button)
        
        """
        11.Click "<Value>"
        12.Select "Parameter" from Type dropdown
        13.Click Dynamic radio button
        14.Check off 'Select multiple values at runtime'
        15.Click "COUNTRY_NAME"
        16.Click OK > OK
          
        """
        value_ele = self.driver.find_element_by_css_selector("#dlgWhere #dlgWhereWhereTree div[id^='InlineControlValue']")
        core_utils.left_click(value_ele)
        report_obj.select_filter_type("Parameter")
        report_obj.select_filter_parameter_type("Dynamic")
        report_obj.select_filter_parameter_checkbox(ParamMultiple= True)
        report_obj.select_field_in_filter_tree("Dimensions->COUNTRY_NAME", 1)
        report_obj.close_filter_where_value_popup_dialog()
        report_obj.close_filter_dialog()
        parentcss="pfjTableChart_1"
        iaresult.verify_color_scale_esri_maps(parentcss, ['RANDOM_NUMBER', '10', '247', '484', '721', '958'], "Step 16.00:verify scale color")
          
        """
        17.Click "Save" icon
        18.Save fex as "C2229113"
        19.Logout:http://machine:port/alias/service/wf_security_logout.jsp
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        20.Reopen fex using IA API:http://machine:port/alias/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2229113.fex&tool=chart
        21.verify the map and filter are restored
        22.Click "Run"
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart','P292/S10032_leaflet_1', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element("#pfjTableChart_1 path[class='riser!s0!g12!mstate!']", 1, 30)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        utillobj.switch_to_frame()
 
        """
        23.Multi-select values "Angola", "Benin" in the Autoprompt form > "Run"
        24.Verify output with Angola, Benin countries only
        25.Logout:http://machine:port/alias/service/wf_security_logout.jsp
        """
        iarun.select_amper_value('COUNTRY_NAME',['Angola','Benin'], Search=True, verify_default_radio_button = False)
        iarun.select_amper_menu('Run')
        frame_height=self.driver.find_element_by_css_selector("#mainPage #header").size['height']
        utillobj.switch_to_frame(1,frame_css="[class^='autop-wf-output']",frame_height_value=frame_height)
        iaresult.verify_color_scale_esri_maps("jschart_HOLD_0",['RANDOM_NUMBER', '748', '782.3', '816.5', '850.8', '885'], "Step 24.01")
        utillobj.verify_chart_color('jschart_HOLD_0', 'riser!s0!g1!mstate!', 'persian_red', 'Step 24.02: Verify the color of Benin')
        utillobj.verify_chart_color('jschart_HOLD_0', 'riser!s0!g0!mstate!', 'elf_green', 'Step 24.03: Verify the color of Angola')
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()