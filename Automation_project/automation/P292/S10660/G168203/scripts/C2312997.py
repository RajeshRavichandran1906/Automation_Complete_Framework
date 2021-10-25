'''
Created on December 16, 2017

@author: PM14587
Testcase Name : Verify SET command for Missing Value with Join in request
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2312997
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea,ia_ribbon,ia_run
from common.lib import utillity

class C2312997_TestClass(BaseTestCase):

    def test_C2312997(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2312997'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbon= ia_ribbon.IA_Ribbon(self.driver)
        iaresult= ia_resultarea.IA_Resultarea(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        
        """
            Step 01 : Launch Report Mode: http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/empdata&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('Report','ibisamp/empdata','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(3)
         
        """
            Step 02 : Select Data Tab > Join
            Step 03 : Click 'Add New' > training > Open
            Step 04 : Click OK
        """
        iaribbon.create_join('ibisamp->training.mas',save_folder='ibisamp')
        iaribbon.select_join_menu_buttons('ok')
        resultobj.wait_for_property("#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr:nth-child(13)>td[class='']", 1,20,string_value='COURSECODE')
        
        """
            Step 05 : Add fields DEPT, LASTNAME, COURSECODE, EXPENSES 
        """
        metaobj.datatree_field_click('Dimensions->DEPT',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,20,string_value='DEPT')
        
        metaobj.datatree_field_click('Dimensions->LASTNAME',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,20,string_value='LASTNAME')
        
        metaobj.datatree_field_click('Dimensions->COURSECODE',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(6)", 1,20,string_value='COURSECODE')
        
        metaobj.datatree_field_click('Measures/Properties->EXPENSES',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,20,string_value='EXPENSES')
        time.sleep(3)
        
        """
            Step 06 : Click on the 'Procedure Settings' button in the toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_showfex_setting')
        
        """
            Step 07.0 : Verify default settings 
            Step 07.1 : Verify Unchecked values
        """
        unchecked_row=['Collation Sequence','Summary Lines','Missing Value','Decimal Notation']
        for row in unchecked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','unchecked','Step 07.1 : Verify '+row+' is not selected')
        
        """
             Step 07.2 : Verify checked values
        """
        checked_row=['HTML Encode','Empty Report']
        for row in checked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','checked','Step 07.2 : Verify '+row+' is selected')
        
        """
            Step 07.3 : Verify default combobox values
        """
        combobox_row=['Collation Sequence','Summary Lines']
        expected_chombobox_values=['Code Page','New']
        for i in range(len(combobox_row)) :
            iaribbon.procedure_setting_dialogverify(combobox_row[i],'combobox',expected_chombobox_values[i],'Step 07.3 : Verify '+combobox_row[i]+' default value is '+expected_chombobox_values[i])
        
        """
            Step 07.4 : Verify "Missing Value" default value
        """
        iaribbon.procedure_setting_dialogverify('Missing Value','textbox','.','Step 07.4 : Verify Missing Value default value')
        
        """
            Step 07.5 : Verify Decimal Notation ON and OFF status 
        """
        iaribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','unchecked','Step 07.5 : Verify Decimal Notation ON is not selected',1)
        iaribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','checked','Step 07.5 : Verify Decimal Notation OFF is selected',2)
            
        """
            Step 07.6 : Verify HTML Encode ON and OFF status 
        """
        iaribbon.procedure_setting_dialogverify('HTML Encode','radiobutton','checked','Step 07.6 : Verify HTML Encode ON is selected',1)
        iaribbon.procedure_setting_dialogverify('HTML Encode','radiobutton','unchecked','Step 07.6 : Verify HTML Encode OFF is not selected',2)
        
        """
            Step 07.7 : Verify Empty Report ON and OFF status 
        """
        iaribbon.procedure_setting_dialogverify('Empty Report','radiobutton','checked','Step 07.7 : Verify Empty Report ON is selected',1)
        iaribbon.procedure_setting_dialogverify('Empty Report','radiobutton','unchecked','Step 07.7 : Verify Empty Report OFF is not selected',2)
        
        """
            Step 08 : Check off 'Missing Value' > Type None > Click OK
        """
        iaribbon.procedure_setting_dialog_input('Missing Value','checkbox','unchecked')
        iaribbon.procedure_setting_dialog_input('Missing Value','textbox','None')
        iaribbon.procedure_setting_dialog_dismiss('OK')
        
        """
            Step 09 : Click 'View Source' button in the toolbar > Verify Syntax for Missing Value > Click OK
        """
        expected_syntax_list=["DEFAULTH &WF_NODATA='None';","SET NODATA=&WF_NODATA"]
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 09.1 : Verify Syntax for Missing Value')
        
        """
            Step 10 : Verify Live Preview displaying 'None' for each missing value
        """
        iaresult.verify_row_total_report_titles_on_preview(4,4,'TableChart_1',['DEPT', 'LASTNAME', 'COURSECODE', 'EXPENSES'],'Step 10.1 : Verify Live Preview')
        none_value_element=self.driver.find_elements_by_css_selector("#TableChart_1 div[class^='x']")[10]
        utillobj.asequal('None',none_value_element.text.strip(),'Step 10.2 : Verify Live Preview displaying "None" for each missing value')
        none_value_element=self.driver.find_elements_by_css_selector("#TableChart_1 div[class^='x']")[13]
        utillobj.asequal('None',none_value_element.text.strip(),'Step 10.3 : Verify Live Preview displaying "None" for each missing value')
        none_value_element=self.driver.find_elements_by_css_selector("#TableChart_1 div[class^='x']")[16]
        utillobj.asequal('None',none_value_element.text.strip(),'Step 10.4 : Verify Live Preview displaying "None" for each missing value')
        
        """
            Step 11 : Click 'Run' in the toolbar 
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("table[summary] tr:nth-child(1)>td", 1,20,string_value='DEPT')
        
        """
            Step 11.1 : Verify output displaying 'None' for each missing value
        """
        #iarun.create_table_data_set("table[summary]",Test_Case_ID+'_DataSet_01.xlsx')
        iarun.verify_table_data_set("table[summary]",Test_Case_ID+'_DataSet_01.xlsx',"Step 11.1 : Verify  output displaying 'None' for each missing value")
        
        """
            Step 12 : Click 'Save' in the toolbar > Save as > C2312997 > Click 'Save'
        """
        utillobj.switch_to_default_content(3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 13 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 14 : Restore saved Fex: http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Public/C2312997.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_4',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(5)
        
        """
            Step 15 : Verify Live Preview
        """
        iaresult.verify_row_total_report_titles_on_preview(4,4,'TableChart_1',['DEPT', 'LASTNAME', 'COURSECODE', 'EXPENSES'],'Step 15.1 : Verify Live Preview')
        none_value_element=self.driver.find_elements_by_css_selector("#TableChart_1 div[class^='x']")[10]
        utillobj.asequal('None',none_value_element.text.strip(),'Step 15.2 : Verify Live Preview displaying "None" for each missing value')
        none_value_element=self.driver.find_elements_by_css_selector("#TableChart_1 div[class^='x']")[13]
        utillobj.asequal('None',none_value_element.text.strip(),'Step 15.3 : Verify Live Preview displaying "None" for each missing value')
        none_value_element=self.driver.find_elements_by_css_selector("#TableChart_1 div[class^='x']")[16]
        utillobj.asequal('None',none_value_element.text.strip(),'Step 15.4 : Verify Live Preview displaying "None" for each missing value')
        
        """
            Step 16 : Click on the 'Procedure Settings' button in the toolbar > Verify selections
        """
        ribbonobj.select_top_toolbar_item('toolbar_showfex_setting')
        
        """
            Step 16.1 : Verify Unchecked values
        """
        unchecked_row=['Collation Sequence','Summary Lines','Decimal Notation']
        for row in unchecked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','unchecked','Step 16.1 : Verify '+row+' is not selected')
        
        """
             Step 16.2 : Verify checked values
        """
        checked_row=['Missing Value','HTML Encode','Empty Report']
        for row in checked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','checked','Step 16.2 : Verify '+row+' is selected')
        
        """
            Step 16.3 : Verify default combobox values
        """
        combobox_row=['Collation Sequence','Summary Lines']
        expected_chombobox_values=['Code Page','New']
        for i in range(len(combobox_row)) :
            iaribbon.procedure_setting_dialogverify(combobox_row[i],'combobox',expected_chombobox_values[i],'Step 16.3 : Verify '+combobox_row[i]+' default value is '+expected_chombobox_values[i])
        
        """
            Step 16.4 : Verify Decimal Notation ON and OFF status 
        """
        iaribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','unchecked','Step 16.4 : Verify Decimal Notation ON is not selected',1)
        iaribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','checked','Step 16.4 : Verify Decimal Notation OFF is selected',2)
            
        """
            Step 16.5 : Verify HTML Encode ON and OFF status 
        """
        iaribbon.procedure_setting_dialogverify('HTML Encode','radiobutton','checked','Step 16.5 : Verify HTML Encode ON is selected',1)
        iaribbon.procedure_setting_dialogverify('HTML Encode','radiobutton','unchecked','Step 16.5 : Verify HTML Encode OFF is not selected',2)
        
        """
            Step 16.6 : Verify Empty Report ON and OFF status 
        """
        iaribbon.procedure_setting_dialogverify('Empty Report','radiobutton','checked','Step 16.7 : Verify Empty Report ON is selected',1)
        iaribbon.procedure_setting_dialogverify('Empty Report','radiobutton','unchecked','Step 16.5 : Verify Empty Report OFF is not selected',2)
        
        """
            Step 16.7 : Verify "Missing Value"  value
        """
        iaribbon.procedure_setting_dialogverify('Missing Value','textbox','None','Step 16.7 : Verify Missing None value')
        
        """
            Step 17 : Click Cancel
        """
        iaribbon.procedure_setting_dialog_dismiss('Cancel')
        
        """
            Step 18 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()