"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 21 April 2020
----------------------------------------------------"""

from common.webservices.lib.github_api import GitHubApi
from common.webservices import BaseTestCase

class C9945450_TestClass(BaseTestCase):
    
    def test_C9945450(self):
        
        """
        TEST CASE VARIABLS
        """
        github_repro  =  self.get_config_file_key_value('git_repro')
        
        STEP_01 = """
            STEP 01 : Sign into https://github.com  with credentials: ID=scmdev1, psw=IBIqascm1
        """
        self.Log.Message(STEP_01)
        GitHub = GitHubApi()
        
        STEP_02 = """
            STEP 02 : Create Public GitHub repository QA_Val_API with option "Initialize this repository with a README"
        """
        self.Log.Message(STEP_02)
        try    : GitHub.delete_repository(github_repro)
        except : pass
        response = GitHub.create_repository(github_repro)
        
        STEP_02_EXPECTED = """
            STEP 02 Expected : Verify Repository is created successfully
        """
        self.Log.Message(STEP_02_EXPECTED)
        msg = "STEP 02.01 : Verify new [{0}] GitHub repository is created successfully".format(github_repro)
        self.Assertions.assertEqual(True, response, msg)