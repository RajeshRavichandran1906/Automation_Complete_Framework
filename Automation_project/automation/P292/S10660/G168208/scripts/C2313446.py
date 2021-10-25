'''
Created on DEC 15, 2017

@author: Sowmiya 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10660&group_by=cases:section_id&group_order=asc&group_id=168208
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2313446
TestCase Name = Verify Currency Formats displayed in the Field Tab ribbon, Define and Compute
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, define_compute
from common.lib.basetestcase import BaseTestCase

class C2313446_TestClass(BaseTestCase):

    def test_C2313446(self):
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver) 
        ia_resultobj= ia_resultarea.IA_Resultarea(self.driver)      
        define_obj=define_compute.Define_Compute(self.driver)
        
        """        
        Step 01:Launch Report Mode:
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        time.sleep(2)
        live_preview_page_css="#TableChart_1 div[style*='font-family']"
        utillobj.synchronize_with_visble_text(live_preview_page_css, 'Draganddropfieldsontothecanvasorintothequerypanetobeginbuildingyourreport.', 290)
        
        """        
        Step 02 : Add fields car, sales
        """
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(2)
        parent_css="#queryTreeWindow tr:nth-child(4) td"
        resobj.wait_for_property(parent_css, 1, expire_time=90)
        metaobj.datatree_field_click("SALES", 2, 1)
        time.sleep(2)
        parent_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(parent_css, 22, 290)

        """        
        Step 03 : Click on 'Sales' in the Live Preview 
        Step 04 : Click on the 'Change currency options' button in the Field Tab (Format group)
        Step 05 : Verify list of currency formats
        """
        ia_resultobj.select_field_on_canvas('TableChart_1', 2)
        ribbonobj.select_ribbon_item('Field', 'formatcurrency')
        time.sleep(5)
        list1=['Floating Currency','Non-floating Currency','Fixed Euro symbol','Floating Euro symbol','Euro symbol on the right','Fixed pound sterling sign','Floating pound sterling sign','Fixed Japanese yen symbol','Floating Japanese yen symbol','Fixed dollar sign','Floating dollar sign','Dollar sign on the right','Dollar sign on the left']
        utillobj.select_or_verify_bipop_menu(verify=True, expected_popup_list=list1, msg='Step 03:')
        
        """        
        Step 06 : Select Data Tab > Detail(Define)
        Step 07 : Click on the "Format" button 
        Step 08 : Click on 'Currency Symbol' dropdown box 
        Step 09 : Verify list of currency formats 
        Step 10 : Click Cancel > Cancel
        """
        define_obj.invoke_define_compute_dialog('define')
        utillobj.synchronize_with_visble_text('#btnFormat', 'Format', 190)
        format_css=driver.find_element_by_css_selector('#btnFormat')
        time.sleep(2)
        utillobj.default_left_click(object_locator=format_css)
        utillobj.synchronize_with_number_of_element("#currencySymbolCBox div[class$='combo-box-arrow']", 1, 30)
        combo_btn_elem=driver.find_element_by_css_selector("#currencySymbolCBox div[class$='combo-box-arrow']")
        utillobj.default_left_click(object_locator=combo_btn_elem)
        list1=['None','Floating Currency','Non-floating Currency','Fixed Euro symbol','Floating Euro symbol','Euro symbol on the right','Fixed pound sterling sign','Floating pound sterling sign','Fixed Japanese yen symbol','Floating Japanese yen symbol','Fixed dollar sign','Floating dollar sign','Dollar sign on the right','Dollar sign on the left']
        combo_css=('div[id*="BiList"] div[class^="bi-list-item"]')
        utillobj.select_or_verify_bipop_menu(custom_css=combo_css,expected_popup_list=list1,verify=True,msg='Step 04: ')
        time.sleep(5)
        close_elem=driver.find_element_by_css_selector('div[id="fmtDlgCancel"]')
        utillobj.default_left_click(object_locator=close_elem)
        close_button_elem=driver.find_element_by_css_selector('div[id="fldCreatorCancelBtn"]')
        utillobj.default_left_click(object_locator=close_button_elem)
        utillobj.synchronize_until_element_disappear("[id*='Dialog'] [class*='active']", 90)
        time.sleep(1)
        
        """        
        Step 11 : Select Data Tab > Summary(Compute)
        Step 12 : Click on the "Format" button
        Step 13 : Click on 'Currency Symbol' dropdown box
        Step 14 : Verify list of currency formats
        Step 15 : Click Cancel > Cancel
        """         
        define_obj.invoke_define_compute_dialog('compute')
        utillobj.synchronize_with_visble_text('#btnFormat', 'Format', 190)
        format_css=driver.find_element_by_css_selector('#btnFormat')
        time.sleep(2)
        utillobj.default_left_click(object_locator=format_css)
        utillobj.synchronize_with_number_of_element("#currencySymbolCBox div[class$='combo-box-arrow']", 1, 30)
        combo_btn_elem=driver.find_element_by_css_selector("#currencySymbolCBox div[class$='combo-box-arrow']")
        utillobj.default_left_click(object_locator=combo_btn_elem)
        list1=['None','Floating Currency','Non-floating Currency','Fixed Euro symbol','Floating Euro symbol','Euro symbol on the right','Fixed pound sterling sign','Floating pound sterling sign','Fixed Japanese yen symbol','Floating Japanese yen symbol','Fixed dollar sign','Floating dollar sign','Dollar sign on the right','Dollar sign on the left']
        combo_css=('div[id*="BiList"] div[class^="bi-list-item"]')
        utillobj.select_or_verify_bipop_menu(custom_css=combo_css,expected_popup_list=list1,verify=True,msg='Step 05: ')
        time.sleep(5)
        close_elem=driver.find_element_by_css_selector('div[id="fmtDlgCancel"]')
        utillobj.default_left_click(object_locator=close_elem)
        close_button_elem=driver.find_element_by_css_selector('div[id="fldCreatorCancelBtn"]')
        utillobj.default_left_click(object_locator=close_button_elem)
        utillobj.synchronize_until_element_disappear("[id*='Dialog'] [class*='active']", 90)
        
        """        
        Step 16 : Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
   
if __name__ == '__main__':
    unittest.main()