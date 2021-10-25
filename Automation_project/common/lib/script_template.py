from datetime import datetime
from testrail_api import TestRailAPI
import textwrap
import os
import getpass

base_template = '''"""-------------------------------------------------------------------------------------------
Author Name  : {auther_name}
Automated On : {date}
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C{case_id}_TestClass(BaseTestCase):
    
    def test_C{case_id}(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        
'''

step_template = '''{step_num_var} = """
    STEP {step_num} : {step_desc}
"""

HomePage.Home._utils.capture_screenshot("{step_num}", {step_num_var}{verify_img})

'''

class ScriptTemplate:
    
    def __init__(self, user_id, password, case_id):
        
        self.case_id = case_id.lower().replace('c', '')
        today_date = datetime.strftime(datetime.date(datetime.now()), "%d-%B-%Y")
        self.base_template = base_template.format(auther_name=user_id.upper(), date=today_date, case_id=self.case_id)
        self.__testrail = self.__login_testrail(user_id, password)
    
    def __login_testrail(self, user_id, password):
        
        try:
            testrail = TestRailAPI("http://lnxtestrail.ibi.com/testrail/", user_id, password)
            testrail.users.get_users()
            return testrail
        except:
            raise Exception("Invalid user id or password")
        
    def _get_case_steps(self):
        
        try:
            case_info = self.__testrail.cases.get_case(self.case_id)
            return case_info['custom_steps']
        except:
            raise Exception("C{} case not found in Testrail".format(self.case_id))
            
    def generate(self):
        
        for index, step in enumerate(self._get_case_steps(), 1):
            content = step['content'].split("\n![]")[0].strip().replace("\n", "\n    ").replace('"', "'")
            expected = step['expected'].split("\n![]")[0].strip().replace("\n", "\n    ").replace('"', "'")
            step_number = "0{}".format(index) if index<10 else str(index)
            step_number_var = "STEP_" + step_number
            step_content = step_template.format(step_num=step_number, step_num_var=step_number_var, step_desc=content, verify_img='')
            self.base_template = self.base_template + textwrap.indent(step_content, " "*8)
            if expected.strip() != '':
                exp_step_number = "{} - Expected".format(step_number)
                exp_step_number_var = "STEP_{0}_EXPECTED".format(step_number)
                step_expected = step_template.format(step_num=exp_step_number, step_num_var=exp_step_number_var, step_desc=expected, verify_img=', True')
                self.base_template = self.base_template + textwrap.indent(step_expected, " "*8)
        file_name = "C{}.py".format(self.case_id)
        file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, "w") as file:
            file.write(self.base_template)
        msg = "{0} test case template generated in [{1}] location".format(file_name, file_path)
        print(msg)
    
while True:
    user_nmae = input("Enter the Testail user name : ")
    password = getpass.getpass("Enter the Testail Password : ")
    case_id = input("Enter the case id : ")
    try:
        ScriptTemplate(user_nmae, password, case_id).generate()
    except Exception as msg:
        print(msg)
    status = input("Pree Enter to continue.. or Type exit to close").lower().strip()
    if status == 'exit':
        break;