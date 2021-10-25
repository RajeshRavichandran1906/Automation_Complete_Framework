'''-------------------------------------------------------------------------------------------
Created on January 10, 2019
@author: Prasanth

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270250
Test Case Title =  Help Tooltip
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2270250_TestClass(BaseTestCase):
    
    def test_C2270250(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
         
        """
            COMMON TEST CASE VARIABLES 
        """
        HELP_TOOLTIP = '@ Help Topics List Help topics'
        
        """
            STEP 01 : Hover mouse over the Help icon at the top right of AS window.
            STEP 01 Expected : Tooltip displays: Help Topics. List Help topics.
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HelpMenu.Help, HELP_TOOLTIP, '01.01')
        
       
if __name__=='__main__' :
    unittest.main()