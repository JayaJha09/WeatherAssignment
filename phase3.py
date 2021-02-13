import json
import phaseA
import phase2
import itertools

file = open('userinput.json', "r")
userdata = json.loads(file.read())
variance_tmp = userdata['Variance']
for (city, phase1temp, phase2temp) in zip(userdata['City'], phaseA.city_temp, phase2.list_temp):
    if variance_tmp >= abs((int(phase1temp)) - (int(phase2temp))):
        print("SUCCESS!! temperature is in specified range for city : %s" % city)
    else:
        print("matcher exception for city : %s" % city)
