# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:35:14 2021
PyBoss_YangShi
@author: YangShi
"""
import os, csv,datetime

employee_csv=os.path.join("r","..","employee_data.csv")
output_csv=os.path.join("r","..","formatted_data.csv")
emp_id=[]
first_name=[]
last_name=[]
dob=[]
ssn=[]
state=[]
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open (employee_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")    #read csv file
    csvheader=next(csvreader)                       #find header
    for row in csvreader:
        emp_id.append(row[0])
        x=row[1].split(' ')
        first_name.append(x[0])
        last_name.append(x[1])
        dob.append(datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y'))
        y=row[3].split("-")
        ssn.append("***-**-" + y[2])
        state.append(us_state_abbrev[row[4]])

with open(output_csv,"w",newline="") as csvfile:
    #initialize csv.writer
    csvwriter=csv.writer(csvfile,delimiter=",")
    #writer column headers
    csvwriter.writerow(["Employee ID","First Name","Last Name","DOB","SSN","State"])
    for i in range(len(emp_id)):
        csvwriter.writerow([emp_id[i], first_name[i],last_name[i],dob[i],ssn[i], state[i]])

