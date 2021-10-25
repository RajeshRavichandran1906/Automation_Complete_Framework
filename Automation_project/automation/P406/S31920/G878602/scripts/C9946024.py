"""----------------------------------------------------
Author Name : Prabhakaran
Automated on : 22-June-2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_cloud_trail import WFCloudTrail
from common.lib.utillity import UtillityMethods

class C9946024_TestClass(BaseTestCase):
    
    def test_C9946024(self):
        
        """TESTCASE OBJECTS"""
        
        CloudTrail = WFCloudTrail()
        email_id = CloudTrail.Registation._coreutils_.parseinitfile('email_id')
        first_name = CloudTrail.Registation._coreutils_.parseinitfile('first_name')
        cloud_provider = CloudTrail.Registation._coreutils_.parseinitfile('cloud_provider')
        css = "#page div[data-text-theme='light']"
        instance_type = UtillityMethods.parseinitfile(self, 'instance_type').lower()
        
        STEP_01 = """
            STEP 01 : Access IBI Cloud Analytics (Dev) Trial Page
        """
        CloudTrail.Registation.invoke_page()
        CloudTrail.Registation._utils_.wait_for_page_loads(120)
        CloudTrail.Registation._utils_.capture_screenshot('01.00', STEP_01)
        
        STEP_01_01 = """
            STEP 01.01 : Verify the following page is displayed
        """ 
        title = "Cloud Analytics Trial for Business Intelligence | ibi"
        CloudTrail.Registation._utils_.asequal(title, self.driver.title, "Step 01.01 : Verify IBI Cloud Analytics (Dev) Trial Page displayed")
        CloudTrail.Registation._utils_.capture_screenshot('01.01', STEP_01_01, True)
        
        STEP_02 = """
            STEP 02.00 : Verify default form values
        """
        CloudTrail.Registation.Country.verify_selected_option('United States', '02.01')
        if instance_type == "prod":
            CloudTrail.Registation.State.verify_selected_option('', '02.02')
        else:
            CloudTrail.Registation.State.verify_selected_option('Alabama', '02.02')
            
        CloudTrail.Registation.FirstName.verify_placeholder('', '02.03')
        CloudTrail.Registation.LastName.verify_placeholder('', '02.04')
        CloudTrail.Registation.Email.verify_placeholder('', '02.05')
        CloudTrail.Registation.Phone.verify_placeholder('', '02.06')
        CloudTrail.Registation.JobTitle.verify_placeholder('', '02.07')
        CloudTrail.Registation.Company.verify_placeholder('', '02.08')
        JobTitle = CloudTrail.Registation.JobTitle._object
        TermsConditions = CloudTrail.Registation.TermsConditions._object_
        CloudTrail.Registation._utils_.asequal(False,TermsConditions.is_selected(),"Step 02.09 : Verify Terms and Conditions is Unchecked.")
        #CloudTrail.Registation.TermsConditions.verify_unchecked('02.09')
        CloudTrail.Registation._utils_.capture_screenshot('02.00', STEP_02, True)
        
        STEP_03 = """
            STEP 03.00 : Enter the following form entries:
        """
        CloudTrail.Registation.Country.select('United States')
        CloudTrail.Registation.State.select('New York')
        CloudTrail.Registation.FirstName._object.send_keys(first_name)
        CloudTrail.Registation.LastName._object.send_keys('IBIQA')
        CloudTrail.Registation.Email._object.send_keys(email_id)
        CloudTrail.Registation.Phone._object.send_keys('212-736-4433')
        CloudTrail.Registation.JobTitle._object.send_keys('Automation Engineer')
        CloudTrail.Registation.Company._object.send_keys('Information Builders')
        CloudTrail.Registation._utils_.capture_screenshot('03.00', STEP_03)
        
        STEP_04 = """
            STEP 04.00 : Select Checkbox "I have and read and agree with Information Builders' Terms and Conditions
        """
        CloudTrail.Registation._javescript.scrollIntoView(JobTitle)
        CloudTrail.Registation._utils_.wait_for_page_loads(10)
        TermsConditions.click()
        CloudTrail.Registation._utils_.capture_screenshot('04.00', STEP_04)
        
        STEP_06 = """
            STEP 06 : Click on "See What You Can Build"
        """
        if cloud_provider == "aws":
            self.driver.find_element(*CloudTrail.Registation._locators.Registration.aws).click()
        else:
            self.driver.find_element(*CloudTrail.Registation._locators.Registration.azure).click()
        CloudTrail.Registation.Submit._object_.click()
        CloudTrail.Registation._utils_.wait_for_page_loads(120)
        CloudTrail.Registation._utils_.synchronize_with_visble_text(css, 'Your trial is about', 120)
        CloudTrail.Registation._utils_.capture_screenshot('06.00', STEP_06)
         
        STEP_07_00 = """
            STEP 07.00 : Verify the following page appears
        """
        expected = "Yourtrialisabouttobegin.Getready.Thisisgoingtobefun."
        actual_text = self.driver.find_element_by_css_selector(css).text.replace("\n", " ").replace(" ", "") 
        CloudTrail.Registation._utils_.asin(expected, actual_text, "Step 07.00 : Verify the following page appears")
        CloudTrail.Registation._utils_.capture_screenshot('07.00', STEP_07_00, True)
