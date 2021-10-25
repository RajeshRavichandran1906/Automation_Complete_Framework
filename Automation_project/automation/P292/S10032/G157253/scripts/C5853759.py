'''
Created on Jun 26, 2018

@author: Magesh

TestCase Name : Verify Search field and double click
TestCase ID :http://172.19.2.180/testrail/index.php?/cases/view/5853759
'''

import unittest, time, keyboard
from common.pages import visualization_metadata 
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver import ActionChains

class C5853759_TestClass(BaseTestCase):
    
    def test_C5853759(self):
        Test_Case_ID = "C5853759"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        def datatree_click(field_name, position):
            action = ActionChains(driver)
            row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] td[class='']"
            try:
                l=[el for el in driver.find_elements_by_css_selector(row_css) if el.text.strip().replace(' ','')==field_name.replace(' ','')]
                l[position-1].find_element_by_css_selector("img[class='icon']").click()
            except:
                print("except")
                l=[el for el in driver.find_elements_by_css_selector(row_css) if el.text.strip().replace(' ','')==field_name.replace(' ','')]
                l[position-1].find_element_by_css_selector("img[class='icon']").click()
            time.sleep(2)
            row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected'] img[class='icon']"
            newelement = driver.find_element_by_css_selector(row_css)
            browser=utillobj.parseinitfile('browser')
            if browser == 'Firefox':
                utillobj.click_on_screen(newelement, coordinate_type='middle',x_offset=20,click_type=2)
                time.sleep(2)
            else:
                action.double_click(newelement).perform()
            time.sleep(6)
            
        """
        Step 02: Launch IA Report mode:
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 02: Click on the "Search" input box in the Data pane
        Step 03: Type prod > Verify list displayed
        """
        element = driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
        element.click()
        time.sleep(3)
        field_name = 'prod'
        keyboard.write(field_name,delay=1)
        time.sleep(3)
        exp_val_list=['Product Filter', 'Product,Category', 'Product,Subcategory', 'Product,Cost', 'Product,Description', 'Product Name', 'Product,Weight', 'Product,Weight,Units', '']
        field_items=driver.find_elements_by_css_selector("div[id^='QbMetaDataTree'] .bi-tree-view-table tr")
        act_val_list = [el.text.strip() for el in field_items]
        utillobj.as_List_equal(exp_val_list, act_val_list, 'step03: Verify list displayed')
        time.sleep(3)
        
        """
        Step 04: Double click "Product,Category"
        """
        datatree_click('Product,Category', 1)
        time.sleep(3)
        
        """
        Step 05: Verify "Product,Category" is displayed in the Query and Live Preview
        """
        metaobj.verify_query_pane_field('By', 'Product,Category', 1, "Step 05:01:")
        expected_list=['Product', 'Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        preview_items = driver.find_elements_by_css_selector("#TableChart_1 div[class^='x']")
        actual_list = [i.text.strip() for i in preview_items]
        utillobj.as_List_equal(expected_list, actual_list, 'step05.2: Verify Live Preview')
        time.sleep(3)
        
        """
        Step 06: Click on the x icon in the Search input box
        """
        cancel_icon = driver.find_element_by_css_selector("#iaMetaDataBrowser [class='bi-tool-bar-button text-field'] img[src*='search_cancel']")
        browser=utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillobj.click_on_screen(cancel_icon, coordinate_type='middle',click_type=0)
        else:
            cancel_icon.click()
        time.sleep(6)
        
        """
        Step 07: Verify Data pane is resetted
        """
        metaobj.verify_data_pane_field('Query Variables', 'Measures', 1, "Step 07.1:")
        metaobj.verify_data_pane_field('Query Variables', 'Sales', 2, "Step 07.2:")
        metaobj.verify_data_pane_field('Query Variables', 'Shipments', 3, "Step 07.3:")
        metaobj.verify_data_pane_field('Query Variables', 'Dimensions', 4, "Step 07.4:")
        metaobj.verify_data_pane_field('Query Variables', 'Sales_Related', 5, "Step 07.5:")
        metaobj.verify_data_pane_field('Query Variables', 'Product', 6, "Step 07.6:")
        metaobj.verify_data_pane_field('Query Variables', 'Shipments_Related', 7, "Step 07.7:")
        metaobj.verify_data_pane_field('Query Variables', 'Store', 8, "Step 07.8:")
        metaobj.verify_data_pane_field('Query Variables', 'Customer', 9, "Step 07.9:")
        
        """
        Step 08: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
    
if __name__ == '__main__':
    unittest.main()