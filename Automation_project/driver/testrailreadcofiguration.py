import re, os
from configparser import ConfigParser
#import testrail as tr
from testrail import testrail as tr

class TestRailReadConfiguration():
    
    def __init__(self):
        self.client = self.get_testrail_object()
        self.result_fields=self.client.send_get('get_result_fields')
        self.case_fields=self.client.send_get('get_case_fields')
    
    def getFieldsDictionary(self, fields_str):
        theDictionary = {}
        for item in fields_str.split('\n'):
                pair = item.split(',')
                if len(pair) > 1:
                    if bool(re.match('.*:.*', pair[1])):
                        reobj=re.match('(.*):.*', pair[1])
                        theDictionary.update({reobj.group(1): pair[0].strip()})
                    else:
                        theDictionary.update({re.sub(' ','', pair[1]): pair[0].strip()})
        return theDictionary
    
    def get_testrail_object(self):
        conf_file=os.getcwd() + "\\qa\\selenium\\driver\\config.ini"
        print("current path: ", os.getcwd())
        print("conf_file path: ", conf_file)
        parser = ConfigParser()
        parser.read(conf_file)
        section='testrail'
        client = tr.APIClient(parser[section]['tr_link'])
        client.user = parser[section]['tr_uid']
        client.password = parser[section]['tr_pwd']
        return(client)


    def get_result_dictionary(self, key):
        for i in range(len(self.result_fields)):
            if self.result_fields[i]['name'] == key:
                return(self.getFieldsDictionary(self.result_fields[i]['configs'][0]['options']['items']))
