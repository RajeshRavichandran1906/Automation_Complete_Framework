'''
Created on Jan 02, 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348942
Test_Case Name : Renaming group value name doesn't accept existing name
'''
import unittest,time
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea
from common.lib import utillity
import pyautogui

class C2348942_TestClass(BaseTestCase):

    def test_C2348942(self):
        
        """   
            TESTCASE VARIABLES 
        """
       
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        br_type = UtillityMethods.parseinitfile(self,'browser')
     
        
        '''    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
        '''  http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=empdata  '''
   
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_paperclipping_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 svg text", 'Drop Measures or Sorts into the Query Pane', 60, pause_time=2)
       
        '''    Step 2. Double click to add "Cost of Goods" and "Product, Category"    '''
        
        metadata.datatree_field_click('Cost of Goods', 2, 1)
        parent_css="#resultArea .chartPanel .yaxis-title"
        utillobj.synchronize_with_visble_text(parent_css, 'Cost of Goods', 35, 2)
        metadata.datatree_field_click('Product,Category', 2, 1)
        parent_css="#resultArea .chartPanel .xaxisOrdinal-title"
        utillobj.synchronize_with_visble_text(parent_css, 'Product Category', 35, 2)
        
        '''    Step 3. Lasso on First two risers (Accessories, Camcorder)    '''
        #visul_result.create_lasso('MAINTABLE_wbody1', 'rect', 'riser!s0!g0!mbar!',target_tag='rect', target_riser='riser!s0!g5!mbar!')
        visul_result.create_lasso('MAINTABLE_wbody1', 'rect', 'riser!s0!g0!mbar!', target_tag='rect', target_riser='riser!s0!g1!mbar!')
        
        time.sleep(5)
        '''    Step 4. Select "Group Product, Category selection"    '''
        visul_result.select_or_verify_lasso_filter(select="Group Product,Category Selection", msg='Step 4. Click on the Group selection')
        
        '''    Step 4.1 Verify following chart with group created    '''
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='PRODUCT_CATEGORY_1')
        
        xaxis_value="PRODUCT_CATEGORY_1"
        yaxis_value="Cost of Goods"
        parentcss="MAINTABLE_wbody1_f"
        visul_result.verify_xaxis_title(parentcss, xaxis_value, "Step 04:a(i) Verify X-Axis Title")
        visul_result.verify_yaxis_title(parentcss, yaxis_value, "Step 04:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visul_result.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, "Step 04:c(iii):Verify XY labels")
        visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 6, 'Step 4d. Verify no of risers')
        
        '''    Step 5. Click on grouped riser (Accessories and Camcorder), Expected to see following tool tip values    '''
        riser1_ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g0!mbar!']")
        
        utillobj.click_on_screen(riser1_ele, coordinate_type='middle', click_type=0)
        
        expected_tooltip_list=['1 item selected', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename Accessories and Camcorder...', 'Ungroup Accessories and Camcorder...', 'Ungroup All']
        
        visul_result.select_or_verify_lasso_filter(verify=expected_tooltip_list, msg='Step 5. Verify tooltip values')
        
        '''    Step 6. Click "Rename Accessories and Camcorder    '''
        
        visul_result.select_or_verify_lasso_filter(select="Rename Accessories and Camcorder...", msg='Step 6. Click on Rename Accessories and Camcorder...')
        time.sleep(2)
        
        '''    Step 7. Add empty spaces to existing text at the beginning in rename dialog, OK button still disabled    '''
        
        element_css="div[id^='BiDialog'] [class*='window-active']"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=20)
        edit_title_obj=self.driver.find_element_by_css_selector(element_css)
        edit_title_obj.find_element_by_css_selector("input").click()
        pyautogui.hotkey('home')
        time.sleep(2)
        pyautogui.typewrite("    ")
        time.sleep(5)
        dialog_css="div[id^='BiDialog'] [class*='window-active']" + " div[id^='BiButton']"
        dialog_btns=self.driver.find_elements_by_css_selector(dialog_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        class_status=dialog_btns[btn_text_list.index("OK")].get_attribute('class')
        
        if "button-disabled" in class_status:
            status=True
        else:
            status=False
        utillobj.asequal(True,status,'Step 7. Verify OK button is disabled with empty spaces before def text')
        
        '''    '8. Add empty spaces to existing text at the end in rename dialog, OK button still disabled    '''
        
        edit_title_obj.find_element_by_css_selector("input").click()
        pyautogui.hotkey('end')
        time.sleep(2)
        pyautogui.typewrite("    ")
        time.sleep(5)
        dialog_css="div[id^='BiDialog'] [class*='window-active']" + " div[id^='BiButton']"
        dialog_btns=self.driver.find_elements_by_css_selector(dialog_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        class_status=dialog_btns[btn_text_list.index("OK")].get_attribute('class')
        
        if "button-disabled" in class_status:
            status=True
        else:
            status=False
        utillobj.asequal(True,status,'Step 8. Verify OK button is still disabled')
        
        
        
        '''    Step 9. Click Cancel, Expected to no change on group value name    '''
        
        utillobj.click_dialog_button("div[id^='BiDialog']", "Cancel")
        
        expected_xval_list=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visul_result.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, "Step 9 :Verify XY labels")
        visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 6, 'Step 9. Verify no of risers')
        
        '''    Step 10. Logout using API (without saving)    '''
        
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()