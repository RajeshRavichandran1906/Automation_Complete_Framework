'''
Created on Sep 3, 2020

@author: ly14557
@description: Modify group level config files programmatically with preferred parameters (generally taken from a Jenkins job run).
'''
import requests
import sys
import os

EXIT_MESSAGE = "Exiting program."
if len(sys.argv) < 4:
    print("Lacking a required parameter. ", EXIT_MESSAGE)
    sys.exit(1)
    
file_path_base = sys.argv[1]
instance_type = sys.argv[2]
cloud_provider = sys.argv[3] 


class Config_Fixer:

    @staticmethod
    def get_env_port(res_dict):
        try:
            port = res_dict['httpport']
        except:
            port = -1
            print("Port not found. Leaving default port value from config file intact.")
        return port
    
    @staticmethod
    def get_cvs_config(prodid, confid, relid):
        res = Config_Fixer.cvs_confcgi_call(prodid, confid, relid)
        res_dict = Config_Fixer.create_cvs_response_dict(res.text)
        return res_dict
    
    @staticmethod
    def get_node_id(res_dict):
        node = res_dict['nodeid']
        if 'unxrh7' in node:
            node += '.ibi.com'
        return node
    
    @staticmethod    
    def create_cvs_response_dict(res_text):
        res_dict = {}
        res_list = res_text.strip().split('\n')
        for entry in res_list:
            res_dict[entry.split(' ')[0]] = entry.split(' ')[1]
        return res_dict
        
    @staticmethod
    def cvs_api_call(base_url, arg_dict=None):
        if arg_dict == None:
            url = base_url
        else:
            url = base_url + '?'
            first = True
            for key, value in arg_dict.items():
                argument = key + '=' + value
                if first != True:
                    argument = '&' + argument
                first = False
                url += argument     
        response = requests.get(url)
        if response == None:
            print("Did not receive a response back for: [" + url + "].")
            raise ValueError
        return response
    
    @staticmethod
    def cvs_confcgi_call(prodid, confid, relid):
        base_url = "http://cvs.ibi.com:3007/pkg_cgi/confCgi.pl"
        arg_dict = {
                        'prodid': prodid,
                        'confid': confid,
                        'relid': relid,
                    }
        return Config_Fixer.cvs_api_call(base_url, arg_dict)
      
    @staticmethod  
    def edit_config_init_value(file_path, edit_dict):
        '''
        Check what is already inside the file in case the key exists.
        '''
        with open(file_path, 'r') as f:
            text = f.read()
        conf_list = text.split('\n')
        
        for key, value in edit_dict.items():  
            fixed_line = key + ' ' + value 
            if "\n" + key in text:
                '''
                If the key is found, append the values to change.
                '''
                for i, entry in enumerate(conf_list):
                    if entry.split(' ')[0] == key:
                        conf_list[i] = fixed_line
                        print("Changed the config file's value for [" + key + "] to [" + value + "].")
            else:
                '''
                If the key is not found, add a new entry for the key and value.
                '''
                conf_list.append(fixed_line)
                
        new_text = '\n'.join(conf_list)
        with open(file_path, 'w') as f:
            f.write(new_text)
            
    @staticmethod
    def lookup_browser_key(browser):
        if "_" in browser:
            browser_code = browser.split('_', 1)[0]
        else:
            browser_code = browser
        browser_lookup_dict = {'cr': 'chrome', 'eg': 'edge', 'ff': 'firefox', 'ie': 'iexplore'}
        if browser_code.lower() in browser_lookup_dict.keys():
            browser_key = browser_lookup_dict[browser_code.lower()]
        else:
            print("Did not find browser to change.")
            raise ValueError
        return browser_key
        
if __name__ == '__main__':
    #res_dict = Config_Fixer.get_cvs_config(prodid, confid, relid)
    #port = Config_Fixer.get_env_port(res_dict)
    #node = Config_Fixer.get_node_id(res_dict)
    if instance_type != 'none':
        file_path = os.getcwd() + "\\qa\\selenium\\" + file_path_base + '\\config.init'
        if cloud_provider != 'none':
            edit_dict = {'instance_type': instance_type, 'cloud_provider': cloud_provider }
        else:
            edit_dict = {'instance_type': instance_type}
        #edit_dict = { 'node': node, 'port': port, 'browser': Config_Fixer.lookup_browser_key(browser), 'lang_code': lang_code } if port != -1 else {'node': node, 'browser': Config_Fixer.lookup_browser_key(browser), 'lang_code': lang_code }
        Config_Fixer.edit_config_init_value(file_path, edit_dict)
