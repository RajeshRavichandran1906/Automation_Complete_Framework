'''
Created on Aug 20, 2019

@author: Niranjan

Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6156535
Test case Name : GIS_DISTANCE in Compute in Report
'''

import unittest
from common.lib import utillity
from common.wftools.report import Report
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.pages.define_compute import Define_Compute, DefineCompute

class C6156535_TestClass(BaseTestCase):

    def test_C6156535(self):
        
        """
        TESTCASE OBJECTS
        """
        reportobj = Report(self.driver)
        def_com_obj = Define_Compute(self.driver)
        definecom_obj = DefineCompute(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        
        """
        TESTCASE VARIABLES
        """        
        geographyexpand_css = '#functionsTree > div.bi-tree-view-body-content > table > tbody > tr:nth-child(11) > td > img.bi-tree-view-expand-icon'
        gis_distance_field_css = '#functionsTree > div.bi-tree-view-body-content > table > tbody > tr:nth-child(13)'
        
        '''
        Step 1 : Reopen the saved fex using API link
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S11397/G435147/C5917058_base.fex&tool=Report
        '''
        reportobj.edit_fex_using_api_url(fex_name = 'C5917058_base', folder_name='P292_S11397/G490496' )
        self.driver.set_page_load_timeout(100)
        reportobj.wait_for_visible_text('#TableChart_1', 'start')

        '''
        Step 2 : Click "Data tab" and Click "Summary (Compute)" option.
        '''
        def_com_obj.invoke_define_compute_dialog(calculation_type = 'compute')
        reportobj.wait_for_visible_text('#DataTab', 'Calculation')
        
        '''
        Step 3 : Click "Function (fx)" icon in Compute dialog.
        '''
        def_com_obj.select_menu_button_in_compute(menu_path = 'functions')
        reportobj.wait_for_visible_text('#functionsTree','Geography')
                 
        '''
        Step 4 : Expand "Geography" folder and Double click "GIS_DISTANCE".
        '''
        expand_obj = utillobj.validate_and_get_webdriver_object(geographyexpand_css, 'geography expand')
        core_utils.left_click(expand_obj)
        reportobj.wait_for_visible_text('#functionsTree', 'GIS_DISTANCE (geo_point1, geo_point2 )')
        gis_distance_field_obj = utillobj.validate_and_get_webdriver_object(gis_distance_field_css, 'field selection')
        core_utils.double_click(gis_distance_field_obj)
        
        '''
        Step 5 : Replace "geo_point1" with "start station GIS Point".
        Step 6 : Replace "geo_point2" with "end station GIS Point"
        Check the Expression area in Compute dialog.
        '''
        expected_expression = 'GIS_DISTANCE ("start station GIS Point", "end station GIS Point")'
        definecom_obj.enter_values_in_text_area(expected_expression)
        definecom_obj.verify_text_area_expression(expected_expression, '06.00')
      
        '''
        Step 7 : Enter "MILES" in Field text box and Click "OK" button.
        Check the Query pane and Live preview.
        '''
        definecom_obj.enter_values_in_field_textbox(value = 'MILES')
        definecom_obj.click_ok_button()
        reportobj.wait_for_visible_text('#TableChart_1', 'start')
#         reportobj.create_acrossreport_data_set_in_preview('TableChart_1',1,3, 10, 3,"C6156535_DS01.xlsx")
        reportobj.verify_across_report_data_set_in_preview('TableChart_1',1,3, 10, 3,"C6156535_DS01.xlsx", msg = 'Step 07.00 : Verify dataset')
        
        '''
        Step 8 : Click "IA" menu and Select "Save As" option.
        '''
        reportobj.select_visualization_application_menu_item('save_as')   
        reportobj.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")     
         
        '''
        Step 9 : Enter "C6156535" and Click "Save" button.
        '''
        reportobj.save_file_in_save_dialog('C6156535') 
                 
        '''
        Step 10 : Logout
        http://machine:port/alias/service/wf_security_logout.jsp
        '''
        reportobj.api_logout()        
         
        '''
        Step 11 : Run the saved fex from BIP using API
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P292_S11397/G435147&BIP_item=C6156535.fex
        
        Check the following Output.
        '''
        reportobj.run_fex_using_api_url(folder_name = 'P292_S11397/G490496', fex_name='C6156535', mrid='mrid', mrpass='mrpass')
        reportobj.wait_for_visible_text('table[summary="Summary"]', 'start')
#         reportobj.create_html_report_dataset("C6156535_DS02.xlsx" )
        reportobj.verify_html_report_dataset("C6156535_DS02.xlsx" , msg = "Step 11.00 : Verify the data set")
                                     
        '''
        Step 12 : Logout
        http://machine:port/alias/service/wf_security_logout.jsp
        '''
        
if __name__ == '__main__':
    unittest.main()