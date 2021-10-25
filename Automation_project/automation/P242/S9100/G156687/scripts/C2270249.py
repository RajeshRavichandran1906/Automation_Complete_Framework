'''-------------------------------------------------------------------------------------------
Created on January 10, 2019
@author: Prasanth

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270249
Test Case Title =  Controls Group
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2270249_TestClass(BaseTestCase):
    
    def test_C2270249(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
         
        """
            COMMON TEST CASE VARIABLES 
        """
        STYLE_TOOLTIP  =  'Modify Visual Style Choose one of the Office 2007 themes'
        
        """
            STEP 01 : Hover on Edit Box
            STEP 01 Expected : Tool tip displays: Edit Box Insert Edit Box
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.StyleMenu.Style, STYLE_TOOLTIP,'01.01' )
        
        
if __name__=='__main__' :
    unittest.main()