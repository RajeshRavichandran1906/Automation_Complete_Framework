'''
Created on Jul 8, 2019

@author: td13786
'''
import os

path = '\\\\bigrepos01\\bigscm\\TA\\qa'

files = []
for r, d, f in os.walk(path):
    for file in f:
        if 'cr_suite.bat' in file:
            files.append(os.path.join(r, file))


chrome_case_set = set()

for f in files:
    with open(f) as bat_file:
        for line in bat_file:
            if '/resultname  ' in line:
                case_substring = line[line.index('/resultname  ') + 14:] 
                space_index = case_substring.find('  ')
                case_substring = case_substring[:space_index -1]
                if case_substring[0].upper() == 'C' and case_substring[1].isdigit():
                    chrome_case_set.add(case_substring)
                    
print(chrome_case_set.__len__())

with open('TA_cases.txt', 'w') as f:         
    for case_id in sorted(chrome_case_set):    
        f.write(str(case_id) + '\n')
