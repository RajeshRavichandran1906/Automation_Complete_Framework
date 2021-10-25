'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229084
Test case Name =  Verify converting between map types
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229084_TestClass(BaseTestCase):

    def test_C2229084(self):
    
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        driver.implicitly_wait(15)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2229084"
#         Test_Case_ID = "a"+browser_type
        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
        
        """    2. Double click "Store,Country", "Revenue"    """
        metaobj.datatree_field_click('Store,Country', 2,1)
        metaobj.datatree_field_click('Revenue', 2,1)
        
        xaxis_value="Store Country"
        yaxis_value="Revenue"
        parentcss="pfjTableChart_1"
        resultobj.verify_xaxis_title(parentcss, xaxis_value, "Step 02:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title(parentcss, yaxis_value, "Step 02:a(ii) Verify Y-Axis Title")
        expected_xval_list_cr=['Australia', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Czech Republic', 'Denmark', 'Egypt', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Mexico', 'Netherlands', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Singapore', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'United Kingdom', 'United States']
        expected_xval_list_ff=['Australia', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Czech Republic', 'Denmark', 'Egypt', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Mexico', 'Netherlands', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Singapore', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'United Kingdom', 'United States']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        if browser_type=="Chrome":
            resultobj.verify_riser_chart_XY_labels(parentcss, expected_xval_list_cr, expected_yval_list, "Step 02:c(iii):Verify XY labels")
        else:
            resultobj.verify_riser_chart_XY_labels(parentcss, expected_xval_list_ff, expected_yval_list, "Step 02:c(iii):Verify XY labels")
        resultobj.verify_number_of_riser(parentcss, 1, 34, 'Step 02.d: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color(parentcss, "riser!s0!g0!mbar", "bar_blue", "Step 02.e: Verify first bar color")
        time.sleep(5)          
          
        """    3. Go to Format tab    """
        """    4. Click "Choropleth" in Chart Types group    """
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        defcss="#pfjTableChart_1 path[class^='riser!s0!g33!mregion!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(5)
        
                
        """    5. Verify the map is updated    """
        parentcss="pfjTableChart_1"
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 5.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mregion!", 'sorbus_2', 'Step 5.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mregion!", 'elf_green', 'Step 5.3 Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step05'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        
        """    6. Click "Proportional Symbol" in Chart Types group    """
        """    7. Verify the map is converted to bubble map    """

        ribbonobj.select_ribbon_item("Format", "proportional_symbol")
        defcss="#pfjTableChart_1 circle[class^='riser!s0!g33!mmarker!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        
        parentcss="pfjTableChart_1"
        expected_label_list=['Revenue']
        msg="Step 7.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 7.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        utillobj.verify_chart_color(parentcss, "riser!s0!g28!mmarker!", 'bar_blue', 'Step 7.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 7.3b Verify map color')
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step07'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
       
        
        """    8. Click "Save" icon    """
        """    9. Save fex as "C2229084" and dismiss IA    """
        #utillobj.switch_to_default_content(pause=3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
               
        """    10. Reopen the fex using API code:    """
        """    11. Verify the map is restored    """
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        
        defcss="#pfjTableChart_1 circle[class^='riser!s0!g33!mmarker!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        
        parentcss="pfjTableChart_1"
        expected_label_list=['Revenue']
        msg="Step 11.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 11.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        utillobj.verify_chart_color(parentcss, "riser!s0!g28!mmarker!", 'bar_blue', 'Step 11.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 11.3b Verify map color')
        
        """    12. Go to Format tab    """
        """    13. Click "Choropleth"    """
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        defcss="#pfjTableChart_1 path[class^='riser!s0!g33!mregion!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(5)
        
        
        """    14. Verify the map is converted to Choropleth map    """
        """    15. Dismiss IA (Do not save changes)    """
        parentcss="pfjTableChart_1"
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 14.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mregion!", 'sorbus_2', 'Step 14.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mregion!", 'elf_green', 'Step 14.3 Verify map color')



        
if __name__ == '__main__':
    unittest.main()
    
        
