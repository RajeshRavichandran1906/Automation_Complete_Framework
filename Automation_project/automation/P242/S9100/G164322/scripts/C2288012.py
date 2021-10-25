'''-------------------------------------------------------------------------------------------
Reworked on January 29, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288102
Test Case Title =  View Options Menu
-----------------------------------------------------------------------------------------------'''
import unittest
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import ToolBarMenu


class C2288102_TestClass(BaseTestCase):
    
    def test_C2288102(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
         
        """
            STEP 01.01 : Click on the View Options icon
        """
        EXPECTED_VIEW_GROUP_OPTIONS = ['View items sorted in Alphabetical order', 'View items sorted in reverse Alphabetical order', 'View items sorted in Chronological order', 'View items sorted in reverse Chronological order', 'View items grouped by File Type', 'Respect Sort Order Property', 'View items by Title', 'View items by Name', 'Refresh View']
        ToolBarMenu.verify_view_options(EXPECTED_VIEW_GROUP_OPTIONS, '01.01')
        
if __name__=='__main__' :
    unittest.main()         
        