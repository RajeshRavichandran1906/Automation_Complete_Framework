'''
Created on DEC 15, 2017

@author: Pavithra 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313519&group_by=cases:section_id&group_id=168208&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2316513
TestCase Name = Edit Test Case
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea,ia_run,ia_ribbon
from common.lib.basetestcase import BaseTestCase

class C2313528_TestClass(BaseTestCase):

    def test_C2313528(self):
        
        Test_Case_ID = "C2313528"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver) 
        ia_resultobj= ia_resultarea.IA_Resultarea(self.driver)      
        runobj=ia_run.IA_Run(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """        
        Step 01:Launch Report Mode:
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        parent_css="div[align='justify']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        time.sleep(6)

        """
        Step 02:Add fields 'Product,Category' and 'Cost of Goods'
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(4) td"
        resobj.wait_for_property(parent_css, 1, string_value='Product,Category', with_regular_exprestion=True,expire_time=50)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(parent_css, 18, 290)

        """
        Step 03:Click on 'Cost of Goods' in the Live Preview
        """
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 2, 7, 2, Test_Case_ID+'_DataSet_01.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,2,7,2,Test_Case_ID+'_DataSet_01.xlsx','Step 03: Verify report')

        """
        Step 04:Click on the "Change currency options" button in the Field Tab Ribbon > Select "Floating Euro symbol (!E)"
        """
        ia_resultobj.select_field_on_canvas('TableChart_1', 2, click_type=0)
        time.sleep(5)
        metaobj.querytree_field_click("Cost of Goods",1,)
        parent_css="#FieldFormatCurrency div[class$='drop-down-arrow']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        time.sleep(5)
        combo_btn_elem=driver.find_element_by_css_selector("#FieldFormatCurrency div[class$='drop-down-arrow']") 
        utillobj.default_left_click(object_locator=combo_btn_elem)
        utillobj.select_or_verify_bipop_menu('Floating Euro symbol')
        data_euro_css="div[class^='x']:nth-child(16)"
        utillobj.synchronize_with_visble_text(data_euro_css, '\u20AC104,866,857.00', 90)
        
        """
        Step 05:Verify currency symbol in Live Preview
        """
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 2, 7, 2, Test_Case_ID+'_DataSet_02.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,2,7,2,Test_Case_ID+'_DataSet_02.xlsx','Step 05: Verify report')

        """
        Step 06:Click on the "Procedure Settings" icon in the toolbar
        """
        ribbonobj.select_top_toolbar_item("toolbar_showfex_setting")
        
        """
        Step 07:Check off "Decimal Notation" option > Select "On" radio button > Click OK
        """
        ia_ribbobj.procedure_setting_dialog_input("Decimal Notation", "checkbox", "unchecked")
        ia_ribbobj.procedure_setting_dialog_input("Decimal Notation", "radiobutton", "unchecked")
        ia_ribbobj.procedure_setting_dialog_dismiss(button_name='OK')
        time.sleep(4)
        utillobj.synchronize_with_visble_text(data_euro_css, '\u20AC104.866.857,00', 90)
        
        """
        Step 08:Verify change in Live Preview
        """
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 2, 7, 2, Test_Case_ID+'_DataSet_03.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,2,7,2,Test_Case_ID+'_DataSet_03.xlsx','Step 08: Verify report')
 
        """
        Step 09:Run > Verify output
        """
        time.sleep(3)
        ribbonobj.select_top_toolbar_item("toolbar_run")
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(8)
#         runobj.create_table_data_set("table[summary='Summary']", Test_Case_ID+'_DataSet_04.xlsx')
        runobj.verify_table_data_set("table[summary='Summary']",  Test_Case_ID+'_DataSet_04.xlsx', "Step 09:verify data set")

        """
        Step 10:Click "Save" > Save As "C2313528" > Click Save
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(4)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)

        """
        Step 11:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
        Step 12:Restore saved Fex:http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Public/C2313528.fex&tool=Report
        """
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_infoassist_3',mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text(data_euro_css, '\u20AC104.866.857,00', 290)
        
        """
        Step 13:Verify Live Preview
        """
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,2,7,2,Test_Case_ID+'_DataSet_03.xlsx','Step 13: Verify report')

        """
        Step 14:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main() 