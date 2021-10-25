'''
Created on May 19, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227622
TestCase Name = Drill down with Gauge chart type
'''

import unittest,time, operator, re
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from functools import reduce

class C2227622_TestClass(BaseTestCase):

    def test_C2227622(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227622'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
          
        """
        Step 02: Click "Change" in the Home Tab > Select "Gauge" chart
        """
        ribbonobj.change_chart_type("gauge")
         
        """
        Step 03: Double-click "Cost of Goods"
        """
        time.sleep(5)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
         
        """
        Step 04: Drag and drop "Product,Category" into the Columns bucket
        """
        time.sleep(4)
        metaobj.datatree_field_click('Product,Category',1, 1, 'Add To Query', 'Columns')
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Step 05: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 7, 'Step 05a: Verify number of Circle displayed')
        expected_header='Product Category'
        expected_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns',expected_header,expected_label,"Step 05.b:")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mrange!r0!c4!", "bar_blue", "Step 05.c: Verify first bar color")
        time.sleep(5)
        parent_elem=self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1 [class*='gauge_secondary_ring']")
        utillobj.click_on_screen(parent_elem[4], 'right',x_offset=-15)
        expected_tooltip=['Product Category:Stereo Systems', 'Cost of Goods:$205,113,863.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mrange!r0!c4!",expected_tooltip, "Step 05.d: verify the default tooltip values", default_move=True)
        
        
        """
        Step 06: Hover over "Stereo Systems" > Verify menu > Select "Drill down to Product Subcategory"
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mrange!r0!c4!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1) 
        time.sleep(6)
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(css, coordinate_type='start')
        parent_elem=self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1 [class*='gauge_secondary_ring']")
        utillobj.click_on_screen(parent_elem[4], 'right',x_offset=-15)    
        self.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g0!mrange!r0!c4!", "Drill down to Product Subcategory", default_move=True)
        time.sleep(5)
        
        """
        Step 07: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step07:")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 5, 'Step 07.a: Verify number of Circle displayed')
        expected_header='Product Subcategory'
        expected_label=['Boom Box', 'Home Theater Systems', 'Receivers', 'Speaker Kits', 'iPod Docking Station']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns',expected_header,expected_label,"Step 07.b:")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mrange!r0!c2!", "bar_blue", "Step 07.c: Verify first bar color")
        time.sleep(5)
        parent_elem=self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1 [class*='gauge_secondary_ring']")
        utillobj.click_on_screen(parent_elem[2], 'right', x_offset=-15)
        expected_tooltip=['Product Subcategory:Receivers', 'Cost of Goods:$40,329,668.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        self.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mrange!r0!c2!",expected_tooltip, "Step 07.d: verify the default tooltip values", default_move=True)
        
        
        """
        Step 08:  Lasso values: Home Theater Systems, Receivers and Speaker Kits > Select "Filter Chart"
        """
        time.sleep(6)
        raiser="#MAINTABLE_wbody1 [class*='riser!s0!g0!mrange!r0!c1!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        browser = utillobj.parseinitfile('browser')
        move_riser = driver.find_element_by_css_selector(raiser)
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move_riser)
        else:
            action = ActionChains(driver)
            action.move_to_element(move_riser).perform()
        resultobj.create_lasso('MAINTABLE_wbody1','path', 'riser!s0!g0!mrange!r0!c1!', target_tag='path', target_riser='riser!s0!g0!mrange!r0!c3!')
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        
        """
        Step 09: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 3)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step09.1:")
        metaobj.verify_filter_pane_field('Product,Subcategory',2,"Step09.2:")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 3, 'Step 09.a: Verify number of Circle displayed')
        expected_header='Product Subcategory'
        expected_label=['Home Theater Systems', 'Receivers', 'Speaker Kits']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns',expected_header,expected_label,"Step 09.b:")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mrange!r0!c2!", "bar_blue", "Step 09.c: Verify first bar color")
        time.sleep(5)
        parent_elem=self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1 [class*='gauge_secondary_ring']")
        utillobj.click_on_screen(parent_elem[0], 'right', x_offset=-25)
        expected_tooltip=['Product Subcategory:Home Theater Systems', 'Cost of Goods:$56,428,589.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        self.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mrange!r0!c0!",expected_tooltip, "Step 09.d: verify the default tooltip values", default_move=True)
        
        """
        Step10: Click Run > Verify output
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step11: Verify output > Hover over "Speaker Kits > Select "Drill down to Model"
        """
        chart_type_css="path[class*='riser!s0!g0!mrange!r0!c2!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(8)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 3)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 3, 'Step 11.a: Verify number of Circle displayed')
        expected_header='Product Subcategory'
        expected_label=['Home Theater Systems', 'Receivers', 'Speaker Kits']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns',expected_header,expected_label,"Step 11.b:")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mrange!r0!c2!", "bar_blue", "Step 11.c: Verify first bar color")
        time.sleep(5)
        parent_elem=self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1 [class*='gauge_secondary_ring']")
        utillobj.click_on_screen(parent_elem[0], 'right', x_offset=-25)
        expected_tooltip=['Product Subcategory:Home Theater Systems', 'Cost of Goods:$56,428,589.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        self.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mrange!r0!c0!",expected_tooltip, "Step 11.d: verify the default tooltip values", default_move=True)
        time.sleep(5)
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mrange!r0!c2!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(css, coordinate_type='start') 
        time.sleep(3)
        parent_elem=self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1 [class*='gauge_secondary_ring']")
        utillobj.click_on_screen(parent_elem[2], 'right',x_offset=-25)     
        self.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g0!mrange!r0!c2!", "Drill down to Model", default_move=True)
        time.sleep(5)
        
        """
        Step 12: Verify output
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 10)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 10, 'Step 12.a: Verify number of Circle displayed')
        expected_header='Model'
        expected_label=['BOSE AM10IV', 'BOSE AM16II', 'Harman Kardon HKTS20BQ', 'Harman Kardon HKTS30BQ', 'Onkyo SKSHT540', 'Onkyo SKSHT750B', 'Onkyo SKSHT870', 'Polk Audio LSIFX', 'Polk Audio RM705', 'Yamaha NSSP1800']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns',expected_header,expected_label,"Step 12.b:")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mrange!r0!c0!", "bar_blue", "Step 12.c: Verify first bar color")
        time.sleep(5)
        parent_elem=self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1 [class*='gauge_secondary_ring']")
        utillobj.click_on_screen(parent_elem[0], 'right', x_offset=-10)
        expected_tooltip=['Model:BOSE AM10IV', 'Cost of Goods:$11,092,770.00', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Subcategory']
        self.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mrange!r0!c0!",expected_tooltip, "Step 12.d: verify the default tooltip values", default_move=True)
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227622_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 13: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 14: Click "Save" > Save as "C2167767" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
         
        """
        Step 15: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step 16: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 17: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="path[class*='riser!s0!g0!mrange!r0!c2!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        driver.maximize_window()
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 3)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step17.1:")
        metaobj.verify_filter_pane_field('Product,Subcategory',2,"Step17.2:")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 3, 'Step 17.a: Verify number of Circle displayed')
        expected_header='Product Subcategory'
        expected_label=['Home Theater Systems', 'Receivers', 'Speaker Kits']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns',expected_header,expected_label,"Step 17.b:")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mrange!r0!c2!", "bar_blue", "Step 17.c: Verify first bar color")
        time.sleep(5)
        parent_elem=self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1 [class*='gauge_secondary_ring']")
        utillobj.click_on_screen(parent_elem[0], 'right', x_offset=-25)
        expected_tooltip=['Product Subcategory:Home Theater Systems', 'Cost of Goods:$56,428,589.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        self.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mrange!r0!c0!",expected_tooltip, "Step 17.d: verify the default tooltip values", default_move=True)
        time.sleep(5)
        
        """
        Step 18: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
    def verify_default_tooltip_values(self,parent_id, raiser_class, expected_tooltip_list, msg, **kwargs):
        """
        :kwargs: default_move= False (if default_move in kwargs -> mouse not move)
        :param parent_id = 'MAINTABLE_wbody1'
        :param : raiser_class = 'riser!s4!g4!mbar!'
        :param : expected_tooltip_list = ['Product:French Roast', 'Unit Price:73,710.00', 'Ordered Units:285689', 'Product:French Roast', 'Order Number:1965387', 'Filter Chart', 'Exclude from Chart']
        :param : color = 'red' or 'green'....color should be added in the color.data file
        expected_tooltip=['Product:French Roast', 'Unit Price:73,710.00', 'Ordered Units:285689', 'Product:French Roast', 'Order Number:1965387', 'Filter Chart', 'Exclude from Chart']
        Usage: verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "red", "Step 8: verify the default tooltip values")
        """
        if 'default_move' in kwargs:
            pass
        else:
            action1 = ActionChains(self.driver)
            move1 = self.driver.find_element_by_css_selector("#"+ parent_id)
            if self.browser == 'Firefox':
                utillity.UtillityMethods.click_type_using_pyautogui(self, move1, move=True)
            else:
                action1.move_to_element_with_offset(move1,1,1).perform()
            time.sleep(5)
            del action1
        tooltip_css="#"+ parent_id + " span[id='tdgchart-tooltip']>div>ul>li"
        time.sleep(1)
        tooltips=self.driver.find_elements_by_css_selector(tooltip_css)
        tooltip_list=[]
        for i in range(len(tooltips)):
            tooltip_list.append((tooltips[i].text.strip()).split('\n'))
        actual_tooltip_list=[line for line in reduce(operator.add, tooltip_list) if len(line)>1]
        actual_list = []
        for line in actual_tooltip_list:
            if bool(re.match(r'.*:\s.*', line)):
                reqobj = re.match('(.*):\s{1,}(.*)', line)
                new_element = str(reqobj.group(1)) + ":" + str(reqobj.group(2))
            elif bool(re.match(r'^>', line)):
                new_element=re.sub('>', '', line)
            else:
                new_element=line
            actual_list.append(new_element)
        print(expected_tooltip_list)
        print(actual_list)
        utillity.UtillityMethods.asequal(self, expected_tooltip_list, actual_list, msg)
        time.sleep(3)
        
    def select_default_tooltip_menu(self,parent_id, raiser_class, menu_path, wait_time=2, **kwargs):
        """
        param parent_id = 'MAINTABLE_wbody1'
        param : raiser_class = 'riser!s4!g4!mbar!'
        kwargs: verify_menu1=['Customer State Province', 'Product Subcategory'](if given then it will just verify, if not given it will click on menu)
        param : menu_path = 'Drill up to->Product Category' (At this point, i am considering one level of sub menu. We can enhance, if the level increases.)
        Usage: select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g0!mbar", 'Drill up to->Product Category')
        Usage: select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g0!mbar", 'Filter Chart')
        Usage: select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g2!mbar",'Drill down to Product Subcategory',drilldown_menu='Computers')
        Usage:resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0",'Drill down to->Product Subcategory',
        wait_time=1,x_offset=1,y_offset=-25,x_offset_menu1=0,y_offset_menu1=-25,verify_menu1=['Customer State Province', 'Product Subcategory'],msg="Step15: Verify Drill down to menu")
        Usage:resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0",'Drill down to->Product Subcategory',
        wait_time=1,x_offset=1,y_offset=-25,x_offset_menu1=0,y_offset_menu1=-25)
        Author: Niranjan
        """
        if 'default_move' in kwargs:
            pass
        else:
            action1 = ActionChains(self.driver)
            move1 = self.driver.find_element_by_css_selector("#"+ parent_id)
            if self.browser == 'Firefox':
                utillity.UtillityMethods.click_type_using_pyautogui(self, move1, move=True)
            else:
                action1.move_to_element_with_offset(move1,1,1).perform()
            time.sleep(5)
            del action1
        browser = utillity.UtillityMethods.parseinitfile(self, 'browser')
        action1 = ActionChains(self.driver)
        menus=menu_path.split('->')
        raiser_css="#"+ parent_id + " [class*='" + raiser_class + "']"
        if len(menus)>1:
            tooltip_css="#"+ parent_id + " span[id='tdgchart-tooltip']>div>ul>li"
            obj_locator=self.driver.find_element_by_css_selector(raiser_css)
#             if self.browser == 'Firefox':
#                 utillity.UtillityMethods.click_type_using_pyautogui(self, obj_locator,**kwargs)
#             else:
#                 action1.move_to_element(obj_locator).perform()
#                 del action1
            if self.browser in ['Firefox','Chrome']:
                wait_time=0
            else:
                wait_time=1
            time.sleep(wait_time)
            tooltips=self.driver.find_elements_by_css_selector(tooltip_css)
            if browser=='IE':
                action1=ActionChains(self.driver)
                action1.move_to_element(tooltips[0]).perform()
                del action1
            for i in range(len(tooltips)):
                line1=tooltips[i].text.strip()
                if menus[0] in (re.sub('>', '', line1) if bool(re.match(r'^>', line1)) else tooltips[i].text.strip()).split('\n'):
                    print(tooltips[i].text+"-menu1")
                    if self.browser == 'Firefox':
                        utillity.UtillityMethods.click_type_using_pyautogui(self, tooltips[i],**kwargs)
                        tooltips[i].click()
                        break
                    else:
                        tooltips[i].click()
                        break
            tooltip_css1="div[class='tdgchart-submenu']>div>ul>li>span"
            tooltips1=self.driver.find_elements_by_css_selector(tooltip_css1)    
            if browser=='IE':
                action1=ActionChains(self.driver)
                action1.move_to_element(tooltips1[0]).perform()
                del action1 
            browser = utillity.UtillityMethods.parseinitfile(self,'browser')          
            if browser == 'Firefox':
                utillity.UtillityMethods.click_type_using_pyautogui(self, tooltips1[0],**kwargs)
            else:
                action1=ActionChains(self.driver)
                action1.move_to_element(tooltips1[0]).perform()
                del action1
            if 'verify_menu1' in kwargs:                               
                menu1=[el.text.strip() for el in tooltips1]
                print(menu1)
                utillity.UtillityMethods.as_List_equal(self,menu1,kwargs['verify_menu1'],kwargs['msg'])
            else:
                tooltip_css2="div[class='tdgchart-submenu']>div>ul>li>span"
                tooltips2=self.driver.find_elements_by_css_selector(tooltip_css2)
                for i in range(len(tooltips1)):
                    if menus[1] in (tooltips1[i].text.strip()).split('\n'):
                        tooltips1[i].click()
                        print(tooltips1[i].text+"- after click menu2")
                        break               
        else:
            if 'drilldown_menu' in kwargs:
                option=kwargs['drilldown_menu']#removed .lower(), since 1st level not working in visualization
                tooltip_css="#"+ parent_id + " span[id='tdgchart-tooltip']>div>ul>li>span[onclick*='"+option+"']"
            else:
                tooltip_css="#"+ parent_id + " span[id='tdgchart-tooltip'] [onclick^='ibiChart']"
#             obj_locator=self.driver.find_element_by_css_selector(raiser_css)
#             browser = utillity.UtillityMethods.parseinitfile(self,'browser')
#             if browser == 'Firefox':
#                 utillity.UtillityMethods.click_type_using_pyautogui(self, obj_locator,**kwargs)
#             else:
#                 action1=ActionChains(self.driver)
#                 action1.move_to_element(obj_locator).perform()
#                 del action1
            time.sleep(2)
            tooltips=self.driver.find_elements_by_css_selector(tooltip_css)
            tooltips[[el.text.strip() for el in tooltips].index(menus[0])].click()    
        
if __name__ == '__main__':
    unittest.main()  
        