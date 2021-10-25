'''
Created on May 15, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227619
'''
import unittest
from selenium.webdriver import ActionChains
import time,re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.wftools import visualization

class C2227619_TestClass(BaseTestCase):
    def test_C2227619(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227619'

        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(self.driver)
        resultobj._validate_page(elem1)
               
        """
        Step02: Click "Change" in the Home Tab > Select "Matrix Markers" chart
        """
        ribbonobj.change_chart_type('matrix_marker')
        time.sleep(5)
                 
        """
        Step03: Double-click "Gross Profit"
        Step04: Double-click "Product,Category"
        Step05: Drag and drop "Sale,Quarter" to the Columns bucket (field located under 'Sales_Related' > 'Trasaction Date, Simple' dimension
        """
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Sale,Quarter', 1, 'Columns', 0)
        time.sleep(8)
           
        """
        Step06: Verify Preview
        """
        parent_css="#MAINTABLE_wbody1 text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 4)
        metaobj.verify_query_pane_field('Columns', 'Sale,Quarter', 1, "Step06: Verify Columns")
              
        time.sleep(5)
        expected_label=['1','2','3','4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns', 'Sale Quarter', expected_label, "Step06a(ii): Verify column header and labels")
        expected_label=['Accessories', 'Camcorder', 'Computers', 'Media Player']#verifying only 4 because other rows are visible only after scroll
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Product Category', expected_label, "Step06a(ii): Verify row header and labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 28, 29, 'Step 06b: Verify number of Circle displayed')
              
        time.sleep(5)
        bar=['Product Category:Stereo Systems', 'Sale Quarter:2', 'Gross Profit:$19,861,017.39', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r4!c1", bar, "Step06: Verify bar value")
                       
        """
        Step07:Hover over "Stereo Systems" for Quarter 2 > Verify menu
        Step08:Select "Drill down to" > "Product Subcategory"
        """
        time.sleep(3)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')
        time.sleep(2)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mmarker!r4!c1']")
        utillobj.click_on_screen(parent_elem, 'middle',mouse_duration=2.5)
        time.sleep(3)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r4!c1",'Drill down to->Product Subcategory',wait_time=1,verify_menu1=['Product Subcategory','Sale Month'],msg="Step07: Verify Drill down to menu")
        time.sleep(3)
        #visual_obj=visualization.Visualization(self.driver)
        #visual_obj.select_tooltip("riser!s0!g0!mmarker!r4!c1",'Drill down to->Product Subcategory',"MAINTABLE_wbody1")
        #ia_resultarea_obj.select_autolink_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r4!c1", 'Drill down to->Product Subcategory')
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r4!c1",'Drill down to->Product Subcategory')
        time.sleep(5)
          
        """
        Step09:Verify Preview
        """
        parent_css="#MAINTABLE_wbody1 text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 1)
              
        time.sleep(5)
        expected_label=['2']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns', 'Sale Quarter', expected_label, "Step09a(ii): Verify column header and labels")
        expected_label=['Boom Box', 'Home Theater Systems', 'Receivers', 'Speaker Kits', 'iPod Docking Station']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Product Subcategory', expected_label, "Step09a(ii): Verify row header and labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 5, 6, 'Step 09b: Verify number of Circle displayed')

        """
        Step10: Lasso values for "Home Theater Systems", "Receivers", and "Speakers" > Select "Filter Chart" (3 points)
        Step11: Verify Preview
        """
        time.sleep(3)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')
        time.sleep(3)
        resultobj.create_lasso("MAINTABLE_wbody1","circle",'riser!s0!g0!mmarker!r1!c0',target_tag='circle', target_riser='riser!s0!g0!mmarker!r3!c0')
        time.sleep(1)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
         
        parent_css="#MAINTABLE_wbody1 text[class*='rowLabel']"
        resultobj.wait_for_property(parent_css, 3)
          
        time.sleep(5)
        expected_label=['2']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns', 'Sale Quarter', expected_label, "Step11a(ii): Verify column header and labels")
        expected_label=['Home Theater Systems', 'Receivers', 'Speaker Kits']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Product Subcategory', expected_label, "Step11a(ii): Verify row header and labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 3, 4, 'Step11b: Verify number of Circle displayed')
              
        """
        Step12: Hover over "Home Theater Systems" > Verify "Drill up to" menu options
        Step13: Hover over "Home Theater Systems" > Verify "Drill down to" menu options
        """
        time.sleep(3)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')
        time.sleep(2)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0",'Drill up to->Product Category',wait_time=1, verify_menu1=['Product Category', 'Sale Year', '', ''],msg="Step12: Verify Drill up to")
        time.sleep(3)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')
        time.sleep(2)    
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0",'Drill down to->Product Category',wait_time=1,verify_menu1=['', '', 'Model', 'Sale Month'],msg="Step13: Verify Drill down to menu")
        #self.only_verify_select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0",'Drill down to->Product Category',wait_time=1,verify_menu1=['','','Model', 'Sale Month'],msg="Step13: Verify Drill down to") 
        """
        Step14: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
                  
        """
        Step15: Hover over "Home Theater Systems" > Select "Drill up to" > "Sale,Year"
        Step16: Verify output
        """
        parent_css="#MAINTABLE_wbody1 text[class*='rowLabel']"
        resultobj.wait_for_property(parent_css, 3)
        time.sleep(2)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')
        time.sleep(2)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0",'Drill up to->Sale Year')
        parent_css="#MAINTABLE_wbody1 text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 6)
           
        time.sleep(5)
        expected_label=['2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns', 'Sale Year', expected_label, "Step16a(ii): Verify column header and labels")
        expected_label=['Home Theater Systems', 'Receivers', 'Speaker Kits']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Product Subcategory', expected_label, "Step16a(ii): Verify row header and labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 18, 19, 'Step16b: Verify number of Circle displayed')
               
        time.sleep(5)
        bar=['Product Subcategory:Home Theater Systems', 'Sale Year:2011', 'Gross Profit:$241,954.66', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0", bar, "Step16: Verify bar value")
           
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227619_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
             
        """
        Step17: Click Save in the toolbar
        Step18: Save as "C2158150" > Click Save
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
             
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
             
        """
        Step19: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
             
        """
        Step20: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
              
        """
        Step21: Verify canvas
        """
        parent_css="#MAINTABLE_wbody1 text[class*='rowLabel']"
        resultobj.wait_for_property(parent_css, 3)
           
        time.sleep(5)
        expected_label=['2']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns', 'Sale Quarter', expected_label, "Step21a(ii): Verify column header and labels")
        expected_label=['Home Theater Systems', 'Receivers', 'Speaker Kits']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Product Subcategory', expected_label, "Step21a(ii): Verify row header and labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 3, 4, 'Step21b: Verify number of Circle displayed')
               
        time.sleep(5)
        bar=['Product Subcategory:Home Theater Systems', 'Sale Quarter:2', 'Gross Profit:$6,373,088.67', 'Filter Chart', 'Exclude from Chart', 'Drill up to', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0", bar, "Step21: Verify bar value")
        
    def only_verify_select_default_tooltip_menu(self,parent_id, raiser_class, menu_path, wait_time=2, **kwargs):#Need to Delete
        
        if 'default_move' in kwargs:
            pass
        else:
            move1 = self.driver.find_element_by_css_selector("#"+ parent_id)
            utillity.UtillityMethods.click_type_using_pyautogui(self, move1, move=True, **kwargs)
            time.sleep(5)
        browser = utillity.UtillityMethods.parseinitfile(self, 'browser')
        action1 = ActionChains(self.driver)
        menus=menu_path.split('->')
        raiser_css="#"+ parent_id + " [class*='" + raiser_class + "']"
        if len(menus)>1:
            tooltip_css="#"+ parent_id + " span[id*='tdgchart-tooltip']>div>ul>li"
            obj_locator=self.driver.find_element_by_css_selector(raiser_css)
            if 'default_move' in kwargs:
                pass
            else:
                utillity.UtillityMethods.click_type_using_pyautogui(self, obj_locator,**kwargs)
                time.sleep(0.5)
            if browser in ['Firefox','Chrome']:
                wait_time=0
            else:
                wait_time=1
            time.sleep(wait_time)
            tooltips=self.driver.find_elements_by_css_selector(tooltip_css)
            if browser in ['IE','Chrome']:
                action1=ActionChains(self.driver)
                action1.move_to_element(tooltips[0]).perform()
                del action1
            else:
                utillity.UtillityMethods.click_type_using_pyautogui(self, tooltips[0],**kwargs)
            for i in range(len(tooltips)):
                line1=tooltips[i].text.strip()
                if menus[0] in (re.sub('>', '', line1) if bool(re.match(r'^>', line1)) else tooltips[i].text.strip()).split('\n'):
                    if browser == 'Firefox':
                        utillity.UtillityMethods.click_type_using_pyautogui(self, tooltips[i], leftClick=True, **kwargs)
#                         tooltips[i].click()
                        break
                    else:
                        tooltips[i].click()
                        break
            tooltip_css1="div[class='tdgchart-submenu']>div>ul>li>span"
            tooltips1=self.driver.find_elements_by_css_selector(tooltip_css1) 
            if 'verify_menu1' in kwargs:                               
                menu1=[el.text.strip() for el in tooltips1]
                utillity.UtillityMethods.as_List_equal(self,menu1,kwargs['verify_menu1'],kwargs['msg'])
    

if __name__ == '__main__':
    unittest.main()

