'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229071
Test case Name =  Verify Color By in a Bubble map
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229071_TestClass(BaseTestCase):

    def test_C2229071(self):
    
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        driver.implicitly_wait(15)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2229071"
        

        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','places/noplaces_xy','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
          
          
        """    2. Go to Format tab    """
        """    3. Click "Proportional Symbol"    """
        ribbonobj.select_ribbon_item("Format", "proportional_symbol")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(9)
        #ribbonobj.switch_ia_tab('Home')
        #time.sleep(6)
        """    4. Right click "COUNTRY " > "Map As"    """
        """    5. Verify the menu is alphabetized and contains all georoles    """
        
        metaobj.datatree_field_click('COUNTRY', 1,1)
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Map As')
        
        time.sleep(1)
        expected_list=['3 Digit Zipcode', '5 Digit Zipcode', 'City (United States)...', 'City...', 'Continent', 'Country (ISO2)', 'Country (ISO3)', 'Country (Name)', 'County (United States)...', 'County...', 'Geometry (Point)', 'Latitude...', 'Longitude...', 'Postal code', 'State/Province...', 'US State (Abbreviation)', 'US State (FIPS)', 'US State (Name)']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=expected_list,msg='Step 5: Verify popup menu')
        
        
        """    "6. Select "Country (Name)"    """
        """    "7. Verify the field is updated    """
        metaobj.datatree_field_click('STATE', 1,1)
        time.sleep(3)
        
        metaobj.datatree_field_click('COUNTRY', 1, 1, 'Map As', 'Country (Name)')
                
        '''to verify the field is updated'''
        expected_list=['Segment: NOPLACES_XY','Name: COUNTRY','Alias: COUNTRY','Title: COUNTRY','Description: COUNTRY','Format: A26V','Geographic Role: COUNTRY']
        
        metaobj.verify_datatree_tooltip(field_name='COUNTRY', position=1, expected_list=expected_list,msg="Verify Tooltip", x_offset=20, y_offset=5)
        
        
        
        """    "8. Click "Undo" button    """
        """    "9. Verify the field is reverted    """
        
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        
        time.sleep(10)
        
        '''toverify the field is reverted'''
        
        expected_list=['Segment: NOPLACES_XY','Name: COUNTRY','Alias: COUNTRY','Title: COUNTRY','Description: COUNTRY','Format: A26V']
        
        metaobj.verify_datatree_tooltip(field_name='COUNTRY', position=1, expected_list=expected_list,msg="Verify Tooltip", x_offset=20, y_offset=5)
        
        """    10. Right click "COUNTRY " > "Map As" > "Country (Name)"    """
        """    11. Double click "COUNTRY", "POPULATION"    """
        metaobj.datatree_field_click('COUNTRY', 1, 1, 'Map As', 'Country (Name)')
        metaobj.datatree_field_click('COUNTRY', 2,1)
        metaobj.datatree_field_click('POPULATION', 2,1)
        
        
        """    12. Verify fields are added to query and map is updated    """
        parentcss="pfjTableChart_1"
        expected_label_list=['POPULATION']
        msg="Step 12.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['POPULATION']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 12.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        utillobj.verify_chart_color(parentcss, "riser!s0!g16!mmarker!", 'bar_blue', 'Step 12.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g10!mmarker!", 'bar_blue', 'Step 12.3b Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step12'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    13. Click "Run"    """
        """    14. Verify the map is displayed correctly    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#jschart_HOLD_0', 1)
        
        expected_label_list=['POPULATION']
        msg="Step 14.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['POPULATION']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 14.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        utillobj.verify_chart_color(parentcss, "riser!s0!g16!mmarker!", 'bar_blue', 'Step 14.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g10!mmarker!", 'bar_blue', 'Step 14.3b Verify map color')
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
       
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step14'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        """    15. Click "Save"    """
        """    16. Enter Title "C2229071"    """
        """    17. Click "Save" and dismiss IA    """
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        
        """    18. Run the saved fex.    """
        """    19. Verify the map is run in a new window and hover over a bubble.    """
        """    19.1. Verify the tooltip is displayed correctly    """
        """    20. Dismiss the chart window    """
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10032_esrimap_1', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        utillobj.switch_to_window(wndnum=0, pause=15)
        
        elem1="#jschart_HOLD_0 [class^='riser!s0!g16!mmarker!']"
        
        resultobj.wait_for_property(elem1, 1, expire_time=90)
        time.sleep(8)
        parentcss="jschart_HOLD_0"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#jschart_HOLD_0', 1)
        
        expected_label_list=['POPULATION']
        msg="Step 19.a. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['POPULATION']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 19.b. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        utillobj.verify_chart_color(parentcss, "riser!s0!g16!mmarker!", 'bar_blue', 'Step 19.c Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g10!mmarker!", 'bar_blue', 'Step 19.d Verify map color')
        
        expected_tooltip=['COUNTRY:Uzbekistan', 'POPULATION:8477259']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g183!mmarker!",expected_tooltip, "Step 19.1: Verify Tooltip is displayed correctly")       
        
        
        """    21. Reopen the fex using API code:    """
        """    22. Verify IA is launched, preserving the map    """
        """    23. Dismiss IA window    """
        """    24. Log out :    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#pfjTableChart_1', 1)
        parentcss="pfjTableChart_1"
        time.sleep(7)
        
        expected_label_list=['POPULATION']
        msg="Step 22.a. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['POPULATION']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 22.b. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        utillobj.verify_chart_color(parentcss, "riser!s0!g16!mmarker!", 'bar_blue', 'Step 22.c Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g10!mmarker!", 'bar_blue', 'Step 22.d Verify map color')


        
if __name__ == '__main__':
    unittest.main()
    
        