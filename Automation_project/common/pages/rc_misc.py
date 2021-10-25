from common.lib import utillity
from common.lib.base import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time, re, os


class RC_Misc(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(RC_Misc, self).__init__(driver)

    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
    
    def verify_defered_report_notification(self, report_name):
        """
        report_name: Name of the report
        """
        title=self.driver.find_element_by_css_selector("html #deferTitle").text.strip()
        utillity.UtillityMethods.asequal(self, 'Deferred Report Notification', title, "Step X: Verify Deferred Report's Notification Title.")
        utillity.UtillityMethods.asin(self, report_name, [el.text for el in self.driver.find_elements_by_css_selector("html #deferMsg")], "Step X: Verify Report name displays in Deferred Report's Notification Page.")
        
    def click_defered_report_notification_link(self):
        self.driver.find_element_by_css_selector("html #deferMsg > a").click()
          
    def click_defered_report_button(self, report_name, btn_name, **kwargs):
        """
        report_name: Name of the report
        btn_name: "Delete", Or "View" Or "Save", Or "Run"
        alert_click_btn='OK' OR 'Cancel'
        """
        from selenium.webdriver.common import alert
        x=self.driver.find_elements_by_css_selector("html table:nth-child(5) tr")
        for i in range(len(x)):
            if report_name in x[i].text:
                oClick=x[i].find_element_by_css_selector("img[title^='" + btn_name + "']")
                utillity.UtillityMethods.default_left_click(self,object_locator=oClick)
                break
        time.sleep(4)
        if btn_name == "Delete":
            utillity.UtillityMethods.verify_js_alert(self, 'Are you sure you want to delete Deferred report', "Step X: Verify Delete Confirmation message.")
            utillity.UtillityMethods.verify_js_alert(self, report_name, "Step X: Verify " + report_name + " is available.")
            als = alert.Alert(self.driver)
            if 'alert_click_btn' in kwargs:
                if kwargs['alert_click_btn']=='OK':
                    als.accept()
                    time.sleep(2)
                    status=True
                    for i in range(len(x)):
                        if report_name in x[i].text:
                            status=False
                            break
                    utillity.UtillityMethods.asequal(self, True, status, "Step X: Verify the schedule " + report_name + " is deleted.")
                if kwargs['alert_click_btn']=='Cancel':
                    als.dismiss()

    def set_task_password(self, id_elem, userid, password_btn_elem, passwd, **kwargs):
        """
        param: execution_id_elem
        params: password_btn_elem
        Syntax: set_task_password('eda',execution_id_elem, password_btn_elem)
        @author = Niranjan
        """
        if id_elem.get_attribute("value")=='':
            utillity.UtillityMethods.set_text_field_using_actionchains(self, id_elem, userid)
            password_btn_elem.click()
            time.sleep(2)
            first_password_elem=self.driver.find_element_by_css_selector("#rcBiTaskPasswordDlg #TaskPasswordDlg_firstPasswordField")
            utillity.UtillityMethods.set_text_field_using_actionchains(self, first_password_elem, passwd)
            second_password_elem=self.driver.find_element_by_css_selector("#rcBiTaskPasswordDlg #TaskPasswordDlg_confirmPasswordField")
            utillity.UtillityMethods.set_text_field_using_actionchains(self, second_password_elem, passwd)
            self.driver.find_element_by_css_selector("#rcBiTaskPasswordDlg #TaskPasswordDlg_btnOK").click()
            time.sleep(2)