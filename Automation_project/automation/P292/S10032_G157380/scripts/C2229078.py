'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229078
Test case Name =  Verify right click menu for fields 
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229078_TestClass(BaseTestCase):

    def test_C2229078(self):
    
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        driver.implicitly_wait(15)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        
                
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
          
          
        """    2. Go to Format tab    """
        """    3. Click "Proportional Symbol"    """
        ribbonobj.select_ribbon_item("Format", "proportional_symbol")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(9)
        #ribbonobj.switch_ia_tab('Home')
        #time.sleep(6)
        """    4. Right click "Store,Country"    """
        """    5. Verify the right click menu    """
        
        metaobj.datatree_field_click('Store,Country', 1,1)
        time.sleep(3)
        expected_list=['Sum', 'Create Group...', 'Add To Query', 'Filter', 'Slicers', 'Map As']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=expected_list,msg='Step 5: Verify right click popup menu for Store,Country')
        
        
        """    6. Hover over "Add To Query"    """
        """    7. Verify the menu    """
        utillobj.select_or_verify_bipop_menu('Add To Query')
        time.sleep(3)
        expected_list=['Size', 'Color', 'Layer', 'Tooltip', 'Multi-graph']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=expected_list,msg='Step 7: Verify Add to Query popup menu')
        
        """    "8. Verify "Slicers" menu    """
        """    "9. Verify "Map As" menu    """
        metaobj.datatree_field_click('Store,Country', 1,1)
        time.sleep(3)
        
        utillobj.select_or_verify_bipop_menu('Slicers')
        time.sleep(3)
        expected_list=['New Group']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=expected_list,msg='Step 8: Verify Slicers popup menu')
        
        metaobj.datatree_field_click('Store,Country', 1,1)
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Map As')
        time.sleep(3)
        expected_list=['3 Digit Zipcode', '5 Digit Zipcode', 'City (United States)...', 'City...', 'Continent', 'Country (ISO2)', 'Country (ISO3)', 'Country (Name)', 'County (United States)...', 'County...', 'Geometry (Point)', 'Latitude...', 'Longitude...', 'Postal code', 'State/Province...', 'US State (Abbreviation)', 'US State (FIPS)', 'US State (Name)']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=expected_list,msg='Step 9: Verify Map as popup menu')
        
        """    10. Right click "Cost of Goods"    """
        """    11. Verify the right click menu    """
        metaobj.datatree_field_click('Cost of Goods', 1,1)
        time.sleep(3)
        expected_list=['Sum', 'Create Bins...', 'Add To Query', 'Filter', 'Map As']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=expected_list,msg='Step 11: Verify Cost of Goods right click popup menu')
        
        """    12. Verify the "Add To Query" menu    """
        """    13. Verify "Map As" menu    """
        """    14. Dismiss IA    """
        """    15.Log out :    """
        utillobj.select_or_verify_bipop_menu('Add To Query')
        time.sleep(3)
        expected_list=['Size', 'Color', 'Tooltip', 'Multi-graph']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=expected_list,msg='Step 12: Verify Add to query popup menu')
        
        metaobj.datatree_field_click('Cost of Goods', 1,1)
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Map As')
        time.sleep(3)
        expected_list=['3 Digit Zipcode', '5 Digit Zipcode', 'City (United States)...', 'City...', 'Continent', 'Country (ISO2)', 'Country (ISO3)', 'Country (Name)', 'County (United States)...', 'County...', 'Geometry (Point)', 'Latitude...', 'Longitude...', 'Postal code', 'State/Province...', 'US State (Abbreviation)', 'US State (FIPS)', 'US State (Name)']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=expected_list,msg='Step 13: Verify Map as popup menu')

        
if __name__ == '__main__':
    unittest.main()
    
        