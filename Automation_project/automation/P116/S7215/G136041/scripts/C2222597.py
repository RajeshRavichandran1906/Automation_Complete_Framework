'''
Created on April 19, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2222597
Description = AHTML: Add Sets to override cache format and mode. (ACT-362)
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea
from common.lib import utillity
import unittest, time, re



class C2222597_TestClass(BaseTestCase):

    def test_C2222597(self):
        
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        rsltobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """ Step 1: Execute the attached repro - ACT-362.fex
                    This repro runs 12 different combinations of the three control syntax commands: WEBVIEWER, ARCACHEMODE & ARCACHEFMT.
                    Expect to see just the HOLD output, no Active output.
                    All requests should give 18 records in Table and 10 lines of HTML output.
        """
        utillobj.active_run_fex_api_login("ACT-362.fex", "S7215", 'mrid', 'mrpass')
        time.sleep(5)
        parent_css='h5'
        rsltobj.wait_for_property(parent_css, 1)
        time.sleep(2)
        actual_data=driver.find_element_by_css_selector('h3').text.strip().split('\n')
        expected_data=['Your request did not return any output to display.', 'Possible causes:', '- No data rows matched the specified selection criteria.', '- Output was directed to a destination such as a file or printer.', '- An error occurred during the parsing or running of the request.']
        utillobj.asequal(actual_data, expected_data, 'Step 1: Expect to see just the HOLD output, no Active output.')
        time.sleep(2)
        actual_hold_data=driver.find_element_by_css_selector('h5').text.strip().replace('\n', '')
        hold_data = re.sub(' ', '', actual_hold_data)
        expected_hold_data = 'Cache=On,Arcachemode=Noextract,Arcachefmt=Binary********************************************************WEBVIEWERONARCACHEMODENOEXTRACTARCACHEFMTBINARY0NUMBEROFRECORDSINTABLE=18LINES=100HTMLFILESAVED...********************************************************Cache=On,Arcachemode=Noextract,Arcachefmt=Focus*******************************************************WEBVIEWERONARCACHEMODENOEXTRACTARCACHEFMTFOCUS0NUMBEROFRECORDSINTABLE=18LINES=100HTMLFILESAVED...******************************************************Cache=On,Arcachemode=Hold,Arcachefmt=Binary*****************************************************WEBVIEWERONARCACHEMODEHOLDARCACHEFMTBINARY0NUMBEROFRECORDSINTABLE=18LINES=100HTMLFILESAVED...******************************************************Cache=On,Arcachemode=Hold,Arcachefmt=Focus*****************************************************WEBVIEWERONARCACHEMODEHOLDARCACHEFMTFOCUS0NUMBEROFRECORDSINTABLE=18LINES=100HTMLFILESAVED...******************************************************Cache=On,Arcachemode=Nohold,Arcachefmt=Binary*****************************************************WEBVIEWERONARCACHEMODENOHOLDARCACHEFMTBINARY0NUMBEROFRECORDSINTABLE=18LINES=100HTMLFILESAVED...******************************************************Cache=On,Arcachemode=Nohold,Arcachefmt=Focus*****************************************************WEBVIEWERONARCACHEMODENOHOLDARCACHEFMTFOCUS0NUMBEROFRECORDSINTABLE=18LINES=100HTMLFILESAVED...**********************************************************Cache=Off,Arcachemode=Noextract,Arcachefmt=Binary*********************************************************WEBVIEWEROFFARCACHEMODENOEXTRACTARCACHEFMTBINARY0NUMBEROFRECORDSINTABLE=18LINES=100HTMLFILESAVED...**********************************************************Cache=Off,Arcachemode=Noextract,Arcachefmt=Focus*********************************************************WEBVIEWEROFFARCACHEMODENOEXTRACTARCACHEFMTFOCUS0NUMBEROFRECORDSINTABLE=18LINES=100HTMLFILESAVED...******************************************************Cache=Off,Arcachemode=Hold,Arcachemt=Binary*****************************************************WEBVIEWEROFFARCACHEMODEHOLDARCACHEFMTBINARY0NUMBEROFRECORDSINTABLE=18LINES=100HTMLFILESAVED...******************************************************Cache=Off,Arcachemode=Hold,Arcachemt=Focus*****************************************************WEBVIEWEROFFARCACHEMODEHOLDARCACHEFMTFOCUS0NUMBEROFRECORDSINTABLE=18LINES=100HTMLFILESAVED...*******************************************************Cache=Off,Arcachemode=Nohold,Arcachefmt=Binary******************************************************WEBVIEWEROFFARCACHEMODENOHOLDARCACHEFMTBINARY0NUMBEROFRECORDSINTABLE=18LINES=100HTMLFILESAVED...*******************************************************Cache=Off,Arcachemode=Nohold,Arcachefmt=Focus******************************************************WEBVIEWEROFFARCACHEMODENOHOLDARCACHEFMTFOCUS0NUMBEROFRECORDSINTABLE=18LINES=100HTMLFILESAVED...'
        utillobj.asequal(hold_data, expected_hold_data, 'Step 1.1: All requests should give 18 records in Table and 10 lines of HTML output.')
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()  