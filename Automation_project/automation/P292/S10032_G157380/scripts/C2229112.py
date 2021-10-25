'''
Created on DEC 18, 2017

@author: Sowmiya 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157431
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229112
TestCase Name = Convert Map Chart to Report
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon,wf_map
from common.lib.basetestcase import BaseTestCase
class C2229112_TestClass(BaseTestCase):

    def test_C2229112(self):
        
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj= ia_resultarea.IA_Resultarea(self.driver)      
        wfmapobj=wf_map.Wf_Map(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        Test_Case_ID='C2229112'
        """        
            Step 01:Launch Report Mode:
                    http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail','P292/S10660_chart_1', 'mrid', 'mrpass')
        parent_css=driver.find_element_by_css_selector('#TableChart_1')
        resobj.wait_for_property(parent_css,1,expire_time=10)
        """        
            Step 02 : Add fields car, sales
        """
        metaobj.datatree_field_click("Store,Country", 2, 1)
        time.sleep(2)
        parent_css="#queryTreeWindow tr:nth-child(4) td"
        resobj.wait_for_property(parent_css, 1, expire_time=50)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(2)
        parent_css="#queryTreeWindow tr:nth-child(3) td"
        resobj.wait_for_property(parent_css, 1, expire_time=50)
        """        
            Step 03 : Select Format tab -> "Other" > "Map" > "Leaflet Choropleth" -> "World" as Territory > OK -> "country_name" as Geographic Role > OK
        """
        ribbonobj.select_ribbon_item("Format", "Other")
        ia_ribbonobj.select_other_chart_type('map', 'leaflet_choropleth', 1)
        time.sleep(3)
        combo_btn_obj=self.driver.find_element_by_css_selector("div[id^='SelectChartTypeDlg'] div[id^='RightPane'] div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn_obj, 'World')
        time.sleep(3)
        ok_btn_css="div[id='qbSelectChartTypeDlgOkBtn']"
        self.driver.find_element_by_css_selector(ok_btn_css).click()
        time.sleep(10)
        wfmapobj.set_location_geo_role(role_name='country_name (Afghanistan, Aland Islands, Albania)', btn_click='Ok')
        """        
            Step 04 : Verify the map is displayed in Live Preview
        """
        parent_css="#pfjTableChart_1 path[class^='riser!s0!g3!mstate!']"
        resobj.wait_for_property(parent_css,1,expire_time=10)
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s0!g3!mstate!', color='sorbus_2', msg='Step 04:')
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s0!g33!mstate!', color='elf_green', msg='Step 04:')
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s0!g2!mstate!', color='Vermilion', msg='Step 04:')
        ia_resultobj.verify_color_scale_esri_maps("pfjTableChart_1", ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M',], msg='Step 04:')
        """        
            Step 05 : Click "Report" under Home tab to convert Map Chart to Report -> Verify Report is displayed on canvas
        """
        ribbonobj.select_ribbon_item("Home", "report")
        time.sleep(3)
        #ia_resultobj.create_report_data_set('TableChart_1', 34, 2, Test_Case_ID+"_Ds01.xlsx", msg='Step 05:')
        ia_resultobj.verify_report_data_set('TableChart_1', 34, 2, Test_Case_ID+"_Ds01.xlsx", msg='Step 05:',no_of_cells=2)
        
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        """        
            Step 06 : Click "Save" icon
              Save Report fex as "C2229112"
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """        
            Step 07 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout() 
        
        """  Step 08 : Reopen saved FEX:    
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227571.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3',mrid='mrid', mrpass='mrpass')
        
   
if __name__ == '__main__':
    unittest.main()        
        