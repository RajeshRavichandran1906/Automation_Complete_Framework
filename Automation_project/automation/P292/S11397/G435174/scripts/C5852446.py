"""-------------------------------------------------------------------------------------------
Created on August 12, 2019
@author: Niranjan

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5852446
Test Case Title =  Verify create and modify thumbnail
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
import time

class C5852446_TestClass(BaseTestCase):

    def test_C5852446(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        qwerty_tree_css = "#queryTreeWindow"
        chart_css = "#pfjTableChart_1"
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        ok_button_css = "div[id*='BiDialog'] div[class^='bi-button button button-focus']"
        
        """
            STEP 1 : Launch Chart Mode:
            http://machine:port/alias/ia?tool=Chart&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/P292_S11397/G435147
        """
        chart.invoke_chart_tool_using_api("baseapp/wf_retail_lite")
        chart.wait_for_visible_text(chart_css, "Group 0")
        
        """
            STEP 2 : Double click "Product,Category" and "Cost of Goods" in Data pane.
        """ 
        chart.double_click_on_datetree_item("Product,Category", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Product,Category")
        
        chart.double_click_on_datetree_item("Cost of Goods", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Cost of Goods")
        
        """
            STEP 3 : Drag "Gross Profit" from Data pane to "Color" bucket in Query pane.
        """
        chart.drag_field_from_data_tree_to_query_pane("Gross Profit", 1, "Color", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Gross Profit")
        
        """
            STEP 4 : Click "Create Thumbnail" button from the toolbar.
        """
        chart.select_ia_toolbar_item("toolbar_thumbnail")
        chart.wait_for_visible_text("#qbThumbNailDlgOkBtn", "OK")
        
        """
            STEP 4.1 : Check the "Create Thumbnail" dialog.
        """
        utils.verify_picture_using_sikuli("C5852446_step4.png", "Step 4.1 : Check the 'Create Thumbnail' dialog")
        
        """
            STEP 5 : Click "OK" button.
        """
        button_obj = utils.validate_and_get_webdriver_object("#qbThumbNailDlgOkBtn", "OK button")
        core_utils.python_left_click(button_obj)
        
        """
            STEP 6 : Click "Save" in toolbar Enter "C5852446" and Click "Save" button.
        """
        chart.select_ia_toolbar_item("toolbar_save")
        chart.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")
        
        chart.save_file_in_save_dialog("C5852446")
        
        """
            STEP 7 : Logout
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        chart.api_logout()
        
        """
            STEP 8 : Launch the API link.
            http://machine:port/{alias}
        """
        login.invoke_home_page('mrid', 'mrpass')
        utils.synchronize_with_visble_text(content_css, "Content", main_page.home_page_long_timesleep)
        
        """
            STEP 9 : Click "P292_S11397" and Click "G435147" folder.
        """
        main_page.select_option_from_crumb_box("Domains")
        time.sleep(10)
        
        main_page.expand_repository_folder("P292_S11397->G435147")
        chart.wait_for_visible_text(".action-bar-tab[data-ibxp-user-value='common']", "Connect")
        
        """
            STEP 10 : Right click the "C5852446"saved fex and Select "Properties" option.
        """
        main_page.right_click_folder_item_and_select_menu("C5852446", "Properties")
        chart.wait_for_visible_text("div[class^='propPage ibx-widget ibx-flexbox']", "Cancel")
        
        """
            STEP 11 : Click "Advanced" Tab. 
        """
        main_page.select_property_tab_value("Advanced")
        
        """
            STEP 11.1 : Check that the thumbnail image is displayed.
        """
        utils.verify_picture_using_sikuli("C5852446_step11.png", "Step 11.1 : Check that the thumbnail image is displayed.")
        
        """    
            STEP 12 : Click "Cancel" in the properties dialog.
        """
        main_page.select_property_dialog_save_cancel_button("Cancel")
        
        """
            STEP 13 : Logout
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        chart.api_logout()
 
        """
            STEP 14 : Reopen the saved fex using API link
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S11397/G435147/C203670.fex&tool=Chart
        """
        chart.edit_fex_using_api_url("P292_S11397%2FG435147", tool='Chart', fex_name='C5852446' , mrid="mrid", mrpass="mrpass")
        chart.wait_for_visible_text("div#pfjTableChart_1", "Computers")
        
        """
            STEP 15 : Right click "Gross Profit" field in the Query pane and Select "Delete" option.
        """
        chart.right_click_on_field_under_query_tree("Gross Profit", 1, "Delete")
        
        """
            STEP 16 : Click "Save" from the toolbar and Click "OK" button.
        """
        chart.select_ia_toolbar_item("toolbar_save")
        chart.wait_for_visible_text("div[id*='BiDialog']", "OK")
        
        ok_button_obj = utils.validate_and_get_webdriver_object(ok_button_css, "Ok css")
        core_utils.python_left_click(ok_button_obj)
        
        """
            STEP 17 : Click "Create Thumbnail" button from the toolbar.
        """
        chart.select_ia_toolbar_item("toolbar_thumbnail")
        chart.wait_for_visible_text("#qbThumbNailDlgOkBtn", "OK")
        
        """
            STEP 17.1 : Check the "Create Thumbnail" dialog.
        """
        utils.verify_picture_using_sikuli("C5852446_step17.png", "Step 17.1 : Check the 'Create Thumbnail' dialog")
        
        """
            STEP 18 : Click "OK" button.
        """
        button_obj = utils.validate_and_get_webdriver_object("#qbThumbNailDlgOkBtn", "OK button")
        core_utils.python_left_click(button_obj)
        
        """
            STEP 19 : Click "IA" menu and Select "Close" option.
        """
        chart.select_ia_application_menu("close")
        chart.wait_for_visible_text("#btnYes", "Yes")
        
        """
            STEP 20 : Click "YES" option and Click "OK" button.
        """
        yes_button_obj = utils.validate_and_get_webdriver_object("#btnYes", "Yes button css")
        core_utils.python_left_click(yes_button_obj)
        chart.wait_for_visible_text(ok_button_css, "OK")
        
        ok_button_obj = utils.validate_and_get_webdriver_object(ok_button_css, "Ok css")
        core_utils.python_left_click(ok_button_obj)
        
        """
            STEP 21 : Logout:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()
        
        """
            STEP 22 : Launch the API link.
            http://machine:port/{alias}
        """
        login.invoke_home_page('mrid', 'mrpass')
        utils.synchronize_with_visble_text(content_css, "Content", main_page.home_page_long_timesleep)
        
        """
            STEP 23 : Click "P292_S11397" and Click "G435147" folder.
        """
        main_page.select_option_from_crumb_box("Domains")
        time.sleep(10)
        
        main_page.expand_repository_folder("P292_S11397->G435147")
        chart.wait_for_visible_text(".action-bar-tab[data-ibxp-user-value='common']", "Connect")
        
        """
            STEP 24 : Right click the "C5852446"saved fex and Select "Properties" option.
        """
        main_page.right_click_folder_item_and_select_menu("C5852446", "Properties")
        chart.wait_for_visible_text("div[class^='propPage ibx-widget ibx-flexbox']", "Cancel")
        
        """
            STEP 25 : Click "Advanced" Tab.
        """
        main_page.select_property_tab_value("Advanced")
        
        """
            STEP 25.1 : Check that the thumbnail image has been updated.
        """
        utils.verify_picture_using_sikuli("C5852446_step25.png", "Step 25.1 : Check that the thumbnail image has been updated.")
        
        """
            STEP 26 : Click "Cancel" in the properties dialog.
        """
        main_page.select_property_dialog_save_cancel_button("Cancel")
        
        """
            STEP 27 : Logout
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()

if __name__ == '__main__':
    unittest.main()