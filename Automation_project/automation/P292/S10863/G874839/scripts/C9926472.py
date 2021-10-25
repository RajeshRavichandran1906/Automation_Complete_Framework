"""------------------------------------------------------------------------
Author Name : Niranjan
Automated On : 5-September-2019
------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.login import Login
from common.lib.utillity import UtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C9926472_TestClass(BaseTestCase):

    def test_C9926472(self):
        
        """CLASS OBJECT"""
        main_page = Wf_Mainpage(self.driver)
        Login_page = Login(self.driver)
        utils = UtillityMethods(self.driver)
        locator_obj = WfMainPageLocators()
        
        """COMMON VARIABLES"""
        
        repository_folder = "Retail Samples->Reports"
                        
        step1 = """
        Launch WF_Home Page as Developer user.
        """
        Login_page.invoke_home_page('mrid','mrpass')
        utils.capture_screenshot("01.01",step1)
        
        step2 ="""
        Under Domain tree >> Navigate to Retail_Samples domain >> Click on 'Reports' folder.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        main_page.expand_repository_folder(repository_folder)
        utils.capture_screenshot("02.01",step2)

        step3 ="""Right click on Margin by Product Category >> Select 'Properties' from context menu.
        Properties dialog will open & Action Bar disappears.
        """
        
        utils.synchronize_with_visble_text(locator_obj.content_area_css,'Margin by Product Category',main_page.report_medium_timesleep)
        main_page.right_click_folder_item_and_select_menu('Margin by Product Category','Properties')
        utils.capture_screenshot("03.01",step3)
        
        step4 = """Under Properties dialog, Three tabs are showing in the properties dialog:
        General Tab.
        Advanced Tab.
        Query Details tab.
        """
        utils.synchronize_with_visble_text('.propPage', 'Margin by Product Category', main_page.report_medium_timesleep)
        main_page.verify_property_dialog_tab_list(['General', 'Advanced', 'Query Detail'],"Step 4")
        utils.capture_screenshot("04.01",step4)
 
        step5 = """Verify page when User click on each tab.
        General Tab:
        Advanced Tab:
        Query Details Tab:
        """
        """
        GENERAL TAB
        """
        
        main_page.verify_property_dialog_value('Title','text_value',"Margin by Product Category","Step05:01")
        main_page.verify_property_dialog_value('Name','text_value',"Margin_by_Product_Category.fex","Step05:02")
        main_page.verify_property_dialog_value('Summary','text_area',"","Step05:03")
        main_page.verify_property_dialog_value('Path','text_value',"IBFS:/WFC/Repository/Retail_Samples/Reports/Margin_by_Product_Category.fex","Step05:04")
        main_page.verify_property_dialog_value('Tool','text',"report","Step05:05")
        main_page.verify_property_dialog_value('Publish','radiobutton_value',"Yes","Step05:06")
        main_page.verify_property_dialog_value('Show','radiobutton_value',"Yes","Step05:07")
        main_page.verify_label_in_property_dialog("General", "Created","05:08")
        main_page.verify_label_in_property_dialog("General", "Modified","05:09")
        main_page.verify_label_in_property_dialog("General", "Accessed","05:10")
        main_page.verify_label_in_property_dialog("General", "Owner","05:11")
        main_page.verify_label_in_property_dialog("General", "Size","05:12")
        
        """
        ADVANCED TAB
        """
        main_page.select_property_tab_value("Advanced")
        utils.synchronize_with_number_of_element(".properties-advanced-item-fex .properties-page-row .properties-page-col",12,main_page.report_medium_timesleep)
        main_page.verify_label_in_property_dialog("Advanced","Thumbnail","05:12")
        main_page.verify_label_in_property_dialog("Advanced","Sort order","05:13")
        main_page.verify_label_in_property_dialog("Advanced","Language","05:14")
        main_page.verify_label_in_property_dialog("Advanced","Menu Icon","05:14")
        main_page.verify_label_in_property_dialog("Advanced","Load in iframe","05:15")
        main_page.verify_label_in_property_dialog("Advanced",'Prompt for parameters',step_number="step 05:16",checkbox='enable')
        main_page.verify_label_in_property_dialog("Advanced","Default width","05:17")
        main_page.verify_label_in_property_dialog("Advanced","Default height","05:17")
        utils.verify_object_visible(".properties-advanced-prompt [class*='simple-marker-check']", True,"05:22")
        
        """
        QUERY_DETAIL
        """
        main_page.select_property_tab_value("Query Detail")
        main_page.verify_label_in_property_dialog("Query Detail","Master Files","05:15")
        main_page.verify_label_in_property_dialog("Query Detail","Data Elements","05:16")
        main_page.verify_label_in_property_dialog("Query Detail","Sorts","05:17")
        main_page.verify_label_in_property_dialog("Query Detail","Conditions","05:18")
        main_page.verify_label_in_property_dialog("Query Detail","Expressions","05:19")
        main_page.verify_label_in_property_dialog("Query Detail","Output Formats","05:20")
        main_page.verify_label_in_property_dialog("Query Detail","Joins","05:21")
        utils.verify_object_visible('.query-detail-master-files', True, "05:22")
        utils.capture_screenshot("05.01",step5,expected_image_verify=True)
        
        step6 = """Close the properties dialog.
        Action Bar appears again after the properties dialog is closed.
        """
        main_page.close_property_dialog()
        utils.synchronize_with_number_of_element('.action-bar-tab', 6,main_page.report_medium_timesleep)
        utils.capture_screenshot("06.01",step6,expected_image_verify=True)

        step7 = """In the banner link, click on the top right username > Sign Out."""

        main_page.signout_from_username_dropdown_menu()
        utils.capture_screenshot("07.01",step7)
        
if __name__ == '__main__':
    unittest.main()

