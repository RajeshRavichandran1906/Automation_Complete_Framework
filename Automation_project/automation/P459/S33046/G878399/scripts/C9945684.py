"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 13 May 2020
----------------------------------------------------"""

from common.webservices.git import gitRevisionContent
from common.webservices import BaseTestCase

class C9945684_TestClass(BaseTestCase):
    
    def test_C9945684(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path') + "/scm_vis1.fex"
        attributes = {'_jt': 'IBFSComponentContent', 'binary': 'false'}
        rootObject_text = "RU5HSU5FIElOVCBDQUNIRSBTRVQgT04KU0VUIFBBR0UtTlVNPU5PTEVBRApTRVQgU1FVRUVaRT1PTgotREVGQVVMVEggJldGX0hUTUxFTkNPREU9T047ClNFVCBIVE1MRU5DT0RFPSZXRl9IVE1MRU5DT0RFCgpTRVQgSFRNTENTUz1PTgotREVGQVVMVEggJldGX0VNUFRZUkVQT1JUPU9OOwpTRVQgRU1QVFlSRVBPUlQ9JldGX0VNUFRZUkVQT1JUCgpTRVQgRU1CRURIRUFESU5HPU9OClNFVCBHUkFQSERFRkFVTFQ9T0ZGClNFVCBDT01QT05FTlQ9VGFibGVDaGFydF8xClNFVCBBUlZFUlNJT049MgotREVGQVVMVEggJldGX1RJVExFPSdXZWJGT0NVUyBSZXBvcnQnOwpHUkFQSCBGSUxFIHJldGFpbF9zYW1wbGVzL3dmX3JldGFpbF90aW55Ci0qIENyZWF0ZWQgYnkgRGVzaWduZXIgZm9yIEdyYXBoClNVTSBXRl9SRVRBSUxfVElOWS5XRl9SRVRBSUxfU0FMRVMuQ09HU19VUwpCWSBXRl9SRVRBSUxfVElOWS5XRl9SRVRBSUxfVElNRV9TQUxFUy5USU1FX1lFQVIKT04gR1JBUEggUENIT0xEIEZPUk1BVCBKU0NIQVJUCk9OIEdSQVBIIFNFVCBWWkVSTyBPRkYKT04gR1JBUEggU0VUIEhBWElTIDEwMDguMApPTiBHUkFQSCBTRVQgVkFYSVMgNzY4LjAKT04gR1JBUEggU0VUIExPT0tHUkFQSCBCQVIKT04gR1JBUEggU0VUIEVNQkVESEVBRElORyBPTgpPTiBHUkFQSCBTRVQgQVVUT0ZJVCBPTgpPTiBHUkFQSCBTRVQgU1RZTEUgKgpJTkNMVURFPUlCRlM6L1dGQy9HbG9iYWwvVGhlbWVzL1N0YW5kYXJkL0RlZmF1bHQvdGhlbWUuc3R5LCQKVFlQRT1SRVBPUlQsIFRJVExFVEVYVD0nQ2hhcnQxJywgT1JJRU5UQVRJT049TEFORFNDQVBFLCBBUlJFUE9SVFNJWkU9RElNRU5TSU9OLCBBUkZJTFRFUl9UQVJHRVQ9JyonLCBBUkdSQVBIRU5HSU5FPUpTQ0hBUlQsICQKVFlQRT1EQVRBLCBDT0xVTU49TjEsIEJVQ0tFVD14LWF4aXMsICQKVFlQRT1EQVRBLCBDT0xVTU49TjIsIEJVQ0tFVD15LWF4aXMsICQKKkdSQVBIX1NDUklQVAoKKkdSQVBIX0pTX0ZJTkFMCiJibGFQcm9wZXJ0aWVzIjogewogICAgInNlcmllc0xheW91dCI6ICJzdGFja2VkIgp9LAoiYWdub3N0aWNTZXR0aW5ncyI6IHsKICAgICJjaGFydFR5cGVGdWxsTmFtZSI6ICJCYXJfU3RhY2tlZCIKfQoKKkVORApFTkRTVFlMRQpFTkQKCg=="
        
        STEP_01 = """
            STEP 01 : Run gitRevisionContent with IBIRS_path=IBFS:/WFC/Repository/P459_S33046_Val_API/scm_vis1.fex
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_revs_cont = gitRevisionContent(IBIRS_path)
         
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" and <rootObject _jt="IBFSComponentContent" binary="false">{binary value}</rootObject>
        """
        self.Log.Message(STEP_01_EXPECTED)
        git_revs_cont.verify_returncode('01.01')
        git_revs_cont.XMLAssertions.assertAttributesEqual(git_revs_cont.XmlNode.rootObject, attributes, '01.02')
        root_object = git_revs_cont._xml_parser_.root.find(git_revs_cont.XmlNode.rootObject)
        msg = "STEP 01.03 : Verify rootObject text"
        self.Assertions.assertEqual(rootObject_text, root_object.text.strip(), msg)