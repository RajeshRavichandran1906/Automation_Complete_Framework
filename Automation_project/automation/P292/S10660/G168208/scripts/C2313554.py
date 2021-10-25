'''
Created on May 09, 2018

@author: Magesh 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/64295&group_by=cases:section_id&group_order=asc&group_id=167893
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313554
TestCase Name = Verify Currency Formats in Visualization Mode
'''

import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.lib.basetestcase import BaseTestCase

class C2313554_TestClass(BaseTestCase):

    def test_C2313554(self):
        
        Test_Case_ID = "C2313554"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver) 
        
        """        
        Step 01: Launch Visualization Mode:
        http://machine:port/ibi_apps/ia?tool=vis&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
  
        """
        Step 02: Add fields 'Product,Category' and 'Cost of Goods'
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 30)
          
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 30)
          
        """
        Step 03: Click on 'Cost of Goods' in the Query Pane > Click on the "Change currency options" button in the Field Tab Ribbon
        Step 04: Verify list of options
        Step 05: Select "Floating Euro symbol" 
        """
        metaobj.querytree_field_click("Cost of Goods",1)
        time.sleep(5)
        parent_css="#FieldFormatCurrency div[class$='drop-down-arrow']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        ribbonobj.select_ribbon_item('Field', 'formatcurrency')
        time.sleep(5)
        list1=['Floating Currency','Non-floating Currency','Fixed Euro symbol','Floating Euro symbol','Euro symbol on the right','Fixed pound sterling sign','Floating pound sterling sign','Fixed Japanese yen symbol','Floating Japanese yen symbol','Fixed dollar sign','Floating dollar sign','Dollar sign on the right','Dollar sign on the left']
        utillobj.select_or_verify_bipop_menu('Floating Euro symbol',verify=True,expected_popup_list=list1,msg='Step 05: ')
          
        """
        Step 06: Hover over "Computers" riser in the Live Preview > Verify the selected currency symbol is displayed in the tooltip
        """
        time.sleep(8)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 20)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 20)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 06:a(i) Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 06:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M','240M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 06:a(iii):Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 06.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 06.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Computers', 'Cost of Goods:\u20ac69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar, "Step 06.d: Verify bar value")
        time.sleep(5)
          
        """
        Step 07: Click Run 
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
          
        """
        Step 08: Hover over "Media Player" > Verify the selected currency symbol is displayed
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 20)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 20)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 08:a(i) Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 08:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M','240M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08:a(iii):Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:\u20ac190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar", bar, "Step 08.d: Verify bar value")
           
        """
        Step 09: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        parent_css="#applicationButton img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
          
        """
        Step 10: Click "Save" > Save As "C2313554" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
         
        """
        Step 11: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
             
        """
        Step 12: Restore saved Fex: http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Public/C2313554.fex&tool=vis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_infoassist_2',mrid='mrid',mrpass='mrpass')
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 30)
        
        """
        Step 13: Click on 'Cost of Goods' in the Query Pane > Click on the "Change currency options" button in the Field Tab Ribbon
        Step 14: Verify "Floating Euro symbol" appears selected
        Step 15: Select "Euro symbol on the right"
        """
        metaobj.querytree_field_click("Cost of Goods",1)
        parent_css="#FieldFormatCurrency div[class$='drop-down-arrow']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        ribbonobj.select_ribbon_item('Field', 'formatcurrency')
        time.sleep(5)
        list1=['Floating Currency','Non-floating Currency','Fixed Euro symbol','Floating Euro symbol','Euro symbol on the right','Fixed pound sterling sign','Floating pound sterling sign','Fixed Japanese yen symbol','Floating Japanese yen symbol','Fixed dollar sign','Floating dollar sign','Dollar sign on the right','Dollar sign on the left']
        utillobj.select_or_verify_bipop_menu('Euro symbol on the right', verify=True, expected_popup_list=list1, expected_ticked_list=['Floating Euro symbol'], msg='Step 15: ')
        
        """
        Step 16: Hover over "Accessories" riser > Verify selection is displayed
        """
        time.sleep(8)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 20)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 20)
        bar=['Product Category:Accessories', 'Cost of Goods:89,753,898.00\u20ac', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 16: Verify bar value")
        time.sleep(5)
        
        """
        Step 17: Click on the "Decimal" dropdown box in the Field Tab ribbon > Select "More options..."
        """
        ribbonobj.select_ribbon_item('Field', 'formattype')
        time.sleep(5)
        parent_css="div[id^='BiPopup'][style*='inherit']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        utillobj.select_or_verify_bipop_menu('More options...', custom_css="div[id^='BiComboBoxItem']")

        """        
        Step 18 : Verify "Euro symbol on the right" is the current selection in the "Currency Symbol" dropdown box
        Step 19 : Click on the "Currency Symbol" dropdown box > Verify list of options
        Step 20 : Select "Floating pound sterling sign" > Click OK
        """
        parent_css="div[id='fmtDlgOk']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        
        act_symbol_value = driver.find_element_by_css_selector("#currencySymbolCBox").text.strip()
        print(act_symbol_value)
        exp_symbol_value = 'Euro symbol on the right'
        utillobj.asequal(act_symbol_value, exp_symbol_value, "Step 18: Verify Euro symbol on the right is the current selection in the Currency Symbol dropdown box")
        
        combo_btn_elem=driver.find_element_by_css_selector("#currencySymbolCBox div[class$='combo-box-arrow']")
        utillobj.default_left_click(object_locator=combo_btn_elem)
        list1=['None','Floating Currency','Non-floating Currency','Fixed Euro symbol','Floating Euro symbol','Euro symbol on the right','Fixed pound sterling sign','Floating pound sterling sign','Fixed Japanese yen symbol','Floating Japanese yen symbol','Fixed dollar sign','Floating dollar sign','Dollar sign on the right','Dollar sign on the left']
        parent_css="div[id^='BiPopup'][style*='inherit']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        utillobj.select_or_verify_bipop_menu('Floating pound sterling sign',expected_popup_list=list1,verify=True,msg='Step 20: ',custom_css="div[id^='BiComboBoxItem']")
        time.sleep(5)
        close_elem=driver.find_element_by_css_selector('div[id="fmtDlgOk"]')
        utillobj.default_left_click(object_locator=close_elem)
        time.sleep(5)
        
        """
        Step 21: Hover over "Camcorder" riser > Verify selected currency format is displayed in the tooltip
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 20)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 20)
        bar=['Product Category:Camcorder', 'Cost of Goods:\u00a3104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar", bar, "Step 21: Verify bar value")
        time.sleep(5)
        
        """
        Step 22: Click "Save" in the toolbar > OK
        """
        ribbonobj.select_top_toolbar_item('infomini_save')
        parent_css="div[id^='BiDialog']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
        time.sleep(5)
        
        """        
        Step 23: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
   
if __name__ == '__main__':
    unittest.main()