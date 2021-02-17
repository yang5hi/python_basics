# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:50:25 2021
PyParagraph_YangShi
@author: YangShi
Your task is to create a Python script to automate the analysis of any such passage using these metrics. 
Your script will need to do the following:
* Import a text file filled with a paragraph of your choosing.
* Assess the passage for each of the following:
  * Approximate word count
  * Approximate sentence count
  * Approximate letter count (per word)
  * Average sentence length (in words)
```output
Paragraph Analysis on paragraph_0.txt
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.6
Average Sentence Length: 24.0
```
* **Special Hint:** You may find this code snippet helpful when determining sentence length 
(look into [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) if interested in learning more):
"""
import os,re
txt_input1=os.path.join("r","..","raw_data","paragraph_1.txt")
txt_input2=os.path.join("r","..","raw_data","paragraph_2.txt")

def split_count (paragraph_sc):     #function to split the word and count the letters
    word_num=0
    letter_num=0
    for i in range(len(paragraph_sc)):
        paragraph_sentence=re.split("(?<=[.!?]) +", paragraph_1[i])   #split a paragragh to sentences
        paragraph_word=paragraph_sc[i].split(" ")       #count words in a paragraph
        for j in range(len(paragraph_word)):
            paragraph_letter=list(paragraph_word[j])
            letter_num+=len(paragraph_letter)
        word_num+=len(paragraph_word)
    sentence_num=len(paragraph_sentence)
    average_letter_count=round((letter_num-sentence_num)/word_num,1)
    average_sentence_length=round(word_num/sentence_num,1)
    print("Paragraph Analysis")
    print("-----------------------------------------")
    print(f"Approximate Word Count: {word_num}")
    print(f"Approximate Sentence Count: {sentence_num}")
    print(f"Average Letter Count: {average_letter_count}")
    print(f"Average Sentence Length: {average_sentence_length}")

with open(txt_input1,"r",encoding="utf-8") as text1:
    paragraph_1=text1.readlines()
    split_count(paragraph_1)
    
with open(txt_input2,"r") as text2:
    
'''

#hot_days = [temperature for temperature in july_temperatures if temperature > 90]

#2
When Jackie Chan saw an Oscar at Sylvester Stallone's house 23 years ago, he said that was the moment he decided he wanted one.

On Saturday at the annual Governors Awards, the Chinese actor and martial arts star finally received his little gold statuette, an honorary Oscar for his decades of work in film.

"After 56 years in the film industry, making more than 200 films, after so many bones, finally," Chan, 62, quipped at the star-studded gala dinner while holding his Oscar.

The actor recalled watching the ceremony with his parents and his father always asking him why he didn't have Hollywood's top accolade despite having made so many movies.

He praised his hometown Hong Kong for making him "proud to be Chinese," and thanked his fans, saying they were the reason "I continue to make movies, jumping through windows, kicking and punching, breaking my bones."

The actor was introduced by his "Rush Hour" co-star Chris Tucker, actress Michelle Yeoh and Tom Hanks, who referred to him as "Jackie 'Chantastic' Chan."

Hanks said it was especially gratifying to be able to acknowledge Chan's work because martial arts and action comedy films were two genres often overlooked during awards season.

The Academy of Motion Pictures Arts and Sciences, hosts of the annual ceremony, also bestowed honorary Oscars on British film editor Anne V. Coates, casting director Lynn Stalmaster and prolific documentarian Frederick Wiseman.

The evening was attended by Hollywood's elite, including Denzel Washington, Lupita Nyong'o, Nicole Kidman, Emma Stone, Ryan Reynolds, Amy Adams and Dev Patel.

Stalmaster, 88, credited with securing career-defining roles for actors such as Jeff Bridges, Andy Garcia, Christopher Reeve and John Travolta, is the first casting director to receive an Oscar.
'''