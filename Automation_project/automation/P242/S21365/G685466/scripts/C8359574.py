'''-------------------------------------------------------------------------------------------
Created on January 10, 2019
@author: Prasanth

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8359574
Test Case Title =  Style Tooltip
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C8359574_TestClass(BaseTestCase):
    
    def test_C8359574(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
         
        """
            COMMON TEST CASE VARIABLES 
        """
        STYLE_TOOLTIP  = 'Modify Visual Style Choose one of the themes'
        
        """
            STEP 01 : Hover on Style at the top right of AS window.
            STEP 01 Expected : Tool tip displays: Modify Visual Style Choose one of the themes.
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.StyleMenu.Style, STYLE_TOOLTIP,'01.01' )
        
if __name__=='__main__' :
    unittest.main()