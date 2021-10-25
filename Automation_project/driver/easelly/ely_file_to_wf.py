'''
@author: Lawrence
@description: This uses webservices to upload an ely file to WebFocus.
'''

import base64
import xml.etree.ElementTree as ET
import requests
import sys

protocol_arg = sys.argv[1]
host_arg = sys.argv[2]
port_arg = sys.argv[3]
userid_arg = sys.argv[4]
password_arg = sys.argv[5]
local_file_path = sys.argv[6]
folder_arg = sys.argv[7]
fex_arg = sys.argv[8] 
report_title_arg = sys.argv[9]
print(local_file_path)
        
class Session(requests.Session):
    """Extend the features of Requests' Session object."""
    def __init__(self):
        'log in to WF'
        login = self.mr_sign_on(protocol=protocol_arg,
                           host=host_arg,
                           port=port_arg,
                           userid=userid_arg,
                           password=password_arg)

        print(login.text)

    def save_ibi_csrf_token(self, xml):
        """Save IBI_CSRF_Token_Value from response to sign-on request."""

        tree = ET.fromstring(xml)
        token = tree.find('properties/entry[@key="IBI_CSRF_Token_Value"]')

        token_value = token.attrib['value']
        self.IBIWF_SES_AUTH_TOKEN = token_value


    def mr_sign_on(self,
                   protocol='http',
                   host='localhost',
                   port='8080',
                   userid='admin',
                   password='admin'):
        """WebFOCUS Repository: Authenticating WebFOCUS Sign-On Requests."""

        self.protocol = protocol
        self.host = host
        self.port = port

        method = 'post'
        data = {
            'IBIRS_action': 'signOn',
            'IBIRS_userName': userid,
            'IBIRS_password': password,
        }

        url = '{}://{}:{}/ibi_apps/rs/ibfs'.format(self.protocol,
                                                   self.host,
                                                   self.port) 

        response = self.request(method=method, url=url, data=data)
        self.save_ibi_csrf_token(response.content)
        return response
    
    
    def mr_upload_report(self, folder_name='', fex_name='', report_title='', local_file_path=''):
        """WebFOCUS Repository: Uploading a WebFOCUS Report.
        """

        method = 'post'

        with open(local_file_path, 'rb') as f:
            content = f.read()
        content_base64 = base64.b64encode(content)
        content_string = content_base64.decode("utf-8")
  
        #=======================================================================
        # objects = """<rootObject _jt="IBFSMRObject"
        #                description="{0}"
        #                type="HTMLFile">
        #                <content _jt="IBFSByteContent"
        #                  char_set="Cp1252">{1}</content>
        #              </rootObject>""".format(report_title,content_base64)
        #=======================================================================
                     
        fex_file = str(fex_name.split('.')[:-1])
        objects = """<rootObject _jt="IBFSMRObject"
                  description= """+ fex_file + """ type="FileFex">
                  <content _jt="IBFSByteContent" charset="Cp1252">{0}</content>
                </rootObject> """.format(content_string)


        data = {'IBIRS_action': 'put'
                ,'IBIRS_object': objects,
        }
        url = '{}://{}:{}/ibi_apps/rs/ibfs/WFC/Repository/{}/{}'.format(
                                                                 self.protocol,
                                                                 self.host,
                                                                 self.port,
                                                                 folder_name,
                                                                 fex_name)

        # add the CSRF token value to the body (data) of the request
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        return self.request(method=method, url=url, data=data)
    
    def get_file(self, folder_name='', fex_name='', path=''):
        
        method = 'get'
        url = '{}://{}:{}/ibi_apps/rs/ibfs'.format(self.protocol,
                                                   self.host,
                                                   self.port)
        params={"IBIRS_path": path, "IBIRS_action": "get", "IBIRS_args": "__null"}
        

        response = self.request(method=method, url=url, params=params)
        return response
        
    def validate_xml(self, xml, fex_name):
        
        xml_msg = "The xml provided does not contain the file at the path requested. Exiting program with an error"
        tree = ET.fromstring(xml)
        returndesc_token = tree.attrib['returndesc']
        returncode_token = tree.attrib['returncode']

        fullpath = ''
        dict = tree[1].attrib
        fullpath = dict['fullPath']

        
        if fullpath.find(fex_name) == -1 or returncode_token != "10000" or returndesc_token != "SUCCESS":
            print(xml_msg)
            sys.exit(1)
    

#  --[ main ]------------------------------------------------------------------
if __name__ == '__main__':

    session = Session()
    
    'upload a file'
    #local_file_path=r"\\ibirisc2\bipgqashare\easel_ly\latest_templates\UnitedWay.ely"
    upload = session.mr_upload_report(folder_name=folder_arg, fex_name=fex_arg, report_title=report_title_arg, local_file_path=local_file_path)
    result = session.get_file(folder_name=folder_arg, fex_name=fex_arg, path="/WFC/Repository/" + folder_arg + "/" + fex_arg)
    print(result.content)
    session.validate_xml(result.content, fex_name=fex_arg)
    #print(upload.text)
    #http://unxrh7:19064/ibi_apps/ia?is508=false&item=IBFS%3A%2FWFC%2FRepository%2FP413_S18040%2FELY_Templates&tool=document&layoutTemplate=IBFS:/WFC/Repository/P413_S18040/ELY_Templates/United_Way.ely

    
    
    

        