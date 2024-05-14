String = "oolloo0"
charrr = ''
int =''

duplicate = []

for char in String:
    if not char.isnumeric():
        charrr += char
    if char.isnumeric():
        int += char

    
for i in String:
    if String.count(i) > 1 and i not in duplicate:
        duplicate.append(i)

if String == String[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


print(String.replace('V2', 'H3'))
print(String)


print(String.count("n"))
print(duplicate)
print(charrr)
print(int)



