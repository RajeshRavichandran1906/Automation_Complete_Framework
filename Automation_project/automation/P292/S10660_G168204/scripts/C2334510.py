'''
Created on Oct 26, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2334510
TestCase Name = Visualization "bucket mode" Stacked Bar charts sorting up/down on Y-Axis
'''

import unittest, time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea
from common.locators import visualization_resultarea_locators
from common.lib import utillity

class C2334510_TestClass(BaseTestCase):

    def test_C2334510(self):
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2334510'

        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10660_visual_2', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Double click "Cost of Goods", "Product, SubCategory"
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        
        time.sleep(4)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        
        """
        Step 03: Drag and drop "Sale,Year" to Color bucket.
        """
        time.sleep(4)
        metaobj.datatree_field_click("Sale,Year", 1, 1, 'Add To Query', 'Color')
        time.sleep(2) 
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 101)  
        
        """
        Step 04: Verify following preview displayed
        """
        time.sleep(4)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step04:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step04:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step04:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 101, 'Step04.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step04.c: Verify first bar color")
        legend=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step04.d: Verify Legends Title")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$74,193,750.00', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s5!g0!mbar!", bar,"Step04: Verify bar value")
        time.sleep(5)
        
        """ 
        Step 05: Right click on Horizontal axis 
        Expected to see following options:
        Suppress Empty Group (Checked by default)
        Sort by Total Value > 
        """
        time.sleep(2)
        metaobj.querytree_field_click("Horizontal Axis", 1, 1)
        time.sleep(2)
        a=['Suppress Empty Group','Sort By Total Value']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,expected_ticked_list=['Suppress Empty Group'],msg='Step05: Expected to see following options:')
        time.sleep(0.5)
        
        """ 
        Step 06: Hover on Sort by Total Value  
        Expected to see
        Off (Grey dot)
        Ascending
        Descending 
        """
        utillobj.select_or_verify_bipop_menu('Sort By Total Value')
        time.sleep(0.5)
        a=['Off','Ascending','Descending']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,expected_ticked_list=['Off'],msg='Step06: Verify the list of options')
        
        """
        Step 07: Click Ascending
        """
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Ascending')
        
        """
        Step 08: Verify preview updated following
        """
        time.sleep(6)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 101) 
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step08:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step08:a(ii) Verify Y-Axis Title")
        expected_xval_list=['DVD Players - Portable', 'Portable TV', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'Streaming', 'Handheld', 'Tablet', 'iPod Docking Station', 'Professional', 'Universal Remote Controls', 'Video Editing', 'Receivers', 'Smartphone', 'Standard', 'Headphones', 'Home Theater Systems', 'Flat Panel TV', 'Speaker Kits', 'Blu Ray']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step08:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 101, 'Step08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step08.c: Verify first bar color")
        legend=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step08.d: Verify Legends Title")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$74,193,750.00', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s5!g0!mbar!", bar,"Step08: Verify bar value")
        time.sleep(5)
        
        """ 
        Step 09: Right click on Horizontal axis > Hover on Sort by Total Value 
        """
        time.sleep(2)
        metaobj.querytree_field_click("Horizontal Axis", 1, 1)
        time.sleep(2)
        a=['Suppress Empty Group','Sort By Total Value']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,expected_ticked_list=['Suppress Empty Group'],msg='Step09: Expected to see following options:')
        time.sleep(0.5)
        utillobj.select_or_verify_bipop_menu('Sort By Total Value')
        
        """ 
        Step 10: Verify Ascending option selected
        """
        time.sleep(0.5)
        a=['Off','Ascending','Descending']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,expected_ticked_list=['Ascending'],msg='Step10: Verify Ascending option selected')
        
        """
        Step 11: Hover on first and last riser and verify tooltip value
        """
        time.sleep(5)
        bar=['Product Subcategory:DVD Players', 'Cost of Goods:$3,498,240.00', 'Sale Year:2011', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!", bar,"Step11a: Verify first bar value")
        time.sleep(8)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$74,193,750.00', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s5!g0!mbar!", bar,"Step11b: Verify last bar value")
        time.sleep(5)

        """
        Step12: Click Save in the toolbar > Save as "C2334510" > Click Save
        """     
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step13: Run the chart with API call: 
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P292_S10660&BIP_item=C2334510.FEX
        """  
        utillobj.active_run_fex_api_login('C2334510.fex','S10660_visual_2','mrid','mrpass')
        time.sleep(10)
        
        """
        Step14: Hover on' HANDHELD' and 'Home theater systems' riser and verify tooltip value
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 101) 
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step14:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step14:a(ii) Verify Y-Axis Title")
        expected_xval_list=['DVD Players - Portable', 'Portable TV', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'Streaming', 'Handheld', 'Tablet', 'iPod Docking Station', 'Professional', 'Universal Remote Controls', 'Video Editing', 'Receivers', 'Smartphone', 'Standard', 'Headphones', 'Home Theater Systems', 'Flat Panel TV', 'Speaker Kits', 'Blu Ray']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step14:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 101, 'Step14.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step14.c: Verify first bar color")
        legend=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step14.d: Verify Legends Title")
        time.sleep(5)
        bar=['Product Subcategory:Handheld', 'Cost of Goods:$8,422,989.00', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s5!g7!mbar!", bar,"Step14a: Verify first bar value")
        time.sleep(8)
        bar=['Product Subcategory:Home Theater Systems', 'Cost of Goods:$23,121,631.00', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s5!g9!mbar!", bar,"Step14b: Verify last bar value")
        time.sleep(5)
        
        """
        Step15: Close output window.
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step16: Restore the saved fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2334509.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)

        """ 
        Step17: Right click on Horizontal axis > Hover on Sort by Total Value > Select Off 
        """
        time.sleep(2)
        metaobj.querytree_field_click("Horizontal Axis", 1, 1)
        time.sleep(2)
        a=['Suppress Empty Group','Sort By Total Value']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,expected_ticked_list=['Suppress Empty Group'],msg='Step09: Expected to see following options:')
        time.sleep(0.5)
        utillobj.select_or_verify_bipop_menu('Sort By Total Value')
        time.sleep(0.5)
        utillobj.select_or_verify_bipop_menu('Off')
         
        """
        Step18: Verify preview updated following
        """
        time.sleep(4)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step18:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step18:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step18:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 101, 'Step18.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step18.c: Verify first bar color")
        legend=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step18.d: Verify Legends Title")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$74,193,750.00', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s5!g0!mbar!", bar,"Step18.e: Verify bar value")
        time.sleep(5)
 
        """ 
        Step 19: Right click on Horizontal axis > Hover on Sort by Total Value > Descending
        """
        time.sleep(2)
        metaobj.querytree_field_click("Horizontal Axis", 1, 1)
        time.sleep(2)
        a=['Suppress Empty Group','Sort By Total Value']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,expected_ticked_list=['Suppress Empty Group'],msg='Step19: Expected to see following options:')
        time.sleep(0.5)
        utillobj.select_or_verify_bipop_menu('Sort By Total Value')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Descending')
         
        """
        Step 20: Verify preview updated
        """
        time.sleep(8)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 101)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step20:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step20:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Speaker Kits', 'Flat Panel TV', 'Home Theater Systems', 'Headphones', 'Standard', 'Smartphone', 'Receivers', 'Video Editing', 'Universal Remote Controls', 'Professional', 'iPod Docking Station', 'Tablet', 'Handheld', 'Streaming', 'DVD Players', 'Charger', 'CRT TV', 'Boom Box', 'Portable TV', 'DVD Players - Portable']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step20:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 101, 'Step20.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step20.c: Verify first bar color")
        legend=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step20.d: Verify Legends Title")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$74,193,750.00', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s5!g0!mbar!", bar,"Step20: Verify bar value")
        time.sleep(5)
 
        """
        Step 21: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
                   
        """
        Step 22: Hover on first and last riser and verify tooltip value
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 101)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step22:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step22:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Speaker Kits', 'Flat Panel TV', 'Home Theater Systems', 'Headphones', 'Standard', 'Smartphone', 'Receivers', 'Video Editing', 'Universal Remote Controls', 'Professional', 'iPod Docking Station', 'Tablet', 'Handheld', 'Streaming', 'DVD Players', 'Charger', 'CRT TV', 'Boom Box', 'Portable TV', 'DVD Players - Portable']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step22:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 101, 'Step22.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step22.c: Verify first bar color")
        legend=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step22.d: Verify Legends Title")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$74,193,750.00', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s5!g0!mbar!", bar,"Step22: Verify first riser tool tip value")
        time.sleep(8)
        bar=['Product Subcategory:Tablet', 'Cost of Goods:$21,101,061.00', 'Sale Year:2016', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s5!g17!mbar!", bar,"Step22: Verify last riser tool tip value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2334510_Actual_step22', image_type='actual',x=1, y=1, w=-1, h=-1)
              
        """
        Step23: Close run window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
 
        """
        Step24: Logout using API (without saving): http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()