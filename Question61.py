'''Raman received a mail from his friend Ravi, for filling the slam book. While filling the answer to a 
particular question, he inserted special characters at a particular index of every word he entered. Now he 
wants his friend to retrieve that character from each word and concatenate them in order to know the answer 
to his question. Write a program to help Ravi in finding out the answer to that question. 
Input Format: 
First Line :  Enter the String        
Second Line: Index Value           
word                      
Output Format: 
# Input the String               
# If index value is 2 then it is used to extract 3rd character from each 
String concatenation of characters at given index value of each word 
Sample Input: 
keep exploring 
2 
Sample Output: 
ep '''

sentence = input()
index = int(input())
sentence_arr = sentence.split()
word_arr = []

for word in sentence_arr:
    index_str = word[index]
    word_arr.append(index_str)

word = ''.join(word_arr)
print(word)
