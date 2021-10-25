'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229083
Test case Name =  Verify redefining GeoRole 
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229083_TestClass(BaseTestCase):

    def test_C2229083(self):
    
        
        utillobj = utillity.UtillityMethods(self.driver)
        
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        georoledlg="body[id=wndApp] div[id^='QbDialog']"
        georolebox="div[id^='QbDialog'] div[id$='cbGeoRole']"
        geoformat="div[id^='QbDialog'] div[id$='geoFormatBox']"
        
       
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','places/NOPLACES_XY','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
          
          
        """    2. Go to Format tab    """
        """    3. Click "Choropleth"    """
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(9)
        """    4. Right click "STATE" > "Map As" > "Country (Name)"    """
        """    5. Right click "STATE" > "Map As" > "State/Province"    """
        """    6. Verify the georole dialog appears    """
        """    7. Click "Stored As" value > "Name"    """
        """    "8. Click the Field dropdown > "COUNTRY" > OK    """
        metaobj.datatree_field_click("STATE", 1, 1, 'Map As', 'Country (Name)')
        
        time.sleep(3)
        
        metaobj.datatree_field_click("STATE", 1, 1, 'Map As', 'State/Province...')
        
        time.sleep(3)
   
        resultobj.wait_for_property(georoledlg, 1, expire_time=60)
        utillobj.verify_object_visible(georoledlg, True, "Step 7. Verify Georole dialog is open")
        utillobj.verify_object_visible(georolebox, True, "Step 7.2 Verify Georolebox")
        utillobj.verify_object_visible(geoformat, True, "Step 7.3 Verify Georoleformat")
        wfmapobj.set_geo_role(store_as='Name', dep_field_name='COUNTRY', btn_click='Ok')
          
        utillobj.verify_object_visible(georoledlg, False, "Step 8. Wait for Georole dialog to close")
        
        """    "9. Verify both "STATE" and "COUNTRY" fields are updated with geographic roles    """
        """    10. Dismiss IA (do not save changes)"""
        """    11. Log out :    """
        expected_list=['Segment: NOPLACES_XY', 'Name: STATE', 'Alias: STATE', 'Title: STATE', 'Description: STATE', 'Format: A45V', 'Geographic Role: STATE']
        
        metaobj.verify_datatree_tooltip(field_name='STATE', position=1, expected_list=expected_list,msg="Step 9. Verify Tooltip for STATE", x_offset=20, y_offset=5)
        
        element = self.driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
        utillity.UtillityMethods.set_text_field_using_actionchains(self, element, 'STATE')
        
        utillobj.verify_object_visible("div[id^='QbMetaDataTree'] img[src*='geo_level3_16']", True, 'Step 9.1 Verify the icon for STATE')
        
        
        
        expected_list=['Segment: NOPLACES_XY', 'Name: COUNTRY', 'Alias: COUNTRY', 'Title: COUNTRY', 'Description: COUNTRY', 'Format: A26V', 'Geographic Role: COUNTRY']
        
        metaobj.verify_datatree_tooltip(field_name='COUNTRY', position=1, expected_list=expected_list,msg="Step 9. Verify Tooltip for COUNTRY", x_offset=20, y_offset=5)
        
        element = self.driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
        utillity.UtillityMethods.set_text_field_using_actionchains(self, element, 'COUNTRY')
        utillobj.verify_object_visible("div[id^='QbMetaDataTree'] img[src*='geo_level1_16']", True, 'Step 9.1 Verify the icon for COUNTRY')

        
        
if __name__ == '__main__':
    unittest.main()
    
        
        