"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 23 April 2020
----------------------------------------------------"""

from common.webservices.git import gitRemote
from common.webservices import BaseTestCase

class C9945231_TestClass(BaseTestCase):
    
    def test_C9945231(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')
        gitRepository = self.get_config_file_key_value('git_repro_url')  
        addResult_attrib = [{'_jt': 'IBFSGitRemoteConfig', 'mirror': 'false', 'name': 'origin', 'receivePack': 'git-receive-pack'}]
        addResult_items_attrib = [{'_jt': 'string', 'index': '0', 'value': gitRepository}]
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS and Run gitRemote
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_remote = gitRemote(IBIRS_path, '--add', 'origin ' + gitRepository) 
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" and <addResult _jt="IBFSGitRemoteConfig" mirror="false" name="origin" receivePack="git-receive-pack>
            and <item _jt="string" index="0" value="https://github.com/scmdev1/QA_Val_API"/>
        """
        self.Log.Message(STEP_01_EXPECTED)
        git_remote.verify_returncode('01.01')
        git_remote.XMLAssertions.assertAttributesListIn(git_remote.XmlNode.addResult, addResult_attrib, '01.02', match_case=True)
        git_remote.XMLAssertions.assertAttributesListEqual(git_remote.XmlNode.addResult_URIs_item, addResult_items_attrib, '01.03')