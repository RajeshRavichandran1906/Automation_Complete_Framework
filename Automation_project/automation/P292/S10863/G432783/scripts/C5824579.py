'''
Created on Apr 27, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5824579
TestCase Name = Verify Ribbon menus
'''

import unittest, time, re
from common.pages import visualization_metadata, visualization_ribbon, ia_resultarea, ia_run
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C5824579_TestClass(BaseTestCase):

    def test_C5824579(self):
        
        Test_Case_ID = "C5824579"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)

        """
            Step 01: Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.invoke_infoassist_api_login('report','ibisamp/car','P292_S10863/G432783', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
            Step 02: Double-click CAR and SALES
        """
        metaobj.datatree_field_click('CAR', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('SALES', 2, 1)
        time.sleep(4)
        
        """ 
            Step 03: Verify Preview
        """
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 2, Test_Case_ID+"_Ds01.xlsx", "Step 03: Verify live preview data")
          
        """ 
            Step 04: Click on the "Records:" dropdown menu in the Home Tab > Verify menu
            Step 05: Select value "10"
        """
        elem1=self.driver.find_element_by_css_selector("#singleReportCaptionLabel").text
        print(elem1)
        utillobj.asequal(elem1, "Live Preview (500 Records)", "Step 04:01: Verify live preview label caption")
        ribbonobj.switch_ia_tab('Home')
        time.sleep(5)
        
        a=['All', '1', '10', '50', '100', '500', '1000', '2000', '5000', '10000']
        combo_css=driver.find_element_by_css_selector("#HomeRecordLimit div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_css,'10', verify=True, expected_combobox_list=a, msg='Step 04:01: Records:dropdown menu in the Home Tab > Verify menu')
        time.sleep(10)
          
        """ 
            Step 06: Verify Preview
        """
        ia_resultobj.verify_report_data_set('TableChart_1', 7, 2, Test_Case_ID+"_Ds02.xlsx", "Step 06:01: Verify live preview data")
        elem1=self.driver.find_element_by_css_selector("#singleReportCaptionLabel").text
        print(elem1)
        utillobj.asequal(elem1, "Live Preview (10 Records)", "Step 06:02: Verify live preview label caption")
        
        """ 
            Step 07: Select the Slicers Tab > Click on the "Run Time" dropdown menu
        """
        ribbonobj.switch_ia_tab('Slicers')
        time.sleep(5)
        combo_elem=self.driver.find_element_by_css_selector("#SlicersRunTimeComboBox div[id^='BiButton']")
        utillobj.default_left_click(object_locator=combo_elem)
        time.sleep(1)
           
        """ 
            Step 08: Verify list of values
        """
        menu_items=driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit'] div[id^='BiComboBoxItem']")
        expected_popup_list=['All', '50', '100', '500', '1000', '5000', '10000', '50000']
        actual_popup_list=[el.text.strip() for el in menu_items  if bool(re.match('\S+', el.text.strip()))]
        print("Actual:", actual_popup_list)
        utillobj.as_List_equal(expected_popup_list, actual_popup_list, "Step 08:01: Verify List of Values")
        
        """ 
            Step 09: Select field "CAR" in the Preview
        """  
        ia_resultobj.select_field_on_canvas('TableChart_1', 1, click_type=0)
        time.sleep(5) 
        
        """ 
            Step 10: Click on "No Limit" dropdown menu in the Field Tab ribbon > Verify values
        """
        combo_elem=self.driver.find_element_by_css_selector("#FieldSortLimit div[id^='BiButton']")
        utillobj.default_left_click(object_locator=combo_elem)
        time.sleep(1)
        
        menu_items=driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit'] div[id^='BiComboBoxItem']")
        expected_popup_list=['No Limit', '5','10','15','20']
        actual_popup_list=[el.text.strip() for el in menu_items  if bool(re.match('\S+', el.text.strip()))]
        print("Actual:",actual_popup_list)
        utillobj.as_List_equal(expected_popup_list, actual_popup_list, "Step 10:01: Verify List of Values")
        time.sleep(3)
        
        """ 
            Step 11: Click on the Font (ARIAL) dropdown > Verify menu
        """
        combo_elem=self.driver.find_element_by_css_selector("#FieldFont div[id^='BiButton']")
        utillobj.default_left_click(object_locator=combo_elem)
        time.sleep(1)
        
        menu_items=driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit'] div[id^='BiComboBoxItem']")
        expected_popup_list=['ARIAL', 'ARIAL BLACK', 'ARIAL UNICODE MS', 'AVANT GARDE GOTHIC', 'BATANG', 'BATANGCHE', 'BOOKMAN', 'CALIBRI', 'CAMBRIA', 'COMIC SANS MS', 'COURIER', 'COURIER NEW', 'DFKAI-SB', 'DOTUM', 'DOTUMCHE', 'FOCUS-OEM862', 'GEORGIA', 'GUTTMANKAV', 'HELVETICA', 'HELVETICA NARROW', 'IMPACT', 'LUBALIN GRAPH', 'LUCIDA CONSOLE', 'LUCIDA SANS UNICODE', 'MEIRYO', 'MINGLIU', 'MS GOTHIC', 'MS MINCHO', 'MS PGOTHIC', 'MS PMINCHO', 'NEW CENTURY SCHOOLBOOK', 'NSIMSUN', 'PALATINO', 'PALATINO LINOTYPE', 'PMINGLIU', 'PSSAMP1A', 'PSSAMP1B', 'PSSAMP2A', 'PSSAMP2B', 'SANS-SERIF', 'SIMHEI', 'SIMSUN', 'SOUVENIR', 'SRLHEBREW', 'SYMBOL', 'TAHOMA', 'TIMES', 'TIMES NEW ROMAN', 'TRADITIONAL ARABIC', 'TREBUCHET MS', 'VERDANA', 'ZAPF CHANCERY', 'ZAPFDINGBATS']
        actual_popup_list=[el.text.strip() for el in menu_items  if bool(re.match('\S+', el.text.strip()))]
        print("Actual:",actual_popup_list)
        utillobj.as_List_equal(expected_popup_list, actual_popup_list, "Step 11:01: Verify List of Values")
        time.sleep(2)
            
        """ 
            Step 12: Click on the Font Size (9) dropdown > Verify menu
        """ 
        combo_elem=self.driver.find_element_by_css_selector("#FieldFontSize div[id^='BiButton']")
        utillobj.default_left_click(object_locator=combo_elem)
        time.sleep(1)
        
        menu_items=driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit'] div[id^='BiComboBoxItem']")
        expected_popup_list=['4', '5', '6', '7', '8', '9', '10', '11', '12', '14', '18', '24', '36', '48', '72']
        actual_popup_list=[el.text.strip() for el in menu_items  if bool(re.match('\S+', el.text.strip()))]
        print(actual_popup_list)
        utillobj.as_List_equal(expected_popup_list, actual_popup_list, "Step 12:01: Verify List of Values")
        
        """ 
            Step 13: Click on the Run menu in the toolbar > Verify menu
            Step 14: Select Preview > Verify Preview output
        """  
        combo_elem=self.driver.find_element_by_css_selector("#runMenuButton")
        utillobj.default_left_click(object_locator=combo_elem)
        time.sleep(1)
        a=['Run', 'Preview', 'Run with Default Parameter Values']
        utillobj.select_or_verify_bipop_menu('Preview', verify='true', expected_popup_list=a, msg='Step 13 Verify menu displayed')
        time.sleep(5)
        utillobj.switch_to_frame(pause=1)
        time.sleep(10)
#         ia_runobj.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx", "Step 14:01 verify runtime data")
        utillobj.switch_to_default_content(1)
        
        """ 
            Step 15: Double-click "DEALER_COST" > Verify Preview
        """ 
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        ia_resultobj.verify_report_data_set('TableChart_1', 7, 3, Test_Case_ID+"_Ds04.xlsx", "Step 15:01: Verify live preview output") 
        
        """ 
            Step 16: Click Undo in the toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        time.sleep(5)
        
        """ 
            Step 17: Verify "DEALER_COST" is removed
        """
        ia_resultobj.verify_report_data_set('TableChart_1', 7, 2, Test_Case_ID+"_Ds03.xlsx", "Step 17:01: Verify DEALER_COST is removed")  
          
        """ 
            Step 18: Select the Home Tab
        """ 
        ribbonobj.switch_ia_tab('Home')
        time.sleep(2)
          
        """ 
            Step 19: Click on the Hide Ribbon button in the upper right corner
        """
        ribbonobj.select_top_toolbar_item('show_hide_ribbon')
        
        """ 
            Step 20: Verify Ribbon is hidden
        """
        css_obj=driver.find_element_by_css_selector("#HomeFormatCluster")
        status=css_obj.is_displayed()
        utillobj.asequal(status, False, "Step 20:01: Verify Ribbon is hidden")   
         
        """ 
            Step 21: Click button again to Show Ribbon
        """ 
        ribbonobj.select_top_toolbar_item('show_hide_ribbon') 
         
        """ 
            Step 22: Verify Ribbon is displayed
        """
        css_obj=driver.find_element_by_css_selector("#HomeFormatCluster")
        status=css_obj.is_displayed()
        utillobj.asequal(status, True, "Step 20:01: Verify Ribbon is hidden")
         
        """ 
            Step 23: Click on the ? Help icon in the upper right corner
        """
        ribbonobj.select_top_toolbar_item('helpmenu')
        utillobj.switch_to_window(2)
        time.sleep(5)
           
        """ 
            Step 24: Verify topic "Introducing InfoAssist" is displayed
        """
        utillobj.switch_to_frame(pause=2, frame_css="frame[name='HelpFrame']",frame_height_value=0)
        utillobj.switch_to_frame(pause=2, frame_css="frame[name='ContentFrame']",frame_height_value=0)
        utillobj.switch_to_frame(pause=2, frame_css="frame[name='ContentViewFrame']",frame_height_value=0)
        verify_btn_css="html h1[class='title topictitle1']"
        utillobj.verify_popup(verify_btn_css,'Step 24:01: Verify ', popup_text_css="html h1[class='title topictitle1']", popup_text="Introducing InfoAssist")
        
        """ 
            Step 25: Close the window
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        driver.close()
        
        """ 
            Step 26: Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()