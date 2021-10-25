"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 11 May 2020
----------------------------------------------------"""

from common.webservices.git import gitRevisionContent
from common.webservices import BaseTestCase

class C9945710_TestClass(BaseTestCase):
    
    def test_C9945710(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path') + "/scm_vis1.fex"
        attributes = {'_jt': 'IBFSComponentContent', 'binary': 'false'}
        rootObject_text = "VEFCTEUgRklMRSBDQVINClBSSU5UIENBUg0KRU5E"
        
        STEP_01 = """
            STEP 01 : Run gitRevisionContent with IBIRS_path=IBFS:/WFC/Repository/P459_S33046_Val_API/scm_vis1.fex
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_revs_cont = gitRevisionContent(IBIRS_path)
         
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" and <rootObject _jt="IBFSComponentContent" binary="false">VEFCTEUgRklMRSBDQVINClBSSU5UIENBUg0KRU5E</rootObject>
        """
        self.Log.Message(STEP_01_EXPECTED)
        git_revs_cont.verify_returncode('01.01')
        git_revs_cont.XMLAssertions.assertAttributesEqual(git_revs_cont.XmlNode.rootObject, attributes, '01.02')
        root_object = git_revs_cont._xml_parser_.root.find(git_revs_cont.XmlNode.rootObject)
        msg = "STEP 01.03 : Verify rootObject text"
        self.Assertions.assertEqual(rootObject_text, root_object.text.strip(), msg)