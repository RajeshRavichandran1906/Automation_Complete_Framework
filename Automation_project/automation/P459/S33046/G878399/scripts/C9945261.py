"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 23 April 2020
----------------------------------------------------"""

from common.webservices.git import gitBranch
from common.webservices import BaseTestCase

class C9945261_TestClass(BaseTestCase):
    
    def test_C9945261(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')
        branch_name = ['refs/heads/master', 'refs/remotes/origin/Branch_Val_API', 'refs/remotes/origin/master']
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS and Run gitBranch with IBIRS_path=IBFS:/WFC/Repository/P459_S33046_Val_API IBFS_gitBranchOptions = --list --all
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_branch = gitBranch(IBIRS_path, IBIRS_gitBranchOptions='--list --all')
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" and [name="refs/heads/master", name="refs/remotes/origin/Branch_Val_API", name="refs/remotes/origin/master"]
        """
        self.Log.Message(STEP_01_EXPECTED)
        git_branch.verify_returncode('01.01')
        git_branch.verify_IBFSGitRef_name(branch_name, '01.02')