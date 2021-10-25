'''
Created on Nov 21, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348794
TestCase Name = Verify redefining GeoRole
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, wf_map
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2348794_TestClass(BaseTestCase):

    def test_C2348794(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348794'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        
        """
        Step 01: Launch the IA API with Visalization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=idis&master=places/NO_PLACESXY
        """
        utillobj.infoassist_api_login('idis','places/noplaces_xy','P292/S10660_esrimap_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css,1)
          
        """
        Step 02: Click "Change" dropdown > "Choropleth"
        """
        ribbonobj.change_chart_type("choropleth_map")
        time.sleep(5)
        parent_css="[class*='esriScalebarSecondNumber']"
        resultobj.wait_for_property(parent_css,2)
        
        """
        Step 03: Right click "STATE" > "Map As" > "US State (Name)"
        """
        time.sleep(4)
        metaobj.datatree_field_click('STATE',1, 1, 'Map As', 'US State (Name)')
        
        """
        Step 04: Right click "STATE" > "Map As" > "State/Province"
        """
        time.sleep(6)
        metaobj.datatree_field_click('STATE',1, 1, 'Map As', 'State/Province...')
        
        """
        Step 05. Verify the georole dialog appears
        """
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#geoRoleCancelBtn')
        resultobj._validate_page(elem)
        cap_css="div[id^='QbDialog']  div[class^='bi-window-caption window-caption'] div[class^='bi-label'][style*='left']"
        cap_text='Map STATE'
        utillobj.verify_popup("div[id^='QbDialog']>div[class*='active']", "Step 05: Verify the georole dialog appears", caption_css=cap_css, caption_text=cap_text)
        
        """ 
        Step 06. Click "Stored As" value > "Name"
        Step 07. Click the Field dropdown > "COUNTRY_CODE" > OK
        """
        wfmapobj.set_geo_role(store_as='Name', dep_field_name='COUNTRY_CODE', btn_click='Ok')
        
        """
        Step 08. Verify both "STATE" and "COUNTRY_CODE" fields are updated with geographic roles
        """
        time.sleep(8)
        items_list = ['COUNTRY','COUNTRY_CODE','STATE'] 
        metaobj.verify_fields_in_datatree('Geography', items_list, 'step 08.a: verify list of values in datatree')
        time.sleep(3)
        expected_list=['Segment: NOPLACES_XY', 'Name: STATE', 'Alias: STATE', 'Title: STATE', 'Description: STATE', 'Format: A45V', 'Geographic Role: STATE']
        metaobj.verify_datatree_tooltip('STATE', 1, expected_list, "Step 08.b: Verify STATE field is updated with geographic roles")
        time.sleep(5)
        expected_list=['Segment: NOPLACES_XY', 'Name: COUNTRY_CODE', 'Alias: COUNTRY_CODE', 'Title: COUNTRY_CODE', 'Description: COUNTRY_CODE', 'Format: A2V', 'Geographic Role: COUNTRY']
        metaobj.verify_datatree_tooltip('COUNTRY_CODE', 1, expected_list, "Step 08.c: Verify COUNTRY_CODE field is updated with geographic roles", keyboard_type=True)
        time.sleep(3)
        
        """
        Step 09: Exit IA
        """
                
if __name__ == '__main__':
    unittest.main()