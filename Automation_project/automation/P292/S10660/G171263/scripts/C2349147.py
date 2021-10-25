'''
Created on DEC 06, 2017

@author: Pavithra/Updated by : Bhagavathi

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2349147
TestCase Name = Verify Sort By Total Value menu is displayed in the Vertical Axis when chart type is rotated
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,ia_ribbon
from common.lib.basetestcase import BaseTestCase

class C2349147_TestClass(BaseTestCase):

    def test_C2349147(self):
        
        Test_Case_ID = "C2349147"
        driver = self.driver
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        parent_css="#queryTreeWindow"
        
        """        
            Step 01:Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10660_chart_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        """        
            Step 02:Select Format > Chart Types > Other > Bar > Stacked Bar
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        time.sleep(5) 
        ia_ribbonobj.select_other_chart_type('bar', 'vertical_stacked_bars', 2, ok_btn_click=True)
        time.sleep(5)

        """
            Step 03:Double click "Cost of Goods", "Revenue" and "Product, SubCategory"
        """ 
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        utillobj.synchronize_with_visble_text(parent_css, "Cost of Goods", 15)
        
        metaobj.datatree_field_click("Revenue", 2, 1)
        utillobj.synchronize_with_visble_text(parent_css, "Revenue", 15)
        
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        utillobj.synchronize_with_visble_text(parent_css, "Product,Subcategory", 15)

        resobj.verify_xaxis_title("TableChart_1", 'Product Subcategory', "Step 03.01: Verify X-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 03.02: Verify XY Label')
        expected_label_list=['Cost of Goods', 'Revenue']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 03.03: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar!', 'bar_green', 'Step 03.04: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 03.05: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 42, 'Step 03.06: Verify the total number of risers displayed on preview')
        
        """
            Step 04:Right-click Horizontal Axis > Verify menu with "Sort By Total Value"
        """
        metaobj.querytree_field_click("Horizontal Axis",1,1)
        utillobj.select_or_verify_bipop_menu(verify=True,expected_popup_list=['New Parameter', 'Suppress Empty Group', 'Sort By Total Value'],msg='Step 04.01: Verify menu with "Sort By Total Value')
        
        """
            Step 05:Right-click Vertical Axis > Verify menu ("Sort By Total Value" should not be available)
        """
        metaobj.querytree_field_click("Vertical Axis",1,1)
        utillobj.select_or_verify_bipop_menu(verify=True,expected_popup_list=['New Parameter', 'Multi-Y split'],msg='Step 05.01: Verify menu ("Sort By Total Value" should not be available)')
        
        """
            Step 06:Select Format Tab > Select "Rotate"
        """
        ribbonobj.select_visualization_ribbon_item('Format', 'features')
        ribbonobj.select_visualization_ribbon_item('Format','rotate')
#         ribbonobj.select_ribbon_item('Format', 'rotate')
        parent_css = '#queryTreeWindow tr:nth-child(10) td'
        utillobj.synchronize_with_visble_text(parent_css, "Revenue", 15)
        
        """
            Step 07:Right-click Horizontal Axis > Verify menu ("Sort By Total Value" should not be available once chart is rotated)
        """
        metaobj.querytree_field_click("Horizontal Axis",1,1)
        utillobj.select_or_verify_bipop_menu(verify=True,expected_popup_list=['New Parameter', 'Multi-Y split'],msg='Step 07.01: Verify menu ("Sort By Total Value" should not be available once chart is rotated)')
        
        """
            Step 08:Right-click Vertical Axis > Verify menu with "Sort By Total Value"
        """
        metaobj.querytree_field_click("Vertical Axis",1,1)
        utillobj.select_or_verify_bipop_menu(verify=True,expected_popup_list=['New Parameter', 'Suppress Empty Group', 'Sort By Total Value'],msg='Step 08.01: Verify menu with "Sort By Total Value')
        
        
        """
            Step 09:Select "Sort By Total Value" > "Descending"
        """
        utillobj.select_or_verify_bipop_menu('Sort By Total Value')
        utillobj.select_or_verify_bipop_menu('Descending')
        
        """
            Step 10:Verify Live Preview
        """
        resobj.verify_xaxis_title("TableChart_1", 'Product Subcategory', "Step 10.01: Verify X-Axis Title")
        expected_xval_list=['Blu Ray', 'Speaker Kits', 'Home Theater Systems', 'Flat Panel TV', 'Headphones', 'Standard', 'Smartphone', 'Video Editing', 'Receivers', 'Universal Remote Controls', 'Professional', 'Tablet', 'iPod Docking Station', 'Handheld', 'Streaming', 'DVD Players', 'Charger', 'CRT TV', 'Boom Box', 'Portable TV', 'DVD Players - Portable']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 10.02: Verify XY Label')
        expected_label_list=['Cost of Goods', 'Revenue']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 10.03: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar!', 'bar_green', 'Step 10.04: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 10.05: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 42, 'Step 10.06: Verify the total number of risers displayed on preview')
        
        """
            Step 11:lick Save in the toolbar > Save as "C2349147" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 12:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
            
        """
            Step 13:Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2349147.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10660_chart_2', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1 g.legend text[class*='s1']"
        utillobj.synchronize_with_visble_text(parent_css, "Revenue", 70)
        
        """
            Step 14:Verify Live Preview
        """
        resobj.verify_xaxis_title("TableChart_1", 'Product Subcategory', "Step 14.01: Verify X-Axis Title")
        expected_xval_list=['Blu Ray', 'Speaker Kits', 'Home Theater Systems', 'Flat Panel TV', 'Headphones', 'Standard', 'Smartphone', 'Video Editing', 'Receivers', 'Universal Remote Controls', 'Professional', 'Tablet', 'iPod Docking Station', 'Handheld', 'Streaming', 'DVD Players', 'Charger', 'CRT TV', 'Boom Box', 'Portable TV', 'DVD Players - Portable']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 14.02: Verify XY Label')
        expected_label_list=['Cost of Goods', 'Revenue']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 14.03: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar!', 'bar_green', 'Step 14.04: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 14.05: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 42, 'Step 14.06: Verify the total number of risers displayed on preview')
        
        """
            Step 15:Click Run in the toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
            
        """
            Step 16:Verify output
        """
        
        utillobj.synchronize_with_visble_text('#jschart_HOLD_0','Product Subcategory',90)
        resobj.verify_xaxis_title("jschart_HOLD_0", 'Product Subcategory', "Step 16.01: Verify X-Axis Title")
        expected_xval_list=['Blu Ray', 'Speaker Kits', 'Home Theater Systems', 'Flat Panel TV', 'Headphones', 'Standard', 'Smartphone', 'Video Editing', 'Receivers', 'Universal Remote Controls', 'Professional', 'Tablet', 'iPod Docking Station', 'Handheld', 'Streaming', 'DVD Players', 'Charger', 'CRT TV', 'Boom Box', 'Portable TV', 'DVD Players - Portable']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        resobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 16.02: Verify XY Label')
        resobj.verify_number_of_riser("jschart_HOLD_0", 1, 42, 'Step 16.03: Verify the total number of risers ')
        utillobj.verify_chart_color('jschart_HOLD_0', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 16.04: Verify Color')
        expected_label_list=['Cost of Goods', 'Revenue']
        resobj.verify_riser_legends('jschart_HOLD_0', expected_label_list, 'Step 16.05: Verify Legends ')
        
        """
            Step 17:Select Format Tab > Click on "Rotate" to deselect option
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(5)
        ribbonobj.select_visualization_ribbon_item('Format', 'features')
        ribbonobj.select_visualization_ribbon_item('Format','rotate')
#         ribbonobj.select_ribbon_item('Format', 'rotate')
        parent_css="#queryTreeWindow tr:nth-child(10) td"
        utillobj.synchronize_with_visble_text(parent_css, "Product,Subcategory", 35)
         
        """
            Step 18:Verify Live Preview
        """
        resobj.verify_xaxis_title("TableChart_1", 'Product Subcategory', "Step 18.01: Verify X-Axis Title")
        expected_xval_list=['Blu Ray', 'Speaker Kits', 'Home Theater Systems', 'Flat Panel TV', 'Headphones', 'Standard', 'Smartphone', 'Video Editing', 'Receivers', 'Universal Remote Controls', 'Professional', 'Tablet', 'iPod Docking Station', 'Handheld', 'Streaming', 'DVD Players', 'Charger', 'CRT TV', 'Boom Box', 'Portable TV', 'DVD Players - Portable']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 18.02: Verify XY Label')
        expected_label_list=['Cost of Goods', 'Revenue']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 18.03: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar!', 'bar_green', 'Step 18.04: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 18.05: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 42, 'Step 18.06: Verify the total number of risers displayed on preview')
        
        """
            Step 19:Right-click Horizontal Axis > Verify menu "Sort By Total Value" > "Descending" appears selected
        """
        metaobj.querytree_field_click("Horizontal Axis",1,1)
        utillobj.select_or_verify_bipop_menu('Sort By Total Value')
        utillobj.select_or_verify_bipop_menu(expected_ticked_list=['Descending'],msg='Step 19.01: Verify menu "Sort By Total Value" > "Descending" appears selected')
   
        """
            Step 20:Click Save > OK
        """
        ribbonobj.select_tool_menu_item('menu_save')
        btn_ok=driver.find_element_by_css_selector("[id^='BiOptionPane'] div[id^='BiButton']")
        utillobj.default_left_click(object_locator=btn_ok)
                
        """
            Step 21:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
        time.sleep(5) 

if __name__ == '__main__':
    unittest.main()