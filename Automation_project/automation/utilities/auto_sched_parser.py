"""
{
"validation":{
    "chrome":{
        "odd": {
            "sunday":{
                "698":{
                    "plans": ["R123", "R234", "R345"],
                    "executed":"true"
                }
            },
            "monday":{},
            "tuesday":{},
            "wednesday":{},
            "thursday":{},
            "friday":{},
            "saturday":{},    
        },
        "even":{}
    },
    "firefox":{},
    "edge":{},
    "ie":{}
    }, 
"regression":{}
    
}
"""



import os
import csv
import json


class Auto_Sched():
    
    def __init__(self, rel):
        self.rel = str(rel)
    
        
    '''pass in fully qualified path to csv directory, return the name of the csv file based on the release value'''
    def get_csv_by_rel(self, location):
        csv_name = ''
        for name in os.listdir(location):
            if os.path.isfile(os.path.join(location, name)) and self.rel in name and '.csv' in name:
                csv_name = name
        if csv_name != '' and os.path.exists(location):
            return os.path.join(location, csv_name)
        return ''
    
    
    '''
    utility function to create a dictionary branch
    needs to add data validation logic - to verify input data is correct    
    '''
    def fill_dict_branch(self, result_dict, plan_type, week, day, brs, plan, conf):
        if brs not in result_dict[plan_type]:
            result_dict[plan_type][brs] = {"odd":{}, "even":{}}
        if day not in result_dict[plan_type][brs][week]:
            result_dict[plan_type][brs][week][day] = {}
        if conf not in result_dict[plan_type][brs][week][day]:
            result_dict[plan_type][brs][week][day][conf] = {}
        if "executed" not in result_dict[plan_type][brs][week][day][conf]:
            result_dict[plan_type][brs][week][day][conf]["executed"] = "false"
        if "plans" not in result_dict[plan_type][brs][week][day][conf]:
            result_dict[plan_type][brs][week][day][conf]["plans"] = []
        result_dict[plan_type][brs][week][day][conf]["plans"].append(plan)
        return
    
    
    '''pass in fully qualified path to a csv file, transform it into a dictionary'''
    def generate_dict(self, csv_path, type_list):
        result_dict = {}        
        csv_full_path = str(csv_path)
        
        if os.path.isfile(csv_full_path):              
            plan_type = ''
            with open(csv_full_path) as csv_file:
                #only initialize result_dict when csv can be opened
                for automation_type in type_list:
                    result_dict[automation_type] = {}
                    
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    if row[0].lower().strip() in type_list:
                        plan_type = row[0].lower().strip()
        
                    if row[1] != '' and plan_type != '':
                        day = row[4].lower().strip()
                        brs_1 = row[5].lower().strip()
                        plan_1 = row[6].upper().strip()
                        if plan_1 != '':
                            conf_1 = row[7].split(':')[-1].strip()[-3:]
                            if conf_1.isdigit() and plan_1[0] == 'R' and brs_1 != 'n/a':
                                self.fill_dict_branch(result_dict, plan_type, 'odd', day, brs_1, plan_1, conf_1)
                        brs_2 = row[8].lower().strip()
                        plan_2 = row[9].upper().strip()
                        if plan_2 != '':    
                            conf_2 = row[10].split(':')[-1].strip()[-3:]
                            if conf_2.isdigit() and plan_2[0] == 'R' and brs_2 != 'n/a':
                                self.fill_dict_branch(result_dict, plan_type, 'even', day, brs_2, plan_2, conf_2)
                       
        return result_dict
    
    
if __name__ == '__main__':
    rel = '8207'
    pkg = "wf093019a"
    csv_dir = "\\\\qaops\\qaops\\schedules\\csv"
    data_folder = os.path.join(csv_dir, 'data\\')
    
    parser = Auto_Sched(rel)
    file = parser.get_csv_by_rel(csv_dir)
    print(file)
    sched_dict = parser.generate_dict(file, ['validation', 'regression', 'testcomplete'])    
    print(sched_dict)
    
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        
    with open(os.path.join(data_folder, rel + '.json'), 'w+') as dict_writer:
        dict_writer.write(json.dumps(sched_dict))
        print("done")
