"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 21 April 2020
----------------------------------------------------"""

from common.webservices.lib.github_api import GitHubApi
from common.webservices import BaseTestCase

class C9945451_TestClass(BaseTestCase):
    
    def test_C9945451(self):
        
        """
        TEST CASE VARIABLS
        """
        github_repro  =  self.get_config_file_key_value('git_repro')
        branch_name   =  self.get_config_file_key_value('git_branch')
        
        STEP_01 = """
            STEP 01 : For repository QA_Val_API create a new branch Branch_Val_API
        """
        self.Log.Message(STEP_01)
        response = GitHubApi().create_branch(github_repro, branch_name)
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify Branch_Val_API branch is created.
        """
        self.Log.Message(STEP_01_EXPECTED)
        msg = "STEP 01.01 : Verify new [{0}] GitHub branch is created successfully".format(branch_name)
        self.Assertions.assertEqual(True, response, msg)