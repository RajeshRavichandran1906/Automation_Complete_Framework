'''
Created on DEC 18, 2017

@author: Sowmiya 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157431
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229112
TestCase Name = Convert Map Chart to Report
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon,wf_map
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart

class C2229112_TestClass(BaseTestCase):

    def test_C2229112(self):
        
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj= ia_resultarea.IA_Resultarea(self.driver)      
        wfmapobj=wf_map.Wf_Map(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        chart = Chart(self.driver)
        Test_Case_ID='C2229112'
        
        """        
            Step 01:Launch Report Mode:
                    http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10032_leaflet_1', 'mrid', 'mrpass')
        chart.wait_for_visible_text("#pfjTableChart_1", "Group 0")
        
        """        
            Step 02. Add fields "Store,Country", "Revenue"
        """
        chart.double_click_on_datetree_item("Store,Country", 1)
        chart.wait_for_visible_text("#queryTreeWindow", "Store,Country")
        
        chart.double_click_on_datetree_item("Revenue", 1)
        chart.wait_for_visible_text("#queryTreeWindow", "Revenue")
        
        """        
            Step 03. Select Format tab
            Step 04. Select "Other" > "Map" > "Leaflet Choropleth"
            Step 05. Select "World" as Territory > OK
            Step 06. Select "country_name" as Geographic Role > OK
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
            
            Step 07. Verify the map is displayed in Live Preview

        """
        parent_css="#pfjTableChart_1 path[class^='riser!s0!g3!mstate!']"
        resobj.wait_for_property(parent_css,1,expire_time=10)
        time.sleep(5) #giving time for unexpected load
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s0!g3!mstate!', color='sorbus_2', msg='Step 04:')
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s0!g33!mstate!', color='elf_green', msg='Step 04:')
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s0!g2!mstate!', color='Vermilion', msg='Step 04:')
        ia_resultobj.verify_color_scale_esri_maps("pfjTableChart_1", ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M',], msg='Step 04:')
        """        
            Step 08. Click "Report" under Home tab to convert Map Chart to Report
            Step 09. Verify Report is displayed on canvas
        """
        ribbonobj.select_ribbon_item("Home", "report")
        time.sleep(3)
        #ia_resultobj.create_report_data_set('TableChart_1', 34, 2, Test_Case_ID+"_Ds01.xlsx", msg='Step 05:')
        ia_resultobj.verify_report_data_set('TableChart_1', 34, 2, Test_Case_ID+"_Ds01.xlsx", msg='Step 05:',no_of_cells=2)
        
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        """        
            Step 10. Click "Save" icon
            Step 11. Save Report fex as "C2229112"
            Step 12. Logout:
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        chart.wait_for_visible_text("#IbfsOpenFileDialog7_btnOK", "Save")
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.synchronize_until_element_disappear("#IbfsOpenFileDialog7_btnOK", chart.home_page_medium_timesleep)
        
        """        
            Step 12. Logout:
        """
        chart.api_logout()
        time.sleep(10)
        
        """
              Step 13. Ropen fex using IA API:
              Step 14. Verify Report fex can be reopened in IA
              Step 15. logout:
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_leaflet_1',mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1", 1, 120, 1)
        
        ia_resultobj.verify_report_data_set('TableChart_1', 34, 2, Test_Case_ID+"_Ds01.xlsx", msg='Step 05:')
        
   
if __name__ == '__main__':
    unittest.main()        
        