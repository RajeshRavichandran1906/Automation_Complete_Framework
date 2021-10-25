'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229111
Test case Name =  Create a Map with Theme and Header & Footer
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon, wf_map, ia_styling
from common.lib import utillity 
import time,datetime
from common.lib.basetestcase import BaseTestCase



class C2229111_TestClass(BaseTestCase):

    def test_C2229111(self):
        
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C2229111"
        
        '''
        css variables
        '''
        signin_css = "#SignonbtnLogin"
        map_css = "#pfjTableChart_1 > div > div > div.leaflet-map-pane > div.leaflet-objects-pane > div.leaflet-overlay-pane > svg"
        
        '''    1. Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=jsonmaps/south_america    '''
        utillobj.infoassist_api_login('chart','jsonmaps/jp','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
         
        '''    2. Add fields REGION_NAME, RANDOM_NUMBER    '''
        metaobj.datatree_field_click('REGION_NAME', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RANDOM_NUMBER', 2, 1)
        time.sleep(4)
         
         
         
        '''    3. Select Format tab    '''
        '''    4. Click "Other" > "Map"  '''
        '''    5. Select "Leaflet Choropleth"    '''
        '''    6. Select 'Japan' Territory > OK    '''
         
        ribbonobj.select_ribbon_item("Format", "Other")
         
        time.sleep(4)
        ia_ribbonobj.select_other_chart_type('map', 'leaflet_choropleth', 1)
         
        time.sleep(3)
        combo_btn_obj=self.driver.find_element_by_css_selector("div[id^='SelectChartTypeDlg'] div[id^='RightPane'] div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn_obj, 'Japan')
        time.sleep(3)
        ok_btn_css="div[id='qbSelectChartTypeDlgOkBtn']"
        self.driver.find_element_by_css_selector(ok_btn_css).click()
        time.sleep(3)
         
        '''   7. Select "region_name" as Geographic Role > OK    '''
        wfmapobj.set_location_geo_role(role_name='region_name (Aichi, Akita, Aomori)', btn_click='Ok')
         
        '''    '8. Select Home tab    '''
        '''    9. Click "Theme"    '''
        '''    10. Select Legacy Templates > theme "ENGreen_DarkComp.sty" > "Open"    '''
        '''    11. Verify the theme is in effect    '''
        
        ribbonobj.switch_ia_tab('Home')
        
        time.sleep(5)
        ribbonobj.select_theme('Legacy Templates', 'ENGreen_DarkComp.sty')
        
        parentcss="pfjTableChart_1"
        
        resultobj.wait_for_property("#pfjTableChart_1 path[class^='riser!s0!g11!mstate!']", 1, expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['RANDOM_NUMBER', '11', '256.5', '502', '747.5', '993'], "Step 11.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g11!mstate!", 'cream', 'Step 11.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mstate!", 'fountain_blue', 'Step 11.2 Verify map color')
        
        
        bkele=self.driver.find_element_by_css_selector("#pfjTableChart_1 rect[class='background']")
        bkcolor=bkele.get_attribute("fill").strip().replace(' ','')
        
        excolor="rgb(118,147,60)"
        
        utillobj.asequal(bkcolor,excolor,'Step 11.3 Verify theme is in effect')
        
        
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step09'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        '''    12. Click "Header & Footer" in the Home tab    '''
        '''    13. Type "Map with Theme" for the Page Header    '''
        
        
        ia_stylingobj.create_header_footer('ribbon', 'Page Header', 'Map with Theme')
        
        '''    14. Select "Page Footer"    '''
        '''    15. Click the "preformatted text" dropdown > "Date" > first option    '''
                
        ia_stylingobj.create_header_footer('frame','Page Footer','')
        time.sleep(2)
        option=driver.find_element_by_css_selector("#QuickText div[class^='bi-component tool-bar-menu-button-drop-down-arrow']")
        utillobj.click_on_screen(option, 'middle')
        utillobj.click_on_screen(option, 'middle', click_type=0)
        time.sleep(1)
        currentDT = datetime.datetime.now()
        current_date1 = currentDT.strftime("%B %d,%Y")
        print (current_date1)
        utillobj.select_or_verify_bipop_menu('Date')
        utillobj.select_or_verify_bipop_menu(current_date1)
        
        '''    16. Click the "text options" dropdown > "Embed Header and Footer in the chart"    '''
        '''    17. Click OK    '''

        
        quicktext=self.driver.find_element_by_css_selector('#EmbedInChart')
        
        utillobj.default_left_click(object_locator=quicktext)
        
        utillobj.select_or_verify_bipop_menu('Embed Header and Footer in the chart')
        
        self.driver.find_element_by_id("okBtn").click()
        time.sleep(1)
        
        '''    18. Verify Preview    '''
        
        head_foot=self.driver.find_elements_by_css_selector('#pfjTableChart_1 span[style]')
        d = datetime.date.today()
        month1=d.strftime("%B")
        day1='%02d' % d.day
        year1=d.year
        
        footer_txt=str(month1) + " " + str(day1) +"," + str(year1)
        
        utillobj.asequal(head_foot[0].text.strip(),"Map with Theme", 'Step 18.1 Verify Header displayed in the map')
        utillobj.asequal(head_foot[1].text.strip().replace(" ",""),footer_txt.replace(" ",""), 'Step 18.2 Verify Footer displayed in the map')

        '''  19. Click "Save" icon   '''
        '''  20. Save fex as "C2229111"  '''
        '''  21. Logout: '''

        
        utillobj.switch_to_window(0, pause=3)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
         
        
        '''    22. Reopen fex using IA API:    '''
        '''    23. Verify the map is restored    '''
         
         
        utillobj.infoassist_api_logout()
        utillobj.synchronize_until_element_is_visible(signin_css, metaobj.home_page_medium_timesleep)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_until_element_is_visible(map_css, metaobj.home_page_medium_timesleep)
        
        parentcss="pfjTableChart_1"
        
        resultobj.wait_for_property("#pfjTableChart_1 path[class^='riser!s0!g11!mstate!']", 1, expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['RANDOM_NUMBER', '11', '256.5', '502', '747.5', '993'], "Step 23.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g11!mstate!", 'cream', 'Step 23.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mstate!", 'fountain_blue', 'Step 23.2 Verify map color')
        
        bkele=self.driver.find_element_by_css_selector("#pfjTableChart_1 rect[class='background']")
        bkcolor=bkele.get_attribute("fill").strip().replace(' ','')
        
        excolor="rgb(118,147,60)"
        
        utillobj.asequal(bkcolor,excolor,'Step 23.3 Verify theme is in effect')
        head_foot=self.driver.find_elements_by_css_selector('#pfjTableChart_1 span[style]')
        d = datetime.date.today()
        month1=d.strftime("%B")
        day1='%02d' % d.day
        year1=d.year
        
        footer_txt=str(month1) + " " + str(day1) +"," + str(year1)
        utillobj.asequal(head_foot[0].text.strip(),"Map with Theme", 'Step 23.4 Verify Header displayed in the map')
        utillobj.asequal(head_foot[1].text.strip().replace(' ',''),footer_txt.replace(" ",""), 'Step 23.5 Verify Footer displayed in the map')
        
        
        '''    24. Click Run    '''
        '''    25. Verify output displays a chart for each country    '''
        '''    26. Logout: '''
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        resultobj.wait_for_property("#jschart_HOLD_0 path[class^='riser!s0!g11!mstate!']", 1,expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['RANDOM_NUMBER', '11', '256.5', '502', '747.5', '993'], "Step 25.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g11!mstate!", 'cream', 'Step 25.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mstate!", 'fountain_blue', 'Step 25.2 Verify map color')
        
        bkele=self.driver.find_element_by_css_selector("#jschart_HOLD_0 rect[class='background']")
        bkcolor=bkele.get_attribute("fill").strip().replace(' ','')
        
        excolor="rgb(118,147,60)"
        
        utillobj.asequal(bkcolor,excolor,'Step 25.3 Verify theme is in effect')
        
        head_foot=self.driver.find_elements_by_css_selector('#jschart_HOLD_0 span[style]')
        d = datetime.date.today()
        month1=d.strftime("%B")
        day1='%02d' % d.day
        year1=d.year
        
        footer_txt=str(month1) + " " + str(day1) +"," + str(year1)
        utillobj.asequal(head_foot[0].text.strip(),"Map with Theme", 'Step 25.4 Verify Header displayed in the map')
        utillobj.asequal(head_foot[1].text.strip().replace(' ',''),footer_txt.replace(" ",""), 'Step 25.5 Verify Footer displayed in the map')
        utillobj.infoassist_api_logout()


if __name__ == '__main__':
    unittest.main()
    