"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 05 May 2020
----------------------------------------------------"""

from common.webservices.git import gitStatus, gitCommit
from common.webservices import BaseTestCase

class C9945706_TestClass(BaseTestCase):
    
    def test_C9945706(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')
        expected_item_attrib = [{'_jt': 'IBFSScmStatusObjectPair', 'path': 'IBFS:/WFC/Repository/P459_S33046_Val_API'}, {'_jt': 'IBFSScmStatusObjectPair', 'path': 'IBFS:/WFC/Repository/P459_S33046_Val_API/Hidden_Content'}]
        expected_status_attrib = [{'_jt': 'IBFSScmStatusObject', 'metadatsStatus': 'UNTRACKED', 'status': 'UNTRACKED'}, {'_jt': 'IBFSScmStatusObject', 'contentStatus': 'UNTRACKED_FOLDER', 'metadatsStatus': 'UNTRACKED', 'status': 'UNTRACKED|UNTRACKED_FOLDER'}]
        added_file = [{'path' : IBIRS_path + "/scm_vis1.fex"}]
        item_attib = [{'_jt' : 'IBFSGitRevCommit', 'fullMessage' : "'Commit2'"}]
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS and Run gitCommit with [IBFS_gitCommitOptions = --message 'Commit2', gitCommitParams = IBFS:/WFC/Repository/P459_S33046_Val_API]
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_commit = gitCommit(IBIRS_gitCommitOptions="--message 'Commit2'", IBIRS_gitCommitParams=IBIRS_path)
         
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" and <item _jt="IBFSGitRevCommit" commitTime='' fullMessage='Commit2'/>
        """
        self.Log.Message(STEP_01_EXPECTED)
        git_commit.verify_returncode('01.01')
        git_commit.XMLAssertions.assertAttributesListIn(git_commit.XmlNode.IBFSGitRevCommit_item, item_attib, '01.02', match_case=True)
        
        STEP_02 = """
            STEP 02 : Run gitStatus with IBFS_gitStatusParams=IBFS:/WFC/Repository/P459_S33046_Val_API
        """
        self.Log.Message(STEP_02)
        git_status = gitStatus(IBIRS_gitStatusParams=IBIRS_path)
        
        STEP_02_EXPECTED = """
            STEP 02 Expected : Verify returncode="10000" and <item>, <status> tags values.
            path='IBFS:/WFC/Repository/P459_S33046_Val_API/scm_vis1.fex not in item
        """
        self.Log.Message(STEP_02_EXPECTED)
        folder_xpath = git_status.XmlNode.rootObject_item_staus.format(expected_item_attrib[0]['path'])
        hidden_content_xpath = git_status.XmlNode.rootObject_item_staus.format(expected_item_attrib[1]['path'])
        git_status.verify_returncode('02.01')
        git_status.XMLAssertions.assertAttributesListIn(git_status.XmlNode.rootObject_item, expected_item_attrib, '02.02', ['index'])
        git_status.XMLAssertions.assertAttributesEqual(folder_xpath, expected_status_attrib[0], '02.03')
        git_status.XMLAssertions.assertAttributesEqual(hidden_content_xpath, expected_status_attrib[1], '02.04')
        git_status.XMLAssertions.assertAttributesListNotIn(git_status.XmlNode.rootObject_item, added_file, '02.05')