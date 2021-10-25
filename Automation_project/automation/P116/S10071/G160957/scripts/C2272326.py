'''
Created on Feb 6, 2018

@author: BM13368
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2272326
TestCase Name : AHTML: Story ticket to Add new Tree Filter control. (ACT-510).
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2272326_TestClass(BaseTestCase):

    def test_C2272326(self):
        
        """
            TESTCASE VARIABLES
        """
        Report_fex1="act-510-tree-1field.fex"
        Report_fex2="act-510-tree-2fields.fex"
        Report_fex3="act-510-treeckbx-1field.fex"
        Report_fex4="act-510-treeckbx-2fields.fex"
        Test_Case_ID="C2272326"
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 1:Execute the attached repro act-510-tree-1field.fex
        Expect to see the following AHTML Document with the new TREE filter structure, displaying a single row for FRANCE, as the default value in the Fex.
        """
        utillobj.active_run_fex_api_login(Report_fex1, 'S10071_4', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 tt", "COUNTRY", 60)
        
        column_list=['COUNTRY', 'CAR', 'MODEL', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01:02: Verify report heading')
        miscelanousobj.verify_page_summary(0, '1of18records,Page1of1', 'Step 01:03: Verify the Report Heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds01.xlsx", 'Step 01:04: Verify report data')
        toc_elems=self.driver.find_elements_by_css_selector("#OBJECT3_cs #tree_dOBJECT3 li a")
        list_items=[item.text.strip() for item in toc_elems]
        expected_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        utillobj.asequal(expected_list, list_items, "Step 01:05:Verify the list of items")
        
        """
        Step 2:In the Tree filter structure click on JAPAN.
        """
        toc_elems=self.driver.find_elements_by_css_selector("#OBJECT3_cs #tree_dOBJECT3 li a")
        list_items=[item.text.strip() for item in toc_elems]
        expected_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        utillobj.asequal(expected_list, list_items, "Step 02:05:Verify the list of items")
        toc_elems[list_items.index("JAPAN")].click()
        time.sleep(4)
        
        """
        Expect to see the Filter selection of JAPAN appear in the report as 2 rows, one for each Car.
        """
        miscelanousobj.verify_page_summary(0, '2of18records,Page1of1', 'Step 02:01: Verify the Report Heading')
        column_list=['COUNTRY', 'CAR', 'MODEL', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 02:02: Verify report heading')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02a.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02a.xlsx", 'Step 02:03: Verify report data')
        utillobj.infoassist_api_logout()
        utillobj.synchronize_with_number_of_element("#SignonbtnLogin", 1, 50)
        
        """
        Step 3:Execute the attached repro act-510-tree-2fields.fex
        Expect to see the following AHTML Document with the new TREE filter structure, displaying a single row for JAPAN/DATSUN, as the default value in the Fex.
        """
        utillobj.active_run_fex_api_login(Report_fex2, 'S10071_4', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 tt", 'COUNTRY', 55)
        column_list=['COUNTRY', 'CAR', 'MODEL', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 03:01: Verify report heading')
        miscelanousobj.verify_page_summary(0, '1of18records,Page1of1', 'Step 03:02: Verify the Report Heading')

        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02.xlsx", 'Step 03:04: Verify report data')
        
        toc_elems=self.driver.find_elements_by_css_selector("#OBJECT3_cs #tree_dOBJECT3 li a")
        list_items=[item.text.strip() for item in toc_elems]
        expected_list=['ENGLAND', 'JAGUAR', 'JENSEN', 'TRIUMPH', 'FRANCE', 'PEUGEOT', 'ITALY', 'ALFA ROMEO', 'MASERATI', 'JAPAN', 'DATSUN', 'TOYOTA', 'W GERMANY', 'AUDI', 'BMW']
        utillobj.asequal(expected_list, list_items, "Step 03:05:Verify the list of items")
        
        """
        Step 4:In the Tree filter structure, click on W GERMANY.
        """
        toc_elems=self.driver.find_elements_by_css_selector("#OBJECT3_cs #tree_dOBJECT3 li a")
        list_items=[item.text.strip() for item in toc_elems]
        expected_list=['ENGLAND', 'JAGUAR', 'JENSEN', 'TRIUMPH', 'FRANCE', 'PEUGEOT', 'ITALY', 'ALFA ROMEO', 'MASERATI', 'JAPAN', 'DATSUN', 'TOYOTA', 'W GERMANY', 'AUDI', 'BMW']
        utillobj.asequal(expected_list, list_items, "Step 04:01:Verify the list of items")
        toc_elems[list_items.index("W GERMANY")].click()
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 tt", 'COUNTRY', 25)
#         resultobj.wait_for_property("#ITableData0 #TCOL_0_C_0 tt",1,55,string_value='COUNTRY')
        """
        Expect to see the Filter selection of W GERMANY and all Cars, including AUDI & BMW.
        """
        miscelanousobj.verify_page_summary(0, '7of18records,Page1of1', 'Step 04:02: Verify the Report Heading')
        column_list=['COUNTRY', 'CAR', 'MODEL', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 04:03: Verify report heading')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds03a.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds03a.xlsx", 'Step 04:04: Verify report data')
        
        """
        Step 5:In the Tree filter structure, click on AUDI to further filter the W GERMANY data.
        """
        toc_elems=self.driver.find_elements_by_css_selector("#OBJECT3_cs #tree_dOBJECT3 li a")
        list_items=[item.text.strip() for item in toc_elems]
        expected_list=['ENGLAND', 'JAGUAR', 'JENSEN', 'TRIUMPH', 'FRANCE', 'PEUGEOT', 'ITALY', 'ALFA ROMEO', 'MASERATI', 'JAPAN', 'DATSUN', 'TOYOTA', 'W GERMANY', 'AUDI', 'BMW']
        utillobj.asequal(expected_list, list_items, "Step 04:05:Verify the list of items")
        toc_elems[list_items.index("AUDI")].click()
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 tt", 'COUNTRY', 25)
#         resultobj.wait_for_property("#ITableData0 #TCOL_0_C_0 tt",1,55,string_value='COUNTRY')
        """
        Expect to see the Filter selection of W GERMANY/AUDI and only 1 row for AUDI.
        """
        miscelanousobj.verify_page_summary(0, '1of18records,Page1of1', 'Step 05:01: Verify the Report Heading')
        column_list=['COUNTRY', 'CAR', 'MODEL', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 05:02: Verify report heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds03.xlsx", 'Step 05:03: Verify report data')
        utillobj.infoassist_api_logout()
        utillobj.synchronize_with_number_of_element("#SignonbtnLogin", 1, 35)
        """
        Step 6:Execute the attached repro 
        act-510-treeckbx-1field.fex
        """
        utillobj.active_run_fex_api_login(Report_fex3, 'S10071_4', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 tt", 'COUNTRY', 60)
               
        """
        Expect to see the following AHTML Document with the new TREE Checkbox filter structure, displaying two rows for JAPAN, as the default value in the Fex.
        """
        column_list=['COUNTRY', 'CAR', 'MODEL', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 06:01: Verify report heading')
        miscelanousobj.verify_page_summary(0, '2of18records,Page1of1', 'Step 06:02: Verify the Report Heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds04.xlsx", 'Step 06:03: Verify report data')
        
        toc_elems=self.driver.find_elements_by_css_selector("#OBJECT3_cs div[class*='checkbox'] a")
        list_items=[item.text.strip() for item in toc_elems]
        expected_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        utillobj.asequal(expected_list, list_items, "Step 06:04:Verify the list of items")
        
        checkbox_elem=self.driver.find_elements_by_css_selector("#OBJECT3_cs div[class*='checkbox'] a[class$='clicked']")
        actual_text=[item.get_attribute('text') for item in checkbox_elem]
        expected_text=['JAPAN']
        utillobj.asequal(expected_text, actual_text, "Step 06:05:Verify the checkbox is selected for JAPAN")
        
        """
        Step 7:In the Tree Checkbox filter structure click on ITALY.
        """
        toc_elems=self.driver.find_elements_by_css_selector("#OBJECT3_cs div[class*='checkbox'] a")
        list_items=[item.text.strip() for item in toc_elems]
        toc_elems[list_items.index("ITALY")].click()
        """
        Expect to see 6 rows, one for each Country/Car combination for both ITALY and JAPAN.
        Expect to see the additional Checkbox value of ITALY added to the report.
        """
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 tt", 'COUNTRY', 25)
        column_list=['COUNTRY', 'CAR', 'MODEL', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 07:01: Verify report heading')
        miscelanousobj.verify_page_summary(0, '6of18records,Page1of1', 'Step 07:02: Verify the Report Heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds05.xlsx", 'Step 07:03: Verify report data')
        
        checkbox_elem=self.driver.find_elements_by_css_selector("#OBJECT3_cs div[class*='checkbox'] a[class$='clicked']")
        actual_text=[item.get_attribute('text') for item in checkbox_elem]
        expected_text=['ITALY','JAPAN']
        utillobj.asequal(expected_text, actual_text, "Step 07:04:Verify the checkbox is selected for JAPAN")
        
        utillobj.infoassist_api_logout()
        utillobj.synchronize_with_number_of_element("#SignonbtnLogin", 1, 65)
        
        """
        Step 8:Execute the attached repro 
        act-510-treeckbx-2fields.fex
        Expect to see the following AHTML Document with the new TREE Checkbox filter structure, displaying one row for ITALY/MASERATI, as the default value in the Fex.
        """
        utillobj.active_run_fex_api_login(Report_fex4, 'S10071_4', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 tt", 'COUNTRY', 65)
        
        column_list=['COUNTRY', 'CAR', 'MODEL', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 08:01: Verify report heading')
        miscelanousobj.verify_page_summary(0, '1of18records,Page1of1', 'Step 08:02: Verify the Report Heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds06.xlsx", 'Step 08:03: Verify report data')
        
        toc_elems=self.driver.find_elements_by_css_selector("#OBJECT3_cs div[class*='checkbox'] a")
        list_items=[item.text.strip() for item in toc_elems]
        expected_list=['ENGLAND', 'JAGUAR', 'JENSEN', 'TRIUMPH', 'FRANCE', 'PEUGEOT', 'ITALY', 'ALFA ROMEO', 'MASERATI', 'JAPAN', 'DATSUN', 'TOYOTA', 'W GERMANY', 'AUDI', 'BMW']
        utillobj.asequal(expected_list, list_items, "Step 08:04: Verify the list of fields")
        
        checkbox_elem=self.driver.find_elements_by_css_selector("#OBJECT3_cs div[class*='checkbox'] a[class$='clicked']")
        actual_text=[item.get_attribute('text') for item in checkbox_elem]
        expected_text=['MASERATI']
        utillobj.asequal(expected_text, actual_text, "Step 08:05:Verify the checkbox is selected for JAPAN")
        
        """
        Step 9:In the Tree Checkbox filter structure click on value JENSEN.
        """
        toc_elems=self.driver.find_elements_by_css_selector("#OBJECT3_cs div[class*='checkbox'] a")
        list_items=[item.text.strip() for item in toc_elems]
        toc_elems[list_items.index("JENSEN")].click()
        
        """
        Expect to see the additional Checkbox value of ENGLAND/JENSEN added to the report.
        Expect to see 2 rows.
        """
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 tt", 'COUNTRY', 25)
               
        column_list=['COUNTRY', 'CAR', 'MODEL', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 09:01: Verify report heading')
        miscelanousobj.verify_page_summary(0, '2of18records,Page1of1', 'Step 09:02: Verify the Report Heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds07.xlsx", 'Step 09:03: Verify report data') 
        """
        Step 10:In the Tree Checkbox filter structure click on value ITALY.
        Clicking on a Country activates all Cars.
        """
        toc_elems=self.driver.find_elements_by_css_selector("#OBJECT3_cs div[class*='checkbox'] a")
        list_items=[item.text.strip() for item in toc_elems]
        toc_elems[list_items.index("ITALY")].click()
        
        """
        Expect to see the additional Checkbox value of ITALY/ALFA ROMEO added to the report.
        Expect to see 5 rows.
        """
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 tt", 'COUNTRY', 25)
        column_list=['COUNTRY', 'CAR', 'MODEL', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 10:01: Verify report heading')
        miscelanousobj.verify_page_summary(0, '5of18records,Page1of1', 'Step 10:02: Verify the Report Heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds08.xlsx", 'Step 10:03: Verify report data')
        
        """
        Verify the list of selected items in toc table
        """
        checkbox_elem=self.driver.find_elements_by_css_selector("#OBJECT3_cs div[class*='checkbox'] a[class$='clicked']")
        actual_text=[item.get_attribute('text') for item in checkbox_elem]
        expected_text=['JENSEN', 'ITALY', 'ALFA ROMEO', 'MASERATI']
        utillobj.asequal(expected_text, actual_text, "Step 08:05:Verify the checkbox is selected for JAPAN")
        """
        Step 11:In the Tree Checkbox filter structure click on value JRNSEN.
        Removing all Cars removes all references to Country.
        """
        toc_elems=self.driver.find_elements_by_css_selector("#OBJECT3_cs div[class*='checkbox'] a")
        list_items=[item.text.strip() for item in toc_elems]
        toc_elems[list_items.index("JENSEN")].click()
        time.sleep(4)
        
        """
        Expect to see all Checkboxes removed for JENSEN and ENGLAND.
        """
        checkbox_elem=self.driver.find_elements_by_css_selector("#OBJECT3_cs div[class*='checkbox'] a[class$='clicked']")
        actual_text=[item.get_attribute('text') for item in checkbox_elem]
        expected_text=['ITALY', 'ALFA ROMEO', 'MASERATI']
        utillobj.asequal(expected_text, actual_text, "Step 11:01:Verify the checkbox is selected only for ITALY, ALFA ROMEO, MASERATI")
        
        """
        Expect to see 4 rows.
        """
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 tt", 'COUNTRY', 25)
        column_list=['COUNTRY', 'CAR', 'MODEL', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 11:01: Verify report heading')
        miscelanousobj.verify_page_summary(0, '4of18records,Page1of1', 'Step 11:02: Verify the Report Heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds09.xlsx", 'Step 11:03: Verify report data')

if __name__ == "__main__":
    unittest.main()