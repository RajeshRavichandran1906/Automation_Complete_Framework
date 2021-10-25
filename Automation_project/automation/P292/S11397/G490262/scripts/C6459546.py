'''
Created on Aug 14, 2018

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6459546
Test case Name =  Verify field Titles in the Define dialog 
'''

import unittest
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, define_compute, metadata
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase

class C6459546_TestClass(BaseTestCase):

    def test_C6459546(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        metadataobj=metadata.MetaData(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C6459546"
        
        """    
        Step 1. http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S11397    
        """
        utillobj.invoke_infoassist_api_login('report','baseapp/wf_retail_lite','P292_S11397/G490262', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65) 
          
        '''    
        Step 2. Add fields "Product,Category" and "Cost of Goods"    
        '''
        metadataobj.collapse_data_field_section("Filters and Variables")
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(4)
        
        """    
        Step 3. Select the Data Tab > Click "Detail(Define)"    
        """
        defcomp.invoke_define_compute_dialog('define')
        elem1="#fname"
        resultobj.wait_for_property(elem1, expected_number=1, expire_time=20)
        
        '''    
        Step 4. Click on the "Additional Options" button
        Step 5. Verify "Use Field Titles" is displayed and selected by default    
        '''
        web_elements=self.driver.find_elements_by_css_selector("div[id='defineMetaData'] div[id^='BiToolBarSplitToggleMenuButton']")
        utillobj.verify_checked_class_property(web_elements[0], 'Step 4.1: Verify view_databusiness button is disabled', check_property=False)
        utillobj.verify_checked_class_property(web_elements[2], 'Step 4.2: Verify view_datatechnical button is enabled', check_property=True)
        time.sleep(5)
        settings_btn=self.driver.find_element_by_css_selector("div[id='defineMetaData'] div[id^='BiToolBarMenuButton'] img[src*='settings']")
        utillobj.default_left_click(object_locator=settings_btn)
        utillobj.select_or_verify_bipop_menu(verify='true', expected_popup_list=['Use field titles', 'Preserve null value', 'Missing Values'], expected_ticked_list=['Use field titles'], msg='Step 06:01 Verify popup menu')
        utillobj.default_left_click(object_locator=settings_btn)
        
        '''    
        Step 6. Expand "Product" Dimension > Double-click "Product,SubCategory"
        Step 7. Verify Define text area displays the field title "Product,SubCategory"    
        '''
        defcomp.select_define_compute_field("Product,Subcategory",1)
        time.sleep(10)
        textarea=self.driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #fldCreatorSplitPane #ftext")
        txtele=textarea.get_attribute("value").strip()
        deftxt='"Product,Subcategory"'
        utillobj.asequal(txtele,deftxt, 'Step 7. Verify Define Field Text in textarea')
        
        '''    
        Step 8. Change the Format to A50V > Click OK    
        '''
        type_format="A50V"
        field_format = self.driver.find_element_by_id("fformat")
        field_format.clear()
        field_format.send_keys(type_format)
        time.sleep(3)
        self.driver.find_element_by_id("fldCreatorOkBtn").click()
        time.sleep(5)
        
        '''    
        Step 9. Add "Define_1" to Query
        Step 10. Verify Data pane, Query pane, and Live Preview  
        '''
        metaobj.datatree_field_click("Dimensions->Product->Product->Define_1", 2, 1)
        time.sleep(5)
        metaobj.verify_data_pane_field('Model', 'Define_1', 1, "Step 10.1:")
        metaobj.verify_field_in_query_pane('By', 'Define_1', 2, "Step 10.2:")
        coln_list = ['ProductCategory', 'Define_1', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_1", coln_list, "Step 10.3: Verify the following report is displayed")
        
        '''    
        Step 11. Click "Save" in the toolbar
        Step 12. Save As "C6459546" > Click Save    
        '''
        time.sleep(5)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        '''    
        Step 13. Logout: 
        Step 14. Reopen the saved fex:
        Step 15. Verify Live Preview    
        '''
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit_(Test_Case_ID, 'report', 'P292_S11397/G490262',mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        coln_list = ['ProductCategory', 'Define_1', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_1", coln_list, "Step 15: Verify Live preview titles")
        
        '''    
        Step 16. Right-click "Define_1" in the Data pane > Edit...
        Step 17. Verify field Title is displayed in the Text area
        Step 18. Click Cancel
        Step 19. Logout:    
        '''
        metaobj.datatree_field_click("Dimensions->Product->Product->Define_1", 1, 1, 'Edit...')
        resultobj.wait_for_property("div[id^='QbDialog']", expected_number=1, expire_time=20)
        utillobj.asequal(txtele,deftxt, 'Step 17. Verify Define Field Text in textarea')
        self.driver.find_element_by_id("fldCreatorCancelBtn").click()
        time.sleep(6)
        utillobj.infoassist_api_logout()

        
        
if __name__ == '__main__':
    unittest.main()