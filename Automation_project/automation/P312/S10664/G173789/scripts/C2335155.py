'''
Created on Jan 02, 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2335155
Test_Case Name : Renaming group value name doesn't accept existing name
'''
import unittest,time
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea
from common.lib import utillity

class C2335155_TestClass(BaseTestCase):

    def test_C2335155(self):
        
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
        visul_result.wait_for_property("#pfjTableChart_1 svg text", 1, 120, string_value='DropMeasuresorSortsintotheQueryPane', with_regular_exprestion=True)
        time.sleep(3)
        
       
        '''    Step 2. Double click to add "Cost of Goods" and "Product, Category"    '''
    
        metadata.datatree_field_click('Cost of Goods', 2, 1)
        parent_css="#resultArea .chartPanel .yaxis-title"
        utillobj.synchronize_with_visble_text(parent_css, 'Cost of Goods', 35, 2)
        metadata.datatree_field_click('Product,Category', 2, 1)
        parent_css="#resultArea .chartPanel .xaxisOrdinal-title"
        utillobj.synchronize_with_visble_text(parent_css, 'Product Category', 35, 2)
        
        '''    Step 3. Lasso on First three riser (Accessories, Camcorder, Computers)    '''
        #visul_result.create_lasso('MAINTABLE_wbody1', 'rect', 'riser!s0!g0!mbar!',target_tag='rect', target_riser='riser!s0!g5!mbar!')
        visul_result.create_lasso('MAINTABLE_wbody1', 'rect', 'riser!s0!g0!mbar!', target_tag='rect', target_riser='riser!s0!g2!mbar!')        
        time.sleep(5)
        
        '''    Step 4. Select "Group Product, Category selection"    '''
        visul_result.select_or_verify_lasso_filter(select="Group Product,Category Selection", msg='Step 4. Click on the Group selection')
        
        '''    Step 5. Verify following chart with group created    '''
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='PRODUCT_CATEGORY_1')  
        xaxis_value="PRODUCT_CATEGORY_1"
        yaxis_value="Cost of Goods"
        parentcss="MAINTABLE_wbody1_f"
        visul_result.verify_xaxis_title(parentcss, xaxis_value, "Step 05:a(i) Verify X-Axis Title")
        visul_result.verify_yaxis_title(parentcss, yaxis_value, "Step 05:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories and Camcorder and Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M']
        visul_result.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, "Step 05:c(iii):Verify XY labels")
        visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 5, 'Step 5d. Verify no of risers')
        
        '''    Step 6. Click on grouped riser (Accessories and Camcorder and Computers)    '''
        riser1_ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g0!mbar!']")
        utillobj.click_on_screen(riser1_ele, coordinate_type='middle')
        time.sleep(1)
        utillobj.click_on_screen(riser1_ele, coordinate_type='middle', click_type=0)
        time.sleep(3)
        
        '''    Step 7. Click "Rename Accessories and Camcorder..."    '''
        
        visul_result.select_or_verify_lasso_filter(select="Rename Accessories and Camcorder...", msg='Step 6. Click on Rename Accessories and Camcorder...')
        time.sleep(3)
        
        '''    Step 8. Verify following text box populated, Expected to see Rename Value text box and OK button disabled by default    '''
        
#         btn_css = "div[id^='BiDialog'] [class*='window-active']"
    
        def_name= 'Accessories and Camcorder and Computers'
        print("----------------------------------")
#         visul_result.wait_for_property(self, btn_css, 1)
        element_css="div[id^='BiDialog'] [class*='window-active']"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=20)
        edit_title_obj=self.driver.find_element_by_css_selector(element_css)
        actual_name=edit_title_obj.find_element_by_css_selector("input").get_attribute('value')
        utillobj.asequal(actual_name, def_name, "Step 8. Verify current name.")
        time.sleep(3)
        
        dialog_css="div[id^='BiDialog'] [class*='window-active']" + " div[id^='BiButton']"
        dialog_btns=self.driver.find_elements_by_css_selector(dialog_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        class_status=dialog_btns[btn_text_list.index("OK")].get_attribute('class')
        
        if "button-disabled" in class_status:
            status=True
        else:
            stats=False
        utillobj.asequal(True,status,'Step 8. Verify OK button is disabled by Default')
        
        
        '''    Step 9. Clear default text and enter "ACC"    '''
        text_field = edit_title_obj.find_element_by_css_selector("input")
        utillobj.set_text_field_using_actionchains(text_field, 'ACC')
        
        '''    Step 10. Verify OK button enabled    '''
        
        dialog_css="div[id^='BiDialog'] [class*='window-active']" + " div[id^='BiButton']"
        dialog_btns=self.driver.find_elements_by_css_selector(dialog_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        class_status=dialog_btns[btn_text_list.index("OK")].get_attribute('class')
        
        if "button-disabled" not in class_status:
            status=True
        else:
            stats=False
        utillobj.asequal(True,status,'Step 10. Verify OK button is enabled now')
        
        
        '''    Step 11. Click OK    '''
        
        utillobj.click_dialog_button(element_css,"OK")
        time.sleep(1)
        
        '''    Step 12. Verify group value name updated with new name    '''
        expected_xval_list=['ACC', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M']
        visul_result.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, "Step 12 :Verify XY labels")
        visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 5, 'Step 12. Verify no of risers')
        
        
        '''    13. Click Run    '''
        '''    14. Hover on ACC riser and verify tooltip values    '''

        
        
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_window(1, pause=3)
        #utillobj.switch_to_frame(pause=2)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='PRODUCT_CATEGORY_1')
        
        xaxis_value="PRODUCT_CATEGORY_1"
        yaxis_value="Cost of Goods"
        parentcss="MAINTABLE_wbody1_f"
        visul_result.verify_xaxis_title(parentcss, xaxis_value, "Step 14:a(i) Verify X-Axis Title")
        visul_result.verify_yaxis_title(parentcss, yaxis_value, "Step 14:a(ii) Verify Y-Axis Title")
        expected_xval_list=['ACC', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M']
        visul_result.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, "Step 14:c(iii):Verify XY labels")
        visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 5, 'Step 14d. Verify no of risers')
        
        expected_tooltip_list=['PRODUCT_CATEGORY_1:ACC', 'Cost of Goods:$264,428,419.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visul_result.verify_default_tooltip_values("MAINTABLE_wbody1_f", 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 14. Verify tooltip values')
        

        '''    15. Close run window    '''
        '''    16. Logout using API (without saving)   '''
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        parent_css="#MAINTABLE_wbody1 [class^='riser!']" 
        utillobj.synchronize_with_number_of_element(parent_css, 5,30, pause_time=2)        
        
if __name__ == '__main__':
    unittest.main()