# It has at least 6 characters and at most 20 characters.
# It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It does not contain three repeating characters in a row

password = "Passsword8"

if 6 <= len(password) <= 20:
    if any(char.islower() for char in password):
        if any(char.isupper() for char in password):
            if any(char.isdigit() for char in password):
                if not any(password[i] == password[i+1] == password[i+2] for i in range(len(password)-2)):
                    print("Valid Password")
                    exit()
print("Not Valid Password")



