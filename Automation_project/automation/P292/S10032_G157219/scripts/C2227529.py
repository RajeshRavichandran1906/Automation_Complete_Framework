'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227529
'''
import unittest
import time, re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous, ia_run
from common.lib import utillity
from selenium.webdriver.support.ui import Select
import keyboard as local_keyboard

class C2227529_TestClass(BaseTestCase):

    def test_C2227529(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2227529'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        time_out=30
        val1=['[All]']
        val2=['[All]', '100 LS 2 DOOR AUTO', '2000 4 DOOR BERLINA', '2000 GT VELOCE', '2000 SPIDER VELOCE', '2002 2 DOOR', '2002 2 DOOR AUTO', '3.0 SI 4 DOOR', '3.0 SI 4 DOOR AUTO', '504 4 DOOR', '530I 4 DOOR', '530I 4 DOOR AUTO', 'B210 2 DOOR AUTO', 'COROLLA 4 DOOR DIX AUTO', 'DORA 2 DOOR', 'INTERCEPTOR III', 'TR7', 'V12XKE AUTO', 'XJ12L AUTO']
        val3=['[All]', '0', '4800', '7800', '8900', '8950', '12000', '12400', '13000', '14000', '15600', '18940', '35030', '43000']
        
        
        """    1. Launch IA Document mode: http://machine:port/ibi_apps/ia?tool=Document&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032    """
        utillobj.infoassist_api_login('document','ibisamp/car','P292/S10032', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", visble_element_text='Document', expire_time=time_out)
        
        """    2. Double click "COUNTRY", "CAR", "MODEL", "DEALER_COST", "SALES".    """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 6, time_out)
        metaobj.datatree_field_click("CAR", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 17, time_out)
        metaobj.datatree_field_click("MODEL", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 36, time_out)    
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 55, time_out)
        metaobj.datatree_field_click("SALES", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 74, time_out)  
        ribbonobj.repositioning_document_component('0.5', '0.75')
        
        """    3. Verify the following "Report" in Canvas    """
        coln_list = ["COUNTRY", "CAR", "MODEL", "DEALER_COST", "SALES"]
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1 ", coln_list, "Step 03a: Verify column titles")
        ia_resultobj.create_report_data_set('TableChart_1 ', 18, 5, 'C2227529_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1 ', 18, 5, 'C2227529_Ds01.xlsx', 'Step 03b: Verify Preview report dataset')
        
        """    4. Select "Insert" > "Drop Down" (Active Dashboard Prompts Group).    """
        ribbonobj.select_ribbon_item("Insert", "Drop_down")
        
        """    5. Resize the inserted ADP component little larger     """
        ribbonobj.resizing_document_component('0.25', '2.5')
        
        """    6. Re-position the newly added "Drop Down" so that it will not be on top of the report.    """
        ribbonobj.repositioning_document_component('8', '1')
        time.sleep(3)
        
        """    7. Right mouse click "Drop Down" > "Properties" > Field = "COUNTRY".    """
        """    8. Verify "Report1" goes to "Targets" section.    """
        """    9. Verify "Include All" checkbox is enabled    """
        """    10. Click "OK".    """
        resultobj.choose_right_click_menu_item_for_prompt(1, 'Properties')
        time.sleep(3)
        ComboBox_1_source = {'select_field':'COUNTRY', 'verify_includeall':True}
        ComboBox_1_target = {'verify_target_name':['Report1']}
        resultobj.customize_active_dashboard_properties(source=ComboBox_1_source, targets=ComboBox_1_target, msg="Step 08.", btn_type='ok') 
        time.sleep(5)
        
        """    11. Click "Checkbox" icon.    """
        ribbonobj.select_ribbon_item("Insert", "Checkbox")
        
        """    12. Resize the inserted ADP component little larger     """
        ribbonobj.resizing_document_component('1.04', '2.5')

        """    13. Re-position the newly added "Checkbox" so that it will not be on top of the report.    """
        ribbonobj.repositioning_document_component('8', '2')
        
        """    14. Right mouse click "Checkbox" > "Properties" > Field = "MODEL"    """
        """    15. Verify "Include All" checkbox is enabled.    """
        """    16. Click > "OK".    """
        resultobj.choose_right_click_menu_item_for_prompt(2, 'Properties')
        time.sleep(3)
        ComboBox_1_source = {'select_field':'MODEL', 'verify_includeall':True}
        resultobj.customize_active_dashboard_properties(source=ComboBox_1_source, msg="Step 15.", btn_type='ok') 
        time.sleep(5)
        
        """    17. Click "Radio Button" icon.    """
        ribbonobj.select_ribbon_item("Insert", "Radio_button")

        """    18. Resize the inserted ADP component little larger     """
        ribbonobj.resizing_document_component('1.04', '2.5')

        """    19. Re-position the newly added "Radio Button" so that it will not be on top of the report.    """
        ribbonobj.repositioning_document_component('8', '4')
        time.sleep(3)
        
        """    20. Right mouse click "Radio Button" > Properties > Field = "SALES".    """
        """    21. Verify "Include All" checkbox is enabled.    """
        """    22. Click "OK"    """
        resultobj.choose_right_click_menu_item_for_prompt(3, 'Properties')
        time.sleep(3)
        ComboBox_1_source = {'select_field':'SALES', 'verify_includeall':True}
        resultobj.customize_active_dashboard_properties(source=ComboBox_1_source, msg="Step 21.", btn_type='ok') 
        time.sleep(5)
        
        """    23. Select "Drop Down" (Active Dashboard Prompt) that is on the canvas > Right mouse click > Properties.    """
        resultobj.choose_right_click_menu_item_for_prompt(1, 'Properties')
        time.sleep(5)
        
        """    24. Click "Cascades".    """
        """    25. Verify name of "prompts" are displayed as shown.    """
        cascade_Btn=driver.find_element_by_css_selector('#btnCascadesOpt img')
        utillobj.default_left_click(object_locator=cascade_Btn)
        expected_prompts=['combobox_1', 'checkbox_2', 'radiobutton_3']
        item_list=driver.find_elements_by_css_selector("#gridAvailableADP div[class$='content'] table tr>td:nth-child(1)")
        actual_prompts=[el.text.strip() for el in item_list if bool(re.match('\S+', el.text.strip()))]
        utillobj.asequal(actual_prompts, expected_prompts, "Step 25: Verify name of 'prompts' are displayed")
        
        """    26. Select "COUNTRY", "MODEL".    """
        utillobj.click_on_screen(item_list[0], coordinate_type='middle', click_type=1)
        time.sleep(1)
        local_keyboard.press('ctrl')
        time.sleep(1)
        utillobj.click_on_screen(item_list[1], coordinate_type='middle', click_type=1)
        time.sleep(1)
        local_keyboard.release('ctrl')
        time.sleep(1)
                        
        """    27. Click double arrow.    """
        add_cascade_Btn=driver.find_element_by_css_selector('#btnAddToCascade img')
        utillobj.default_left_click(object_locator=add_cascade_Btn)
        time.sleep(2)
        
        """    28. Verify those fields are moved to "Selected Prompts" area.    """
        selected__prompts={'verify_selected_items':['combobox_1', 'checkbox_2']}
        resultobj.add_and_verify_prompts_in_cascade(selected_prompts=selected__prompts, msg="Step 28.")
        
        """    29. Click "OK".    """
        resultobj.customize_active_dashboard_properties(btn_type='ok') 
        time.sleep(5)
        
        """    30. Verify the following components are displayed on Canvas    """
        coln_list = ["COUNTRY", "CAR", "MODEL", "DEALER_COST", "SALES"]
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1 ", coln_list, "Step 30a: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1 ', 18, 5, 'C2227529_Ds01.xlsx', 'Step 30b: Verify Preview report dataset')
        p1=driver.find_elements_by_css_selector("#Prompt_1")
        prompt1=[el.text.strip() for el in p1]
        utillobj.asequal(prompt1, val1, "Step 30c Verify prompt 1 Combobox")
        p2=driver.find_elements_by_css_selector("#Prompt_2 div[id^='BiCheckBox-']")
        prompt2=[el.text.strip() for el in p2]
        utillobj.asequal(prompt2, val2, "Step 30d Verify prompt 2 Checkbox")
        p3=driver.find_elements_by_css_selector("#Prompt_3 div[id^='BiRadioButton-']")
        prompt3=[el.text.strip() for el in p3]
        utillobj.asequal(prompt3, val3, "Step 30e Verify prompt 3 Radio buttons")
        
        """    31. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        
        """    32. Verify all inserted Active Dashboard Prompts components are displayed.    """
        utillobj.switch_to_frame()
        miscobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 32a: Verify the Report Heading')
        column_list=["COUNTRY", "CAR", "MODEL", "DEALER_COST", "SALES"]
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 32b: Verify the column heading')
        utillobj.create_data_set('ITableData0', 'I0r', 'C2227529_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2227529_Ds02.xlsx', 'Step 32c: Verify data.')
        val11=['[All]', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        p1=driver.find_elements_by_css_selector("#combobox_dPROMPT_1 option")
        prompt1=[el.text.strip() for el in p1]
        utillobj.asequal(prompt1, val11, "Step 32d Verify prompt 1 Combobox")
        p2=driver.find_elements_by_css_selector("#checkbox_dPROMPT_2 tr")
        prompt2=[el.text.strip() for el in p2]
        utillobj.asequal(prompt2, val2, "Step 32e Verify prompt 2 Checkbox")
        p3=driver.find_elements_by_css_selector("#radiobutton_dPROMPT_3 tr")
        prompt3=[el.text.strip() for el in p3]
        utillobj.asequal(prompt3, val3, "Step 32f Verify prompt 3 Radio buttons")
                
        """    33. Click "Drop Down" arrow > select "ITALY".    """
        time.sleep(5)
        sel=Select(driver.find_element_by_id("combobox_dsPROMPT_1"))
        sel.select_by_value('ITALY')
        
        """    34. Verify output window is updated with "ITALY" information.    """
        miscobj.verify_page_summary(0, '4of18records,Page1of1', 'Step 34a: Verify the Report Heading')
        column_list=["COUNTRY", "CAR", "MODEL", "DEALER_COST", "SALES"]
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 34b: Verify the column heading')
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2227529_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2227529_Ds03.xlsx', 'Step 34c: Verify data.')
        
        cascade_prompt_2=['[All]', '2000 4 DOOR BERLINA', '2000 GT VELOCE', '2000 SPIDER VELOCE', 'DORA 2 DOOR']
        p2=driver.find_elements_by_css_selector("#checkbox_dPROMPT_2 tr")
        prompt2=[el.text.strip() for el in p2]
        print("prompt2:", prompt2)
        utillobj.asequal(prompt2, cascade_prompt_2, "Step 34c Verify prompt 2 Checkbox updated due to Cascade")
        
        """    35. Enable "7800" in the Radio Button control.    """
        ia_runobj.select_active_dashboard_prompts('radio_button', "#PROMPT_3_cs", ['7800'])
#         driver.find_element_by_css_selector("#radiobutton_dPROMPT_3 input[value='7800']").click()
        time.sleep(2)
        
        """    36. Verify output is refreshed and SALES = 7800 is displayed correctly.    """
        miscobj.verify_page_summary(0, '1of18records,Page1of1', 'Step 36a: Verify the Report Heading')
        column_list=["COUNTRY", "CAR", "MODEL", "DEALER_COST", "SALES"]
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 36b: Verify the column heading')
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2227529_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2227529_Ds04.xlsx', 'Step 36c: Verify data.')
        
        p2=driver.find_elements_by_css_selector("#checkbox_dPROMPT_2 tr")
        prompt2=[el.text.strip() for el in p2]
        print("prompt2:", prompt2)
        utillobj.asequal(prompt2, cascade_prompt_2, "Step 36d Verify prompt 2 Checkbox updated has no change")
        utillobj.switch_to_default_content()
        
        """    37. Click "IA" > "Save".    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        
        """    38. Enter Title = "C2227529".    """
        """    39. Click "Save".    """
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    40. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        
        """    41. Run saved FEX: http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2227529.fex    """
        oFolder=utillobj.parseinitfile('suite_id')
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", oFolder, 'mrid', 'mrpass')
        
        """    42. Verify report    """
        miscobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 42a: Verify the Report Heading')
        column_list=["COUNTRY", "CAR", "MODEL", "DEALER_COST", "SALES"]
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 42b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2227529_Ds02.xlsx', 'Step 42c: Verify data.')
        
        val11=['[All]', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        p1=driver.find_elements_by_css_selector("#combobox_dPROMPT_1 option")
        prompt1=[el.text.strip() for el in p1]
        utillobj.asequal(prompt1, val11, "Step 42d Verify prompt 1 Combobox")
        p2=driver.find_elements_by_css_selector("#checkbox_dPROMPT_2 tr")
        prompt2=[el.text.strip() for el in p2]
        utillobj.asequal(prompt2, val2, "Step 42e Verify prompt 2 Checkbox")
        p3=driver.find_elements_by_css_selector("#radiobutton_dPROMPT_3 tr")
        prompt3=[el.text.strip() for el in p3]
        utillobj.asequal(prompt3, val3, "Step 42f Verify prompt 3 Radio buttons")
        
        """    43. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()