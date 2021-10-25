'''
Created on Jul 16, 2018

@author: Vishnu priya
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea

class C2349148_TestClass(BaseTestCase):


    def test_C2349148(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2349148'
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        
        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1", 1, 65)
        
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
        
        time.sleep(4)
        metaobj.datatree_field_click("Revenue", 2, 1)
        #parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        #resultobj.wait_for_property(parent_css, 21)
        
        """
        Step 03:Right-click Horizontal Axis > Verify menu with "Sort By Total Value"
        
        """
        time.sleep(2)
        metaobj.querytree_field_click("Horizontal Axis", 1, 1)
        time.sleep(2)
        a=['Suppress Empty Group','Sort By Total Value']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,expected_ticked_list=['Suppress Empty Group'],msg='Step03: Expected to see following options:')
        time.sleep(0.5)
        
        """
        Step 04: Right-click Vertical Axis > Verify menu ("Sort By Total Value" should not be available) 
        
        """
        time.sleep(2)
        metaobj.querytree_field_click("Vertical Axis", 1, 1)
        time.sleep(2)
        b=['Multi-Y split']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=b, msg='Step04: Expected to see following options:')
        time.sleep(0.5)
        
        """
        Step:5 Select Home Tab > Select "Swap"
        
        """
        ribbonobj.select_ribbon_item('Home', 'Swap')
        time.sleep(4)
        
        """
        Step:6 Right-click Horizontal Axis > Verify menu ("Sort By Total Value" should not be available once chart is rotated)
        """
        time.sleep(2)
        metaobj.querytree_field_click("Horizontal Axis", 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=b, msg='Step06: Expected to see following options:')
        time.sleep(3)
        
        """
        Step: 7 Right-click Vertical Axis > Verify menu with "Sort By Total Value"
        
        """
        time.sleep(2)
        metaobj.querytree_field_click("Vertical Axis", 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,msg='Step03: Expected to see following options:')
        
        """
        Step: 8 Select "Sort By Total Value" > "Descending"
        """
        utillobj.select_or_verify_bipop_menu('Sort By Total Value')
        time.sleep(0.5)
        a1=['Off','Ascending','Descending']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a1,expected_ticked_list=['Off'],msg='Step08: Verify the list of options')
        
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Descending')
        
        """
        Step 09: Verify preview updated following
        """
        time.sleep(4)
        expected_xval_list=['Blu Ray','Speaker Kits','Home Theater Systems','Flat Panel TV','Headphones','Standard','Smartphone','Video Editing','Receivers','Universal Remote Controls','Professional','Tablet','iPod Docking Station','Handheld','Streaming','DVD Players','Charger', 'CRT TV','Boom Box','Portable TV','DVD Players - Portable']
        expected_yval_list=['0', '50M','100M','150M','200M','250M','300M','350M','400M','450M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step09:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 42, 'Step09.b: Verify the total number of risers displayed on preview')       
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step08.c: Verify first bar color")
        legend=['Cost of Goods', 'Revenue']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step08.d: Verify Legends Title")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$181,112,921.00','Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar,"Step08: Verify bar value")
        time.sleep(5)
        
        """
        Step10: Click Save in the toolbar > Save as "C2349148" > Click Save
        """     
        
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """
        Step:11 Logout Using API
        """
        
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
    
        """
        Step:12 http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2349148.fex
        """  
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_2', mrid='mrid', mrpass='mrpass')
        #utillobj.active_run_fex_api_login('C2349148.fex','S10660_visual_2','mrid','mrpass')
        time.sleep(10)
        
        """
        Step:13 verify the live preview
        
        """
        time.sleep(2)          
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step13:a(ii) Verify x-Axis Title")
        expected_xval_list=['Blu Ray','Speaker Kits','Home Theater Systems','Flat Panel TV','Headphones','Standard','Smartphone','Video Editing','Receivers','Universal Remote Controls','Professional','Tablet','iPod Docking Station','Handheld','Streaming','DVD Players','Charger', 'CRT TV','Boom Box','Portable TV','DVD Players - Portable']
        expected_yval_list=['0', '50M','100M','150M','200M','250M','300M','350M','400M','450M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step13:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 42, 'Step13.b: Verify the total number of risers displayed on preview')       
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step13.c: Verify first bar color")
        legend=['Cost of Goods', 'Revenue']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 13.c: Verify Legends Title")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$181,112,921.00','Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar,"Step 13.d: Verify bar value")
        time.sleep(5)
        
        """
        Step:14 click "RUN"
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        """
        Step:15 verify output
        """
        time.sleep(2)          
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step15:a(ii) Verify x-Axis Title")
        expected_xval_list=['Blu Ray','Speaker Kits','Home Theater Systems','Flat Panel TV','Headphones','Standard','Smartphone','Video Editing','Receivers','Universal Remote Controls','Professional','Tablet','iPod Docking Station','Handheld','Streaming','DVD Players','Charger', 'CRT TV','Boom Box','Portable TV','DVD Players - Portable']
        expected_yval_list=['0', '50M','100M','150M','200M','250M','300M','350M','400M','450M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step15:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 42, 'Step15.b: Verify the total number of risers displayed on preview')       
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step13.c: Verify first bar color")
        legend=['Cost of Goods', 'Revenue']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 15.c: Verify Legends Title")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$181,112,921.00','Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar,"Step 15.d: Verify bar value")
        time.sleep(5)
        
        """
        Step 16: Close run window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        
        """
        Step 17:Select Home Tab > Click on "Swap"
        
        """
        ribbonobj.select_ribbon_item('Home', 'Swap')
        time.sleep(4)
        
        """
        Step 18:Verify Live Preview
        
        """
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(parent_css,42)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step18:a(ii) Verify x-Axis Title")
        expected_xval_list=['Blu Ray','Speaker Kits','Home Theater Systems','Flat Panel TV','Headphones','Standard','Smartphone','Video Editing','Receivers','Universal Remote Controls','Professional','Tablet','iPod Docking Station','Handheld','Streaming','DVD Players','Charger', 'CRT TV','Boom Box','Portable TV','DVD Players - Portable']
        expected_yval_list=['0', '50M','100M','150M','200M','250M','300M','350M','400M','450M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step18:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 42, 'Step18.b: Verify the total number of risers displayed on preview')       
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step08.c: Verify first bar color")
        legend=['Cost of Goods', 'Revenue']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step18.d: Verify Legends Title")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$181,112,921.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar,"Step18e: Verify bar value")
        time.sleep(5)
        
        """
        Step:19 Right-click Horizontal Axis > Verify menu "Sort By Total Value" > "Descending" appears selected
        
        """
        metaobj.querytree_field_click("Horizontal Axis", 1, 1)
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a, msg='Step06: Expected to see following options:')
        utillobj.select_or_verify_bipop_menu('Sort By Total Value')
        a1=['Off','Ascending','Descending']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a1,expected_ticked_list=['Descending'],msg='Step19: Verify the list of options')
        
        """
        Step:20 Click Save > OK
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(2)
        utillobj.click_dialog_button("div[id^='BiDialog']", 'OK')
        
        """
        Step:21 logoutLogout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
if __name__ == "__main__":
    
    unittest.main()