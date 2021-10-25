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
'''Parameters: 1. Template plan ID, 2. Name of the new plan, 3. Target Milestone'''
input_file_name_with_path=os.getcwd() + '\\target\\plan_detail.data'
parser = get_configparser_object(input_file_name_with_path)
for section in parser.sections():
    plan_id=read_configparser_key_value(section, 'existing_plan_id', parser_object=parser)
    new_plan_name=read_configparser_key_value(section, 'new_plan_name', parser_object=parser)
    milestone_name=read_configparser_key_value(section, 'milestone_name', parser_object=parser)
 
     
    '''Step 1. Read High level suite/run etc informations from template'''
    
    high_level_plan_detail=tr_client.get('get_plan/' + plan_id) #Getting plan from a particular plan.
    old_plan_name=high_level_plan_detail['name']
    old_description=high_level_plan_detail['description']
    project_id=high_level_plan_detail['project_id']
     
    milestone_dict={}
    milestones=tr_client.get('get_milestones/' + str(project_id))
    for milestone in milestones:
        milestone_dict[milestone['name'].lower()] = milestone['id']
    milestone_id = milestone_dict[milestone_name.lower()]    
     
    new_plan_dict = {"name":new_plan_name, "description":old_description, "milestone_id":milestone_id}
    new_plan_ret = tr_client.post('add_plan/' + str(project_id), new_plan_dict)
    current_plan_id=new_plan_ret["id"]    
    for entry in high_level_plan_detail['entries']:
        run_id=entry['runs'][0]['id']
        description=entry['runs'][0]['name']
        suite_id=entry['runs'][0]['suite_id']
        plan_id=entry['runs'][0]['plan_id']
        '''Step 2. Read the test case IDs from each run ID within the plan'''
        case_ids=[]
        for runid in tr_client.get('get_tests/' + str(run_id)):
            case_ids.append(runid['case_id'])
        create_run={'suite_id' : suite_id, 'description' : description, 'include_all': False, 'case_ids' : case_ids}
        tr_client.post('add_plan_entry/' + str(current_plan_id), create_run)
     
    '''Step 3. Create a Test Plan'''
 
    print("The New Plan is : ", current_plan_id)


