'''-------------------------------------------------------------------------------------------
Reworked on January 29, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2303737
Test Case Title =  TXT Domains Contextual New Menu
-----------------------------------------------------------------------------------------------'''
import unittest
from appstudio import settings
from appstudio.tools.common.ribbon import Ribbon
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common import environments as Environments


class C2303737_TestClass(BaseTestCase):
    
    def test_C2303737(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            STEP 01.01 : While App Studio is launched, verify the View group options
        """
        Ribbon.verify_tab_item_is_selected(Ribbon.Locators.HomeTab.View.EnvironmentsTree, '01.01')
        
        """
            STEP 01.02 : While App Studio is launched, verify the View group options
        """
        Ribbon.verify_tab_item_is_selected(Ribbon.Locators.HomeTab.View.ProcedureView, '01.02')
        
        """
            STEP 01.03 : While App Studio is launched, verify the View group options
        """
        Ribbon.verify_tab_item_is_unselected(Ribbon.Locators.HomeTab.View.HelpWizard, '01.03')
        
        """
            STEP 01.04 : While App Studio is launched, verify the View group options
        """
        Ribbon.verify_tab_item_is_unselected(Ribbon.Locators.HomeTab.View.EnvironmentsDetail, '01.04')
        
        """
            STEP 01.05 : While App Studio is launched, verify the View group options
        """
        Ribbon.verify_tab_item_is_unselected(Ribbon.Locators.HomeTab.View.ContextBar, '01.05')
        
        """
            STEP 01.06 : While App Studio is launched, verify the View group options
        """
        Ribbon.verify_tab_item_is_selected(Ribbon.Locators.HomeTab.View.FileFolderProperties, '01.06')
        
        """
            STEP 01.07 : While App Studio is launched, verify the View group options
        """
        Ribbon.verify_tab_item_is_unselected(Ribbon.Locators.HomeTab.View.StatusBar, '01.07')
        
        """
            STEP 02.01 : Environments Tree is checked by default. Un-check Environments Tree
            STEP 02.01 Expected : Environments Tree panel disappears
        """
        Ribbon.unselect_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsTree)
        Environments.Tree.verify_environment_tree_panel_not_exists('02.01')
        
        """
            STEP 02.02 : Check Environments Details.
            STEP 02.02 Expected : Environments Details panel displays along the left side.
        """
        Ribbon.select_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsDetail)
        Environments.Detail.verify_environment_details_panel_exists('02.03')
        
        """
            STEP 03.01 : Reselect Environments Tree
            STEP 03.01 Expected : Now both Tree and Details panels display. Environments Tree displays on the left of Environments Details
        """
        Ribbon.select_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsTree)
        Environments.Tree.verify_environment_tree_panel_exists('03.01')
        Environments.Detail.verify_environment_details_panel_exists('03.01')
        
        """
            STEP 04.01 : Close the Environments Details panel via the X at the top right corner of the panel
            STEP 04.01 Expected : The Environments Details check box in the Home ribbon is now deselected and only the Environments Tree panel is showing and is selected.
        """
        Environments.Detail.close_environment_details_panel_by_click_on_x_icon()
        Ribbon.verify_tab_item_is_unselected(Ribbon.Locators.HomeTab.View.EnvironmentsDetail, '04.01')
        
        """
            STEP 05.01 : Close the Environment Tree using the X at the top right of panel
            STEP 05.01 Expected : Neither panel is now displaying, and both are deselected in the Home ribbon
        """
        Environments.Tree.close_environment_tree_panel_by_click_on_x_icon()
        Ribbon.verify_tab_item_is_unselected(Ribbon.Locators.HomeTab.View.EnvironmentsDetail, '05.01')
        Ribbon.verify_tab_item_is_unselected(Ribbon.Locators.HomeTab.View.EnvironmentsTree, '05.01')
        
        Ribbon.select_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsTree)
        
if __name__=='__main__' :
    unittest.main()        
        