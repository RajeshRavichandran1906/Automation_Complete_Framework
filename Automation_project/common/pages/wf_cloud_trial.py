from common.lib.global_variables import Global_variables as GV
from common.locators import wf_cloud_trial as Locators
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.lib.javascript import JavaScript
from common.lib import html_controls
from common.lib.web_element_utils import WebElementUtils
from datetime import datetime
import imaplib
import email
import time
import bs4
import re


class Registration:
    
    def __init__(self):
        
        self._utils_ = UtillityMethods(GV.webdriver)
        self._coreutils_ = CoreUtillityMethods(GV.webdriver)
        self._javescript = JavaScript(GV.webdriver)
        self._locators = Locators
        self._webelemutils = WebElementUtils()
        
    def invoke_page(self):
        """ """
        instance_type  = self._coreutils_.parseinitfile('instance_type')
        if instance_type =="test":
            url = "https://cloud-dev-information-builders.pantheonsite.io/free-trial/"
        else:
            url = "https://www.ibi.com/free-trial"
        GV.webdriver.get(url)
        page_status = self._webelemutils.wait_until_element_visible(Locators.Registration.country, 60, raise_error=False)
        if page_status== False:
            GV.webdriver.get(url)
            self._utils_.synchronize_with_visble_text(Locators.Registration.form[1], 'Country', 60)
        else:
            print("Cloud Registration Form Loaded Successfully...")
        
    @property
    def Country(self): return html_controls.DropDown(GV.webdriver.find_element(*Locators.Registration.country), "Country DropDown")
    
    @property
    def State(self): return self._state_()
    
    @property
    def FirstName(self): return self._textbox_(Locators.Registration.first_name, Locators.Registration.fname_error, "First Name")
    
    @property
    def LastName(self): return self._textbox_(Locators.Registration.last_name, Locators.Registration.lname_error, "Last Name")
    
    @property
    def Email(self): return self._textbox_(Locators.Registration.email, Locators.Registration.email_error, "Email")
    
    @property
    def Phone(self): return html_controls.TextBox(GV.webdriver.find_element(*Locators.Registration.phone), "Phone")
    
    @property
    def JobTitle(self): return self._textbox_(Locators.Registration.job_title, Locators.Registration.job_error, "Job Title")
    
    @property
    def Company(self): return self._textbox_(Locators.Registration.company, Locators.Registration.company_error, "Company")
    
    @property
    def TermsConditions(self): return self._terms_conditions_()
    
    @property
    def Submit(self): return html_controls.Button(GV.webdriver.find_element(*Locators.Registration.sumbmit), "See What You Can Do")
    
    class _terms_conditions_(html_controls.CheckBox):
        
        def __init__(self):
            
            super().__init__(GV.webdriver.find_element(*Locators.Registration.terms), "Terms and Conditions")
        
        @property
        def ErrorMessage(self):
            
            label_object = GV.webdriver.find_element(*Locators.Registration.terms_error)
            return html_controls.Label(label_object, "Terms and Conditions Error Label")
        
    class _textbox_(html_controls.TextBox):
        
        def __init__(self, textbox_loc, err_label_loc, textbox_name):
            
            self.__label_loc = err_label_loc
            self.__textbox_name = textbox_name
            text_object = GV.webdriver.find_element(*textbox_loc)
            super().__init__(text_object, self.__textbox_name + " TextBox")
        
        @property
        def ErrorMessage(self):
            
            label_object = GV.webdriver.find_element(*self.__label_loc)
            return html_controls.Label(label_object, self.__textbox_name + " Error Label")
    
    class _state_(html_controls.DropDown):
        
        def __init__(self):
            
            ctr_obj = GV.webdriver.find_element(*Locators.Registration.state)
            super().__init__(ctr_obj, "State DropDown")
        
        @property
        def ErrorMessage(self):
            
            label_object = GV.webdriver.find_element(*Locators.Registration.state_error)
            return html_controls.Label(label_object, "State Error Label")
    

