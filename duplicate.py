# Remove Duplicate from a List


list =[1, 5, 8, 9, 5, 3, 1, 7]

newlist =[]

for i in list:
    if list.count(i) == 1:
        newlist.append(i)

print(newlist)

# 
# Python function to accept a string and return total number of vowels



def countOfVowels(str):
    count =0
    for ch in str:
        if ch in "aeiouAEIOU":
            count +=1
    return count
    
countvowel = countOfVowels("Hello world!")
print(countvowel)          