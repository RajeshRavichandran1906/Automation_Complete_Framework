from testrail_utils import Testrail_Utils as tr_tr_client
import sys, os
from configparser import ConfigParser

def get_configparser_object(file_name_with_path):
        """
        This method used to read given file path using ConfigParser package and return object 
        """
        Error_Msg="[{0}] path not exists in file system".format(file_name_with_path)
        if os.path.exists(file_name_with_path) :
            parser=ConfigParser()
            parser.optionxform = str
            parser.read(file_name_with_path)
            return parser
        else :
            raise FileNotFoundError(Error_Msg)
    
def read_configparser_key_value(section, parser_key, parser_object=None, file_path=None):
    """
    This method used to read specific section key value
    """
    if parser_object == None:
        parser_obj=get_configparser_object(file_path)
        SECTION_MISSING_ERROR=" [{0}] section is not listed in [{1}] file ".format(section, file_path)
        SECTION_KEY_MISSING_ERROR=" [{0}] key is not listed under the [{1}] section in [{2}] file".format(parser_key, section, file_path)
    else:
        parser_obj=parser_object
        SECTION_MISSING_ERROR=" [{0}] section is not listed".format(section)
        SECTION_KEY_MISSING_ERROR=" [{0}] key is not listed under the [{1}] section".format(parser_key, section)
    if  parser_obj.has_section(section) :
        if parser_obj.has_option(section, parser_key):
            return parser_obj[section][parser_key]
        else :
            raise KeyError(SECTION_KEY_MISSING_ERROR)  
    else :
        raise KeyError(SECTION_MISSING_ERROR)

tr_client=tr_tr_client()
close_filter = {'is_completed': True}

input_file_name_with_path=os.getcwd() + '\\target\\project_milestone.data'
parser = get_configparser_object(input_file_name_with_path)
for section in parser.sections():
    project_id=section.replace('P', '').replace('p', '')
    milestone_name_list = list(map(lambda parser_key : parser[section][parser_key] , list(parser[section].keys())))
    for milestone_name in milestone_name_list:
        #Read all the milestones of the project
        milestone_detail=tr_client.get('get_milestones/' + project_id)
        for each_milestone in milestone_detail:
            #Search the required milestone by name.
            if each_milestone['name'] == milestone_name:
                #Get the milestone ID
                required_milestone_id = each_milestone['id']
                break
        #Get corresponding Plans according to milestone 
        plan_details = tr_client.get('get_plans/' + project_id + '&milestone_id=' + str(required_milestone_id))
        for each_plan in plan_details:
            #Get the plan ID
            required_plan_id = each_plan['id']
            #Close the plan
            try:
                close_plan_ret = tr_client.post('close_plan/' + str(required_plan_id), close_filter)
            except:
                msg='TestRail API returned HTTP 403 ("This operation is not allowed. The test plan is already completed.")'
                if msg in str(sys.exc_info()[1]):
                    print('The Requested Plan ' + str(required_plan_id) + ' is already completed.')
        #Close the milestone
        try:
            close_milestone_ret = tr_client.post('update_milestone/' + str(required_milestone_id), close_filter)
        except:
            print('Close milestone exception : ', sys.exc_info()[1])
