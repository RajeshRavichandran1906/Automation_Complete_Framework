"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 04 May 2020
----------------------------------------------------"""

from common.webservices.ibfs import put
from common.webservices import BaseTestCase
from common.webservices.git import gitStatus

class C9945701_TestClass(BaseTestCase):
    
    def test_C9945701(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')
        fex_path = IBIRS_path + "/scm_vis1.fex"
        IBIRS_object = '<rootObject _jt="IBFSFile" type="IBFSFile"><content _jt="IBFSByteContent" charset="Cp1252">VEFCTEUgRklMRSBDQVINClBSSU5UIENBUg0KRU5E</content></rootObject>'
        expected_item_attrib = [{'_jt': 'IBFSScmStatusObjectPair', 'path': 'IBFS:/WFC/Repository/P459_S33046_Val_API/scm_vis1.fex'}]
        expected_status_attrib = {'_jt': 'IBFSScmStatusObject', 'contentStatus': 'MODIFIED', 'metadatsStatus': 'MODIFIED', 'status': 'MODIFIED'}
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS and Run ibfs put with Run gitStatus with IBIRS_path and IBIRS_object= 
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        ibfs_put = put(fex_path, IBIRS_object=IBIRS_object)
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000"
        """
        self.Log.Message(STEP_01_EXPECTED)
        ibfs_put.verify_returncode('01.01')
        
        STEP_02 = """
            STEP 02 : Run gitStatus with IBFS_gitStatusParams=IBFS:/WFC/Repository/P459_S33046_Val_API 
        """
        self.Log.Message(STEP_02)
        git_status = gitStatus( IBIRS_gitStatusParams=IBIRS_path)
        
        STEP_02_EXPECTED = """
            STEP 02 Expected : Verify returncode="10000" and <item>, <status> tags values.
        """
        self.Log.Message(STEP_02_EXPECTED)
        file_xpath = git_status.XmlNode.rootObject_item_staus.format(expected_item_attrib[0]['path'])
        git_status.verify_returncode('02.01')
        git_status.XMLAssertions.assertAttributesListIn(git_status.XmlNode.rootObject_item, expected_item_attrib, '02.02', ['index'])
        git_status.XMLAssertions.assertAttributesEqual(file_xpath, expected_status_attrib, '02.03')