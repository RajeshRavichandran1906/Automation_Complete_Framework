'''-------------------------------------------------------------------------------------------
Reworked on January 18, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2271424
Test Case Title =  Verify the contextual menu for a folder and a new folder under Domains.
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
import unittest
from appstudio.tools.common.ribbon import Ribbon

class C2271424_TestClass(BaseTestCase):
    
    def test_C2271424(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            STEP 01.01 : Click on "Data" tab
        """
        Ribbon.select_tab(Ribbon.Locators.DataTab.DATA)
    
        """
            STEP 01.02 : Hover on "Summary (Compute)"
            STEP 01.02 Expected : Tool tip displays: Summary (Compute) Manage calculated values   
        """
        SUMMARY_COMPUTE_TOOLTIP = 'Summary (Compute) Manage calculated values'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.DataTab.Calculation.SummaryCompute, SUMMARY_COMPUTE_TOOLTIP, '01.02')
        
        """
            STEP 01.03 : Hover on "Across Compute"
            STEP 01.03 Expected : Tool tip displays: Across Compute Add COMPUTE to Across field 
        """
        ACROSS_COMPUTE_TOOLTIP = 'Across Compute Add COMPUTE to Across field'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.DataTab.Calculation.AcrossCompute, ACROSS_COMPUTE_TOOLTIP, '01.02')
        
        """
            STEP 02.01 : Hover on "Forecast"
            STEP 02.01 Expected : Tool tip displays: Forecast Add a Forecast column to the report
        """
        FORECAST_TOOLTIP = 'Forecast  Add a Forecast column to the report'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.DataTab.Forecast.Forecast, FORECAST_TOOLTIP, '02.01', image_size=80)
        
        """
            STEP 03.01 : Hover on "Generate Parameter Group"
            STEP 03.01 Expected : Tool tip displays: Generate Parameter Group. Enable Guided Report prompting at runtime for the selected columns
        """
        GENERATE_PARAMETER_GROUP_TOOLTIP = 'Generate Parameter Group  Enable Guided Report prompting at runtime for the selected columns'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.DataTab.GuidedReport.GenerateReportGroup, GENERATE_PARAMETER_GROUP_TOOLTIP, '03.01', crop_x1=20)
        
        """
            STEP 03.02 : Hover on "Remove from Parameter Group"
            STEP 03.02 Expected : Tool tip displays: Remove from Parameter Group Remove Guided Report prompting for the selected columns
        """
        REMOVE_FROM_PARAMETER_GROUP_TOOLTIP = 'Remove from Parameter Group  Remove Guided Report prompting for the selected columns'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.DataTab.GuidedReport.RemoveFromParameterGroup, REMOVE_FROM_PARAMETER_GROUP_TOOLTIP, '03.02', image_size=80, crop_x1=23)
        
if __name__=='__main__' :
    unittest.main()