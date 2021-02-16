# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 09:42:44 2021
PyPoll_YangShi
@author: YangShi
"""
import os, csv

#input file path
election_csv=os.path.join('r','..','Resources','election_data.csv')
#output file path
output_txt=os.path.join("r","..", "analysis","election_analysis.txt")

votes=[]                #list of valid votes
candidate_percent=[]    #percentage of votes each candidate won
candidate_votes=[]      #total number of votes each candidate won

with open (election_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csvheader=next(csvreader)       #find the header
    for row in csvreader:
        votes.append(row[2])
total_votes=len(votes)              #total number of votes casted
candidates=list(set(votes))         #find the list of candidates
Num_of_candidate=len(candidates)

#output to the terminal
print("Election Results")
print("--------------------------------------------------")
print(f"Total Votes:  {total_votes}")
print("--------------------------------------------------")
#calcuate the election results and put into lists
for i in range(Num_of_candidate):
    candidate_votes.append(votes.count(candidates[i]))      #count the votes
    candidate_percent.append(round(candidate_votes[i]/total_votes*100,3))   #calculate percentage
    print(f"{candidates[i]} : {candidate_percent[i]}%  ({candidate_votes[i]})")
#find the winner
winner=candidates[candidate_votes.index(max(candidate_votes))]
print("--------------------------------------------------")
print(f"Winner:  {winner}")
print("--------------------------------------------------")

#output to text file
with open (output_txt,"w",newline='') as text:
    text.write("Election Results \n -------------------------------\n Total Votes: ")
    text.write(str(total_votes))
    text.write("\n ------------------------------- \n" )
    for i in range(Num_of_candidate):
        text.write(str(candidates[i]))
        text.write(":  ")
        text.write(str(candidate_percent[i]))
        text.write("%   (")
        text.write(str(candidate_votes[i]))
        text.write(")\n")
    text.write("------------------------------------\n Winner:   ")
    text.write(str(winner))
    text.write(" \n -----------------------------------------")

