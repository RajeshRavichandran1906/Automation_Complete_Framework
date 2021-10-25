'''
Created on Dec 21, 2017

@author: Praveen

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229113
Test case Name =  Create a Map with Advanced Filter, Dynamic Parameter prompt
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon, wf_map,wf_reporting_object,ia_run
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



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
        wfreportobj = wf_reporting_object.Wf_Reporting_Object(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C2229113"
        
        '''    1.Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=jsonmaps/africa.mas   '''
         
        utillobj.infoassist_api_login('chart','jsonmaps/africa','P292/S10032_leaflet_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
           
        '''    2. Add fields REGION_NAME, RANDOM_NUMBER    '''
        metaobj.datatree_field_click('COUNTRY_NAME', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RANDOM_NUMBER', 2, 1)
        time.sleep(4)
                    
           
        '''    3. Select Format tab    '''
        '''    4. Select "Other" > "Map" > "Leaflet Choropleth"  '''
        '''    5. Select Territory "Africa"    '''
                   
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(4)
        ia_ribbonobj.select_other_chart_type('map', 'leaflet_choropleth', 1)
        time.sleep(3)
        combo_btn_obj=self.driver.find_element_by_css_selector("div[id^='SelectChartTypeDlg'] div[id^='RightPane'] div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn_obj, 'Africa')
        time.sleep(3)
        ok_btn_css="div[id='qbSelectChartTypeDlgOkBtn']"
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
        wfreportobj.ro_where_filter_field_click("COUNTRY_NAME", 1)
        
        """
        11.Click "<Value>"
        12.Select "Parameter" from Type dropdown
        13.Click Dynamic radio button
        14.Check off 'Select multiple values at runtime'
        15.Click "COUNTRY_NAME"
        16.Click OK > OK
          
        """
        value_elem=self.driver.find_element_by_css_selector("[id*='InlineControlValue'] div[class^='bi-button button']")
        utillobj.click_on_screen(value_elem, 'right',click_type=0,pause=1)
        utillobj.select_combobox_item("id_wv_combo_type", "Parameter")
        utillobj.click_on_screen(value_elem, 'right', click_type=2,pause=1)
        ia_ribbonobj.create_parameter_filter_condition('Dynamic', ['COUNTRY_NAME'],ParamMultiple=True)
        parentcss="pfjTableChart_1"
        iaresult.verify_color_scale_esri_maps(parentcss, ['RANDOM_NUMBER', '10', '247', '484', '721', '958'], "Step 16:verify scale color")
          
          
        """
        17.Click "Save" icon
        18.Save fex as "C2229113"
        19.Logout:http://machine:port/alias/service/wf_security_logout.jsp
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
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
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        utillobj.switch_to_frame()
 
        """
        20.Multi-select values "Angola", "Benin" in the Autoprompt form > "Run"
        21.Verify output with Angola, Benin countries only
        22.Logout:http://machine:port/alias/service/wf_security_logout.jsp
        """
                
        iarun.select_amper_value('COUNTRY_NAME',['Angola','Benin'], Search=True)
        iarun.select_amper_menu('Run')
        frame_height=self.driver.find_element_by_css_selector("#mainPage #header").size['height']
        utillobj.switch_to_frame(1,frame_css="[class^='autop-wf-output']",frame_height_value=frame_height)
        iaresult.verify_color_scale_esri_maps("jschart_HOLD_0",['RANDOM_NUMBER', '748', '782.3', '816.5', '850.8', '885'], "Step 21.1:Verify color scale")
        utillobj.verify_chart_color('jschart_HOLD_0', 'riser!s0!g1!mstate!', 'persian_red', 'Step 21.2:')
        utillobj.verify_chart_color('jschart_HOLD_0', 'riser!s0!g0!mstate!', 'elf_green', 'Step 21.3:')
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()