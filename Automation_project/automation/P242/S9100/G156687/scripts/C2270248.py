'''-------------------------------------------------------------------------------------------
Reworked on January 10, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270248
Test Case Title =  WebFOCUS Administration Tooltip
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2270248_TestClass(BaseTestCase):

    def test_C2270248(self):
       
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            STEP 01 : Hover on "WebFOCUS Administration" label at the top right of the AS window
            STEP 01 Expected : Tool tip displays: WebFOCUS Administration WebFOCUS Administration tools.
        """
        WEBFOCUS_ADMINSTRATION_TOOLTIP = 'WebFOCUS Administration WebFOCUS Administration tools'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.WebFOCUSAdministrationMenu.WebFOCUSAdministration, WEBFOCUS_ADMINSTRATION_TOOLTIP, '01.01')
        
if __name__=='__main__' :
    unittest.main()