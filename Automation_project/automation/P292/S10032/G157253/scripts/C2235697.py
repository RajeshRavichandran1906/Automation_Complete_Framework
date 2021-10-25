'''
Created on Nov 30, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2235697
TestCase Name : Verify Document Canvas context menus 
'''
import unittest, time
from common.pages import visualization_metadata, visualization_ribbon, ia_resultarea, ia_styling
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2235697_TestClass(BaseTestCase):

    def test_C2235697(self):
        
        Test_Case_ID = "C2235697"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_styling_obj=ia_styling.IA_Style(self.driver)
        browser=utillobj.parseinitfile('browser')
        
        """    
            Step 01:Launch IA Document mode:
            http://machine:port/ibi_apps/ia?tool=Document&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('document','new_retail/wf_retail_lite','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        elem1="#resultArea"
        utillobj.synchronize_with_number_of_element(elem1, 1, 30)
          
        """
            Step 02:Double-click "Cost of Goods" and "Product,Subcategory"
        """
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='Cost of Goods', expire_time=30)
        time.sleep(4)
        metaobj.datatree_field_click('Product,Subcategory', 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='Product,Subcategory', expire_time=20)
        ia_resultobj.verify_across_report_data_set('TableChart_1', 2, 2, 10, 2, Test_Case_ID+"_Ds01.xlsx", "Step 02: Verify the created report")
        time.sleep(4)
          
        """ 
            Step 03:Drag "Product,Category" into the "Coordinated" bucket in the Query pane
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Product,Category', 1, 'Coordinated', 0)
        time.sleep(8)
        metaobj.verify_query_pane_field('Coordinated', 'Product,Category', 1, "Step 03: Verify Product Category is added underneath Coordinated bucket", color='Trolley_Grey', font_style='italic')
         
        """ 
            Step 04:Right-click "Product,Category" in Coordinated bucket > Verify menu
            Step 05:Select "Delete"
        """
        metaobj.querytree_field_click('Product,Category', 1, 1)
        time.sleep(1)   
           
        a=['Visibility', 'Create Group...', 'Drill Down', 'Delete']
        utillobj.select_or_verify_bipop_menu('Delete', verify='true', expected_popup_list=a, msg='Step 05:01 Verify menu and select Delate menu')    
        time.sleep(5)
         
        """
            Step 06:Verify field is deleted
        """ 
        metaobj.verify_query_pane_field_available('By', 'Product,Category', 'Coordinated', "Step 06:01: Verify Product,Category field is deleted in querypane", availability=False)
            
        """ 
            Step 07:Right-click "Product,Category" in the Data pane > Verify menu
            Step 08:Select "Across"
        """
        metaobj.datatree_field_click('Product,Category', 1, 1)
        time.sleep(1)
          
        a=['Sum', 'Sort', 'Create Group...', 'Across', 'Filter', 'Slicers']
        utillobj.select_or_verify_bipop_menu('Across', verify='true', expected_popup_list=a, msg='Step 07:01 Right-click "Product,Category" in the Data pane > Verify menu and select Across') 
        time.sleep(5)
         
        """ 
            Step 09:Verify Query and Canvas
        """
        metaobj.verify_query_pane_field('Across','Product,Category',1, "Step 09:01:")
#         ia_resultobj.create_across_report_data_set('TableChart_1', 3, 8, 10, 8, Test_Case_ID+"_Ds02.xlsx")
        ia_resultobj.verify_across_report_data_set('TableChart_1', 3, 8, 10, 8, Test_Case_ID+"_Ds02.xlsx", "Step 09:01: Verify report after adding Product,Categpry in Across")
          
        """ 
            Step 10:Right-click across value "Computers" > Verify menu
        """
        elem=driver.find_elements_by_css_selector("#TableChart_1 div[class^='x']")[3] 
        utillobj.click_on_screen(elem, 'middle',0)
        time.sleep(1)
        utillobj.click_on_screen(elem, 'middle', 1)
        time.sleep(2)
             
        """ 
        Step 11:Select "Keep - Computers" > Verify Query, Filter, and Canvas
        """
        a=['Keep - Computers', 'Remove - Computers', 'Filter Values...', 'Sort', 'Break', 'Visibility', 'Create Group...', 'Change Title...', 'Drill Down', 'Delete']
        utillobj.select_or_verify_bipop_menu('Keep - Computers', verify='true', expected_popup_list=a, msg='Step 11:01: Verify right click menu')
        time.sleep(2)
