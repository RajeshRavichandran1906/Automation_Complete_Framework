'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229076
Test case Name =  Verify converting Chart to Map
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229076_TestClass(BaseTestCase):

    def test_C2229076(self):
    
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2229076"
#         Test_Case_ID = "a"+browser_type
        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','places/noplaces_xy','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
        
        """    2. Double click "Country", "Population"    """
        metaobj.datatree_field_click('COUNTRY', 2,1)
        metaobj.datatree_field_click('POPULATION', 2,1)
        
        xaxis_value="COUNTRY"
        yaxis_value="POPULATION"
        parentcss="pfjTableChart_1"
        resultobj.verify_xaxis_title(parentcss, xaxis_value, "Step 02:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title(parentcss, yaxis_value, "Step 02:a(ii) Verify Y-Axis Title")
        expected_xval_list_cr=['"Bahamas, The"', '"Gambia, The"', '"Korea, North"']
        expected_xval_list_ff=['"Bahamas, The"', '"Gambia, The"', '"Korea, North"', '"Korea, South"', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M']
        resultobj.verify_data_labels("pfjTableChart_1", expected_xval_list_cr, "Step 02:c(iii):Verify X labels", data_label_length=3,custom_css="svg > g text[class^='xaxis'][class*='labels']")
        resultobj.verify_data_labels("pfjTableChart_1", expected_yval_list, "Step 02:d(iii):Verify Y labels", custom_css="svg > g text[class^='yaxis'][class*='labels']")
#         if browser_type=="Chrome":
#             resultobj.verify_riser_chart_XY_labels(parentcss, expected_xval_list_cr, expected_yval_list, "Step 02:c(iii):Verify XY labels")
#         else:
#             resultobj.verify_riser_chart_XY_labels(parentcss, expected_xval_list_ff, expected_yval_list, "Step 02:c(iii):Verify XY labels")
        resultobj.verify_number_of_riser(parentcss, 1, 27, 'Step 02.d: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mbar", "bar_blue", "Step 02.e: Verify first bar color")
        time.sleep(5)          
          
        """    3. Go to Format tab    """
        """    4. Click "Choropleth" in Chart Types group    """
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        defcss="#pfjTableChart_1"
        utillobj.synchronize_with_number_of_element(defcss, 1, 90, 1)
        
        time.sleep(10)
         
        """    5. Double click "COUNTRY"    """
        """    6. Set Geographic Role = Country    """
        """    7. Set Stored As value = Name > OK    """
        metaobj.datatree_field_click('COUNTRY', 2,1)
        wfmapobj.set_geo_role(role_name='Country', store_as='Name', btn_click='Ok')
        defcss="#pfjTableChart_1 path[class^='riser!s0!g12!mregion!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(8)
        
        """    "8. Verify the map is displayed    """
        parentcss="pfjTableChart_1"
        iaresult.verify_color_scale_esri_maps(parentcss, ['POPULATION', '0M', '8.3M', '16.5M', '24.7M', '33M'], "Step 8.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g26!mregion!", 'sorbus_3', 'Step 8.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g12!mregion!", 'banana_mania1', 'Step 8.3 Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step08'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)

        
        
        """    9. Click "Save" icon    """
        """    10. Enter Title "C2229076"    """
        """    11. Click "Save" and close IA window.    """
        #utillobj.switch_to_default_content(pause=3)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
               
        """    12. Reopen the saved fex.    """
        """    13. Verify IA is launched, preserving the map    """
        """    14. Dismiss IA window    """
        """    15. Log out :    """
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        
        defcss="#pfjTableChart_1 path[class^='riser!s0!g12!mregion!']"
        utillobj.synchronize_with_number_of_element(defcss, 1, 120, 1)
        
        
        parentcss="pfjTableChart_1"
        iaresult.verify_color_scale_esri_maps(parentcss, ['POPULATION', '0M', '8.3M', '16.5M', '24.7M', '33M'], "Step 13.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g26!mregion!", 'sorbus_3', 'Step 13.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g12!mregion!", 'banana_mania1', 'Step 13.3 Verify map color')
        


        
if __name__ == '__main__':
    unittest.main()
    
        
