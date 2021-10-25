'''
Created on 21-Sep-2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324219
TestCase Name = Portal Designer_Layout : Change_Layout_options_from_Layout_tab
'''

import unittest, time
from common.lib import utillity
from common.lib import core_utility
from common.pages import vfour_portal_ribbon,vfour_portal_canvas, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324219_TestClass(BaseTestCase):

    def test_C2324219(self):
        
        workspace = "Workspaces"
        utiliobj=utillity.UtillityMethods(self.driver)
        core_utiliobj=core_utility.CoreUtillityMethods(self.driver)
        mainpage = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        v4p_ribbon=vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        v4p_canvas=vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        project_id=utiliobj.parseinitfile('project_id')
        suite_id=utiliobj.parseinitfile('suite_id')
        folder_path=project_id+'->'+suite_id
        user_name = utiliobj.parseinitfile('mrid03')
        
        '''
        Step 01 : Sign in as WF Developer
        '''
        utiliobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utiliobj.synchronize_with_visble_text(parent_css, workspace, 190) 
           
        '''
        Step 02 : Edit 'BIP_xxx_Portal123_V4' portal
        '''
        mainpage.select_repository_menu(folder_path+'->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
        time.sleep(5)
        core_utiliobj.switch_to_new_window()
        utiliobj.synchronize_with_number_of_element("#applicationButton img",1, 120)
           
        '''
        Step 03 : From layout tab; Click on the Banner button and choose Left; 
        Verify that the banner now appears on the left
        '''
        v4p_ribbon.select_layout_banner(banner_area='Left', verify=True, expected_banner_name_list=['Top','Bottom','Left','Right'],msg='Step 03.1 : Verify layout banner buttons',close=True)
        time.sleep(3)
        v4p_canvas.verify_banner_position('left','Step 03.2 : Verify that the banner now appears on the left')
          
        '''
        Step 04 : Click on menubar link and select Menu Bar dropdown form the layout tab
        Change the Menubar position to Top center with Center alignment
        '''
        menus=[user_name, 'Tools', 'Administration', 'Resources', 'Help', 'Close', 'Sign Out']
        v4p_ribbon.select_or_verify_menu_bar(select=True,menu_list=menus,msg='Step 04.1 : Verify menu bar names') 
        v4p_ribbon.select_layout_menubar('topcenter_32',verify=True,expected_no_of_btns=15,msg='Step 04.2 : Verify no of menu bar alignment options')
        time.sleep(3)
        v4p_ribbon.select_or_verify_menu_bar(menu_list=menus,position='center',msg='Step 04.2 : Verify menu bar names') 
          
        '''
        Step 05 : Click on the Theme button.Change the Theme to Red color Click OK
        '''
        v4p_ribbon.select_or_verify_layout_base_theme(button_click='OK',default_theme_name='Neutral',theme_name='Red',msg='Step 05.0 : Verify default theme')
        time.sleep(2)
          
        '''
        Step 05.1 : Verify the changes are reflected in the portal design mode.
        '''
        v4p_ribbon.select_or_verify_top_banner(bg_color='chestnut_red',msg='Step 05.1 : Verify the changes are reflected in the portal design mode')
         
        '''
        Step 06.0 : Select Page 1 Change the page layout to 4 columns from Ribbon-> Layout button.
        Right click on the page canvas and choose page layout then 4 columns or click on the layout button and choose 4 Columns.
        '''
        expected_list=["Single Area", "Fluid Canvas", "One Column", "Two Column", "Three Column", "Four Column"]
        v4p_canvas.select_page_in_navigation_bar('Page 1')
        time.sleep(3)
        v4p_ribbon.select_layout_layout(navigate_item="Four Column",verify=True,expected_btn_name_list=expected_list,msg='Step 06.1 : Verify layout options')
        time.sleep(10)
        
        '''
        Step 06.1 : Verify the changes are reflected in portal design mode by clicking on the areas in the page canvas to make sure the outlines show
        '''
        v4p_canvas.verify_column_selected(1,'top','Step 06.2 : Verify the changes are reflected in portal design mode by clicking on the areas in the page canvas to make sure the outlines show')
        v4p_canvas.verify_column_selected(2,'left','Step 06.3 : Verify the changes are reflected in portal design mode by clicking on the areas in the page canvas to make sure the outlines show')
        v4p_canvas.verify_column_selected(3,'right','Step 06.4 : Verify the changes are reflected in portal design mode by clicking on the areas in the page canvas to make sure the outlines show')
        v4p_canvas.verify_column_selected(4,'bottom','Step 06.5 : Verify the changes are reflected in portal design mode by clicking on the areas in the page canvas to make sure the outlines show')
        
        '''
        Step 06.2 : Right click on the page canvas and choose page layout then 4 columns or click on the layout button and choose 4 Columns.
        '''
        v4p_ribbon.select_layout_from_page_canvas(navigate_item='Four Column',verify=True,expected_btn_name_list=expected_list,msg='Step 06.6 : Verify layout options')
        time.sleep(3)
        
        '''
        Step 06.3 : Verify the changes are reflected in portal design mode by clicking on the areas in the page canvas to make sure the outlines show
        '''
        v4p_canvas.verify_column_selected(1,'top','Step 06.7 : Verify the changes are reflected in portal design mode by clicking on the areas in the page canvas to make sure the outlines show')
        v4p_canvas.verify_column_selected(2,'left','Step 06.8 : Verify the changes are reflected in portal design mode by clicking on the areas in the page canvas to make sure the outlines show')
        v4p_canvas.verify_column_selected(3,'right','Step 06.9 : Verify the changes are reflected in portal design mode by clicking on the areas in the page canvas to make sure the outlines show')
        v4p_canvas.verify_column_selected(4,'bottom','Step 06.10 : Verify the changes are reflected in portal design mode by clicking on the areas in the page canvas to make sure the outlines show')
        
        '''
        Step 07 : Save and exit portal
        '''
        v4p_ribbon.select_tool_menu_item('menu_Save')
        v4p_ribbon.select_tool_menu_item('menu_Exit')
        core_utiliobj.switch_to_previous_window(window_close=False)
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()