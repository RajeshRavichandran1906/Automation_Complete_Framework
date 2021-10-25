'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348649
Test case Name =  Verify defining GeoRole with dependency  
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2348649_TestClass(BaseTestCase):

    def test_C2348649(self):
    
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
        Test_Case_ID = "C2348649"
        

         
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','places/NOPLACES_XY','P292/S10660', 'mrid', 'mrpass')
        #time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        #time.sleep(6)
           
           
        """    2. Go to Format tab    """
        """    3. Click "Proportinal Symbol" in Chart Types group    """
        ribbonobj.select_ribbon_item("Format", "proportional_symbol")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(9)
         
        """    4. Double click "STATE"    """
        """    5. Select "Geographic Role" > "State"    """
        """    6. Select "Stored As" > "Name"    """
        """    7. Verify the OK button is still disabeld    """        
        metaobj.datatree_field_click('STATE', 2, 1)
        resultobj.wait_for_property(georoledlg, 1, expire_time=60)
        utillobj.verify_object_visible(georoledlg, True, "Step 5.1 Verify Georole dialog is open")
        utillobj.verify_object_visible(georolebox, True, "Step 5.2 Verify Georolebox")
        utillobj.verify_object_visible(geoformat, True, "Step 5.3 Verify Georoleformat")
        wfmapobj.set_geo_role(role_name='State', store_as='Name')
         
        utillobj.verify_object_visible("div[id='geoRoleOkBtn'][class*='button-disabled']", True, 'Step 7. Verify OK button is still disabled')
         
        """    "8. Click the dropdown under "Field" radio button > "COUNTRY"    """
        """    "9. Set "Stored As" = "Name"    """
        """    10. Click OK    """
         
        wfmapobj.set_geo_role(dep_row_num=1, dep_field_name='COUNTRY', dep_store_as='Name', btn_click='Ok')
         
        """    11. Verify both "STATE" and "COUNTRY" icons are updated    """
        element = self.driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
        utillity.UtillityMethods.set_text_field_using_actionchains(self, element, 'COUNTRY')
        utillobj.verify_object_visible("div[id^='QbMetaDataTree'] img[src*='geo_level1_16']", True, 'Step 11.1 Verify the icon for COUNTRY')
         
        utillity.UtillityMethods.set_text_field_using_actionchains(self, element, 'STATE')
        utillobj.verify_object_visible("div[id^='QbMetaDataTree'] img[src*='geo_level3_16']", True, 'Step 11.1 Verify the icon for STATE')
         
        """    12. Hover over "STATE"    """
        """    13. Verify "Geographic Role: STATE"    """
        """    14. Verify the map is updated    """
         
        expected_list=['Segment: SEG01', 'Name: STATE', 'Alias: E03', 'Title: STATE', 'Description: STATE', 'Format: A50', 'Geographic Role: STATE']
         
        metaobj.verify_datatree_tooltip('STATE', 1, expected_list, 'Step 13. Verify Geographic Role for STATE')
         
        defcss="#pfjTableChart_1 circle[class='riser!s0!g227!mmarker!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1, expire_time=50)
        
        parentcss="pfjTableChart_1"
         
        utillobj.verify_chart_color(parentcss, "riser!s0!g148!mmarker!", 'bar_blue', 'Step 14.1a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g200!mmarker!", 'bar_blue', 'Step 14.1b Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g227!mmarker!", 'bar_blue', 'Step 14.1b Verify map color')
         
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step14'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """    15. Double click "POPULATION"    """
        """    16. Drag "COUNTRY" into Color    """
        """    17. Verify the map is updated    """
        """    18. Click "Run"    """
        """    19. Verify the correct map is displayed at runtime    """
         
        metaobj.datatree_field_click('POPULATION', 2, 1)
         
        time.sleep(4)
        metaobj.datatree_field_click('COUNTRY', 1, 1, 'Add To Query', 'Color')
         
        time.sleep(4)
         
        defcss="#pfjTableChart_1 circle[class='riser!s16!g2!mmarker!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
         
        parentcss="pfjTableChart_1"
        expected_label_list_cr=['"Bahamas, The"', '"Gambia, The"', '"Korea, North"', '"Korea, South"', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil']
        expected_label_list_ff=['"Bahamas, The"', '"Gambia, The"', '"Korea, North"', '"Korea, South"', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil']
        msg="Step 17.1. Verify Map Legends"
         
        if browser_type=="Chrome":
            resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list_cr, msg, custom_css="text[class^='legend-labels']", same_group=True)
        else:
            resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list_ff, msg, custom_css="text[class^='legend-labels']", same_group=True)
         
#         resultobj.verify_riser_legends(parentcss, expected_label_list, msg)
        expected_title_list=['COUNTRY']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 17.2. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        time.sleep(5)
        utillobj.verify_chart_color(parentcss, "riser!s16!g2!mmarker!", 'apricot', 'Step 17.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s8!g9!mmarker!", 'mantis', 'Step 17.3b Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step17'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
   
 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(9)
        utillobj.switch_to_frame(1)
        parentcss1="jschart_HOLD_0"
        #visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#jschart_HOLD_0 circle[class^='riser!s16!g2!mmarker!']", 1,expire_time=25)
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#jschart_HOLD_0 circle:nth-child(332)",1,expire_time=60)
        time.sleep(6)
        expected_label_list_cr=['"Bahamas, The"', '"Gambia, The"', '"Korea, North"', '"Korea, South"', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo (Kinshasa)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        expected_label_list_ie=['"Bahamas, The"', '"Gambia, The"', '"Korea, North"', '"Korea, South"', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        expected_label_list_ff=['"Bahamas, The"', '"Gambia, The"', '"Korea, North"', '"Korea, South"', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'French Republic', 'Gabon', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'Indeterminate', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kingdom of Norway', 'Kingdom of Spain', 'Kingdom of the Netherlands', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Northern Cyprus', 'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Republic of Serbia', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'Somaliland', 'South Africa', 'South Sudan', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United Republic of Tanzania', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican (Holy Sea)', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
        msg="Step 19.1. Verify Map Legends"
         
        if browser_type=="Chrome":
            resultobj.verify_riser_pie_labels_and_legends(parentcss1, expected_label_list_cr, msg, custom_css="text[class^='legend-labels']", same_group=True)
        elif browser_type=="IE":
            resultobj.verify_riser_pie_labels_and_legends(parentcss1, expected_label_list_ie, msg, custom_css="text[class^='legend-labels']", same_group=True)
        else:
            resultobj.verify_riser_pie_labels_and_legends(parentcss1, expected_label_list_ff, msg, custom_css="text[class^='legend-labels']", same_group=True)
   
        expected_title_list=['COUNTRY']
        resultobj.verify_riser_pie_labels_and_legends(parentcss1, expected_title_list, 'Step 19.2. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        time.sleep(5)
        utillobj.verify_chart_color(parentcss1, "riser!s16!g2!mmarker!", 'flame_pea', 'Step 19.3a Verify map color')
        utillobj.verify_chart_color(parentcss1, "riser!s8!g9!mmarker!", 'apple1', 'Step 19.3b Verify map color')
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step19'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
   
        """    20. Click "Save" icon    """
        """    21. Enter Title "C2348649"    """
        """    22. Click "Save" and dismiss IA window    """
        utillobj.switch_to_default_content(pause=3)
 
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
         
        """    23. Run the saved fex.    """
        """    24. Verify the map is run in a new window    """
         
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10660_esrimap_1', mrid='mrid', mrpass='mrpass')
        print (1)
        
        #utillobj.switch_to_window(wndnum=0, pause=5)
        print (2)
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#jschart_HOLD_0 circle:nth-child(279)", 1)
        print (3)
        time.sleep(8)
        parentcss="jschart_HOLD_0"
        expected_label_list_cr=['"Bahamas, The"', '"Gambia, The"', '"Korea, North"', '"Korea, South"', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        expected_label_list_ff=['"Bahamas, The"', '"Gambia, The"', '"Korea, North"', '"Korea, South"', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'French Republic', 'Gabon', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'Indeterminate', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kingdom of Norway', 'Kingdom of Spain', 'Kingdom of the Netherlands', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Northern Cyprus', 'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Republic of Serbia', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'Somaliland', 'South Africa', 'South Sudan', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United Republic of Tanzania', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican (Holy Sea)', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
        expected_label_list_ie=['"Bahamas, The"', '"Gambia, The"', '"Korea, North"', '"Korea, South"', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        msg="Step 24.1. Verify Map Legends"
        print (4)
        if browser_type=="Chrome":
            resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list_cr, msg, custom_css="text[class^='legend-labels']", same_group=True)
        elif browser_type=="IE":
            resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list_ie, msg, custom_css="text[class^='legend-labels']", same_group=True)
        else:
            resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list_ff, msg, custom_css="text[class^='legend-labels']", same_group=True)
        print (5)
        expected_title_list=['COUNTRY']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 24.2. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        time.sleep(5)
        utillobj.verify_chart_color(parentcss, "riser!s26!g12!mmarker!", 'apple2', 'Step 24.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s78!g18!mmarker!", 'polo_blue', 'Step 24.3b Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s117!g2!mmarker!", 'salomie', 'Step 24.3c Verify map color')
        
        
        """    25. Hover over a bubble in the map    """
        """    26. Verify the tooltip displays correct information    """
        
        
        expected_tooltip=['STATE:Eastern Cape|South Africa', 'POPULATION:1939761', 'COUNTRY:South Africa']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0',"riser!s161!g0!mmarker!",expected_tooltip, "Step 26: Verify Tooltip is displayed correctly")

        """    27. Dismiss the map window    """
        """    28. Launch the IA API with chart in edit mode    """
        """    29. Verify IA is launched, preserving the map    """
        """    30. Log out :    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10660', mrid='mrid', mrpass='mrpass')
        time.sleep(3)
        defcss="#pfjTableChart_1 circle[class^='riser!s16!g2!mmarker!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        
        parentcss="pfjTableChart_1"
        expected_label_list_cr=['"Bahamas, The"', '"Gambia, The"', '"Korea, North"', '"Korea, South"', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil']
        expected_label_list_ff=['"Bahamas, The"', '"Gambia, The"', '"Korea, North"', '"Korea, South"', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil']
        msg="Step 29.1. Verify Map Legends"
        
        if browser_type=="Chrome":
            resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list_cr, msg, custom_css="text[class^='legend-labels']", same_group=True)
        else:
            resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list_ff, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['COUNTRY']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 29.2. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        time.sleep(5)
        utillobj.verify_chart_color(parentcss, "riser!s16!g2!mmarker!", 'apricot', 'Step 29.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s8!g9!mmarker!", 'mantis', 'Step 29.3b Verify map color')
       
if __name__ == '__main__':
    unittest.main()
    
        
        