#         ia_resultobj.create_across_report_data_set('TableChart_1', 3, 2, 2, 2, Test_Case_ID+"_Ds03.xlsx")
        ia_resultobj.verify_across_report_data_set('TableChart_1', 3, 2, 2, 2, Test_Case_ID+"_Ds03.xlsx", "Step 11:02: Verify report after adding Product,Categpry in Across")
        time.sleep(2)
             
        """ 
            Step 12:Right-click filter in the Filter pane > Verify menu
            Step 13:Select "Delete"
        """
        metaobj.filter_tree_field_click('Product,Category Equal to Computers', 1, 1)
        time.sleep(1)
        a=['Edit','Delete','Exclude']
        utillobj.select_or_verify_bipop_menu('Delete', verify='true', expected_popup_list=a, msg='Step 12:01:-Step13:01 Verify menu displayed')  
        time.sleep(5)
               
        """ 
            Step 14:Verify Query, Filter, and Canvas
        """
        metaobj.verify_query_pane_field('Sum', 'Cost of Goods', 1, "Step14 :01:")
        metaobj.verify_query_pane_field('By', 'Product,Subcategory', 1, "Step14 :02:")
        metaobj.verify_query_pane_field('Across', 'Product,Category', 1, "Step14 :03:")
        ia_resultobj.verify_across_report_data_set('TableChart_1', 3, 8, 10, 8, Test_Case_ID+"_Ds02.xlsx", "Step 14:01: Verify report")
        time.sleep(2)
          
        """ 
            Step 15:Right-click on value "Boom Box" in the "Product,Category" column > Verify menu
        """ 
        total_elements=self.driver.find_elements_by_css_selector("#TableChart_1 div[class^='x']")[32]
        utillobj.click_on_screen(total_elements, 'middle', 0)
        time.sleep(1)
        utillobj.click_on_screen(total_elements, 'middle', 1)
        time.sleep(1)
            
        """ 
            Step 16:Select "Remove - Boom Box"
        """
        a=['Keep - Boom Box', 'Remove - Boom Box', 'Filter Values...', 'Sort', 'Break', 'Visibility', 'Create Group...', 'Change Title...', 'Drill Down', 'More', 'Delete']
        utillobj.select_or_verify_bipop_menu('Remove - Boom Box', verify='true', expected_popup_list=a, msg='Step16:01 Verify menu displayed')     
         
        """ 
            Step 17:Verify Query, Filter, and Canvas
        """
        time.sleep(5)
        metaobj.verify_query_pane_field('Sum', 'Cost of Goods', 1, "Step17 :01:")
        metaobj.verify_query_pane_field('By', 'Product,Subcategory', 1, "Step17 :02:")
        metaobj.verify_query_pane_field('Across', 'Product,Category', 1, "Step17 :03:")
        metaobj.verify_filter_pane_field("Product,Subcategory Not equal to Boom Box", 1, "Step 17:04: Verify Filter")
#         ia_resultobj.create_across_report_data_set('TableChart_1', 3, 8, 10, 8, Test_Case_ID+"_Ds04.xlsx")
        ia_resultobj.verify_across_report_data_set('TableChart_1', 3, 8, 10, 8, Test_Case_ID+"_Ds04.xlsx", "Step 17:05: Verify report after adding Product,Categpry in Across")
        time.sleep(2)
          
        """ 
            Step 18:Click on any values in "Accessories" column > Verify menu
        """
        total_elements=self.driver.find_elements_by_css_selector("#TableChart_1 div[class^='x']")[41]
        utillobj.click_on_screen(total_elements, 'middle', 0)
        time.sleep(1)
        utillobj.click_on_screen(total_elements, 'middle', 1)
        time.sleep(1)
             
        """ 
            Step 19:Select More->Aggregation Functions->Average
        """
        a=['Filter Values...', 'Sort', 'Visibility', 'Change Title...', 'Edit Format', 'Drill Down', 'More', 'Delete']
        utillobj.select_or_verify_bipop_menu(verify='true', expected_popup_list=a, msg='Step 19:01 Verify menu displayed')
        utillobj.select_or_verify_bipop_menu('More')
        utillobj.select_or_verify_bipop_menu('Aggregation Functions')
        utillobj.select_or_verify_bipop_menu('Average')
        time.sleep(5)
         
        """ 
            Step 20:Verify Canvas
        """
