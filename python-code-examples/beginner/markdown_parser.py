import re
import csv
import os 
from os import listdir

def match_spec_header(md_str):
    pattern = re.compile(r'^(#{1}[ ]{1})[a-zA-Z0-9 ]*')
    matches = re.findall(pattern, md_str)
    mo = pattern.match(md_str)
    if (len(matches) == 1):
        print ("Specification Header Match found")
    else:
        print ("Specification Header Match NOT found")
    return len(matches)
        
def match_scenario_header(md_str):
    pattern = re.compile(r'^(#{2}[ ]{1})[a-zA-Z0-9 ]*')
    matches = re.findall(pattern, md_str)
    mo = pattern.match(md_str)
    if (len(matches) == 1):
        print ("Scenario Header Match found")
    else:
        print ("Scenario Header Match NOT found")
    return len(matches)
        
def match_step_line(md_str):
    pattern = re.compile(r'^(\*{1}[ ]{1})[a-zA-Z0-9 ]*')
    matches = re.findall(pattern, md_str)
    mo = pattern.match(md_str)
    if (len(matches) == 1):
        print ("Step Line Match found")
    else:
        print ("Step Line Match NOT found")
    return len(matches)

def write_test_header_csv_file():
    with open('test.csv', 'w',newline='') as csvfile:
        fieldnames = ['Specification', 'Scenario','Step']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)    
        writer.writeheader()
        
def write_test_in_csv_file(line,type):
    with open('test.csv', 'a',newline = '') as csvfile:
        fieldnames = ['Specification', 'Scenario','Step']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)    
        if type == 'SPEC':
            writer.writerow({'Specification': line, 'Scenario': '', 'Step':''})
        elif type == 'SCENARIO':
            writer.writerow({'Specification': '', 'Scenario': line, 'Step':''})
        elif type == 'STEP':
            writer.writerow({'Specification': '', 'Scenario': '', 'Step':line})    

print("--Extracting test details from markdown file--")

write_test_header_csv_file()

total_spec = 0
total_scenario = 0
total_step = 0
             
for file in os.listdir("md_files"):    
    with open("md_files" + '/' + file) as f:
        lines = f.readlines()
        for line in lines:
            print ("Line under Match:" + line)
            spec_count = match_spec_header(line)
            scenario_count = match_scenario_header(line)
            step_count = match_step_line(line)
            
            total_spec = spec_count + total_spec
            total_scenario = scenario_count + total_scenario
            total_step = step_count + total_step
            
            if(spec_count):
                write_test_in_csv_file(line, 'SPEC')
            elif(scenario_count):
                write_test_in_csv_file(line, 'SCENARIO')
            elif(step_count):
                write_test_in_csv_file(line, 'STEP')

print("--Extraction completed: Please refer test.csv file--")
print("Statistics of processed md files are:")
print("Total Specs:" + str(total_spec))
print("Total Scenarios:" + str(total_scenario))
print("Total Steps:" + str(total_step))

