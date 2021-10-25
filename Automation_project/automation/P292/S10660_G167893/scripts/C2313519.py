'''
Created on DEC 15, 2017

@author: Pavithra 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313519&group_by=cases:section_id&group_id=168208&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/edit/2313519
TestCase Name = Edit Test Case
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea,ia_run
from common.lib.basetestcase import BaseTestCase

class C2313519_TestClass(BaseTestCase):

    def test_C2313519(self):
        
        Test_Case_ID = "C2313519"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver) 
        ia_resultobj= ia_resultarea.IA_Resultarea(self.driver)      
        runobj=ia_run.IA_Run(self.driver)
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
        parent_css="#queryTreeWindow tr:nth-child(3) td"
        resobj.wait_for_property(parent_css, 1, string_value='CostofGoods', with_regular_exprestion=True,expire_time=50)

        """
            Step 03:Click on 'Cost of Goods' in the Live Preview > Click on the "Decimal" dropdown box in the Field Tab Ribbon
        """
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,2,7,2,Test_Case_ID+'_DataSet_01.xlsx','Step 03: Verify report')
        ia_resultobj.select_field_on_canvas('TableChart_1', 2, click_type=0)
        time.sleep(5)
        ribbonobj.select_ribbon_item('Field', 'formattype', custom_css='div', opt="More options...")
        
        """
            Step 04:Select "More Options"
        """     
        parent_css="div[id^='QbDialog'] [class*='active ']>div[class*='window']>div[class='bi-label']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        time.sleep(6)

        """
            Step 05:Verify dialog
        """
        utillobj.verify_object_visible("[id^='QbDialog']", True, "Step 05: Verify save prompt appears")

        """
            Step 06:Click on the "Currency Symbol" dropdown box > Verify list of options
            
            Step 07:Select "Floating Euro symbol (!E)" > Click OK
        """
        combo_btn_elem=driver.find_element_by_css_selector("#currencySymbolCBox div[class$='combo-box-arrow']") 
        exp=['None', 'Floating Currency', 'Non-floating Currency', 'Fixed Euro symbol', 'Floating Euro symbol', 'Euro symbol on the right', 'Fixed pound sterling sign', 'Floating pound sterling sign', 'Fixed Japanese yen symbol', 'Floating Japanese yen symbol', 'Fixed dollar sign', 'Floating dollar sign', 'Dollar sign on the right', 'Dollar sign on the left']
        utillobj.select_any_combobox_item(combo_btn_elem, 'Floating Euro symbol', verify=True, expected_combobox_list=exp, msg="Step 07:")    
        dlgok=driver.find_element_by_id("fmtDlgOk")
        utillobj.default_left_click(object_locator=dlgok)
        """
            Step 08:Verify currency symbol in Live Preview
        """
        time.sleep(3)
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,2,7,2,Test_Case_ID+'_DataSet_02.xlsx','Step 08: Verify report')


        """
            Step 09:Click Run > Verify output

        """
        time.sleep(3)
        ribbonobj.select_top_toolbar_item("toolbar_run")
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(8)
        runobj.verify_table_data_set("table[summary='Summary']",  Test_Case_ID+'_DataSet_03.xlsx', "Step 09:verify data set")

        """
            Step 10:Click "Save" > Save As "C2313519" > Click Save
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
            Step 12:Restore saved Fex:http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Public/C2313519.fex&tool=Report

        """
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_infoassist_3',mrid='mrid', mrpass='mrpass')
        parent_css="#queryTreeWindow tr:nth-child(2) td"
        resobj.wait_for_property(parent_css, 1, string_value='Sum', with_regular_exprestion=True,expire_time=50)

        """
            Step 13:Verify Live Preview
        """
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,2,7,2,Test_Case_ID+'_DataSet_02.xlsx','Step 13: Verify report')

        """
            Step 14:Click on 'Cost of Goods' in the Live Preview > Click on the "Decimal" dropdown box in the Field Tab Ribbon
        """
        ia_resultobj.select_field_on_canvas('TableChart_1', 2, click_type=0)
        time.sleep(2)
        ribbonobj.select_ribbon_item('Field', 'formattype', custom_css='div', opt="More options...")
        parent_css="[id^='QbDialog'] [class*='active ']>div[class*='window']>div[class='bi-label']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        time.sleep(6)
        combo_btn_elem=driver.find_element_by_css_selector("#currencySymbolCBox div[class$='combo-box-arrow']")
        utillobj.default_left_click(object_locator=combo_btn_elem)

        """
            Step 15:Verify "Floating Euro symbol (!E)" appears selected

        """
        utillobj.verify_object_visible("div[id^='BiPopup'][style*='inherit'] div[id^='BiComboBoxItem'][class*='item-selected']", True, 'Step 15:Verify "Floating Euro symbol (!E)" appears selected')
        dlgok=driver.find_element_by_id("fmtDlgOk")
        utillobj.default_left_click(object_locator=dlgok)
        """
            Step 16:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main() 