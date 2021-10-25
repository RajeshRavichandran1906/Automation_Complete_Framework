'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348659
Test case Name =  Verify Georole dialog  
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2348659_TestClass(BaseTestCase):

    def test_C2348659(self):
    
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        georoledlg="body[id=wndApp] div[id^='QbDialog']"
        georolebox="div[id^='QbDialog'] div[id$='oldGeoRoleBox']"
        georolebtn="div[id^='QbDialog'] div[id$='GeoRoleBox'][style*='left'] div[id^='BiButton']"
        geoformat="div[id^='QbDialog'] div[id$='geoFormatBox']"
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2348659"
        

        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','places/noplaces_xy','P292/S10660', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1", 1, 90, 1)
        
          
          
        """    2. Go to Format tab    """
        """    3. Click "Choropleth"    """
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(9)
        
        """    4. Double click "COUNTRY"    """
        """    5. Verify the Georole dialog appears    """
        """    6. Click "Geographic Role" dropdown    """
        """    7. Verify the Georoles are alphabetized    """        
        metaobj.datatree_field_click('COUNTRY', 2, 1)
        resultobj.wait_for_property(georoledlg, 1, expire_time=60)
        utillobj.verify_object_visible(georoledlg, True, "Step 5.1 Verify Georole dialog is open")
        utillobj.verify_object_visible(georolebox, True, "Step 5.2 Verify Georolebox")
        utillobj.verify_object_visible(geoformat, True, "Step 5.3 Verify Georoleformat")
        georolebtnobj=self.driver.find_element_by_css_selector(georolebtn)
        utillobj.default_left_click(object_locator=georolebtnobj)
        combolist=['City', 'Continent', 'Country', 'County', 'Five digit Zip Code', 'Geometry' , 'Postal Code', 'State', 'Three digit Zip Code', 'US City', 'US County', 'US State']
        utillobj.select_or_verify_bipop_menu(verify=True, custom_css="div[id^='BiList'] div[id^='BiComboBoxItem']", expected_popup_list=combolist, msg='Step 7. Verify geroles are alphabetized')
        
        time.sleep(4)
        utillobj.default_left_click(object_locator=georolebtnobj)
        """    8. Select "City"    """
        """    9. Verify the Geo role dialog.    """
        """    10. Click "Stored As" drop down for Country Geographic Role    """
        """    11. Verify the list is alphabetized    """
        
        wfmapobj.set_geo_role(role_name='City')
        time.sleep(3)
        
        row_num=1
        row_index=(row_num-1)*3
        elist=[]
        for i in range(row_index, row_index+3):
            elist.append(i)
        arrowlst=self.driver.find_elements_by_css_selector("div[id^='QbDialog'] [class*='group-box']  div[id^='BiComboBox']  div[id^='BiButton']")
        radiolst=self.driver.find_elements_by_css_selector("div[id^='QbDialog'] [class*='group-box'] div[id^='BiRadioButton']")
        utillobj.asequal(6,len(arrowlst), 'Step 9. Verify the combobox items in the Georole dialog')
        utillobj.asequal(4,len(radiolst), 'Step 9. Verify the radiobutton items in the Georole dialog')
        utillobj.default_left_click(object_locator=arrowlst[elist[1]])
        combolist=['FIPS', 'Name']
        utillobj.select_or_verify_bipop_menu(verify=True, custom_css="div[id^='BiList'] div[id^='BiComboBoxItem']", expected_popup_list=combolist, msg='Step 11. Verify list is alphabetized')
        #utillity.UtillityMethods.select_any_combobox_item(self, "arrowlst[" + (row_num*2-1) +"]", kwargs['dep_store_as'])

        
        time.sleep(4)
        
        """    12. Click "Geographic Role" dropdown > "State"    """
        """    13. Click the "Stored As" dropdown    """
        """    14. Verify the list.    """
        wfmapobj.set_geo_role(dep_row_num=2, dep_role_name='State')
        
        time.sleep(5)
        row_num=2
        row_index=(row_num-1)*3
        elist=[]
        for i in range(row_index, row_index+3):
            elist.append(i)
        arrowlst=self.driver.find_elements_by_css_selector("div[id^='QbDialog'] [class*='group-box']  div[id^='BiComboBox']  div[id^='BiButton']")
        utillobj.default_left_click(object_locator=arrowlst[elist[1]])
        combolist=['Name']
        utillobj.select_or_verify_bipop_menu(verify=True, custom_css="div[id^='BiList'] div[id^='BiComboBoxItem']", expected_popup_list=combolist, msg='Step 14. Verify list')
        
        """    15. Click "Geographic Role" dropdown > "GEOMETRY"    """
        """    16. Click the "Stored As" dropdown    """
        """    17. Verify "AREA" is listed    """
        
        wfmapobj.set_geo_role(role_name='Geometry')
        
        set_store_as_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[id='geoFormatBox'][style*='left'] div[id^='BiButton']")
        utillobj.default_left_click(object_locator=set_store_as_obj)
        
        combolist=['Area']
        utillobj.select_or_verify_bipop_menu(verify=True, custom_css="div[id^='BiList'] div[id^='BiComboBoxItem']", expected_popup_list=combolist, msg='Step 17. Verify Area is listed')
        
        
        """    18. Click "Geographic Role" dropdown > "State"    """
        """    19. Click the "Stored As" dropdown    """
        """    20. Verify the list is alphabetized    """
        wfmapobj.set_geo_role(role_name='State')
        
        set_store_as_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[id='geoFormatBox'][style*='left'] div[id^='BiButton']")
        utillobj.default_left_click(object_locator=set_store_as_obj)
        
        combolist=['ISO code', 'Name']
        utillobj.select_or_verify_bipop_menu(verify=True, custom_css="div[id^='BiList'] div[id^='BiComboBoxItem']", expected_popup_list=combolist, msg='Step 20. Verify list is alphabeticed')
        
        """    21. Click the "Stored As" dropdown in the "Depends on" section    """
        """    22. Verify the list is alphabetized    """
        row_num=1
        row_index=(row_num-1)*3
        elist=[]
        for i in range(row_index, row_index+3):
            elist.append(i)
        arrowlst=self.driver.find_elements_by_css_selector("div[id^='QbDialog'] [class*='group-box']  div[id^='BiComboBox']  div[id^='BiButton']")
        utillobj.default_left_click(object_locator=arrowlst[elist[1]])
        combolist=['ISO2 code', 'Name']
        utillobj.select_or_verify_bipop_menu(verify=True, custom_css="div[id^='BiList'] div[id^='BiComboBoxItem']", expected_popup_list=combolist, msg='Step 22. Verify list is alphabetized')
        
        """    23. Click "Geographic Role" dropdown > "US State"    """
        """    24. Click the "Stored As" dropdown    """
        """    25. Verify the list is alphabetized    """
        """    26. Click "Cancel"    """
        """    27. Dismiss IA window    """
        """    28. Log out :    """
        
        wfmapobj.set_geo_role(role_name='US State')
        
        set_store_as_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[id='geoFormatBox'][style*='left'] div[id^='BiButton']")
        utillobj.default_left_click(object_locator=set_store_as_obj)
        
        combolist=['Abbreviation', 'FIPS', 'Name']
        utillobj.select_or_verify_bipop_menu(verify=True, custom_css="div[id^='BiList'] div[id^='BiComboBoxItem']", expected_popup_list=combolist, msg='Step 25. Verify list is alphabetized')

        wfmapobj.set_geo_role(btn_click='Cancel')

        
if __name__ == '__main__':
    unittest.main()
    
        
        