#         ia_resultobj.create_across_report_data_set('TableChart_1', 3, 8, 10, 8, Test_Case_ID+"_Ds05.xlsx")
        ia_resultobj.verify_across_report_data_set('TableChart_1', 3, 8, 10, 8, Test_Case_ID+"_Ds05.xlsx", "Step 20:01: Verify report after adding Product,Categpry in Across") 
        time.sleep(2)
           
        """ 
            Step 21:Right-click on the Report component on Canvas (around border) > Verify menu
            Step 22:Select "Size and Position..."
        """
        table_css_obj=self.driver.find_element_by_css_selector("#TableChart_1")
        before_h1=table_css_obj.size['height']
        before_w1=table_css_obj.size['width']
        utillobj.click_on_screen(table_css_obj, 'middle', click_type=0)
        time.sleep(2)
        elem="#TableChart_1 div[id*='BiResizeHandle']"
        utillobj.synchronize_with_number_of_element(elem, 8, 20)
        parent=driver.find_elements_by_css_selector("#TableChart_1 div[id*='BiResizeHandle']")
        utillobj.click_on_screen(parent[0], 'middle')
        time.sleep(1)
        utillobj.click_on_screen(parent[0], 'middle', click_type=1) 
        time.sleep(2)
          
        """ 
            Step 22:Select "Size and Position..."
        """
        a=['Copy', 'Cut', 'Duplicate', 'Rename', 'Size and Position...', 'Delete']
        utillobj.select_or_verify_bipop_menu('Size and Position...', verify='true', expected_popup_list=a, msg='Step 22:01 Verify menu displayed')
        time.sleep(5) 
           
        """ 
            Step 23:Change Height to 6 and Width to 9 > Click OK
        """
        elem="div[id^='QbDialog'] [class*='active'] #sapOkBtn"
        utillobj.synchronize_with_number_of_element(elem, 1, 20)
        textfield_elem=self.driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #sizeHeightSpinner")
        utillobj.set_text_field_using_actionchains(textfield_elem, "6")
        textfield_elem=self.driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #sizeWidthSpinner")
        utillobj.set_text_field_using_actionchains(textfield_elem, "9")
        ok_btn = driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #sapOkBtn")
        utillobj.default_click(ok_btn)
        time.sleep(5)
          
        """ 
            Step 24:Verify Canvas
        """
        table_css1_obj=self.driver.find_element_by_css_selector("#TableChart_1")
        after_h1=table_css1_obj.size['height']
        after_w1=table_css1_obj.size['width']
        total_h=float(after_h1)-float(before_h1)
        total_w=float(before_w1)-float(after_w1)
        if total_h >= 25:
            utillobj.asequal(True, True, 'Step 24:01 : Verify table height is not exceeded the thershold  limit')
        else:
            utillobj.asequal(False, True, 'Step 24:01: Verify table height is exceeded the thershold')
        if total_w >= 100:
            utillobj.asequal(True, True, 'Step 24:02: Verify table weight is not exceeded the thershold  limit')
        else:
            utillobj.asequal(False, True, 'Step 24:02: Verify table weight is exceeded the thershold  limit')
             
        """ 
            Step 25:Right-click on the Canvas space (outside of Report) > Verify menu
        """ 
        canvas_obj=self.driver.find_element_by_css_selector("#TableChart_1")
        utillobj.click_on_screen(canvas_obj, 'start', click_type=0, x_offset=-15, y_offset=-15)
        time.sleep(1)
        utillobj.click_on_screen(canvas_obj, 'start', click_type=1, x_offset=-15, y_offset=-15)
        time.sleep(1)
          
        a=['Page Color']
        utillobj.select_or_verify_bipop_menu('Page Color', verify='true', expected_popup_list=a, msg='Step 25:01 Verify menu displayed')
        time.sleep(5)
             
        """ 
            Step 26:Select "Page Color" > Verify dialog
        """ 
        ia_styling_obj.set_color('blue')
        time.sleep(5)
              
        """ 
            Step 27:Select a shade of blue > Click OK
            Step 28:Verify Canvas
        """
        page_canvas_obj=self.driver.find_element_by_css_selector("#canvasContainer #theCanvas")
        ia_styling_obj.verify_background_color(page_canvas_obj, 'blue')
        obj1=driver.find_element_by_css_selector("#resultArea")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step28'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)  
              
        """ 
            Step 29:Click "Save" > save as "C2235697" > Click "Save"
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID) 
            
        """ 
            Step 30:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)
        utillobj.infoassist_api_logout()
         
        """ 
            Step 31:Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2235697.fex&tool=Document
        """
        parent_css="input[id='SignonUserName']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_4', mrid='mrid', mrpass='mrpass')
        elem1="#TableChart_1"
        utillobj.synchronize_with_number_of_element(elem1, 1, 35)
        
        """ 
            Step 32:Verify successful restore
        """
#         ia_resultobj.create_across_report_data_set('TableChart_1', 3, 8, 10, 8, Test_Case_ID+"_Ds06.xlsx")
        ia_resultobj.verify_across_report_data_set('TableChart_1', 3, 8, 10, 8, Test_Case_ID+"_Ds06.xlsx", "Step 32:01: Verify report after adding Product,Categpry in Across")
        page_canvas_obj=self.driver.find_element_by_css_selector("#canvasContainer #theCanvas")
        ia_styling_obj.verify_background_color(page_canvas_obj, 'blue')
        
        """ 
            Step 33:Click Run > Verify output
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=1)
        time.sleep(10)
        table_css_obj=self.driver.find_element_by_css_selector("div[id^='orgdivouter']")
        ia_styling_obj.verify_background_color(table_css_obj, 'blue')
        table_css=self.driver.find_element_by_css_selector("#MAINTABLE_0").is_displayed()
        utillobj.asequal(table_css, True, "Step 33: Report table is displayed inside the report frame")
        utillobj.switch_to_default_content(1)
        obj1=driver.find_element_by_css_selector("#resultArea")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step33'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
            
        """ 
            Step 34:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__ == "__main__":
    unittest.main()