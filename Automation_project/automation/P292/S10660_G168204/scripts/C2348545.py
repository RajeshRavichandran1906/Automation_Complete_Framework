'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348545
Test case Name =  Verify dialog appears when a non GeoRole field is added to Geolocation bucket
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2348545_TestClass(BaseTestCase):

    def test_C2348545(self):
    
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        georoledlg="body[id=wndApp] div[id^='QbDialog']"
        georolebox="div[id^='QbDialog'] div[id$='oldGeoRoleBox']"
        geoformat="div[id^='QbDialog'] div[id$='geoFormatBox']"
        assoccord="div[id^='QbDialog'] div[id='geoAssocCoordinateHBox']"
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2348545"
        

        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','places/NOPLACES_XY','P292/S10660', 'mrid', 'mrpass')
        #time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        #time.sleep(6)
          
          
        """    2. Go to Format tab > Click "Proportional Symbol"    """
        
        ribbonobj.select_ribbon_item("Format", "proportional_symbol")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(9)
        
        """    "3. Verify default query pane and map canvas    """

        mapcanvas="#pfjTableChart_1"
        utillobj.verify_object_visible(mapcanvas, True, "Step 3. Verify Map Canvas")
        
        Field_items=self.driver.find_elements_by_css_selector("div[id^='queryTreeColumn'] .bi-tree-view-table tr")
        actual_list=[i.text.strip() for i in Field_items]
        print('actual query list', actual_list)
        expected_list=['Chart (NOPLACES_XY)', 'Location', 'Layer', 'Marker', 'Size', 'Color', 'Tooltip', 'Multi-graph', '']
        
        utillity.UtillityMethods.asequal(self, actual_list, expected_list, "Step 3. Verify the query pane")
        
        """    "4. Drag "COUNTRY" to "Layer" in query pane.    """
        """    "5. Verify the GeoRole dialog appears    """
        """    "6. Click "Cancel"    """
        
        metaobj.drag_drop_data_tree_items_to_query_tree('COUNTRY', 1, 'Layer', 0,ty_offset=5)
        
        
        
        resultobj.wait_for_property(georoledlg, 1, expire_time=60)
        utillobj.verify_object_visible(georoledlg, True, "Step 5. Verify Georole dialog is open")
        utillobj.verify_object_visible(georolebox, True, "Step 5.2 Verify Georolebox")
        utillobj.verify_object_visible(geoformat, True, "Step 5.3 Verify Georoleformat")
        self.driver.find_element_by_css_selector("#geoRoleCancelBtn").click()
        
        
        utillobj.verify_object_visible(georoledlg, False, "Step 8. Wait for Georole dialog to close")
        
        
        """    "7. Verify "COUNTRY" is not in the query pane    """
        """    8. Right click "LATITUDE" > "Add To Query" > "Layer"    """
        """    9. Verify Layer option not available on context menu   """
        
        Field_items=self.driver.find_elements_by_css_selector("div[id^='queryTreeColumn'] .bi-tree-view-table tr")
        actual_list=[i.text.strip() for i in Field_items]
        print('actual query list', actual_list)
        expected_list=['Chart (NOPLACES_XY)', 'Location', 'Layer', 'Marker', 'Size', 'Color', 'Tooltip', 'Multi-graph', '']
        
        utillity.UtillityMethods.asequal(self, actual_list, expected_list, "Step 9. Verify the query pane")
        
        metaobj.datatree_field_click("LATITUDE", 1, 1)
        time.sleep(3)
        
        utillobj.select_or_verify_bipop_menu('Add To Query')
        time.sleep(3)
        expected_list=['Size', 'Color', 'Tooltip', 'Multi-graph']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=expected_list,msg='Step 9: Verify Layer option not available on context menu')

        """ 10. Right click "LONGITUDE" > "Map As" > "Longitude"    """
        """ 11. Verify the GeoRole dialog appears   """
        """ 12. Click "Cancel"  """
        """ 13. Log out :   """
        metaobj.datatree_field_click("LONGITUDE", 1, 1, 'Map As', 'Longitude...')
        
        resultobj.wait_for_property(georoledlg, 1, expire_time=60)
        utillobj.verify_object_visible(georoledlg, True, "Step 14.1 Verify Georole dialog is open")
        utillobj.verify_object_visible(georolebox, True, "Step 14.2 Verify Georolebox")
        utillobj.verify_object_visible(geoformat, True, "Step 14.3 Verify Georoleformat")
        utillobj.verify_object_visible(assoccord, True, "Step 14.4 Verify Assoc Cordinate box")
        
        
        self.driver.find_element_by_css_selector("#geoRoleCancelBtn").click()
        
        
        
if __name__ == '__main__':
    unittest.main()
    
        
        