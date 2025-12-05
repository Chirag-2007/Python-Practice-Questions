'''Question 2 — map() Function
Problem Statement
Convert the prices of grocery items from dollars to rupees (1 USD = 83 INR).
Given item prices in dollars, print their rupee values.
Input Format
Space-separated decimal values (prices in USD).
Output Format
List of prices in INR.
Sample Test Case 1
Input:
1.5 2.0 3.0
Output:
[124.5, 166.0, 249.0]
Sample Test Case 2
Input:
0.5 1.2
Output:
[41.5, 99.6]'''

ruppe = list(map(float,input().split()))

dollar = list(map(lambda x: x*83,ruppe))
print(dollar)

