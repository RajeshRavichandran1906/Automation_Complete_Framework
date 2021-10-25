import re
import os

class Utils:
    
    @staticmethod
    def get_config_file_key_value(key):
        """
        Description : Read the value of given key from config.init file.
        Raise error if key not found in the config.init file
        :param - key : name of the key to read the value
        :usage - get_config_file_key_value('node')
        """
        config_file = 'config.init'
        if os.path.exists(config_file) != True:
            error_msg = "[{0}] File not found in current working directory.".format(config_file)
            raise FileNotFoundError(error_msg)
        key_values = {}
        with open(config_file, "r") as fileObj:
            line = fileObj.readline()
            while line:
                match = re.match(r'(\S*)\s(.*)', line.lstrip())
                if match:
                    keyName = match.group(1).strip()
                    value = match.group(2).strip()
                    key_values[keyName] = value
                line = fileObj.readline()
        if key not in key_values:
            error_msg = "[{0}] Key not defined in [{1}] file".format(key, config_file)
            raise KeyError(error_msg)
        return key_values[key]
    
    @staticmethod
    def get_webfocus_url():
        """
        Description : Return the webfocus absolute url.
        """
        note_name = Utils.get_config_file_key_value('nodeid')
        port_number = Utils.get_config_file_key_value('httpport')
        context = Utils.get_config_file_key_value('wfcontext')
        url = "http://{0}:{1}{2}/".format(note_name, port_number, context)
        return url