# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:50:25 2021
PyParagraph_YangShi
@author: YangShi
"""
import os,re
txt_input1=os.path.join("r","..","raw_data","paragraph_1.txt")
txt_input2=os.path.join("r","..","raw_data","paragraph_2.txt")

def split_count (txt_input):     #function to analyse the paragraph
    with open(txt_input,"r",encoding="utf-8") as text:  #open text file
        paragraph_sc=text.read().replace("\n", " ")                   #read text content, replace \n with space
        letter_count_list=[]
        paragraph_sentence=re.split("(?<=[.!?]) +", paragraph_sc)   #split a paragragh to sentences
        sentence_count=len(paragraph_sentence)           #count sentence
        paragraph_word=paragraph_sc.split(" ")       #count words in a paragraph
        for i in range(len(paragraph_word)):
                paragraph_letter=list(paragraph_word[i])    #split words into letters
                letter_count_list.append(len(paragraph_letter))           #store the number of the letters into a list
        word_count=len(paragraph_word)                   #find the word count
        average_letter_count=round(sum(letter_count_list)/len(letter_count_list),1)    #calculate the average letter count
        average_sentence_length=round(word_count/sentence_count,1)              #calculate the average sentence length
        print("Paragraph Analysis")                                         #output title
        print("-----------------------------------------")              
        print(f"Approximate Word Count: {word_count}")                        #output word count
        print(f"Approximate Sentence Count: {sentence_count}")                #output sentence count
        print(f"Average Letter Count: {average_letter_count}")              #output average letter count
        print(f"Average Sentence Length: {average_sentence_length}")        #output average sentence length

split_count(txt_input1)
split_count(txt_input2)