"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 22 April 2020
----------------------------------------------------"""

from common.webservices.git import gitInit, gitBranch
from common.webservices import BaseTestCase

class C9945224_TestClass(BaseTestCase):
    
    def test_C9945224(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')

        STEP_01 = """
            STEP 01 : Sign into WebFOCUS and gitInit with IBIRS_path=IBFS:/WFC/Repository/P459_S33046_Val_API
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_init = gitInit(IBIRS_path)
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" and [entry key="IBIRS_path" value="IBFS:/WFC/Repository/P459_S33046_Val_API"]
        """
        self.Log.Message(STEP_01_EXPECTED)
        git_init.verify_returncode('01.01')
        git_init.verify_ibfsparams_key_value('IBIRS_path', [IBIRS_path], '01.02')
        
        STEP_02 = """
            STEP 02 : To verify pwa (local) master branch is created by gitInit, Run gitBranch with
            [IBIRS_path=IBFS:/WFC/Repository/P459_S33046_Val_API, IBFS_gitBranchOptions = --list --all]
        """
        self.Log.Message(STEP_02)
        git_branch = gitBranch(IBIRS_path, IBIRS_gitBranchOptions='--list --all')
        
        STEP_02_EXPECTED = """
            STEP 02 Expected : Verify returncode="10000" and [item _jt="IBFSGitRef" index="0" name="refs/heads/master" peeled="false" symbolic="false"]
        """
        self.Log.Message(STEP_02_EXPECTED)
        git_branch.verify_returncode('02.01')
        git_branch.verify_IBFSGitRef_name(['refs/heads/master'], '02.02')