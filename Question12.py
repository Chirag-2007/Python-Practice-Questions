# Taking input of 5 students and print the list and also print the list items

name_list = []
for i in range(1,6):
    name = input("Enter name: ")
    name_list.append(name)
print("List of students is: ",name_list)

for i in name_list:
    print(i)


