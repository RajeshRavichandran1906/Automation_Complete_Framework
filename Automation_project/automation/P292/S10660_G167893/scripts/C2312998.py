'''
Created on December 18, 2017

@author: PM14587
Testcase Name : Verify SET commands are carried over when promoting Report to Document mode
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2312998
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea,ia_ribbon,ia_run,active_miscelaneous
from common.lib import utillity

class C2312998_TestClass(BaseTestCase):

    def test_C2312998(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2312998'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbon= ia_ribbon.IA_Ribbon(self.driver)
        iaresult= ia_resultarea.IA_Resultarea(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        def verify_procedure_settings(msg_step):
            
            #Verify checked values
            checked_row=['Collation Sequence','Summary Lines','Missing Value','Decimal Notation','HTML Encode','Empty Report']
            for row in checked_row :
                iaribbon.procedure_setting_dialogverify(row,'checkbox','checked','Step '+msg_step+'.1 : Verify '+row+' is selected')
            
            #Verify combobox values
            combobox_row=['Collation Sequence','Summary Lines']
            expected_chombobox_values=['Case Sensitive','Explicit']
            for i in range(len(combobox_row)) :
                iaribbon.procedure_setting_dialogverify(combobox_row[i],'combobox',expected_chombobox_values[i],'Step '+msg_step+'.2 : Verify '+combobox_row[i]+' value is '+expected_chombobox_values[i])
            
            #Verify Missing Value text value
            iaribbon.procedure_setting_dialogverify('Missing Value','textbox','no val','Step '+msg_step+'.3 : Verify "Missing Value" value')
            
            #Verify Radio button status
            radio_button_rows=['Decimal Notation','HTML Encode','Empty Report']
            for row in radio_button_rows :
                iaribbon.procedure_setting_dialogverify(row,'radiobutton','checked','Step '+msg_step+'.4 : Verify '+row+' is ON',1)
                iaribbon.procedure_setting_dialogverify(row,'radiobutton','unchecked','Step '+msg_step+'.4 : Verify '+row+' is OFF',2)
        
        
        """
            Step 01 : Launch Report Mode: http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/car&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('Report','ibisamp/car','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(3)
         
        """
            Step 02 : Add fields CAR, SALES 
        """
        metaobj.datatree_field_click('CAR',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,20,string_value='CAR')
        
        metaobj.datatree_field_click('SALES',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,20,string_value='SALES')
        
        """
            Step 03 : Drag COUNTRY into the Across bucket
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('COUNTRY', 1, 'Across', 0)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(7)", 1,20,string_value='COUNTRY')
        time.sleep(3)
        
        """
            Step 04 : Click on the 'Procedure Settings' button in the toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_showfex_setting')
        time.sleep(3)
        
        """
            Step 05 : Verify default settings
            Step 05.1 : Verify default Unchecked values 
        """
        unchecked_row=['Collation Sequence','Summary Lines','Missing Value','Decimal Notation']
        for row in unchecked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','unchecked','Step 05.1 : Verify '+row+' is not selected as default')
        
        """
             Step 05.2 : Verify default checked values
        """
        checked_row=['HTML Encode','Empty Report']
        for row in checked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','checked','Step 05.2 : Verify '+row+' is selected as default')
        
        """
            Step 05.3 : Verify default combobox values
        """
        combobox_row=['Collation Sequence','Summary Lines']
        expected_chombobox_values=['Code Page','New']
        for i in range(len(combobox_row)) :
            iaribbon.procedure_setting_dialogverify(combobox_row[i],'combobox',expected_chombobox_values[i],'Step 05.3 : Verify '+combobox_row[i]+' default value is '+expected_chombobox_values[i])
        
        """
            Step 05.4 : Verify "Missing Value" default value
        """
        iaribbon.procedure_setting_dialogverify('Missing Value','textbox','.','Step 05.4 : Verify Missing Value default value')
        
        """
            Step 05.5 : Verify Decimal Notation ON and OFF status 
        """
        iaribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','unchecked','Step 05.5 : Verify Decimal Notation ON is not selected',1)
        iaribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','checked','Step 05.5 : Verify Decimal Notation OFF is selected',2)
            
        """
            Step 05.6 : Verify HTML Encode ON and OFF status 
        """
        for row in ['HTML Encode', 'Empty Report'] :
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','checked','Step 05.6 : Verify '+row+' ON is selected',1)
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','unchecked','Step 05.6 : Verify '+row+' OFF is not selected',2)
        
        """
            Step 06 : Check off 'Collation Sequence' > Verify drop menu 
            Step 07 : Select "Case Sensitive"
        """
        expected_items=['Code Page', 'Binary', 'Case Insensitive', 'Case Sensitive']
        iaribbon.procedure_setting_dialog_input('Collation Sequence','checkbox','unchecked')
        iaribbon.procedure_setting_dialog_input('Collation Sequence','combobox','Case Sensitive',verify=True,expected_combobox_list=expected_items,msg='Step 06.1 : Verify Collation Sequence drop menu')
        
        """
            Step 08 : Check off 'Summary Lines' > Verify drop menu
            Step 09 : Select "Explicit"
        """
        expected_items=['New', 'Old', 'Explicit']
        iaribbon.procedure_setting_dialog_input('Summary Lines','checkbox','unchecked')
        iaribbon.procedure_setting_dialog_input('Summary Lines','combobox','Explicit',verify=True,expected_combobox_list=expected_items,msg='Step 08.1 : Verify Summary Lines drop menu')
        time.sleep(4)
        
        """
            Step 10 : Check off 'Missing Value' > Type no val
        """
        iaribbon.procedure_setting_dialog_input('Missing Value','checkbox','unchecked')
        iaribbon.procedure_setting_dialog_input('Missing Value','textbox','no val')
        
        """
            Step 11 : Check off 'Decimal Notation' > Select 'On' radio button
        """
        iaribbon.procedure_setting_dialog_input('Decimal Notation','checkbox','unchecked')
        iaribbon.procedure_setting_dialog_input('Decimal Notation','radiobutton','unchecked')
        
        """
            Step 12 : Verify selections in dialog > Click OK
        """
        verify_procedure_settings('12')
        iaribbon.procedure_setting_dialog_dismiss('OK')    
        time.sleep(4)
        
        """
            Step 13 : Verify Preview
        """
        #iaresult.create_across_report_data_set('TableChart_1', 2, 6, 10, 6, Test_Case_ID+'_DataSet_01.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1', 2, 6, 10, 6, Test_Case_ID+'_DataSet_01.xlsx','Step 13.1 : Verify preview')
        
        """
            Step 14 : Click "Document" in the Home Tab ribbon
        """
        ribbonobj.select_ribbon_item('Home', 'document')
        resultobj.wait_for_property("#canvasContainer #TableChart_1 div[class^='x']", 1,20,string_value='COUNTRY')
        
        """
            Step 15 : Verify Document Canvas
        """
        iaresult.verify_across_report_data_set('canvasContainer #TableChart_1', 2, 6, 10, 6, Test_Case_ID+'_DataSet_01.xlsx','Step 15.1 : Verify Document Canvas')
        
        """
            Step 16 : Click on the 'Procedure Settings' button in the toolbar > Verify selections made in Report mode are carried over to Document mode.
        """
        ribbonobj.select_top_toolbar_item('toolbar_showfex_setting')
        time.sleep(3)
        verify_procedure_settings('16')
        
        """
            Step 17 : Click Cancel
        """
        iaribbon.procedure_setting_dialog_dismiss('Cancel')    
        
        """
            Step 18 : Click Run 
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("#ITableData0 tr:nth-child(1)>td span", 1,20,string_value='COUNTRY')
        
        """
            Step 18.1 : Verify output with "no val" for missing values
        """
        #iarun.create_table_data_set("#ITableData0",Test_Case_ID+'_DataSet_02.xlsx')
        iarun.verify_table_data_set("#ITableData0",Test_Case_ID+'_DataSet_02.xlsx',"Step 18.1 : Verify output with 'no val' for missing values")
        active.verify_page_summary(0,'10of10records,Page1of1', 'Step 18.2 : Verify docuemnt report page summary')

        """
            Step 19 : Save the Document fex: Click 'Save' in the toolbar > Save as > C2312998 > Click 'Save'
        """
        utillobj.switch_to_default_content(3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 20 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 21 : Restore saved Fex: http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Public/C2312998.fex&tool=Document
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'Document', 'S10660_infoassist_2',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#canvasContainer #TableChart_1 div[class^='x']", 1,20,string_value='COUNTRY')
        time.sleep(2)
        
        """
            Step 22 : Verify Document Canvas
        """
        iaresult.verify_across_report_data_set('canvasContainer #TableChart_1', 2, 6, 10, 6, Test_Case_ID+'_DataSet_01.xlsx','Step 15.1 : Verify Document Canvas')
        
        """
            Step 23 : Click on the 'Procedure Settings' button in the toolbar > Verify selections
        """
        ribbonobj.select_top_toolbar_item('toolbar_showfex_setting')
        time.sleep(3)
        verify_procedure_settings('23')
        
        """
            Step 24 : Click Cancel
        """
        iaribbon.procedure_setting_dialog_dismiss('Cancel')    
        time.sleep(2)
        
        """
            Step 25 : Click 'View Source' button in the toolbar > Verify Syntax
            Step 26 : Click Ok
        """
        expected_syntax_list=["SET ARGRAPHENGINE=JSCHART", "-DEFAULTH &WF_EMPTYREPORT=ON;", "SET EMPTYREPORT=&WF_EMPTYREPORT", "-DEFAULTH &WF_COLLATION=SRV_CS;", "SET COLLATION=&WF_COLLATION", "-DEFAULTH &WF_SUMMARYLINES=EXPLICIT;", "SET SUMMARYLINES=&WF_SUMMARYLINES", "-DEFAULTH &WF_NODATA='no val';", "SET NODATA=&WF_NODATA", "-DEFAULTH &WF_CDN=ON;", "SET CDN=&WF_CDN"]
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 25.1 : Verify Syntax')
        
        """
            Step 27 : Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()