"""----------------------------------------------------
Author Name : Robert
Automated on : 22-Oct-2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert 
from common.pages import wf_cloud_trial


class C9948415_TestClass(BaseTestCase):
    
    def test_C9948415(self):
        
        """TESTCASE OBJECTS"""
        pardot_url = "https://pi.pardot.com/"
        utils = UtillityMethods(self.driver)
        coreutils = CoreUtillityMethods(self.driver)
        
        
        """TESTCASE VARIABLES"""
        instance_type = UtillityMethods.parseinitfile(self, 'instance_type').lower()
        if instance_type == "prod":
            username = "webqa@ibi.com"
            password_text = "Plaza1!@!"
        else:
            username = "webqcs@ibi.com"
            password_text = "Plaza123!"
            
        loginpage_label_css = "#logInWithSalesforceButton"
        remind_me_button_css = "button[id$='modal-remind']"
        userid_css = "#email_address"
        password_css = "#password"
        submit_btn_css = "input[value='Log In']"
        dashboard_label = "h1[title='Dashboard']"
        briefcase_icon_css = ".icon-briefcase"
        recycle_bin_menu_xpath ="//a[contains(text(),'Recycle Bin')]"
        prospects_link_css = "a[href*='prospect/recycleBin']"
        date_combo_range_css = "#dateRange_pr"
        today_option_xpath = "//option[contains(text(),'This Month')]"
        email_id1 = CoreUtillityMethods.parseinitfile(self, 'email_id')
        email_id2 = CoreUtillityMethods.parseinitfile(self, 'invite_user1_email')
        email_id3 = CoreUtillityMethods.parseinitfile(self, 'invite_user2_email')
        prospect_query = "input#query"
        prospect_filter_css = "#prospect_table_filter"
        record_count_css ="#prospect_table tbody tr:not([style*='display:none'])"
        check_all_checkbox= "input.check-all"
        row_dropdown_toggle="//td//*[@class='dropdown-toggle'][1]"
        perm_delete ="//*[contains(@id,'prospect_row_a0')]//*[contains(text(),'Permanently Delete')]"
        delete_menu_css ="//*[contains(@id,'prospect_row_a0')]//*[contains(text(),'Delete')]"
        alert_confirm_checkbox = "#permanentlyDelete[style*='block'] #permanently_delete_confirm"
        alert_delete_button = "#permanentlyDelete[style*='block'] #permanently_delete_button"
        login_sf_button_css = "a#logInWithSalesforceButton"
        sf_user_css = "#username"
        sf_password_css = "#password"
        sf_submit_css = "#Login"
        sf_code_input = ".formArea input"
        sf_code_verify_btn = "input[value='Verify']"
         
        email_list = [email_id1, email_id2, email_id3]
        
        STEP_01 = """
            STEP 01 : Login to Pardot system
        """
        self.driver.get(pardot_url)
        utils.synchronize_with_visble_text(loginpage_label_css, 'Log In with Salesforce', 60)
        
        if instance_type == "prod":
            self.driver.find_element_by_css_selector(login_sf_button_css).click()
            coreutils.switch_to_new_window()
            self.driver.find_element_by_css_selector(sf_user_css).send_keys(username)
            self.driver.find_element_by_css_selector(sf_password_css).send_keys(password_text)
            self.driver.find_element_by_css_selector(sf_submit_css).click()
            utils.wait_for_page_loads(30)
            time.sleep(20)
            html1=wf_cloud_trial.Email._get_email_html_content_(self,'Verify your identity in Salesforce',40)
            text1=str(html1).replace("\\n", "").replace("\\r", "").replace("\\t", "")
            verification_code = text1.partition("Code: ")[2].partition("If")[0]
            self.driver.find_element_by_css_selector(sf_code_input).send_keys(verification_code)
            self.driver.find_element_by_css_selector(sf_code_verify_btn).click()
            coreutils.switch_to_previous_window(window_close = False)
        else:
            self.driver.find_element_by_css_selector(userid_css).send_keys(username)
            self.driver.find_element_by_css_selector(password_css).send_keys(password_text)
            self.driver.find_element_by_css_selector(submit_btn_css).click()
        
        utils.capture_screenshot('01.00', STEP_01)
        
        STEP_01_01 = """
            STEP 01.01 : Verify the Dashboard screen opens up
        """ 
        utils.synchronize_with_number_of_element(dashboard_label, 1, 60)
        try:
            if (self.driver.find_element_by_css_selector(remind_me_button_css).is_displayed()):
                self.driver.find_element_by_css_selector(remind_me_button_css).click()
        except:
            pass
        
        utils.verify_element_visiblty(element_css=dashboard_label, visible=True, msg="Step 01.01 Verify Dashboard screen opens up")
        
        utils.capture_screenshot('01.01', STEP_01_01, True)
        
        STEP_02 = """
            STEP 02.00 : Click on the Briefcase icon on the left to bring up the popup menu and select Recycle Bin
        """
        for emailid in email_list:
            print("------------------------------------------------------------------------------")
            print("Search and Delete Active prospects for Email id : "+emailid)
            print("------------------------------------------------------------------------------")
            
            self.driver.find_element_by_css_selector(prospect_query).click()
            self.driver.find_element_by_css_selector(prospect_query).clear()
            self.driver.find_element_by_css_selector(prospect_query).send_keys(emailid)
            self.driver.find_element_by_css_selector(prospect_query).send_keys(Keys.ENTER)
            utils.wait_for_page_loads(30)
            
            try:
                elems = self.driver.find_elements_by_css_selector(record_count_css)
                print("Step 02.00 No of Active prospect records displayed is "+str(len(elems))+" for "+emailid)
            except:
                print("Step 02.00 No of Active prospect records displayed is "+str(len(elems))+" for "+emailid)
            

            if len(elems)>0:
                
                try:
                    self.driver.find_element_by_css_selector(check_all_checkbox).click()
                    time.sleep(3)
                except:
                    pass
                
                try:
            
                    self.driver.find_element_by_xpath(row_dropdown_toggle).click()
                    time.sleep(3)
                    self.driver.find_element_by_xpath(delete_menu_css).click()
                    time.sleep(5)
                    alert = Alert(self.driver)
                    alert.accept()
                    utils.wait_for_page_loads(10)
                    
                except:
                    print("Step 02.00 "+str(len(elems))+" records for "+emailid+ ". Unable to delete the Active prospect records")
            else:
                print("Step 02.00 No Active prospects to delete for "+emailid)
            print("\n")

        utils.wait_for_page_loads(30)
        self.driver.find_element_by_css_selector(briefcase_icon_css).click()
        utils.wait_for_page_loads(10)
        self.driver.find_element_by_xpath(recycle_bin_menu_xpath).click()
        utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
            STEP 03.00 : Click on Prospects link to load the Deleted Prospects screen
        """
        utils.synchronize_with_visble_text("thead>tr>th:nth-of-type(1)", "MODULE NAME", 30)
        
        self.driver.find_element_by_css_selector(prospects_link_css).click()
        #time.sleep(3)

        utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04 = """
            STEP 04.00 : Select Today from the Deleted dropdown time
        """
        utils.synchronize_with_visble_text("div h2", "Deleted Prospects", 30)
        self.driver.find_element_by_css_selector(date_combo_range_css).click()
        utils.wait_for_page_loads(10)
        self.driver.find_element_by_xpath(today_option_xpath).click()

        utils.capture_screenshot('04.00', STEP_04)
        
        STEP_05 = """
            STEP 05.00 : Type the email id of the account you want to be deleted
        """
        STEP_06 = """
            STEP 06.00 : Click on the All checkbox next to Name title to select the displayed records
        """
        STEP_07 = """
            STEP 07.00 : Click on Action and select Permanently Delete. In the confirmation box, confirm the delete.
        """
        

        for emailid in email_list:
            print("------------------------------------------------------------------------------")
            print("Search and Deleting account for Email id : "+emailid)
            print("------------------------------------------------------------------------------")
            self.driver.find_element_by_css_selector(prospect_filter_css).clear()
            self.driver.find_element_by_css_selector(prospect_filter_css).send_keys(emailid)
            self.driver.find_element_by_css_selector(prospect_filter_css).send_keys(Keys.ENTER)
            utils.wait_for_page_loads(30)
            
            try:
                elems = self.driver.find_elements_by_css_selector(record_count_css)
                print("Step 05.00 No of records displayed is "+str(len(elems))+" for "+emailid)
            except:
                print("Step 05.00 No of records displayed is "+str(len(elems))+" for "+emailid)
            utils.capture_screenshot('05.00', STEP_05)

            if len(elems)>0:
                
                try:
                    self.driver.find_element_by_css_selector(check_all_checkbox).click()
                    time.sleep(3)
                except:
                    print("Step 06.00 No All checkbox found for "+emailid)
        
                utils.capture_screenshot('06.00', STEP_06)

                try:
            
                    self.driver.find_element_by_xpath(row_dropdown_toggle).click()
                    time.sleep(3)
                    self.driver.find_element_by_xpath(perm_delete).click()
                    utils.wait_for_page_loads(10)
                    utils.synchronize_with_number_of_element(alert_delete_button,1,30)
                    self.driver.find_element_by_css_selector(alert_confirm_checkbox).click()
                    utils.wait_for_page_loads(10)
                    self.driver.find_element_by_css_selector(alert_delete_button).click()
                    print ("Step 07.00 Successfully deleted the prospect for "+emailid)
                except:
                    print("Step 07.00 "+str(len(elems))+" records for "+emailid+ ". Unable to delete the records")
            else:
                print("Step 07.00 No prospects to delete for "+emailid)
            print("\n")
            utils.capture_screenshot('07.00', STEP_07)
        