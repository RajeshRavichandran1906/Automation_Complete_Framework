'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2321232
Test case Name =  Verify the expected qualified NAME is displayed while setting is "Use field titles" and MFD does not have titles
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon, define_compute, ia_run, wf_map
from common.lib import utillity 
import time, keyboard
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class C2321232_TestClass(BaseTestCase):

    def test_C2321232(self):
    
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser=utillobj.parseinitfile('browser')
        driver.implicitly_wait(15)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2321232"
        Test_fex_name="C2321232"

        
        """    1. Launch IA Report mode using car.mas,    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)  
          
        '''    2. Double click field "SALES"    '''
        metaobj.datatree_field_click("SALES", 2, 1)
        time.sleep(4)
        
        
        """    3. Select the Data Tab > Click "Detail(Define)"   """
        
        
        defcomp.invoke_define_compute_dialog('define')
        elem1="#fname"
        resultobj.wait_for_property(elem1, expected_number=1, expire_time=20)
        
        '''    4. Click on the "Additional Options" button, Verify "Use Field Titles" is displayed and selected by default,    '''
        '''    5. Double-click "COUNTRY", Verify Define text area displays the qualified NAME "CAR.ORIGIN.COUNTRY "    '''
        
        settings_btn=self.driver.find_element_by_css_selector("div[id='defineMetaData'] div[id^='BiToolBarMenuButton'] img[src*='settings']")
        
        utillobj.default_left_click(object_locator=settings_btn)
        
#         chkd_td="div[id^='BiPopup'] tr td[class='icon-column checkbox-checked']"
#         
#         utillobj.verify_object_visible(chkd_td, True, msg='Step 4. Verify use Field Ttiles is Checked')
        
        utillobj.select_or_verify_bipop_menu(verify='true', expected_popup_list=['Use field titles', 'Preserve null value', 'Missing Values'], expected_ticked_list=['Use field titles'], msg='Step 04:01 Verify popup menu')
        
        utillobj.default_left_click(object_locator=settings_btn)
        
#         chkd_td_el=self.driver.find_element_by_css_selector(chkd_td)
#         
#         utillobj.asequal(chkd_td_el.text(),"Use field titles", msg='Step 5. Verify use field titles is chceked')
        
        '''    '6. Expand "Product" Dimension > Double-click "Product,SubCategory"    '''
        '''    '7. Verify Define text area displays the field title "Product,SubCategory"    '''
        action = ActionChains(self.driver)
        data_field="COUNTRY"
        sf = self.driver.find_element_by_id("defineMetaData").find_element_by_id("metaDataSearchTxtFld")
        sf.click()
        time.sleep(2)
        sf.clear()
        time.sleep(2)
        keyboard.write(data_field, delay=1)
        time.sleep(2)
        lastxpath = "//div[starts-with(@id, 'defineMetaData')]//tr[*]/td[.='" + data_field + "']/img[2]"
        newelement = self.driver.find_element_by_xpath(lastxpath)
        newelement.click()
        if browser=='Firefox':
            utillity.UtillityMethods.click_type_using_pyautogui(self, newelement, doubleClick=True)
        else: 
            utillobj.click_on_screen(newelement, coordinate_type='middle', click_type=2)
        time.sleep(10)
        
        textarea=self.driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #fldCreatorSplitPane #ftext")
        txtele=textarea.get_attribute("value").strip()
        
        deftxt='CAR.ORIGIN.COUNTRY'
        
        utillobj.asequal(txtele,deftxt, 'Step 5. Verify Define Field Text in textarea')
        
        '''    '6. Change the Format to A50V > Click OK    '''
        type_format="A50V"
        field_format = self.driver.find_element_by_id("fformat")
        field_format.clear()
        field_format.send_keys(type_format)
        time.sleep(3)
        self.driver.find_element_by_id("fldCreatorOkBtn").click()
        time.sleep(5)
        
        '''   7. Double click on "Define_1" in data pane, Verify Data pane, Query pane, and Live Preview,    '''
        
        
        metaobj.datatree_field_click("Define_1", 2, 1)

        time.sleep(5)
        
        utillobj.verify_object_visible("#queryTreeColumn  table  tbody tr:nth-child(6)", True, msg='Verify Define in Query Pane')
        
        coln_list = ['Define_1', 'SALES']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 07: Verify the following report is displayed")
        
        '''    8. Click "Save" in the toolbar    '''
        '''    9. Save As "C2321232" > Click Save    '''

        time.sleep(5)
        
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        '''    10. Logout:    '''
        '''    11. Reopen the saved fex:    '''
        

        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10660_infoassist_2',mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        
        coln_list = ['Define_1', 'SALES']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 11: Verify Live preview titles")
        
        '''    12. Right-click "Define_1" in the Data pane > Edit...    '''
        '''    12.1 Verify field Title is displayed in the Text area    '''
        '''    13. Click Cancel    '''
        '''    14. Logout:    '''
        
        metaobj.datatree_field_click("Define_1", 1, 1, 'Edit...')
        
        resultobj.wait_for_property("div[id^='QbDialog']", expected_number=1, expire_time=20)
        
        utillobj.asequal(txtele,deftxt, 'Step 12.1 Verify Define Field Text in textarea')
        
        
        self.driver.find_element_by_id("fldCreatorCancelBtn").click()
        
        utillobj.infoassist_api_logout()

        
        
if __name__ == '__main__':
    unittest.main()
    
        