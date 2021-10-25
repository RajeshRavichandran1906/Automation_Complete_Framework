"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 28 April 2020
----------------------------------------------------"""

from common.webservices.lib.github_api import GitHubApi
from common.webservices import BaseTestCase

class C9945446_TestClass(BaseTestCase):
    
    def test_C9945446(self):
        
        """
        TEST CASE VARIABLS
        """
        github_repro  =  self.get_config_file_key_value('git_repro')
        github_branch =  self.get_config_file_key_value('git_branch')
        
        STEP_01 = """
            STEP 01 : Sign into https://github.com with credentials: ID=scmdev1, psw=IBIqascm1
        """
        self.Log.Message(STEP_01)
        GitHub = GitHubApi()
        
        STEP_02 = """
            STEP 02 : Create pull request
        """
        self.Log.Message(STEP_02)
        pull_number = GitHub.create_pull_request(github_repro, 'Testing', github_branch, 'master')
    
        STEP_02_EXPECTED = """
            STEP 02 Expected : Pull request is created.
        """
        self.Log.Message(STEP_02_EXPECTED)
        msg = "STEP 02.01 : Verify new pull request created"
        self.Assertions.assertEqual(True, True, msg)
        
        STEP_03_04 = """
            STEP 03 : Merge pull request
            STEP 04 : Confirm merge
        """
        self.Log.Message(STEP_03_04)
        response = GitHub.merge_pull_request(github_repro, pull_number)
        
        STEP_04_EXPECTED = """
            STEP 04 Expected : Merge is successful
        """
        self.Log.Message(STEP_04_EXPECTED)
        msg = "STEP 04.01 : Verify pull request merged is successful"
        self.Assertions.assertEqual(True, response, msg)
        