'''
Created on Sep 25, 2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324240
TestCase Name = Run Mode_Run Tree : Portal Designer_Design Properties : Test_For_Style
'''

import unittest, time
from common.lib import utillity, core_utility
from common.pages import wf_legacymainpage, ia_styling, vfour_portal_ribbon, vfour_portal_canvas
from common.lib.basetestcase import BaseTestCase

class C2324240_TestClass(BaseTestCase):

    def test_C2324240(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        v4p_ribbon=vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        v4p_canvas=vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        sty_obj=ia_styling.IA_Style(self.driver)
        proj_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        parent_folder_name='BIP_V4_Portal'
        BIP_Portal_Path = str(proj_id)+'->'+str(suite_id)+'->'+parent_folder_name
        
        """    1. Sign into WebFOCUS home page as Developer User
                   Navigate URL to http://environment_name:port/alias/legacyhome    """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css="#bipTreePanel tbody tr:nth-child(1)> td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        
        """    2. Right click on 'BIP_xxx_Portal123_V4' and Edit the portal.    """
        wf_mainobj.select_repository_menu(BIP_Portal_Path+'->BIP_xxx_Portal123_V4', 'Edit')
        time.sleep(5)
        core_utilobj.switch_to_new_window()
        element_css="#applicationButton img"
        utillobj.synchronize_with_number_of_element(element_css, 1, 190)
        
        """    3. Click the theme button and change it to red. The next few steps cant be done with the neutral theme    """
        v4p_ribbon.select_or_verify_layout_base_theme(button_click='OK',theme_name='Red')
        time.sleep(5)
        v4p_ribbon.select_or_verify_top_banner(bg_color='chestnut_red',msg='Step 03 : Verify the theme applied in portal design mode')
        
        """    4. Select 'Test_Page'. Click on Style Tab;    """
        v4p_canvas.select_page_in_navigation_bar('Test_Page')
        time.sleep(8)
        
        """    5. Click on Image Icon and Change the background image to any uploaded image.    """
        v4p_ribbon.select_ribbon_item("Style", "Style_Image")
        time.sleep(8)
        v4p_canvas.open_files_from_repository_window(BIP_Portal_Path, ['honda_integra'], msg="Step 5: ")
        background_image=v4p_canvas.get_current_page()
        bg_image=background_image.value_of_css_property('background-image')
        utillobj.asin('honda_integra', bg_image, 'Step 05.1: Verify background image applied')
        
        """    6. Change Repeat background image(click on Repeat icon) to Horizontally;    """
        v4p_ribbon.select_ribbon_item("Style", "Style_Repeat")
        btns=self.driver.find_elements_by_css_selector("#ChooseBackgroundRepeatWindow div[id^='BiToolBarRadioButton']")
        actual_btn_name_list=[el.text.strip() for el in btns]
        elem=btns[actual_btn_name_list.index('Horizontally')].find_element_by_css_selector("[class*='button'][class*='label']")
        utillobj.default_click(elem)
        time.sleep(8)
        background_image=v4p_canvas.get_current_page()
        bg_image=background_image.value_of_css_property('background-image')
        utillobj.asin('honda_integra', bg_image, 'Step 06: Verify background image exist')
        bg_image_horizontal_repeat=background_image.value_of_css_property('background-repeat')
        utillobj.asequal('repeat-x', bg_image_horizontal_repeat.lower(), "Step 06.1: Verify background image changed to Horizontally.")
        
        """    7. Change Background Position to Top Middle.        """
        v4p_ribbon.select_ribbon_item("Style", "Style_Position")
        elem=driver.find_element_by_css_selector("#ChooseBackgroundPositionWindow #BackgroundPosTopCenterClick")
        utillobj.default_click(elem)
        time.sleep(8)
        background_image=v4p_canvas.get_current_page()
        bg_image=background_image.value_of_css_property('background-image')
        utillobj.asin('honda_integra', bg_image, 'Step 07: Verify background image exist')
        bg_image_postion=background_image.value_of_css_property('background-position')
        utillobj.asequal('50% 0%', bg_image_postion, "Step 07.1: Verify background image changed to Horizontally.")
        
        """    8. Change the theme back to neutral    """
        v4p_ribbon.select_or_verify_layout_base_theme(button_click='OK',theme_name='Neutral')
        time.sleep(8)
        v4p_ribbon.select_or_verify_top_banner(bg_color='Zambezi_grey',msg='Step 08a : Verify Neutral theme applied in portal design mode')
        background_image=v4p_canvas.get_current_page()
        bg_image=background_image.value_of_css_property('background-image')
        utillobj.asin('honda_integra', bg_image, 'Step 08b: Verify background image exist with neutral theme')
        
        
        """    9. Select the menubar links area by clicking on the menubar links in banner. Change the Menubar background color to Yellow;    """
        elem=driver.find_element_by_css_selector("div[class*='bip-menu-bar-item'][style*='inherit']")
        utillobj.default_click(elem)
        time.sleep(5)
        v4p_ribbon.select_ribbon_item("Style", "Style_background_color")
        time.sleep(5)
        sty_obj.set_color("yellow")
        
        """    10. Change the MenuBar Style to Solid, Menubar Border width to 4px;    """
        v4p_ribbon.select_ribbon_item("Style", "Style_Style")
        v4p_ribbon.select_border_style("solid")
        v4p_ribbon.select_ribbon_item("Style", "Style_border_width_up")
        time.sleep(2)
        v4p_ribbon.select_ribbon_item("Style", "Style_border_color")
        time.sleep(5)
                
        """    11. Border Color to Red;    """
        sty_obj.set_color("red")
        
        """    12. Change the menubar font to Arial, Bold, Italicized, and Underline; Font color to Blue; font size to 9px;    """
        utillobj.select_combobox_item("FieldFontFamily", "Arial")
        time.sleep(2)
        v4p_ribbon.select_ribbon_item("Style", "Style_font_bold")
        time.sleep(2)
        v4p_ribbon.select_ribbon_item("Style", "Style_font_italic")
        time.sleep(2)
        v4p_ribbon.select_ribbon_item("Style", "Style_font_underline")
        time.sleep(2)
        v4p_ribbon.select_ribbon_item("Style", "Style_font_color")
        time.sleep(5)
        sty_obj.set_color("blue")
        time.sleep(2)
        utillobj.select_combobox_item("FieldFontSize", "9")
        time.sleep(2)
        v4p_ribbon.verify_menu_bar_style(menu_item_font_name='Arial', menu_item_font_size=9, menu_item_bold=True, menu_item_italic=True, 
                                                     menu_item_underline=True, border_width=4, menu_item_text_color='blue',
                                                     border_color='red', border_style='solid', menubar_background='yellow')
        
        """    13. Save and exit the portal.    """
        v4p_ribbon.select_tool_menu_item('menu_Save')
        time.sleep(2)
        v4p_ribbon.select_tool_menu_item('menu_Exit')
        time.sleep(2)
        
        """    14. Sign Out from WebFOCUS    """
        core_utilobj.switch_to_previous_window(window_close=False)
        
        
if __name__ == '__main__':
    unittest.main()