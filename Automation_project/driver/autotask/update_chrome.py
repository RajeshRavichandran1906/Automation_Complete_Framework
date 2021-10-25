import os
import sys
import shutil
import argparse
import win32wnet
import pywintypes
from win32com.client import Dispatch
from configparser import ConfigParser

path = os.path.abspath(os.path.dirname(__file__))

class UpdateChrome:
    
    def __init__(self, version):
        
        self.version = str(version)
        
    def update(self):
        """
        Description: 
        """
        unsuccessful_machine = []
        root_path = "\\\\{0}\\c$"
        machines = self._get_machines()
        shared_cr_application_path = self._get_application_path()
        for machine_name, credential in machines.items():
            print("\n-------------------------------------- [{0}] --------------------------------------\n".format(machine_name))
            self._write_info_log("Connecting to [{0}] machine.".format(machine_name))
            machine_c_path = root_path.format(machine_name)
            user_name = credential[0]
            password = credential[1]
            chrome_application_path = machine_c_path + "\\Program Files (x86)\\Google\\Chrome\\Application"
            try:
                self._connect_shared_location(chrome_application_path, user_name, password)
                msg = "[{0}] machine is connected. User Name: {1}, Password: {2}".format(machine_name, user_name, password)
                self._write_info_log(msg)
            except Exception as error:
                self._write_error_log(error)
                msg = "Unable to connect [{0}] machine. Please check machine name and credential. User Name: {1}, Password: {2}".format(machine_name, user_name, password)
                self._write_error_log(msg)
                unsuccessful_machine.append(machine_name)
                continue
            if os.path.exists(chrome_application_path):
                self._write_info_log("Checking chrome version...")
                version = self._get_version(chrome_application_path)
                if version == self.version:
                    msg = "Already required chrome version {0} updated".format(self.version)
                    self._write_info_log(msg)
                else:
                    msg = "Required chrome version {0} not updated".format(self.version)
                    self._write_info_log(msg)
                    try:
                        self._write_info_log("Deleting chrome {0} version application folder".format(version))
                        shutil.rmtree(chrome_application_path)
                    except Exception as error:
                        self._write_error_log(error)
                        self._write_error_log("Unable to delete chrome application folder.")
                        unsuccessful_machine.append(machine_name)
                        continue
                    try:
                        self._write_info_log("Coping chrome {0} version application folder from shared location".format(self.version))
                        shutil.copytree(shared_cr_application_path, chrome_application_path)
                        cr_version = self._get_version(chrome_application_path)
                        if cr_version == self.version:
                            self._write_info_log("Updated chrome {0} version successfully.".format(cr_version))
                        else:
                            self._write_error_log("Unable update chrome {} version".format(self.version))
                    except Exception as error:
                        self._write_error_log(error)
                        self._write_error_log("Unable to copy and update the chrome {}".format(self.version))
                        unsuccessful_machine.append(machine_name)
                        continue
            else:
                msg = "Chrome browser application not found. Pleae check whether chrome browser installed in [{0}] machine.".format(machine_name)
                self._write_error_log(msg)
                
        print("\n---------------------------------------------------------------------------------\n")
        if unsuccessful_machine != []:
            self._write_error_log("Unable to update chrome version {0} for following machine".format(self.version))
            print("\n".join(unsuccessful_machine))
            sys.exit(-1)
            
    def _get_application_path(self):
        """
        Description: Get given chrome version applicatio folder path from \\bipgsrv\Selenium_Automation_Project\Browser\\chrome
        """
        user_name = "IBI\qaauto"
        password = "Automate1"
        shared_location_path = "\\\\bipgsrv\\Selenium_Automation_Project\\Browser\\chrome"
        self._write_info_log("Connecting to [{0}] location.".format(shared_location_path))
        self._connect_shared_location(shared_location_path, user_name, password)
        msg = "[{0}] shared location connected. User Name: {1}, Password: {2}".format(shared_location_path, user_name, password)
        self._write_info_log(msg)
        self._write_info_log("Checking whether chrome {0} version application folder available in [{1}] location".format(self.version, shared_location_path))
        cr_application_path = os.path.join(shared_location_path, self.version, "Application")
        if os.path.exists(cr_application_path):
            version = self._get_version(cr_application_path)
            if version == self.version:
                return cr_application_path
            elif version == None:
                    raise RuntimeError("Unable to find the chrome version. Please check the chrome application folder")
            else:
                msg = "[{0}] location contains chrome {1} version. Required version is {2}.".format(cr_application_path, version, self.version)
                raise RuntimeError(msg)
        else:
            msg = "Chrome [{0}] version application folder not available in [{1}] location".format(self.version, shared_location_path)
            self._write_error_log(msg)
            raise FileNotFoundError(msg)
    
    def _connect_shared_location(self, path, username, password):
        """
        Description : Connection to shared path
        """
        try:
            win32wnet.WNetAddConnection2(0, None, path, None, username, password)
        except pywintypes.error as error:
            if error[0] == 1219:
                win32wnet.WNetCancelConnection2(path, 0, 0)
                return self._connect_shared_location(path, username, password)
            else:
                raise error
        except Exception as error:
            raise error
        
    def _get_version(self, application_path):
        """
        Descriprion: Return chrome version.
        """
        parser = Dispatch("Scripting.FileSystemObject")
        try:
            version = parser.GetFileVersion(os.path.join(application_path, "chrome.exe")).split(".")[0]
            self._write_info_log("Chrome version {}".format(version))
            return version
        except:
            self._write_error_log("Unable to find the chrome version.")
            return None
        
    def _write_info_log(self, msg): print("[INFO]  : " + str(msg))
        
    def _write_error_log(self, msg): print("[ERROR] : " + str(msg))
        
    def _get_machines(self):
        """
        Description : Return the machines and credential as list
        """
        machines_config_file = os.path.join(path, "runnerbox.config")
        if os.path.exists(machines_config_file):
            parser = ConfigParser()
            parser.read(machines_config_file)
            machines_section = parser['machines']
            machines = dict()
            for machine, credential in list(machines_section.items()):
                user_pass = credential.strip().split(":")
                if len(user_pass) == 2:
                    machines[machine] = (user_pass[0], user_pass[1])
            return machines
        else:
            msg = "[{0}] file not found.".format(machines_config_file)
            self._write_error_log(msg)
            raise FileNotFoundError(msg)

print("\n------------------------------------------- Logs ------------------------------------------\n")
arg_parse = argparse.ArgumentParser()
arg_parse.add_argument("-version", help="Chrome version to update. Exp : 84", required=True, type=str)
args = arg_parse.parse_args()
UpdateChrome(args.version).update()