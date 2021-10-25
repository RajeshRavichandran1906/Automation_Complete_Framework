'''
Created on Apr 27, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5824543
TestCase Name = Verify SET commands default settings, syntax, save and restore
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea,ia_ribbon
from common.lib import utillity

class C5824543_TestClass(BaseTestCase):

    def test_C5824543(self):
        
        """   
        TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C5824543'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbon= ia_ribbon.IA_Ribbon(self.driver)
        iaresult= ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step 01 : Launch Report Mode: http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/car&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.invoke_infoassist_api_login('Report','ibisamp/car','P292_S10863/G432775', 'mrid', 'mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(3)
         
        """
        Step 02 : Click on the 'Procedure Settings' button in the toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_showfex_setting')
        time.sleep(3)
        
        """
        Step 03 : Verify default settings
        Step 03.1 : Verify default Unchecked values 
        """
        unchecked_row=['Collation Sequence','Summary Lines','Missing Value','Decimal Notation']
        for row in unchecked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','unchecked','Step 03.1 : Verify '+row+' is not selected as default')
        
        """
        Step 03.2 : Verify default checked values
        """
        checked_row=['HTML Encode','Empty Report']
        for row in checked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','checked','Step 03.2 : Verify '+row+' is selected as default')
        
        """
        Step 03.3 : Verify default combobox values
        """
        combobox_row=['Collation Sequence','Summary Lines']
        expected_chombobox_values=['Code Page','New']
        for i in range(len(combobox_row)) :
            iaribbon.procedure_setting_dialogverify(combobox_row[i],'combobox',expected_chombobox_values[i],'Step 03.3 : Verify '+combobox_row[i]+' default value is '+expected_chombobox_values[i])
        
        """
        Step 03.4 : Verify "Missing Value" default value
        """
        iaribbon.procedure_setting_dialogverify('Missing Value','textbox','.','Step 03.4 : Verify Missing Value default value')
        
        """
        Step 03.5 : Verify Decimal Notation ON and OFF status 
        """
        iaribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','unchecked','Step 03.5 : Verify Decimal Notation ON is not selected',1)
        iaribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','checked','Step 03.5 : Verify Decimal Notation OFF is selected',2)
            
        """
        Step 03.6 : Verify HTML Encode, Empty Report ON and OFF status 
        """
        for row in ['HTML Encode', 'Empty Report'] :
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','checked','Step 03.6 : Verify '+row+' ON is selected',1)
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','unchecked','Step 03.6 : Verify '+row+' OFF is not selected',2)
        """
        Step 04 : Click Cancel 
        """
        iaribbon.procedure_setting_dialog_dismiss('Cancel')
        time.sleep(2)
        
        """
        Step 05 : Click 'View Source' button in the toolbar
        Step 06 : Verify syntax for Settings enabled by default
        SET HTMLENCODE=ON
        SET EMPTYREPORT=ON
        Step 07 : Click OK
        """
        expected_syntax_list=["-DEFAULTH &WF_HTMLENCODE=ON;","SET HTMLENCODE=&WF_HTMLENCODE", "-DEFAULTH &WF_EMPTYREPORT=ON;","SET EMPTYREPORT=&WF_EMPTYREPOR"]
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 06.1 : Verify syntax for Settings enabled by default')
        
        """
        Step 08 : Click on the 'Procedure Settings' button in the toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_showfex_setting')
        
        """
        Step 09 : Check off 'Collation Sequence', 'Summary Lines' and 'Missing Value'
        """
        iaribbon.procedure_setting_dialog_input('Collation Sequence','checkbox','unchecked')
        iaribbon.procedure_setting_dialog_input('Summary Lines','checkbox','unchecked')
        iaribbon.procedure_setting_dialog_input('Missing Value','checkbox','unchecked')
        
        """
        Step 10 : Check off 'Decimal Notation' > Select 'On' radio button
        """
        iaribbon.procedure_setting_dialog_input('Decimal Notation','checkbox','unchecked')
        iaribbon.procedure_setting_dialog_input('Decimal Notation','radiobutton','unchecked')
        
        """
        Step 11 : Verify selections in dialog
        """
        checked_row=['Collation Sequence','Summary Lines','Missing Value','Decimal Notation','HTML Encode','Empty Report']
        for row in checked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','checked','Step 11.1 : Verify '+row+' is selected')
        
        """
        Step 11.2 : Verify combobox values
        """
        combobox_row=['Collation Sequence','Summary Lines']
        expected_chombobox_values=['Code Page','New']
        for i in range(len(combobox_row)) :
            iaribbon.procedure_setting_dialogverify(combobox_row[i],'combobox',expected_chombobox_values[i],'Step 11.2 : Verify '+combobox_row[i]+' value is '+expected_chombobox_values[i])
        
        """
        Step 11.3 : Verify "Missing Value" value
        """
        iaribbon.procedure_setting_dialogverify('Missing Value','textbox','.','Step 11.3 : Verify "Missing Value" value')
        
        """
        Step 11.4 : Verify Radio button ON 
        """
        radio_button_rows=['Decimal Notation','HTML Encode','Empty Report']
        for row in radio_button_rows :
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','checked','Step 11.4 : Verify '+row+' is ON',1)
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','unchecked','Step 11.4 : Verify '+row+' is OFF',2)
        iaribbon.procedure_setting_dialog_dismiss('OK')    
        
        """
        Step 12 : Click 'View Source' button in the toolbar > Verify Syntax
        Step 13 : Click OK
        """
        expected_syntax_list=["-DEFAULTH &WF_HTMLENCODE=ON;","SET HTMLENCODE=&WF_HTMLENCODE","-DEFAULTH &WF_EMPTYREPORT=ON;","SET EMPTYREPORT=&WF_EMPTYREPORT","-DEFAULTH &WF_COLLATION=CODEPAGE;","SET COLLATION=&WF_COLLATION","-DEFAULTH &WF_SUMMARYLINES=NEW;","SET SUMMARYLINES=&WF_SUMMARYLINES","-DEFAULTH &WF_NODATA='.';","SET NODATA='&WF_NODATA'","-DEFAULTH &WF_CDN=ON;","SET CDN=&WF_CDN"]
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 12.1 : Verify Syntax')
        
        """
        Step 14 : Add fields CAR, SALES 
        """
        metaobj.datatree_field_click('CAR',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,20,string_value='CAR')
        
        metaobj.datatree_field_click('SALES',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,20,string_value='SALES')
        
        """
        Step 15 : Drag COUNTRY into the Across bucket
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('COUNTRY', 1, 'Across', 0)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(7)", 1,20,string_value='COUNTRY')
        time.sleep(3)
        #iaresult.create_across_report_data_set('TableChart_1', 2, 6, 10, 6, Test_Case_ID+'_DataSet_01.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1', 2, 6, 10, 6, Test_Case_ID+'_DataSet_01.xlsx','Step 16.1 : Verify preview')
        
        """
        Step 16 : Click 'Save' in the toolbar > Save as > C2312991 > Click 'Save'
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
        Step 17 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
        Step 18 : Restore saved Fex: http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/S10660/C2312991.fex&tool=Report
        """
        utillobj.infoassist_api_edit_(Test_Case_ID, 'report', 'P292_S10863/G432775',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 1,60,string_value='COUNTRY')
        time.sleep(3)
        
        """
        Step 19 : Verify no errors are displayed in Live Preview 
        """
        iaresult.verify_across_report_data_set('TableChart_1', 2, 6, 10, 6, Test_Case_ID+'_DataSet_01.xlsx','Step 20.1 : Verify no errors are displayed in Live Preview')

        """
        Step 20 : Click on the 'Procedure Settings' button in the toolbar > Verify selections
        """
        ribbonobj.select_top_toolbar_item('toolbar_showfex_setting')
        time.sleep(2)
        checked_row=['Collation Sequence','Summary Lines','Missing Value','Decimal Notation','HTML Encode','Empty Report']
        for row in checked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','checked','Step 20.1 : Verify '+row+' is selected')
        
        """
        Step 20.2 : Verify combobox values
        """
        combobox_row=['Collation Sequence','Summary Lines']
        expected_chombobox_values=['Code Page','New']
        for i in range(len(combobox_row)) :
            iaribbon.procedure_setting_dialogverify(combobox_row[i],'combobox',expected_chombobox_values[i],'Step 20.2 : Verify '+combobox_row[i]+' value is '+expected_chombobox_values[i])
        
        """
        Step 20.3 : Verify "Missing Value" value
        """
        iaribbon.procedure_setting_dialogverify('Missing Value','textbox','.','Step 20.3 : Verify "Missing Value" value')
        
        """
        Step 20.4 : Verify Radio button ON 
        """
        radio_button_rows=['Decimal Notation','HTML Encode','Empty Report']
        for row in radio_button_rows :
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','checked','Step 20.4 : Verify '+row+' is ON',1)
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','unchecked','Step 20.4 : Verify '+row+' is OFF',2)
        
        """
        Step 21 : Click Cancel
        """
        iaribbon.procedure_setting_dialog_dismiss('Cancel')
        time.sleep(2)
        
        """
        Step 22 : Click 'View Source' button in the toolbar > Verify Syntax
        Step 23 : Click OK
        """
        expected_syntax_list=["-DEFAULTH &WF_HTMLENCODE=ON;","SET HTMLENCODE=&WF_HTMLENCODE","-DEFAULTH &WF_EMPTYREPORT=ON;","SET EMPTYREPORT=&WF_EMPTYREPORT","-DEFAULTH &WF_COLLATION=CODEPAGE;","SET COLLATION=&WF_COLLATION","-DEFAULTH &WF_SUMMARYLINES=NEW;","SET SUMMARYLINES=&WF_SUMMARYLINES","-DEFAULTH &WF_NODATA='.';","SET NODATA='&WF_NODATA'","-DEFAULTH &WF_CDN=ON;","SET CDN=&WF_CDN"]
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 23.1 : Verify Syntax')
        
        """
        Step 24 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()