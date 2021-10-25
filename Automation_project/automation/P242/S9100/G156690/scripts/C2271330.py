'''-------------------------------------------------------------------------------------------
Created on January 10, 2019
@author: Prasanth

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2271330
Test Case Title =  Controls Group
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2271330_TestClass(BaseTestCase):
    
    def test_C2271330(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
         
        """
            COMMON TEST CASE VARIABLES 
        """
        EDIT_BOX_TOOLTIP       = 'Edit Box Insert Edit Box'
        DROP_DOWN_TOOLTIP      = 'Drop Down Insert Drop Down'
        LIST_BOX_TOOLTIP       = 'List Box Insert List Box'
        RADIO_BUTTON_TOOLTIP   = 'Radio Button Insert Radio Button'
        CHECK_BOX_TOOLTIP      = 'Check Box Insert Check Box'
        

        """
            STEP 01 : Hover on Edit Box
            STEP 01 Expected : Tool tip displays: Edit Box Insert Edit Box
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Controls.EditBox, EDIT_BOX_TOOLTIP, '01.01' )
        
        """
            STEP 02 : Hover on Drop Down
            STEP 02 Expected : Tool tip displays: Drop Down Insert Drop Down
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Controls.DropDown, DROP_DOWN_TOOLTIP, '02.01' )
        
        """
            STEP 03 : Hover on List Box
            STEP 03 Expected : Tool tip displays: List Box Insert List Box
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Controls.ListBox, LIST_BOX_TOOLTIP, '03.01', crop_x1=40)
        
        """
            STEP 04 : Hover on Radio Button
            STEP 04 Expected : Tool tip displays: Radio Button Insert Radio Button
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Controls.RadioButton, RADIO_BUTTON_TOOLTIP, '04.01' )
        
        """
            STEP 05 : Hover on Check Box
            STEP 05 Expected : Tool tip displays: Check Box Insert Check Box
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Controls.CheckBox, CHECK_BOX_TOOLTIP, '05.01', image_size=300 )
       
if __name__=='__main__' :
    unittest.main()