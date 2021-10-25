"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 11 May 2020
----------------------------------------------------"""

from common.webservices.git import gitFetch, gitLog
from common.webservices import BaseTestCase

class C9945709_TestClass(BaseTestCase):
    
    def test_C9945709(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')
        git_email = self.get_config_file_key_value('git_email')
        git_user = self.get_config_file_key_value('git_userid')
        FexPath = IBIRS_path + "/scm_vis1.fex"
        IBFSGitRevCommit_attrib = [{'fullMessage': "'Commit2'"}, {'fullMessage': "'Commit Validation'"}]
        authorIdent_attrib = [{'_jt' : 'IBFSGitPersonIdent', 'emailAddress' : git_email, 'name' : git_user}]
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS and Run gitFetch with IBIRS_path=IBFS:/WFC/Repository/P459_S33046_Val_API
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_fetch = gitFetch(IBIRS_path) 
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000"
        """
        self.Log.Message(STEP_01_EXPECTED)
        git_fetch.verify_returncode('01.01')
    
        STEP_02 = """
            STEP 02 : Run gitLog with IBIRS_gitLogParams=IBFS:/WFC/Repository/P459_S33046_Val_API/scm_vis1.fex
        """
        self.Log.Message(STEP_02)
        git_log = gitLog(IBIRS_gitLogParams=FexPath)
        
        STEP_02_EXPECTED = """
            STEP 02 Expected : Verify returncode="10000" and fullMessage="'Commit Validation'", <authorIdent _jt="IBFSGitPersonIdent" emailAddress="scmdevone@gmail.com" name="scmdev1"
        """
        authorIdent_xpath = git_log.XmlNode.item_authorIdent.format(IBFSGitRevCommit_attrib[0]['fullMessage'])
        self.Log.Message(STEP_02_EXPECTED)
        git_log.verify_returncode('02.01')
        git_log.XMLAssertions.assertAttributesListIn(git_log.XmlNode.item_IBFSGitRevCommit, IBFSGitRevCommit_attrib, '02.02', match_case=True)
        git_log.XMLAssertions.assertAttributesListIn(authorIdent_xpath, authorIdent_attrib, '02.03', match_case=True)