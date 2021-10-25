"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 28 May 2020
----------------------------------------------------"""

from common.webservices.lib.github_api import GitHubApi
from common.webservices import BaseTestCase

class C9945445_TestClass(BaseTestCase):
    
    def test_C9945445(self):
        
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
            STEP 02 : Delete repository QA_Val_API
        """
        self.Log.Message(STEP_02)
        GitHub.delete_repository(github_repro)