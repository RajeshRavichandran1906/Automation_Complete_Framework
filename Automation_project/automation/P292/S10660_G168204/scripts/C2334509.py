'''
Created on Nov 2, 2017

@author: BM13368
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2334509_TestClass(BaseTestCase):


    def test_C2334509(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2334509'
        
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """
            Step 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=wf_retail_lite
        """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10660_chart_2', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """
            Step 02 : Select Format > Chart type > Other > BAR > Stacked Bar 
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('bar', 'vertical_stacked_bars', 2, ok_btn_click=True)
        """
            Verification : the default vertical stacked bar
        """
        time.sleep(5)
        expected_yval_list=['0', '40', '80', '120', '160', '200']
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 02:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 02:02: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 02:03: Verify second bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mbar!", "dark_green", "Step 02:04: Verify third bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mbar!", "pale_yellow", "Step 02:05: Verify four bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mbar!", "brick_red", "Step 02:06: Verify five bar color")
        resultobj.verify_riser_legends('TableChart_1',['Series0','Series1','Series2','Series3','Series4'], 'Step 02.07 : Verify chart legends')
        resultobj.verify_number_of_riser('TableChart_1', 1, 25, 'Step 02.07: Verify Number chart segment')
        time.sleep(2)
        
        """
            Step 03 : Double click "Cost of Goods", "Revenue" and "Product, SubCategory"
        """
        metadataobj.datatree_field_click('Cost of Goods', 2, 0)
        time.sleep(2)
        metadataobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(2)
        metadataobj.datatree_field_click('Product,Subcategory', 2, 0)
        time.sleep(3)
        """
            Step 04 : Verify following preview displayed
        """
        time.sleep(5)
        parent_css=("#TableChart_1 text[class^='xaxis'][class$='title']")
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Porta...', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Syst...', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote C...', 'Video Editing', 'iPod Docking Station']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 04:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 04:02: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 04:03: Verify second bar color")
        resultobj.verify_riser_legends('TableChart_1',['Cost of Goods', 'Revenue'], 'Step 04.04 : Verify chart legends')
        resultobj.verify_number_of_riser('TableChart_1', 1, 42, 'Step 04.05: Verify Number chart segment')
        time.sleep(2)
        resultobj.verify_xaxis_title('TableChart_1', 'Product Subcategory', "Step 04:06: Verify X-Axis Title")
        time.sleep(1)
        """
            Step 05 : Right click on Horizontal axis 
        """
        metadataobj.querytree_field_click('Horizontal Axis', 1, 1)
        time.sleep(2)
        """
            Verification : Expected to see following options
            New Parameter
            Suppress Empty Group (Checked by default)
            Sort by Total Value >
        """
        a=['New Parameter','Suppress Empty Group','Sort By Total Value']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,expected_ticked_list=['Suppress Empty Group'],msg='Step05: Verify menu in query pane')
        time.sleep(2)
        """
            Step 06 : Hover on Sort by Total Value 
        """
        utillobj.select_or_verify_bipop_menu('Sort By Total Value')
        time.sleep(2)
        
        """
            Verification : Expect to see the following :
            Off (Grey dot)
            Ascending
            Descending
        """
        a=['Off','Ascending','Descending']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a, expected_ticked_list=['Off'], msg='Step06: Verify menu in query pane')
        time.sleep(2)
        """
            Step 07 : Click Ascending
        """
        utillobj.select_or_verify_bipop_menu('Ascending')
        time.sleep(2)
        """
            Step 08: Verify preview updated following
        """
        time.sleep(5)
        parent_css=("#pfjTableChart_1 text[class^='xaxis'][class$='title']")
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        expected_xval_list=['DVD Players - Porta...', 'Portable TV', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'Streaming', 'Handheld', 'iPod Docking Station', 'Tablet', 'Professional', 'Universal Remote C...', 'Receivers', 'Video Editing', 'Smartphone', 'Standard', 'Headphones', 'Flat Panel TV', 'Home Theater Syst...', 'Speaker Kits', 'Blu Ray']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 08:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 08:02: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 08:03: Verify second bar color")
        resultobj.verify_riser_legends('TableChart_1',['Cost of Goods', 'Revenue'], 'Step 08.04 : Verify chart legends')
        resultobj.verify_number_of_riser('TableChart_1', 1, 42, 'Step 08.05: Verify Number chart segment')
        time.sleep(2)
        resultobj.verify_xaxis_title('TableChart_1', 'Product Subcategory', "Step 08:06: Verify X-Axis Title")
        """
            Step 09 : Right click on Horizontal axis > Hover on Sort by Total Value
            Step 10 : Verify Ascending option selected
        """
        metadataobj.querytree_field_click('Horizontal Axis', 1, 1)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu('Sort By Total Value')
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu(expected_ticked_list=['Ascending'], msg='Step 10: Verify Ascending option selected')
        time.sleep(2)
        """
            Step 11: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css=("#jschart_HOLD_0 text[class^='xaxis'][class$='title']")
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(2)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        expected_xval_list=['DVD Players - Porta...', 'Portable TV', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'Streaming', 'Handheld', 'iPod Docking Station', 'Tablet', 'Professional', 'Universal Remote...', 'Receivers', 'Video Editing', 'Smartphone', 'Standard', 'Headphones', 'Flat Panel TV', 'Home Theater Syst...', 'Speaker Kits', 'Blu Ray']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 11:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 11:02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar!", "pale_green", "Step 11:03: Verify second bar color")
        resultobj.verify_riser_legends('jschart_HOLD_0',['Cost of Goods', 'Revenue'], 'Step 11.04 : Verify chart legends')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 42, 'Step 11.05: Verify Number chart segment')
        time.sleep(2)
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Subcategory', "Step 11:06: Verify X-Axis Title")
        """
            Step 12 : Hover on first and last riser of "Revenue" value and verify tooltip value
        """
        expected_tooltip_list=['Product Subcategory:DVD Players - Portable', 'Revenue:$571,726.77']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s1!g5!mbar!", expected_tooltip_list, "Step 12:01: Hover on first Revenue value n verify tooltip value")
        time.sleep(1)
        expected_tooltip_list=['Product Subcategory:Blu Ray', 'Revenue:$232,884,116.13']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s1!g0!mbar!", expected_tooltip_list, "Step 12:02: Hover on last riser n verify tooltip value")
        time.sleep(1)
        """
            Step 13 : Dismiss run window
        """
        
        """
            Step 14 : Click Save in the toolbar > Save as "C2334509" > Click Save 
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(1)
        obj1=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step14', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """
            Step 15 : Run the chart with API call
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P292_S10660&BIP_item=C2334509.FEX
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10660_chart_2", 'mrid', 'mrpass')
        time.sleep(6)
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(2)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        expected_xval_list=['DVD Players - Porta...', 'Portable TV', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'Streaming', 'Handheld', 'iPod Docking Station', 'Tablet', 'Professional', 'Universal Remote...', 'Receivers', 'Video Editing', 'Smartphone', 'Standard', 'Headphones', 'Flat Panel TV', 'Home Theater Syst...', 'Speaker Kits', 'Blu Ray']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 15:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 15:02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar!", "pale_green", "Step 15:03: Verify second bar color")
        resultobj.verify_riser_legends('jschart_HOLD_0',['Cost of Goods', 'Revenue'], 'Step 15.04 : Verify chart legends')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 42, 'Step 15.05: Verify Number chart segment')
        time.sleep(2)
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Subcategory', "Step 15:06: Verify X-Axis Title")
        """
            Step 16 :Close output window.
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        """
            Step 17 : Restore the saved fex using API
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2334509.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_2', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(5)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        expected_xval_list=['DVD Players - Porta...', 'Portable TV', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'Streaming', 'Handheld', 'iPod Docking Station', 'Tablet', 'Professional', 'Universal Remote...', 'Receivers', 'Video Editing', 'Smartphone', 'Standard', 'Headphones', 'Flat Panel TV', 'Home Theater Syst...', 'Speaker Kits', 'Blu Ray']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 17:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 17:02: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 17:03: Verify second bar color")
        resultobj.verify_riser_legends('TableChart_1',['Cost of Goods', 'Revenue'], 'Step 17.04 : Verify chart legends')
        resultobj.verify_number_of_riser('TableChart_1', 1, 42, 'Step 17.05: Verify Number chart segment')
        time.sleep(2)
        resultobj.verify_xaxis_title('TableChart_1', 'Product Subcategory', "Step 17:06: Verify X-Axis Title")
        """
            Step 18 : Right click on Horizontal axis > Hover on Sort by Total Value > Select Off
        """
        metadataobj.querytree_field_click('Horizontal Axis', 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Sort By Total Value')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Off')
        time.sleep(2)
        """
            Step 19 : Verify preview updated following
        """
        time.sleep(5)
        parent_css=("#TableChart_1 text[class^='xaxis'][class$='title']")
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        expected_xval_list=['Blu Ray', 'Speaker Kits', 'Home Theater Systems', 'Flat Panel TV', 'Headphones', 'Standard', 'Smartphone', 'Video Editing', 'Receivers', 'Universal Remote Controls', 'Professional', 'Tablet', 'iPod Docking Station', 'Handheld', 'Streaming', 'DVD Players', 'Charger', 'CRT TV', 'Boom Box', 'Portable TV', 'DVD Players - Portable']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 19:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 19:02: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 19:03: Verify second bar color")
        resultobj.verify_riser_legends('TableChart_1',['Cost of Goods', 'Revenue'], 'Step 19.04 : Verify chart legends')
        resultobj.verify_number_of_riser('TableChart_1', 1, 42, 'Step 19.05: Verify Number chart segment')
        time.sleep(2)
        resultobj.verify_xaxis_title('TableChart_1', 'Product Subcategory', "Step 19:06: Verify X-Axis Title")
        time.sleep(1)
        """
            Step 20 : Right click on Horizontal axis > Hover on Sort by Total Value > Descending
        """
        metadataobj.querytree_field_click('Horizontal Axis', 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Sort By Total Value')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Descending')
        time.sleep(2)
        
        """
            Step 21 : Verify preview updated
        """
        time.sleep(5)
        parent_css=("#TableChart_1 text[class^='xaxis'][class$='title']")
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Porta...', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Syst...', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote C...', 'Video Editing', 'iPod Docking Station']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 21:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 21:02: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 21:03: Verify second bar color")
        resultobj.verify_riser_legends('TableChart_1',['Cost of Goods', 'Revenue'], 'Step 21.04 : Verify chart legends')
        resultobj.verify_number_of_riser('TableChart_1', 1, 42, 'Step 21.05: Verify Number chart segment')
        time.sleep(2)
        resultobj.verify_xaxis_title('TableChart_1', 'Product Subcategory', "Step 21:06: Verify X-Axis Title")
        time.sleep(1)
        """
            Step 22 : Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        parent_css=("#jschart_HOLD_0 text[class^='xaxis'][class$='title']")
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        expected_xval_list=['Blu Ray', 'Speaker Kits', 'Home Theater Systems', 'Flat Panel TV', 'Headphones', 'Standard', 'Smartphone', 'Video Editing', 'Receivers', 'Universal Remote Controls', 'Professional', 'Tablet', 'iPod Docking Station', 'Handheld', 'Streaming', 'DVD Players', 'Charger', 'CRT TV', 'Boom Box', 'Portable TV', 'DVD Players - Portable']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 22:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 22:02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar!", "pale_green", "Step 22:03: Verify second bar color")
        resultobj.verify_riser_legends('jschart_HOLD_0',['Cost of Goods', 'Revenue'], 'Step 22.04 : Verify chart legends')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 42, 'Step 22.05: Verify Number chart segment')
        time.sleep(2)
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Subcategory', "Step 21:06: Verify X-Axis Title")
        time.sleep(1)
        """
            Step 23 : Hover on first and last riser of "Revenue" value and verify tooltip value
        """
        expected_tooltip_list=['Product Subcategory:Blu Ray', 'Revenue:$232,884,116.13']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s1!g0!mbar!", expected_tooltip_list, "Step 23:01: Hover on FIRST riser n verify tooltip value")
        time.sleep(1)
        expected_tooltip_list=['Product Subcategory:DVD Players - Portable', 'Revenue:$571,726.77']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s1!g5!mbar!", expected_tooltip_list, "Step 23:01: Hover on FIRST riser n verify tooltip value")
        time.sleep(1)
        
        """
            Step 24 : Right click on Horizontal axis > Hover on Sort by Total Value 
            Verification : Expected to see Descending selected
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(1)
        metadataobj.querytree_field_click('Horizontal Axis', 1, 1)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu('Sort By Total Value')
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu(expected_ticked_list=['Descending'], msg='Step 24: Verify Dscending option selected')
        time.sleep(2)
        
        """
            Step 25 : Logout using API (without saving)
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        


if __name__ == "__main__":
    unittest.main()