class Email:
    
    def __init__(self):
        
        self._utils_ = UtillityMethods(GV.webdriver)
    
    def _get_email_html_content_(self, subject, wait_time):
            
            today_date = datetime.strftime(datetime.date(datetime.now()), "%d-%b-%Y")
            html_content = None
            start_time = time.time()
            while True:
                email_server = imaplib.IMAP4_SSL("outlook.office365.com")
                email_server.login("webqa@ibi.com", "plaza1")
                _, _ = email_server.select("INBOX")
                email_filter_patten = '(since "{0}" unseen)'.format(today_date)
                _, email_id_obj = email_server.search(None, email_filter_patten)
                email_id_list = email_id_obj[0].decode().split()
                email_id_list.reverse()
                for email_id in email_id_list:
                    _, email_data = email_server.fetch(email_id, '(RFC822)')
                    email_data = email.message_from_bytes(email_data[0][1])
                    
                    condition = all([subject.lower().replace(" ", "") in email_data['subject'].lower().replace(" ", "")])
                    
                    if condition:
                        if isinstance(email_data.get_payload(), list):
                            html_content = email_data.get_payload()[1].get_payload(decode=True)
                        else:
                            html_content = email_data.get_payload(decode=True)
                        return html_content
                    else:
                        email_server.store(email_id, '-FLAGS', '(\Seen)')
                end_time = time.time() - start_time
                if end_time > wait_time:
                    return None
                time.sleep(0.5) 
    
    def _get_email_text_content_(self, html_content, css_selector):
        
        if not html_content:
            return html_content
        text_contents = bs4.BeautifulSoup(html_content, 'html.parser').select(css_selector)[0].get_text()
        text_contents = text_contents.replace("\n", "").replace("\r", "").replace("\t", "")
        return text_contents
    
    def _get_hyperlink_from_email_(self, html_content, hyperlink_text):
        
        if not html_content:
            return html_content
        html = bs4.BeautifulSoup(html_content, 'html.parser')
        hyperlink = html.find("a", text = re.compile(hyperlink_text)).attrs['href']
        return hyperlink
    
    def verify_content_of_wf_cloud_trial_email(self, step_num, wait_time=900):
        mail_sub = "Thank you for your interest in ibi's 14-Day Cloud Analytics Trial"
        expected_msg = "We have received your request for the 14-day trial of ibi Cloud Analytics platform.What happens now? You will get another e-mail shortly with some easy next steps on validating your e-mail and setting up the trial, with your own personal cloud environment. Delivery of this e-mail may take a little time."
        html_content = self._get_email_html_content_(mail_sub, wait_time)
        actual_msg = self._get_email_text_content_(html_content, 'td.em_color1')
        msg = "Step {0} : Verify contents of WebFOCUS Cloud Analytics Trial Email".format(step_num)
        if isinstance(actual_msg, str):
            self._utils_.asin(expected_msg, actual_msg, msg)
        else:
            self._utils_.asequal(expected_msg, actual_msg, msg)
            
    def verify_email_to_start_wf_cloud_trail(self, step_num, wait_time=300):
        
        mail_sub = "Verify your e-mail to start your WebFOCUS Cloud Trial"
        expected_msg = "Thank you for requesting a 14-day trial of WebFOCUS, your all-in-one, easy-to-use tool for creating and sharing reports, dashboards, data visualizations, and more"
        html_content = self._get_email_html_content_(mail_sub, wait_time)
        hyperlink = self._get_hyperlink_from_email_(html_content, 'Verify Your E-mail')
        actual_msg = self._get_email_text_content_(html_content, 'body')
        msg = "Step {0} : Verify your e-mail to start your WebFOCUS Cloud Trial".format(step_num)
        if isinstance(actual_msg, str):
            self._utils_.asin(expected_msg, actual_msg, msg)
        else:
            self._utils_.asequal(expected_msg, actual_msg, msg)
        return hyperlink