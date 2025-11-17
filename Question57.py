'''Problem Statement2 : Greatest Common divisor of two integers 
Kirti has been asked to give a sentence in the form of a string as a function parameter. The task 
is to print the sentence such that each word in the sentence is reversed. 
Input Format: 
The only line of input contains a string that represents the sentence given by Kirti. 
Output Format: 
The only line of output prints the sentence such that each word in the sentence is reversed. The  
position of the word should be same. 
Constraints: 
0 <= N <= 100 
Where N is the length of the input string. 
Sample Input: 
Welcome To Chitkara 
Sample Output: 
emocleW oT araktihC'''


def rev_sentence(n):
    reverse_arr = []
    for reverse in n:
        reverse_each = reverse[::-1]
        reverse_arr.append(reverse_each)
    for i in reverse_arr:
        print(i,end=" ")

n = input()
alpha_list = n.split()
rev_sentence(alpha_list)